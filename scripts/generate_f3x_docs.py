import textwrap
import xml.etree.ElementTree as ET
from collections import defaultdict
from pathlib import Path
from typing import Iterable, List

REPO_ROOT = Path(__file__).resolve().parent.parent
CHEATS_DIR = REPO_ROOT / "cheats"

# The F3x platform covers F30-F36 (3/4 Series) and the closely-related F80-F83 M3/M4 models.
F3X_KEYWORDS = [
    "F30",
    "F31",
    "F32",
    "F33",
    "F34",
    "F35",
    "F36",
    "F80",
    "F82",
    "F83",
    "F03X",
    "F3X",
]

# Chassis that share most modules with the F3x platform (F2x 1/2 Series, etc.).
POTENTIAL_KEYWORDS = [
    "F20",
    "F21",
    "F22",
    "F23",
    "F2",
    "F87",
    "F020",
    "F021",
    "F022",
    "F023",
    "F024",
    "F025",
    "F026",
]

MarkdownBlock = List[str]


def iter_xml_files() -> Iterable[Path]:
    for path in sorted(CHEATS_DIR.glob("*.xml")):
        if path.name.startswith("xml-documentation"):
            # Skip the generated documentation file, should it be present as XML.
            continue
        yield path


def tokenize_series(series: str | None) -> List[str]:
    if not series:
        return []
    series = series.replace("/", ",")
    return [token.strip().upper() for token in series.split(",") if token.strip()]


def classify_entry(code_series: str | None, cafd_series: str | None) -> str | None:
    code_tokens = tokenize_series(code_series)
    cafd_tokens = tokenize_series(cafd_series)
    combined_tokens = code_tokens or cafd_tokens

    if any(any(keyword in token for keyword in F3X_KEYWORDS) for token in combined_tokens):
        return "confirmed"

    all_tokens = code_tokens + cafd_tokens
    if any(any(keyword in token for keyword in POTENTIAL_KEYWORDS) for token in all_tokens):
        return "potential"

    return None


def describe_function(group_id: str | None, function: ET.Element) -> str:
    parts: List[str] = []
    comment = function.get("comment")
    if comment:
        parts.append(comment)

    start = function.get("start")
    end = function.get("end")
    if start and end:
        bit_label = f"bit {start}" if start == end else f"bits {start}-{end}"
        parts.append(bit_label)

    mask = function.get("mask")
    if mask:
        parts.append(f"mask {mask}")

    value_text = (function.text or "").strip()
    descriptor = ", ".join(parts) if parts else "set value"
    group_label = f"Group {group_id}" if group_id else "Group"
    return f"{group_label}: {descriptor} → `{value_text}`"


def collect_code_steps(code: ET.Element) -> List[str]:
    steps: List[str] = []
    for child in code:
        if child.tag == "group":
            group_id = child.get("id")
            for func in child:
                if func.tag != "function":
                    continue
                steps.append(describe_function(group_id, func))
        elif child.tag == "function":
            steps.append(describe_function(None, child))
    return steps


def add_code_block(blocks: defaultdict, classification: str, source_file: Path, cafd: ET.Element, code: ET.Element) -> None:
    module_name = cafd.get("name", "<unknown module>")
    cafd_id = cafd.get("id", "<unknown id>")
    author = cafd.get("author") or "Unknown"
    module_series = cafd.get("series") or "Unspecified"

    header = f"## {source_file.name} — {module_name} (CAFD {cafd_id}, author: {author})"
    series_line = f"**Module series coverage:** {module_series}"

    code_description = code.get("description", "<no description provided>")
    applies_to = code.get("series") or "Inherits module coverage"
    steps = collect_code_steps(code)

    lines: MarkdownBlock = []
    lines.append(header)
    lines.append("")
    lines.append(series_line)
    lines.append("")
    lines.append(f"### {code_description}")
    lines.append(f"*Applies to:* {applies_to}")
    if steps:
        lines.append("*Implementation details:*")
        for step in steps:
            lines.append(f"  * {step}")
    else:
        lines.append("*Implementation details:* No explicit function values captured in XML.")
    lines.append("")

    blocks[classification].append("\n".join(lines))


def build_markdown(blocks: Iterable[str], intro: str) -> str:
    content: List[str] = [intro.strip(), ""]
    for block in blocks:
        content.append(block)
    return "\n".join(content).strip() + "\n"


def main() -> None:
    sections: defaultdict[str, List[str]] = defaultdict(list)

    for xml_file in iter_xml_files():
        try:
            tree = ET.parse(xml_file)
        except ET.ParseError as exc:
            raise SystemExit(f"Failed to parse {xml_file}: {exc}")
        root = tree.getroot()
        for cafd in root.findall("cafd"):
            for code in cafd.findall("code"):
                classification = classify_entry(code.get("series"), cafd.get("series"))
                if not classification:
                    continue
                add_code_block(sections, classification, xml_file, cafd, code)

    confirmed_intro = textwrap.dedent(
        """
        # F3x-Compatible Cheat Codes

        The entries below are collected from the XML presets in this repository and have
        explicit series coverage for BMW F3x chassis (F30–F36, F80–F83). Each item lists the
        module, the original preset description, and the exact function values required to
        reproduce the coding.
        """
    )
    confirmed_markdown = build_markdown(sections.get("confirmed", []), confirmed_intro)

    potential_intro = textwrap.dedent(
        """
        # F3x-Potential Cheat Codes

        These presets target closely related F-series chassis (primarily F2x 1/2 Series and
        other shared-module vehicles). They are likely to work on an F3x thanks to common
        control units, but the original XML does not explicitly declare F3x coverage. Review
        and test carefully before applying them to an F3x vehicle.
        """
    )
    potential_markdown = build_markdown(sections.get("potential", []), potential_intro)

    (CHEATS_DIR / "f3x-confirmed.md").write_text(confirmed_markdown, encoding="utf-8")
    (CHEATS_DIR / "f3x-potential.md").write_text(potential_markdown, encoding="utf-8")


if __name__ == "__main__":
    main()

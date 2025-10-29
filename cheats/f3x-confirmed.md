# F3x-Compatible Cheat Codes

The entries below are collected from the XML presets in this repository and have
explicit series coverage for BMW F3x chassis (F30–F36, F80–F83). Each item lists the
module, the original preset description, and the exact function values required to
reproduce the coding.

## Almaretto.xml — CFAS-PLX_1 (CAFD 000000B5, author: Almaretto)

**Module series coverage:** F010,F015,F030,F80

### Time Period Seats will Remember heating/cooling/massage settings (0 minutes)
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: 0 minutes, bit 4, mask 00000011b -> `00`

## Almaretto.xml — CFAS-PLX_1 (CAFD 000000B5, author: Almaretto)

**Module series coverage:** F010,F015,F030,F80

### Time Period Seats will Remember heating/cooling/massage settings (15 minutes)
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: 15 minutes, bit 4, mask 00000011b -> `01`

## Almaretto.xml — CFAS-PLX_1 (CAFD 000000B5, author: Almaretto)

**Module series coverage:** F010,F015,F030,F80

### Time Period Seats will Remember heating/cooling/massage settings (24 hours)
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: 24 hours, bit 4, mask 00000011b -> `02`

## Almaretto.xml — CFAS-PLX_1 (CAFD 000000B5, author: Almaretto)

**Module series coverage:** F010,F015,F030,F80

### Time Period Seats will Remember heating/cooling/massage settings (Infinity)
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: Infinity, bit 4, mask 00000011b -> `03`

## Almaretto.xml — CFAS-PLX_1 (CAFD 000000B5, author: Almaretto)

**Module series coverage:** F010,F015,F030,F80

### Easy Entry/Exit Steering Wheel and Driver Seat. Step 1 of 2. See FRM for F10
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: bit 0, mask 00011100b -> `Modus_FA_SLV`
  * Group 3012: bits 0-1, mask 11111111b -> `00, 28`
  * Group 3012: bits 4-5, mask 11111111b -> `00, 32`

## Bundang_Thunder.xml — ACSM_4B (CAFD 00000911, author: Bundang Thunder 1 Series)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Seat belt warning chime for only 5 seconds                                                                                 --** by Bundang Thunder ^^
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3001: GWF_SBR_WARNDAUER, bit 3, mask 11111111b -> `05`

## Bundang_Thunder.xml — ACSM_4B (CAFD 00000911, author: Bundang Thunder 1 Series)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Delete driver seat belt warning light
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: SBR_PreWarning_Fahrer, bit 16, mask 00000001b -> `00`

## Bundang_Thunder.xml — ACSM_4B (CAFD 00000911, author: Bundang Thunder 1 Series)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Delete passenger seat belt warning light
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: SBR_PreWarning_Beifahrer, bit 16, mask 00000010b -> `00`

## Bundang_Thunder.xml — ACSM_4B (CAFD 00000911, author: Bundang Thunder 1 Series)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Disable driver seat belt warning chime
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: SeatBeltReminder_SBR_Fahrer, bit 15, mask 00000010b -> `00`

## Bundang_Thunder.xml — ACSM_4B (CAFD 00000911, author: Bundang Thunder 1 Series)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Disable passenger seat belt warning chime
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: SeatBeltReminder_SBR_Beifahrer, bit 15, mask 00000100b -> `00`

## Bundang_Thunder.xml — DSC_CT01 (CAFD 000019CC, author: Bundang Thunder 1 Series)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Enable launch control (also enables EGS)                                                                     --** by Bundang Thunder ^^
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: C_Funktion_LaunchControl, bit 26, mask 00010000b -> `01`

## Bundang_Thunder.xml — GKEB23 (CAFD 0000023F, author: Bundang Thunder 1 Series)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Enable launch control (also enables DSC)                                                                     --** by Bundang Thunder ^^
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: LC, bit 1, mask 10000000b -> `01`

## Bundang_Thunder.xml — GKEB23 (CAFD 0000023F, author: Bundang Thunder 1 Series)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Show gear number in Dynamic Sport mode
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: Sportschalter, bit 1, mask 00000001b -> `01`
  * Group 3000: Sportschalter_alt, bit 0, mask 01000000b -> `01`

## Bundang_Thunder.xml — FEM_01 (CAFD 00000794, author: Bundang Thunder 1 Series)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Activate hazard lights during hard braking
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3060: WB_GB_ENABLE, bit 26, mask 00000001b -> `01`

## Bundang_Thunder.xml — FEM_01 (CAFD 00000794, author: Bundang Thunder 1 Series)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Set auto start/stop off by default
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3023: TCM_MSA_DEFAULT_OFF, bit 0, mask 00010000b -> `01`

## Bundang_Thunder.xml — FEM_01 (CAFD 00000794, author: Bundang Thunder 1 Series)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Remember last auto start/stop state
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3023: TCM_MSA_MEMORY, bit 0, mask 00100000b -> `01`

## Bundang_Thunder.xml — FEM_01 (CAFD 00000794, author: Bundang Thunder 1 Series)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Turn off audio when engine stops
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3020: TCM_LOGIC_R_OFF_DOOR, bit 1, mask 00000001b -> `01`

## Bundang_Thunder.xml — FEM_01 (CAFD 00000794, author: Bundang Thunder 1 Series)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Double horn when locking with engine running - enable
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3040: CLM_HORN_AT_SECURE, bit 1, mask 00100000b -> `01`

## Bundang_Thunder.xml — FEM_01 (CAFD 00000794, author: Bundang Thunder 1 Series)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Double horn when locking with engine running - disable
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3040: CLM_HORN_AT_SECURE, bit 1, mask 00100000b -> `00`

## Bundang_Thunder.xml — FEM_01 (CAFD 00000794, author: Bundang Thunder 1 Series)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Fold mirrors immediately when locking (lock folding)
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3053: KOMFORT_SCHLIESSEN, bit 9, mask 11111111b -> `00`

## Bundang_Thunder.xml — FEM_01 (CAFD 00000794, author: Bundang Thunder 1 Series)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Start engine without pressing brake
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3020: TCM_STARTLOCK_BRAKE, bit 0, mask 00000001b -> `00`

## Bundang_Thunder.xml — FEM_01 (CAFD 00000794, author: Bundang Thunder 1 Series)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Start engine without pressing clutch
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3020: TCM_STARTLOCK_CLUTCH, bit 0, mask 00000100b -> `00`

## Bundang_Thunder.xml — FEM_01 (CAFD 00000794, author: Bundang Thunder 1 Series)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Allow engine start in park
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3020: TCM_STARTLOCK_PARK, bit 0, mask 00000010b -> `00`
  * Group 3020: TCM_STARTLOCK_DRIVINGREADINESS, bit 1, mask 00010000b -> `00`

## Bundang_Thunder.xml — FEM_01 (CAFD 00000794, author: Bundang Thunder 1 Series)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### One-touch turn signal flashes five times
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3060: BLINKZYKLEN_ANZAHL_TIPP, bit 7, mask 00000111b -> `04`

## Bundang_Thunder.xml — FEM_01 (CAFD 00000794, author: Bundang Thunder 1 Series)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Welcome fog lights (hard on)
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3063: MAPPING_NEBELSCHW_L_PART_OF_WL, bit 55, mask 11000000b -> `hard_On`
  * Group 3063: MAPPING_NEBELSCHW_R_PART_OF_WL, bit 66, mask 11000000b -> `hard_On`

## Bundang_Thunder.xml — FEM_01 (CAFD 00000794, author: Bundang Thunder 1 Series)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Welcome fog lights (soft on)
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3063: MAPPING_NEBELSCHW_L_PART_OF_WL, bit 55, mask 11000000b -> `soft_On`
  * Group 3063: MAPPING_NEBELSCHW_R_PART_OF_WL, bit 66, mask 11000000b -> `soft_On`

## Bundang_Thunder.xml — FEM_01 (CAFD 00000794, author: Bundang Thunder 1 Series)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Cornering fog lights
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3073: C_CLC_ENA, bit 218, mask 00000010b -> `01`
  * Group 3073: C_BLC_ENA, bit 66, mask 00000001b -> `01`
  * Group 3066: KL_ENABLE_LI, bit 0, mask 00000001b -> `01`
  * Group 3066: KL_ENABLE_RE, bit 80, mask 00000001b -> `01`
  * Group 3062: MAPPING_abbiegel_L_output, bit 110, mask 00111111b -> `0B`
  * Group 3062: MAPPING_abbiegel_R_output, bit 121, mask 00111111b -> `0C`

## Bundang_Thunder.xml — FEM_01 (CAFD 00000794, author: Bundang Thunder 1 Series)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Turn on catch lights when reversing
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3070: OVT_BEI_RUECKFAHRLICHT, bit 11, mask 00010000b -> `01`

## Bundang_Thunder.xml — FEM_01 (CAFD 00000794, author: Bundang Thunder 1 Series)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Unlock doors automatically when engine off
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3040: CLM_UNLOCK_KL15OFF_AFTER_PIA_AUTO_LOCK, bit 1, mask 00000010b -> `01`

## Bundang_Thunder.xml — FEM_01 (CAFD 00000794, author: Bundang Thunder 1 Series)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Enable paddle shifter operation
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3190: PADDLES_VERBAUT, bit 9, mask 00000001b -> `01`

## Bundang_Thunder.xml — FEM_01 (CAFD 00000794, author: Bundang Thunder 1 Series)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Allow windows to keep closing with door open
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3050: FH_TUERAUF_STOP_MAUT, bit 0, mask 00000001b -> `00`

## Bundang_Thunder.xml — FEM_01 (CAFD 00000794, author: Bundang Thunder 1 Series)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Limit passenger mirror tilt to 30 degrees in reverse
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3110: ASP_BORDSTEINAUTOMATIK_DELTA, bit 2, mask 11111111b -> `1E`

## Bundang_Thunder.xml — HU_NBT (CAFD 00000DED, author: Bundang Thunder 1 Series)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Set time automatically                                                                                         --** by Bundang Thunder ^^
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: SETTINGS_TIME_AUTOMATIC, bit 19, mask 00000110b -> `navigation`
  * Group 3000: CLOCK_CHANGE_AUTOMATIC, bit 105, mask 00100000b -> `01`

## Bundang_Thunder.xml — HU_NBT (CAFD 00000DED, author: Bundang Thunder 1 Series)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Watch video/DMB/navigation while driving
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: SPEEDLOCK_X_KMH_MAX, bit 72, mask 11111111b -> `FF`
  * Group 3000: SPEEDLOCK_X_KMH_MIN, bit 71, mask 11111111b -> `FF`
  * Group 3000: VIDEO_FRONT_LOCKED, bit 5, mask 00010000b -> `00`
  * Group 3000: VIDEO_HANDBRAKE, bit 5, mask 00000100b -> `00`
  * Group 3000: VIDEO_SPEEDLOCK_CONDITION, bit 57, mask 00000111b -> `None`

## Bundang_Thunder.xml — HU_NBT (CAFD 00000DED, author: Bundang Thunder 1 Series)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Suppress all warning messages
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3001: LEGAL_DISCLAIMER_TIME, bit 58, mask 11111111b -> `kein_ld`
  * Group 3001: MACRO_CAM_LEGALDISCLAIMER, bit 52, mask 11111111b -> `kein_ld`

## Bundang_Thunder.xml — HU_NBT (CAFD 00000DED, author: Bundang Thunder 1 Series)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Enable trailer zoom menu when reversing
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3001: MACRO_TRAILER_COUPLING, bit 54, mask 00000001b -> `01`

## Bundang_Thunder.xml — HU_NBT (CAFD 00000DED, author: Bundang Thunder 1 Series)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Close windows when it rains
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: REGEN_SCHLIESSEN, bit 19, mask 00001000b -> `01`

## Bundang_Thunder.xml — HU_NBT (CAFD 00000DED, author: Bundang Thunder 1 Series)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### X-Drive
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: COMPASS, bit 5, mask 00000001b -> `01`
  * Group 3000: X_VIEW, bit 15, mask 00000001b -> `01`
  * Group 3000: X_VIEW_GRAPHIC_SLOP, bit 26, mask 00110000b -> `trajectory1`
  * Group 3000: X_VIEW_GRAPHIC_ROLL, bit 26, mask 11000000b -> `trajectory1`
  * Group 3000: MOMENTDISTRIBUTION_MENU, bit 110, mask 00000010b -> `01`

## Bundang_Thunder.xml — HU_NBT (CAFD 00000DED, author: Bundang Thunder 1 Series)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Enable USB video playback 1/2
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: ENT_CODEC_OGG, bit 15, mask 00010000b -> `01`
  * Group 3000: ENT_CODEC_XVID, bit 15, mask 00100000b -> `01`
  * Group 3000: ENT_CODEC_VCD, bit 15, mask 01000000b -> `01`
  * Group 3000: ENT_MC_VIDEO_SUPPORT, bit 13, mask 00000100b -> `01`

## Bundang_Thunder.xml — HU_NBT (CAFD 00000DED, author: Bundang Thunder 1 Series)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Enable USB video playback 2/2
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3003: API_USB_VIDEO, bit 33, mask 00000110b -> `both`
  * Group 3003: API_IPOD_VIDEO, bit 33, mask 00011000b -> `both`

## Bundang_Thunder.xml — HU_NBT (CAFD 00000DED, author: Bundang Thunder 1 Series)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Change warning chime to Rolls-Royce sound
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3002: SOUND_SIGNAL_SET, bit 26, mask 00111000b -> `rolls_royce`

## Bundang_Thunder.xml — HU_NBT (CAFD 00000DED, author: Bundang Thunder 1 Series)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Configure Sport mode
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3001: MACRO_FDS, bit 55, mask 00011000b -> `popup_and_config`
  * Group 3000: EFF_DYN_SPORT_CID, bit 101, mask 00010000b -> `01`
  * Group 3000: EFF_DYN_SPORT_UNIT, bit 107, mask 00000100b -> `01`

## Bundang_Thunder.xml — HU_NBT (CAFD 00000DED, author: Bundang Thunder 1 Series)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Startup animation
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3001: STARTUP_TYPE, bit 62, mask 00000110b -> `animation`
  * Group 3001: STARTUP_EMBLEM, bit 62, mask 01111000b -> `variant_01`

## Bundang_Thunder.xml — HU_NBT (CAFD 00000DED, author: Bundang Thunder 1 Series)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Volume adjustment bar
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3002: VOLUME_POPUP_DISPLAY, bit 52, mask 01000000b -> `01`
  * Group 3002: VOLUME_POPUP_REJECTION, bit 52, mask 10000000b -> `01`
  * Group 3002: VOLUME_POPUP_EXCEPTION, bit 53, mask 00000001b -> `01`

## Bundang_Thunder.xml — HU_NBT (CAFD 00000DED, author: Bundang Thunder 1 Series)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Show TPMC tire pressure temperature
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3001: RDC_DRUCK_TEMP, bit 66, mask 00001100b -> `druck_und_temperatur`

## Bundang_Thunder.xml — HU_NBT (CAFD 00000DED, author: Bundang Thunder 1 Series)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Output ringtone through speakers (iPhone only)
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3003: INBAND_RINGING, bit 6, mask 10000000b -> `01`

## Bundang_Thunder.xml — HU_NBT (CAFD 00000DED, author: Bundang Thunder 1 Series)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Lock/unlock confirmation chime (requires piezo buzzer sensor)
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: ACOUSTICAL_LOCK_CONFIRM, bit 110, mask 00000001b -> `01`

## Bundang_Thunder.xml — HU_NBT (CAFD 00000DED, author: Bundang Thunder 1 Series)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Change M Sport display cluster colors
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: M_VEHICLE, bit 133, mask 01000000b -> `01`

## Bundang_Thunder.xml — HU_NBT (CAFD 00000DED, author: Bundang Thunder 1 Series)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Adjust high-beam assistant in iDrive
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: HIGH_BEAM_ASSISTANT, bit 109, mask 10000000b -> `01`

## Bundang_Thunder.xml — HU_NBT (CAFD 00000DED, author: Bundang Thunder 1 Series)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Show currently playing album art in iDrive
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: ENT_BTAS_IAP_COVERART, bit 9, mask 00000100b -> `01`
  * Group 3003: ENT_BTAS_METADATA, bit 19, mask 00000100b -> `01`
  * Group 3003: ENT_BTAS_BROWSING, bit 19, mask 00001000b -> `01`

## Bundang_Thunder.xml — HU_NBT (CAFD 00000DED, author: Bundang Thunder 1 Series)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Unlock DVD region code
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: ENT_VIDEO_DVD_AREA_CODE, bit 7, mask 11111111b -> `alle_anderen`

## Bundang_Thunder.xml — HU_NBT (CAFD 00000DED, author: Bundang Thunder 1 Series)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Show turn signals in HUD
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3001: HUD_TURNSIGNAL, bit 55, mask 10000000b -> `01`

## Bundang_Thunder.xml — HU_NBT (CAFD 00000DED, author: Bundang Thunder 1 Series)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Set sound system to Bang & Olufsen
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: HIGH_END_AUDIO_B_UND_W, bit 21, mask 01100000b -> `keine_insz`

## Bundang_Thunder.xml — HU_NBT (CAFD 00000DED, author: Bundang Thunder 1 Series)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Enable Logic7 (S667A HiFi vehicles)
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: LOGIC7_SYMBOL, bit 22, mask 00001000b -> `01`

## Bundang_Thunder.xml — HU_NBT (CAFD 00000DED, author: Bundang Thunder 1 Series)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Enhance audio mid-bass
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3002: AUDIO_SYSTEM, bit 29, mask 00111100b -> `highpremium`
  * Group 3002: AUDIO_SYSTEM_VAR, bit 21, mask 00000011b -> `variant3`

## Bundang_Thunder.xml — ICMQL (CAFD 0000067B, author: Bundang Thunder 1 Series)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Default to Eco mode at start                                                                              --** by Bundang Thunder ^^
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: IcmKod_B_InitEco, bit 36, mask 00001000b -> `verbaut`

## Bundang_Thunder.xml — ICMQL (CAFD 0000067B, author: Bundang Thunder 1 Series)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Enable cruise control
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: C_Fahrfunktion, bit 128, mask 00001110b -> `01`

## Bundang_Thunder.xml — ICMQL (CAFD 0000067B, author: Bundang Thunder 1 Series)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Enable Sport+ mode
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: IcmKod_B_S2TBA, bit 18, mask 11111111b -> `verbaut`

## Bundang_Thunder.xml — IHKA_VA02 (CAFD 000016EE, author: Bundang Thunder 1 Series)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Remember last air conditioning state                                                                               --** by Bundang Thunder ^^
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3003: MEMORY_OFF, bit 0, mask 00000010b -> `01`

## Bundang_Thunder.xml — IHKA_VA02 (CAFD 000016EE, author: Bundang Thunder 1 Series)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Prevent AUTO button from turning on A/C
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3003: AC_ON_WITH_AUTO, bit 0, mask 00000100b -> `00`

## Bundang_Thunder.xml — IHKA_VA02 (CAFD 000016EE, author: Bundang Thunder 1 Series)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Remember HVAC recirculation mode
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3003: MEMORY_UMLUFT, bit 0, mask 00000001b -> `01`

## Bundang_Thunder.xml — KAFAS2 (CAFD 00001148, author: Bundang Thunder 1 Series)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Automatic high-beam assistant
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3050: FLA_ON_OFF, bit 1, mask 00000001b -> `FLA_on`
  * Group 3050: SPEED_SWITCHING_HIGH_BEAMS_ON, bit 6, mask 11111111b -> `CN`
  * Group 3050: SPEED_SWITCHING_HIGH_BEAMS_OFF, bit 7, mask 11111111b -> `China`

## Bundang_Thunder.xml — KOMBI L7_BASIS (CAFD 00000760, author: Bundang Thunder 1 Series)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Show logo on instrument cluster                                                                                    --** by Bundang Thunder ^^
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: BMW_LOGO, bit 0, mask 11110000b -> `mpm`

## Bundang_Thunder.xml — KOMBI L7_BASIS (CAFD 00000760, author: Bundang Thunder 1 Series)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Digital speed readout in cluster
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: BC_DIGITAL_V, bit 1, mask 00000010b -> `01`

## Bundang_Thunder.xml — KOMBI L7_BASIS (CAFD 00000760, author: Bundang Thunder 1 Series)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Disable warning chime below 3 degrees
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: CC_TEMPERATURWARNUNG, bit 19, mask 00000001b -> `00`

## Bundang_Thunder.xml — KOMBI L7_BASIS (CAFD 00000760, author: Bundang Thunder 1 Series)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Show auto start/stop status in cluster
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3003: MSA_VERFUEGBARANZEIGE_ENABLE, bit 3, mask 00001000b -> `01`

## Bundang_Thunder.xml — KOMBI L7_BASIS (CAFD 00000760, author: Bundang Thunder 1 Series)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Use GPS time
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: GPS_UHR, bit 1, mask 10000000b -> `01`

## Bundang_Thunder.xml — KOMBI L7_BASIS (CAFD 00000760, author: Bundang Thunder 1 Series)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Display gear number in Dynamic Sport mode
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: SPA_SPORT_ENABLE, bit 41, mask 00010000b -> `01`

## Bundang_Thunder.xml — KOMBI L7_BASIS (CAFD 00000760, author: Bundang Thunder 1 Series)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Enable Sport+ menu in cluster
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 300C: FDS_MENUE_TEXT_1, bit 0, mask 00001111b -> `menue_3`
  * Group 300C: FDS_MENUE_SIGNAL_1, bit 0, mask 11110000b -> `menue_3`
  * Group 300C: FDS_MENUE_TEXT_2, bit 1, mask 00001111b -> `menue_3`
  * Group 300C: FDS_MENUE_SIGNAL_2, bit 1, mask 11110000b -> `menue_3`
  * Group 300C: FDS_MENUE_TEXT_3, bit 2, mask 00001111b -> `menue_3`
  * Group 300C: FDS_MENUE_SIGNAL_3, bit 2, mask 11110000b -> `menue_3`
  * Group 300C: FDS_MENUE_TEXT_4, bit 3, mask 00001111b -> `menue_3`
  * Group 300C: FDS_MENUE_SIGNAL_4, bit 3, mask 11110000b -> `menue_3`
  * Group 300C: FDS_MENUE, bit 54, mask 11111111b -> `menue_3`

## Bundang_Thunder.xml — CFAS_PLX_1 (CAFD 000000B5, author: Bundang Thunder 1 Series)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Enable Easy Access                                                                         --** by Bundang Thunder ^^
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: EINAUSSTIEGSHILFE, bit 0, mask 00011100b -> `Modus_FA_SLV`

## Bundang_Thunder.xml — CFAS_PLX_1 (CAFD 000000B5, author: Bundang Thunder 1 Series)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Easy Access seat starts moving from end position
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3012: EAH_SCHUTZFREIRAUM_HINTEN_SLV_PHYS, bits 4-5, mask 11111111b -> `00, 01`

## Bundang_Thunder.xml — CFAS_PLX_1 (CAFD 000000B5, author: Bundang Thunder 1 Series)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Easy Access seat starts moving with 1 cm remaining
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3012: EAH_SCHUTZFREIRAUM_HINTEN_SLV_PHYS, bits 4-5, mask 11111111b -> `00, 0A`

## Bundang_Thunder.xml — CFAS_PLX_1 (CAFD 000000B5, author: Bundang Thunder 1 Series)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Easy Access seat starts moving with 2 cm remaining
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3012: EAH_SCHUTZFREIRAUM_HINTEN_SLV_PHYS, bits 4-5, mask 11111111b -> `00, 14`

## Bundang_Thunder.xml — CFAS_PLX_1 (CAFD 000000B5, author: Bundang Thunder 1 Series)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Easy Access seat starts moving with 3 cm remaining
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3012: EAH_SCHUTZFREIRAUM_HINTEN_SLV_PHYS, bits 4-5, mask 11111111b -> `00, 1E`

## Bundang_Thunder.xml — CFAS_PLX_1 (CAFD 000000B5, author: Bundang Thunder 1 Series)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Easy Access seat travel distance: 4 cm
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3012: EAH_VERFAHRWEG_SLV_PHYS, bits 0-1, mask 11111111b -> `00, 28`

## Bundang_Thunder.xml — CFAS_PLX_1 (CAFD 000000B5, author: Bundang Thunder 1 Series)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Easy Access seat travel distance: 5 cm
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3012: EAH_VERFAHRWEG_SLV_PHYS, bits 0-1, mask 11111111b -> `00, 32`

## Bundang_Thunder.xml — CFAS_PLX_1 (CAFD 000000B5, author: Bundang Thunder 1 Series)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Easy Access seat travel distance: 6 cm
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3012: EAH_VERFAHRWEG_SLV_PHYS, bits 0-1, mask 11111111b -> `00, 3C`

## Bundang_Thunder.xml — CFAS_PLX_1 (CAFD 000000B5, author: Bundang Thunder 1 Series)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Easy Access seat travel distance: 7 cm
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3012: EAH_VERFAHRWEG_SLV_PHYS, bits 0-1, mask 11111111b -> `00, 46`

## Bundang_Thunder.xml — CFAS_PLX_1 (CAFD 000000B5, author: Bundang Thunder 1 Series)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Set gong when saving seat position
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: MEMORY_GONG, bit 2, mask 00001000b -> `01`

## Bundang_Thunder.xml — TRSVC (CAFD 00000223, author: Bundang Thunder 1 Series)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Allow side view at any time                                                                   --** by Bundang Thunder ^^
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: SV_Activate_Speed_Limit, bit 114, mask 11111111b -> `FF`
  * Group 3000: SV_Deactivate_Speed, bit 115, mask 11111111b -> `FF`

## Bundang_Thunder.xml — ACSM_4B (CAFD 00000911, author: Bundang Thunder 3 Series)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Seat belt warning chime for only 5 seconds                                                                                 --** by Bundang Thunder ^^
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3001: GWF_SBR_WARNDAUER, bit 3, mask 11111111b -> `05`

## Bundang_Thunder.xml — ACSM_4B (CAFD 00000911, author: Bundang Thunder 3 Series)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Delete driver seat belt warning light
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: SBR_PreWarning_Fahrer, bit 16, mask 00000001b -> `00`

## Bundang_Thunder.xml — ACSM_4B (CAFD 00000911, author: Bundang Thunder 3 Series)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Delete passenger seat belt warning light
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: SBR_PreWarning_Beifahrer, bit 16, mask 00000010b -> `00`

## Bundang_Thunder.xml — ACSM_4B (CAFD 00000911, author: Bundang Thunder 3 Series)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Disable driver seat belt warning chime
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: SeatBeltReminder_SBR_Fahrer, bit 15, mask 00000010b -> `00`

## Bundang_Thunder.xml — ACSM_4B (CAFD 00000911, author: Bundang Thunder 3 Series)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Disable passenger seat belt warning chime
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: SeatBeltReminder_SBR_Beifahrer, bit 15, mask 00000100b -> `00`

## Bundang_Thunder.xml — ASD01 (CAFD 00000F9B, author: Bundang Thunder 3 Series)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Set exhaust sound to M4 engine                                                                                       --** by Bundang Thunder ^^
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: Model Range, bit 0, mask 11111111b -> `16`
  * Group 3000: Engine, bit 1, mask 11111111b -> `0A`

## Bundang_Thunder.xml — ASD01 (CAFD 00000F9B, author: Bundang Thunder 3 Series)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### ASD audio level
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: Audio Level, bit 2, mask 11111111b -> `01`

## Bundang_Thunder.xml — ASD01 (CAFD 00000F9B, author: Bundang Thunder 3 Series)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### ASD power class maximum
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: Power Class, bit 3, mask 11111111b -> `03`

## Bundang_Thunder.xml — ASD01 (CAFD 00000F9B, author: Bundang Thunder 3 Series)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### ASD power class medium
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: Power Class, bit 3, mask 11111111b -> `00`

## Bundang_Thunder.xml — DSC_CT01 (CAFD 000019CC, author: Bundang Thunder 3 Series)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Enable launch control (also enables EGS)                                                                     --** by Bundang Thunder ^^
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: C_Funktion_LaunchControl, bit 26, mask 00010000b -> `01`

## Bundang_Thunder.xml — GKEB23 (CAFD 0000023F, author: Bundang Thunder 3 Series)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Enable launch control (also enables DSC)                                                                     --** by Bundang Thunder ^^
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: LC, bit 1, mask 10000000b -> `01`

## Bundang_Thunder.xml — GKEB23 (CAFD 0000023F, author: Bundang Thunder 3 Series)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Show gear number in Dynamic Sport mode
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: Sportschalter, bit 1, mask 00000001b -> `01`
  * Group 3000: Sportschalter_alt, bit 0, mask 01000000b -> `01`

## Bundang_Thunder.xml — FEM_01 (CAFD 00000794, author: Bundang Thunder 3 Series)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Activate hazard lights during hard braking                                                                                   --** by Bundang Thunder ^^
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3060: WB_GB_ENABLE, bit 26, mask 00000001b -> `01`

## Bundang_Thunder.xml — FEM_01 (CAFD 00000794, author: Bundang Thunder 3 Series)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Set auto start/stop off by default
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3023: TCM_MSA_DEFAULT_OFF, bit 0, mask 00010000b -> `01`

## Bundang_Thunder.xml — FEM_01 (CAFD 00000794, author: Bundang Thunder 3 Series)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Remember last auto start/stop state
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3023: TCM_MSA_MEMORY, bit 0, mask 00100000b -> `01`

## Bundang_Thunder.xml — FEM_01 (CAFD 00000794, author: Bundang Thunder 3 Series)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Turn off audio when engine stops
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3020: TCM_LOGIC_R_OFF_DOOR, bit 1, mask 00000001b -> `01`

## Bundang_Thunder.xml — FEM_01 (CAFD 00000794, author: Bundang Thunder 3 Series)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Double horn when locking with engine running - enable
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3040: CLM_HORN_AT_SECURE, bit 1, mask 00100000b -> `01`

## Bundang_Thunder.xml — FEM_01 (CAFD 00000794, author: Bundang Thunder 3 Series)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Double horn when locking with engine running - disable
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3040: CLM_HORN_AT_SECURE, bit 1, mask 00100000b -> `00`

## Bundang_Thunder.xml — FEM_01 (CAFD 00000794, author: Bundang Thunder 3 Series)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Fold mirrors immediately when locking (lock folding)
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3053: KOMFORT_SCHLIESSEN, bit 9, mask 11111111b -> `00`

## Bundang_Thunder.xml — FEM_01 (CAFD 00000794, author: Bundang Thunder 3 Series)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Start engine without pressing brake
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3020: TCM_STARTLOCK_BRAKE, bit 0, mask 00000001b -> `00`

## Bundang_Thunder.xml — FEM_01 (CAFD 00000794, author: Bundang Thunder 3 Series)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Start engine without pressing clutch
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3020: TCM_STARTLOCK_CLUTCH, bit 0, mask 00000100b -> `00`

## Bundang_Thunder.xml — FEM_01 (CAFD 00000794, author: Bundang Thunder 3 Series)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Allow engine start in park
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3020: TCM_STARTLOCK_PARK, bit 0, mask 00000010b -> `00`
  * Group 3020: TCM_STARTLOCK_DRIVINGREADINESS, bit 1, mask 00010000b -> `00`

## Bundang_Thunder.xml — FEM_01 (CAFD 00000794, author: Bundang Thunder 3 Series)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### One-touch turn signal flashes five times
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3060: BLINKZYKLEN_ANZAHL_TIPP, bit 7, mask 00000111b -> `04`

## Bundang_Thunder.xml — FEM_01 (CAFD 00000794, author: Bundang Thunder 3 Series)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Welcome fog lights (hard on)
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3063: MAPPING_NEBELSCHW_L_PART_OF_WL, bit 55, mask 11000000b -> `hard_On`
  * Group 3063: MAPPING_NEBELSCHW_R_PART_OF_WL, bit 66, mask 11000000b -> `hard_On`

## Bundang_Thunder.xml — FEM_01 (CAFD 00000794, author: Bundang Thunder 3 Series)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Welcome fog lights (soft on)
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3063: MAPPING_NEBELSCHW_L_PART_OF_WL, bit 55, mask 11000000b -> `soft_On`
  * Group 3063: MAPPING_NEBELSCHW_R_PART_OF_WL, bit 66, mask 11000000b -> `soft_On`

## Bundang_Thunder.xml — FEM_01 (CAFD 00000794, author: Bundang Thunder 3 Series)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Cornering fog lights
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3073: C_CLC_ENA, bit 218, mask 00000010b -> `01`
  * Group 3073: C_BLC_ENA, bit 66, mask 00000001b -> `01`
  * Group 3066: KL_ENABLE_LI, bit 0, mask 00000001b -> `01`
  * Group 3066: KL_ENABLE_RE, bit 80, mask 00000001b -> `01`
  * Group 3062: MAPPING_abbiegel_L_output, bit 110, mask 00111111b -> `0B`
  * Group 3062: MAPPING_abbiegel_R_output, bit 121, mask 00111111b -> `0C`

## Bundang_Thunder.xml — FEM_01 (CAFD 00000794, author: Bundang Thunder 3 Series)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Turn on catch lights when reversing
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3070: OVT_BEI_RUECKFAHRLICHT, bit 11, mask 00010000b -> `01`

## Bundang_Thunder.xml — FEM_01 (CAFD 00000794, author: Bundang Thunder 3 Series)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Unlock doors automatically when engine off
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3040: CLM_UNLOCK_KL15OFF_AFTER_PIA_AUTO_LOCK, bit 1, mask 00000010b -> `01`

## Bundang_Thunder.xml — FEM_01 (CAFD 00000794, author: Bundang Thunder 3 Series)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Enable paddle shifter operation
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3190: PADDLES_VERBAUT, bit 0, mask 00000001b -> `01`

## Bundang_Thunder.xml — FEM_01 (CAFD 00000794, author: Bundang Thunder 3 Series)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Allow windows to keep closing with door open
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3050: FH_TUERAUF_STOP_MAUT, bit 0, mask 00000001b -> `00`

## Bundang_Thunder.xml — FEM_01 (CAFD 00000794, author: Bundang Thunder 3 Series)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Limit passenger mirror tilt to 30 degrees in reverse
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3110: ASP_BORDSTEINAUTOMATIK_DELTA, bit 1, mask 11111111b -> `1E`

## Bundang_Thunder.xml — HU_NBT (CAFD 00000DED, author: Bundang Thunder 3 Series)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Set time automatically                                                                                         --** by Bundang Thunder ^^
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: SETTINGS_TIME_AUTOMATIC, bit 19, mask 00000110b -> `navigation`
  * Group 3000: CLOCK_CHANGE_AUTOMATIC, bit 105, mask 00100000b -> `01`

## Bundang_Thunder.xml — HU_NBT (CAFD 00000DED, author: Bundang Thunder 3 Series)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Watch video/DMB/navigation while driving
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: SPEEDLOCK_X_KMH_MAX, bit 72, mask 11111111b -> `FF`
  * Group 3000: SPEEDLOCK_X_KMH_MIN, bit 71, mask 11111111b -> `FF`
  * Group 3000: VIDEO_FRONT_LOCKED, bit 5, mask 00010000b -> `00`
  * Group 3000: VIDEO_HANDBRAKE, bit 5, mask 00000100b -> `00`
  * Group 3000: VIDEO_SPEEDLOCK_CONDITION, bit 57, mask 00000111b -> `None`

## Bundang_Thunder.xml — HU_NBT (CAFD 00000DED, author: Bundang Thunder 3 Series)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Suppress all warning messages
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3001: LEGAL_DISCLAIMER_TIME, bit 58, mask 11111111b -> `kein_ld`
  * Group 3001: MACRO_CAM_LEGALDISCLAIMER, bit 52, mask 11111111b -> `kein_ld`

## Bundang_Thunder.xml — HU_NBT (CAFD 00000DED, author: Bundang Thunder 3 Series)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Enable trailer zoom menu when reversing
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3001: MACRO_TRAILER_COUPLING, bit 54, mask 00000001b -> `01`

## Bundang_Thunder.xml — HU_NBT (CAFD 00000DED, author: Bundang Thunder 3 Series)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Close windows when it rains
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: REGEN_SCHLIESSEN, bit 19, mask 00001000b -> `01`

## Bundang_Thunder.xml — HU_NBT (CAFD 00000DED, author: Bundang Thunder 3 Series)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### X-Drive
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: COMPASS, bit 5, mask 00000001b -> `01`
  * Group 3000: X_VIEW, bit 15, mask 00000001b -> `01`
  * Group 3000: X_VIEW_GRAPHIC_SLOP, bit 26, mask 00110000b -> `trajectory1`
  * Group 3000: X_VIEW_GRAPHIC_ROLL, bit 26, mask 11000000b -> `trajectory1`
  * Group 3000: MOMENTDISTRIBUTION_MENU, bit 110, mask 00000010b -> `01`

## Bundang_Thunder.xml — HU_NBT (CAFD 00000DED, author: Bundang Thunder 3 Series)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Enable USB video playback 1/2
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: ENT_CODEC_OGG, bit 15, mask 00010000b -> `01`
  * Group 3000: ENT_CODEC_XVID, bit 15, mask 00100000b -> `01`
  * Group 3000: ENT_CODEC_VCD, bit 15, mask 01000000b -> `01`
  * Group 3000: ENT_MC_VIDEO_SUPPORT, bit 13, mask 00000100b -> `01`

## Bundang_Thunder.xml — HU_NBT (CAFD 00000DED, author: Bundang Thunder 3 Series)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Enable USB video playback 2/2
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3003: API_USB_VIDEO, bit 33, mask 00000110b -> `both`
  * Group 3003: API_IPOD_VIDEO, bit 33, mask 00011000b -> `both`

## Bundang_Thunder.xml — HU_NBT (CAFD 00000DED, author: Bundang Thunder 3 Series)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Change warning chime to Rolls-Royce sound
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3002: SOUND_SIGNAL_SET, bit 26, mask 00111000b -> `rolls_royce`

## Bundang_Thunder.xml — HU_NBT (CAFD 00000DED, author: Bundang Thunder 3 Series)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Configure Sport mode
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3001: MACRO_FDS, bit 55, mask 00011000b -> `popup_and_config`
  * Group 3000: EFF_DYN_SPORT_CID, bit 101, mask 00010000b -> `01`
  * Group 3000: EFF_DYN_SPORT_UNIT, bit 107, mask 00000100b -> `01`

## Bundang_Thunder.xml — HU_NBT (CAFD 00000DED, author: Bundang Thunder 3 Series)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Startup animation
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3001: STARTUP_TYPE, bit 62, mask 00000110b -> `animation`
  * Group 3001: STARTUP_EMBLEM, bit 62, mask 01111000b -> `variant_01`

## Bundang_Thunder.xml — HU_NBT (CAFD 00000DED, author: Bundang Thunder 3 Series)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Volume adjustment bar
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3002: VOLUME_POPUP_DISPLAY, bit 52, mask 01000000b -> `01`
  * Group 3002: VOLUME_POPUP_REJECTION, bit 52, mask 10000000b -> `01`
  * Group 3002: VOLUME_POPUP_EXCEPTION, bit 53, mask 00000001b -> `01`

## Bundang_Thunder.xml — HU_NBT (CAFD 00000DED, author: Bundang Thunder 3 Series)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Show TPMC tire pressure temperature
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3001: RDC_DRUCK_TEMP, bit 66, mask 00001100b -> `druck_und_temperatur`

## Bundang_Thunder.xml — HU_NBT (CAFD 00000DED, author: Bundang Thunder 3 Series)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Output ringtone through speakers (iPhone only)
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3003: INBAND_RINGING, bit 6, mask 10000000b -> `01`

## Bundang_Thunder.xml — HU_NBT (CAFD 00000DED, author: Bundang Thunder 3 Series)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Lock/unlock confirmation chime (requires piezo buzzer sensor)
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: ACOUSTICAL_LOCK_CONFIRM, bit 110, mask 00000001b -> `01`

## Bundang_Thunder.xml — HU_NBT (CAFD 00000DED, author: Bundang Thunder 3 Series)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Change M Sport display cluster colors
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: M_VEHICLE, bit 133, mask 01000000b -> `01`

## Bundang_Thunder.xml — HU_NBT (CAFD 00000DED, author: Bundang Thunder 3 Series)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Adjust high-beam assistant in iDrive
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: HIGH_BEAM_ASSISTANT, bit 109, mask 10000000b -> `01`

## Bundang_Thunder.xml — HU_NBT (CAFD 00000DED, author: Bundang Thunder 3 Series)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Show currently playing album art in iDrive
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: ENT_BTAS_IAP_COVERART, bit 9, mask 00000100b -> `01`
  * Group 3003: ENT_BTAS_METADATA, bit 19, mask 00000100b -> `01`
  * Group 3003: ENT_BTAS_BROWSING, bit 19, mask 00001000b -> `01`

## Bundang_Thunder.xml — HU_NBT (CAFD 00000DED, author: Bundang Thunder 3 Series)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Unlock DVD region code
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: ENT_VIDEO_DVD_AREA_CODE, bit 7, mask 11111111b -> `alle_anderen`

## Bundang_Thunder.xml — HU_NBT (CAFD 00000DED, author: Bundang Thunder 3 Series)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Show turn signals in HUD
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3001: HUD_TURNSIGNAL, bit 55, mask 10000000b -> `01`

## Bundang_Thunder.xml — HU_NBT (CAFD 00000DED, author: Bundang Thunder 3 Series)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Set sound system to Bang & Olufsen
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: HIGH_END_AUDIO_B_UND_W, bit 21, mask 01100000b -> `keine_insz`

## Bundang_Thunder.xml — HU_NBT (CAFD 00000DED, author: Bundang Thunder 3 Series)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Enable Logic7 (S667A HiFi vehicles)
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: LOGIC7_SYMBOL, bit 22, mask 00001000b -> `01`

## Bundang_Thunder.xml — HU_NBT (CAFD 00000DED, author: Bundang Thunder 3 Series)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Enhance audio mid-bass
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3002: AUDIO_SYSTEM, bit 29, mask 00111100b -> `highpremium`
  * Group 3002: AUDIO_SYSTEM_VAR, bit 21, mask 00000011b -> `variant3`

## Bundang_Thunder.xml — ICMQL (CAFD 0000067B, author: Bundang Thunder 3 Series)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Default to Eco mode at start
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: IcmKod_B_InitEco, bit 36, mask 00001000b -> `verbaut`

## Bundang_Thunder.xml — ICMQL (CAFD 0000067B, author: Bundang Thunder 3 Series)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Enable cruise control
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: C_Fahrfunktion, bit 128, mask 00001110b -> `01`

## Bundang_Thunder.xml — ICMQL (CAFD 0000067B, author: Bundang Thunder 3 Series)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Enable Sport+ mode
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: IcmKod_B_S2TBA, bit 18, mask 11111111b -> `verbaut`

## Bundang_Thunder.xml — IHKA_VA02 (CAFD 000016EE, author: Bundang Thunder 3 Series)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Remember last air conditioning state                                                                               --** by Bundang Thunder ^^
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3003: MEMORY_OFF, bit 0, mask 00000010b -> `01`

## Bundang_Thunder.xml — IHKA_VA02 (CAFD 000016EE, author: Bundang Thunder 3 Series)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Prevent AUTO button from turning on A/C
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3003: AC_ON_WITH_AUTO, bit 0, mask 00000100b -> `00`

## Bundang_Thunder.xml — IHKA_VA02 (CAFD 000016EE, author: Bundang Thunder 3 Series)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Remember HVAC recirculation mode
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3003: MEMORY_UMLUFT, bit 0, mask 00000001b -> `01`

## Bundang_Thunder.xml — KAFAS2 (CAFD 00001148, author: Bundang Thunder 3 Series)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Automatic high-beam assistant                                                                                --** by Bundang Thunder ^^
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3050: FLA_ON_OFF, bit 1, mask 00000001b -> `FLA_on`
  * Group 3050: SPEED_SWITCHING_HIGH_BEAMS_ON, bit 6, mask 11111111b -> `CN`
  * Group 3050: SPEED_SWITCHING_HIGH_BEAMS_OFF, bit 7, mask 11111111b -> `China`

## Bundang_Thunder.xml — KOMBI FPK_I12 (CAFD 000009C8, author: Bundang Thunder 3 Series)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Show phone, entertainment, and voice prompts in HUD                                                               --** by Bundang Thunder ^^
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3003: HUD_ENTERTAINMENT_ENABLE, bit 10, mask 00000001b -> `01`
  * Group 3003: HUD_STARTUP_ENABLE, bit 5, mask 00000010b -> `01`
  * Group 3000: HUD_TLC_ENABLE, bit 41, mask 00000001b -> `01`
  * Group 3000: HUD_VZA_ENABLE, bit 40, mask 10000000b -> `01`

## Bundang_Thunder.xml — KOMBI FPK_I12 (CAFD 000009C8, author: Bundang Thunder 3 Series)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Show turn signals in HUD
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3003: HUD_BLINKER_ENABLE, bit 4, mask 00000001b -> `01`
  * Group 3008: HUD_PIA_BLINKER, bit 5, mask 00000001b -> `01`

## Bundang_Thunder.xml — KOMBI FPK_I12 (CAFD 000009C8, author: Bundang Thunder 3 Series)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Show logo on instrument cluster
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3003: MPM_ENABLE, bit 7, mask 00000010b -> `01`
  * Group 3000: MPM_LOGO, bit 43, mask 11110000b -> `bmw`
  * Group 3000: BMW_LOGO, bit 0, mask 00001111b -> `mpm`

## Bundang_Thunder.xml — KOMBI FPK_I12 (CAFD 000009C8, author: Bundang Thunder 3 Series)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Digital speed readout in cluster
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: BC_DIGITAL_V, bit 1, mask 00000010b -> `01`

## Bundang_Thunder.xml — KOMBI FPK_I12 (CAFD 000009C8, author: Bundang Thunder 3 Series)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Disable warning chime below 3 degrees
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: CC_TEMPERATURWARNUNG, bit 30, mask 00000001b -> `00`

## Bundang_Thunder.xml — KOMBI FPK_I12 (CAFD 000009C8, author: Bundang Thunder 3 Series)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Show auto start/stop status in cluster
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3003: MSA_VERFUEGBARANZEIGE_ENABLE, bit 6, mask 00001000b -> `01`

## Bundang_Thunder.xml — KOMBI FPK_I12 (CAFD 000009C8, author: Bundang Thunder 3 Series)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Use GPS time
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: GPS_UHR, bit 1, mask 10000000b -> `01`

## Bundang_Thunder.xml — KOMBI FPK_I12 (CAFD 000009C8, author: Bundang Thunder 3 Series)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Display gear number in Dynamic Sport mode
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: SPA_SPORT_ENABLE, bit 41, mask 00010000b -> `01`

## Bundang_Thunder.xml — KOMBI FPK_I12 (CAFD 000009C8, author: Bundang Thunder 3 Series)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Enable Sport+ menu in cluster
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 300C: FDS_MENUE_TEXT_1, bit 0, mask 00001111b -> `menue_3`
  * Group 300C: FDS_MENUE_SIGNAL_1, bit 0, mask 11110000b -> `menue_3`
  * Group 300C: FDS_MENUE_TEXT_2, bit 1, mask 00001111b -> `menue_3`
  * Group 300C: FDS_MENUE_SIGNAL_2, bit 1, mask 11110000b -> `menue_3`
  * Group 300C: FDS_MENUE_TEXT_3, bit 2, mask 00001111b -> `menue_3`
  * Group 300C: FDS_MENUE_SIGNAL_3, bit 2, mask 11110000b -> `menue_3`
  * Group 300C: FDS_MENUE_TEXT_4, bit 3, mask 00001111b -> `menue_3`
  * Group 300C: FDS_MENUE_SIGNAL_4, bit 3, mask 11110000b -> `menue_3`
  * Group 300C: FDS_MENUE, bit 54, mask 11111111b -> `menue_3`

## Bundang_Thunder.xml — CFAS_PLX_1 (CAFD 000000B5, author: Bundang Thunder 3 Series)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Enable Easy Access                                                                         --** by Bundang Thunder ^^
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: EINAUSSTIEGSHILFE, bit 0, mask 00011100b -> `Modus_FA_SLV`

## Bundang_Thunder.xml — CFAS_PLX_1 (CAFD 000000B5, author: Bundang Thunder 3 Series)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Easy Access seat starts moving from end position
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3012: EAH_SCHUTZFREIRAUM_HINTEN_SLV_PHYS, bits 4-5, mask 11111111b -> `00, 01`

## Bundang_Thunder.xml — CFAS_PLX_1 (CAFD 000000B5, author: Bundang Thunder 3 Series)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Easy Access seat starts moving with 1 cm remaining
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3012: EAH_SCHUTZFREIRAUM_HINTEN_SLV_PHYS, bits 4-5, mask 11111111b -> `00, 0A`

## Bundang_Thunder.xml — CFAS_PLX_1 (CAFD 000000B5, author: Bundang Thunder 3 Series)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Easy Access seat starts moving with 2 cm remaining
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3012: EAH_SCHUTZFREIRAUM_HINTEN_SLV_PHYS, bits 4-5, mask 11111111b -> `00, 14`

## Bundang_Thunder.xml — CFAS_PLX_1 (CAFD 000000B5, author: Bundang Thunder 3 Series)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Easy Access seat starts moving with 3 cm remaining
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3012: EAH_SCHUTZFREIRAUM_HINTEN_SLV_PHYS, bits 4-5, mask 11111111b -> `00, 1E`

## Bundang_Thunder.xml — CFAS_PLX_1 (CAFD 000000B5, author: Bundang Thunder 3 Series)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Easy Access seat travel distance: 4 cm
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3012: EAH_VERFAHRWEG_SLV_PHYS, bits 0-1, mask 11111111b -> `00, 28`

## Bundang_Thunder.xml — CFAS_PLX_1 (CAFD 000000B5, author: Bundang Thunder 3 Series)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Easy Access seat travel distance: 5 cm
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3012: EAH_VERFAHRWEG_SLV_PHYS, bits 0-1, mask 11111111b -> `00, 32`

## Bundang_Thunder.xml — CFAS_PLX_1 (CAFD 000000B5, author: Bundang Thunder 3 Series)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Easy Access seat travel distance: 6 cm
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3012: EAH_VERFAHRWEG_SLV_PHYS, bits 0-1, mask 11111111b -> `00, 3C`

## Bundang_Thunder.xml — CFAS_PLX_1 (CAFD 000000B5, author: Bundang Thunder 3 Series)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Easy Access seat travel distance: 7 cm
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3012: EAH_VERFAHRWEG_SLV_PHYS, bits 0-1, mask 11111111b -> `00, 46`

## Bundang_Thunder.xml — CFAS_PLX_1 (CAFD 000000B5, author: Bundang Thunder 3 Series)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Gentleman
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: GENTLEMAN, bit 1, mask 00000001b -> `01`
  * Group 3000: MEMORY, bit 0, mask 00000001b -> `01`

## Bundang_Thunder.xml — CFAS_PLX_1 (CAFD 000000B5, author: Bundang Thunder 3 Series)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Set gong when saving seat position
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: MEMORY_GONG, bit 2, mask 00001000b -> `01`

## Bundang_Thunder.xml — TRSVC (CAFD 00000223, author: Bundang Thunder 3 Series)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Allow side view at any time                                                                   --** by Bundang Thunder ^^
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: SV_Activate_Speed_Limit, bit 114, mask 11111111b -> `FF`
  * Group 3000: SV_Deactivate_Speed, bit 115, mask 11111111b -> `FF`

## Bundang_Thunder.xml — ACSM_4B (CAFD 00000911, author: Bundang Thunder 4 Series)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Seat belt warning chime for only 5 seconds                                                                                 --** by Bundang Thunder ^^
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3001: GWF_SBR_WARNDAUER, bit 3, mask 11111111b -> `05`

## Bundang_Thunder.xml — ACSM_4B (CAFD 00000911, author: Bundang Thunder 4 Series)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Delete driver seat belt warning light
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: SBR_PreWarning_Fahrer, bit 16, mask 00000001b -> `00`

## Bundang_Thunder.xml — ACSM_4B (CAFD 00000911, author: Bundang Thunder 4 Series)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Delete passenger seat belt warning light
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: SBR_PreWarning_Beifahrer, bit 16, mask 00000010b -> `00`

## Bundang_Thunder.xml — ACSM_4B (CAFD 00000911, author: Bundang Thunder 4 Series)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Disable driver seat belt warning chime
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: SeatBeltReminder_SBR_Fahrer, bit 15, mask 00000010b -> `00`

## Bundang_Thunder.xml — ACSM_4B (CAFD 00000911, author: Bundang Thunder 4 Series)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Disable passenger seat belt warning chime
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: SeatBeltReminder_SBR_Beifahrer, bit 15, mask 00000100b -> `00`

## Bundang_Thunder.xml — ASD01 (CAFD 00000F9B, author: Bundang Thunder 4 Series)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Set exhaust sound to M4 engine                                                                                       --** by Bundang Thunder ^^
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: Model Range, bit 0, mask 11111111b -> `16`
  * Group 3000: Engine, bit 1, mask 11111111b -> `0A`

## Bundang_Thunder.xml — ASD01 (CAFD 00000F9B, author: Bundang Thunder 4 Series)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### ASD audio level
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: Audio Level, bit 2, mask 11111111b -> `01`

## Bundang_Thunder.xml — ASD01 (CAFD 00000F9B, author: Bundang Thunder 4 Series)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### ASD power class maximum
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: Power Class, bit 3, mask 11111111b -> `03`

## Bundang_Thunder.xml — ASD01 (CAFD 00000F9B, author: Bundang Thunder 4 Series)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### ASD power class medium
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: Power Class, bit 3, mask 11111111b -> `00`

## Bundang_Thunder.xml — DSC_CT01 (CAFD 000019CC, author: Bundang Thunder 4 Series)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Enable launch control (also enables EGS)                                                                     --** by Bundang Thunder ^^
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: C_Funktion_LaunchControl, bit 26, mask 00010000b -> `01`

## Bundang_Thunder.xml — GKEB23 (CAFD 0000023F, author: Bundang Thunder 4 Series)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Enable launch control (also enables DSC)                                                                     --** by Bundang Thunder ^^
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: LC, bit 1, mask 10000000b -> `01`

## Bundang_Thunder.xml — GKEB23 (CAFD 0000023F, author: Bundang Thunder 4 Series)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Show gear number in Dynamic Sport mode
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: Sportschalter, bit 1, mask 00000001b -> `01`
  * Group 3000: Sportschalter_alt, bit 0, mask 01000000b -> `01`

## Bundang_Thunder.xml — FEM_01 (CAFD 00000794, author: Bundang Thunder 4 Series)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Activate hazard lights during hard braking                                                                                   --** by Bundang Thunder ^^
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3060: WB_GB_ENABLE, bit 26, mask 00000001b -> `01`

## Bundang_Thunder.xml — FEM_01 (CAFD 00000794, author: Bundang Thunder 4 Series)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Set auto start/stop off by default
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3023: TCM_MSA_DEFAULT_OFF, bit 0, mask 00010000b -> `01`

## Bundang_Thunder.xml — FEM_01 (CAFD 00000794, author: Bundang Thunder 4 Series)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Remember last auto start/stop state
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3023: TCM_MSA_MEMORY, bit 0, mask 00100000b -> `01`

## Bundang_Thunder.xml — FEM_01 (CAFD 00000794, author: Bundang Thunder 4 Series)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Turn off audio when engine stops
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3020: TCM_LOGIC_R_OFF_DOOR, bit 1, mask 00000001b -> `01`

## Bundang_Thunder.xml — FEM_01 (CAFD 00000794, author: Bundang Thunder 4 Series)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Double horn when locking with engine running - enable
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3040: CLM_HORN_AT_SECURE, bit 1, mask 00100000b -> `01`

## Bundang_Thunder.xml — FEM_01 (CAFD 00000794, author: Bundang Thunder 4 Series)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Double horn when locking with engine running - disable
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3040: CLM_HORN_AT_SECURE, bit 1, mask 00100000b -> `00`

## Bundang_Thunder.xml — FEM_01 (CAFD 00000794, author: Bundang Thunder 4 Series)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Fold mirrors immediately when locking (lock folding)
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3053: KOMFORT_SCHLIESSEN, bit 9, mask 11111111b -> `00`

## Bundang_Thunder.xml — FEM_01 (CAFD 00000794, author: Bundang Thunder 4 Series)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Start engine without pressing brake
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3020: TCM_STARTLOCK_BRAKE, bit 0, mask 00000001b -> `00`

## Bundang_Thunder.xml — FEM_01 (CAFD 00000794, author: Bundang Thunder 4 Series)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Start engine without pressing clutch
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3020: TCM_STARTLOCK_CLUTCH, bit 0, mask 00000100b -> `00`

## Bundang_Thunder.xml — FEM_01 (CAFD 00000794, author: Bundang Thunder 4 Series)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Allow engine start in park
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3020: TCM_STARTLOCK_PARK, bit 0, mask 00000010b -> `00`
  * Group 3020: TCM_STARTLOCK_DRIVINGREADINESS, bit 1, mask 00010000b -> `00`

## Bundang_Thunder.xml — FEM_01 (CAFD 00000794, author: Bundang Thunder 4 Series)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### One-touch turn signal flashes five times
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3060: BLINKZYKLEN_ANZAHL_TIPP, bit 7, mask 00000111b -> `04`

## Bundang_Thunder.xml — FEM_01 (CAFD 00000794, author: Bundang Thunder 4 Series)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Welcome fog lights (hard on)
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3063: MAPPING_NEBELSCHW_L_PART_OF_WL, bit 55, mask 11000000b -> `hard_On`
  * Group 3063: MAPPING_NEBELSCHW_R_PART_OF_WL, bit 66, mask 11000000b -> `hard_On`

## Bundang_Thunder.xml — FEM_01 (CAFD 00000794, author: Bundang Thunder 4 Series)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Welcome fog lights (soft on)
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3063: MAPPING_NEBELSCHW_L_PART_OF_WL, bit 55, mask 11000000b -> `soft_On`
  * Group 3063: MAPPING_NEBELSCHW_R_PART_OF_WL, bit 66, mask 11000000b -> `soft_On`

## Bundang_Thunder.xml — FEM_01 (CAFD 00000794, author: Bundang Thunder 4 Series)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Cornering fog lights
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3073: C_CLC_ENA, bit 218, mask 00000010b -> `01`
  * Group 3073: C_BLC_ENA, bit 66, mask 00000001b -> `01`
  * Group 3066: KL_ENABLE_LI, bit 0, mask 00000001b -> `KL_Ein`
  * Group 3066: KL_ENABLE_RE, bit 80, mask 00000001b -> `KL_Ein`
  * Group 3062: MAPPING_abbiegel_L_output, bit 110, mask 00111111b -> `0B`
  * Group 3062: MAPPING_abbiegel_R_output, bit 121, mask 00111111b -> `0C`

## Bundang_Thunder.xml — FEM_01 (CAFD 00000794, author: Bundang Thunder 4 Series)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Turn on catch lights when reversing
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3070: OVT_BEI_RUECKFAHRLICHT, bit 11, mask 00010000b -> `01`

## Bundang_Thunder.xml — FEM_01 (CAFD 00000794, author: Bundang Thunder 4 Series)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Unlock doors automatically when engine off
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3040: CLM_UNLOCK_KL15OFF_AFTER_PIA_AUTO_LOCK, bit 1, mask 00000010b -> `01`

## Bundang_Thunder.xml — FEM_01 (CAFD 00000794, author: Bundang Thunder 4 Series)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Enable paddle shifter operation
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3190: PADDLES_VERBAUT, bit 0, mask 00000001b -> `01`

## Bundang_Thunder.xml — FEM_01 (CAFD 00000794, author: Bundang Thunder 4 Series)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Allow windows to keep closing with door open
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3050: FH_TUERAUF_STOP_MAUT, bit 0, mask 00000001b -> `00`

## Bundang_Thunder.xml — FEM_01 (CAFD 00000794, author: Bundang Thunder 4 Series)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Limit passenger mirror tilt to 30 degrees in reverse
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3110: ASP_BORDSTEINAUTOMATIK_DELTA, bit 1, mask 11111111b -> `1E`

## Bundang_Thunder.xml — HU_NBT (CAFD 00000DED, author: Bundang Thunder 4 Series)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Set time automatically                                                                                         --** by Bundang Thunder ^^
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: SETTINGS_TIME_AUTOMATIC, bit 19, mask 00000110b -> `navigation`
  * Group 3000: CLOCK_CHANGE_AUTOMATIC, bit 105, mask 00100000b -> `01`

## Bundang_Thunder.xml — HU_NBT (CAFD 00000DED, author: Bundang Thunder 4 Series)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Watch video/DMB/navigation while driving
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: SPEEDLOCK_X_KMH_MAX, bit 72, mask 11111111b -> `FF`
  * Group 3000: SPEEDLOCK_X_KMH_MIN, bit 71, mask 11111111b -> `FF`
  * Group 3000: VIDEO_FRONT_LOCKED, bit 5, mask 00010000b -> `00`
  * Group 3000: VIDEO_HANDBRAKE, bit 5, mask 00000100b -> `00`
  * Group 3000: VIDEO_SPEEDLOCK_CONDITION, bit 57, mask 00000111b -> `None`

## Bundang_Thunder.xml — HU_NBT (CAFD 00000DED, author: Bundang Thunder 4 Series)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Suppress all warning messages
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3001: LEGAL_DISCLAIMER_TIME, bit 58, mask 11111111b -> `kein_ld`
  * Group 3001: MACRO_CAM_LEGALDISCLAIMER, bit 52, mask 11111111b -> `kein_ld`

## Bundang_Thunder.xml — HU_NBT (CAFD 00000DED, author: Bundang Thunder 4 Series)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Enable trailer zoom menu when reversing
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3001: MACRO_TRAILER_COUPLING, bit 54, mask 00000001b -> `01`

## Bundang_Thunder.xml — HU_NBT (CAFD 00000DED, author: Bundang Thunder 4 Series)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Close windows when it rains
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: REGEN_SCHLIESSEN, bit 19, mask 00001000b -> `01`

## Bundang_Thunder.xml — HU_NBT (CAFD 00000DED, author: Bundang Thunder 4 Series)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### X-Drive
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: COMPASS, bit 5, mask 00000001b -> `01`
  * Group 3000: X_VIEW, bit 15, mask 00000001b -> `01`
  * Group 3000: X_VIEW_GRAPHIC_SLOP, bit 26, mask 00110000b -> `trajectory1`
  * Group 3000: X_VIEW_GRAPHIC_ROLL, bit 26, mask 11000000b -> `trajectory1`
  * Group 3000: MOMENTDISTRIBUTION_MENU, bit 110, mask 00000010b -> `01`

## Bundang_Thunder.xml — HU_NBT (CAFD 00000DED, author: Bundang Thunder 4 Series)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Enable USB video playback 1/2
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: ENT_CODEC_OGG, bit 15, mask 00010000b -> `01`
  * Group 3000: ENT_CODEC_XVID, bit 15, mask 00100000b -> `01`
  * Group 3000: ENT_CODEC_VCD, bit 15, mask 01000000b -> `01`
  * Group 3000: ENT_MC_VIDEO_SUPPORT, bit 13, mask 00000100b -> `01`

## Bundang_Thunder.xml — HU_NBT (CAFD 00000DED, author: Bundang Thunder 4 Series)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Enable USB video playback 2/2
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3003: API_USB_VIDEO, bit 33, mask 00000110b -> `both`
  * Group 3003: API_IPOD_VIDEO, bit 33, mask 00011000b -> `both`

## Bundang_Thunder.xml — HU_NBT (CAFD 00000DED, author: Bundang Thunder 4 Series)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Change warning chime to Rolls-Royce sound
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3002: SOUND_SIGNAL_SET, bit 26, mask 00111000b -> `rolls_royce`

## Bundang_Thunder.xml — HU_NBT (CAFD 00000DED, author: Bundang Thunder 4 Series)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Configure Sport mode
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3001: MACRO_FDS, bit 55, mask 00011000b -> `popup_and_config`
  * Group 3000: EFF_DYN_SPORT_CID, bit 101, mask 00010000b -> `01`
  * Group 3000: EFF_DYN_SPORT_UNIT, bit 107, mask 00000100b -> `01`

## Bundang_Thunder.xml — HU_NBT (CAFD 00000DED, author: Bundang Thunder 4 Series)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Startup animation
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3001: STARTUP_TYPE, bit 62, mask 00000110b -> `animation`
  * Group 3001: STARTUP_EMBLEM, bit 62, mask 01111000b -> `variant_01`

## Bundang_Thunder.xml — HU_NBT (CAFD 00000DED, author: Bundang Thunder 4 Series)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Volume adjustment bar
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3002: VOLUME_POPUP_DISPLAY, bit 52, mask 01000000b -> `01`
  * Group 3002: VOLUME_POPUP_REJECTION, bit 52, mask 10000000b -> `01`
  * Group 3002: VOLUME_POPUP_EXCEPTION, bit 53, mask 00000001b -> `01`

## Bundang_Thunder.xml — HU_NBT (CAFD 00000DED, author: Bundang Thunder 4 Series)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Show TPMC tire pressure temperature
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3001: RDC_DRUCK_TEMP, bit 66, mask 00001100b -> `druck_und_temperatur`

## Bundang_Thunder.xml — HU_NBT (CAFD 00000DED, author: Bundang Thunder 4 Series)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Output ringtone through speakers (iPhone only)
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3003: INBAND_RINGING, bit 6, mask 10000000b -> `01`

## Bundang_Thunder.xml — HU_NBT (CAFD 00000DED, author: Bundang Thunder 4 Series)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Lock/unlock confirmation chime (requires piezo buzzer sensor)
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: ACOUSTICAL_LOCK_CONFIRM, bit 110, mask 00000001b -> `01`

## Bundang_Thunder.xml — HU_NBT (CAFD 00000DED, author: Bundang Thunder 4 Series)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Change M Sport display cluster colors
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: M_VEHICLE, bit 133, mask 01000000b -> `01`

## Bundang_Thunder.xml — HU_NBT (CAFD 00000DED, author: Bundang Thunder 4 Series)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Adjust high-beam assistant in iDrive
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: HIGH_BEAM_ASSISTANT, bit 109, mask 10000000b -> `01`

## Bundang_Thunder.xml — HU_NBT (CAFD 00000DED, author: Bundang Thunder 4 Series)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Show currently playing album art in iDrive
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: ENT_BTAS_IAP_COVERART, bit 9, mask 00000100b -> `01`
  * Group 3003: ENT_BTAS_METADATA, bit 19, mask 00000100b -> `01`
  * Group 3003: ENT_BTAS_BROWSING, bit 19, mask 00001000b -> `01`

## Bundang_Thunder.xml — HU_NBT (CAFD 00000DED, author: Bundang Thunder 4 Series)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Unlock DVD region code
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: ENT_VIDEO_DVD_AREA_CODE, bit 7, mask 11111111b -> `alle_anderen`

## Bundang_Thunder.xml — HU_NBT (CAFD 00000DED, author: Bundang Thunder 4 Series)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Show turn signals in HUD
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3001: HUD_TURNSIGNAL, bit 55, mask 10000000b -> `01`

## Bundang_Thunder.xml — HU_NBT (CAFD 00000DED, author: Bundang Thunder 4 Series)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Set sound system to Bang & Olufsen
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: HIGH_END_AUDIO_B_UND_W, bit 21, mask 01100000b -> `keine_insz`

## Bundang_Thunder.xml — HU_NBT (CAFD 00000DED, author: Bundang Thunder 4 Series)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Enable Logic7 (S667A HiFi vehicles)
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: LOGIC7_SYMBOL, bit 22, mask 00001000b -> `01`

## Bundang_Thunder.xml — HU_NBT (CAFD 00000DED, author: Bundang Thunder 4 Series)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Enhance audio mid-bass
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3002: AUDIO_SYSTEM, bit 29, mask 00111100b -> `highpremium`
  * Group 3002: AUDIO_SYSTEM_VAR, bit 21, mask 00000011b -> `variant3`

## Bundang_Thunder.xml — ICMQL (CAFD 0000067B, author: Bundang Thunder 4 Series)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Default to Eco mode at start                                                                              --** by Bundang Thunder ^^
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: IcmKod_B_InitEco, bit 36, mask 00001000b -> `verbaut`

## Bundang_Thunder.xml — ICMQL (CAFD 0000067B, author: Bundang Thunder 4 Series)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Enable cruise control
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: C_Fahrfunktion, bit 128, mask 00001110b -> `01`

## Bundang_Thunder.xml — ICMQL (CAFD 0000067B, author: Bundang Thunder 4 Series)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Enable Sport+ mode
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: IcmKod_B_S2TBA, bit 18, mask 11111111b -> `verbaut`

## Bundang_Thunder.xml — IHKA_VA02 (CAFD 000016EE, author: Bundang Thunder 4 Series)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Remember last air conditioning state                                                                               --** by Bundang Thunder ^^
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3003: MEMORY_OFF, bit 0, mask 00000010b -> `01`

## Bundang_Thunder.xml — IHKA_VA02 (CAFD 000016EE, author: Bundang Thunder 4 Series)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Prevent AUTO button from turning on A/C
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3003: AC_ON_WITH_AUTO, bit 0, mask 00000100b -> `00`

## Bundang_Thunder.xml — IHKA_VA02 (CAFD 000016EE, author: Bundang Thunder 4 Series)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Remember HVAC recirculation mode
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3003: MEMORY_UMLUFT, bit 0, mask 00000001b -> `01`

## Bundang_Thunder.xml — KAFAS2 (CAFD 00001148, author: Bundang Thunder 4 Series)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Automatic high-beam assistant                                                                                --** by Bundang Thunder ^^
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3050: FLA_ON_OFF, bit 1, mask 00000001b -> `FLA_on`
  * Group 3050: SPEED_SWITCHING_HIGH_BEAMS_ON, bit 6, mask 11111111b -> `CN`
  * Group 3050: SPEED_SWITCHING_HIGH_BEAMS_OFF, bit 7, mask 11111111b -> `China`

## Bundang_Thunder.xml — KOMBI L7_MID (CAFD 000009C8, author: Bundang Thunder 4 Series)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Show phone, entertainment, and voice prompts in HUD                                                               --** by Bundang Thunder ^^
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3003: HUD_ENTERTAINMENT_ENABLE, bit 4, mask 00010000b -> `01`
  * Group 3003: HUD_STARTUP_ENABLE, bit 5, mask 00000010b -> `01`
  * Group 3000: HUD_TLC_ENABLE, bit 41, mask 00000001b -> `01`
  * Group 3000: HUD_VZA_ENABLE, bit 42, mask 00001000b -> `01`

## Bundang_Thunder.xml — KOMBI L7_MID (CAFD 000009C8, author: Bundang Thunder 4 Series)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Show turn signals in HUD
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3003: HUD_BLINKER_ENABLE, bit 4, mask 00000001b -> `01`
  * Group 3008: HUD_PIA_BLINKER, bit 5, mask 00000001b -> `01`

## Bundang_Thunder.xml — KOMBI L7_MID (CAFD 000009C8, author: Bundang Thunder 4 Series)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Show logo on instrument cluster
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3003: MPM_ENABLE, bit 7, mask 00000100b -> `01`
  * Group 3000: MPM_LOGO, bit 43, mask 11110000b -> `ag`
  * Group 3000: BMW_LOGO, bit 0, mask 11110000b -> `m_performance`

## Bundang_Thunder.xml — KOMBI L7_MID (CAFD 000009C8, author: Bundang Thunder 4 Series)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Digital speed readout in cluster
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: BC_DIGITAL_V, bit 1, mask 00000010b -> `01`

## Bundang_Thunder.xml — KOMBI L7_MID (CAFD 000009C8, author: Bundang Thunder 4 Series)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Disable warning chime below 3 degrees
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: CC_TEMPERATURWARNUNG, bit 30, mask 00000001b -> `00`

## Bundang_Thunder.xml — KOMBI L7_MID (CAFD 000009C8, author: Bundang Thunder 4 Series)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Show auto start/stop status in cluster
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3003: MSA_VERFUEGBARANZEIGE_ENABLE, bit 6, mask 00001000b -> `01`

## Bundang_Thunder.xml — KOMBI L7_MID (CAFD 000009C8, author: Bundang Thunder 4 Series)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Use GPS time
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: GPS_UHR, bit 1, mask 10000000b -> `01`

## Bundang_Thunder.xml — KOMBI L7_MID (CAFD 000009C8, author: Bundang Thunder 4 Series)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Display gear number in Dynamic Sport mode
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: SPA_SPORT_ENABLE, bit 41, mask 00010000b -> `01`

## Bundang_Thunder.xml — KOMBI L7_MID (CAFD 000009C8, author: Bundang Thunder 4 Series)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Enable Sport+ menu in cluster
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 300C: FDS_MENUE_TEXT_1, bit 0, mask 00001111b -> `menue_3`
  * Group 300C: FDS_MENUE_SIGNAL_1, bit 0, mask 11110000b -> `menue_3`
  * Group 300C: FDS_MENUE_TEXT_2, bit 1, mask 00001111b -> `menue_3`
  * Group 300C: FDS_MENUE_SIGNAL_2, bit 1, mask 11110000b -> `menue_3`
  * Group 300C: FDS_MENUE_TEXT_3, bit 2, mask 00001111b -> `menue_3`
  * Group 300C: FDS_MENUE_SIGNAL_3, bit 2, mask 11110000b -> `menue_3`
  * Group 300C: FDS_MENUE_TEXT_4, bit 3, mask 00001111b -> `menue_3`
  * Group 300C: FDS_MENUE_SIGNAL_4, bit 3, mask 11110000b -> `menue_3`
  * Group 300C: FDS_MENUE, bit 54, mask 11111111b -> `menue_3`

## Bundang_Thunder.xml — CFAS_PLX_1 (CAFD 000000B5, author: Bundang Thunder 4 Series)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Enable Easy Access                                                                         --** by Bundang Thunder ^^
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: EINAUSSTIEGSHILFE, bit 0, mask 00011100b -> `Modus_FA_SLV`

## Bundang_Thunder.xml — CFAS_PLX_1 (CAFD 000000B5, author: Bundang Thunder 4 Series)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Easy Access seat starts moving from end position
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3012: EAH_SCHUTZFREIRAUM_HINTEN_SLV_PHYS, bits 4-5, mask 11111111b -> `00, 01`

## Bundang_Thunder.xml — CFAS_PLX_1 (CAFD 000000B5, author: Bundang Thunder 4 Series)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Easy Access seat starts moving with 1 cm remaining
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3012: EAH_SCHUTZFREIRAUM_HINTEN_SLV_PHYS, bits 4-5, mask 11111111b -> `00, 0A`

## Bundang_Thunder.xml — CFAS_PLX_1 (CAFD 000000B5, author: Bundang Thunder 4 Series)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Easy Access seat starts moving with 2 cm remaining
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3012: EAH_SCHUTZFREIRAUM_HINTEN_SLV_PHYS, bits 4-5, mask 11111111b -> `00, 14`

## Bundang_Thunder.xml — CFAS_PLX_1 (CAFD 000000B5, author: Bundang Thunder 4 Series)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Easy Access seat starts moving with 3 cm remaining
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3012: EAH_SCHUTZFREIRAUM_HINTEN_SLV_PHYS, bits 4-5, mask 11111111b -> `00, 1E`

## Bundang_Thunder.xml — CFAS_PLX_1 (CAFD 000000B5, author: Bundang Thunder 4 Series)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Easy Access seat travel distance: 4 cm
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3012: EAH_VERFAHRWEG_SLV_PHYS, bits 0-1, mask 11111111b -> `00, 28`

## Bundang_Thunder.xml — CFAS_PLX_1 (CAFD 000000B5, author: Bundang Thunder 4 Series)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Easy Access seat travel distance: 5 cm
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3012: EAH_VERFAHRWEG_SLV_PHYS, bits 0-1, mask 11111111b -> `00, 32`

## Bundang_Thunder.xml — CFAS_PLX_1 (CAFD 000000B5, author: Bundang Thunder 4 Series)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Easy Access seat travel distance: 6 cm
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3012: EAH_VERFAHRWEG_SLV_PHYS, bits 0-1, mask 11111111b -> `00, 3C`

## Bundang_Thunder.xml — CFAS_PLX_1 (CAFD 000000B5, author: Bundang Thunder 4 Series)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Easy Access seat travel distance: 7 cm
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3012: EAH_VERFAHRWEG_SLV_PHYS, bits 0-1, mask 11111111b -> `00, 46`

## Bundang_Thunder.xml — CFAS_PLX_1 (CAFD 000000B5, author: Bundang Thunder 4 Series)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Gentleman
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: GENTLEMAN, bit 1, mask 00000001b -> `01`
  * Group 3000: MEMORY, bit 0, mask 00000001b -> `01`

## Bundang_Thunder.xml — CFAS_PLX_1 (CAFD 000000B5, author: Bundang Thunder 4 Series)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Set gong when saving seat position
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: MEMORY_GONG, bit 2, mask 00001000b -> `01`

## Bundang_Thunder.xml — TRSVC (CAFD 00000223, author: Bundang Thunder 4 Series)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Allow side view at any time                                                                   --** by Bundang Thunder ^^
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: SV_Activate_Speed_Limit, bit 114, mask 11111111b -> `FF`
  * Group 3000: SV_Deactivate_Speed, bit 115, mask 11111111b -> `FF`

## Bundang_Thunder.xml — ACSM_4B (CAFD 00000911, author: Bundang Thunder 3GT)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Seat belt warning chime for only 5 seconds                                                                                 --** by Bundang Thunder ^^
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3001: GWF_SBR_WARNDAUER, bit 3, mask 11111111b -> `05`

## Bundang_Thunder.xml — ACSM_4B (CAFD 00000911, author: Bundang Thunder 3GT)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Delete driver seat belt warning light
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: SBR_PreWarning_Fahrer, bit 16, mask 00000001b -> `00`

## Bundang_Thunder.xml — ACSM_4B (CAFD 00000911, author: Bundang Thunder 3GT)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Delete passenger seat belt warning light
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: SBR_PreWarning_Beifahrer, bit 16, mask 00000010b -> `00`

## Bundang_Thunder.xml — ACSM_4B (CAFD 00000911, author: Bundang Thunder 3GT)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Disable driver seat belt warning chime
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: SeatBeltReminder_SBR_Fahrer, bit 15, mask 00000010b -> `00`

## Bundang_Thunder.xml — ACSM_4B (CAFD 00000911, author: Bundang Thunder 3GT)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Disable passenger seat belt warning chime
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: SeatBeltReminder_SBR_Beifahrer, bit 15, mask 00000100b -> `00`

## Bundang_Thunder.xml — DSC_CT01 (CAFD 000019CC, author: Bundang Thunder 3GT)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Enable launch control (also enables EGS)                                                                     --** by Bundang Thunder ^^
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: C_Funktion_LaunchControl, bit 26, mask 00010000b -> `01`

## Bundang_Thunder.xml — GKEB23 (CAFD 0000023F, author: Bundang Thunder 3GT)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Enable launch control (also enables DSC)                                                                     --** by Bundang Thunder ^^
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: LC, bit 1, mask 10000000b -> `01`

## Bundang_Thunder.xml — GKEB23 (CAFD 0000023F, author: Bundang Thunder 3GT)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Show gear number in Dynamic Sport mode
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: Sportschalter, bit 1, mask 00000001b -> `01`
  * Group 3000: Sportschalter_alt, bit 0, mask 01000000b -> `01`

## Bundang_Thunder.xml — FEM_01 (CAFD 00000794, author: Bundang Thunder 3GT)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Activate hazard lights during hard braking                                                                                   --** by Bundang Thunder ^^
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3060: WB_GB_ENABLE, bit 26, mask 00000001b -> `01`

## Bundang_Thunder.xml — FEM_01 (CAFD 00000794, author: Bundang Thunder 3GT)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Set auto start/stop off by default
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3023: TCM_MSA_DEFAULT_OFF, bit 0, mask 00010000b -> `01`

## Bundang_Thunder.xml — FEM_01 (CAFD 00000794, author: Bundang Thunder 3GT)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Remember last auto start/stop state
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3023: TCM_MSA_MEMORY, bit 0, mask 00100000b -> `01`

## Bundang_Thunder.xml — FEM_01 (CAFD 00000794, author: Bundang Thunder 3GT)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Turn off audio when engine stops
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3020: TCM_LOGIC_R_OFF_DOOR, bit 1, mask 00000001b -> `01`

## Bundang_Thunder.xml — FEM_01 (CAFD 00000794, author: Bundang Thunder 3GT)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Double horn when locking with engine running - enable
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3040: CLM_HORN_AT_SECURE, bit 1, mask 00100000b -> `01`

## Bundang_Thunder.xml — FEM_01 (CAFD 00000794, author: Bundang Thunder 3GT)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Double horn when locking with engine running - disable
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3040: CLM_HORN_AT_SECURE, bit 1, mask 00100000b -> `00`

## Bundang_Thunder.xml — FEM_01 (CAFD 00000794, author: Bundang Thunder 3GT)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Fold mirrors immediately when locking (lock folding)
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3053: KOMFORT_SCHLIESSEN, bit 9, mask 11111111b -> `00`

## Bundang_Thunder.xml — FEM_01 (CAFD 00000794, author: Bundang Thunder 3GT)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Start engine without pressing brake
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3020: TCM_STARTLOCK_BRAKE, bit 0, mask 00000001b -> `00`

## Bundang_Thunder.xml — FEM_01 (CAFD 00000794, author: Bundang Thunder 3GT)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Start engine without pressing clutch
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3020: TCM_STARTLOCK_CLUTCH, bit 0, mask 00000100b -> `00`

## Bundang_Thunder.xml — FEM_01 (CAFD 00000794, author: Bundang Thunder 3GT)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Allow engine start in park
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3020: TCM_STARTLOCK_PARK, bit 0, mask 00000010b -> `00`
  * Group 3020: TCM_STARTLOCK_DRIVINGREADINESS, bit 1, mask 00010000b -> `00`

## Bundang_Thunder.xml — FEM_01 (CAFD 00000794, author: Bundang Thunder 3GT)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### One-touch turn signal flashes five times
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3060: BLINKZYKLEN_ANZAHL_TIPP, bit 7, mask 00000111b -> `04`

## Bundang_Thunder.xml — FEM_01 (CAFD 00000794, author: Bundang Thunder 3GT)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Welcome fog lights (hard on)
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3063: MAPPING_NEBELSCHW_L_PART_OF_WL, bit 55, mask 11000000b -> `hard_On`
  * Group 3063: MAPPING_NEBELSCHW_R_PART_OF_WL, bit 66, mask 11000000b -> `hard_On`

## Bundang_Thunder.xml — FEM_01 (CAFD 00000794, author: Bundang Thunder 3GT)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Welcome fog lights (soft on)
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3063: MAPPING_NEBELSCHW_L_PART_OF_WL, bit 55, mask 11000000b -> `soft_On`
  * Group 3063: MAPPING_NEBELSCHW_R_PART_OF_WL, bit 66, mask 11000000b -> `soft_On`

## Bundang_Thunder.xml — FEM_01 (CAFD 00000794, author: Bundang Thunder 3GT)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Cornering fog lights
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3073: C_CLC_ENA, bit 218, mask 00000010b -> `01`
  * Group 3073: C_BLC_ENA, bit 66, mask 00000001b -> `01`
  * Group 3066: KL_ENABLE_LI, bit 0, mask 00000001b -> `01`
  * Group 3066: KL_ENABLE_RE, bit 80, mask 00000001b -> `01`
  * Group 3062: MAPPING_ABBIEGEL_L_OUTPUT, bit 110, mask 00111111b -> `0B`
  * Group 3062: MAPPING_ABBIEGEL_R_OUTPUT, bit 121, mask 00111111b -> `0C`

## Bundang_Thunder.xml — FEM_01 (CAFD 00000794, author: Bundang Thunder 3GT)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Turn on catch lights when reversing
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3070: OVT_BEI_RUECKFAHRLICHT, bit 11, mask 00010000b -> `01`

## Bundang_Thunder.xml — FEM_01 (CAFD 00000794, author: Bundang Thunder 3GT)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Unlock doors automatically when engine off
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3040: CLM_UNLOCK_KL15OFF_AFTER_PIA_AUTO_LOCK, bit 1, mask 00000010b -> `01`

## Bundang_Thunder.xml — FEM_01 (CAFD 00000794, author: Bundang Thunder 3GT)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Enable paddle shifter operation
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3190: PADDLES_VERBAUT, bit 0, mask 00000001b -> `01`

## Bundang_Thunder.xml — FEM_01 (CAFD 00000794, author: Bundang Thunder 3GT)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Allow windows to keep closing with door open
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3050: FH_TUERAUF_STOP_MAUT, bit 0, mask 00000001b -> `00`

## Bundang_Thunder.xml — FEM_01 (CAFD 00000794, author: Bundang Thunder 3GT)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Limit passenger mirror tilt to 30 degrees in reverse
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3110: ASP_BORDSTEINAUTOMATIK_DELTA, bit 2, mask 11111111b -> `1E`

## Bundang_Thunder.xml — HKFM (CAFD 0000157F, author: Bundang Thunder 3GT)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Auto-close trunk (footwell switch + remote)                                                                   --** by Bundang Thunder ^^
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3010: TASTER_FBD, bit 0, mask 00001000b -> `01`
  * Group 3010: SCH_TOEHKI, bit 2, mask 00000100b -> `01`
  * Group 3010: SCH_FBD, bit 2, mask 00001000b -> `01`

## Bundang_Thunder.xml — HKFM (CAFD 0000157F, author: Bundang Thunder 3GT)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Spoiler deployment speed: 70 km/h
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3100: V_ASP_OUT, bits 0-1, mask 11111111b -> `00, 46`

## Bundang_Thunder.xml — HKFM (CAFD 0000157F, author: Bundang Thunder 3GT)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Spoiler deployment speed: 80 km/h
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3100: V_ASP_OUT, bits 0-1, mask 11111111b -> `00, 50`

## Bundang_Thunder.xml — HKFM (CAFD 0000157F, author: Bundang Thunder 3GT)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Spoiler deployment speed: 90 km/h
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3100: V_ASP_OUT, bits 0-1, mask 11111111b -> `00, 5A`

## Bundang_Thunder.xml — HKFM (CAFD 0000157F, author: Bundang Thunder 3GT)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Spoiler deployment speed: 100 km/h
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3100: V_ASP_OUT, bits 0-1, mask 11111111b -> `00, 64`

## Bundang_Thunder.xml — HKFM (CAFD 0000157F, author: Bundang Thunder 3GT)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Spoiler retract speed: 80 km/h
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3100: V_ASP_IN, bits 2-3, mask 11111111b -> `00, 50`

## Bundang_Thunder.xml — HKFM (CAFD 0000157F, author: Bundang Thunder 3GT)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Spoiler retract speed: 70 km/h
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3100: V_ASP_IN, bits 2-3, mask 11111111b -> `00, 46`

## Bundang_Thunder.xml — HKFM (CAFD 0000157F, author: Bundang Thunder 3GT)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Spoiler retract speed: 60 km/h
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3100: V_ASP_IN, bits 2-3, mask 11111111b -> `00, 3C`

## Bundang_Thunder.xml — HKFM (CAFD 0000157F, author: Bundang Thunder 3GT)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Spoiler retract speed: 50 km/h
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3100: V_ASP_IN, bits 2-3, mask 11111111b -> `00, 32`

## Bundang_Thunder.xml — HU_NBT_EVO (CAFD 00001EF6, author: Bundang Thunder 3GT)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Set time automatically                                                                                         --** by Bundang Thunder ^^
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: SETTINGS_TIME_AUTOMATIC, bit 19, mask 00000110b -> `navigation`
  * Group 3000: CLOCK_CHANGE_AUTOMATIC, bit 105, mask 00100000b -> `01`

## Bundang_Thunder.xml — HU_NBT_EVO (CAFD 00001EF6, author: Bundang Thunder 3GT)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Watch video/DMB/navigation while driving (up to 63 km/h)
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3006: SPEEDLOCK_X_KMH_MAX, bit 26, mask 11111111b -> `1F`
  * Group 3006: SPEEDLOCK_X_KMH_MIN, bit 25, mask 11111111b -> `3F`

## Bundang_Thunder.xml — HU_NBT_EVO (CAFD 00001EF6, author: Bundang Thunder 3GT)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Watch video/DMB/navigation while driving 2
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: VIDEO_FRONT_LOCKED, bit 5, mask 00010000b -> `00`
  * Group 3000: VIDEO_HANDBRAKE, bit 5, mask 00000100b -> `00`
  * Group 3000: VIDEO_SPEEDLOCK_CONDITION, bit 2, mask 00000111b -> `None`

## Bundang_Thunder.xml — HU_NBT_EVO (CAFD 00001EF6, author: Bundang Thunder 3GT)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Suppress all warning messages
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3001: LEGAL_DISCLAIMER_TIME, bit 58, mask 11111111b -> `kein_ld`
  * Group 3001: MACRO_CAM_LEGALDISCLAIMER, bit 52, mask 11111111b -> `kein_ld`

## Bundang_Thunder.xml — HU_NBT_EVO (CAFD 00001EF6, author: Bundang Thunder 3GT)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Enable trailer zoom menu when reversing
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3001: MACRO_TRAILER_COUPLING, bit 54, mask 00000001b -> `01`

## Bundang_Thunder.xml — HU_NBT_EVO (CAFD 00001EF6, author: Bundang Thunder 3GT)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Close windows when it rains
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: REGEN_SCHLIESSEN, bit 19, mask 00001000b -> `01`

## Bundang_Thunder.xml — HU_NBT_EVO (CAFD 00001EF6, author: Bundang Thunder 3GT)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### X-Drive
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: COMPASS, bit 5, mask 00000001b -> `01`
  * Group 3000: X_VIEW, bit 15, mask 00000001b -> `01`
  * Group 3000: X_VIEW_GRAPHIC_SLOP, bit 26, mask 00110000b -> `trajectory1`
  * Group 3000: X_VIEW_GRAPHIC_ROLL, bit 26, mask 11000000b -> `trajectory1`
  * Group 3000: MOMENTDISTRIBUTION_MENU, bit 110, mask 00000010b -> `01`

## Bundang_Thunder.xml — HU_NBT_EVO (CAFD 00001EF6, author: Bundang Thunder 3GT)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Enable USB video playback 1/2
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: ENT_CODEC_OGG, bit 15, mask 00010000b -> `01`
  * Group 3000: ENT_CODEC_XVID, bit 15, mask 00100000b -> `01`
  * Group 3000: ENT_CODEC_VCD, bit 15, mask 01000000b -> `01`
  * Group 3000: ENT_MC_VIDEO_SUPPORT, bit 13, mask 00000100b -> `01`

## Bundang_Thunder.xml — HU_NBT_EVO (CAFD 00001EF6, author: Bundang Thunder 3GT)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Enable USB video playback 2/2
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3003: API_USB_VIDEO, bit 32, mask 00000110b -> `both`
  * Group 3003: API_IPOD_VIDEO, bit 32, mask 00011000b -> `both`

## Bundang_Thunder.xml — HU_NBT_EVO (CAFD 00001EF6, author: Bundang Thunder 3GT)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Change warning chime to Rolls-Royce sound
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3002: SOUND_SIGNAL_SET, bit 26, mask 00111000b -> `rolls_royce`

## Bundang_Thunder.xml — HU_NBT_EVO (CAFD 00001EF6, author: Bundang Thunder 3GT)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Configure Sport mode
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3008: MACRO_FDS, bit 79, mask 11000000b -> `popup_and_config`
  * Group 3009: EFF_DYN_SPORT_CID, bit 9, mask 00010000b -> `01`
  * Group 3009: EFF_DYN_SPORT_UNIT, bit 9, mask 00100000b -> `01`

## Bundang_Thunder.xml — HU_NBT_EVO (CAFD 00001EF6, author: Bundang Thunder 3GT)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Startup animation
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3001: STARTUP_TYPE, bit 62, mask 00000110b -> `animation`
  * Group 3001: STARTUP_EMBLEM, bit 62, mask 01111000b -> `variant_01`

## Bundang_Thunder.xml — HU_NBT_EVO (CAFD 00001EF6, author: Bundang Thunder 3GT)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Volume adjustment bar
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3002: VOLUME_POPUP_DISPLAY, bit 52, mask 01000000b -> `01`
  * Group 3002: VOLUME_POPUP_REJECTION, bit 52, mask 10000000b -> `01`
  * Group 3002: VOLUME_POPUP_EXCEPTION, bit 53, mask 00000001b -> `01`

## Bundang_Thunder.xml — HU_NBT_EVO (CAFD 00001EF6, author: Bundang Thunder 3GT)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Show TPMC tire pressure temperature
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3001: RDC_DRUCK_TEMP, bit 66, mask 00001100b -> `druck_und_temperatur`

## Bundang_Thunder.xml — HU_NBT_EVO (CAFD 00001EF6, author: Bundang Thunder 3GT)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Output ringtone through speakers (iPhone only)
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3003: INBAND_RINGING, bit 6, mask 10000000b -> `01`

## Bundang_Thunder.xml — HU_NBT_EVO (CAFD 00001EF6, author: Bundang Thunder 3GT)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Lock/unlock confirmation chime (requires piezo buzzer sensor)
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: ACOUSTICAL_LOCK_CONFIRM, bit 110, mask 00000001b -> `01`

## Bundang_Thunder.xml — HU_NBT_EVO (CAFD 00001EF6, author: Bundang Thunder 3GT)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Change M Sport display cluster colors
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: M_VEHICLE, bit 33, mask 01000000b -> `01`

## Bundang_Thunder.xml — HU_NBT_EVO (CAFD 00001EF6, author: Bundang Thunder 3GT)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Adjust high-beam assistant in iDrive
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: HIGH_BEAM_ASSISTANT, bit 109, mask 10000000b -> `01`

## Bundang_Thunder.xml — HU_NBT_EVO (CAFD 00001EF6, author: Bundang Thunder 3GT)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Show currently playing album art in iDrive
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: ENT_BTAS_IAP_COVERART, bit 9, mask 00000100b -> `01`
  * Group 3003: ENT_BTAS_METADATA, bit 19, mask 00000100b -> `01`
  * Group 3003: ENT_BTAS_BROWSING, bit 19, mask 00001000b -> `01`

## Bundang_Thunder.xml — HU_NBT_EVO (CAFD 00001EF6, author: Bundang Thunder 3GT)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Unlock DVD region code
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: ENT_VIDEO_DVD_AREA_CODE, bit 7, mask 11111111b -> `alle_anderen`

## Bundang_Thunder.xml — HU_NBT_EVO (CAFD 00001EF6, author: Bundang Thunder 3GT)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Show turn signals in HUD
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 300C: HUD_TURNSIGNAL, bit 0, mask 01000000b -> `01`

## Bundang_Thunder.xml — HU_NBT_EVO (CAFD 00001EF6, author: Bundang Thunder 3GT)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Set sound system to Bang & Olufsen
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: HIGH_END_AUDIO_B_UND_W, bit 21, mask 01100000b -> `keine_insz`

## Bundang_Thunder.xml — HU_NBT_EVO (CAFD 00001EF6, author: Bundang Thunder 3GT)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Enable Logic7 (S667A HiFi vehicles)
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: LOGIC7_SYMBOL, bit 22, mask 00001000b -> `01`

## Bundang_Thunder.xml — HU_NBT_EVO (CAFD 00001EF6, author: Bundang Thunder 3GT)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Enhance audio mid-bass
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3002: AUDIO_SYSTEM, bit 29, mask 00111100b -> `highpremium`
  * Group 3002: AUDIO_SYSTEM_VAR, bit 21, mask 00000011b -> `variant3`

## Bundang_Thunder.xml — ICMQL (CAFD 0000067B, author: Bundang Thunder 3GT)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Default to Eco mode at start                                                                              --** by Bundang Thunder ^^
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: IcmKod_B_InitEco, bit 36, mask 00001000b -> `verbaut`

## Bundang_Thunder.xml — ICMQL (CAFD 0000067B, author: Bundang Thunder 3GT)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Enable cruise control
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: C_Fahrfunktion, bit 128, mask 00001110b -> `01`

## Bundang_Thunder.xml — ICMQL (CAFD 0000067B, author: Bundang Thunder 3GT)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Enable Sport+ mode
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: IcmKod_B_S2TBA, bit 18, mask 11111111b -> `verbaut`

## Bundang_Thunder.xml — IHKA_VA02 (CAFD 000016EE, author: Bundang Thunder 3GT)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Remember last air conditioning state                                                                               --** by Bundang Thunder ^^
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3003: MEMORY_OFF, bit 0, mask 00000010b -> `01`

## Bundang_Thunder.xml — IHKA_VA02 (CAFD 000016EE, author: Bundang Thunder 3GT)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Prevent AUTO button from turning on A/C
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3003: AC_ON_WITH_AUTO, bit 0, mask 00000100b -> `00`

## Bundang_Thunder.xml — IHKA_VA02 (CAFD 000016EE, author: Bundang Thunder 3GT)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Remember HVAC recirculation mode
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3003: MEMORY_UMLUFT, bit 0, mask 00000001b -> `01`

## Bundang_Thunder.xml — Kafas2 (CAFD 00001148, author: Bundang Thunder 3GT)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Automatic high-beam assistant                                                                                --** by Bundang Thunder ^^
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3050: FLA_ON_OFF, bit 1, mask 00000001b -> `FLA_on`
  * Group 3050: SPEED_SWITCHING_HIGH_BEAMS_ON, bit 6, mask 11111111b -> `CN`
  * Group 3050: SPEED_SWITCHING_HIGH_BEAMS_OFF, bit 7, mask 11111111b -> `China`

## Bundang_Thunder.xml — KOMBI L7_MID (CAFD 000009C8, author: Bundang Thunder 3GT)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Show phone, entertainment, and voice prompts in HUD                                                               --** by Bundang Thunder ^^
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3003: HUD_ENTERTAINMENT_ENABLE, bit 4, mask 00000001b -> `01`
  * Group 3003: HUD_STARTUP_ENABLE, bit 5, mask 00000010b -> `01`
  * Group 3000: HUD_VZA_ENABLE, bit 42, mask 00001000b -> `01`

## Bundang_Thunder.xml — KOMBI L7_MID (CAFD 000009C8, author: Bundang Thunder 3GT)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Show turn signals in HUD
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3003: HUD_BLINKER_ENABLE, bit 4, mask 00000001b -> `01`
  * Group 3008: HUD_PIA_BLINKER, bit 5, mask 00000001b -> `01`

## Bundang_Thunder.xml — KOMBI L7_MID (CAFD 000009C8, author: Bundang Thunder 3GT)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Show logo on instrument cluster
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3003: MPM_ENABLE, bit 7, mask 00000010b -> `01`
  * Group 3000: MPM_LOGO, bit 43, mask 11110000b -> `bmw`
  * Group 3000: BMW_LOGO, bit 0, mask 00001111b -> `01`

## Bundang_Thunder.xml — KOMBI L7_MID (CAFD 000009C8, author: Bundang Thunder 3GT)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Digital speed readout in cluster
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: BC_DIGITAL_V, bit 1, mask 00000010b -> `01`

## Bundang_Thunder.xml — KOMBI L7_MID (CAFD 000009C8, author: Bundang Thunder 3GT)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Disable warning chime below 3 degrees
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: CC_TEMPERATURWARNUNG, bit 30, mask 00000001b -> `00`

## Bundang_Thunder.xml — KOMBI L7_MID (CAFD 000009C8, author: Bundang Thunder 3GT)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Show auto start/stop status in cluster
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3003: MSA_VERFUEGBARANZEIGE_ENABLE, bit 6, mask 00001000b -> `01`

## Bundang_Thunder.xml — KOMBI L7_MID (CAFD 000009C8, author: Bundang Thunder 3GT)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Use GPS time
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: GPS_UHR, bit 1, mask 10000000b -> `01`

## Bundang_Thunder.xml — KOMBI L7_MID (CAFD 000009C8, author: Bundang Thunder 3GT)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Display gear number in Dynamic Sport mode
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: SPA_SPORT_ENABLE, bit 41, mask 00010000b -> `01`

## Bundang_Thunder.xml — KOMBI L7_MID (CAFD 000009C8, author: Bundang Thunder 3GT)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Enable Sport+ menu in cluster
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 300C: FDS_MENUE_TEXT_1, bit 0, mask 00001111b -> `menue_3`
  * Group 300C: FDS_MENUE_SIGNAL_1, bit 0, mask 11110000b -> `menue_3`
  * Group 300C: FDS_MENUE_TEXT_2, bit 1, mask 00001111b -> `menue_3`
  * Group 300C: FDS_MENUE_SIGNAL_2, bit 1, mask 11110000b -> `menue_3`
  * Group 300C: FDS_MENUE_TEXT_3, bit 2, mask 00001111b -> `menue_3`
  * Group 300C: FDS_MENUE_SIGNAL_3, bit 2, mask 11110000b -> `menue_3`
  * Group 300C: FDS_MENUE_TEXT_4, bit 3, mask 00001111b -> `menue_3`
  * Group 300C: FDS_MENUE_SIGNAL_4, bit 3, mask 11110000b -> `menue_3`
  * Group 300C: FDS_MENUE, bit 54, mask 11111111b -> `menue_3`

## Bundang_Thunder.xml — CFAS_PLX_1 (CAFD 000000B5, author: Bundang Thunder 3GT)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Enable Easy Access                                                                         --** by Bundang Thunder ^^
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: EINAUSSTIEGSHILFE, bit 0, mask 00011100b -> `Modus_FA_SLV`

## Bundang_Thunder.xml — CFAS_PLX_1 (CAFD 000000B5, author: Bundang Thunder 3GT)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Easy Access seat starts moving from end position
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3012: EAH_SCHUTZFREIRAUM_HINTEN_SLV_PHYS, bits 4-5, mask 11111111b -> `00, 01`

## Bundang_Thunder.xml — CFAS_PLX_1 (CAFD 000000B5, author: Bundang Thunder 3GT)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Easy Access seat starts moving with 1 cm remaining
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3012: EAH_SCHUTZFREIRAUM_HINTEN_SLV_PHYS, bits 4-5, mask 11111111b -> `00, 0A`

## Bundang_Thunder.xml — CFAS_PLX_1 (CAFD 000000B5, author: Bundang Thunder 3GT)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Easy Access seat starts moving with 2 cm remaining
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3012: EAH_SCHUTZFREIRAUM_HINTEN_SLV_PHYS, bits 4-5, mask 11111111b -> `00, 14`

## Bundang_Thunder.xml — CFAS_PLX_1 (CAFD 000000B5, author: Bundang Thunder 3GT)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Easy Access seat starts moving with 3 cm remaining
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3012: EAH_SCHUTZFREIRAUM_HINTEN_SLV_PHYS, bits 4-5, mask 11111111b -> `00, 1E`

## Bundang_Thunder.xml — CFAS_PLX_1 (CAFD 000000B5, author: Bundang Thunder 3GT)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Easy Access seat travel distance: 4 cm
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3012: EAH_VERFAHRWEG_SLV_PHYS, bits 2-3, mask 11111111b -> `00, 28`

## Bundang_Thunder.xml — CFAS_PLX_1 (CAFD 000000B5, author: Bundang Thunder 3GT)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Easy Access seat travel distance: 5 cm
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3012: EAH_VERFAHRWEG_SLV_PHYS, bits 2-3, mask 11111111b -> `00, 32`

## Bundang_Thunder.xml — CFAS_PLX_1 (CAFD 000000B5, author: Bundang Thunder 3GT)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Easy Access seat travel distance: 6 cm
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3012: EAH_VERFAHRWEG_SLV_PHYS, bits 2-3, mask 11111111b -> `00, 3C`

## Bundang_Thunder.xml — CFAS_PLX_1 (CAFD 000000B5, author: Bundang Thunder 3GT)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Easy Access seat travel distance: 7 cm
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3012: EAH_VERFAHRWEG_SLV_PHYS, bits 2-3, mask 11111111b -> `00, 46`

## Bundang_Thunder.xml — CFAS_PLX_1 (CAFD 000000B5, author: Bundang Thunder 3GT)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Gentleman
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: GENTLEMAN, bit 1, mask 00000001b -> `01`
  * Group 3000: MEMORY, bit 0, mask 00000001b -> `01`

## Bundang_Thunder.xml — CFAS_PLX_1 (CAFD 000000B5, author: Bundang Thunder 3GT)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Set gong when saving seat position
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: MEMORY_GONG, bit 2, mask 00001000b -> `01`

## Bundang_Thunder.xml — CBFS_PLX_1 (CAFD 000000B6, author: Bundang Thunder 3GT)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Gentleman                                                                                                --** by Bundang Thunder ^^
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: GENTLEMAN, bit 1, mask 00000001b -> `01`
  * Group 3000: MEMORY, bit 0, mask 00000001b -> `01`

## Bundang_Thunder.xml — TRSVC (CAFD 00000223, author: Bundang Thunder 3GT)

**Module series coverage:** F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

### Allow side view at any time                                                                   --** by Bundang Thunder ^^
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: SV_Activate_Speed_Limit, bit 114, mask 11111111b -> `FF`
  * Group 3000: SV_Deactivate_Speed, bit 115, mask 11111111b -> `FF`

## Kip_M3.xml — ICMQL (CAFD 0000067B, author: Kip_M3)

**Module series coverage:** F808,F082

### Enable speed limiter (also need to code KOMBI)
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: C_SLD_Funktion, bit 173, mask 00000001b -> `aktiv`
  * Group 3000: C_Umschaltung_ACC_DCC, bit 197, mask 11100000b -> `zugelassen`

## Kip_M3.xml — TMS_03 (CAFD 00001082, author: Kip_M3)

**Module series coverage:** F03X,F08X

### Turn sidemarker LEDs OFF - Driver side. Step 1 of 2(need to test)
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3005: Turn sidemarker LEDs OFF, bits 16-31, mask 11111111b -> `00, 03, 00, 00, 00, 03, 00, 00, 64, 03, 00, 00, 2B, 04, 00, 00`
  * Group 3005: Turn sidemarker LEDs OFF, bits 32-47, mask 11111111b -> `00, 03, 00, 00, 00, 03, 00, 00, 64, 03, 00, 00, 2B, 04, 00, 00`
  * Group 3005: Turn sidemarker LEDs OFF, bits 80-95, mask 11111111b -> `00, 03, 00, 00, 00, 03, 00, 00, 64, 03, 00, 00, 2E, 04, 00, 00`

## Kip_M3.xml — TMS_03 (CAFD 00001082, author: Kip_M3)

**Module series coverage:** F03X,F08X

### Turn sidemarker LEDs ON - Driver side. Step 1 of 2(need to test)
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3005: Turn sidemarker LEDs ON, bits 16-31, mask 11111111b -> `00, 03, 00, 00, 64, 03, 00, 00, 64, 03, 00, 00, 2B, 04, 00, 00`
  * Group 3005: Turn sidemarker LEDs ON, bits 32-47, mask 11111111b -> `00, 03, 00, 00, 64, 03, 00, 00, 64, 03, 00, 00, 2B, 04, 00, 00`
  * Group 3005: Turn sidemarker LEDs ON, bits 80-95, mask 11111111b -> `00, 03, 00, 00, 64, 03, 00, 00, 64, 03, 00, 00, 2E, 04, 00, 00`

## Kip_M3.xml — TMS_03 (CAFD 00001083, author: Kip_M3)

**Module series coverage:** F03X,F08X

### Turn sidemarker LEDs OFF - Passenger side. Step 2 of 2(need to test)
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3005: Turn sidemarker LEDs OFF, bits 16-31, mask 11111111b -> `00, 03, 00, 00, 00, 03, 00, 00, 64, 03, 00, 00, 2B, 04, 00, 00`
  * Group 3005: Turn sidemarker LEDs OFF, bits 32-47, mask 11111111b -> `00, 03, 00, 00, 00, 03, 00, 00, 64, 03, 00, 00, 2B, 04, 00, 00`
  * Group 3005: Turn sidemarker LEDs OFF, bits 80-95, mask 11111111b -> `00, 03, 00, 00, 00, 03, 00, 00, 64, 03, 00, 00, 2E, 04, 00, 00`

## Kip_M3.xml — TMS_03 (CAFD 00001083, author: Kip_M3)

**Module series coverage:** F03X,F08X

### Turn sidemarker LEDs ON - Passenger side. Step 2 of 2(need to test)
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3005: Turn sidemarker LEDs ON, bits 16-31, mask 11111111b -> `00, 03, 00, 00, 64, 03, 00, 00, 64, 03, 00, 00, 2B, 04, 00, 00`
  * Group 3005: Turn sidemarker LEDs ON, bits 32-47, mask 11111111b -> `00, 03, 00, 00, 64, 03, 00, 00, 64, 03, 00, 00, 2B, 04, 00, 00`
  * Group 3005: Turn sidemarker LEDs ON, bits 80-95, mask 11111111b -> `00, 03, 00, 00, 64, 03, 00, 00, 64, 03, 00, 00, 2E, 04, 00, 00`

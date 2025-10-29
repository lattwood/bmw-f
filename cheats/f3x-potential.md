# F3x-Potential Cheat Codes

These presets target closely related F-series chassis (primarily F2x 1/2 Series and
other shared-module vehicles). They are likely to work on an F3x thanks to common
control units, but the original XML does not explicitly declare F3x coverage. Review
and test carefully before applying them to an F3x vehicle.

## Almaretto.xml — IHKA_VA02 (CAFD 000016EE, author: Almaretto)

**Module series coverage:** F020,F020,I001

### ENABLE HVAC memory - A/C stay OFF if OFF at vehicle shutdown
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3003: MEMORY_OFF, bit 0, mask 00000010b -> `aktiv`

## Almaretto.xml — IHKA_VA02 (CAFD 000016EE, author: Almaretto)

**Module series coverage:** F020,F020,I001

### ENABLE Air Re-Circulation memory - Remembers shutdown Setting
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3003: MEMORY_UMLUFT, bit 0, mask 00000001b -> `aktiv`

## Almaretto.xml — IHKA_VA02 (CAFD 000016EE, author: Almaretto)

**Module series coverage:** F020,F020,I001

### DISABLE A/C from turning ON if Auto Button is pressed
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3003: bit 0, mask 00000100b -> `aktiv`

## Almaretto.xml — HKFM (CAFD 000007C8, author: Almaretto)

**Module series coverage:** F001,F010,F015,F025,F030,F045

### ENABLE Trunk Close via keyFOB/Footwell button (NA vehicles)
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3010: bit 0, mask 00001000b -> `aktiv`
  * Group 3010: bit 2, mask 00000100b -> `aktiv`
  * Group 3010: bit 2, mask 00001000b -> `aktiv`

## Almaretto.xml — KOMBI L7_MID (CAFD 000009C8, author: Almaretto)

**Module series coverage:** F020,F030

### Trip Computer Auto Reset (Never)
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: BC_AUTORESET_ZEIT, bit 44, mask 11111111b -> `FF`

## Almaretto.xml — KOMBI L7_MID (CAFD 000009C8, author: Almaretto)

**Module series coverage:** F020,F030

### Trip Computer Auto Reset (0 Hours)
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: BC_AUTORESET_ZEIT, bit 44, mask 11111111b -> `00`

## Almaretto.xml — KOMBI L7_MID (CAFD 000009C8, author: Almaretto)

**Module series coverage:** F020,F030

### DISABLE Digital Speed Display in Cluster
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: BC_DIGITAL_V, bit 1, mask 00000010b -> `nicht_aktiv`

## Almaretto.xml — KOMBI L7_MID (CAFD 000009C8, author: Almaretto)

**Module series coverage:** F020,F030

### ENABLE Digital Speed Display in Cluster
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: BC_DIGITAL_V, bit 1, mask 00000010b -> `aktiv`

## Almaretto.xml — KOMBI L7_MID (CAFD 000009C8, author: Almaretto)

**Module series coverage:** F020,F030

### ENABLE Speed Correction
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: bit 1, mask 01000000b -> `Aktiv`

## Almaretto.xml — KOMBI L7_MID (CAFD 000009C8, author: Almaretto)

**Module series coverage:** F020,F030

### DISABLE Speed Correction
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: bit 1, mask 01000000b -> `nicht_aktiv`

## Almaretto.xml — KOMBI L7_MID (CAFD 000009C8, author: Almaretto)

**Module series coverage:** F020,F030

### DISABLE Auto Start Stop notificaiton in Cluster
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3003: bit 6, mask 00001000b -> `nicht_aktiv`

## Almaretto.xml — KOMBI L7_MID (CAFD 000009C8, author: Almaretto)

**Module series coverage:** F020,F030

### ENABLE Day White Instrument Cluster at night
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3007: bit 10, mask 11111111b -> `FF`

## Almaretto.xml — KOMBI L7_MID (CAFD 000009C8, author: Almaretto)

**Module series coverage:** F020,F030

### ENABLE LIM Function. Part 1 of 2. See ICM
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3003: bit 3, mask 00000001b -> `aktiv`

## Almaretto.xml — KOMBI L7_MID (CAFD 000009C8, author: Almaretto)

**Module series coverage:** F020,F030

### Changes M3/M4 Instrument Cluster Startup Logo to GTS
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: bit 0, mask 11110000b -> `0C`

## Almaretto.xml — KOMBI L7_MID (CAFD 000009C8, author: Almaretto)

**Module series coverage:** F020,F030

### ENABLE Night Vision with Background Pedestrian Detection. Part 1 of 2. See NIVI
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3003: FGS_NIVI_KI_ENABLE, bit 7, mask 00001000b -> `aktiv`

## Almaretto.xml — FRM_03CT (CAFD 0000106D, author: Almaretto)

**Module series coverage:** F025

### F25 NGHB. Part 3 of 3. See LHM43/LHM44. Step 3 of PDF
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3080: LAMP_MAP_PARA_SATZ_09, bits 32-35, mask 11111111b -> `00, 00, 00, 00`
  * Group 3080: LAMP_MAP_PARA_SATZ_10, bits 36-39, mask 11111111b -> `00, 00, 00, 00`

## Almaretto.xml — LHM2 (CAFD 000010BA, author: Almaretto)

**Module series coverage:** F025

### F25 NGHB. Part 1 of 3. See LHM44/FRM. Step 2 of PDF
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: M1, bits 0-6, mask 11111111b -> `FA, 64, 00, 00, FA, FA, 00`
  * Group 3000: M2, bits 7-13, mask 11111111b -> `FA, 64, 00, 00, FA, FA, 00`
  * Group 3000: M3, bits 14-20, mask 11111111b -> `FA, 00, 00, 00, FA, FA, 00`
  * Group 3000: M4, bits 21-27, mask 11111111b -> `FA, 00, 00, 00, C8, C8, 00`
  * Group 3000: M14, bits 91-97, mask 11111111b -> `FA, 00, 00, FA, FA, FA, 00`
  * Group 3000: M15, bits 98-104, mask 11111111b -> `FA, FA, 00, FA, FA, FA, FA`

## Almaretto.xml — LHM2 (CAFD 000016BF, author: Almaretto)

**Module series coverage:** F025

### F25 NGHB. Part 2 of 3. See LHM43/FRM. Step 2 of PDF
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: M1, bits 0-6, mask 11111111b -> `FA, FA, 00, 00, FA, FA, 00`
  * Group 3000: M2, bits 7-13, mask 11111111b -> `FA, FA, 00, 00, FA, FA, 00`
  * Group 3000: M3, bits 14-20, mask 11111111b -> `FA, FA, 00, 00, FA, FA, 00`
  * Group 3000: M4, bits 21-27, mask 11111111b -> `FA, 00, 00, 00, C8, C8, 00`
  * Group 3000: M6, bits 35-41, mask 11111111b -> `FA, FA, 00, 00, FA, FA, 00`
  * Group 3000: M7, bits 42-48, mask 11111111b -> `FA, FA, 00, 00, FA, FA, 00`
  * Group 3000: M8, bits 49-55, mask 11111111b -> `FA, FA, 00, 00, FA, FA, 00`
  * Group 3000: M9, bits 56-62, mask 11111111b -> `FA, FA, 00, 00, FA, FA, 00`
  * Group 3000: M14, bits 91-97, mask 11111111b -> `FA, FA, 00, FA, FA, FA, 00`
  * Group 3000: M15, bits 98-104, mask 11111111b -> `FA, FA, 00, FA, FA, FA, FA`

## Botho.xml — ACSM_4B (CAFD 00000911, author: Botho (public))

**Module series coverage:** F020,F030

### Seat belt: reminder duration set to 10s (default: 100s)
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3001: GWF_SBR_WARNDAUER (default: 64), bit 3, mask 11111111b -> `0A`

## Botho.xml — ACSM_4B (CAFD 00000911, author: Botho (public))

**Module series coverage:** F020,F030

### Seat belt: disable reminder chime
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: SeatBeltReminder_SBR_Fahrer (default: aktiv), bit 15, mask 00000100b -> `nicht_aktiv`
  * Group 3000: SeatBeltReminder_SBR_Beifahrer (default: aktiv), bit 15, mask 00000010b -> `nicht_aktiv`

## Botho.xml — ACSM_4B (CAFD 00000911, author: Botho (public))

**Module series coverage:** F020,F030

### Seat belt: disable indicator in instrument cluster
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: Gurtzustandsanzeige_Fahrer_GWF_GZA_FA (default: aktiv), bit 15, mask 00010000b -> `nicht_aktiv`
  * Group 3000: Gurtzustandsanzeige_Beifahrer_GWF_GZA_BF (default: aktiv), bit 15, mask 00001000b -> `nicht_aktiv`

## Botho.xml — ACSM_4B (CAFD 00000911, author: Botho (public))

**Module series coverage:** F020,F030

### Seat belt: disable chime when belt is unlatched
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: SBR_PreWarning_Fahrer (default: aktiv), bit 16, mask 00000001b -> `nicht_aktiv`
  * Group 3000: SBR_PreWarning_Beifahrer (default: aktiv), bit 16, mask 00000010b -> `nicht_aktiv`

## Botho.xml — GKEB23 (CAFD 0000023F, author: Botho (public))

**Module series coverage:** F020,F030

### Activation Launch Control (default: aktiv)
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: LC (default: 01), bit 1, mask 10000000b -> `01`

## Botho.xml — FEM_01 (CAFD 00000794, author: Botho (public))

**Module series coverage:** F020,F030

### Vitres avant: actives lors de l'ouverture des portes avant
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3050: FH_TUERAUF_STOP_MAUT (default: aktiv), bit 0, mask 00000001b -> `nicht_aktiv`

## Botho.xml — FEM_01 (CAFD 00000794, author: Botho (public))

**Module series coverage:** F020,F030

### Comfort access: auto-lock delay to 30s without door action (default: 120s)
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3040: CLM_TIME_PIA_LOCK_AT_TIMEOUT (default: 0C), bit 7, mask 11111111b -> `03`

## Botho.xml — FEM_01 (CAFD 00000794, author: Botho (public))

**Module series coverage:** F020,F030

### Comfort access: enable panic alarm and set remote hold time to 500ms (SHORT=Follow-Me-Home; MID=Trunk; LONG=Panic Alarm)
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 30D0: RC_PANIC_ALARM (default: nicht_aktiv), bit 2, mask 00000100b -> `aktiv`
  * Group 30D0: RC_DEFAULT_IDG_3RD_BUTTON_SHORT (default: 00), bit 3, mask 00001111b -> `04`
  * Group 30D0: RC_DEFAULT_IDG_3RD_BUTTON_MID (default: 02), bit 3, mask 11110000b -> `02`
  * Group 30D0: RC_DEFAULT_IDG_3RD_BUTTON_LONG (default: 02), bit 4, mask 00001111b -> `03`
  * Group 30D0: RC_TIME_DELAY_BOOTLID (default: 05), bit 8, mask 11111111b -> `14`
  * Group 30D0: RC_TIME_DELAY_PANIC (default: 14), bit 9, mask 11111111b -> `28`

## Botho.xml — FEM_01 (CAFD 00000794, author: Botho (public))

**Module series coverage:** F020,F030

### Comfort access: open flash count = 3 (default: 2)
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3060: QUITTBLK_ENTSCHAERFEN_ANZAHL (default: 02), bit 6, mask 00001100b -> `03`

## Botho.xml — FEM_01 (CAFD 00000794, author: Botho (public))

**Module series coverage:** F020,F030

### Comfort access: close flash count = 2 (default: 1)
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3060: QUITTBLK_SICHERN_ANZAHL (default: 01), bit 6, mask 00000011b -> `02`

## Botho.xml — FEM_01 (CAFD 00000794, author: Botho (public))

**Module series coverage:** F020,F030

### Comfort access: enable comfort closing after 1s (default: 1.5s)
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3053: KOMFORT_SCHLIESSEN (default: 0F), bit 9, mask 11111111b -> `0A`

## Botho.xml — FEM_01 (CAFD 00000794, author: Botho (public))

**Module series coverage:** F020,F030

### Comfort access: enable comfort opening after 2s (default: 2.5s)
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3053: KOMFORT_OEFFNEN (default: 19), bit 8, mask 11111111b -> `14`

## Botho.xml — FEM_01 (CAFD 00000794, author: Botho (public))

**Module series coverage:** F020,F030

### Comfort access: close trunk with foot (requires 322, 316) (step 1 of 2 - see HKFM)
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3030: CAM_SMART_CLOSER (default: aktiv si production date après 0315), bit 5, mask 00000110b -> `aktiv`

## Botho.xml — FEM_01 (CAFD 00000794, author: Botho (public))

**Module series coverage:** F020,F030

### Comfort access: trunk opening delay (smart opening only) to 0.3s (default 0.7s)
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3040: CLM_TIMEOUT_HK_SMO (default: wert_03), bit 12, mask 11111111b -> `wert_02`

## Botho.xml — FEM_01 (CAFD 00000794, author: Botho (public))

**Module series coverage:** F020,F030

### Comfort access: trunk opening delay (no smart opening) to 0.1s (default 0.3s)
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3040: CLM_TIME_DELAY_BOOTLID (default: wert_02), bit 6, mask 11111111b -> `wert_01`

## Botho.xml — FEM_01 (CAFD 00000794, author: Botho (public))

**Module series coverage:** F020,F030

### Comfort access: disable turn signals when opening trunk (default: enabled)
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3040: CLM_SMO_INDICATOR (default: aktiv), bit 2, mask 00000100b -> `nicht_aktiv`

## Botho.xml — FEM_01 (CAFD 00000794, author: Botho (public))

**Module series coverage:** F020,F030

### Door locking: speed threshold to 8 km/h (only if auto-lock enabled - default 16 km/h)
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3040: CLM_SPEED_LIMIT_PIA_AUTO_LOCK (default: wert_04), bit 8, mask 11111111b -> `wert_03`

## Botho.xml — FEM_01 (CAFD 00000794, author: Botho (public))

**Module series coverage:** F020,F030

### Unlock doors when engine stops (only if auto-lock enabled)
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3040: CLM_UNLOCK_KL15OFF_AFTER_PIA_AUTO_LOCK (default: aktiv), bit 1, mask 00000010b -> `aktiv`

## Botho.xml — FEM_01 (CAFD 00000794, author: Botho (public))

**Module series coverage:** F020,F030

### Angel Eyes (DRL): Activation des feux de jour (Step 1 sur 3 - voir HU-NBT and REM)
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3060: TFL_MODUS (default: 02), bit 31, mask 00110000b -> `02`

## Botho.xml — FEM_01 (CAFD 00000794, author: Botho (public))

**Module series coverage:** F020,F030

### Angel Eyes (DRL): set DRL brightness to 50% when xenons are on
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3062: MAPPING_STANDL_V_L_PWM_LEVEL_STANDARD (default: 8), bit 46, mask 11111111b -> `32`
  * Group 3062: MAPPING_STANDL_V_R_PWM_LEVEL_STANDARD (default: 8), bit 57, mask 11111111b -> `32`

## Botho.xml — FEM_01 (CAFD 00000794, author: Botho (public))

**Module series coverage:** F020,F030

### Angel Eyes (DRL): set DRL brightness to 100% when xenons are on
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3062: MAPPING_STANDL_V_L_PWM_LEVEL_STANDARD (default: 8), bit 46, mask 11111111b -> `64`
  * Group 3062: MAPPING_STANDL_V_R_PWM_LEVEL_STANDARD (default: 8), bit 57, mask 11111111b -> `64`

## Botho.xml — FEM_01 (CAFD 00000794, author: Botho (public))

**Module series coverage:** F020,F030

### Angel Eyes (DRL): set DRL brightness to 50% when DRLs are on
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3062: MAPPING_TAGFAHRL_V_L_PWM_LEVEL_1 (default: 64), bit 90, mask 11111111b -> `32`
  * Group 3062: MAPPING_TAGFAHRL_V_R_PWM_LEVEL_1 (default: 64), bit 101, mask 11111111b -> `32`

## Botho.xml — FEM_01 (CAFD 00000794, author: Botho (public))

**Module series coverage:** F020,F030

### Angel Eyes (DRL): set DRL brightness to 100% when DRLs are on
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3062: MAPPING_TAGFAHRL_V_L_PWM_LEVEL_1 (default: 64), bit 90, mask 11111111b -> `64`
  * Group 3062: MAPPING_TAGFAHRL_V_R_PWM_LEVEL_1 (default: 64), bit 101, mask 11111111b -> `64`

## Botho.xml — FEM_01 (CAFD 00000794, author: Botho (public))

**Module series coverage:** F020,F030

### Xenon: enable cornering lights (fog lights required)
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3073: C_CLC_ENA (default: 01), bit 218, mask 00000010b -> `01`
  * Group 3073: C_BLC_ENA (default: 01), bit 66, mask 00000001b -> `01`
  * Group 3066: KL_ENABLE_LI (default: 01), bit 0, mask 00000001b -> `01`
  * Group 3066: KL_ENABLE_RE (default: 01), bit 80, mask 00000001b -> `01`
  * Group 3062: MAPPING_ABBIEGEL_L_OUTPUT (default: 0B), bit 110, mask 00111111b -> `0B`
  * Group 3062: MAPPING_ABBIEGEL_R_OUTPUT (default: 0C), bit 121, mask 00111111b -> `0C`

## Botho.xml — FEM_01 (CAFD 00000794, author: Botho (public))

**Module series coverage:** F020,F030

### Xenon: enable US daytime running sidemarkers
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3063: MAPPING_SIDEMARKER_L_OUTPUT (default: off), bit 11, mask 00111111b -> `fra_v_l`
  * Group 3063: MAPPING_SIDEMARKER_R_OUTPUT (default: off), bit 22, mask 00111111b -> `fra_v_r`
  * Group 3063: MAPPING_SIDEMARKER_L_FUNCTION (default: 01), bit 12, mask 00011111b -> `04`
  * Group 3063: MAPPING_SIDEMARKER_R_FUNCTION (default: 01), bit 23, mask 00011111b -> `04`
  * Group 3063: MAPPING_SIDEMARKER_L_PWM_LEVEL_STANDARD (default: off), bit 13, mask 11111111b -> `8.2V`
  * Group 3063: MAPPING_SIDEMARKER_R_PWM_LEVEL_STANDARD (default: off), bit 24, mask 11111111b -> `8.2V`

## Botho.xml — FEM_01 (CAFD 00000794, author: Botho (public))

**Module series coverage:** F020,F030

### Front light cleaning (Disable)
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3080: WW_SCHEINWERFERREINIGUNG (default: aktiv), bit 8, mask 00000001b -> `nicht_aktiv`

## Botho.xml — FEM_01 (CAFD 00000794, author: Botho (public))

**Module series coverage:** F020,F030

### Front light cleaning (Enable - Default)
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3080: WW_SCHEINWERFERREINIGUNG (default: aktiv), bit 8, mask 00000001b -> `aktiv`

## Botho.xml — FEM_01 (CAFD 00000794, author: Botho (public))

**Module series coverage:** F020,F030

### Front light cleaning: Sprays number (2 - Default)
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3080: WW_ANZAHL_SPRITZIMPULSE_SRA (default: 02), bit 8, mask 00011000b -> `02`

## Botho.xml — FEM_01 (CAFD 00000794, author: Botho (public))

**Module series coverage:** F020,F030

### Front light cleaning: Sprays number (3)
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3080: WW_ANZAHL_SPRITZIMPULSE_SRA (default: 02), bit 8, mask 00011000b -> `03`

## Botho.xml — FEM_01 (CAFD 00000794, author: Botho (public))

**Module series coverage:** F020,F030

### Front light cleaning: Wash cycles to enable next washing (10 - Default)
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3080: WW_ANZAHL_WASCHBET_ZUR_SRA (default: 0A), bit 2, mask 00011110b -> `0A`

## Botho.xml — FEM_01 (CAFD 00000794, author: Botho (public))

**Module series coverage:** F020,F030

### Front light cleaning: Wash cycles to enable next washing (5)
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3080: WW_ANZAHL_WASCHBET_ZUR_SRA (default: 0A), bit 2, mask 00011110b -> `05`

## Botho.xml — FEM_01 (CAFD 00000794, author: Botho (public))

**Module series coverage:** F020,F030

### Front light cleaning: Time to wait before next washing (10 mins - Default)
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3080: WW_SRA_SPERRZEIT (default: 0A), bit 10, mask 00001111b -> `0A`

## Botho.xml — FEM_01 (CAFD 00000794, author: Botho (public))

**Module series coverage:** F020,F030

### Front light cleaning: Time to wait before next washing (3 mins)
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3080: WW_SRA_SPERRZEIT (default: 0A), bit 10, mask 00001111b -> `03`

## Botho.xml — FEM_01 (CAFD 00000794, author: Botho (public))

**Module series coverage:** F020,F030

### Front light cleaning: Time to wait before next washing (5 mins)
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3080: WW_SRA_SPERRZEIT (default: 0A), bit 10, mask 00001111b -> `05`

## Botho.xml — FEM_01 (CAFD 00000794, author: Botho (public))

**Module series coverage:** F020,F030

### Automatic rear wiper in reverse (Enable - Default)
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3080: WW_HECKWISCHER_EIN_RUECKWGANG (default: aktiv), bit 0, mask 10000000b -> `aktiv`

## Botho.xml — FEM_01 (CAFD 00000794, author: Botho (public))

**Module series coverage:** F020,F030

### Automatic rear wiper in reverse (Disable)
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3080: WW_HECKWISCHER_EIN_RUECKWGANG (default: aktiv), bit 0, mask 10000000b -> `nicht_aktiv`

## Botho.xml — FEM_01 (CAFD 00000794, author: Botho (public))

**Module series coverage:** F020,F030

### Rear wiper: Wipe cycles after washing (1)
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3080: WW_ANZAHL_NACHWISCHZ_HECK (default: 02), bit 8, mask 11100000b -> `01`

## Botho.xml — FEM_01 (CAFD 00000794, author: Botho (public))

**Module series coverage:** F020,F030

### Rear wiper: Wipe cycles after washing (2 - Default)
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3080: WW_ANZAHL_NACHWISCHZ_HECK (default: 02), bit 8, mask 11100000b -> `02`

## Botho.xml — FEM_01 (CAFD 00000794, author: Botho (public))

**Module series coverage:** F020,F030

### Rear wiper: Wipe cycles after washing (3)
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3080: WW_ANZAHL_NACHWISCHZ_HECK (default: 02), bit 8, mask 11100000b -> `03`

## Botho.xml — FEM_01 (CAFD 00000794, author: Botho (public))

**Module series coverage:** F020,F030

### Rear wiper: Wipe cycles after washing (4)
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3080: WW_ANZAHL_NACHWISCHZ_HECK (default: 02), bit 8, mask 11100000b -> `04`

## Botho.xml — FEM_01 (CAFD 00000794, author: Botho (public))

**Module series coverage:** F020,F030

### Front wiper: Wipe cycles after rear washing (1)
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3080: WW_ANZAHL_NACHWISCHZ_FRONT (default: 03), bit 18, mask 01110000b -> `01`

## Botho.xml — FEM_01 (CAFD 00000794, author: Botho (public))

**Module series coverage:** F020,F030

### Front wiper: Wipe cycles after rear washing (2)
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3080: WW_ANZAHL_NACHWISCHZ_FRONT (default: 03), bit 18, mask 01110000b -> `02`

## Botho.xml — FEM_01 (CAFD 00000794, author: Botho (public))

**Module series coverage:** F020,F030

### Front wiper: Wipe cycles after washing (3 - Default)
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3080: WW_ANZAHL_NACHWISCHZ_FRONT (default: 03), bit 18, mask 01110000b -> `03`

## Botho.xml — FEM_01 (CAFD 00000794, author: Botho (public))

**Module series coverage:** F020,F030

### Front wiper: Wipe cycles after rear washing (4)
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3080: WW_ANZAHL_NACHWISCHZ_FRONT (default: 03), bit 18, mask 01110000b -> `04`

## Botho.xml — FEM_01 (CAFD 00000794, author: Botho (public))

**Module series coverage:** F020,F030

### Mirrors: allow folding below 49 km/h (default: 20 km/h)
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3110: ASP_MAX_GESCHWINDIGKEIT_BEIKLAPPEN (default: 14), bit 9, mask 11111111b -> `31`

## Botho.xml — FEM_01 (CAFD 00000794, author: Botho (public))

**Module series coverage:** F020,F030

### Mirrors: auto unfold from 50 km/h (default: 40 km/h)
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3110: ASP_GESCHWINDIGKEIT_AUTO_AUSKLAPPEN (default: 28), bit 10, mask 11111111b -> `32`

## Botho.xml — FEM_01 (CAFD 00000794, author: Botho (public))

**Module series coverage:** F020,F030

### Passenger mirror: increase reverse tilt to 70 digits (default: 59 digits - I-Step after 3.61.x)
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3110: ASP_BORDSTEINAUTOMATIK_DELTA (default: 3B), bit 2, mask 11111111b -> `46`

## Botho.xml — FEM_01 (CAFD 00000794, author: Botho (public))

**Module series coverage:** F020,F030

### Passenger mirror: restore reverse tilt to 59 digits (default: 59 digits - I-Step after 3.61.x)
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3110: ASP_BORDSTEINAUTOMATIK_DELTA (default: 3B), bit 2, mask 11111111b -> `3B`

## Botho.xml — FEM_01 (CAFD 00000794, author: Botho (public))

**Module series coverage:** F020,F030

### Turn signals: set flash count to 5 (default: 00 - I-Step before 3.61.x)
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3060: BLINKZYKLEN_ANZAHL_TIPP (default: 00), bit 7, mask 00000111b -> `04`

## Botho.xml — FEM_01 (CAFD 00000794, author: Botho (public))

**Module series coverage:** F020,F030

### -- Don't work -- Turn signals: set flash count to 5 (00 = 1, 01 = 3, 02 = 5; default: 01 - I-Step after 3.61.x)
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3064: PIA_DEFAULT_TIPPBLINKEN (default: 01), bit 215, mask 00000001b -> `02`

## Botho.xml — FEM_01 (CAFD 00000794, author: Botho (public))

**Module series coverage:** F020,F030

### Turn signals: single flash when opening tailgate (default: double)
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3060: HECKKLAPPE_REVERSIEREN_BLINKEN (default: 01), bit 6, mask 10000000b -> `00`

## Botho.xml — FEM_01 (CAFD 00000794, author: Botho (public))

**Module series coverage:** F020,F030

### Rear fog lights: activation (step 2 of 2 - see REM_01)
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3060: NSL_VERBAUT (default: 01), bit 7, mask 00001000b -> `01`

## Botho.xml — FEM_01 (CAFD 00000794, author: Botho (public))

**Module series coverage:** F020,F030

### Rear fog lights: deactivation (step 2 of 2 - see REM_01)
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3060: NSL_VERBAUT (default: 01), bit 7, mask 00001000b -> `00`

## Botho.xml — FEM_01 (CAFD 00000794, author: Botho (public))

**Module series coverage:** F020,F030

### Fog lights: allow fogs to stay on with high beams
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3060: NSW_AUS_BEI_FL (default: 00), bit 20, mask 00100000b -> `00`

## Botho.xml — FEM_01 (CAFD 00000794, author: Botho (public))

**Module series coverage:** F020,F030

### Fog lights: allow fogs to stay on with parking lights
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3060: NSW_EIN_AUF_LDS_STL (default: 00 dans certains pays comme les USA), bit 29, mask 01000000b -> `01`

## Botho.xml — FEM_01 (CAFD 00000794, author: Botho (public))

**Module series coverage:** F020,F030

### Feux anti-brouillard: active cornering lights
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3073: C_CLC_ENA (default: F020_enable), bit 218, mask 00000010b -> `F020_enable`
  * Group 3073: C_BLC_ENA (default: F020_enable), bit 66, mask 00000001b -> `F020_enable`
  * Group 3066: KL_ENABLE_LI (default: KL_Ein), bit 0, mask 00000001b -> `KL_Ein`
  * Group 3066: KL_ENABLE_RE (default: KL_Ein), bit 80, mask 00000001b -> `KL_Ein`
  * Group 3062: MAPPING_ABBIEGEL_L_OUTPUT (default: nsw_l), bit 110, mask 00111111b -> `nsw_l`
  * Group 3062: MAPPING_ABBIEGEL_R_OUTPUT (default: nsw_r), bit 121, mask 00111111b -> `nsw_r`

## Botho.xml — FEM_01 (CAFD 00000794, author: Botho (public))

**Module series coverage:** F020,F030

### High-Beam Assistant motorway (HBA): activate immediately from 120 km/h (default: 140 km/h) or between 90-110 km/h for 15s (default: 30s)
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3074: C_HBA_HGWY_V_LO (default: 5A - 90 km/h), bit 5, mask 11111111b -> `5A`
  * Group 3074: C_HBA_HGWY_V_HI (default: 8C - 140 km/h), bit 6, mask 11111111b -> `82`
  * Group 3074: C_HBA_HGWY_V_MIN (default: 6E - 110 km/h), bit 7, mask 11111111b -> `6E`
  * Group 3074: C_HBA_HGWY_T_MIN (default: 1E - 30 sec), bit 8, mask 11111111b -> `0F`

## Botho.xml — FEM_01 (CAFD 00000794, author: Botho (public))

**Module series coverage:** F020,F030

### High-Beam Assistant motorway (HBA): activate immediately from 140 km/h or between 90-110 km/h for 30s (default)
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3074: C_HBA_HGWY_V_LO (default: 5A - 90 km/h), bit 5, mask 11111111b -> `5A`
  * Group 3074: C_HBA_HGWY_V_HI (default: 8C - 140 km/h), bit 6, mask 11111111b -> `8C`
  * Group 3074: C_HBA_HGWY_V_MIN (default: 6E - 110 km/h), bit 7, mask 11111111b -> `6E`
  * Group 3074: C_HBA_HGWY_T_MIN (default: 1E - 30 sec), bit 8, mask 11111111b -> `1E`

## Botho.xml — FEM_01 (CAFD 00000794, author: Botho (public))

**Module series coverage:** F020,F030

### High-Beam Assistant (HBA): anti-glare tunnel activate at 50 km/h and deactivate at 45 km/h (default: 70-60 km/h)
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3074: C_HBA_ENA_V_LO (default: 3C - 60 km/h), bit 0, mask 11111111b -> `2D`
  * Group 3074: C_HBA_ENA_V_HI (default: 46 - 70 km/h), bit 1, mask 11111111b -> `32`

## Botho.xml — FEM_01 (CAFD 00000794, author: Botho (public))

**Module series coverage:** F020,F030

### High-Beam Assistant (HBA): anti-glare tunnel activate at 70 km/h and deactivate at 60 km/h (default)
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3074: C_HBA_ENA_V_LO (default: 3C - 60 km/h), bit 0, mask 11111111b -> `3C`
  * Group 3074: C_HBA_ENA_V_HI (default: 46 - 70 km/h), bit 1, mask 11111111b -> `46`

## Botho.xml — FEM_01 (CAFD 00000794, author: Botho (public))

**Module series coverage:** F020,F030

### High-Beam Assistant (HBA): activate via light switch to the right (default: no)
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3060: FLA_AKTIVIERUNG (default: LDS_in_A), bit 22, mask 11000000b -> `LDS_in_A_oder_2`

## Botho.xml — FEM_01 (CAFD 00000794, author: Botho (public))

**Module series coverage:** F020,F030

### High-Beam Assistant (HBA): deactivate via light switch to the right (default)
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3060: FLA_AKTIVIERUNG (default: LDS_in_A), bit 22, mask 11000000b -> `LDS_in_A`

## Botho.xml — FEM_01 (CAFD 00000794, author: Botho (public))

**Module series coverage:** F020,F030

### Fog lights: disable cornering lights
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3073: C_CLC_ENA (default: F020_enable), bit 218, mask 00000010b -> `F020_disable`
  * Group 3073: C_BLC_ENA (default: F020_enable), bit 66, mask 00000001b -> `F020_disable`
  * Group 3066: KL_ENABLE_LI (default: KL_Ein), bit 0, mask 00000001b -> `KL_Aus`
  * Group 3066: KL_ENABLE_RE (default: KL_Ein), bit 80, mask 00000001b -> `KL_Aus`
  * Group 3062: MAPPING_ABBIEGEL_L_OUTPUT (default: nsw_l), bit 110, mask 00111111b -> `off`
  * Group 3062: MAPPING_ABBIEGEL_R_OUTPUT (default: nsw_r), bit 121, mask 00111111b -> `off`

## Botho.xml — FEM_01 (CAFD 00000794, author: Botho (public))

**Module series coverage:** F020,F030

### Fog lights: allow fogs to turn on in reverse
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3073: C_CLC_REV_ALWAYS_ON (default: 01), bit 218, mask 00000100b -> `01`
  * Group 3073: C_CLC_REV_CURV_BOTH_ON (default: 01), bit 218, mask 00010000b -> `01`

## Botho.xml — FEM_01 (CAFD 00000794, author: Botho (public))

**Module series coverage:** F020,F030

### Welcome lighting: activate door lights when reversing
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3070: OVT_BEI_RUECKFAHRLICHT (default: nicht_aktiv), bit 11, mask 00010000b -> `aktiv`

## Botho.xml — FEM_01 (CAFD 00000794, author: Botho (public))

**Module series coverage:** F020,F030

### Eclairage d'accueil: Activation des anti-brouillard
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3063: MAPPING_NEBELSCHW_L_PART_OF_WL (default: 00), bit 55, mask 11000000b -> `01`
  * Group 3063: MAPPING_NEBELSCHW_R_PART_OF_WL (default: 00), bit 66, mask 11000000b -> `01`

## Botho.xml — FEM_01 (CAFD 00000794, author: Botho (public))

**Module series coverage:** F020,F030

### Welcome lighting: set DRL brightness to 50% (default 100%)
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3070: WL_HELLIGKEIT (default: 64), bit 14, mask 11111111b -> `32`

## Botho.xml — FEM_01 (CAFD 00000794, author: Botho (public))

**Module series coverage:** F020,F030

### Welcome lighting: duration 60s (default: 20s)
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3060: WL_TIMEOUT (default: 14), bit 15, mask 11111111b -> `3C`

## Botho.xml — FEM_01 (CAFD 00000794, author: Botho (public))

**Module series coverage:** F020,F030

### Lighting: reduce automatic light sensor sensitivity
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3130: RLS_DEF_FLC_SCHWELLWERT_SATZ (default: 00), bit 5, mask 00000111b -> `03`

## Botho.xml — FEM_01 (CAFD 00000794, author: Botho (public))

**Module series coverage:** F020,F030

### Door puddle lighting (FollowMeHome step 1 of 2 - see HU-NBT) - 4th button or quick third press (default: inactive)
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3060: FOLLOWMEHOME_VIA_FFB (default: nicht_aktiv), bit 14, mask 00000010b -> `aktiv`

## Botho.xml — FEM_01 (CAFD 00000794, author: Botho (public))

**Module series coverage:** F020,F030

### Door puddle lighting (FollowMeHome): duration 30s (default: 20s)
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3064: PIA_DEFAULT_FMH (default: 14), bit 216, mask 11111111b -> `1E`

## Botho.xml — FEM_01 (CAFD 00000794, author: Botho (public))

**Module series coverage:** F020,F030

### Ambient lighting: activate when unlocking
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3070: WELCOME_AMBIENTE (default: nicht_aktiv), bit 1, mask 10000000b -> `aktiv`

## Botho.xml — FEM_01 (CAFD 00000794, author: Botho (public))

**Module series coverage:** F020,F030

### Ambient lighting: stay on 60s after unlocking (default: 20s)
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3070: IB_EINSCHALT_BEGR_ULOK (default: 14), bit 9, mask 00011111b -> `3C`

## Botho.xml — FEM_01 (CAFD 00000794, author: Botho (public))

**Module series coverage:** F020,F030

### Ambient lighting: stay on 20s after locking (default: 8s)
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3070: IB_EINSCHALT_BEGR_LOK (default: 08), bit 10, mask 00011111b -> `14`

## Botho.xml — FEM_01 (CAFD 00000794, author: Botho (public))

**Module series coverage:** F020,F030

### Separate brightness control for cluster and ambient lighting
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3070: AMBIENTE_NACHFUEHRUNG (default: aktiv), bit 4, mask 10000000b -> `nicht_aktiv`

## Botho.xml — FEM_01 (CAFD 00000794, author: Botho (public))

**Module series coverage:** F020,F030

### Feux freinage d'urgence: activation mode clignotement
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3060: ESS_AKTIVIERBARER_AUSGANG (default: bremslicht_blinkend), bit 16, mask 00000011b -> `bremslicht_blinkend`

## Botho.xml — FEM_01 (CAFD 00000794, author: Botho (public))

**Module series coverage:** F020,F030

### Emergency brake lights: lower deceleration threshold to 3 m/s^2 (default: 7 m/s^2)
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3060: ESS_AKTIVIERUNG_REALE_VERZ (default: 0E), bit 20, mask 00011111b -> `06`

## Botho.xml — FEM_01 (CAFD 00000794, author: Botho (public))

**Module series coverage:** F020,F030

### Emergency brake lights: minimum speed above 20 km/h (default: 50 km/h)
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3060: ESS_AKTIVIERUNG_GESCHW (default: 32), bit 17, mask 11111110b -> `14`

## Botho.xml — FEM_01 (CAFD 00000794, author: Botho (public))

**Module series coverage:** F020,F030

### Auto Start/Stop: disable by default
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3023: TCM_MSA_DEFAULT_OFF (default: nicht_aktiv), bit 0, mask 00010000b -> `aktiv`

## Botho.xml — FEM_01 (CAFD 00000794, author: Botho (public))

**Module series coverage:** F020,F030

### Auto Start/Stop: disable in Eco Pro mode
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3023: TCM_MSA_ECO_MODE (default: aktiv), bit 0, mask 10000000b -> `nicht_aktiv`

## Botho.xml — FEM_01 (CAFD 00000794, author: Botho (public))

**Module series coverage:** F020,F030

### Auto Start/Stop: remember last state (after restart)
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3023: TCM_MSA_MEMORY (default: nicht_aktiv), bit 0, mask 00100000b -> `aktiv`

## Botho.xml — FEM_01 (CAFD 00000794, author: Botho (public))

**Module series coverage:** F020,F030

### Double horn when locking with engine running
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3040: CLM_HORN_AT_SECURE (default: aktiv), bit 1, mask 00100000b -> `aktiv`

## Botho.xml — FEM_01 (CAFD 00000794, author: Botho (public))

**Module series coverage:** F020,F030

### Turn off radio/navigation when driver's door opens (default: disabled)
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3020: TCM_LOGIC_R_OFF_DOOR (default: nicht_aktiv), bit 1, mask 00000001b -> `aktiv`

## Botho.xml — FEM_01 (CAFD 00000794, author: Botho (public))

**Module series coverage:** F020,F030

### Turn on radio/navigation when driver's door opens (default: disabled)
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3020: TCM_LOGIC_R_OFF_DOOR (default: nicht_aktiv), bit 1, mask 00000001b -> `nicht_aktiv`

## Botho.xml — FEM_01 (CAFD 00000794, author: Botho (public))

**Module series coverage:** F020,F030

### Engine: start without pressing brake pedal (automatic)
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3020: TCM_STARTLOCK_BRAKE (default: aktiv), bit 0, mask 00000001b -> `nicht_aktiv`
  * Group 3020: TCM_STARTLOCK_DRIVINGREADINESS (default: aktiv), bit 0, mask 00010000b -> `nicht_aktiv`

## Botho.xml — FZD__07 (CAFD 00000A07, author: Botho (public))

**Module series coverage:** F020,F030

### Acoustical lock/unlock confirmation Buzzer level low (level 2 - default)
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3001: Buzzer level low (default: level_2), bit 33, mask 11111111b -> `level_2`

## Botho.xml — FZD__07 (CAFD 00000A07, author: Botho (public))

**Module series coverage:** F020,F030

### Acoustical lock/unlock confirmation Buzzer level low (level 3)
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3001: Buzzer level low (default: level_2), bit 33, mask 11111111b -> `level_3`

## Botho.xml — FZD__07 (CAFD 00000A07, author: Botho (public))

**Module series coverage:** F020,F030

### Acoustical lock/unlock confirmation Buzzer level low (level 4)
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3001: Buzzer level low (default: level_2), bit 33, mask 11111111b -> `level_4`

## Botho.xml — FZD__07 (CAFD 00000A07, author: Botho (public))

**Module series coverage:** F020,F030

### Acoustical lock/unlock confirmation Buzzer level low (level 5)
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3001: Buzzer level low (default: level_2), bit 33, mask 11111111b -> `level_5`

## Botho.xml — FZD__07 (CAFD 00000A07, author: Botho (public))

**Module series coverage:** F020,F030

### Acoustical lock/unlock confirmation Buzzer level low (level 6)
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3001: Buzzer level low (default: level_2), bit 33, mask 11111111b -> `level_6`

## Botho.xml — FZD__07 (CAFD 00000A07, author: Botho (public))

**Module series coverage:** F020,F030

### Acoustical lock/unlock confirmation Buzzer level low (level 7)
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3001: Buzzer level low (default: level_2), bit 33, mask 11111111b -> `level_7`

## Botho.xml — FZD__07 (CAFD 00000A07, author: Botho (public))

**Module series coverage:** F020,F030

### Acoustical lock/unlock confirmation Buzzer level low (level 8)
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3001: Buzzer level low (default: level_2), bit 33, mask 11111111b -> `level_8`

## Botho.xml — FZD__07 (CAFD 00000A07, author: Botho (public))

**Module series coverage:** F020,F030

### Acoustical lock/unlock confirmation Buzzer level low (level 9)
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3001: Buzzer level low (default: level_2), bit 33, mask 11111111b -> `level_9`

## Botho.xml — FZD__07 (CAFD 00000A07, author: Botho (public))

**Module series coverage:** F020,F030

### Acoustical lock/unlock confirmation Buzzer level low (level 10)
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3001: Buzzer level low (default: level_2), bit 33, mask 11111111b -> `level_10`

## Botho.xml — FZD__07 (CAFD 00000A07, author: Botho (public))

**Module series coverage:** F020,F030

### Acoustical lock/unlock confirmation Buzzer level high (level 2)
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3001: Buzzer level high (default: level_3), bit 34, mask 11111111b -> `level_2`

## Botho.xml — FZD__07 (CAFD 00000A07, author: Botho (public))

**Module series coverage:** F020,F030

### Acoustical lock/unlock confirmation Buzzer level high (level 3 - default)
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3001: Buzzer level high (default: level_3), bit 34, mask 11111111b -> `level_3`

## Botho.xml — FZD__07 (CAFD 00000A07, author: Botho (public))

**Module series coverage:** F020,F030

### Acoustical lock/unlock confirmation Buzzer level high (level 4)
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3001: Buzzer level high (default: level_3), bit 34, mask 11111111b -> `level_4`

## Botho.xml — FZD__07 (CAFD 00000A07, author: Botho (public))

**Module series coverage:** F020,F030

### Acoustical lock/unlock confirmation Buzzer level high (level 5)
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3001: Buzzer level high (default: level_3), bit 34, mask 11111111b -> `level_5`

## Botho.xml — FZD__07 (CAFD 00000A07, author: Botho (public))

**Module series coverage:** F020,F030

### Acoustical lock/unlock confirmation Buzzer level high (level 6)
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3001: Buzzer level high (default: level_3), bit 34, mask 11111111b -> `level_6`

## Botho.xml — FZD__07 (CAFD 00000A07, author: Botho (public))

**Module series coverage:** F020,F030

### Acoustical lock/unlock confirmation Buzzer level high (level 7)
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3001: Buzzer level high (default: level_3), bit 34, mask 11111111b -> `level_7`

## Botho.xml — FZD__07 (CAFD 00000A07, author: Botho (public))

**Module series coverage:** F020,F030

### Acoustical lock/unlock confirmation Buzzer level high (level 8)
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3001: Buzzer level high (default: level_3), bit 34, mask 11111111b -> `level_8`

## Botho.xml — FZD__07 (CAFD 00000A07, author: Botho (public))

**Module series coverage:** F020,F030

### Acoustical lock/unlock confirmation Buzzer level high (level 9)
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3001: Buzzer level high (default: level_3), bit 34, mask 11111111b -> `level_9`

## Botho.xml — FZD__07 (CAFD 00000A07, author: Botho (public))

**Module series coverage:** F020,F030

### Acoustical lock/unlock confirmation Buzzer level high (level 10)
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3001: Buzzer level high (default: level_3), bit 34, mask 11111111b -> `level_10`

## Botho.xml — FZD__07 (CAFD 00000A07, author: Botho (public))

**Module series coverage:** F020,F030

### Acoustical lock/unlock confirmation sound frequency (Low)
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3001: Buzzer frequency (default: 8F), bit 35, mask 11111111b -> `8F`

## Botho.xml — FZD__07 (CAFD 00000A07, author: Botho (public))

**Module series coverage:** F020,F030

### Acoustical lock/unlock confirmation sound frequency (Normal - Default)
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3001: Buzzer frequency (default: 8F), bit 35, mask 11111111b -> `8F`

## Botho.xml — FZD__07 (CAFD 00000A07, author: Botho (public))

**Module series coverage:** F020,F030

### Acoustical lock/unlock confirmation sound frequency (High)
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3001: Buzzer frequency (default: 8F), bit 35, mask 11111111b -> `8F`

## Botho.xml — FZD__07 (CAFD 00000A07, author: Botho (public))

**Module series coverage:** F020,F030

### Acoustical lock/unlock confirmation sound duration (Short)
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3001: Buzzer duration (default: 0A), bit 36, mask 11111111b -> `05`

## Botho.xml — FZD__07 (CAFD 00000A07, author: Botho (public))

**Module series coverage:** F020,F030

### Acoustical lock/unlock confirmation sound duration (Normal - Default)
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3001: Buzzer duration (default: 0A), bit 36, mask 11111111b -> `0A`

## Botho.xml — FZD__07 (CAFD 00000A07, author: Botho (public))

**Module series coverage:** F020,F030

### Acoustical lock/unlock confirmation sound duration (Long)
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3001: Buzzer duration (default: 0A), bit 36, mask 11111111b -> `0F`

## Botho.xml — FZD__07 (CAFD 00000A07, author: Botho (public))

**Module series coverage:** F020,F030

### Acoustical lock/unlock confirmation sound duration (Very Long)
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3001: Buzzer duration (default: 0A), bit 36, mask 11111111b -> `14`

## Botho.xml — FZD__07 (CAFD 00000A07, author: Botho (public))

**Module series coverage:** F020,F030

### Alarm type Europe (Default)
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3001: Alarm type Europe (default: ece), bit 17, mask 11111111b -> `ece`

## Botho.xml — FZD__07 (CAFD 00000A07, author: Botho (public))

**Module series coverage:** F020,F030

### Alarm type GB
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3001: Alarm type GB (default: ece), bit 17, mask 11111111b -> `gb`

## Botho.xml — FZD__07 (CAFD 00000A07, author: Botho (public))

**Module series coverage:** F020,F030

### Alarm type US
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3001: Alarm type US (default: ece), bit 17, mask 11111111b -> `08`

## Botho.xml — FZD__07 (CAFD 00000A07, author: Botho (public))

**Module series coverage:** F020,F030

### Alarm Arming delay time (30 sec - Default)
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3001: Arming time (default: 30s), bit 15, mask 11111111b -> `3C`

## Botho.xml — FZD__07 (CAFD 00000A07, author: Botho (public))

**Module series coverage:** F020,F030

### Alarm Arming delay time (60 sec)
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3001: Arming time (default: 30s), bit 15, mask 11111111b -> `78`

## Botho.xml — FZD__07 (CAFD 00000A07, author: Botho (public))

**Module series coverage:** F020,F030

### Panic Alarm - Active
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3002: Panikalarm (default: nicht_aktiv), bit 0, mask 00000100b -> `aktiv`

## Botho.xml — FZD__07 (CAFD 00000A07, author: Botho (public))

**Module series coverage:** F020,F030

### Panic Alarm - Not active
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3002: Panikalarm (default: nicht_aktiv), bit 0, mask 00000100b -> `nicht_aktiv`

## Botho.xml — FZD__07 (CAFD 00000A07, author: Botho (public))

**Module series coverage:** F020,F030

### Alarm: delay to disable volumetric sensor after arming - normal (10s - Default)
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3002: Zeitfenster Deaktivierung NG-US (default: 0A), bit 2, mask 00001111b -> `0A`

## Botho.xml — FZD__07 (CAFD 00000A07, author: Botho (public))

**Module series coverage:** F020,F030

### Alarm: delay to disable volumetric sensor after arming - long (20s)
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3002: Zeitfenster Deaktivierung NG-US (default: 0A), bit 2, mask 00001111b -> `14`

## Botho.xml — FZD__07 (CAFD 00000A07, author: Botho (public))

**Module series coverage:** F020,F030

### Alarm: Disable Acoustic acknowledgment when arming, regardless of door status (Default)
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3002: Akustische Quittierung Schaerfen (default: 00), bit 7, mask 00000001b -> `00`

## Botho.xml — FZD__07 (CAFD 00000A07, author: Botho (public))

**Module series coverage:** F020,F030

### Alarm: Enable Acoustic acknowledgment when arming, regardless of door status)
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3002: Akustische Quittierung Schaerfen (default: 00), bit 7, mask 00000001b -> `01`

## Botho.xml — ICMQL (CAFD 0000067B, author: Botho (public))

**Module series coverage:** F020,F030

### Active Cruise Control default distance (Level 1 - la plus faible)
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: C_Abstandsstufe_init (default: 03), bit 184, mask 00000111b -> `01`

## Botho.xml — ICMQL (CAFD 0000067B, author: Botho (public))

**Module series coverage:** F020,F030

### Active Cruise Control default distance (Level 2)
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: C_Abstandsstufe_init (default: 03), bit 184, mask 00000111b -> `02`

## Botho.xml — ICMQL (CAFD 0000067B, author: Botho (public))

**Module series coverage:** F020,F030

### Active Cruise Control default distance (Level 3 - Default)
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: C_Abstandsstufe_init (default: 03), bit 184, mask 00000111b -> `03`

## Botho.xml — ICMQL (CAFD 0000067B, author: Botho (public))

**Module series coverage:** F020,F030

### Active Cruise Control default distance (Level 4)
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: C_Abstandsstufe_init (default: 03), bit 184, mask 00000111b -> `04`

## Botho.xml — ICMQL (CAFD 0000067B, author: Botho (public))

**Module series coverage:** F020,F030

### Active Cruise Control: Enable from 10 km/h (30 km/h ou 20 mph par default)
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: C_Wunschgeschw_min_kmh (default: 1E), bit 142, mask 11111111b -> `0A`
  * Group 3000: C_Wunschgeschw_min_mph (default: 14), bit 143, mask 11111111b -> `06`

## Botho.xml — ICMQL (CAFD 0000067B, author: Botho (public))

**Module series coverage:** F020,F030

### Active Cruise Control: Enable from 30 km/h (Default)
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: C_Wunschgeschw_min_kmh (default: 1E), bit 142, mask 11111111b -> `1E`
  * Group 3000: C_Wunschgeschw_min_mph (default: 14), bit 143, mask 11111111b -> `14`

## Botho.xml — ICMQL (CAFD 0000067B, author: Botho (public))

**Module series coverage:** F020,F030

### Mode de conduite: Enable default ECO PRO when startup
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: IcmKod_B_InitEco (default: 00), bit 36, mask 00001000b -> `01`

## Botho.xml — ICMQL (CAFD 0000067B, author: Botho (public))

**Module series coverage:** F020,F030

### Mode de conduite: Enable default CONFORT when startup (Default)
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: IcmKod_B_InitEco (default: 00), bit 36, mask 00001000b -> `00`

## Botho.xml — ICMQL (CAFD 0000067B, author: Botho (public))

**Module series coverage:** F020,F030

### Blindspot detection: Enable from 10km/h
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: C_ZSW_Aktivierunggeschwindigkeit_Funktion_low (default: 01), bit 190, mask 00111111b -> `00`

## Botho.xml — ICMQL (CAFD 0000067B, author: Botho (public))

**Module series coverage:** F020,F030

### Blindspot detection: Enable from 20km/h (Default)
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: C_ZSW_Aktivierunggeschwindigkeit_Funktion_low (default: 01), bit 190, mask 00111111b -> `01`

## Botho.xml — ICMQL (CAFD 0000067B, author: Botho (public))

**Module series coverage:** F020,F030

### Blindspot detection: Enable from 30km/h
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: C_ZSW_Aktivierunggeschwindigkeit_Funktion_low (default: 01), bit 190, mask 00111111b -> `02`

## Botho.xml — ICMQL (CAFD 0000067B, author: Botho (public))

**Module series coverage:** F020,F030

### Blindspot detection: Enable from 50km/h
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: C_ZSW_Aktivierunggeschwindigkeit_Funktion_low (default: 01), bit 190, mask 00111111b -> `03`

## Botho.xml — IHKA_VA02 (CAFD 000016EE, author: Botho (public))

**Module series coverage:** F020,F030

### Climate control: remember last on/off state
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3003: MEMORY_OFF (default: aktiv), bit 0, mask 00000010b -> `aktiv`

## Botho.xml — IHKA_VA02 (CAFD 000016EE, author: Botho (public))

**Module series coverage:** F020,F030

### Climate control: remember last airflow position (default: 15 minutes after shutdown)
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3003: MEMORY_UMLUFT (default: nicht_aktiv), bit 0, mask 00000001b -> `aktiv`

## Botho.xml — IHKA_VA02 (CAFD 000016EE, author: Botho (public))

**Module series coverage:** F020,F030

### Climatisation: AC off en mode AUTO
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3003: AC_ON_WITH_AUTO (default: aktiv), bit 0, mask 00000100b -> `nicht_aktiv`

## Botho.xml — IHKA_VA02 (CAFD 000016EE, author: Botho (public))

**Module series coverage:** F020,F030

### Climate control: disable automatic recirculation restart (HO-Words: DAUE)
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3003: AC_ON_WITH_RECIRC (default: nicht_aktiv), bit 1, mask 00010000b -> `aktiv`
  * Group 3003: UMLUFT_AUTO_AUS (default: aktiv), bit 0, mask 10000000b -> `nicht_aktiv`

## Botho.xml — KAFAS2 (CAFD 00001148, author: Botho (public))

**Module series coverage:** F020,F030

### HUD: display distance control assistant (step 3 of 3 - see KOMBI and HU_NBT - requires Active Cruise Control)
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3060: DISPLAY_HEADWAY_DISTANCE (default: 00), bit 1, mask 00011000b -> `01`
  * Group 3060: SEND_STATUS_IBRAKE (default: 00), bit 1, mask 00000010b -> `01`
  * Group 3060: SEND_PARAM_IBRAKE (default: 01), bit 1, mask 00000100b -> `01`

## Botho.xml — KAFAS2 (CAFD 00001148, author: Botho (public))

**Module series coverage:** F020,F030

### Lane departure warning: enable edge detection without road markings
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3020: ROAD_EDGE_WARNING_ENABLED (defaut: 02), bit 2, mask 00000011b -> `detection_for_grass_edge_and_curb_stone`

## Botho.xml — KAFAS2 (CAFD 00001148, author: Botho (public))

**Module series coverage:** F020,F030

### Lane departure warning: activate from 55 km/h (default: 70) and deactivate below 50 km/h (default: 65)
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3020: THRV_AVAI_TLC_HIGH (default: 46), bit 3, mask 11111111b -> `37`
  * Group 3020: THRV_AVAI_TLC_LOW (default: 41), bit 4, mask 11111111b -> `32`

## Botho.xml — KAFAS2 (CAFD 00001148, author: Botho (public))

**Module series coverage:** F020,F030

### -- Don't work -- High-Beam Assistant (HBA): enable sensitivity adjustment (default: no_sensitivity_change)
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3050: ALLOW_SENS_CHANGE (default: 00), bit 1, mask 00010000b -> `01`

## Botho.xml — KAFAS2 (CAFD 00001148, author: Botho (public))

**Module series coverage:** F020,F030

### -- Don't work -- High-Beam Assistant (HBA): disable sensitivity adjustment (default)
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3050: ALLOW_SENS_CHANGE (default: 00), bit 1, mask 00010000b -> `00`

## Botho.xml — KAFAS2 (CAFD 00001148, author: Botho (public))

**Module series coverage:** F020,F030

### High-Beam Assistant (HBA): activate at 30 km/h and deactivate at 25 km/h (default: 40-30 km/h)
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3050: SPEED_SWITCHING_HIGH_BEAMS_ON (default: 28), bit 6, mask 11111111b -> `1E`
  * Group 3050: SPEED_SWITCHING_HIGH_BEAMS_OFF (default: 1E), bit 7, mask 11111111b -> `19`

## Botho.xml — KAFAS2 (CAFD 00001148, author: Botho (public))

**Module series coverage:** F020,F030

### High-Beam Assistant (HBA): activate at 40 km/h and deactivate at 30 km/h (default)
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3050: SPEED_SWITCHING_HIGH_BEAMS_ON (default: 28), bit 6, mask 11111111b -> `28`
  * Group 3050: SPEED_SWITCHING_HIGH_BEAMS_OFF (default: 1E), bit 7, mask 11111111b -> `1E`

## Botho.xml — KAFAS2 (CAFD 00001148, author: Botho (public))

**Module series coverage:** F020,F030

### High-Beam Assistant (HBA): faster anti-glare tunnel reaction times
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3050: DELAY_AFTER_ONCOMING (default: 06 - 6 sec), bit 8, mask 11111111b -> `03`
  * Group 3050: ONCOMING_HIGH_SPEED_DELAY (default: 0F - 15 sec), bit 10, mask 11111111b -> `04`
  * Group 3050: DELAY_AFTER_PRECEDING (default: 1E - 30 sec), bit 11, mask 11111111b -> `07`
  * Group 3050: DELAY_AFTER_SLOW_OVERTAKING (default: 50 - 80 sec), bit 12, mask 11111111b -> `14`

## Botho.xml — KAFAS2 (CAFD 00001148, author: Botho (public))

**Module series coverage:** F020,F030

### High-Beam Assistant (HBA): anti-glare tunnel reaction times default
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3050: DELAY_AFTER_ONCOMING (default: 06 - 6 sec), bit 8, mask 11111111b -> `06`
  * Group 3050: ONCOMING_HIGH_SPEED_DELAY (default: 0F - 15 sec), bit 10, mask 11111111b -> `0F`
  * Group 3050: DELAY_AFTER_PRECEDING (default: 1E - 30 sec), bit 11, mask 11111111b -> `1E`
  * Group 3050: DELAY_AFTER_SLOW_OVERTAKING (default: 50 - 80 sec), bit 12, mask 11111111b -> `50`

## Botho.xml — KAFAS2 (CAFD 00001148, author: Botho (public))

**Module series coverage:** F020,F030

### High-Beam Assistant (HBA): set urban activation threshold to 75 km/h (default: 85 km/h)
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3050: HIGH_SPEED_SWITCHING_HIGH_BEAMS (default: 55 - 85 km/h), bit 24, mask 11111111b -> `4B`

## Botho.xml — KAFAS2 (CAFD 00001148, author: Botho (public))

**Module series coverage:** F020,F030

### High-Beam Assistant (HBA): urban activation threshold 85 km/h (default)
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3050: HIGH_SPEED_SWITCHING_HIGH_BEAMS (default: 55- 85 km/h), bit 24, mask 11111111b -> `55`

## Botho.xml — HKFM (CAFD 000007C8, author: Botho (public))

**Module series coverage:** F020,F030

### Hayon: Activation fermeture via bouton au tableau de bord
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3010: SCH_FBD (default: aktiv), bit 2, mask 00001000b -> `aktiv`
  * Group 3010: SCH_TOEHKI (default: nicht_aktiv), bit 2, mask 00000100b -> `aktiv`
  * Group 3010: TASTER_FBD (default: nicht_aktiv), bit 0, mask 00001000b -> `aktiv`

## Botho.xml — HKFM (CAFD 000007C8, author: Botho (public))

**Module series coverage:** F020,F030

### Tailgate: opening speed (fast with braking before stop - segments bottom to top)
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3020: DREHZAL_SEGMENT_OEFF (default: 1B, 1B, 1B, 1B, 1B, 1B, 1B, 1B, 1B), bits 2-10, mask 11111111b -> `1B, 1B, 26, 26, 26, 26, 26, 1B, 13`
  * Group 3020: DEFAULT_DREHZ_OEF (default: 1B), bit 21, mask 11111111b -> `1B`

## Botho.xml — HKFM (CAFD 000007C8, author: Botho (public))

**Module series coverage:** F020,F030

### Hayon: Vitesse d'ouverture (par default)
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3020: DREHZAL_SEGMENT_OEFF (default: 1B, 1B, 1B, 1B, 1B, 1B, 1B, 1B, 1B), bits 2-10, mask 11111111b -> `1B, 1B, 1B, 1B, 1B, 1B, 1B, 1B, 1B`
  * Group 3020: DEFAULT_DREHZ_OEF (default: 1B), bit 21, mask 11111111b -> `1B`

## Botho.xml — HKFM (CAFD 000007C8, author: Botho (public))

**Module series coverage:** F020,F030

### Tailgate: closing speed (fast with braking at close - segments bottom to top)
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3020: DREHZAL_SEGMENT_SCHL (default: 13, 1B, 1B, 1B, 1B, 1B, 1B, 1B, 1B), bits 11-19, mask 11111111b -> `0A, 13, 26, 26, 26, 26, 26, 1E, 1B`
  * Group 3020: DEFAULT_DREHZ_SCHL (default: 1B), bit 20, mask 11111111b -> `1B`

## Botho.xml — HKFM (CAFD 000007C8, author: Botho (public))

**Module series coverage:** F020,F030

### Hayon: Vitesse de fermeture (par default)
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3020: DREHZAL_SEGMENT_SCHL (default: 13, 1B, 1B, 1B, 1B, 1B, 1B, 1B, 1B), bits 11-19, mask 11111111b -> `13, 1B, 1B, 1B, 1B, 1B, 1B, 1B, 1B`
  * Group 3020: DEFAULT_DREHZ_SCHL (default: 1B), bit 20, mask 11111111b -> `1B`

## Botho.xml — HKFM (CAFD 000007C8, author: Botho (public))

**Module series coverage:** F020,F030

### Hayon: Activation fermeture sur pression de la main (exercer une pression pour fermer au moins 5% du hayon en moins de 2s)
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3010: MECH_DRUK_AUTO_SCH (default: nicht_aktiv), bit 2, mask 00000010b -> `aktiv`
  * Group 3010: MECH_DRUCK_AUTO_ZEIT (default: 0A) - Duréee x 100ms de la pression à exercer, bit 4, mask 11111111b -> `14`
  * Group 3010: MECH_DRUCK_AUTO_WINKEL (default: 02) - Angle x 5% minimum pour enclecncher la fermeture automatique, bit 5, mask 11111111b -> `01`

## Botho.xml — HKFM (CAFD 000007C8, author: Botho (public))

**Module series coverage:** F020,F030

### Tailgate: disable close-on-hand pressure (default)
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3010: MECH_DRUK_AUTO_SCH (default: nicht_aktiv), bit 2, mask 00000010b -> `nicht_aktiv`
  * Group 3010: MECH_DRUCK_AUTO_ZEIT (default: 0A) - Duréee x 100ms de la pression à exercer, bit 4, mask 11111111b -> `0A`
  * Group 3010: MECH_DRUCK_AUTO_WINKEL (default: 02) - Angle x 5% minimum pour enclecncher la fermeture automatique, bit 5, mask 11111111b -> `02`

## Botho.xml — HKFM (CAFD 000007C8, author: Botho (public))

**Module series coverage:** F020,F030

### Hayon: Activation ouverture sur pression de la main (exercer une pression pour ouvrir au moins 5% du hayon en moins de 2s)
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3010: MECH_DRUCK_AUTO_OEF (default: nicht_aktiv), bit 2, mask 00000001b -> `aktiv`
  * Group 3010: MECH_DRUCK_AUTO_ZEIT (default: 0A) - Duréee x 100ms de la pression à exercer, bit 4, mask 11111111b -> `14`
  * Group 3010: MECH_DRUCK_AUTO_WINKEL (default: 02) - Angle x 5% minimum pour enclecncher la fermeture automatique, bit 5, mask 11111111b -> `01`

## Botho.xml — HKFM (CAFD 000007C8, author: Botho (public))

**Module series coverage:** F020,F030

### Tailgate: disable open-on-hand pressure (default)
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3010: MECH_DRUCK_AUTO_OEF (default: nicht_aktiv), bit 2, mask 00000001b -> `nicht_aktiv`
  * Group 3010: MECH_DRUCK_AUTO_ZEIT (default: 0A) - Duréee x 100ms de la pression à exercer, bit 4, mask 11111111b -> `0A`
  * Group 3010: MECH_DRUCK_AUTO_WINKEL (default: 02) - Angle x 5% minimum pour enclecncher la fermeture automatique, bit 5, mask 11111111b -> `02`

## Botho.xml — HKFM (CAFD 000007C8, author: Botho (public))

**Module series coverage:** F020,F030

### Tailgate: activate smart closing (step 2 of 2 - see FEM_BODY) enabled by default for production 03/15 onwards
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3120: FUNC_SMO (default: 00), bit 0, mask 00100000b -> `wert_F31`
  * Group 3120: FUNC_BUZZER_SMO (default: 00), bit 0, mask 01000000b -> `wert_F31`

## Botho.xml — HU_NBT (CAFD 00000DED, author: Botho (public))

**Module series coverage:** F020,F030

### Media: startup volume at 25% (default value)
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3002: VOL_MAX_ON (default: 19), bit 3, mask 11111111b -> `19`

## Botho.xml — HU_NBT (CAFD 00000DED, author: Botho (public))

**Module series coverage:** F020,F030

### Media: startup volume at 30% (default 25%)
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3002: VOL_MAX_ON (default: 19), bit 3, mask 11111111b -> `1E`

## Botho.xml — HU_NBT (CAFD 00000DED, author: Botho (public))

**Module series coverage:** F020,F030

### Media: startup volume at 40% (default 25%)
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3002: VOL_MAX_ON (default: 19), bit 3, mask 11111111b -> `28`

## Botho.xml — HU_NBT (CAFD 00000DED, author: Botho (public))

**Module series coverage:** F020,F030

### Media: show next track for music (KOMBI_LOW only)
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: BASIS_KOMBI_MMI_LIST (fonctionne que si KOMBI_CIC=kombi_low) (default: nicht_aktiv), bit 110, mask 00100000b -> `aktiv`

## Botho.xml — HU_NBT (CAFD 00000DED, author: Botho (public))

**Module series coverage:** F020,F030

### Media: enable OGG, XVID, XVCD and USB playback
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: ENT_CODEC_OGG (default: nicht_aktiv), bit 15, mask 00010000b -> `aktiv`
  * Group 3000: ENT_CODEC_XVID (default: nicht_aktiv), bit 15, mask 00100000b -> `aktiv`
  * Group 3000: ENT_CODEC_VCD (default: nicht_aktiv), bit 15, mask 01000000b -> `aktiv`
  * Group 3000: ENT_MC_VIDEO_SUPPORT (default: nicht_aktiv), bit 13, mask 00000100b -> `aktiv`

## Botho.xml — HU_NBT (CAFD 00000DED, author: Botho (public))

**Module series coverage:** F020,F030

### Media: enable DVD in motion
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: SPEEDLOCK_X_KMH_MAX (default: 03), bit 72, mask 11111111b -> `FF`
  * Group 3000: SPEEDLOCK_X_KMH_MIN (default: 03), bit 71, mask 11111111b -> `FF`
  * Group 3000: VIDEO_FRONT_LOCKED (default: nicht_aktiv), bit 5, mask 00010000b -> `nicht_aktiv`
  * Group 3000: VIDEO_HANDBRAKE (default: nicht_aktiv), bit 5, mask 00000100b -> `nicht_aktiv`
  * Group 3000: VIDEO_SPEEDLOCK_CONDITION (default: none), bit 57, mask 00000111b -> `none`

## Botho.xml — HU_NBT (CAFD 00000DED, author: Botho (public))

**Module series coverage:** F020,F030

### Media: use Gracenote dB full-size album art
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: ENT_MC_COVER_SCALE (default: nicht_aktiv), bit 14, mask 00100000b -> `aktiv`

## Botho.xml — HU_NBT (CAFD 00000DED, author: Botho (public))

**Module series coverage:** F020,F030

### Media: enable bookmarks in music collection
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: ENT_MC_SONG_BOOKMARKS (default: nicht_aktiv), bit 14, mask 00000100b -> `aktiv`

## Botho.xml — HU_NBT (CAFD 00000DED, author: Botho (public))

**Module series coverage:** F020,F030

### HUD: display distance control assistant (step 2 of 3 - see KOMBI and KAFAS2 - requires Active Cruise Control)
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: HUD_DISTANCE_INFO (default: nicht_aktiv), bit 97, mask 00001000b -> `aktiv`

## Botho.xml — HU_NBT (CAFD 00000DED, author: Botho (public))

**Module series coverage:** F020,F030

### HUD: display multimedia info for 2.5s (default 4s)
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: DISPLAYTIME_LIST_HUD_KOMBI (default: 05), bit 106, mask 00000111b -> `03`

## Botho.xml — HU_NBT (CAFD 00000DED, author: Botho (public))

**Module series coverage:** F020,F030

### HUD: show Sport option (shift indicator - M vehicles only)
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: HUD_SPORTANZEIGE_ENABLE (default: nicht_aktiv), bit 18, mask 00000001b -> `aktiv`
  * Group 3000: HUD_SPORTANZEIGE_MS_GASSE_ENABLE (default: nicht_aktiv), bit 18, mask 00000100b -> `aktiv`

## Botho.xml — HU_NBT (CAFD 00000DED, author: Botho (public))

**Module series coverage:** F020,F030

### Doors: Checkbox acoustical lock confirmation
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: ACOUSTICAL_LOCK_CONFIRM (default: nicht_aktiv), bit 110, mask 00000001b -> `aktiv`

## Botho.xml — HU_NBT (CAFD 00000DED, author: Botho (public))

**Module series coverage:** F020,F030

### Eclairage: Ajout feux de jour (Step 2 sur 3 - voir FEM_BODY et REM)
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: DAYDRIVING_LIGHT (default: 00), bit 92, mask 00011000b -> `02`

## Botho.xml — HU_NBT (CAFD 00000DED, author: Botho (public))

**Module series coverage:** F020,F030

### Status: display tire temperature and pressure
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3001: RDC_SAFETY (default: nicht_aktiv), bit 1, mask 00100000b -> `aktiv`
  * Group 3001: RDC_DRUCK_TEMP (default: 01/druck), bit 66, mask 00001100b -> `02`

## Botho.xml — HU_NBT (CAFD 00000DED, author: Botho (public))

**Module series coverage:** F020,F030

### Statut: Affichage du carnet d'entretien
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: SERVICE_HISTORY (default: aktiv), bit 2, mask 00100000b -> `aktiv`

## Botho.xml — HU_NBT (CAFD 00000DED, author: Botho (public))

**Module series coverage:** F020,F030

### Notice: Utilisation de la notice et jumelage BT en roulant
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: SL06_IBA_1 (default: aktiv), bit 0, mask 00100000b -> `nicht_aktiv`
  * Group 3000: SL07_IBA_2 (default: nicht_aktiv), bit 0, mask 01000000b -> `nicht_aktiv`
  * Group 3000: SL21_IBA_3 (default: nicht_aktiv), bit 2, mask 00010000b -> `nicht_aktiv`
  * Group 3000: SL16_ADD_CEDEVICE (default: nicht_aktiv), bit 1, mask 10000000b -> `nicht_aktiv`

## Botho.xml — HU_NBT (CAFD 00000DED, author: Botho (public))

**Module series coverage:** F020,F030

### Messages: Affichage des SMS, BMW Info, My Info and AKD en entier (default: 3 lignes)
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: MYINFO_DRIVING_TEXT_LENGTH (default: whole_text), bit 34, mask 00011100b -> `whole_text`
  * Group 3000: AKD_DRIVING_TEXT_LENGTH (default: whole_text), bit 34, mask 11100000b -> `whole_text`
  * Group 3000: BMWINFO_DRIVING_TEXT_LENGTH (default: whole_text), bit 35, mask 00000111b -> `whole_text`
  * Group 3000: SERVICES_MESSAGES_SPEEDLOCK_CONDITION (default: none), bit 35, mask 00111000b -> `none`
  * Group 3003: PIM_DRIVING_TEXT_LENGTH (default: 01), bit 11, mask 00000111b -> `07`

## Botho.xml — HU_NBT (CAFD 00000DED, author: Botho (public))

**Module series coverage:** F020,F030

### Sport: Affichage mode M Sport (Rouge et Argent)
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: M_VEHICLE (default: nicht_aktiv), bit 133, mask 01000000b -> `aktiv`

## Botho.xml — HU_NBT (CAFD 00000DED, author: Botho (public))

**Module series coverage:** F020,F030

### Tableau de bord: Affichage du point de commutation (Step 2 sur 2 - voir KOMBI)
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3001: SPA_CHECKBOX (default: nicht_aktiv), bit 66, mask 00010000b -> `aktiv`

## Botho.xml — HU_NBT (CAFD 00000DED, author: Botho (public))

**Module series coverage:** F020,F030

### Navigation: Alerte quand proche du POI
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: NAVI_ALERT_POI (default: nicht_aktiv), bit 111, mask 10000000b -> `aktiv`

## Botho.xml — HU_NBT (CAFD 00000DED, author: Botho (public))

**Module series coverage:** F020,F030

### Navigation: add route preview option
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: NAVI_ROAD_PREVIEW (default: nicht_aktiv), bit 59, mask 00100000b -> `aktiv`

## Botho.xml — HU_NBT (CAFD 00000DED, author: Botho (public))

**Module series coverage:** F020,F030

### Navigation: Ajoute la position GPS en fin de menu
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: NAVI_POSITION_MENU (default: nicht_aktiv), bit 96, mask 10000000b -> `aktiv`

## Botho.xml — HU_NBT (CAFD 00000DED, author: Botho (public))

**Module series coverage:** F020,F030

### Navigation: add route calculation preference for BMW servers
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: NAVI_ONLINE_OPTIMIZATION_BUTTON (default: nicht_aktiv), bit 112, mask 00000010b -> `aktiv`

## Botho.xml — HU_NBT (CAFD 00000DED, author: Botho (public))

**Module series coverage:** F020,F030

### Navigation: Active Real-Time Traffic Info
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: NAVI_TRAFFIC_INFO_MAP, bit 59, mask 00010000b -> `aktiv`
  * Group 3002: TI_CA_TMC, bit 23, mask 00000100b -> `aktiv`
  * Group 3002: TI_VINFO, bit 24, mask 00000010b -> `aktiv`
  * Group 3002: TI_TMC_REGIONAL, bit 23, mask 00100000b -> `aktiv`
  * Group 3002: TI_FALLBACK_DISABLED, bit 23, mask 01000000b -> `aktiv`

## Botho.xml — HU_NBT (CAFD 00000DED, author: Botho (public))

**Module series coverage:** F020,F030

### Navigation: Active la boussole
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: COMPASS, bit 5, mask 00000001b -> `aktiv`

## Botho.xml — HU_NBT (CAFD 00000DED, author: Botho (public))

**Module series coverage:** F020,F030

### Navigation: Affichage de la vue sortie autoroute dans HUD
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: JUNCTION_VIEW_HUD (default: nicht_aktiv. Aktiv si production date après 1114), bit 65, mask 00001000b -> `aktiv`

## Botho.xml — HU_NBT (CAFD 00000DED, author: Botho (public))

**Module series coverage:** F020,F030

### Navigation: enable demo route mode
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: ROUTE_FLIGHT (default: aktiv), bit 135, mask 00001000b -> `aktiv`
  * Group 3000: NAVI_SCROLLING_ALONG_ROUTE (default: nicht_aktiv), bit 111, mask 00001000b -> `aktiv`

## Botho.xml — HU_NBT (CAFD 00000DED, author: Botho (public))

**Module series coverage:** F020,F030

### Navigation: suggest fuel stop when needed
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: NAVI_FUELSTOP_PROPOSAL (default: aktiv), bit 60, mask 00100000b -> `aktiv`

## Botho.xml — HU_NBT (CAFD 00000DED, author: Botho (public))

**Module series coverage:** F020,F030

### Navigation: add traffic info categories to options
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: TRAFFIC_CATEGORIES (default: nicht_aktiv), bit 16, mask 00000010b -> `aktiv`

## Botho.xml — HU_NBT (CAFD 00000DED, author: Botho (public))

**Module series coverage:** F020,F030

### Navigation: add waypoint (magnet function)
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: NAVI_ROUTENMAGNET (default: nicht_aktiv), bit 111, mask 00010000b -> `aktiv`

## Botho.xml — HU_NBT (CAFD 00000DED, author: Botho (public))

**Module series coverage:** F020,F030

### Navigation: add express route menu to guidance preferences
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: NAVI_EXPRESS_ROADS (default: nicht_aktiv), bit 108, mask 00000100b -> `aktiv`

## Botho.xml — HU_NBT (CAFD 00000DED, author: Botho (public))

**Module series coverage:** F020,F030

### Navigation: active les popup de guidage SPLIT et FULL
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: NAVI_SPLIT_GUIDINGPOPUP (default: nicht_aktiv), bit 62, mask 00001000b -> `aktiv`
  * Group 3000: NAVI_FULL_GUIDINGPOPUP (default: nicht_aktiv), bit 62, mask 00010000b -> `aktiv`

## Botho.xml — HU_NBT (CAFD 00000DED, author: Botho (public))

**Module series coverage:** F020,F030

### Navigation: Voix femme (par default)
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: SPRECHERWAHL1 (default: weiblich), bit 73, mask 00001111b -> `weiblich`
  * Group 3000: SPRECHERWAHL2 (default: weiblich), bit 73, mask 11110000b -> `weiblich`
  * Group 3000: SPRECHERWAHL3 (default: weiblich), bit 74, mask 00001111b -> `weiblich`

## Botho.xml — HU_NBT (CAFD 00000DED, author: Botho (public))

**Module series coverage:** F020,F030

### Navigation: Voix homme
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: SPRECHERWAHL1 (default: weiblich), bit 73, mask 00001111b -> `maennlich`
  * Group 3000: SPRECHERWAHL2 (default: weiblich), bit 73, mask 11110000b -> `maennlich`
  * Group 3000: SPRECHERWAHL3 (default: weiblich), bit 74, mask 00001111b -> `maennlich`

## Botho.xml — HU_NBT (CAFD 00000DED, author: Botho (public))

**Module series coverage:** F020,F030

### Office: speech to text (email or SMS) requires Nuance subscription
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3003: SPEECH_2_TEXT (default: nicht_aktiv), bit 1, mask 00010000b -> `aktiv`

## Botho.xml — HU_NBT (CAFD 00000DED, author: Botho (public))

**Module series coverage:** F020,F030

### Cameras: remove legal messages
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3001: MACRO_CAM_LEGALDISCLAIMER (default: 06), bit 52, mask 11111111b -> `00`
  * Group 3001: LEGAL_DISCLAIMER_TIME (default: 00), bit 58, mask 11111111b -> `00`

## Botho.xml — HU_NBT (CAFD 00000DED, author: Botho (public))

**Module series coverage:** F020,F030

### Settings: enable developer menu
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: ENTWICKLER_MENUE (default: nicht_aktiv), bit 74, mask 01000000b -> `aktiv`

## Botho.xml — HU_NBT (CAFD 00000DED, author: Botho (public))

**Module series coverage:** F020,F030

### Phone: iOS ringtone
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3003: INBAND_RINGING (default: nicht_aktiv), bit 6, mask 10000000b -> `aktiv`

## Botho.xml — HU_NBT (CAFD 00000DED, author: Botho (public))

**Module series coverage:** F020,F030

### Phone: BMW ringtone (default: BMW)
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3003: RINGTONE (default: 00), bit 8, mask 00000011b -> `00`

## Botho.xml — HU_NBT (CAFD 00000DED, author: Botho (public))

**Module series coverage:** F020,F030

### Phone: MINI ringtone (default: BMW)
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3003: RINGTONE (default: 00), bit 8, mask 00000011b -> `01`

## Botho.xml — HU_NBT (CAFD 00000DED, author: Botho (public))

**Module series coverage:** F020,F030

### Phone: BMW i ringtone (default: BMW)
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3003: RINGTONE (default: 00), bit 8, mask 00000011b -> `02`

## Botho.xml — HU_NBT (CAFD 00000DED, author: Botho (public))

**Module series coverage:** F020,F030

### Phone: Rolls-Royce ringtone (default: BMW)
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3003: RINGTONE (default: 00), bit 8, mask 00000011b -> `03`

## Botho.xml — HU_NBT (CAFD 00000DED, author: Botho (public))

**Module series coverage:** F020,F030

### Phone: enable Siri Eyes Free (default: aktiv)
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3003: CE_DEVICE_SPEECH_RECOGNITION (default: 01), bit 3, mask 00001000b -> `01`

## Botho.xml — HU_NBT (CAFD 00000DED, author: Botho (public))

**Module series coverage:** F020,F030

### Settings: BMW gong sound (default: BMW)
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3002: SOUND_SIGNAL_SET (default: 00), bit 26, mask 00111000b -> `00`

## Botho.xml — HU_NBT (CAFD 00000DED, author: Botho (public))

**Module series coverage:** F020,F030

### Settings: MINI gong sound (default: BMW)
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3002: SOUND_SIGNAL_SET (default: 00), bit 26, mask 00111000b -> `01`

## Botho.xml — HU_NBT (CAFD 00000DED, author: Botho (public))

**Module series coverage:** F020,F030

### Settings: Rolls-Royce gong sound (default: BMW)
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3002: SOUND_SIGNAL_SET (default: 00), bit 26, mask 00111000b -> `02`

## Botho.xml — HU_NBT (CAFD 00000DED, author: Botho (public))

**Module series coverage:** F020,F030

### Settings: BMW i gong sound (default: BMW)
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3002: SOUND_SIGNAL_SET (default: 00), bit 26, mask 00111000b -> `03`

## Botho.xml — HU_NBT (CAFD 00000DED, author: Botho (public))

**Module series coverage:** F020,F030

### Settings: startup screen BMW ConnectedDrive 1 (default: BMW)
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3001: STARTUP_EMBLEM (default: 00), bit 62, mask 01111000b -> `00`

## Botho.xml — HU_NBT (CAFD 00000DED, author: Botho (public))

**Module series coverage:** F020,F030

### Settings: startup screen M Performance (default: BMW)
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3001: STARTUP_EMBLEM (default: 00), bit 62, mask 01111000b -> `01`

## Botho.xml — HU_NBT (CAFD 00000DED, author: Botho (public))

**Module series coverage:** F020,F030

### Settings: startup screen BMW ConnectedDrive 2 (default: BMW)
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3001: STARTUP_EMBLEM (default: 00), bit 62, mask 01111000b -> `02`

## Botho.xml — HU_NBT (CAFD 00000DED, author: Botho (public))

**Module series coverage:** F020,F030

### Settings: startup screen BMW i (default: BMW)
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3001: STARTUP_EMBLEM (default: 00), bit 62, mask 01111000b -> `03`

## Botho.xml — HU_NBT (CAFD 00000DED, author: Botho (public))

**Module series coverage:** F020,F030

### Settings: startup screen MINI (default: BMW)
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3001: STARTUP_EMBLEM (default: 00), bit 62, mask 01111000b -> `04`

## Botho.xml — HU_NBT (CAFD 00000DED, author: Botho (public))

**Module series coverage:** F020,F030

### Settings: startup screen Rolls-Royce (default: BMW)
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3001: STARTUP_EMBLEM (default: 00), bit 62, mask 01111000b -> `05`

## Botho.xml — HU_NBT (CAFD 00000DED, author: Botho (public))

**Module series coverage:** F020,F030

### Settings: startup screen BMW ConnectedDrive 3 (default: BMW)
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3001: STARTUP_EMBLEM (default: 00), bit 62, mask 01111000b -> `06`

## Botho.xml — HU_NBT (CAFD 00000DED, author: Botho (public))

**Module series coverage:** F020,F030

### Settings: startup screen BMW White (default: BMW)
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3001: STARTUP_EMBLEM (default: 00), bit 62, mask 01111000b -> `07`

## Botho.xml — HU_NBT (CAFD 00000DED, author: Botho (public))

**Module series coverage:** F020,F030

### Settings: startup screen BMW Brown (default: BMW)
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3001: STARTUP_EMBLEM (default: 00), bit 62, mask 01111000b -> `08`

## Botho.xml — HU_NBT (CAFD 00000DED, author: Botho (public))

**Module series coverage:** F020,F030

### Settings: startup screen BMW Christmas and New Year (default: BMW)
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3001: STARTUP_EMBLEM (default: 00), bit 62, mask 01111000b -> `09`

## Botho.xml — HU_NBT (CAFD 00000DED, author: Botho (public))

**Module series coverage:** F020,F030

### Settings: enable GPS tracking (appears to require subscription)
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3003: ASSIST_SVR_SHOW (default: nicht_aktiv), bit 15, mask 00000001b -> `aktiv`
  * Group 3003: ASSIST_VEHICLEFINDER_SHOW (default: aktiv), bit 14, mask 10000000b -> `aktiv`

## Botho.xml — HU_NBT (CAFD 00000DED, author: Botho (public))

**Module series coverage:** F020,F030

### Settings (expert): enable Bluetooth tethering - requires modifying provisioning XML via Tool32
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3003: DUN_PROFILE (default: 00), bit 3, mask 00000010b -> `01`
  * Group 3003: PAN_PROFILE (default: 00), bit 3, mask 00000100b -> `01`

## Botho.xml — HU_NBT (CAFD 00000DED, author: Botho (public))

**Module series coverage:** F020,F030

### -- TESTING -- Navigation: enable guided tours
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: GUIDED_TOURS (default: nicht_aktiv), bit 60, mask 00000010b -> `aktiv`
  * Group 3000: ROUTEN_ID_GUIDEDTOURS (default: nicht_aktiv), bit 60, mask 00010000b -> `aktiv`

## Botho.xml — HU_NBT (CAFD 00000DED, author: Botho (public))

**Module series coverage:** F020,F030

### -- Don't work -- Settings: traction control configuration (menu present but inactive)
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: TRACTION_DEMAND_CONTROL (default: nicht_aktiv), bit 134, mask 00001000b -> `aktiv`

## Botho.xml — HU_NBT (CAFD 00000DED, author: Botho (public))

**Module series coverage:** F020,F030

### -- Don't work -- Phone: show contacts icon
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3003: CONTACTS_ICON (default: nicht_aktiv), bit 12, mask 00001000b -> `aktiv`

## Botho.xml — HU_NBT (CAFD 00000DED, author: Botho (public))

**Module series coverage:** F020,F030

### -- Don't work -- Settings: enable parking exit assistant (requires specific hardware)
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3001: MACRO_PMA_AUSPARKEN (default: nicht_aktiv), bit 13, mask 10000000b -> `aktiv`

## Botho.xml — HU_NBT (CAFD 00000DED, author: Botho (public))

**Module series coverage:** F020,F030

### -- Don't work -- Settings: enable automatic PDC (requires specific hardware)
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3001: ACTIVE_PDC (default: nicht_aktiv), bit 64, mask 00010000b -> `aktiv`
  * Group 3001: AUTO_PDC (default: nicht_aktiv), bit 65, mask 01000000b -> `aktiv`

## Botho.xml — HU_NBT (CAFD 00000DED, author: Botho (public))

**Module series coverage:** F020,F030

### -- Don't work -- HUD: Affichage clignotants (Step 1 sur 2 - voir KOMBI)
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3001: HUD_TURNSIGNAL (default: nicht_aktiv), bit 55, mask 10000000b -> `aktiv`

## Botho.xml — HU_NBT (CAFD 00000DED, author: Botho (public))

**Module series coverage:** F020,F030

### -- Don't work -- Lighting: ambient light (F4x only)
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: DEAKTIVIERUNGSMOEGLICHKEIT_AMBILIGHT (default: 00), bit 35, mask 11000000b -> `01`

## Botho.xml — HU_NBT (CAFD 00000DED, author: Botho (public))

**Module series coverage:** F020,F030

### -- Don't work -- Eclairage: Affichage High-Beam Assistant (HBA)
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: HIGH_BEAM_ASSISTANT (default: nicht_aktiv), bit 109, mask 10000000b -> `aktiv`

## Botho.xml — HU_NBT (CAFD 00000DED, author: Botho (public))

**Module series coverage:** F020,F030

### -- TESTING -- Lighting: add door puddle light (Follow-Me-Home step 2 of 2 - see FEM)
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: KEY_CONF_COMFORT_HOMELIGHT (default: nicht_aktiv), bit 26, mask 00001000b -> `aktiv`

## Botho.xml — HU_NBT (CAFD 00000DED, author: Botho (public))

**Module series coverage:** F020,F030

### -- Don't work -- Statut: Affichage informations de la batterie
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: KI_SELECTION_SOC (default: nicht_aktiv), bit 134, mask 00000001b -> `aktiv`

## Botho.xml — HU_NBT (CAFD 00000DED, author: Botho (public))

**Module series coverage:** F020,F030

### *** TESTING *** Doors: comfort opening (double remote click lowers windows to 75% - useful for coupes)
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: COMFORT_OPENING (default: nicht_aktiv), bit 100, mask 01000000b -> `aktiv`

## Botho.xml — HU_NBT (CAFD 00000DED, author: Botho (public))

**Module series coverage:** F020,F030

### -- Don't work -- Navigation: Zoom automatique aux intersections
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: NAVI_AUTOZOOM (default: nicht_aktiv), bit 111, mask 00000100b -> `aktiv`

## Botho.xml — HU_NBT (CAFD 00000DED, author: Botho (public))

**Module series coverage:** F020,F030

### -- Don't work -- Navigation: Zoom automatique de la carte
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: AUTO_MAP_ZOOM (default: nicht_aktiv), bit 16, mask 00001000b -> `aktiv`

## Botho.xml — HU_NBT (CAFD 00000DED, author: Botho (public))

**Module series coverage:** F020,F030

### -- Don't work -- Navigation: Active le guidage en 2 etapes ?? No difference
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: NAVI_VIOCE_OUTPUT_2_STEP (default: nicht_aktiv), bit 111, mask 00000010b -> `aktiv`

## Botho.xml — KOMBI L7_MID (CAFD 000009C8, author: Botho (public))

**Module series coverage:** F020,F030

### Tableau de bord: Affichage de la vitesse digitale
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: BC_DIGITAL_V (default: nicht_aktiv), bit 1, mask 00000010b -> `aktiv`

## Botho.xml — KOMBI L7_MID (CAFD 000009C8, author: Botho (public))

**Module series coverage:** F020,F030

### Instrument cluster: show actual speed
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: BC_V_KORREKTUR (default: aktiv), bit 1, mask 01000000b -> `nicht_aktiv`

## Botho.xml — KOMBI L7_MID (CAFD 000009C8, author: Botho (public))

**Module series coverage:** F020,F030

### Instrument cluster: first fuel reserve warning at 70 km (default: 90 km)
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: CC_RW_WARNUNG_2 (default: 5A), bit 35, mask 11111111b -> `46`

## Botho.xml — KOMBI L7_MID (CAFD 000009C8, author: Botho (public))

**Module series coverage:** F020,F030

### Instrument cluster: first fuel reserve warning at 90 km (default: 90 km)
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: CC_RW_WARNUNG_2 (default: 5A), bit 35, mask 11111111b -> `5A`

## Botho.xml — KOMBI L7_MID (CAFD 000009C8, author: Botho (public))

**Module series coverage:** F020,F030

### Instrument cluster: second fuel reserve warning at 30 km (default: 50 km)
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: CC_RW_WARNUNG (default: 32), bit 29, mask 11111111b -> `1E`

## Botho.xml — KOMBI L7_MID (CAFD 000009C8, author: Botho (public))

**Module series coverage:** F020,F030

### Instrument cluster: second fuel reserve warning at 50 km (default: 50 km)
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: CC_RW_WARNUNG (default: 32), bit 29, mask 11111111b -> `32`

## Botho.xml — KOMBI L7_MID (CAFD 000009C8, author: Botho (public))

**Module series coverage:** F020,F030

### Instrument cluster: disable automatic trip reset (default: 4h)
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: BC_AUTORESET_ZEIT (default: 04), bit 44, mask 11111111b -> `FF`

## Botho.xml — KOMBI L7_MID (CAFD 000009C8, author: Botho (public))

**Module series coverage:** F020,F030

### Instrument cluster: keep daytime lights active at night
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3007: DIM_NACHT_EIN (default: 08), bit 10, mask 11111111b -> `FF`

## Botho.xml — KOMBI L7_MID (CAFD 000009C8, author: Botho (public))

**Module series coverage:** F020,F030

### Instrument cluster: permanent M Performance logo bottom right (1/2)
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3003: MPM_ENABLE (default: nicht_aktiv), bit 7, mask 00000100b -> `aktiv`

## Botho.xml — KOMBI L7_MID (CAFD 000009C8, author: Botho (public))

**Module series coverage:** F020,F030

### Tableau de bord: Choix Logo M performance M50d (2/2)
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: MPM_LOGO (default: ag), bit 43, mask 11110000b -> `50d`

## Botho.xml — KOMBI L7_MID (CAFD 000009C8, author: Botho (public))

**Module series coverage:** F020,F030

### Tableau de bord: Choix Logo M performance 135i (2/2)
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: MPM_LOGO (default: ag), bit 43, mask 11110000b -> `135i`

## Botho.xml — KOMBI L7_MID (CAFD 000009C8, author: Botho (public))

**Module series coverage:** F020,F030

### Tableau de bord: Choix Logo M performance 140i (2/2)
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: MPM_LOGO (default: ag), bit 43, mask 11110000b -> `140i`

## Botho.xml — KOMBI L7_MID (CAFD 000009C8, author: Botho (public))

**Module series coverage:** F020,F030

### Tableau de bord: Choix Logo M performance 235i (2/2)
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: MPM_LOGO (default: ag), bit 43, mask 11110000b -> `235i`

## Botho.xml — KOMBI L7_MID (CAFD 000009C8, author: Botho (public))

**Module series coverage:** F020,F030

### Tableau de bord: Choix Logo M performance 240i (2/2)
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: MPM_LOGO (default: ag), bit 43, mask 11110000b -> `240i`

## Botho.xml — KOMBI L7_MID (CAFD 000009C8, author: Botho (public))

**Module series coverage:** F020,F030

### Tableau de bord: Choix Logo M performance 340i (2/2)
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: MPM_LOGO (default: ag), bit 43, mask 11110000b -> `340i`

## Botho.xml — KOMBI L7_MID (CAFD 000009C8, author: Botho (public))

**Module series coverage:** F020,F030

### Tableau de bord: Choix Logo M performance 550d (2/2)
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: MPM_LOGO (default: ag), bit 43, mask 11110000b -> `550d`

## Botho.xml — KOMBI L7_MID (CAFD 000009C8, author: Botho (public))

**Module series coverage:** F020,F030

### Tableau de bord: Choix Logo M performance hybride (2/2)
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: MPM_LOGO (default: ag), bit 43, mask 11110000b -> `phev`

## Botho.xml — KOMBI L7_MID (CAFD 000009C8, author: Botho (public))

**Module series coverage:** F020,F030

### Cluster and HUD: default startup logo
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: BMW_LOGO (default: ag), bit 0, mask 11110000b -> `ag`

## Botho.xml — KOMBI L7_MID (CAFD 000009C8, author: Botho (public))

**Module series coverage:** F020,F030

### Cluster and HUD: M Performance startup logo
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: BMW_LOGO (default: ag), bit 0, mask 11110000b -> `m_performance`

## Botho.xml — KOMBI L7_MID (CAFD 000009C8, author: Botho (public))

**Module series coverage:** F020,F030

### Cluster and HUD: M Performance startup logo 135i
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: BMW_LOGO (default: ag), bit 0, mask 11110000b -> `135i`

## Botho.xml — KOMBI L7_MID (CAFD 000009C8, author: Botho (public))

**Module series coverage:** F020,F030

### Cluster and HUD: M Performance startup logo 140i
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: BMW_LOGO (default: ag), bit 0, mask 11110000b -> `140i`

## Botho.xml — KOMBI L7_MID (CAFD 000009C8, author: Botho (public))

**Module series coverage:** F020,F030

### Cluster and HUD: M Performance startup logo 235i
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: BMW_LOGO (default: ag), bit 0, mask 11110000b -> `235i`

## Botho.xml — KOMBI L7_MID (CAFD 000009C8, author: Botho (public))

**Module series coverage:** F020,F030

### Cluster and HUD: M Performance startup logo 240i
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: BMW_LOGO (default: ag), bit 0, mask 11110000b -> `240i`

## Botho.xml — KOMBI L7_MID (CAFD 000009C8, author: Botho (public))

**Module series coverage:** F020,F030

### Cluster and HUD: M Performance startup logo 340i
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: BMW_LOGO (default: ag), bit 0, mask 11110000b -> `340i`

## Botho.xml — KOMBI L7_MID (CAFD 000009C8, author: Botho (public))

**Module series coverage:** F020,F030

### Cluster and HUD: M Performance startup logo 50d
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: BMW_LOGO (default: ag), bit 0, mask 11110000b -> `50d`

## Botho.xml — KOMBI L7_MID (CAFD 000009C8, author: Botho (public))

**Module series coverage:** F020,F030

### Cluster and HUD: M Performance startup logo M2
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: BMW_LOGO (default: ag), bit 0, mask 11110000b -> `M2`

## Botho.xml — KOMBI L7_MID (CAFD 000009C8, author: Botho (public))

**Module series coverage:** F020,F030

### Cluster and HUD: M Performance startup logo M3
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: BMW_LOGO (default: ag), bit 0, mask 11110000b -> `M4`

## Botho.xml — KOMBI L7_MID (CAFD 000009C8, author: Botho (public))

**Module series coverage:** F020,F030

### Cluster and HUD: M Performance startup logo M4 GTS
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: BMW_LOGO (default: ag), bit 0, mask 11110000b -> `M4 GTS`

## Botho.xml — KOMBI L7_MID (CAFD 000009C8, author: Botho (public))

**Module series coverage:** F020,F030

### Cluster and HUD: M Performance startup logo hybride
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: BMW_LOGO (default: ag), bit 0, mask 11110000b -> `phev`

## Botho.xml — KOMBI L7_MID (CAFD 000009C8, author: Botho (public))

**Module series coverage:** F020,F030

### Instrument cluster: show time bottom right (I-Step after 3.54.3)
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: BASISANZEIGE_VARIANTE (default: nicht_aktiv. Aktiv si production date après 0315), bit 53, mask 01000000b -> `aktiv`

## Botho.xml — KOMBI L7_MID (CAFD 000009C8, author: Botho (public))

**Module series coverage:** F020,F030

### Instrument cluster: show gear in Sport mode (S1-S8 instead of DS)
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: SPA_SPORT_ENABLE (default: nicht_aktiv. Aktiv si production date après 0315), bit 41, mask 00010000b -> `aktiv`

## Botho.xml — KOMBI L7_MID (CAFD 000009C8, author: Botho (public))

**Module series coverage:** F020,F030

### Tableau de bord: Affichage du point de commutation (Step 1 sur 2 - voir HU_NBT)
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3003: SPA_KOMBISELECT_DISABLE (default: nicht_aktiv), bit 0, mask 00100000b -> `nicht_aktiv`

## Botho.xml — KOMBI L7_MID (CAFD 000009C8, author: Botho (public))

**Module series coverage:** F020,F030

### Tableau de bord: Affichage rapports au compteur
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3003: SPA_IST_GANG_ENABLE (default: nicht_aktiv), bit 0, mask 00010000b -> `aktiv`

## Botho.xml — KOMBI L7_MID (CAFD 000009C8, author: Botho (public))

**Module series coverage:** F020,F030

### Tableau de bord: Volume clignotant moins fort
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 300B: BLINKER_VOLUME_CONTI (default: E0, F0, FF, FF), bit 4, mask 11111111b -> `A0, B0, C0, FF`

## Botho.xml — KOMBI L7_MID (CAFD 000009C8, author: Botho (public))

**Module series coverage:** F020,F030

### Tableau de bord: Volume clignotant par defaut
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 300B: BLINKER_VOLUME_CONTI (default: E0, F0, FF, FF), bit 4, mask 11111111b -> `E0, F0, FF, FF`

## Botho.xml — KOMBI L7_MID (CAFD 000009C8, author: Botho (public))

**Module series coverage:** F020,F030

### Instrument cluster: DTS separation (value to verify - see http://www.bimmerfest.com/forums/showthread.php?p=10034327)
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: DSC_OFF_ENTFLECHTUNG_ENABLE (default: nicht_aktiv), bit 43, mask 00000010b -> `aktiv`

## Botho.xml — KOMBI L7_MID (CAFD 000009C8, author: Botho (public))

**Module series coverage:** F020,F030

### HUD: extend startup duration to 10s to display logo longer (default: 4s)
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 300B: HUD_STARTUP_TIME (default: 28. 32 si production date après 0315), bit 20, mask 11111111b -> `0A`

## Botho.xml — KOMBI L7_MID (CAFD 000009C8, author: Botho (public))

**Module series coverage:** F020,F030

### HUD: display distance control assistant (step 1 of 3 - see KAFAS2 and HU_NBT - requires Active Cruise Control)
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: IBRAKE_ABSTAND_ENABLE (default: nicht_aktiv), bit 1, mask 00000001b -> `aktiv`
  * Group 3003: IBRAKE_VERBAUT (default: aktiv), bit 3, mask 00000100b -> `aktiv`
  * Group 3003: HUD_IBRAKE_ENABLE (default: aktiv), bit 4, mask 00100000b -> `aktiv`
  * Group 3008: HUD_PIA_IBRAKE (default: nicht_aktiv), bit 6, mask 00100000b -> `aktiv`

## Botho.xml — KOMBI L7_MID (CAFD 000009C8, author: Botho (public))

**Module series coverage:** F020,F030

### -- Don't work -- HUD: Affichage clignotants (Step 1 sur 2 - voir HU_NBT)
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3003: HUD_BLINKER_ENABLE (default: nicht_aktiv), bit 4, mask 00000001b -> `aktiv`
  * Group 3008: HUD_PIA_BLINKER (default: nicht_aktiv), bit 5, mask 00000001b -> `aktiv`

## Botho.xml — KOMBI L7_MID (CAFD 000009C8, author: Botho (public))

**Module series coverage:** F020,F030

### -- TESTING -- HUD: HUD_POSITIONCHANGE_ENABLE
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: HUD_POSITIONCHANGE_ENABLE (défaut : nicht_aktiv), bit 53, mask 10000000b -> `aktiv`

## Botho.xml — KOMBI L7_MID (CAFD 000009C8, author: Botho (public))

**Module series coverage:** F020,F030

### -- TESTING -- HUD: SPA_ENABLE
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3003: SPA_ENABLE - Active l'affichage du point de commutation (défaut : nicht_aktiv), bit 0, mask 0001000b -> `aktiv`

## Botho.xml — REM_01 (CAFD 000007A1, author: Botho (public))

**Module series coverage:** F020,F030

### Rear windows: enable when rear doors open
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3050: FH_TUERAUF_STOP_MAUT (default: aktiv), bit 0, mask 00000001b -> `nicht_aktiv`

## Botho.xml — REM_01 (CAFD 000007A1, author: Botho (public))

**Module series coverage:** F020,F030

### Angel Eyes (DRL): enable tailgate DRLs (step 3 of 3 - see HU-NBT and FEM_BODY)
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3062: MAPPING_TAGFAHRL_H2_L_OUTPUT LED hayon intérieur gauche (default: 00), bit 220, mask 00111111b -> `16`
  * Group 3062: MAPPING_TAGFAHRL_H2_R_OUTPUT LED hayon intérieur droit (default: 00), bit 230, mask 00111111b -> `17`
  * Group 3062: MAPPING_TAGFAHRL_H_L_OUTPUT LED hayon exterieur gauche (default: 00), bit 200, mask 00111111b -> `14`
  * Group 3062: MAPPING_TAGFAHRL_H_R_OUTPUT LED hayon exterieur droit (default: 00), bit 210, mask 00111111b -> `15`

## Botho.xml — REM_01 (CAFD 000007A1, author: Botho (public))

**Module series coverage:** F020,F030

### Rear fog lights: activation (step 1 of 2 - see FEM_BODY)
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3063: Mapping_Nebelschlussl_L_output lampe hayon gauche (default: 1C), bit 40, mask 00111111b -> `1C`
  * Group 3063: Mapping_Nebelschlussl_L_Function lampe hayon gauche (default: 0E), bit 41, mask 00011111b -> `0E`
  * Group 3063: Mapping_Nebelschlussl_R_output lampe hayon droit (default: 1D), bit 50, mask 00111111b -> `1D`
  * Group 3063: Mapping_Nebelschlussl_R_Function lampe hayon droit (default: 0E), bit 51, mask 00011111b -> `0E`

## Botho.xml — REM_01 (CAFD 000007A1, author: Botho (public))

**Module series coverage:** F020,F030

### Rear fog lights: deactivation (step 1 of 2 - see FEM_BODY)
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3063: Mapping_Nebelschlussl_L_output lampe hayon gauche (default: 1C), bit 40, mask 00111111b -> `00`
  * Group 3063: Mapping_Nebelschlussl_L_Function lampe hayon gauche (default: 0E), bit 41, mask 00011111b -> `0E`
  * Group 3063: Mapping_Nebelschlussl_R_output lampe hayon droit (default: 1D), bit 50, mask 00111111b -> `00`
  * Group 3063: Mapping_Nebelschlussl_R_Function lampe hayon droit (default: 0E), bit 51, mask 00011111b -> `0E`

## Botho.xml — REM_01 (CAFD 000007A1, author: Botho (public))

**Module series coverage:** F020,F030

### Rear camera: remove speed limit (side cameras see TRSVC)
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3203: V_SCHWELLE_1: vitesse de désactivation caméras rétroviseurs (default: 0F), bit 7, mask 11111111b -> `FF`
  * Group 3203: V_SCHWELLE_2: vitesse de désactivation caméra arrière (default: 0F), bit 8, mask 11111111b -> `FF`
  * Group 3203: D_SCHWELLE_1: distance de désactivation caméras rétroviseurs (default: 32), bit 9, mask 11111111b -> `FF`
  * Group 3203: D_SCHWELLE_2: distance de désactivation caméra arrière (default: 0A), bit 10, mask 11111111b -> `FF`

## Botho.xml — REM_01 (CAFD 000007A1, author: Botho (public))

**Module series coverage:** F020,F030

### Emergency brake lights: enable rear LEDs (default: enabled)
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3062: MAPPING_BRAKEFORCED_L_OUTPUT (default: bl_l), bit 110, mask 00111111b -> `bl_l`
  * Group 3062: MAPPING_BRAKEFORCED_R_OUTPUT (default: bl_r), bit 120, mask 00111111b -> `bl_r`

## Botho.xml — REM_01 (CAFD 000007A1, author: Botho (public))

**Module series coverage:** F020,F030

### Emergency brake lights: increase rear LED flash frequency (default: 03)
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3064: ESS_BLINKFREQ_1 (default: 03), bit 17, mask 00001110b -> `05`
  * Group 3064: ESS_BLINKFREQ_2 (default: 03), bit 17, mask 01110000b -> `05`

## Botho.xml — CFAS_PLX_1 (CAFD 000000B5, author: Botho (public))

**Module series coverage:** F020,F030

### Power seats: chime when storing position
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: MEMORY_GONG (default: nicht_aktiv. Aktiv si production date après 0714), bit 2, mask 00001000b -> `aktiv`

## Botho.xml — CFAS_PLX_1 (CAFD 000000B5, author: Botho (public))

**Module series coverage:** F020,F030

### Power seats (Easy Entry): enable Easy Entry
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: EINAUSSTIEGSHILFE (default: nicht_aktiv), bit 0, mask 00011100b -> `Modus_FA_SLV`

## Botho.xml — CFAS_PLX_1 (CAFD 000000B5, author: Botho (public))

**Module series coverage:** F020,F030

### Power seats (Easy Entry): minimum seat distance from rear stop
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3012: EAH_SCHUTZFREIRAUM_HINTEN_SLV_PHYS (default: 00, 64), bits 4-5, mask 11111111b -> `00, 32`

## Botho.xml — CFAS_PLX_1 (CAFD 000000B5, author: Botho (public))

**Module series coverage:** F020,F030

### Power seats (Easy Entry): seat travel distance
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3012: EAH_VERFAHRWEG_SLV_PHYS (default: 00, 3C), bits 0-1, mask 11111111b -> `00, 32`

## Botho.xml — TRSVC (CAFD 00000223, author: Botho (public))

**Module series coverage:** F020,F030

### Side cameras: remove speed limit (rear camera see REM_01)
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: SV_Activate_Speed_Limit (default: 0F), bit 114, mask 11111111b -> `FF`
  * Group 3000: SV_Deactivate_Speed (default: 0F), bit 115, mask 11111111b -> `FF`

## Bundang_Thunder.xml — ACSM_4C (CAFD 00000909, author: Bundang Thunder X3)

**Module series coverage:** F15,F16,F25,F26,F48,F85,F86

### Seat belt warning chime for only 5 seconds                                                                                 --** by Bundang Thunder ^^
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: GWF_SBR_WARNDAUER, bit 3, mask 11111111b -> `05`

## Bundang_Thunder.xml — ACSM_4C (CAFD 00000909, author: Bundang Thunder X3)

**Module series coverage:** F15,F16,F25,F26,F48,F85,F86

### Delete driver seat belt warning light
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: SBR_PreWarning_Fahrer, bit 16, mask 00000001b -> `00`

## Bundang_Thunder.xml — ACSM_4C (CAFD 00000909, author: Bundang Thunder X3)

**Module series coverage:** F15,F16,F25,F26,F48,F85,F86

### Delete passenger seat belt warning light
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: SBR_PreWarning_Beifahrer, bit 16, mask 00000010b -> `00`

## Bundang_Thunder.xml — ACSM_4C (CAFD 00000909, author: Bundang Thunder X3)

**Module series coverage:** F15,F16,F25,F26,F48,F85,F86

### Disable driver seat belt warning chime
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: SeatBeltReminder_SBR_Fahrer, bit 15, mask 00000010b -> `00`

## Bundang_Thunder.xml — ACSM_4C (CAFD 00000909, author: Bundang Thunder X3)

**Module series coverage:** F15,F16,F25,F26,F48,F85,F86

### Disable passenger seat belt warning chime
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: SeatBeltReminder_SBR_Beifahrer, bit 15, mask 00000100b -> `00`

## Bundang_Thunder.xml — CAS_04 (CAFD 0000000F, author: Bundang Thunder X3)

**Module series coverage:** F15,F16,F25,F26,F48,F85,F86

### Turn off audio automatically when engine stops                                                                             --** by Bundang Thunder ^^
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 30D0: TC_LOGIC_KLR_OFF_DOOR, bit 2, mask 111111!1b -> `01`

## Bundang_Thunder.xml — CAS_04 (CAFD 0000000F, author: Bundang Thunder X3)

**Module series coverage:** F15,F16,F25,F26,F48,F85,F86

### Double horn when locking with engine running - enable
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3002: CLM_HORN_AT_SECURE, bit 0, mask 00100000b -> `01`

## Bundang_Thunder.xml — CAS_04 (CAFD 0000000F, author: Bundang Thunder X3)

**Module series coverage:** F15,F16,F25,F26,F48,F85,F86

### Double horn when locking with engine running - disable
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3002: CLM_HORN_AT_SECURE, bit 0, mask 00100000b -> `00`

## Bundang_Thunder.xml — CAS_04 (CAFD 0000000F, author: Bundang Thunder X3)

**Module series coverage:** F15,F16,F25,F26,F48,F85,F86

### Set auto start/stop off by default
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: TC_MSA_DEFAULT_OFF, bit 3, mask 00010000b -> `01`

## Bundang_Thunder.xml — CAS_04 (CAFD 0000000F, author: Bundang Thunder X3)

**Module series coverage:** F15,F16,F25,F26,F48,F85,F86

### Remember last auto start/stop state
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: TC_MSA_MEMORY, bit 3, mask 00100000b -> `01`

## Bundang_Thunder.xml — CAS_04 (CAFD 0000000F, author: Bundang Thunder X3)

**Module series coverage:** F15,F16,F25,F26,F48,F85,F86

### Fold mirrors immediately when locking (lock folding)
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3003: KMFRT_SCHLIESSEN, bit 12, mask 11111111b -> `00`

## Bundang_Thunder.xml — CAS_04 (CAFD 0000000F, author: Bundang Thunder X3)

**Module series coverage:** F15,F16,F25,F26,F48,F85,F86

### Change battery capacity to 90 Ah
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3702: VCM_BATTERY_CLASS, bit 0, mask 11111111b -> `01`

## Bundang_Thunder.xml — DXC_CT01 (CAFD 00000629, author: Bundang Thunder X3)

**Module series coverage:** F15,F16,F25,F26,F48,F85,F86

### Enable launch control (EGS coding also required)                                                                     --** by Bundang Thunder ^^
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: C_Funktion_LaunchControl_aktiv_I, bit 26, mask 10000001b -> `01`

## Bundang_Thunder.xml — FRM__03CT (CAFD 0000106D, author: Bundang Thunder X3)

**Module series coverage:** F15,F16,F25,F26,F48,F85,F86

### Welcome fog lights                                                                                            --** by Bundang Thunder ^^
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3050: WL_FUNKTION_AL, bit 30, mask 00001100b -> `soft_on_LED`

## Bundang_Thunder.xml — FRM__03CT (CAFD 0000106D, author: Bundang Thunder X3)

**Module series coverage:** F15,F16,F25,F26,F48,F85,F86

### Activate hazard lights during hard braking flashing
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3050: WB_GB_ENABLE, bit 2, mask 10000000b -> `01`

## Bundang_Thunder.xml — FRM__03CT (CAFD 0000106D, author: Bundang Thunder X3)

**Module series coverage:** F15,F16,F25,F26,F48,F85,F86

### Limit passenger mirror tilt to 30 degrees in reverse
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3020: ASP_BORDSTEINAUTOMATIK_DELTA, bit 1, mask 11111111b -> `1E`

## Bundang_Thunder.xml — FRM__03CT (CAFD 0000106D, author: Bundang Thunder X3)

**Module series coverage:** F15,F16,F25,F26,F48,F85,F86

### VLD
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3073: LUT_FLC_FORWARDLIGHTING_Y, bits 40-42, mask 11111111b -> `F015_ohne_AFS`
  * Group 3073: C_AFS_ENA, bit 152, mask 00000001b -> `F015_enable`

## Bundang_Thunder.xml — FRM__03CT (CAFD 0000106D, author: Bundang Thunder X3)

**Module series coverage:** F15,F16,F25,F26,F48,F85,F86

### Allow windows to keep closing with door open
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3030: FH_TUER_AUF_STOP_MAUT, bit 1, mask 00000100b -> `00`

## Bundang_Thunder.xml — FRM__03CT (CAFD 0000106D, author: Bundang Thunder X3)

**Module series coverage:** F15,F16,F25,F26,F48,F85,F86

### Automatic high-beam assistant
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3050: FLA_AUTO_AKTIV, bit 20, mask 00100000b -> `automatisch`
  * Group 3050: FLA_VERBAUT, bit 20, mask 00010000b -> `01`

## Bundang_Thunder.xml — FRM__03CT (CAFD 0000106D, author: Bundang Thunder X3)

**Module series coverage:** F15,F16,F25,F26,F48,F85,F86

### Turn on fog lights in welcome lighting
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3050: WL_FUNKTION_NSW, bit 29, mask 00001100b -> `soft_on_LED`

## Bundang_Thunder.xml — FRM__03CT (CAFD 0000106D, author: Bundang Thunder X3)

**Module series coverage:** F15,F16,F25,F26,F48,F85,F86

### Turn on headlights in welcome lighting
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3050: WL_FUNKTION_AL, bit 30, mask 00001100b -> `soft_on_LED`

## Bundang_Thunder.xml — FRM__03CT (CAFD 0000106D, author: Bundang Thunder X3)

**Module series coverage:** F15,F16,F25,F26,F48,F85,F86

### Activate hazard lights during hard braking
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3050: ESS_ERSCHEINUNGSBILD, bit 23, mask 01110000b -> `02`

## Bundang_Thunder.xml — FRM__03CT (CAFD 0000106D, author: Bundang Thunder X3)

**Module series coverage:** F15,F16,F25,F26,F48,F85,F86

### One-touch turn signal flashes five times
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3050: BLINKZYKLEN_ANZAHL_TIPP, bit 1, mask 00000111b -> `04`

## Bundang_Thunder.xml — HKFM (CAFD 000007C8, author: Bundang Thunder X3)

**Module series coverage:** F15,F16,F25,F26,F48,F85,F86

### Auto-close trunk (footwell switch + remote)                                                                   --** by Bundang Thunder ^^
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3010: TASTER_FBD, bit 0, mask 00001000b -> `01`
  * Group 3010: SCH_TOEHKI, bit 2, mask 00000100b -> `01`
  * Group 3010: SCH_FBD, bit 2, mask 00001000b -> `01`

## Bundang_Thunder.xml — HU_NBT_EVO (CAFD 00001EF6, author: Bundang Thunder X3)

**Module series coverage:** F15,F16,F25,F26,F48,F85,F86

### Set time automatically                                                                                         --** by Bundang Thunder ^^
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: SETTINGS_TIME_AUTOMATIC, bit 19, mask 00000110b -> `navigation`
  * Group 3000: CLOCK_CHANGE_AUTOMATIC, bit 105, mask 00100000b -> `01`

## Bundang_Thunder.xml — HU_NBT_EVO (CAFD 00001EF6, author: Bundang Thunder X3)

**Module series coverage:** F15,F16,F25,F26,F48,F85,F86

### Watch video/DMB/navigation while driving (up to 63 km/h)
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3006: SPEEDLOCK_X_KMH_MAX, bit 26, mask 11111111b -> `1F`
  * Group 3006: SPEEDLOCK_X_KMH_MIN, bit 25, mask 11111111b -> `3F`
  * Group 3000: VIDEO_FRONT_LOCKED, bit 5, mask 00010000b -> `00`
  * Group 3000: VIDEO_HANDBRAKE, bit 5, mask 00000100b -> `00`
  * Group 3000: VIDEO_SPEEDLOCK_CONDITION, bit 2, mask 00000111b -> `None`

## Bundang_Thunder.xml — HU_NBT_EVO (CAFD 00001EF6, author: Bundang Thunder X3)

**Module series coverage:** F15,F16,F25,F26,F48,F85,F86

### Suppress all warning messages
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3001: LEGAL_DISCLAIMER_TIME, bit 58, mask 11111111b -> `kein_ld`
  * Group 3001: MACRO_CAM_LEGALDISCLAIMER, bit 52, mask 11111111b -> `kein_ld`

## Bundang_Thunder.xml — HU_NBT_EVO (CAFD 00001EF6, author: Bundang Thunder X3)

**Module series coverage:** F15,F16,F25,F26,F48,F85,F86

### Enable trailer zoom menu when reversing
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3001: MACRO_TRAILER_COUPLING, bit 54, mask 00000001b -> `01`

## Bundang_Thunder.xml — HU_NBT_EVO (CAFD 00001EF6, author: Bundang Thunder X3)

**Module series coverage:** F15,F16,F25,F26,F48,F85,F86

### Close windows when it rains
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: REGEN_SCHLIESSEN, bit 19, mask 00001000b -> `01`

## Bundang_Thunder.xml — HU_NBT_EVO (CAFD 00001EF6, author: Bundang Thunder X3)

**Module series coverage:** F15,F16,F25,F26,F48,F85,F86

### X-Drive
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: COMPASS, bit 5, mask 00000001b -> `01`
  * Group 3000: X_VIEW, bit 15, mask 00000001b -> `01`
  * Group 3000: X_VIEW_GRAPHIC_SLOP, bit 26, mask 00110000b -> `trajectory1`
  * Group 3000: X_VIEW_GRAPHIC_ROLL, bit 26, mask 11000000b -> `trajectory1`
  * Group 3000: MOMENTDISTRIBUTION_MENU, bit 110, mask 00000010b -> `01`

## Bundang_Thunder.xml — HU_NBT_EVO (CAFD 00001EF6, author: Bundang Thunder X3)

**Module series coverage:** F15,F16,F25,F26,F48,F85,F86

### Enable USB video playback 1/2
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: ENT_CODEC_OGG, bit 15, mask 00010000b -> `01`
  * Group 3000: ENT_CODEC_XVID, bit 15, mask 00100000b -> `01`
  * Group 3000: ENT_CODEC_VCD, bit 15, mask 01000000b -> `01`
  * Group 3000: ENT_MC_VIDEO_SUPPORT, bit 33, mask 00000100b -> `01`

## Bundang_Thunder.xml — HU_NBT_EVO (CAFD 00001EF6, author: Bundang Thunder X3)

**Module series coverage:** F15,F16,F25,F26,F48,F85,F86

### Enable USB video playback 2/2
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3003: API_USB_VIDEO, bit 32, mask 00000110b -> `both`
  * Group 3003: API_IPOD_VIDEO, bit 32, mask 00011000b -> `both`

## Bundang_Thunder.xml — HU_NBT_EVO (CAFD 00001EF6, author: Bundang Thunder X3)

**Module series coverage:** F15,F16,F25,F26,F48,F85,F86

### Change warning chime to Rolls-Royce sound
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3002: SOUND_SIGNAL_SET, bit 26, mask 00111000b -> `rolls_royce`

## Bundang_Thunder.xml — HU_NBT_EVO (CAFD 00001EF6, author: Bundang Thunder X3)

**Module series coverage:** F15,F16,F25,F26,F48,F85,F86

### Configure Sport mode
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3008: MACRO_FDS, bit 79, mask 11000000b -> `popup_and_config`
  * Group 3009: EFF_DYN_SPORT_CID, bit 9, mask 00010000b -> `01`
  * Group 3009: EFF_DYN_SPORT_UNIT, bit 9, mask 00100000b -> `01`

## Bundang_Thunder.xml — HU_NBT_EVO (CAFD 00001EF6, author: Bundang Thunder X3)

**Module series coverage:** F15,F16,F25,F26,F48,F85,F86

### Startup animation
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3001: STARTUP_TYPE, bit 62, mask 00000110b -> `animation`
  * Group 3001: STARTUP_EMBLEM, bit 62, mask 01111000b -> `variant_01`

## Bundang_Thunder.xml — HU_NBT_EVO (CAFD 00001EF6, author: Bundang Thunder X3)

**Module series coverage:** F15,F16,F25,F26,F48,F85,F86

### Volume adjustment bar
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3002: VOLUME_POPUP_DISPLAY, bit 52, mask 01000000b -> `01`
  * Group 3002: VOLUME_POPUP_REJECTION, bit 52, mask 10000000b -> `01`
  * Group 3002: VOLUME_POPUP_EXCEPTION, bit 53, mask 00000001b -> `01`

## Bundang_Thunder.xml — HU_NBT_EVO (CAFD 00001EF6, author: Bundang Thunder X3)

**Module series coverage:** F15,F16,F25,F26,F48,F85,F86

### Show currently playing album art in iDrive
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: ENT_BTAS_IAP_COVERART, bit 9, mask 00000100b -> `01`
  * Group 3003: ENT_BTAS_METADATA, bit 19, mask 00000100b -> `01`
  * Group 3003: ENT_BTAS_BROWSING, bit 19, mask 00001000b -> `01`

## Bundang_Thunder.xml — HU_NBT_EVO (CAFD 00001EF6, author: Bundang Thunder X3)

**Module series coverage:** F15,F16,F25,F26,F48,F85,F86

### Display Sport mode
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3009: EFF_DYN_SPORT_CID, bit 9, mask 00010000b -> `01`

## Bundang_Thunder.xml — HU_NBT_EVO (CAFD 00001EF6, author: Bundang Thunder X3)

**Module series coverage:** F15,F16,F25,F26,F48,F85,F86

### Show phone, entertainment, and voice prompts in HUD
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 300C: HUD_ENTERTAINMENTLIST, bit 0, mask 00001000b -> `01`
  * Group 300C: HUD_VZA, bit 0, mask 10000000b -> `01`

## Bundang_Thunder.xml — HU_NBT_EVO (CAFD 00001EF6, author: Bundang Thunder X3)

**Module series coverage:** F15,F16,F25,F26,F48,F85,F86

### Show M logo in HUD
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 300C: HUD_M, bit 0, mask 00100000b -> `01`

## Bundang_Thunder.xml — HU_NBT_EVO (CAFD 00001EF6, author: Bundang Thunder X3)

**Module series coverage:** F15,F16,F25,F26,F48,F85,F86

### Show turn signals in HUD
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 300C: HUD_TURNSIGNAL, bit 0, mask 01000000b -> `01`

## Bundang_Thunder.xml — HU_NBT_EVO (CAFD 00001EF6, author: Bundang Thunder X3)

**Module series coverage:** F15,F16,F25,F26,F48,F85,F86

### Show TPMC tire pressure temperature
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3001: RDC_DRUCK_TEMP, bit 66, mask 00001100b -> `druck_und_temperatur`

## Bundang_Thunder.xml — HU_NBT_EVO (CAFD 00001EF6, author: Bundang Thunder X3)

**Module series coverage:** F15,F16,F25,F26,F48,F85,F86

### Output ringtone through speakers (iPhone only)
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3003: INBAND_RINGING, bit 6, mask 10000000b -> `01`

## Bundang_Thunder.xml — HU_NBT_EVO (CAFD 00001EF6, author: Bundang Thunder X3)

**Module series coverage:** F15,F16,F25,F26,F48,F85,F86

### Lock/unlock confirmation chime (requires piezo buzzer sensor)
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: ACOUSTICAL_LOCK_CONFIRM, bit 110, mask 00000001b -> `01`

## Bundang_Thunder.xml — HU_NBT_EVO (CAFD 00001EF6, author: Bundang Thunder X3)

**Module series coverage:** F15,F16,F25,F26,F48,F85,F86

### Change M Sport display cluster colors
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: M_VEHICLE, bit 33, mask 01000000b -> `01`

## Bundang_Thunder.xml — HU_NBT_EVO (CAFD 00001EF6, author: Bundang Thunder X3)

**Module series coverage:** F15,F16,F25,F26,F48,F85,F86

### Adjust high-beam assistant in iDrive
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: HIGH_BEAM_ASSISTANT, bit 109, mask 10000000b -> `01`

## Bundang_Thunder.xml — HU_NBT_EVO (CAFD 00001EF6, author: Bundang Thunder X3)

**Module series coverage:** F15,F16,F25,F26,F48,F85,F86

### Unlock DVD region code
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: ENT_VIDEO_DVD_AREA_CODE, bit 7, mask 11111111b -> `alle_anderen`

## Bundang_Thunder.xml — HU_NBT_EVO (CAFD 00001EF6, author: Bundang Thunder X3)

**Module series coverage:** F15,F16,F25,F26,F48,F85,F86

### Set sound system to Bang & Olufsen
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: HIGH_END_AUDIO_B_UND_W, bit 21, mask 01100000b -> `keine_insz`

## Bundang_Thunder.xml — HU_NBT_EVO (CAFD 00001EF6, author: Bundang Thunder X3)

**Module series coverage:** F15,F16,F25,F26,F48,F85,F86

### Enable Logic7 (S667A HiFi vehicles)
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: LOGIC7_SYMBOL, bit 22, mask 00001000b -> `01`

## Bundang_Thunder.xml — HU_NBT_EVO (CAFD 00001EF6, author: Bundang Thunder X3)

**Module series coverage:** F15,F16,F25,F26,F48,F85,F86

### Enhance audio mid-bass
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3002: AUDIO_SYSTEM, bit 29, mask 00111100b -> `highpremium`
  * Group 3002: AUDIO_SYSTEM_VAR, bit 21, mask 00000011b -> `variant3`

## Bundang_Thunder.xml — ICMQL (CAFD 0000067B, author: Bundang Thunder X3)

**Module series coverage:** F15,F16,F25,F26,F48,F85,F86

### Default to Eco mode at start                                                                              --** by Bundang Thunder ^^
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: IcmKod_B_InitEco, bit 36, mask 00001000b -> `verbaut`

## Bundang_Thunder.xml — ICMQL (CAFD 0000067B, author: Bundang Thunder X3)

**Module series coverage:** F15,F16,F25,F26,F48,F85,F86

### Enable cruise control
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: C_Fahrfunktion, bit 128, mask 00001110b -> `01`

## Bundang_Thunder.xml — ICMQL (CAFD 0000067B, author: Bundang Thunder X3)

**Module series coverage:** F15,F16,F25,F26,F48,F85,F86

### Enable Sport+ mode
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: IcmKod_B_S2TBA, bit 18, mask 11111111b -> `verbaut`

## Bundang_Thunder.xml — IHKA_HIGH (CAFD 000006DE, author: Bundang Thunder X3)

**Module series coverage:** F15,F16,F25,F26,F48,F85,F86

### Remember last air conditioning state                                                                               --** by Bundang Thunder ^^
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: OFF_MEMORY, bit 0, mask 00000001b -> `01`

## Bundang_Thunder.xml — IHKA_HIGH (CAFD 000006DE, author: Bundang Thunder X3)

**Module series coverage:** F15,F16,F25,F26,F48,F85,F86

### Prevent AUTO button from turning on A/C
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: AC_NICHT_EIN_BEI_UMLUFT, bit 18, mask 00100000b -> `01`

## Bundang_Thunder.xml — IHKA_HIGH (CAFD 000006DE, author: Bundang Thunder X3)

**Module series coverage:** F15,F16,F25,F26,F48,F85,F86

### Remember HVAC recirculation mode
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: UMLUFT_MEMORY, bit 0, mask 00000010b -> `01`

## Bundang_Thunder.xml — JBBFE (CAFD 00000014, author: Bundang Thunder X3)

**Module series coverage:** F15,F16,F25,F26,F48,F85,F86

### Allow rear windows to keep closing with door open                                                                --** by Bundang Thunder ^^
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3070: FH_TUERAUF_STOP_MAUT, bit 0, mask 00000100b -> `00`

## Bundang_Thunder.xml — JBBFE (CAFD 00000014, author: Bundang Thunder X3)

**Module series coverage:** F15,F16,F25,F26,F48,F85,F86

### Disable headlight washer
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: SCHEINWERFERREINIGUNG, bit 8, mask 00000001b -> `00`

## Bundang_Thunder.xml — KAFAS2 (CAFD 00001148, author: Bundang Thunder X3)

**Module series coverage:** F15,F16,F25,F26,F48,F85,F86

### High-beam assistant                                                                                     --** by Bundang Thunder ^^
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3050: FLA_ON_OFF, bit 1, mask 00000001b -> `FLA_on`
  * Group 3050: SPEED_SWITCHING_HIGH_BEAMS_ON, bit 6, mask 11111111b -> `CN`
  * Group 3050: SPEED_SWITCHING_HIGH_BEAMS_OFF, bit 7, mask 11111111b -> `China`

## Bundang_Thunder.xml — KAFAS2 (CAFD 00001148, author: Bundang Thunder X3)

**Module series coverage:** F15,F16,F25,F26,F48,F85,F86

### Lane departure warning
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3020: FLA_ON_OFF, bit 2, mask 00000011b -> `detection_for_grass_edge_and_curb_stone`

## Bundang_Thunder.xml — KAFAS2 (CAFD 00001148, author: Bundang Thunder X3)

**Module series coverage:** F15,F16,F25,F26,F48,F85,F86

### Show speed limit info using camera only
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3010: COD_CAM_ONLY, bit 1, mask 10000000b -> `camera_only`

## Bundang_Thunder.xml — KOMBI L6 BO (CAFD 00000069, author: Bundang Thunder X3)

**Module series coverage:** F15,F16,F25,F26,F48,F85,F86

### Show phone, entertainment, and voice prompts in HUD                                                               --** by Bundang Thunder ^^
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: HUD_ENTERTAINMENT_ENABLE, bit 41, mask 00001000b -> `01`
  * Group 3000: HUD_TLC_ENABLE, bit 41, mask 00000001b -> `01`
  * Group 3000: HUD_VZA_ENABLE, bit 40, mask 10000000b -> `01`

## Bundang_Thunder.xml — KOMBI L6 BO (CAFD 00000069, author: Bundang Thunder X3)

**Module series coverage:** F15,F16,F25,F26,F48,F85,F86

### Show turn signals in HUD
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: BLINKER_HUD_ENABLE, bit 42, mask 00100000b -> `01`
  * Group 3008: HUD_PIA_BLINKER, bit 5, mask 00000001b -> `01`

## Bundang_Thunder.xml — KOMBI L6 BO (CAFD 00000069, author: Bundang Thunder X3)

**Module series coverage:** F15,F16,F25,F26,F48,F85,F86

### Show logo on instrument cluster
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3003: MPM_ENABLE, bit 9, mask 00000001b -> `01`
  * Group 3000: MPM_LOGO, bit 53, mask 11110000b -> `bmw`
  * Group 3000: BMW_LOGO, bit 53, mask 00001111b -> `mpm`

## Bundang_Thunder.xml — KOMBI L6 BO (CAFD 00000069, author: Bundang Thunder X3)

**Module series coverage:** F15,F16,F25,F26,F48,F85,F86

### Show compass in instrument cluster
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3003: KOMPASS_GRAPH_ENABLE, bit 9, mask 01000000b -> `01`

## Bundang_Thunder.xml — KOMBI L6 BO (CAFD 00000069, author: Bundang Thunder X3)

**Module series coverage:** F15,F16,F25,F26,F48,F85,F86

### Disable warning chime below 3 degrees
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: CC_TEMPERATURWARNUNG, bit 42, mask 00000100b -> `00`

## Bundang_Thunder.xml — KOMBI L6 BO (CAFD 00000069, author: Bundang Thunder X3)

**Module series coverage:** F15,F16,F25,F26,F48,F85,F86

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
  * Group 3007: FDS_MENUE, bit 35, mask 11111111b -> `menue_3`

## Bundang_Thunder.xml — KOMBI L6 BO (CAFD 00000069, author: Bundang Thunder X3)

**Module series coverage:** F15,F16,F25,F26,F48,F85,F86

### Instrument cluster daytime lower color: gray
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: HINTERGRUND_FARBE_TAG, bit 41, mask 00000010b -> `01`

## Bundang_Thunder.xml — KOMBI L6 BO (CAFD 00000069, author: Bundang Thunder X3)

**Module series coverage:** F15,F16,F25,F26,F48,F85,F86

### Instrument cluster daytime lower color: orange
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: HINTERGRUND_FARBE_TAG, bit 41, mask 00000010b -> `00`

## Bundang_Thunder.xml — KOMBI L6 BO (CAFD 00000069, author: Bundang Thunder X3)

**Module series coverage:** F15,F16,F25,F26,F48,F85,F86

### Instrument cluster nighttime lower color: gray
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: HINTERGRUND_FARBE_NACHT, bit 41, mask 00000100b -> `01`

## Bundang_Thunder.xml — KOMBI L6 BO (CAFD 00000069, author: Bundang Thunder X3)

**Module series coverage:** F15,F16,F25,F26,F48,F85,F86

### Instrument cluster nighttime lower color: orange
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: HINTERGRUND_FARBE_NACHT, bit 41, mask 00000100b -> `00`

## Bundang_Thunder.xml — CFAS_PLX_1 (CAFD 000000B5, author: Bundang Thunder X3)

**Module series coverage:** F15,F16,F25,F26,F48,F85,F86

### Enable Easy Access                                                                         --** by Bundang Thunder ^^
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: EINAUSSTIEGSHILFE, bit 0, mask 00011100b -> `Modus_FA_SLV`

## Bundang_Thunder.xml — CFAS_PLX_1 (CAFD 000000B5, author: Bundang Thunder X3)

**Module series coverage:** F15,F16,F25,F26,F48,F85,F86

### Easy Access seat starts moving from end position
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3012: EAH_SCHUTZFREIRAUM_HINTEN_SLV_PHYS, bits 4-5, mask 11111111b -> `00, 01`

## Bundang_Thunder.xml — CFAS_PLX_1 (CAFD 000000B5, author: Bundang Thunder X3)

**Module series coverage:** F15,F16,F25,F26,F48,F85,F86

### Easy Access seat starts moving with 1 cm remaining
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3012: EAH_SCHUTZFREIRAUM_HINTEN_SLV_PHYS, bits 4-5, mask 11111111b -> `00, 0A`

## Bundang_Thunder.xml — CFAS_PLX_1 (CAFD 000000B5, author: Bundang Thunder X3)

**Module series coverage:** F15,F16,F25,F26,F48,F85,F86

### Easy Access seat starts moving with 2 cm remaining
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3012: EAH_SCHUTZFREIRAUM_HINTEN_SLV_PHYS, bits 4-5, mask 11111111b -> `00, 14`

## Bundang_Thunder.xml — CFAS_PLX_1 (CAFD 000000B5, author: Bundang Thunder X3)

**Module series coverage:** F15,F16,F25,F26,F48,F85,F86

### Easy Access seat starts moving with 3 cm remaining
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3012: EAH_SCHUTZFREIRAUM_HINTEN_SLV_PHYS, bits 4-5, mask 11111111b -> `00, 1E`

## Bundang_Thunder.xml — CFAS_PLX_1 (CAFD 000000B5, author: Bundang Thunder X3)

**Module series coverage:** F15,F16,F25,F26,F48,F85,F86

### Easy Access seat travel distance: 4 cm
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3012: EAH_VERFAHRWEG_SLV_PHYS, bits 0-1, mask 11111111b -> `00, 28`

## Bundang_Thunder.xml — CFAS_PLX_1 (CAFD 000000B5, author: Bundang Thunder X3)

**Module series coverage:** F15,F16,F25,F26,F48,F85,F86

### Easy Access seat travel distance: 5 cm
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3012: EAH_VERFAHRWEG_SLV_PHYS, bits 0-1, mask 11111111b -> `00, 32`

## Bundang_Thunder.xml — CFAS_PLX_1 (CAFD 000000B5, author: Bundang Thunder X3)

**Module series coverage:** F15,F16,F25,F26,F48,F85,F86

### Easy Access seat travel distance: 6 cm
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3012: EAH_VERFAHRWEG_SLV_PHYS, bits 0-1, mask 11111111b -> `00, 3C`

## Bundang_Thunder.xml — CFAS_PLX_1 (CAFD 000000B5, author: Bundang Thunder X3)

**Module series coverage:** F15,F16,F25,F26,F48,F85,F86

### Easy Access seat travel distance: 7 cm
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3012: EAH_VERFAHRWEG_SLV_PHYS, bits 0-1, mask 11111111b -> `00, 46`

## Bundang_Thunder.xml — CFAS_PLX_1 (CAFD 000000B5, author: Bundang Thunder X3)

**Module series coverage:** F15,F16,F25,F26,F48,F85,F86

### Gentleman
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: GENTLEMAN, bit 1, mask 00000001b -> `01`
  * Group 3000: MEMORY, bit 0, mask 00000001b -> `01`

## Bundang_Thunder.xml — CFAS_PLX_1 (CAFD 000000B5, author: Bundang Thunder X3)

**Module series coverage:** F15,F16,F25,F26,F48,F85,F86

### Set gong when saving seat position
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: MEMORY_GONG, bit 2, mask 00001000b -> `01`

## Bundang_Thunder.xml — CBFS_PLX_1 (CAFD 000000B6, author: Bundang Thunder X3)

**Module series coverage:** F15,F16,F25,F26,F48,F85,F86

### Passenger seat Gentleman                                                                                         --** by Bundang Thunder ^^
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: GENTLEMAN, bit 1, mask 00000001b -> `01`
  * Group 3000: MEMORY, bit 0, mask 00000001b -> `01`

## Bundang_Thunder.xml — CFAS_PLX_1 (CAFD 000000B5, author: Bundang Thunder X3)

**Module series coverage:** F15,F16,F25,F26,F48,F85,F86

### Link Gentleman function to SM2                                                                                 --** by Bundang Thunder ^^
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: GENTLEMAN, bit 1, mask 00000001b -> `01`
  * Group 3000: MEMORY, bit 0, mask 00000001b -> `01`

## Bundang_Thunder.xml — ACSM_4C (CAFD 00000909, author: Bundang Thunder X5)

**Module series coverage:** F15,F16,F25,F26,F48,F85,F86

### Seat belt warning chime for only 5 seconds                                                                                 --** by Bundang Thunder ^^
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: GWF_SBR_WARNDAUER, bit 3, mask 11111111b -> `05`

## Bundang_Thunder.xml — ACSM_4C (CAFD 00000909, author: Bundang Thunder X5)

**Module series coverage:** F15,F16,F25,F26,F48,F85,F86

### Delete driver seat belt warning light
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: SBR_PreWarning_Fahrer, bit 16, mask 00000001b -> `00`

## Bundang_Thunder.xml — ACSM_4C (CAFD 00000909, author: Bundang Thunder X5)

**Module series coverage:** F15,F16,F25,F26,F48,F85,F86

### Delete passenger seat belt warning light
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: SBR_PreWarning_Beifahrer, bit 16, mask 00000010b -> `00`

## Bundang_Thunder.xml — ACSM_4C (CAFD 00000909, author: Bundang Thunder X5)

**Module series coverage:** F15,F16,F25,F26,F48,F85,F86

### Disable driver seat belt warning chime
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: SeatBeltReminder_SBR_Fahrer, bit 15, mask 00000010b -> `00`

## Bundang_Thunder.xml — ACSM_4C (CAFD 00000909, author: Bundang Thunder X5)

**Module series coverage:** F15,F16,F25,F26,F48,F85,F86

### Disable passenger seat belt warning chime
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: SeatBeltReminder_SBR_Beifahrer, bit 15, mask 00000100b -> `00`

## Bundang_Thunder.xml — BDC_01 (CAFD 000017BE, author: Bundang Thunder X5)

**Module series coverage:** F15,F16,F25,F26,F48,F85,F86

### Activate hazard lights during hard braking                                                                                   --** by Bundang Thunder ^^
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3068: WB_GB_ENABLE, bit 26, mask 00000001b -> `01`

## Bundang_Thunder.xml — BDC_01 (CAFD 000017BE, author: Bundang Thunder X5)

**Module series coverage:** F15,F16,F25,F26,F48,F85,F86

### Limit passenger mirror tilt to 30 degrees in reverse
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3110: ASP_BORDSTEINAUTOMATIK_DELTA, bit 1, mask 11111111b -> `1E`

## Bundang_Thunder.xml — BDC_01 (CAFD 000017BE, author: Bundang Thunder X5)

**Module series coverage:** F15,F16,F25,F26,F48,F85,F86

### One-touch turn signal flashes five times
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3069: PIA_DEFAULT_TIPPBLINKEN, bit 215, mask 00011000b -> `Tippblinken_fuenfmal`

## Bundang_Thunder.xml — BDC_01 (CAFD 000017BE, author: Bundang Thunder X5)

**Module series coverage:** F15,F16,F25,F26,F48,F85,F86

### Enable welcome lights
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3068: WL_WIEDERHOLSPERRE_01, bit 13, mask 00100000b -> `01`

## Bundang_Thunder.xml — BDC_01 (CAFD 000017BE, author: Bundang Thunder X5)

**Module series coverage:** F15,F16,F25,F26,F48,F85,F86

### Enable follow me home
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3068: FMH_WIEDERHOLSPERRE_01, bit 13, mask 01000000b -> `01`

## Bundang_Thunder.xml — BDC_01 (CAFD 000017BE, author: Bundang Thunder X5)

**Module series coverage:** F15,F16,F25,F26,F48,F85,F86

### Close trunk immediately via remote
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 30D0: RC_TIME_DELAY_BOOTLID, bit 18, mask 111111!1b -> `01`

## Bundang_Thunder.xml — BDC_01 (CAFD 000017BE, author: Bundang Thunder X5)

**Module series coverage:** F15,F16,F25,F26,F48,F85,F86

### Open and close windows with remote
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3056: KOMFORTOEFFNUNG_FB, bit 0, mask 01000000b -> `01`

## Bundang_Thunder.xml — BDC_01 (CAFD 000017BE, author: Bundang Thunder X5)

**Module series coverage:** F15,F16,F25,F26,F48,F85,F86

### Fold mirrors immediately when locking (lock folding)
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3056: KOMFORT_SCHLIESSEN, bit 10, mask 11111111b -> `00`

## Bundang_Thunder.xml — BDC_01 (CAFD 000017BE, author: Bundang Thunder X5)

**Module series coverage:** F15,F16,F25,F26,F48,F85,F86

### Allow windows to keep closing with doors open (front and rear)
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3050: FH_TUERAUF_STOP_MAUT, bit 0, mask 00000001b -> `00`
  * Group 3051: FH_TUERAUF_STOP_MAUT_REAR, bit 0, mask 00000001b -> `00`

## Bundang_Thunder.xml — BDC_01 (CAFD 000017BE, author: Bundang Thunder X5)

**Module series coverage:** F15,F16,F25,F26,F48,F85,F86

### VLD
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3073: LUT_FLC_FORWARDLIGHTING_Y, bits 40-42, mask 11111111b -> `F015_ohne_AFS`
  * Group 3073: C_AFS_ENA, bit 152, mask 00000001b -> `F015_enable`

## Bundang_Thunder.xml — BDC_01 (CAFD 000017BE, author: Bundang Thunder X5)

**Module series coverage:** F15,F16,F25,F26,F48,F85,F86

### Turn on door handle lights when reversing
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3070: OVT_BEI_RUECKFAHRLICHT, bit 128, mask 00000001b -> `F015_ohne_AFS`

## Bundang_Thunder.xml — BDC_01 (CAFD 000017BE, author: Bundang Thunder X5)

**Module series coverage:** F15,F16,F25,F26,F48,F85,F86

### Disable auto start/stop in Comfort mode
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3023: TCM_MSA_DEFAULT_OFF, bit 0, mask 00010000b -> `01`

## Bundang_Thunder.xml — BDC_01 (CAFD 000017BE, author: Bundang Thunder X5)

**Module series coverage:** F15,F16,F25,F26,F48,F85,F86

### Disable auto start/stop in Eco Pro mode
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3023: TCM_MSA_ECO_MODE, bit 1, mask 00001100b -> `00`

## Bundang_Thunder.xml — BDC_01 (CAFD 000017BE, author: Bundang Thunder X5)

**Module series coverage:** F15,F16,F25,F26,F48,F85,F86

### Remember last auto start/stop state
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3023: TCM_MSA_MEMORY, bit 0, mask 00100000b -> `01`

## Bundang_Thunder.xml — BDC_01 (CAFD 000017BE, author: Bundang Thunder X5)

**Module series coverage:** F15,F16,F25,F26,F48,F85,F86

### Double horn when locking with engine running - enable
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3040: VAM_HORN_AT_SECURE, bit 0, mask 00000100b -> `01`

## Bundang_Thunder.xml — BDC_01 (CAFD 000017BE, author: Bundang Thunder X5)

**Module series coverage:** F15,F16,F25,F26,F48,F85,F86

### Double horn when locking with engine running - disable
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3040: VAM_HORN_AT_SECURE, bit 0, mask 00000100b -> `00`

## Bundang_Thunder.xml — HKFM (CAFD 000007C8, author: Bundang Thunder X5)

**Module series coverage:** F15,F16,F25,F26,F48,F85,F86

### Auto-close trunk (footwell switch + remote)                                                                   --** by Bundang Thunder ^^
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3010: TASTER_FBD, bit 0, mask 00001000b -> `01`
  * Group 3010: SCH_TOEHKI, bit 2, mask 00000100b -> `01`
  * Group 3010: SCH_FBD, bit 2, mask 00001000b -> `01`

## Bundang_Thunder.xml — HU_NBT (CAFD 00000DED, author: Bundang Thunder X5)

**Module series coverage:** F15,F16,F25,F26,F48,F85,F86

### Set time automatically                                                                                         --** by Bundang Thunder ^^
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: SETTINGS_TIME_AUTOMATIC, bit 19, mask 00000110b -> `navigation`
  * Group 3000: CLOCK_CHANGE_AUTOMATIC, bit 105, mask 00100000b -> `01`

## Bundang_Thunder.xml — HU_NBT (CAFD 00000DED, author: Bundang Thunder X5)

**Module series coverage:** F15,F16,F25,F26,F48,F85,F86

### Watch video/DMB/navigation while driving
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: SPEEDLOCK_X_KMH_MAX, bit 72, mask 11111111b -> `FF`
  * Group 3000: SPEEDLOCK_X_KMH_MIN, bit 71, mask 11111111b -> `FF`
  * Group 3000: VIDEO_FRONT_LOCKED, bit 5, mask 00010000b -> `00`
  * Group 3000: VIDEO_HANDBRAKE, bit 5, mask 00000100b -> `00`
  * Group 3000: VIDEO_SPEEDLOCK_CONDITION, bit 57, mask 00000111b -> `None`

## Bundang_Thunder.xml — HU_NBT (CAFD 00000DED, author: Bundang Thunder X5)

**Module series coverage:** F15,F16,F25,F26,F48,F85,F86

### Suppress all warning messages
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3001: LEGAL_DISCLAIMER_TIME, bit 58, mask 11111111b -> `kein_ld`
  * Group 3001: MACRO_CAM_LEGALDISCLAIMER, bit 52, mask 11111111b -> `kein_ld`

## Bundang_Thunder.xml — HU_NBT (CAFD 00000DED, author: Bundang Thunder X5)

**Module series coverage:** F15,F16,F25,F26,F48,F85,F86

### Enable trailer zoom menu when reversing
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3001: MACRO_TRAILER_COUPLING, bit 54, mask 00000001b -> `01`

## Bundang_Thunder.xml — HU_NBT (CAFD 00000DED, author: Bundang Thunder X5)

**Module series coverage:** F15,F16,F25,F26,F48,F85,F86

### Close windows when it rains
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: REGEN_SCHLIESSEN, bit 19, mask 00001000b -> `01`

## Bundang_Thunder.xml — HU_NBT (CAFD 00000DED, author: Bundang Thunder X5)

**Module series coverage:** F15,F16,F25,F26,F48,F85,F86

### X-Drive
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: COMPASS, bit 5, mask 00000001b -> `01`
  * Group 3000: X_VIEW, bit 15, mask 00000001b -> `01`
  * Group 3000: X_VIEW_GRAPHIC_SLOP, bit 26, mask 00110000b -> `trajectory1`
  * Group 3000: X_VIEW_GRAPHIC_ROLL, bit 26, mask 11000000b -> `trajectory1`
  * Group 3000: MOMENTDISTRIBUTION_MENU, bit 110, mask 00000010b -> `01`

## Bundang_Thunder.xml — HU_NBT (CAFD 00000DED, author: Bundang Thunder X5)

**Module series coverage:** F15,F16,F25,F26,F48,F85,F86

### Enable USB video playback 1/2
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: ENT_CODEC_OGG, bit 15, mask 00010000b -> `01`
  * Group 3000: ENT_CODEC_XVID, bit 15, mask 00100000b -> `01`
  * Group 3000: ENT_CODEC_VCD, bit 15, mask 01000000b -> `01`
  * Group 3000: ENT_MC_VIDEO_SUPPORT, bit 13, mask 00000100b -> `01`

## Bundang_Thunder.xml — HU_NBT (CAFD 00000DED, author: Bundang Thunder X5)

**Module series coverage:** F15,F16,F25,F26,F48,F85,F86

### Enable USB video playback 2/2
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3003: API_USB_VIDEO, bit 33, mask 00000110b -> `both`
  * Group 3003: API_IPOD_VIDEO, bit 33, mask 00011000b -> `both`

## Bundang_Thunder.xml — HU_NBT (CAFD 00000DED, author: Bundang Thunder X5)

**Module series coverage:** F15,F16,F25,F26,F48,F85,F86

### Change warning chime to Rolls-Royce sound
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3002: SOUND_SIGNAL_SET, bit 26, mask 00111000b -> `rolls_royce`

## Bundang_Thunder.xml — HU_NBT (CAFD 00000DED, author: Bundang Thunder X5)

**Module series coverage:** F15,F16,F25,F26,F48,F85,F86

### Configure Sport mode
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3001: MACRO_FDS, bit 55, mask 00011000b -> `popup_and_config`
  * Group 3000: EFF_DYN_SPORT_CID, bit 101, mask 00010000b -> `01`
  * Group 3000: EFF_DYN_SPORT_UNIT, bit 107, mask 00000100b -> `01`

## Bundang_Thunder.xml — HU_NBT (CAFD 00000DED, author: Bundang Thunder X5)

**Module series coverage:** F15,F16,F25,F26,F48,F85,F86

### Startup animation
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3001: STARTUP_TYPE, bit 62, mask 00000110b -> `animation`
  * Group 3001: STARTUP_EMBLEM, bit 62, mask 01111000b -> `variant_01`

## Bundang_Thunder.xml — HU_NBT (CAFD 00000DED, author: Bundang Thunder X5)

**Module series coverage:** F15,F16,F25,F26,F48,F85,F86

### Volume adjustment bar
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3002: VOLUME_POPUP_DISPLAY, bit 52, mask 01000000b -> `01`
  * Group 3002: VOLUME_POPUP_REJECTION, bit 52, mask 10000000b -> `01`
  * Group 3002: VOLUME_POPUP_EXCEPTION, bit 53, mask 00000001b -> `01`

## Bundang_Thunder.xml — HU_NBT (CAFD 00000DED, author: Bundang Thunder X5)

**Module series coverage:** F15,F16,F25,F26,F48,F85,F86

### Show TPMC tire pressure temperature
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3001: RDC_DRUCK_TEMP, bit 66, mask 00001100b -> `druck_und_temperatur`

## Bundang_Thunder.xml — HU_NBT (CAFD 00000DED, author: Bundang Thunder X5)

**Module series coverage:** F15,F16,F25,F26,F48,F85,F86

### Output ringtone through speakers (iPhone only)
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3003: INBAND_RINGING, bit 6, mask 10000000b -> `01`

## Bundang_Thunder.xml — HU_NBT (CAFD 00000DED, author: Bundang Thunder X5)

**Module series coverage:** F15,F16,F25,F26,F48,F85,F86

### Lock/unlock confirmation chime (requires piezo buzzer sensor)
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: ACOUSTICAL_LOCK_CONFIRM, bit 110, mask 00000001b -> `01`

## Bundang_Thunder.xml — HU_NBT (CAFD 00000DED, author: Bundang Thunder X5)

**Module series coverage:** F15,F16,F25,F26,F48,F85,F86

### Change M Sport display cluster colors
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: M_VEHICLE, bit 133, mask 01000000b -> `01`

## Bundang_Thunder.xml — HU_NBT (CAFD 00000DED, author: Bundang Thunder X5)

**Module series coverage:** F15,F16,F25,F26,F48,F85,F86

### Adjust high-beam assistant in iDrive
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: HIGH_BEAM_ASSISTANT, bit 109, mask 10000000b -> `01`

## Bundang_Thunder.xml — HU_NBT (CAFD 00000DED, author: Bundang Thunder X5)

**Module series coverage:** F15,F16,F25,F26,F48,F85,F86

### Show currently playing album art in iDrive
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: ENT_BTAS_IAP_COVERART, bit 9, mask 00000100b -> `01`
  * Group 3003: ENT_BTAS_METADATA, bit 19, mask 00000100b -> `01`
  * Group 3003: ENT_BTAS_BROWSING, bit 19, mask 00001000b -> `01`

## Bundang_Thunder.xml — HU_NBT (CAFD 00000DED, author: Bundang Thunder X5)

**Module series coverage:** F15,F16,F25,F26,F48,F85,F86

### Unlock DVD region code
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: ENT_VIDEO_DVD_AREA_CODE, bit 7, mask 11111111b -> `alle_anderen`

## Bundang_Thunder.xml — HU_NBT (CAFD 00000DED, author: Bundang Thunder X5)

**Module series coverage:** F15,F16,F25,F26,F48,F85,F86

### Show turn signals in HUD
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3001: HUD_TURNSIGNAL, bit 55, mask 10000000b -> `01`

## Bundang_Thunder.xml — HU_NBT (CAFD 00000DED, author: Bundang Thunder X5)

**Module series coverage:** F15,F16,F25,F26,F48,F85,F86

### Set sound system to Bang & Olufsen
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: HIGH_END_AUDIO_B_UND_W, bit 21, mask 01100000b -> `keine_insz`

## Bundang_Thunder.xml — HU_NBT (CAFD 00000DED, author: Bundang Thunder X5)

**Module series coverage:** F15,F16,F25,F26,F48,F85,F86

### Enable Logic7 (S667A HiFi vehicles)
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: LOGIC7_SYMBOL, bit 22, mask 00001000b -> `01`

## Bundang_Thunder.xml — HU_NBT (CAFD 00000DED, author: Bundang Thunder X5)

**Module series coverage:** F15,F16,F25,F26,F48,F85,F86

### Enhance audio mid-bass
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3002: AUDIO_SYSTEM, bit 29, mask 00111100b -> `highpremium`
  * Group 3002: AUDIO_SYSTEM_VAR, bit 21, mask 00000011b -> `variant3`

## Bundang_Thunder.xml — ICMQL (CAFD 0000067B, author: Bundang Thunder X5)

**Module series coverage:** F15,F16,F25,F26,F48,F85,F86

### Default to Eco mode at start                                                                              --** by Bundang Thunder ^^
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: IcmKod_B_InitEco, bit 36, mask 00001000b -> `verbaut`

## Bundang_Thunder.xml — ICMQL (CAFD 0000067B, author: Bundang Thunder X5)

**Module series coverage:** F15,F16,F25,F26,F48,F85,F86

### Enable cruise control
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: C_Fahrfunktion, bit 128, mask 00001110b -> `01`

## Bundang_Thunder.xml — ICMQL (CAFD 0000067B, author: Bundang Thunder X5)

**Module series coverage:** F15,F16,F25,F26,F48,F85,F86

### Enable cruise control
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: C_Fahrfunktion, bit 128, mask 00001110b -> `04`

## Bundang_Thunder.xml — ICMQL (CAFD 0000067B, author: Bundang Thunder X5)

**Module series coverage:** F15,F16,F25,F26,F48,F85,F86

### Enable Sport+ mode
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: IcmKod_B_S2TBA, bit 18, mask 11111111b -> `verbaut`

## Bundang_Thunder.xml — ICMQL (CAFD 0000067B, author: Bundang Thunder X5)

**Module series coverage:** F15,F16,F25,F26,F48,F85,F86

### ACC distance
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: C_Abstandsstufe_init, bit 184, mask 00000111b -> `01`

## Bundang_Thunder.xml — ICMQL (CAFD 0000067B, author: Bundang Thunder X5)

**Module series coverage:** F15,F16,F25,F26,F48,F85,F86

### Adjust active blind spot activation speed by -20 km/h
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: C_ZSW_01ierunggeschwindigkeit_Funktion_low, bit 190, mask 00111111b -> `01`

## Bundang_Thunder.xml — ICMQL (CAFD 0000067B, author: Bundang Thunder X5)

**Module series coverage:** F15,F16,F25,F26,F48,F85,F86

### Enable coasting mode
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: C_Segeln_vorhanden, bit 120, mask 11000000b -> `01`

## Bundang_Thunder.xml — IHKA_CBF (CAFD 000047D6, author: Bundang Thunder X5)

**Module series coverage:** F15,F16,F25,F26,F48,F85,F86

### Remember last air conditioning state                                                                               --** by Bundang Thunder ^^
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: OFF_MEMORY, bit 5, mask 00010000b -> `01`

## Bundang_Thunder.xml — IHKA_CBF (CAFD 000047D6, author: Bundang Thunder X5)

**Module series coverage:** F15,F16,F25,F26,F48,F85,F86

### Prevent AUTO button from turning on A/C
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: AC_NICHT_EIN_BEI_AUTO, bit 5, mask 00001000b -> `01`

## Bundang_Thunder.xml — IHKA_CBF (CAFD 000047D6, author: Bundang Thunder X5)

**Module series coverage:** F15,F16,F25,F26,F48,F85,F86

### Remember HVAC recirculation mode
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: MEMORY_UMLUFT, bit 0, mask 00000100b -> `01`

## Bundang_Thunder.xml — JBBFE (CAFD 00000014, author: Bundang Thunder X5)

**Module series coverage:** F15,F16,F25,F26,F48,F85,F86

### Disable headlight washer                                                                                --** by Bundang Thunder ^^
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: SCHEINWERFERREINIGUNG, bit 8, mask 00000001b -> `00`

## Bundang_Thunder.xml — KAFAS2 (CAFD 00001148, author: Bundang Thunder X5)

**Module series coverage:** F15,F16,F25,F26,F48,F85,F86

### Automatic high-beam assistant                                                                                --** by Bundang Thunder ^^
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3050: FLA_ON_OFF, bit 1, mask 00000001b -> `FLA_on`
  * Group 3050: SPEED_SWITCHING_HIGH_BEAMS_ON, bit 6, mask 11111111b -> `CN`
  * Group 3050: SPEED_SWITCHING_HIGH_BEAMS_OFF, bit 7, mask 11111111b -> `China`

## Bundang_Thunder.xml — KOMBI FPK_I12 (CAFD 00001060, author: Bundang Thunder X5)

**Module series coverage:** F15,F16,F25,F26,F48,F85,F86

### Show phone, entertainment, and voice prompts in HUD                                                               --** by Bundang Thunder ^^
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3003: HUD_ENTERTAINMENT_ENABLE, bit 10, mask 00000001b -> `01`
  * Group 3003: HUD_STARTUP_ENABLE, bit 9, mask 00100000b -> `01`
  * Group 3000: HUD_TLC_ENABLE, bit 41, mask 00000001b -> `01`
  * Group 3000: HUD_VZA_ENABLE, bit 40, mask 10000000b -> `01`

## Bundang_Thunder.xml — KOMBI FPK_I12 (CAFD 00001060, author: Bundang Thunder X5)

**Module series coverage:** F15,F16,F25,F26,F48,F85,F86

### Show turn signals in HUD
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3003: HUD_BLINKER_ENABLE, bit 11, mask 00000001b -> `01`
  * Group 3008: HUD_PIA_BLINKER, bit 5, mask 00000001b -> `01`

## Bundang_Thunder.xml — KOMBI FPK_I12 (CAFD 00001060, author: Bundang Thunder X5)

**Module series coverage:** F15,F16,F25,F26,F48,F85,F86

### Show logo on instrument cluster
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3003: MPM_ENABLE, bit 3, mask 00000010b -> `01`
  * Group 3000: MPM_LOGO, bit 44, mask 11110000b -> `mpm_x5`
  * Group 3000: BMW_LOGO, bit 44, mask 00001111b -> `mpm_x5`

## Bundang_Thunder.xml — KOMBI FPK_I12 (CAFD 00001060, author: Bundang Thunder X5)

**Module series coverage:** F15,F16,F25,F26,F48,F85,F86

### Show compass in instrument cluster
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3003: KOMPASS_GRAPH_ENABLE, bit 12, mask 00010000b -> `01`

## Bundang_Thunder.xml — KOMBI FPK_I12 (CAFD 00001060, author: Bundang Thunder X5)

**Module series coverage:** F15,F16,F25,F26,F48,F85,F86

### Disable warning chime below 3 degrees
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: CC_TEMPERATURWARNUNG, bit 50, mask 00000001b -> `00`

## Bundang_Thunder.xml — KOMBI FPK_I12 (CAFD 00001060, author: Bundang Thunder X5)

**Module series coverage:** F15,F16,F25,F26,F48,F85,F86

### Show power output in instrument cluster
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3003: MOTORLEISTUNG_ENABLE, bit 11, mask 00000010b -> `01`

## Bundang_Thunder.xml — KOMBI FPK_I12 (CAFD 00001060, author: Bundang Thunder X5)

**Module series coverage:** F15,F16,F25,F26,F48,F85,F86

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
  * Group 300C: FDS_MENUE, bit 51, mask 11111111b -> `menue_3`

## Bundang_Thunder.xml — CFAS_PLX_1 (CAFD 000000B5, author: Bundang Thunder X5)

**Module series coverage:** F15,F16,F25,F26,F48,F85,F86

### Enable Easy Access                                                                         --** by Bundang Thunder ^^
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: EINAUSSTIEGSHILFE, bit 0, mask 00011100b -> `Modus_FA_SLV`

## Bundang_Thunder.xml — CFAS_PLX_1 (CAFD 000000B5, author: Bundang Thunder X5)

**Module series coverage:** F15,F16,F25,F26,F48,F85,F86

### Easy Access seat starts moving from end position
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3012: EAH_SCHUTZFREIRAUM_HINTEN_SLV_PHYS, bits 4-5, mask 11111111b -> `00, 01`

## Bundang_Thunder.xml — CFAS_PLX_1 (CAFD 000000B5, author: Bundang Thunder X5)

**Module series coverage:** F15,F16,F25,F26,F48,F85,F86

### Easy Access seat starts moving with 1 cm remaining
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3012: EAH_SCHUTZFREIRAUM_HINTEN_SLV_PHYS, bits 4-5, mask 11111111b -> `00, 0A`

## Bundang_Thunder.xml — CFAS_PLX_1 (CAFD 000000B5, author: Bundang Thunder X5)

**Module series coverage:** F15,F16,F25,F26,F48,F85,F86

### Easy Access seat starts moving with 2 cm remaining
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3012: EAH_SCHUTZFREIRAUM_HINTEN_SLV_PHYS, bits 4-5, mask 11111111b -> `00, 14`

## Bundang_Thunder.xml — CFAS_PLX_1 (CAFD 000000B5, author: Bundang Thunder X5)

**Module series coverage:** F15,F16,F25,F26,F48,F85,F86

### Easy Access seat starts moving with 3 cm remaining
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3012: EAH_SCHUTZFREIRAUM_HINTEN_SLV_PHYS, bits 4-5, mask 11111111b -> `00, 1E`

## Bundang_Thunder.xml — CFAS_PLX_1 (CAFD 000000B5, author: Bundang Thunder X5)

**Module series coverage:** F15,F16,F25,F26,F48,F85,F86

### Easy Access seat travel distance: 4 cm
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3012: EAH_VERFAHRWEG_SLV_PHYS, bits 0-1, mask 11111111b -> `00, 28`

## Bundang_Thunder.xml — CFAS_PLX_1 (CAFD 000000B5, author: Bundang Thunder X5)

**Module series coverage:** F15,F16,F25,F26,F48,F85,F86

### Easy Access seat travel distance: 5 cm
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3012: EAH_VERFAHRWEG_SLV_PHYS, bits 0-1, mask 11111111b -> `00, 32`

## Bundang_Thunder.xml — CFAS_PLX_1 (CAFD 000000B5, author: Bundang Thunder X5)

**Module series coverage:** F15,F16,F25,F26,F48,F85,F86

### Easy Access seat travel distance: 6 cm
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3012: EAH_VERFAHRWEG_SLV_PHYS, bits 0-1, mask 11111111b -> `00, 3C`

## Bundang_Thunder.xml — CFAS_PLX_1 (CAFD 000000B5, author: Bundang Thunder X5)

**Module series coverage:** F15,F16,F25,F26,F48,F85,F86

### Easy Access seat travel distance: 7 cm
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3012: EAH_VERFAHRWEG_SLV_PHYS, bits 0-1, mask 11111111b -> `00, 46`

## Bundang_Thunder.xml — CFAS_PLX_1 (CAFD 000000B5, author: Bundang Thunder X5)

**Module series coverage:** F15,F16,F25,F26,F48,F85,F86

### Gentleman
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: GENTLEMAN, bit 1, mask 00000001b -> `01`
  * Group 3000: MEMORY, bit 0, mask 00000001b -> `01`

## Bundang_Thunder.xml — CFAS_PLX_1 (CAFD 000000B5, author: Bundang Thunder X5)

**Module series coverage:** F15,F16,F25,F26,F48,F85,F86

### Set gong when saving seat position
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: MEMORY_GONG, bit 2, mask 00001000b -> `01`

## Bundang_Thunder.xml — CBFS_PLX_1 (CAFD 000000B6, author: Bundang Thunder X5)

**Module series coverage:** F15,F16,F25,F26,F48,F85,F86

### Passenger seat Gentleman                                                                                         --** by Bundang Thunder ^^
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: GENTLEMAN, bit 1, mask 00000001b -> `01`
  * Group 3000: MEMORY, bit 0, mask 00000001b -> `01`

## Bundang_Thunder.xml — ACSM_4C (CAFD 00000909, author: Bundang Thunder X6)

**Module series coverage:** F15,F16,F25,F26,F48,F85,F86

### Seat belt warning chime for only 5 seconds                                                                                 --** by Bundang Thunder ^^
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: GWF_SBR_WARNDAUER, bit 3, mask 11111111b -> `05`

## Bundang_Thunder.xml — ACSM_4C (CAFD 00000909, author: Bundang Thunder X6)

**Module series coverage:** F15,F16,F25,F26,F48,F85,F86

### Delete driver seat belt warning light
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: SBR_PreWarning_Fahrer, bit 16, mask 00000001b -> `00`

## Bundang_Thunder.xml — ACSM_4C (CAFD 00000909, author: Bundang Thunder X6)

**Module series coverage:** F15,F16,F25,F26,F48,F85,F86

### Delete passenger seat belt warning light
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: SBR_PreWarning_Beifahrer, bit 16, mask 00000010b -> `00`

## Bundang_Thunder.xml — ACSM_4C (CAFD 00000909, author: Bundang Thunder X6)

**Module series coverage:** F15,F16,F25,F26,F48,F85,F86

### Disable driver seat belt warning chime
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: SeatBeltReminder_SBR_Fahrer, bit 15, mask 00000010b -> `00`

## Bundang_Thunder.xml — ACSM_4C (CAFD 00000909, author: Bundang Thunder X6)

**Module series coverage:** F15,F16,F25,F26,F48,F85,F86

### Disable passenger seat belt warning chime
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: SeatBeltReminder_SBR_Beifahrer, bit 15, mask 00000100b -> `00`

## Bundang_Thunder.xml — BDC_01 (CAFD 000017BE, author: Bundang Thunder X6)

**Module series coverage:** F15,F16,F25,F26,F48,F85,F86

### Activate hazard lights during hard braking                                                                                   --** by Bundang Thunder ^^
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3068: WB_GB_ENABLE, bit 26, mask 00000001b -> `01`

## Bundang_Thunder.xml — BDC_01 (CAFD 000017BE, author: Bundang Thunder X6)

**Module series coverage:** F15,F16,F25,F26,F48,F85,F86

### Limit passenger mirror tilt to 30 degrees in reverse
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3110: ASP_BORDSTEINAUTOMATIK_DELTA, bit 1, mask 11111111b -> `1E`

## Bundang_Thunder.xml — BDC_01 (CAFD 000017BE, author: Bundang Thunder X6)

**Module series coverage:** F15,F16,F25,F26,F48,F85,F86

### One-touch turn signal flashes five times
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3069: PIA_DEFAULT_TIPPBLINKEN, bit 215, mask 00011000b -> `Tippblinken_fuenfmal`

## Bundang_Thunder.xml — BDC_01 (CAFD 000017BE, author: Bundang Thunder X6)

**Module series coverage:** F15,F16,F25,F26,F48,F85,F86

### Enable welcome lights
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3068: WL_WIEDERHOLSPERRE_AKTIV, bit 13, mask 00100000b -> `01`

## Bundang_Thunder.xml — BDC_01 (CAFD 000017BE, author: Bundang Thunder X6)

**Module series coverage:** F15,F16,F25,F26,F48,F85,F86

### Enable follow me home
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3068: FMH_WIEDERHOLSPERRE_AKTIV, bit 13, mask 01000000b -> `01`

## Bundang_Thunder.xml — BDC_01 (CAFD 000017BE, author: Bundang Thunder X6)

**Module series coverage:** F15,F16,F25,F26,F48,F85,F86

### Close trunk immediately via remote
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 30D0: RC_TIME_DELAY_BOOTLID, bit 18, mask 111111!1b -> `01`

## Bundang_Thunder.xml — BDC_01 (CAFD 000017BE, author: Bundang Thunder X6)

**Module series coverage:** F15,F16,F25,F26,F48,F85,F86

### Open and close windows with remote
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3056: KOMFORTOEFFNUNG_FB, bit 0, mask 01000000b -> `01`

## Bundang_Thunder.xml — BDC_01 (CAFD 000017BE, author: Bundang Thunder X6)

**Module series coverage:** F15,F16,F25,F26,F48,F85,F86

### Fold mirrors immediately when locking (lock folding)
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3056: KOMFORT_SCHLIESSEN, bit 10, mask 11111111b -> `00`

## Bundang_Thunder.xml — BDC_01 (CAFD 000017BE, author: Bundang Thunder X6)

**Module series coverage:** F15,F16,F25,F26,F48,F85,F86

### Allow windows to keep closing with doors open (front and rear)
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3050: FH_TUERAUF_STOP_MAUT, bit 0, mask 00000001b -> `00`
  * Group 3051: FH_TUERAUF_STOP_MAUT_REAR, bit 0, mask 00000001b -> `00`

## Bundang_Thunder.xml — BDC_01 (CAFD 000017BE, author: Bundang Thunder X6)

**Module series coverage:** F15,F16,F25,F26,F48,F85,F86

### VLD
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3073: LUT_FLC_FORWARDLIGHTING_Y, bits 40-42, mask 11111111b -> `F015_ohne_AFS`
  * Group 3073: C_AFS_ENA, bit 152, mask 00000001b -> `F015_enable`

## Bundang_Thunder.xml — BDC_01 (CAFD 000017BE, author: Bundang Thunder X6)

**Module series coverage:** F15,F16,F25,F26,F48,F85,F86

### Turn on door handle lights when reversing
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3070: OVT_BEI_RUECKFAHRLICHT, bit 128, mask 00000001b -> `F015_ohne_AFS`

## Bundang_Thunder.xml — BDC_01 (CAFD 000017BE, author: Bundang Thunder X6)

**Module series coverage:** F15,F16,F25,F26,F48,F85,F86

### Disable auto start/stop in Comfort mode
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3023: TCM_MSA_DEFAULT_OFF, bit 0, mask 00010000b -> `01`

## Bundang_Thunder.xml — BDC_01 (CAFD 000017BE, author: Bundang Thunder X6)

**Module series coverage:** F15,F16,F25,F26,F48,F85,F86

### Disable auto start/stop in Eco Pro mode
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3023: TCM_MSA_ECO_MODE, bit 1, mask 00001100b -> `00`

## Bundang_Thunder.xml — BDC_01 (CAFD 000017BE, author: Bundang Thunder X6)

**Module series coverage:** F15,F16,F25,F26,F48,F85,F86

### Remember last auto start/stop state
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3023: TCM_MSA_MEMORY, bit 0, mask 00100000b -> `01`

## Bundang_Thunder.xml — BDC_01 (CAFD 000017BE, author: Bundang Thunder X6)

**Module series coverage:** F15,F16,F25,F26,F48,F85,F86

### Double horn when locking with engine running - enable
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3040: VAM_HORN_AT_SECURE, bit 0, mask 00000100b -> `01`

## Bundang_Thunder.xml — BDC_01 (CAFD 000017BE, author: Bundang Thunder X6)

**Module series coverage:** F15,F16,F25,F26,F48,F85,F86

### Double horn when locking with engine running - disable
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3040: VAM_HORN_AT_SECURE, bit 0, mask 00000100b -> `00`

## Bundang_Thunder.xml — HKFM (CAFD 000007C8, author: Bundang Thunder X6)

**Module series coverage:** F15,F16,F25,F26,F48,F85,F86

### Auto-close trunk (footwell switch + remote)
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3010: TASTER_FBD, bit 0, mask 00001000b -> `01`
  * Group 3010: SCH_TOEHKI, bit 2, mask 00000100b -> `01`
  * Group 3010: SCH_FBD, bit 2, mask 00001000b -> `01`

## Bundang_Thunder.xml — HU_NBT (CAFD 00000DED, author: Bundang Thunder X6)

**Module series coverage:** F15,F16,F25,F26,F48,F85,F86

### Set time automatically                                                                                         --** by Bundang Thunder ^^
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: SETTINGS_TIME_AUTOMATIC, bit 19, mask 00000110b -> `navigation`
  * Group 3000: CLOCK_CHANGE_AUTOMATIC, bit 105, mask 00100000b -> `01`

## Bundang_Thunder.xml — HU_NBT (CAFD 00000DED, author: Bundang Thunder X6)

**Module series coverage:** F15,F16,F25,F26,F48,F85,F86

### Watch video/DMB/navigation while driving
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: SPEEDLOCK_X_KMH_MAX, bit 72, mask 11111111b -> `FF`
  * Group 3000: SPEEDLOCK_X_KMH_MIN, bit 71, mask 11111111b -> `FF`
  * Group 3000: VIDEO_FRONT_LOCKED, bit 5, mask 00010000b -> `00`
  * Group 3000: VIDEO_HANDBRAKE, bit 5, mask 00000100b -> `00`
  * Group 3000: VIDEO_SPEEDLOCK_CONDITION, bit 57, mask 00000111b -> `None`

## Bundang_Thunder.xml — HU_NBT (CAFD 00000DED, author: Bundang Thunder X6)

**Module series coverage:** F15,F16,F25,F26,F48,F85,F86

### Suppress all warning messages
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3001: LEGAL_DISCLAIMER_TIME, bit 58, mask 11111111b -> `kein_ld`
  * Group 3001: MACRO_CAM_LEGALDISCLAIMER, bit 52, mask 11111111b -> `kein_ld`

## Bundang_Thunder.xml — HU_NBT (CAFD 00000DED, author: Bundang Thunder X6)

**Module series coverage:** F15,F16,F25,F26,F48,F85,F86

### Enable trailer zoom menu when reversing
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3001: MACRO_TRAILER_COUPLING, bit 54, mask 00000001b -> `01`

## Bundang_Thunder.xml — HU_NBT (CAFD 00000DED, author: Bundang Thunder X6)

**Module series coverage:** F15,F16,F25,F26,F48,F85,F86

### Close windows when it rains
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: REGEN_SCHLIESSEN, bit 19, mask 00001000b -> `01`

## Bundang_Thunder.xml — HU_NBT (CAFD 00000DED, author: Bundang Thunder X6)

**Module series coverage:** F15,F16,F25,F26,F48,F85,F86

### X-Drive
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: COMPASS, bit 5, mask 00000001b -> `01`
  * Group 3000: X_VIEW, bit 15, mask 00000001b -> `01`
  * Group 3000: X_VIEW_GRAPHIC_SLOP, bit 26, mask 00110000b -> `trajectory1`
  * Group 3000: X_VIEW_GRAPHIC_ROLL, bit 26, mask 11000000b -> `trajectory1`
  * Group 3000: MOMENTDISTRIBUTION_MENU, bit 110, mask 00000010b -> `01`

## Bundang_Thunder.xml — HU_NBT (CAFD 00000DED, author: Bundang Thunder X6)

**Module series coverage:** F15,F16,F25,F26,F48,F85,F86

### Enable USB video playback 1/2
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: ENT_CODEC_OGG, bit 15, mask 00010000b -> `01`
  * Group 3000: ENT_CODEC_XVID, bit 15, mask 00100000b -> `01`
  * Group 3000: ENT_CODEC_VCD, bit 15, mask 01000000b -> `01`
  * Group 3000: ENT_MC_VIDEO_SUPPORT, bit 13, mask 00000100b -> `01`

## Bundang_Thunder.xml — HU_NBT (CAFD 00000DED, author: Bundang Thunder X6)

**Module series coverage:** F15,F16,F25,F26,F48,F85,F86

### Enable USB video playback 2/2
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3003: API_USB_VIDEO, bit 33, mask 00000110b -> `both`
  * Group 3003: API_IPOD_VIDEO, bit 33, mask 00011000b -> `both`

## Bundang_Thunder.xml — HU_NBT (CAFD 00000DED, author: Bundang Thunder X6)

**Module series coverage:** F15,F16,F25,F26,F48,F85,F86

### Change warning chime to Rolls-Royce sound
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3002: SOUND_SIGNAL_SET, bit 26, mask 00111000b -> `rolls_royce`

## Bundang_Thunder.xml — HU_NBT (CAFD 00000DED, author: Bundang Thunder X6)

**Module series coverage:** F15,F16,F25,F26,F48,F85,F86

### Configure Sport mode
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3001: MACRO_FDS, bit 55, mask 00011000b -> `popup_and_config`
  * Group 3000: EFF_DYN_SPORT_CID, bit 101, mask 00010000b -> `01`
  * Group 3000: EFF_DYN_SPORT_UNIT, bit 107, mask 00000100b -> `01`

## Bundang_Thunder.xml — HU_NBT (CAFD 00000DED, author: Bundang Thunder X6)

**Module series coverage:** F15,F16,F25,F26,F48,F85,F86

### Startup animation
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3001: STARTUP_TYPE, bit 62, mask 00000110b -> `animation`
  * Group 3001: STARTUP_EMBLEM, bit 62, mask 01111000b -> `variant_01`

## Bundang_Thunder.xml — HU_NBT (CAFD 00000DED, author: Bundang Thunder X6)

**Module series coverage:** F15,F16,F25,F26,F48,F85,F86

### Volume adjustment bar
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3002: VOLUME_POPUP_DISPLAY, bit 52, mask 01000000b -> `01`
  * Group 3002: VOLUME_POPUP_REJECTION, bit 52, mask 10000000b -> `01`
  * Group 3002: VOLUME_POPUP_EXCEPTION, bit 53, mask 00000001b -> `01`

## Bundang_Thunder.xml — HU_NBT (CAFD 00000DED, author: Bundang Thunder X6)

**Module series coverage:** F15,F16,F25,F26,F48,F85,F86

### Show TPMC tire pressure temperature
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3001: RDC_DRUCK_TEMP, bit 66, mask 00001100b -> `druck_und_temperatur`

## Bundang_Thunder.xml — HU_NBT (CAFD 00000DED, author: Bundang Thunder X6)

**Module series coverage:** F15,F16,F25,F26,F48,F85,F86

### Output ringtone through speakers (iPhone only)
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3003: INBAND_RINGING, bit 6, mask 10000000b -> `01`

## Bundang_Thunder.xml — HU_NBT (CAFD 00000DED, author: Bundang Thunder X6)

**Module series coverage:** F15,F16,F25,F26,F48,F85,F86

### Lock/unlock confirmation chime (requires piezo buzzer sensor)
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: ACOUSTICAL_LOCK_CONFIRM, bit 110, mask 00000001b -> `01`

## Bundang_Thunder.xml — HU_NBT (CAFD 00000DED, author: Bundang Thunder X6)

**Module series coverage:** F15,F16,F25,F26,F48,F85,F86

### Change M Sport display cluster colors
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: M_VEHICLE, bit 133, mask 01000000b -> `01`

## Bundang_Thunder.xml — HU_NBT (CAFD 00000DED, author: Bundang Thunder X6)

**Module series coverage:** F15,F16,F25,F26,F48,F85,F86

### Adjust high-beam assistant in iDrive
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: HIGH_BEAM_ASSISTANT, bit 109, mask 10000000b -> `01`

## Bundang_Thunder.xml — HU_NBT (CAFD 00000DED, author: Bundang Thunder X6)

**Module series coverage:** F15,F16,F25,F26,F48,F85,F86

### Show currently playing album art in iDrive
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: ENT_BTAS_IAP_COVERART, bit 9, mask 00000100b -> `01`
  * Group 3003: ENT_BTAS_METADATA, bit 19, mask 00000100b -> `01`
  * Group 3003: ENT_BTAS_BROWSING, bit 19, mask 00001000b -> `01`

## Bundang_Thunder.xml — HU_NBT (CAFD 00000DED, author: Bundang Thunder X6)

**Module series coverage:** F15,F16,F25,F26,F48,F85,F86

### Unlock DVD region code
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: ENT_VIDEO_DVD_AREA_CODE, bit 7, mask 11111111b -> `alle_anderen`

## Bundang_Thunder.xml — HU_NBT (CAFD 00000DED, author: Bundang Thunder X6)

**Module series coverage:** F15,F16,F25,F26,F48,F85,F86

### Show turn signals in HUD
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3001: HUD_TURNSIGNAL, bit 55, mask 10000000b -> `01`

## Bundang_Thunder.xml — HU_NBT (CAFD 00000DED, author: Bundang Thunder X6)

**Module series coverage:** F15,F16,F25,F26,F48,F85,F86

### Set sound system to Bang & Olufsen
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: HIGH_END_AUDIO_B_UND_W, bit 21, mask 01100000b -> `keine_insz`

## Bundang_Thunder.xml — HU_NBT (CAFD 00000DED, author: Bundang Thunder X6)

**Module series coverage:** F15,F16,F25,F26,F48,F85,F86

### Enable Logic7 (S667A HiFi vehicles)
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: LOGIC7_SYMBOL, bit 22, mask 00001000b -> `01`

## Bundang_Thunder.xml — HU_NBT (CAFD 00000DED, author: Bundang Thunder X6)

**Module series coverage:** F15,F16,F25,F26,F48,F85,F86

### Enhance audio mid-bass
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3002: AUDIO_SYSTEM, bit 29, mask 00111100b -> `highpremium`
  * Group 3002: AUDIO_SYSTEM_VAR, bit 21, mask 00000011b -> `variant3`

## Bundang_Thunder.xml — ICMQL (CAFD 0000067B, author: Bundang Thunder X6)

**Module series coverage:** F15,F16,F25,F26,F48,F85,F86

### Default to Eco mode at start                                                                              --** by Bundang Thunder ^^
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: IcmKod_B_InitEco, bit 36, mask 00001000b -> `verbaut`

## Bundang_Thunder.xml — ICMQL (CAFD 0000067B, author: Bundang Thunder X6)

**Module series coverage:** F15,F16,F25,F26,F48,F85,F86

### Enable cruise control
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: C_Fahrfunktion, bit 128, mask 00001110b -> `01`

## Bundang_Thunder.xml — ICMQL (CAFD 0000067B, author: Bundang Thunder X6)

**Module series coverage:** F15,F16,F25,F26,F48,F85,F86

### Enable cruise control
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: C_Fahrfunktion, bit 128, mask 00001110b -> `04`

## Bundang_Thunder.xml — ICMQL (CAFD 0000067B, author: Bundang Thunder X6)

**Module series coverage:** F15,F16,F25,F26,F48,F85,F86

### Enable Sport+ mode
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: IcmKod_B_S2TBA, bit 18, mask 11111111b -> `verbaut`

## Bundang_Thunder.xml — ICMQL (CAFD 0000067B, author: Bundang Thunder X6)

**Module series coverage:** F15,F16,F25,F26,F48,F85,F86

### ACC distance
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: C_Abstandsstufe_init, bit 184, mask 00000111b -> `01`

## Bundang_Thunder.xml — ICMQL (CAFD 0000067B, author: Bundang Thunder X6)

**Module series coverage:** F15,F16,F25,F26,F48,F85,F86

### Adjust active blind spot activation speed by -20 km/h
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: C_ZSW_Aktivierunggeschwindigkeit_Funktion_low, bit 190, mask 00111111b -> `01`

## Bundang_Thunder.xml — ICMQL (CAFD 0000067B, author: Bundang Thunder X6)

**Module series coverage:** F15,F16,F25,F26,F48,F85,F86

### Enable coasting mode
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: C_Segeln_vorhanden, bit 120, mask 11000000b -> `01`

## Bundang_Thunder.xml — IHKA_CBF (CAFD 000047D6, author: Bundang Thunder X6)

**Module series coverage:** F15,F16,F25,F26,F48,F85,F86

### Remember last air conditioning state                                                                               --** by Bundang Thunder ^^
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: OFF_MEMORY, bit 5, mask 00010000b -> `01`

## Bundang_Thunder.xml — IHKA_CBF (CAFD 000047D6, author: Bundang Thunder X6)

**Module series coverage:** F15,F16,F25,F26,F48,F85,F86

### Prevent AUTO button from turning on A/C
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: AC_NICHT_EIN_BEI_AUTO, bit 5, mask 00001000b -> `01`

## Bundang_Thunder.xml — IHKA_CBF (CAFD 000047D6, author: Bundang Thunder X6)

**Module series coverage:** F15,F16,F25,F26,F48,F85,F86

### Remember HVAC recirculation mode
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: MEMORY_UMLUFT, bit 0, mask 00000100b -> `01`

## Bundang_Thunder.xml — JBBFE (CAFD 00000014, author: Bundang Thunder X6)

**Module series coverage:** F15,F16,F25,F26,F48,F85,F86

### Disable headlight washer                                                                                --** by Bundang Thunder ^^
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: SCHEINWERFERREINIGUNG, bit 8, mask 00000001b -> `00`

## Bundang_Thunder.xml — KAFAS2 (CAFD 00001148, author: Bundang Thunder X6)

**Module series coverage:** F15,F16,F25,F26,F48,F85,F86

### Automatic high-beam assistant                                                                                --** by Bundang Thunder ^^
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3050: FLA_ON_OFF, bit 1, mask 00000001b -> `FLA_on`
  * Group 3050: SPEED_SWITCHING_HIGH_BEAMS_ON, bit 6, mask 11111111b -> `CN`
  * Group 3050: SPEED_SWITCHING_HIGH_BEAMS_OFF, bit 7, mask 11111111b -> `China`

## Bundang_Thunder.xml — KOMBI FPK_I12 (CAFD 00001060, author: Bundang Thunder X6)

**Module series coverage:** F15,F16,F25,F26,F48,F85,F86

### Show phone, entertainment, and voice prompts in HUD                                                               --** by Bundang Thunder ^^
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3003: HUD_ENTERTAINMENT_ENABLE, bit 10, mask 00000001b -> `01`
  * Group 3003: HUD_STARTUP_ENABLE, bit 9, mask 00100000b -> `01`
  * Group 3000: HUD_TLC_ENABLE, bit 41, mask 00000001b -> `01`
  * Group 3000: HUD_VZA_ENABLE, bit 40, mask 10000000b -> `01`

## Bundang_Thunder.xml — KOMBI FPK_I12 (CAFD 00001060, author: Bundang Thunder X6)

**Module series coverage:** F15,F16,F25,F26,F48,F85,F86

### Show turn signals in HUD
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3003: HUD_BLINKER_ENABLE, bit 11, mask 00000001b -> `01`
  * Group 3008: HUD_PIA_BLINKER, bit 5, mask 00000001b -> `01`

## Bundang_Thunder.xml — KOMBI FPK_I12 (CAFD 00001060, author: Bundang Thunder X6)

**Module series coverage:** F15,F16,F25,F26,F48,F85,F86

### Show logo on instrument cluster
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3003: MPM_ENABLE, bit 3, mask 00000010b -> `01`
  * Group 3000: MPM_LOGO, bit 44, mask 11110000b -> `mpm_x6`
  * Group 3000: BMW_LOGO, bit 44, mask 00001111b -> `mpm_x6`

## Bundang_Thunder.xml — KOMBI FPK_I12 (CAFD 00001060, author: Bundang Thunder X6)

**Module series coverage:** F15,F16,F25,F26,F48,F85,F86

### Show compass in instrument cluster
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3003: KOMPASS_GRAPH_ENABLE, bit 12, mask 00010000b -> `01`

## Bundang_Thunder.xml — KOMBI FPK_I12 (CAFD 00001060, author: Bundang Thunder X6)

**Module series coverage:** F15,F16,F25,F26,F48,F85,F86

### Disable warning chime below 3 degrees
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: CC_TEMPERATURWARNUNG, bit 50, mask 00000001b -> `00`

## Bundang_Thunder.xml — KOMBI FPK_I12 (CAFD 00001060, author: Bundang Thunder X6)

**Module series coverage:** F15,F16,F25,F26,F48,F85,F86

### Show power output in instrument cluster
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3003: MOTORLEISTUNG_ENABLE, bit 11, mask 00000010b -> `01`

## Bundang_Thunder.xml — KOMBI FPK_I12 (CAFD 00001060, author: Bundang Thunder X6)

**Module series coverage:** F15,F16,F25,F26,F48,F85,F86

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
  * Group 300C: FDS_MENUE, bit 51, mask 11111111b -> `menue_3`

## Bundang_Thunder.xml — CFAS_PLX_1 (CAFD 000000B5, author: Bundang Thunder X6)

**Module series coverage:** F15,F16,F25,F26,F48,F85,F86

### Enable Easy Access                                                                         --** by Bundang Thunder ^^
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: EINAUSSTIEGSHILFE, bit 0, mask 00011100b -> `Modus_FA_SLV`

## Bundang_Thunder.xml — CFAS_PLX_1 (CAFD 000000B5, author: Bundang Thunder X6)

**Module series coverage:** F15,F16,F25,F26,F48,F85,F86

### Easy Access seat starts moving from end position
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3012: EAH_SCHUTZFREIRAUM_HINTEN_SLV_PHYS, bits 4-5, mask 11111111b -> `00, 01`

## Bundang_Thunder.xml — CFAS_PLX_1 (CAFD 000000B5, author: Bundang Thunder X6)

**Module series coverage:** F15,F16,F25,F26,F48,F85,F86

### Easy Access seat starts moving with 1 cm remaining
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3012: EAH_SCHUTZFREIRAUM_HINTEN_SLV_PHYS, bits 4-5, mask 11111111b -> `00, 0A`

## Bundang_Thunder.xml — CFAS_PLX_1 (CAFD 000000B5, author: Bundang Thunder X6)

**Module series coverage:** F15,F16,F25,F26,F48,F85,F86

### Easy Access seat starts moving with 2 cm remaining
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3012: EAH_SCHUTZFREIRAUM_HINTEN_SLV_PHYS, bits 4-5, mask 11111111b -> `00, 14`

## Bundang_Thunder.xml — CFAS_PLX_1 (CAFD 000000B5, author: Bundang Thunder X6)

**Module series coverage:** F15,F16,F25,F26,F48,F85,F86

### Easy Access seat starts moving with 3 cm remaining
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3012: EAH_SCHUTZFREIRAUM_HINTEN_SLV_PHYS, bits 4-5, mask 11111111b -> `00, 1E`

## Bundang_Thunder.xml — CFAS_PLX_1 (CAFD 000000B5, author: Bundang Thunder X6)

**Module series coverage:** F15,F16,F25,F26,F48,F85,F86

### Easy Access seat travel distance: 4 cm
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3012: EAH_VERFAHRWEG_SLV_PHYS, bits 0-1, mask 11111111b -> `00, 28`

## Bundang_Thunder.xml — CFAS_PLX_1 (CAFD 000000B5, author: Bundang Thunder X6)

**Module series coverage:** F15,F16,F25,F26,F48,F85,F86

### Easy Access seat travel distance: 5 cm
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3012: EAH_VERFAHRWEG_SLV_PHYS, bits 0-1, mask 11111111b -> `00, 32`

## Bundang_Thunder.xml — CFAS_PLX_1 (CAFD 000000B5, author: Bundang Thunder X6)

**Module series coverage:** F15,F16,F25,F26,F48,F85,F86

### Easy Access seat travel distance: 6 cm
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3012: EAH_VERFAHRWEG_SLV_PHYS, bits 0-1, mask 11111111b -> `00, 3C`

## Bundang_Thunder.xml — CFAS_PLX_1 (CAFD 000000B5, author: Bundang Thunder X6)

**Module series coverage:** F15,F16,F25,F26,F48,F85,F86

### Easy Access seat travel distance: 7 cm
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3012: EAH_VERFAHRWEG_SLV_PHYS, bits 0-1, mask 11111111b -> `00, 46`

## Bundang_Thunder.xml — CFAS_PLX_1 (CAFD 000000B5, author: Bundang Thunder X6)

**Module series coverage:** F15,F16,F25,F26,F48,F85,F86

### Gentleman
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: GENTLEMAN, bit 1, mask 00000001b -> `01`
  * Group 3000: MEMORY, bit 0, mask 00000001b -> `01`

## Bundang_Thunder.xml — CFAS_PLX_1 (CAFD 000000B5, author: Bundang Thunder X6)

**Module series coverage:** F15,F16,F25,F26,F48,F85,F86

### Set gong when saving seat position
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: MEMORY_GONG, bit 2, mask 00001000b -> `01`

## Bundang_Thunder.xml — CBFS_PLX_1 (CAFD 000000B6, author: Bundang Thunder X6)

**Module series coverage:** F15,F16,F25,F26,F48,F85,F86

### Passenger seat Gentleman                                                                                         --** by Bundang Thunder ^^
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: GENTLEMAN, bit 1, mask 00000001b -> `01`
  * Group 3000: MEMORY, bit 0, mask 00000001b -> `01`

## PerryGunn.xml — CAS_04 (CAFD 0000000F, author: PerryGunn)

**Module series coverage:** F025

### Unlock/open the tailgate from fob only if the vehicle is unlocked
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3002: HK_GESPERRT_IN_GESICHERT, bit 9, mask 00010000b -> `aktiv`

## PerryGunn.xml — CAS_04 (CAFD 0000000F, author: PerryGunn)

**Module series coverage:** F025

### Unlock/open the tailgate from fob if the vehicle is locked or unlocked
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3002: HK_GESPERRT_IN_GESICHERT, bit 9, mask 00010000b -> `nicht_aktiv`

## ekfxisid.xml — ACSM_4B (CAFD 00000911, author: ekfxisidF030)

**Module series coverage:** F020,F030

### Seat belt warning chime three times (5 seconds) [Changwon ll Daltanyang]
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3001: GWF_SBR_WARNDAUER, bit 3, mask 11111111b -> `05`

## ekfxisid.xml — ASD01 (CAFD 00000F9B, author: ekfxisidF30)

**Module series coverage:** F020,F030

### ASD M4 active sound [Changwon ll Daltanyang]
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: Model Range, bit 0, mask 11111111b -> `F082`
  * Group 3000: Engine, bit 1, mask 11111111b -> `S55B30`
  * Group 3000: Audio Level, bit 2, mask 11111111b -> `Hifi`
  * Group 3000: Power Class, bit 3, mask 11111111b -> `ML`

## ekfxisid.xml — FEM_BODY (CAFD 00000794, author: ekfxisidF030)

**Module series coverage:** F020,F030

### Mirror lock folding (one-touch) [Changwon ll Daltanyang]
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3053: KOMFORT_SCHLIESSEN, bit 9, mask 11111111b -> `00`

## ekfxisid.xml — FEM_BODY (CAFD 00000794, author: ekfxisidF030)

**Module series coverage:** F020,F030

### Allow windows to operate with doors open
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3050: FH_TUERAUF_STOP_MAUT, bit 0, mask 00000001b -> `nicht_aktiv`

## ekfxisid.xml — FEM_BODY (CAFD 00000794, author: ekfxisidF030)

**Module series coverage:** F020,F030

### Turn signal flashes five times
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3060: BLINKZYKLEN_ANZAHL_TIPP, bit 7, mask 00000111b -> `04`

## ekfxisid.xml — FEM_BODY (CAFD 00000794, author: ekfxisidF030)

**Module series coverage:** F020,F030

### Passenger mirror angle adjustment 1
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3110: ASP_BORDSTEINAUTOMAIK_DELTA, bit 2, mask 11111111b -> `1E`

## ekfxisid.xml — FEM_BODY (CAFD 00000794, author: ekfxisidF030)

**Module series coverage:** F020,F030

### Passenger mirror angle adjustment when preset 1 fails
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3110: ASP_HORIZONTALE_MIN_POS, bit 3, mask 11111111b -> `1E`

## ekfxisid.xml — FEM_BODY (CAFD 00000794, author: ekfxisidF030)

**Module series coverage:** F020,F030

### Xenon: Angel Eye brightness 30% when xenon on
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3062: MAPPING_STANDL_V_L_PWM_LEVEL_STANDARD, bit 46, mask 11111111b -> `1E`
  * Group 3062: MAPPING_STANDL_V_R_PWM_LEVEL_STANDARD, bit 57, mask 11111111b -> `1E`

## ekfxisid.xml — FEM_BODY (CAFD 00000794, author: ekfxisidF030)

**Module series coverage:** F020,F030

### Xenon: Angel Eye brightness 100% when xenon on
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3062: MAPPING_STANDL_V_L_PWM_LEVEL_STANDARD, bit 46, mask 11111111b -> `64`
  * Group 3062: MAPPING_STANDL_V_R_PWM_LEVEL_STANDARD, bit 57, mask 11111111b -> `64`

## ekfxisid.xml — FEM_BODY (CAFD 00000794, author: ekfxisidF030)

**Module series coverage:** F020,F030

### Xenon: Angel Eye brightness 50% with parking lights on
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3062: MAPPING_PARKL_V_L_PWM_1_LEFT, bit 68, mask 11111111b -> `32`
  * Group 3062: MAPPING_PARKL_V_L_PWM_2_RIGHT, bit 69, mask 11111111b -> `32`

## ekfxisid.xml — FEM_BODY (CAFD 00000794, author: ekfxisidF030)

**Module series coverage:** F020,F030

### Xenon: Angel Eye brightness 100% with parking lights on
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3062: MAPPING_PARKL_V_L_PWM_1_LEFT, bit 68, mask 11111111b -> `64`
  * Group 3062: MAPPING_PARKL_V_L_PWM_2_RIGHT, bit 69, mask 11111111b -> `64`

## ekfxisid.xml — FEM_BODY (CAFD 00000794, author: ekfxisidF030)

**Module series coverage:** F020,F030

### Xenon: Angel Eye brightness 50% with DRL on
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3062: MAPPING_TAGFAHRL_V_L_PWM_LEVEL_1, bit 90, mask 11111111b -> `32`
  * Group 3062: MAPPING_TAGFAHRL_V_R_PWM_LEVEL_1, bit 101, mask 11111111b -> `32`

## ekfxisid.xml — FEM_BODY (CAFD 00000794, author: ekfxisidF030)

**Module series coverage:** F020,F030

### Xenon: Angel Eye brightness 100% with DRL on
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3062: MAPPING_TAGFAHRL_V_L_PWM_LEVEL_1, bit 90, mask 11111111b -> `64`
  * Group 3062: MAPPING_TAGFAHRL_V_R_PWM_LEVEL_1, bit 101, mask 11111111b -> `64`

## ekfxisid.xml — FEM_BODY (CAFD 00000794, author: ekfxisidF030)

**Module series coverage:** F020,F030

### Simulate adaptive lights with fog lights 1/3
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3073: C_BLC_ENA, bit 66, mask 00000001b -> `01`
  * Group 3073: C_CLC_ENA, bit 218, mask 00000010b -> `01`

## ekfxisid.xml — FEM_BODY (CAFD 00000794, author: ekfxisidF030)

**Module series coverage:** F020,F030

### Simulate adaptive lights with fog lights 2/3
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3066: KL_ENALBE_LI, bit 0, mask 00000001b -> `KL_Ein`
  * Group 3066: KL_ENABLE_RE, bit 80, mask 00000001b -> `KL_Ein`

## ekfxisid.xml — FEM_BODY (CAFD 00000794, author: ekfxisidF030)

**Module series coverage:** F020,F030

### Simulate adaptive lights with fog lights 3/3
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3062: MAPPING_ABBIEGEL_L_OUTPUT, bit 110, mask 00111111b -> `nsw_l`
  * Group 3062: MAPPING_ABBIEGEL_L_OUTPUT, bit 121, mask 00111111b -> `nsw_r`

## ekfxisid.xml — FEM_BODY (CAFD 00000794, author: ekfxisidF030)

**Module series coverage:** F020,F030

### Toggle headlight washer enablement
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3080: WW_SCHEINWERFERREINIGUNG, bit 8, mask 00000001b -> `nicht_aktiv`

## ekfxisid.xml — FEM_BODY (CAFD 00000794, author: ekfxisidF030)

**Module series coverage:** F020,F030

### Welcome fog lights (hard on)
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3063: MAPPING_NEBELSCHW_L_PART_OF_WL, bit 55, mask 11000000b -> `hard_On`
  * Group 3063: MAPPING_NEBELSCHW_R_PART_OF_WL, bit 66, mask 11000000b -> `hard_On`

## ekfxisid.xml — FEM_BODY (CAFD 00000794, author: ekfxisidF030)

**Module series coverage:** F020,F030

### Welcome fog lights (soft on)
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3063: MAPPING_NEBELSCHW_L_PART_OF_WL, bit 55, mask 11000000b -> `soft_On`
  * Group 3063: MAPPING_NEBELSCHW_R_PART_OF_WL, bit 66, mask 11000000b -> `soft_On`

## ekfxisid.xml — FEM_BODY (CAFD 00000794, author: ekfxisidF030)

**Module series coverage:** F020,F030

### Auto unfold mirrors above set speed (40 km/h -> 25 km/h)
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3110: ASP_GESCHWINDIGKEIT_AUTO_AUSKLAPPEN, bit 10, mask 11111111b -> `19`

## ekfxisid.xml — FEM_BODY (CAFD 00000794, author: ekfxisidF030)

**Module series coverage:** F020,F030

### Adjust automatic light sensor
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3130: RLS_DEF_FLC_SCHWELLWERT_SATZ, bit 5, mask 00000111b -> `unempfindlich`

## ekfxisid.xml — FEM_BODY (CAFD 00000794, author: ekfxisidF030)

**Module series coverage:** F020,F030

### Illuminate door handle lights in reverse
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3070: OVT_BEI_RUECKFAHRLICHT, bit 11, mask 00010000b -> `aktiv`

## ekfxisid.xml — FEM_BODY (CAFD 00000794, author: ekfxisidF030)

**Module series coverage:** F020,F030

### Welcome ambient lighting
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3070: WELCOME_AMBIENTE, bit 1, mask 10000000b -> `Aktiv`

## ekfxisid.xml — FEM_BODY (CAFD 00000794, author: ekfxisidF030)

**Module series coverage:** F020,F030

### Ambient lighting maximum brightness
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3070: AMBIENTE_HELLGKELT, bit 5, mask 11111111b -> `99`

## ekfxisid.xml — FEM_BODY (CAFD 00000794, author: ekfxisidF030)

**Module series coverage:** F020,F030

### Turn off audio and navigation when door opens after engine off
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3020: TCM_LOGIC_R_OFF_DOOR, bit 1, mask 00000001b -> `01`

## ekfxisid.xml — FEM_BODY (CAFD 00000794, author: ekfxisidF030)

**Module series coverage:** F020,F030

### Enable dynamic brake lights
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3060: ESS_AKTIVIERBARER_AUSGANG, bit 16, mask 00000011b -> `bremslicht_blinkend`
  * Group 3060: ESS_AKTIVIERUNG_REALE_VERZ, bit 20, mask 00011111b -> `04`
  * Group 3060: ESS_DEAKTIVIERUNG_REALE_VERZ, bit 19, mask 00011111b -> `04`
  * Group 3060: ESS_AKTIVIERUNG_GESCHW, bit 17, mask 11111110b -> `0A`

## ekfxisid.xml — FEM_BODY (CAFD 00000794, author: ekfxisidF030)

**Module series coverage:** F020,F030

### Flash hazard lights during hard braking (50 km/h)
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3060: WB_GB_ENABLE, bit 26, mask 00000001b -> `aktiv`
  * Group 3060: WB_GB_GEFAHRENWERT_MIN, bits 23-24, mask 11111111b -> `00, 32`

## ekfxisid.xml — FEM_BODY (CAFD 00000794, author: ekfxisidF030)

**Module series coverage:** F020,F030

### Remember last auto start/stop state
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3023: TCM_MSA_MEMORY, bit 0, mask 00100000b -> `aktiv`

## ekfxisid.xml — FEM_BODY (CAFD 00000794, author: ekfxisidF030)

**Module series coverage:** F020,F030

### Auto Start/Stop DEFAULT OFF
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3023: TCM_MSA_DEFAULT_OFF, bit 0, mask 00010000b -> `aktiv`

## ekfxisid.xml — FEM_BODY (CAFD 00000794, author: ekfxisidF030)

**Module series coverage:** F020,F030

### Front fog lights -> convert to LED
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3061: NSW_L_KALTUEBERWACHUNG, bit 42, mask 00000001b -> `nicht_aktiv`
  * Group 3061: NSW_L_WARMUEBERWACHUNG, bit 42, mask 00000010b -> `nicht_aktiv`
  * Group 3061: NSW_L_KURZSCHLUSS, bit 42, mask 00000100b -> `aktiv`
  * Group 3061: NSW_L_IS_LED, bit 42, mask 00001000b -> `aktiv`
  * Group 3061: NSW_R_KALTUEBERWACHUNG, bit 46, mask 00000001b -> `nicht_aktiv`
  * Group 3061: NSW_R_WARMUEBERWACHUNG, bit 46, mask 00000010b -> `nicht_aktiv`
  * Group 3061: NSW_R_KURZSCHLUSS, bit 46, mask 00000100b -> `aktiv`
  * Group 3061: NSW_R_IS_LED, bit 46, mask 00001000b -> `aktiv`

## ekfxisid.xml — FEM_BODY (CAFD 00000794, author: ekfxisidF030)

**Module series coverage:** F020,F030

### Front turn signals -> convert to LED
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3061: FRA_V_L_KALTUEBERWACHUNG, bit 50, mask 00000001b -> `nicht_aktiv`
  * Group 3061: FRA_V_L_WARMUEBERWACHUNG, bit 50, mask 00000010b -> `nicht_aktiv`
  * Group 3061: FRA_V_L_KURZSCHLUSS, bit 50, mask 00000100b -> `aktiv`
  * Group 3061: FRA_V_L_IS_LED, bit 50, mask 00001000b -> `aktiv`
  * Group 3061: FRA_V_R_KALTUEBERWACHUNG, bits 50-54, mask 00000001b -> `nicht_aktiv`
  * Group 3061: FRA_V_R_WARMUEBERWACHUNG, bits 50-54, mask 00000010b -> `nicht_aktiv`
  * Group 3061: FRA_V_R_KURZSCHLUSS, bits 50-54, mask 00000100b -> `aktiv`
  * Group 3061: FRA_V_R_IS_LED, bits 50-54, mask 00001000b -> `aktiv`

## ekfxisid.xml — FEM_BODY (CAFD 00000794, author: ekfxisidF030)

**Module series coverage:** F020,F030

### Horn alarm when locking with engine running
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3040: CLM_HORN_AT_SECURE, bit 1, mask 00100000b -> `aktiv`

## ekfxisid.xml — FEM_BODY (CAFD 00000794, author: ekfxisidF030)

**Module series coverage:** F020,F030

### Auto door lock speed (10 km/h = 0A)
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3040: CLM_SPEED_LIMIT_PIA_AUTO_LOCK, bit 6, mask 11111111b -> `0A`

## ekfxisid.xml — FEM_BODY (CAFD 00000794, author: ekfxisidF030)

**Module series coverage:** F020,F030

### Auto re-lock if door unopened after unlock (18 seconds)
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3040: CLM_TIME_PIA_LOCK_AT_TIMEOUT, bit 5, mask 11111111b -> `12`

## ekfxisid.xml — FEM_BODY (CAFD 00000794, author: ekfxisidF030)

**Module series coverage:** F020,F030

### Unlock doors automatically when engine off
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3040: CLM_UNLOCK_KL150OFF_AFTER_PIA_AUTO_LOCK, bit 1, mask 00000010b -> `aktiv`

## ekfxisid.xml — FEM_BODY (CAFD 00000794, author: ekfxisidF030)

**Module series coverage:** F020,F030

### Enable panic alarm 500 ms (short = welcome; MID = trunk; 3 s = panic)
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 30D0: RC_PANIC_ALARM, bit 2, mask 00000100b -> `Aktiv`
  * Group 30D0: RC_DEFAULT_IDG_3RD_BUTTON_SHORT, bit 3, mask 00001111b -> `04`
  * Group 30D0: RC_DEFAULT_IDG_3RD_BUTTON_MID, bit 3, mask 11110000b -> `02`
  * Group 30D0: RC_DEFAULT_IDG_3RD_BUTTON_LONG, bit 4, mask 00001111b -> `03`
  * Group 30D0: RC_TIME_DELAY_BOOTLID, bit 8, mask 11111111b -> `14`
  * Group 30D0: RC_TIME_DELAY_PANIC, bit 9, mask 11111111b -> `28`

## ekfxisid.xml — FEM_BODY (CAFD 00000794, author: ekfxisidF030)

**Module series coverage:** F020,F030

### Enable paddle shifters
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3190: PADDLES_VERBAUT, bit 0, mask 000000001b -> `aktiv`

## ekfxisid.xml — IHKA3 (CAFD 000016EE, author: ekfxisidF030)

**Module series coverage:** F020,F030

### Remember last A/C on/off state [Changwon ll Daltanyang]
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3003: MEMORY_OFF, bit 0, mask 00000010b -> `Aktiv`

## ekfxisid.xml — IHKA3 (CAFD 000016EE, author: ekfxisidF030)

**Module series coverage:** F020,F030

### Remember air recirculation mode
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3003: MEMORY_UMLUFT, bit 0, mask 00000001b -> `Aktiv`

## ekfxisid.xml — IHKA3 (CAFD 000016EE, author: ekfxisidF030)

**Module series coverage:** F020,F030

### Prevent AUTO button from turning on A/C
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3003: AC_NICHT_EIN_BEI_AUTO, bit 0, mask 00000001b -> `Aktiv`

## ekfxisid.xml — IHKA3 (CAFD 000016EE, author: ekfxisidF030)

**Module series coverage:** F020,F030

### Lock air recirculation mode
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3003: UMLUFT_AUTO_AUS, bit 0, mask 10000000b -> `disable`

## ekfxisid.xml — IHKA (CAFD 00000A3F, author: ekfxisidF030)

**Module series coverage:** F020,F030

### Remember last A/C on/off state [Changwon ll Daltanyang]
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3002: MEMORY_OFF, bit 0, mask 00000010b -> `Aktiv`

## ekfxisid.xml — IHKA (CAFD 00000A3F, author: ekfxisidF030)

**Module series coverage:** F020,F030

### Remember air recirculation mode
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3002: MEMORY_UMLUFT, bit 0, mask 00000001b -> `Aktiv`

## ekfxisid.xml — IHKA (CAFD 00000A3F, author: ekfxisidF030)

**Module series coverage:** F020,F030

### Prevent AUTO button from turning on A/C
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3002: AC_NICHT_EIN_BEI_AUTO, bit 0, mask 00000100b -> `Aktiv`

## ekfxisid.xml — HKFM (CAFD 000007C8, author: ekfxisidF030)

**Module series coverage:** F020,F030

### Operate power trunk from interior button [Changwon ll Daltanyang]
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3010: SCH_FBD, bit 2, mask 00001000b -> `Aktiv`
  * Group 3010: SCH_TOEHKI, bit 2, mask 00000100b -> `Aktiv`
  * Group 3010: TASTER_FBD, bit 0, mask 00001000b -> `Aktiv`

## ekfxisid.xml — HKFM (CAFD 0000157F, author: ekfxisidF030)

**Module series coverage:** F020,F030

### Operate power trunk from interior button
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3010: SCH_FBD, bit 2, mask 00001000b -> `Aktiv`
  * Group 3010: SCH_TOEHKI, bit 2, mask 00000100b -> `Aktiv`
  * Group 3010: TASTER_FBD, bit 0, mask 00001000b -> `Aktiv`

## ekfxisid.xml — KOMBI (CAFD 000009C8, author: ekfxisidF030)

**Module series coverage:** F020,F030

### Enable Sport+ menu in cluster       [Changwon ll Daltanyang]
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 300C: FDS_MENUE, bit 54, mask 11111111b -> `menue_3`

## ekfxisid.xml — KOMBI (CAFD 000009C8, author: ekfxisidF030)

**Module series coverage:** F020,F030

### Digital speedometer in instrument cluster
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: BC_DIGITAL_V, bit 1, mask 00000010b -> `Aktiv`
  * Group 3000: BC_V_KORREKTUR, bit 1, mask 01000000b -> `nicht_aktiv`

## ekfxisid.xml — KOMBI (CAFD 000009C8, author: ekfxisidF030)

**Module series coverage:** F020,F030

### Instrument cluster M Performance logo
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: BMW_LOGO, bit 0, mask 11110000b -> `01`

## ekfxisid.xml — KOMBI (CAFD 000009C8, author: ekfxisidF030)

**Module series coverage:** F020,F030

### Enable motor temperature display
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: BC_MOTORTEMP_ENABLE, bit 3, mask 00010000b -> `aktiv`

## ekfxisid.xml — KOMBI (CAFD 000009C8, author: ekfxisidF030)

**Module series coverage:** F020,F030

### Move instrument cluster clock
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: BASISANZEEIGE_VARIANTE, bit 53, mask 01000000b -> `Aktiv`

## ekfxisid.xml — KOMBI (CAFD 000009C8, author: ekfxisidF030)

**Module series coverage:** F020,F030

### Show manual gear steps M1-M8 in DS mode
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: SPA_SPORT_ENABLE, bit 41, mask 00010000b -> `Aktiv`

## ekfxisid.xml — KOMBI (CAFD 000009C8, author: ekfxisidF030)

**Module series coverage:** F020,F030

### Enable MPM
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3003: MPM_ENABLE, bit 7, mask 00000100b -> `Aktiv`

## ekfxisid.xml — KOMBI (CAFD 000009C8, author: ekfxisidF030)

**Module series coverage:** F020,F030

### MPM logo 550d
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: MPM_LOGO, bit 43, mask 11110000b -> `550d`

## ekfxisid.xml — KOMBI (CAFD 000009C8, author: ekfxisidF030)

**Module series coverage:** F020,F030

### MPM logo 50d
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: MPM_LOGO, bit 43, mask 11110000b -> `550d`

## ekfxisid.xml — BKOMBI L7_BASIS (CAFD 00000760, author: ekfxisidF030)

**Module series coverage:** F020,F030

### Enable Sport+ menu in cluster       [Changwon ll Daltanyang]
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 300C: FDS_MENUE, bit 54, mask 11111111b -> `menue_3`

## ekfxisid.xml — BKOMBI L7_BASIS (CAFD 00000760, author: ekfxisidF030)

**Module series coverage:** F020,F030

### Digital speedometer in instrument cluster
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: BC_DIGITAL_V, bit 1, mask 00000010b -> `aktiv`
  * Group 3000: BC_V_KORREKTUR, bit 1, mask 01000000b -> `nicht_aktiv`

## ekfxisid.xml — BKOMBI L7_BASIS (CAFD 00000760, author: ekfxisidF030)

**Module series coverage:** F020,F030

### Enable motor temperature display
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: BC_MOTORTEMP_ENABLE, bit 3, mask 00010000b -> `aktiv`

## ekfxisid.xml — BKOMBI L7_BASIS (CAFD 00000760, author: ekfxisidF030)

**Module series coverage:** F020,F030

### Instrument cluster M Performance logo
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: BMW_LOGO, bit 0, mask 11110000b -> `01`

## ekfxisid.xml — EGS (CAFD 0000023F, author: ekfxisidF030)

**Module series coverage:** F020,F030

### Display gear position S1-S8 in DS mode [Changwon ll Daltanyang]
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: SPORTSCHALTER_ALT, bit 0, mask 01000000b -> `aktiv`
  * Group 3000: SPORTSCHALTER, bit 1, mask 00000001b -> `aktiv`

## ekfxisid.xml — REM (CAFD 000007A1, author: ekfxisidF030)

**Module series coverage:** F020,F030

### Daytime tail lamps synchronized with daytime headlights [Changwon ll Daltanyang]
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3062: MAPPING_TAGFAHRL_H_L_OUTPUT, bit 200, mask 00111111b -> `sl_l`
  * Group 3062: MAPPING_TAGFAHRL_H_R_OUTPUT, bit 210, mask 00111111b -> `sl_r`
  * Group 3062: MAPPING_TAGFAHRL_H2_L_OUTPUT, bit 220, mask 00111111b -> `sl_2_l`
  * Group 3062: MAPPING_TAGFAHRL_H2_R_OUTPUT, bit 230, mask 00111111b -> `sl_2_r`

## ekfxisid.xml — REM (CAFD 000007A1, author: ekfxisidF030)

**Module series coverage:** F020,F030

### Keep rear camera always on
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3203: V_SCHWELLE_1, bit 7, mask 11111111b -> `FF`
  * Group 3203: V_SCHWELLE_2, bit 8, mask 11111111b -> `FF`
  * Group 3203: D_SCHWELLE_1, bit 9, mask 11111111b -> `FF`
  * Group 3203: D_SCHWELLE_2, bit 10, mask 11111111b -> `FF`

## ekfxisid.xml — REM (CAFD 000007A1, author: ekfxisidF030)

**Module series coverage:** F020,F030

### Brake lights -> convert to LED
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3061: BL_L_KALTUEBERWCHUNG, bit 18, mask 00000001b -> `nicht_aktiv`
  * Group 3061: BL_L_WARMUEBERWCHUNG, bit 18, mask 00000010b -> `nicht_aktiv`
  * Group 3061: BL_L_IS_LED, bit 18, mask 00001000b -> `aktiv`
  * Group 3061: BL_R_KALTUEBERWCHUNG, bit 22, mask 00000001b -> `nicht_aktiv`
  * Group 3061: BL_R_WARMUEBERWCHUNG, bit 22, mask 00000010b -> `nicht_aktiv`
  * Group 3061: BL_R_IS_LED, bit 22, mask 00001000b -> `aktiv`

## ekfxisid.xml — REM (CAFD 000007A1, author: ekfxisidF030)

**Module series coverage:** F020,F030

### Rear fog lights -> convert to LED
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3061: NSL_L_KALTUEBERWCHUNG, bit 34, mask 00000001b -> `nicht_aktiv`
  * Group 3061: NSL_L_WARMTUEBERWCHUNG, bit 34, mask 00000010b -> `nicht_aktiv`
  * Group 3061: NSL_L_IS_LED, bit 34, mask 00001000b -> `aktiv`
  * Group 3061: NSL_R_KALTUEBERWCHUNG, bit 38, mask 00000001b -> `nicht_aktiv`
  * Group 3061: NSL_R_WARMUEBERWCHUNG, bit 38, mask 00000010b -> `nicht_aktiv`
  * Group 3061: NSL_R_IS_LED, bit 38, mask 00001000b -> `aktiv`

## ekfxisid.xml — REM (CAFD 000007A1, author: ekfxisidF030)

**Module series coverage:** F020,F030

### Reverse lights -> convert to LED
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3061: RFS_L_KALTUEBERWCHUNG, bit 42, mask 00000001b -> `nicht_aktiv`
  * Group 3061: RFSL_L_WARMTUEBERWCHUNG, bit 42, mask 00000010b -> `nicht_aktiv`
  * Group 3061: RFS_L_IS_LED, bit 42, mask 00001000b -> `aktiv`
  * Group 3061: RFS_R_KALTUEBERWCHUNG, bit 46, mask 00000001b -> `nicht_aktiv`
  * Group 3061: RFS_R_WARMUEBERWCHUNG, bit 46, mask 00000010b -> `nicht_aktiv`
  * Group 3061: RFS_R_IS_LED, bit 46, mask 00001000b -> `aktiv`

## ekfxisid.xml — REM (CAFD 000007A1, author: ekfxisidF030)

**Module series coverage:** F020,F030

### Rear turn signals -> convert to LED
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3061: FRAFRA_L_KALTUEBERWCHUNG, bit 50, mask 00000001b -> `nicht_aktiv`
  * Group 3061: FRAL_L_WARMTUEBERWCHUNG, bit 50, mask 00000010b -> `nicht_aktiv`
  * Group 3061: FRA_L_IS_LED, bit 50, mask 00001000b -> `aktiv`
  * Group 3061: FRA_R_KALTUEBERWCHUNG, bit 54, mask 00000001b -> `nicht_aktiv`
  * Group 3061: FRA_R_WARMUEBERWCHUNG, bit 54, mask 00000010b -> `nicht_aktiv`
  * Group 3061: FRA_R_IS_LED, bit 54, mask 00001000b -> `aktiv`

## ekfxisid.xml — REM (CAFD 000007A1, author: ekfxisidF030)

**Module series coverage:** F020,F030

### == Convert all rear lights to LED ==
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3061: bit 10, mask 00000001b -> `00`
  * Group 3061: bit 10, mask 00000010b -> `00`
  * Group 3061: bit 10, mask 00001000b -> `01`
  * Group 3061: bit 14, mask 00000001b -> `00`
  * Group 3061: bit 14, mask 00000010b -> `00`
  * Group 3061: bit 14, mask 00001000b -> `01`
  * Group 3061: bit 18, mask 00000001b -> `00`
  * Group 3061: bit 18, mask 00000010b -> `00`
  * Group 3061: bit 18, mask 00001000b -> `01`
  * Group 3061: bit 22, mask 00000001b -> `00`
  * Group 3061: bit 22, mask 00000010b -> `00`
  * Group 3061: bit 22, mask 00001000b -> `01`
  * Group 3061: bit 26, mask 00000001b -> `00`
  * Group 3061: bit 26, mask 00000010b -> `00`
  * Group 3061: bit 26, mask 00001000b -> `01`
  * Group 3061: bit 30, mask 00000001b -> `00`
  * Group 3061: bit 30, mask 00000010b -> `00`
  * Group 3061: bit 30, mask 00001000b -> `01`
  * Group 3061: bit 34, mask 00000001b -> `00`
  * Group 3061: bit 34, mask 00000010b -> `00`
  * Group 3061: bit 34, mask 00001000b -> `01`
  * Group 3061: bit 38, mask 00000001b -> `00`
  * Group 3061: bit 38, mask 00000010b -> `00`
  * Group 3061: bit 38, mask 00001000b -> `01`
  * Group 3061: bit 42, mask 00000001b -> `00`
  * Group 3061: bit 42, mask 00000010b -> `00`
  * Group 3061: bit 42, mask 00001000b -> `01`
  * Group 3061: bit 46, mask 00000001b -> `00`
  * Group 3061: bit 46, mask 00000010b -> `00`
  * Group 3061: bit 46, mask 00001000b -> `01`
  * Group 3061: bit 50, mask 00000001b -> `00`
  * Group 3061: bit 50, mask 00000010b -> `00`
  * Group 3061: bit 50, mask 00001000b -> `01`
  * Group 3061: bit 54, mask 00000001b -> `00`
  * Group 3061: bit 54, mask 00000010b -> `00`
  * Group 3061: bit 54, mask 00001000b -> `01`
  * Group 3061: bit 66, mask 00001000b -> `01`
  * Group 3061: bit 70, mask 00001000b -> `01`

## ekfxisid.xml — ICMQL (CAFD 0000067B, author: ekfxisidF030)

**Module series coverage:** F020,F030

### Enable Sport+ mode in cluster -> KOMBI [Changwon ll Daltanyang]
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: IcmKod_B_Sportlenkung, bit 28, mask 11111111b -> `verbaut`

## ekfxisid.xml — ICMQL (CAFD 0000067B, author: ekfxisidF030)

**Module series coverage:** F020,F030

### Set ECO PRO as default driving mode
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: IcmKod_B_InitEco, bit 36, mask 00001000b -> `verbaut`

## ekfxisid.xml — ICMQL (CAFD 0000067B, author: ekfxisidF030)

**Module series coverage:** F020,F030

### Enable cruise control -> KOMBI
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: C_Fahrfunktion, bit 128, mask 00001110b -> `verbaut`

## ekfxisid.xml — SM2 (CAFD 000000B5, author: ekfxisidF030)

**Module series coverage:** F020,F030

### Easy Access 1/3 (Easy Entry) [Changwon ll Daltanyang]
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: EINAUSSTIEGSHILFE, bit 0, mask 00011100b -> `Modus_FA_SLV`

## ekfxisid.xml — SM2 (CAFD 000000B5, author: ekfxisidF030)

**Module series coverage:** F020,F030

### Easy Access 2/3 (Easy Entry)
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3012: EAH_SCHUTZFREIRAUM_HINTEN_SLV_PHYS, bits 4-5, mask 11111111b -> `00, 1E`

## ekfxisid.xml — SM2 (CAFD 000000B5, author: ekfxisidF030)

**Module series coverage:** F020,F030

### Easy Access 3/3 (Easy Entry)
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3012: EAH_VERFAHRWEG_SLV_PHYS, bits 0-1, mask 11111111b -> `00, 46`

## ekfxisid.xml — SM2 (CAFD 000000B5, author: ekfxisidF030)

**Module series coverage:** F020,F030

### Set memory gong alert sound
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: MEMORY_GONG, bit 2, mask 00001000b -> `Aktiv`

## ekfxisid.xml — HU_NBT (CAFD 00000DED, author: ekfxisidF030)

**Module series coverage:** F020,F030

### Unlock DMB/DVD/Navi while driving [Changwon ll Daltanyang]
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: SPEEDLOCK_X_KMH_MAX, bit 72, mask 11111111b -> `FF`
  * Group 3000: SPEEDLOCK_X_KMH_MIN, bit 71, mask 11111111b -> `FF`
  * Group 3000: VIDEO_FRONT_LOCKED, bit 5, mask 00010000b -> `nicht_aktiv`
  * Group 3000: VIDEO_HANDBRAKE, bit 5, mask 00000100b -> `nicht_aktiv`
  * Group 3000: VIDEO_SPEEDLOCK_CONDITION, bit 57, mask 00000111b -> `None`

## ekfxisid.xml — HU_NBT (CAFD 00000DED, author: ekfxisidF030)

**Module series coverage:** F020,F030

### M performance
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3001: STARTUP_EMBLEM, bit 62, mask 01111000b -> `01`

## ekfxisid.xml — HU_NBT (CAFD 00000DED, author: ekfxisidF030)

**Module series coverage:** F020,F030

### X - Drive
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: COMPASS, bit 5, mask 00000001b -> `aktiv`
  * Group 3000: X_VIEW, bit 15, mask 00000001b -> `aktiv`
  * Group 3000: X_VIEW_GRAPHIC_SLOP, bit 26, mask 00110000b -> `trajectory1`
  * Group 3000: X_VIEW_GRAPHIC_ROLL, bit 26, mask 11000000b -> `trajectory1`
  * Group 3000: MOMENTDISTRIBUTION_MENU, bit 110, mask 00000010b -> `aktiv`

## ekfxisid.xml — HU_NBT (CAFD 00000DED, author: ekfxisidF030)

**Module series coverage:** F020,F030

### Change warning sound
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3002: SOUND_SIGNAL_SET, bit 26, mask 00111000b -> `rolls_royce`

## ekfxisid.xml — HU_NBT (CAFD 00000DED, author: ekfxisidF030)

**Module series coverage:** F020,F030

### Enable USB video playback 1/2
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: ENT_CODEC_OGG, bit 15, mask 00010000b -> `aktiv`
  * Group 3000: ENT_CODEC_XVID, bit 15, mask 00100000b -> `aktiv`
  * Group 3000: ENT_CODEC_VCD, bit 15, mask 01000000b -> `aktiv`
  * Group 3000: ENT_MC_VIDEO_SUPPORT, bit 13, mask 00000100b -> `aktiv`

## ekfxisid.xml — HU_NBT (CAFD 00000DED, author: ekfxisidF030)

**Module series coverage:** F020,F030

### Enable USB video playback 2/2
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3003: API_USB_VIDEO, bit 33, mask 00000110b -> `both`
  * Group 3003: API_IPOD_VIEDO, bit 33, mask 00011000b -> `both`

## ekfxisid.xml — HU_NBT (CAFD 00000DED, author: ekfxisidF030)

**Module series coverage:** F020,F030

### Remove all warning messages
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3001: MACRO_CAM_LEGALDISCLAIMER, bit 52, mask 11111111b -> `00`
  * Group 3001: LEGAL_DISCLAIMER_TIME, bit 58, mask 11111111b -> `00`

## ekfxisid.xml — HU_NBT (CAFD 00000DED, author: ekfxisidF030)

**Module series coverage:** F020,F030

### Enable automatic time setting
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: SETTINGS_TIME_AUTOMATIC, bit 19, mask 00000110b -> `navigation`
  * Group 3000: CLOCK_CHANGE_AUTOMATIC, bit 105, mask 00100000b -> `aktiv`

## ekfxisid.xml — HU_NBT (CAFD 00000DED, author: ekfxisidF030)

**Module series coverage:** F020,F030

### Enable rear camera zoom
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3001: MACRO_TRAILER_COUPLING, bit 54, mask 00000001b -> `aktiv`

## ekfxisid.xml — HU_NBT (CAFD 00000DED, author: ekfxisidF030)

**Module series coverage:** F020,F030

### Enable daylight running lights
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: DAYDRIVING_LIGHT, bit 92, mask 00011000b -> `02`

## ekfxisid.xml — HU_NBT (CAFD 00000DED, author: ekfxisidF030)

**Module series coverage:** F020,F030

### Output ringtone through speakers (iOS only)
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3003: INBAND_RINGING, bit 6, mask 10000000b -> `aktiv`

## ekfxisid.xml — HU_NBT (CAFD 00000DED, author: ekfxisidF030)

**Module series coverage:** F020,F030

### Configure Sport mode 1/3
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: EFF_DYN_SPORT_CID, bit 101, mask 00010000b -> `aktiv`

## ekfxisid.xml — HU_NBT (CAFD 00000DED, author: ekfxisidF030)

**Module series coverage:** F020,F030

### Configure Sport mode 2/3
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: EFF_DYN_SPORT_UNIT, bit 107, mask 00000100b -> `aktiv`

## ekfxisid.xml — HU_NBT (CAFD 00000DED, author: ekfxisidF030)

**Module series coverage:** F020,F030

### Configure Sport mode 3/3
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3001: MACRO_FDS, bit 55, mask 00011000b -> `popup_and_config`

## ekfxisid.xml — HU_NBT (CAFD 00000DED, author: ekfxisidF030)

**Module series coverage:** F020,F030

### Bang & Olufsen profile
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: HIGH_END_AUDIO_B_UND_W, bit 21, mask 01100000b -> `keine_insz`

## ekfxisid.xml — HU_NBT (CAFD 00000DED, author: ekfxisidF030)

**Module series coverage:** F020,F030

### Enable Logic7 (S667A HiFi vehicles)
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: LOGIC7_SYMBOL, bit 22, mask 00001000b -> `aktiv`

## ekfxisid.xml — HU_NBT (CAFD 00000DED, author: ekfxisidF030)

**Module series coverage:** F020,F030

### Door lock/unlock chime (vehicles with anti-theft module except M5)
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: ACOUSTICAL_LOCK_CONFIRM, bit 110, mask 00000001b -> `Aktiv`

## ekfxisid.xml — HU_NBT (CAFD 00000DED, author: ekfxisidF030)

**Module series coverage:** F020,F030

### Enable TPMC tire pressure temperature
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3001: RDC_SAFETY, bit 1, mask 00100000b -> `Aktiv`

## ekfxisid.xml — HU_NBT (CAFD 00000DED, author: ekfxisidF030)

**Module series coverage:** F020,F030

### Change M Sport display cluster colors
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: M_VEHICLE, bit 133, mask 01000000b -> `aktiv`

## ekfxisid.xml — HU_NBT (CAFD 00000DED, author: ekfxisidF030)

**Module series coverage:** F020,F030

### High-beam assistant
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: HIGH_BEAM_ASSISTANT, bit 109, mask 10000000b -> `01`

## ekfxisid.xml — HU_NBT2 (CAFD 00001EF6, author: ekfxisidF030)

**Module series coverage:** F020,F030

### Unlock DMB/DVD/Navi while driving 1/2 [Changwon ll Daltanyang]
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3006: SPEEDLOCK_X_KMH_MAX, bit 25, mask 11111111b -> `FF`
  * Group 3006: SPEEDLOCK_X_KMH_MIN, bit 26, mask 11111111b -> `FF`

## ekfxisid.xml — HU_NBT2 (CAFD 00001EF6, author: ekfxisidF030)

**Module series coverage:** F020,F030

### Unlock DMB/DVD/Navi while driving 2/2
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: VIDEO_FRONT_LOCKED, bit 5, mask 00010000b -> `nicht_aktiv`
  * Group 3000: VIDEO_HANDBRAKE, bit 5, mask 00000100b -> `nicht_aktiv`
  * Group 3000: VIDEO_SPEEDLOCK_CONDITION, bit 2, mask 00000111b -> `None`

## ekfxisid.xml — HU_NBT2 (CAFD 00001EF6, author: ekfxisidF030)

**Module series coverage:** F020,F030

### M performance
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3001: STARTUP_EMBLEM, bit 62, mask 01111000b -> `01`

## ekfxisid.xml — HU_NBT2 (CAFD 00001EF6, author: ekfxisidF030)

**Module series coverage:** F020,F030

### X - Drive
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: COMPASS, bit 5, mask 00000001b -> `aktiv`
  * Group 3000: X_VIEW, bit 15, mask 00000001b -> `aktiv`
  * Group 3000: X_VIEW_GRAPHIC_SLOP, bit 26, mask 00110000b -> `trajectory1`
  * Group 3000: X_VIEW_GRAPHIC_ROLL, bit 26, mask 11000000b -> `trajectory1`
  * Group 3000: MOMENTDISTRIBUTION_MENU, bit 110, mask 00000010b -> `aktiv`

## ekfxisid.xml — HU_NBT2 (CAFD 00001EF6, author: ekfxisidF030)

**Module series coverage:** F020,F030

### Change warning sound
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3002: SOUND_SIGNAL_SET, bit 26, mask 00111000b -> `rolls_royce`

## ekfxisid.xml — HU_NBT2 (CAFD 00001EF6, author: ekfxisidF030)

**Module series coverage:** F020,F030

### Enable USB video playback 1/2
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: ENT_CODEC_OGG, bit 15, mask 00010000b -> `aktiv`
  * Group 3000: ENT_CODEC_XVID, bit 15, mask 00100000b -> `aktiv`
  * Group 3000: ENT_CODEC_VCD, bit 15, mask 01000000b -> `aktiv`
  * Group 3000: ENT_MC_VIDEO_SUPPORT, bit 13, mask 00000100b -> `aktiv`

## ekfxisid.xml — HU_NBT2 (CAFD 00001EF6, author: ekfxisidF030)

**Module series coverage:** F020,F030

### Enable USB video playback 2/2
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3003: API_USB_VIDEO, bit 33, mask 00000110b -> `both`
  * Group 3003: API_IPOD_VIEDO, bit 33, mask 00011000b -> `both`

## ekfxisid.xml — HU_NBT2 (CAFD 00001EF6, author: ekfxisidF030)

**Module series coverage:** F020,F030

### Remove all warning messages
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3001: MACRO_CAM_LEGALDISCLAIMER, bit 52, mask 11111111b -> `00`
  * Group 3001: LEGAL_DISCLAIMER_TIME, bit 58, mask 11111111b -> `00`

## ekfxisid.xml — HU_NBT2 (CAFD 00001EF6, author: ekfxisidF030)

**Module series coverage:** F020,F030

### Enable automatic time setting
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: SETTINGS_TIME_AUTOMATIC, bit 19, mask 00000110b -> `navigation`
  * Group 3000: CLOCK_CHANGE_AUTOMATIC, bit 105, mask 00100000b -> `aktiv`

## ekfxisid.xml — HU_NBT2 (CAFD 00001EF6, author: ekfxisidF030)

**Module series coverage:** F020,F030

### Enable rear camera zoom
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3001: MACRO_TRAILER_COUPLING, bit 54, mask 00000001b -> `aktiv`

## ekfxisid.xml — HU_NBT2 (CAFD 00001EF6, author: ekfxisidF030)

**Module series coverage:** F020,F030

### Enable daylight running lights
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: DAYDRIVING_LIGHT, bit 92, mask 00011000b -> `02`

## ekfxisid.xml — HU_NBT2 (CAFD 00001EF6, author: ekfxisidF030)

**Module series coverage:** F020,F030

### Output ringtone through speakers (iOS only)
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3003: INBAND_RINGING, bit 6, mask 10000000b -> `aktiv`

## ekfxisid.xml — HU_NBT2 (CAFD 00001EF6, author: ekfxisidF030)

**Module series coverage:** F020,F030

### Configure Sport mode 1/3
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3009: EFF_DYN_SPORT_CID, bit 9, mask 00010000b -> `aktiv`

## ekfxisid.xml — HU_NBT2 (CAFD 00001EF6, author: ekfxisidF030)

**Module series coverage:** F020,F030

### Configure Sport mode 2/3
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3009: EFF_DYN_SPORT_UNIT, bit 9, mask 00100000b -> `aktiv`

## ekfxisid.xml — HU_NBT2 (CAFD 00001EF6, author: ekfxisidF030)

**Module series coverage:** F020,F030

### Configure Sport mode 3/3
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3008: MACRO_FDS, bit 79, mask 11000000b -> `popup_and_config`

## ekfxisid.xml — HU_NBT2 (CAFD 00001EF6, author: ekfxisidF030)

**Module series coverage:** F020,F030

### Bang & Olufsen profile
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: HIGH_END_AUDIO_B_UND_W, bit 21, mask 01100000b -> `keine_insz`

## ekfxisid.xml — HU_NBT2 (CAFD 00001EF6, author: ekfxisidF030)

**Module series coverage:** F020,F030

### Enable Logic7 (S667A HiFi vehicles)
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: LOGIC7_SYMBOL, bit 22, mask 00001000b -> `aktiv`

## ekfxisid.xml — HU_NBT2 (CAFD 00001EF6, author: ekfxisidF030)

**Module series coverage:** F020,F030

### HUD : Affichage de l'assistant collision Step 2 (Step 1 dans KOMBI)
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 300C: HUD_DISTANCE_INFO, bit 0, mask 00010000b -> `Aktiv`

## ekfxisid.xml — HU_NBT2 (CAFD 00001EF6, author: ekfxisidF030)

**Module series coverage:** F020,F030

### Door lock/unlock chime (vehicles with anti-theft module except M5)
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: ACOUSTICAL_LOCK_CONFIRM, bit 110, mask 00000001b -> `Aktiv`

## ekfxisid.xml — HU_NBT2 (CAFD 00001EF6, author: ekfxisidF030)

**Module series coverage:** F020,F030

### Enable TPMC tire pressure temperature
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3001: RDC_SAFETY, bit 1, mask 00100000b -> `Aktiv`

## ekfxisid.xml — HU_NBT2 (CAFD 00001EF6, author: ekfxisidF030)

**Module series coverage:** F020,F030

### Change M Sport display cluster colors
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: M_VEHICLE, bit 133, mask 01000000b -> `aktiv`

## ekfxisid.xml — HU_NBT2 (CAFD 00001EF6, author: ekfxisidF030)

**Module series coverage:** F020,F030

### High-beam assistant
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: HIGH_BEAM_ASSISTANT, bit 109, mask 10000000b -> `01`

## ekfxisid.xml — HU_CICHB (CAFD 000000F9, author: ekfxisidF030)

**Module series coverage:** F020,F030

### Unlock DMB/DVD/Navi while driving [Changwon ll Daltanyang]
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: SPEEDLOCK_X_KMH_MIN, bit 23, mask 11111111b -> `FF`
  * Group 3000: SPEEDLOCK_X_KMH_MAX, bit 24, mask 11111111b -> `FF`

## ekfxisid.xml — HU_CICHB (CAFD 000000F9, author: ekfxisidF030)

**Module series coverage:** F020,F030

### Enable rear camera zoom
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3001: MACRO_TRAILER_COUPLING, bit 23, mask 00000001b -> `aktiv`

## ekfxisid.xml — HU_CICHB (CAFD 000000F9, author: ekfxisidF030)

**Module series coverage:** F020,F030

### Configure Sport mode 1/3
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: EFF_DYN_SPORT_CID, bit 47, mask 00010000b -> `aktiv`

## ekfxisid.xml — HU_CICHB (CAFD 000000F9, author: ekfxisidF030)

**Module series coverage:** F020,F030

### Configure Sport mode 2/3
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: EFF_DYN_SPORT_UNIT, bit 61, mask 00000100b -> `aktiv`

## ekfxisid.xml — HU_CICHB (CAFD 000000F9, author: ekfxisidF030)

**Module series coverage:** F020,F030

### Configure Sport mode 3/3
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: MACRO_FDS, bit 7, mask 00110000b -> `popup_and_config`

## ekfxisid.xml — BDC_01 (CAFD 000017BE, author: ekfxisidF025)

**Module series coverage:** F015,F016,F025

### Turn off audio and navigation when door opens after engine off [Changwon ll Daltanyang]
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3020: TCM_LOGIC_R_OFF_DOOR, bit 9, mask 00000001b -> `aktiv`

## ekfxisid.xml — BDC_01 (CAFD 000017BE, author: ekfxisidF025)

**Module series coverage:** F015,F016,F025

### Remember last auto start/stop state
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3023: TCM_MSA_MEMORY, bit 0, mask 00100000b -> `aktiv`

## ekfxisid.xml — BDC_01 (CAFD 000017BE, author: ekfxisidF025)

**Module series coverage:** F015,F016,F025

### Turn off auto start/stop in ECO Pro mode
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3023: TCM_MSA_ECO_MODE, bit 1, mask 00000100b -> `nicht_aktiv`

## ekfxisid.xml — BDC_01 (CAFD 000017BE, author: ekfxisidF025)

**Module series coverage:** F015,F016,F025

### Turn off auto start/stop in Comfort mode
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3023: TCM_MSA_DEFAULT_OFF, bit 0, mask 00010000b -> `aktiv`

## ekfxisid.xml — BDC_01 (CAFD 000017BE, author: ekfxisidF025)

**Module series coverage:** F015,F016,F025

### Allow windows to operate with doors open
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3050: FH_TUERAUF_STOP_MAUT, bit 0, mask 00000001b -> `nicht_aktiv`

## ekfxisid.xml — BDC_01 (CAFD 000017BE, author: ekfxisidF025)

**Module series coverage:** F015,F016,F025

### Mirror lock folding (one-touch)
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3056: KOMFORT_SCHLIESSEN, bit 10, mask 11111111b -> `00`

## ekfxisid.xml — BDC_01 (CAFD 000017BE, author: ekfxisidF025)

**Module series coverage:** F015,F016,F025

### Passenger mirror angle adjustment
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3110: ASP_BORDSTEINAUTOMAIK_DELTA, bit 1, mask 11111111b -> `1E`

## ekfxisid.xml — BDC_01 (CAFD 000017BE, author: ekfxisidF025)

**Module series coverage:** F015,F016,F025

### Turn signal flashes five times
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3068: BLINKZYKLEN_ANZAHL_TIPP, bit 7, mask 00000111b -> `04`

## ekfxisid.xml — BDC_01 (CAFD 000017BE, author: ekfxisidF025)

**Module series coverage:** F015,F016,F025

### Flash hazard lights during hard braking(50km/h)
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3068: WB_GB_ENABLE, bit 26, mask 00000001b -> `aktiv`
  * Group 3068: WB_GB_GEFAHRENWERT_MIN, bits 23-24, mask 11111111b -> `00, 32`

## ekfxisid.xml — BDC_01 (CAFD 000017BE, author: ekfxisidF025)

**Module series coverage:** F015,F016,F025

### Enable dynamic brake lights
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3068: ESS_AKTIVIERBARER_AUSGANG, bit 16, mask 00000011b -> `bremslicht_blinkend`
  * Group 3068: ESS_AKTIVIERUNG_REALE_VERZ, bit 20, mask 00011111b -> `04`
  * Group 3068: ESS_DEAKTIVIERUNG_REALE_VERZ, bit 19, mask 00011111b -> `04`
  * Group 3068: ESS_AKTIVIERUNG_GESCHW, bit 17, mask 11111110b -> `05`

## ekfxisid.xml — BDC_01 (CAFD 000017BE, author: ekfxisidF025)

**Module series coverage:** F015,F016,F025

### Auto unfold mirrors above set speed (40 km/h -> 25 km/h)
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3110: ASP_GESCHWINDIGKEIT_AUTO_AUSKLAPPEN, bit 9, mask 11111111b -> `19`

## ekfxisid.xml — BDC_01 (CAFD 000017BE, author: ekfxisidF025)

**Module series coverage:** F015,F016,F025

### Illuminate door handle lights in reverse
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3070: OVT_BEI_RUECKFAHRLICHT, bit 128, mask 00000001b -> `aktiv`

## ekfxisid.xml — BDC_01 (CAFD 000017BE, author: ekfxisidF025)

**Module series coverage:** F015,F016,F025

### Front turn signals -> convert to LED
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3060: FRA_V_L_KALTUEBERWACHUNG, bit 98, mask 00000001b -> `nicht_aktiv`
  * Group 3060: FRA_V_L_WARMUEBERWACHUNG, bit 98, mask 00000010b -> `nicht_aktiv`
  * Group 3060: FRA_V_L_KURZSCHLUSS, bit 98, mask 00000100b -> `aktiv`
  * Group 3060: FRA_V_L_IS_LED, bit 98, mask 00001000b -> `aktiv`
  * Group 3060: FRA_V_R_KALTUEBERWACHUNG, bit 106, mask 00000001b -> `nicht_aktiv`
  * Group 3060: FRA_V_R_WARMUEBERWACHUNG, bit 106, mask 00000010b -> `nicht_aktiv`
  * Group 3060: FRA_V_R_KURZSCHLUSS, bit 106, mask 00000100b -> `aktiv`
  * Group 3060: FRA_V_R_IS_LED, bit 106, mask 00001000b -> `aktiv`

## ekfxisid.xml — BDC_01 (CAFD 000017BE, author: ekfxisidF025)

**Module series coverage:** F015,F016,F025

### Rear turn signals -> convert to LED
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3061: FRA_H_L_KALTUEBERWACHUNG, bit 98, mask 00000001b -> `nicht_aktiv`
  * Group 3061: FRA_H_L_WARMUEBERWACHUNG, bit 98, mask 00000010b -> `nicht_aktiv`
  * Group 3061: FRA_H_L_KURZSCHLUSS, bit 98, mask 00000100b -> `aktiv`
  * Group 3061: FRA_H_L_IS_LED, bit 98, mask 00001000b -> `aktiv`
  * Group 3061: FRA_H_R_KALTUEBERWACHUNG, bit 106, mask 00000001b -> `nicht_aktiv`
  * Group 3061: FRA_H_R_WARMUEBERWACHUNG, bit 106, mask 00000010b -> `nicht_aktiv`
  * Group 3061: FRA_H_R_KURZSCHLUSS, bit 106, mask 00000100b -> `aktiv`
  * Group 3061: FRA_H_R_IS_LED, bit 106, mask 00001000b -> `aktiv`

## ekfxisid.xml — BDC_01 (CAFD 000017BE, author: ekfxisidF025)

**Module series coverage:** F015,F016,F025

### Front fog lights -> convert to LED and remove warning
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3060: NSW_L_KALTUEBERWACHUNG, bit 82, mask 00000001b -> `nicht_aktiv`
  * Group 3060: NSW_L_WARMUEBERWACHUNG, bit 82, mask 00000010b -> `nicht_aktiv`
  * Group 3060: NSW_L_KURZSCHLUSS, bit 82, mask 00000100b -> `aktiv`
  * Group 3060: NSW_L_IS_LED, bit 82, mask 00001000b -> `aktiv`
  * Group 3060: NSW_R_KALTUEBERWACHUNG, bit 90, mask 00000001b -> `nicht_aktiv`
  * Group 3060: NSW_R_WARMUEBERWACHUNG, bit 90, mask 00000010b -> `nicht_aktiv`
  * Group 3060: NSW_R_KURZSCHLUSS, bit 90, mask 00000100b -> `aktiv`
  * Group 3060: NSW_R_IS_LED, bit 90, mask 00001000b -> `aktiv`

## ekfxisid.xml — BDC_01 (CAFD 000017BE, author: ekfxisidF025)

**Module series coverage:** F015,F016,F025

### Daytime tail lamps synchronized with daytime headlights 1/3
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3068: TFL_MODUS, bit 31, mask 00110000b -> `drl_s`

## ekfxisid.xml — BDC_01 (CAFD 000017BE, author: ekfxisidF025)

**Module series coverage:** F015,F016,F025

### Daytime tail lamps synchronized with daytime headlights 2/3
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3064: MAPPING_TAGFAHRL_1_H_L_OUTPUT, bit 221, mask 00111111b -> `sl_l`
  * Group 3064: MAPPING_TAGFAHRL_1_H_R_OUTPUT, bit 234, mask 00111111b -> `sl_r`

## ekfxisid.xml — BDC_01 (CAFD 000017BE, author: ekfxisidF025)

**Module series coverage:** F015,F016,F025

### Daytime tail lamps synchronized with daytime headlights 3/3
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3065: MAPPING_TAGFAHRL_2_H_L_OUTPUT, bit 78, mask 00111111b -> `sl_2_l`
  * Group 3065: MAPPING_TAGFAHRL_2_H_R_OUTPUT, bit 91, mask 00111111b -> `sl_2_r`

## ekfxisid.xml — ACSM_4C (CAFD 00000909, author: ekfxisidF025)

**Module series coverage:** F015,F016,F025

### Seat belt warning chime three times (5 seconds) [Changwon ll Daltanyang]
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3001: GWF_SBR_WARNDAUER, bit 3, mask 11111111b -> `05`

## ekfxisid.xml — ACSM (CAFD 000011AB, author: ekfxisidF025)

**Module series coverage:** F015,F016,F025,F026

### Seat belt warning chime three times (5 seconds) [Changwon ll Daltanyang]
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3001: GWF_SBR_WARNDAUER, bit 11, mask 11111111b -> `05`

## ekfxisid.xml — KAFAS2 (CAFD 00001148, author: ekfxisidF025)

**Module series coverage:** F015,F016,F025

### High-beam assistant 1/4 -> code this first to avoid errors
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3050: FLA_ON_OFF, bit 1, mask 00000001b -> `FLA_on`

## ekfxisid.xml — HKFM (CAFD 000007C8, author: ekfxisidF025)

**Module series coverage:** F015,F016,F025

### Operate power trunk from interior button [Changwon ll Daltanyang]
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3010: SCH_FBD, bit 2, mask 00001000b -> `Aktiv`
  * Group 3010: SCH_TOEHKI, bit 2, mask 00000100b -> `Aktiv`
  * Group 3010: TASTER_FBD, bit 0, mask 00001000b -> `Aktiv`

## ekfxisid.xml — IHKA3 (CAFD 000016EE, author: ekfxisidF025)

**Module series coverage:** F015,F016,F025,F026

### Remember last A/C on/off state [Changwon ll Daltanyang]
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3003: MEMORY_OFF, bit 0, mask 00000010b -> `Aktiv`

## ekfxisid.xml — IHKA3 (CAFD 000016EE, author: ekfxisidF025)

**Module series coverage:** F015,F016,F025,F026

### Remember air recirculation mode
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3003: MEMORY_UMLUFT, bit 0, mask 00000001b -> `Aktiv`

## ekfxisid.xml — IHKA3 (CAFD 000016EE, author: ekfxisidF025)

**Module series coverage:** F015,F016,F025,F026

### Lock air recirculation mode
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3003: UMLUFT_AUTO_AUS, bit 0, mask 10000000b -> `disable`

## ekfxisid.xml — ICM (CAFD 0000067B, author: ekfxisidF025)

**Module series coverage:** F015,F016,F025

### Enable Sport+ mode in cluster -> KOMBI [Changwon ll Daltanyang]
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: IcmKod_B_Sportlenkung, bit 28, mask 11111111b -> `verbaut`

## ekfxisid.xml — ICM (CAFD 0000067B, author: ekfxisidF025)

**Module series coverage:** F015,F016,F025

### Set ECO PRO as default driving mode
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: IcmKod_B_InitEco, bit 36, mask 00001000b -> `verbaut`

## ekfxisid.xml — ICM (CAFD 0000067B, author: ekfxisidF025)

**Module series coverage:** F015,F016,F025

### Enable cruise control -> KOMBI
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: C_Fahrfunktion, bit 128, mask 00001110b -> `verbaut`

## ekfxisid.xml — KOMBI (CAFD 00000069, author: ekfxisidF025)

**Module series coverage:** F015,F016,F025

### Enable Sport+ menu in cluster [Changwon ll Daltanyang]
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

## ekfxisid.xml — KOMBI (CAFD 00000069, author: ekfxisidF025)

**Module series coverage:** F015,F016,F025

### Digital speedometer in instrument cluster
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: BC_DIGITAL_V, bit 1, mask 00000010b -> `Aktiv`
  * Group 3000: BC_V_KORREKTUR, bit 1, mask 01000000b -> `nicht_aktiv`

## ekfxisid.xml — KOMBI (CAFD 00000069, author: ekfxisidF025)

**Module series coverage:** F015,F016,F025

### Show manual gear steps M1-M8 in DS mode
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: SPA_SPORT_ENABLE, bit 39, mask 00010000b -> `Aktiv`

## ekfxisid.xml — KOMBI (CAFD 00000069, author: ekfxisidF025)

**Module series coverage:** F015,F016,F025

### Enable HUD entertainment
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: HUD_ENTERTAINMENT_ENABLE, bit 41, mask 00001000b -> `Aktiv`

## ekfxisid.xml — KOMBI (CAFD 00000069, author: ekfxisidF025)

**Module series coverage:** F015,F016,F025

### Enable HUD phonebook
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: HUD_TELEFONANRUF_ENABLE, bit 41, mask 00010000b -> `Aktiv`
  * Group 3000: HUD_TELEFONBUCH_ENABLE, bit 41, mask 00100000b -> `Aktiv`
  * Group 3000: HUD_SPRACHEINGABE_ENABLE, bit 41, mask 01000000b -> `Aktiv`

## ekfxisid.xml — KOMBI (CAFD 000009C8, author: ekfxisidF025)

**Module series coverage:** F015,F016,F025,F026

### Enable Sport+ menu in cluster [Changwon ll Daltanyang]
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 300C: FDS_MENUE, bit 54, mask 11111111b -> `menue_3`

## ekfxisid.xml — KOMBI (CAFD 000009C8, author: ekfxisidF025)

**Module series coverage:** F015,F016,F025,F026

### Digital speedometer in instrument cluster
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: BC_DIGITAL_V, bit 1, mask 00000010b -> `Aktiv`
  * Group 3000: BC_V_KORREKTUR, bit 1, mask 01000000b -> `nicht_aktiv`

## ekfxisid.xml — KOMBI (CAFD 000009C8, author: ekfxisidF025)

**Module series coverage:** F015,F016,F025,F026

### Logo M performance
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: BMW_LOGO, bit 0, mask 11110000b -> `01`

## ekfxisid.xml — KOMBI (CAFD 000009C8, author: ekfxisidF025)

**Module series coverage:** F015,F016,F025,F026

### Move instrument cluster clock
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: BASISANZEEIGE_VARIANTE, bit 53, mask 01000000b -> `Aktiv`

## ekfxisid.xml — SM2 (CAFD 000000B5, author: ekfxisidF025)

**Module series coverage:** F015,F016,F025

### Easy Access 1/3 (Easy Entry) [Changwon ll Daltanyang]
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: EINAUSSTIEGSHILFE, bit 0, mask 00011100b -> `Modus_FA_SLV`

## ekfxisid.xml — SM2 (CAFD 000000B5, author: ekfxisidF025)

**Module series coverage:** F015,F016,F025

### Easy Access 2/3 (Easy Entry)
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3012: EAH_SCHUTZFREIRAUM_HINTEN_SLV_PHYS, bits 4-5, mask 11111111b -> `00, 1E`

## ekfxisid.xml — SM2 (CAFD 000000B5, author: ekfxisidF025)

**Module series coverage:** F015,F016,F025

### Easy Access 3/3 (Easy Entry)
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3012: EAH_VERFAHRWEG_SLV_PHYS, bits 0-1, mask 11111111b -> `00, 46`

## ekfxisid.xml — SM2 (CAFD 000000B5, author: ekfxisidF025)

**Module series coverage:** F015,F016,F025

### Set memory gong alert sound
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: MEMORY_GONG, bit 2, mask 00001000b -> `Aktiv`

## ekfxisid.xml — CAS_04 (CAFD 0000000F, author: ekfxisidF025)

**Module series coverage:** F015,F016,F025

### Auto start/stop default off [Changwon ll Daltanyang]
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: TCM_MSA_DEFAULT_OFF, bit 3, mask 00010000b -> `01`

## ekfxisid.xml — CAS_04 (CAFD 0000000F, author: ekfxisidF025)

**Module series coverage:** F015,F016,F025

### Remember last auto start/stop state
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: TCM_MSA_MEMORY, bit 3, mask 00100000b -> `aktiv`

## ekfxisid.xml — CAS_04 (CAFD 0000000F, author: ekfxisidF025)

**Module series coverage:** F015,F016,F025

### Start engine without pressing brake 1/2
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: TC_STARTLOCK_BRAKE, bit 1, mask 00000001b -> `nicht_aktiv`

## ekfxisid.xml — CAS_04 (CAFD 0000000F, author: ekfxisidF025)

**Module series coverage:** F015,F016,F025

### Start engine without pressing brake 2/2
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: TC_STARTLOCK_DRIVINGREADINESS, bit 1, mask 00010000b -> `nicht_aktiv`

## ekfxisid.xml — CAS_04 (CAFD 0000000F, author: ekfxisidF025)

**Module series coverage:** F015,F016,F025

### Mirror lock folding
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3003: KMFRT_SCHLESSEN, bit 12, mask 11111111b -> `00`

## ekfxisid.xml — CAS_04 (CAFD 0000000F, author: ekfxisidF025)

**Module series coverage:** F015,F016,F025

### Turn off audio/navigation when door opens after shutdown
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: TC_LOGIC_KLR_OFF_DOOR, bit 2, mask 00000001b -> `aktiv`

## ekfxisid.xml — CAS_04 (CAFD 0000000F, author: ekfxisidF025)

**Module series coverage:** F015,F016,F025

### Horn alarm when locking with engine running
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3002: CLM_HORN_AT_SECURE, bit 0, mask 00100000b -> `aktiv`

## ekfxisid.xml — FRM (CAFD 0000012F, author: ekfxisidF025)

**Module series coverage:** F015,F016,F025

### High-beam assistant 2/4 -> code KAFAS2 1/4 first [Changwon ll Daltanyang]
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3050: FLA_VERBAUT, bit 20, mask 00010000b -> `aktiv`

## ekfxisid.xml — FRM (CAFD 0000012F, author: ekfxisidF025)

**Module series coverage:** F015,F016,F025

### High-beam assistant 3/4 -> code HU_NBT 4/4 last
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3050: FLA_AUTO_AKTIV, bit 20, mask 00100000b -> `automatisch`

## ekfxisid.xml — FRM (CAFD 0000012F, author: ekfxisidF025)

**Module series coverage:** F015,F016,F025

### Passenger mirror angle adjustment
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3020: ASP_BORDSTEINAUTOMAIK_DELTA, bit 1, mask 11111111b -> `1E`

## ekfxisid.xml — FRM (CAFD 0000012F, author: ekfxisidF025)

**Module series coverage:** F015,F016,F025

### Auto unfold mirrors above set speed (40 km/h -> 25 km/h)
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3020: ASP_GESCHWINDIGKEIT_AUTO_AUSKLAPPEN, bit 9, mask 11111111b -> `19`

## ekfxisid.xml — FRM (CAFD 0000012F, author: ekfxisidF025)

**Module series coverage:** F015,F016,F025

### Allow windows to operate with doors open 1/2 (front) -> JBBF 2/2 (rear)
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3030: FH_TUER_AUF_STOP_MAUT, bit 1, mask 00000100b -> `nicht aktiv`

## ekfxisid.xml — FRM (CAFD 0000012F, author: ekfxisidF025)

**Module series coverage:** F015,F016,F025

### Daytime tail lamps
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3050: DRL_MODUS, bit 20, mask 00001110b -> `drl_s`

## ekfxisid.xml — FRM (CAFD 0000012F, author: ekfxisidF025)

**Module series coverage:** F015,F016,F025

### Enable dynamic brake lights
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3050: ESS_ERSCHEINUNGSBILD, bit 23, mask 01110000b -> `bremslicht blinkend`
  * Group 3050: ESS_GESCHW_SCHWELLE, bit 24, mask 01111111b -> `US`
  * Group 3050: ESS_ON_VERZ, bit 21, mask 00011111b -> `04`
  * Group 3050: ESS_OFF_VERZ, bit 22, mask 00011111b -> `04`

## ekfxisid.xml — FRM (CAFD 0000012F, author: ekfxisidF025)

**Module series coverage:** F015,F016,F025

### Flash hazard lights during hard braking
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3050: WB_GB_ENABLE, bit 2, mask 10000000b -> `aktiv`

## ekfxisid.xml — FRM (CAFD 0000012F, author: ekfxisidF025)

**Module series coverage:** F015,F016,F025

### Increase Angel Eye brightness to 30%
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3060: U_EFF_POL, bit 1, mask 11111111b -> `1E`

## ekfxisid.xml — FRM (CAFD 0000012F, author: ekfxisidF025)

**Module series coverage:** F015,F016,F025

### Welcome light fog lamps (hard on)
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3050: WL_FUNKTION_NSW, bit 29, mask 00001100b -> `Hard_on`

## ekfxisid.xml — FRM (CAFD 0000012F, author: ekfxisidF025)

**Module series coverage:** F015,F016,F025

### Welcome light fog lamps (soft on)
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3050: WL_FUNKTION_NSW, bit 29, mask 00001100b -> `Soft_on`

## ekfxisid.xml — FRM (CAFD 0000012F, author: ekfxisidF025)

**Module series coverage:** F015,F016,F025

### Front fog lights -> convert to LED and remove warning
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3090: AUSG_11_NSW_L_WARM_UEBERW_AKTIV, bit 79, mask 00000001b -> `00`
  * Group 3090: AUSG_11_NSW_L_KALT_UEBERW_AKTIV, bit 79, mask 00000010b -> `00`
  * Group 3090: AUSG_11_NSW_L_IS_LED, bit 79, mask 00001000b -> `aktiv`
  * Group 3090: AUSG_11_NSW_R_WARM_UEBERW_AKTIV, bit 83, mask 00000001b -> `00`
  * Group 3090: AUSG_11_NSW_R_KALT_UEBERW_AKTIV, bit 83, mask 00000010b -> `00`
  * Group 3090: AUSG_11_NSW_R_IS_LED, bit 83, mask 00001000b -> `aktiv`

## ekfxisid.xml — FRM (CAFD 0000012F, author: ekfxisidF025)

**Module series coverage:** F015,F016,F025

### Reverse lights -> convert to LED
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3090: AUSG_24_RFS_L_WARM_UEBERW_AKTIV, bit 131, mask 00000001b -> `nicht_aktiv`
  * Group 3090: AUSG_24_RFS_L_KALT_UEBERW_AKTIV, bit 131, mask 00000010b -> `nicht_aktiv`
  * Group 3090: AUSG_24_RFS_L_IS_LED, bit 131, mask 00001000b -> `aktiv`
  * Group 3090: AUSG_24_RFS_R_WARM_UEBERW_AKTIV, bit 135, mask 00000001b -> `nicht_aktiv`
  * Group 3090: AUSG_24_RFS_R_KALT_UEBERW_AKTIV, bit 135, mask 00000010b -> `nicht_aktiv`
  * Group 3090: AUSG_24_RFS_R_IS_LED, bit 135, mask 00001000b -> `aktiv`

## ekfxisid.xml — JBBFE (CAFD 00000014, author: ekfxisidF025)

**Module series coverage:** F015,F016,F025

### Disable headlight washer fluid [Changwon ll Daltanyang]
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: SCHEINWERFERREINIGUNG, bit 8, mask 00000001b -> `nicht_aktiv`

## ekfxisid.xml — JBBFE (CAFD 00000014, author: ekfxisidF025)

**Module series coverage:** F015,F016,F025

### Allow windows to operate when door open 2/2 (rear)
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3070: FH_TUERAUF_STOP_MAUT, bit 0, mask 00000100b -> `nicht_aktiv`

## ekfxisid.xml — JBBFE (CAFD 00000014, author: ekfxisidF025)

**Module series coverage:** F015,F016,F025

### Adjust automatic light sensor
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3530: RLS_FLC_SCHWELLWERT_SATZ, bit 5, mask 00111000b -> `unempfindlich`

## ekfxisid.xml — JBBFE (CAFD 00000014, author: ekfxisidF025)

**Module series coverage:** F015,F016,F025

### Adjust rain sensor
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3530: RLS_DEF_FLC_SCHWELLWERT_SATZ, bit 5, mask 00000111b -> `unempfindlich`

## ekfxisid.xml — HU_CIC (CAFD 000000F9, author: ekfxisidF025)

**Module series coverage:** F015,F016,F025

### Unlock DMB/DVD/Navi while driving [Changwon ll Daltanyang]
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: SPEEDLOCK_X_KMH_MAX, bit 23, mask 11111111b -> `FF`
  * Group 3000: SPEEDLOCK_X_KMH_MIN, bit 24, mask 11111111b -> `FF`
  * Group 3000: VIDEO_NUR_MIT_HANDBREMSE, bit 8, mask 01000000b -> `nicht_aktiv`

## ekfxisid.xml — HU_CIC (CAFD 000000F9, author: ekfxisidF025)

**Module series coverage:** F015,F016,F025

### Enable rear camera zoom
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3001: MACRO_TRAILER_COUPLING, bit 23, mask 00000001b -> `aktiv`

## ekfxisid.xml — HU_CIC (CAFD 000000F9, author: ekfxisidF025)

**Module series coverage:** F015,F016,F025

### Configure Sport mode 1/3
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: EFF_DYN_SPORT_CID, bit 47, mask 00010000b -> `aktiv`

## ekfxisid.xml — HU_CIC (CAFD 000000F9, author: ekfxisidF025)

**Module series coverage:** F015,F016,F025

### Configure Sport mode 2/3
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: EFF_DYN_SPORT_UNIT, bit 61, mask 00000100b -> `aktiv`

## ekfxisid.xml — HU_CIC (CAFD 000000F9, author: ekfxisidF025)

**Module series coverage:** F015,F016,F025

### Configure Sport mode 3/3
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: MACRO_FDS, bit 7, mask 00110000b -> `popup_and_config`

## ekfxisid.xml — FRM (CAFD 0000106D, author: ekfxisidF025)

**Module series coverage:** F015,F016,F025

### High-beam assistant 2/4 -> code KAFAS2 1/4 first [Changwon ll Daltanyang]
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3050: FLA_VERBAUT, bit 20, mask 00010000b -> `aktiv`

## ekfxisid.xml — FRM (CAFD 0000106D, author: ekfxisidF025)

**Module series coverage:** F015,F016,F025

### High-beam assistant 3/4 -> code HU_NBT 4/4 last
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3050: FLA_AUTO_AKTIV, bit 20, mask 00100000b -> `automatisch`

## ekfxisid.xml — FRM (CAFD 0000106D, author: ekfxisidF025)

**Module series coverage:** F015,F016,F025

### Passenger mirror angle adjustment
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3020: ASP_BORDSTEINAUTOMAIK_DELTA, bit 1, mask 11111111b -> `1E`

## ekfxisid.xml — FRM (CAFD 0000106D, author: ekfxisidF025)

**Module series coverage:** F015,F016,F025

### Auto unfold mirrors above set speed (40 km/h -> 25 km/h)
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3020: ASP_GESCHWINDIGKEIT_AUTO_AUSKLAPPEN, bit 9, mask 11111111b -> `19`

## ekfxisid.xml — FRM (CAFD 0000106D, author: ekfxisidF025)

**Module series coverage:** F015,F016,F025

### Allow windows to operate with doors open 1/2 (front) -> JBBF 2/2 (rear)
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3030: FH_TUER_AUF_STOP_MAUT, bit 1, mask 00000100b -> `nicht aktiv`

## ekfxisid.xml — FRM (CAFD 0000106D, author: ekfxisidF025)

**Module series coverage:** F015,F016,F025

### Daytime tail lamps
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3050: DRL_MODUS, bit 20, mask 00001110b -> `drl_s`

## ekfxisid.xml — FRM (CAFD 0000106D, author: ekfxisidF025)

**Module series coverage:** F015,F016,F025

### Enable dynamic brake lights
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3050: ESS_ERSCHEINUNGSBILD, bit 23, mask 01110000b -> `02`
  * Group 3050: ESS_GESCHW_SCHWELLE, bit 24, mask 01111111b -> `US`
  * Group 3050: ESS_ON_VERZ, bit 21, mask 00011111b -> `04`
  * Group 3050: ESS_OFF_VERZ, bit 22, mask 00011111b -> `04`

## ekfxisid.xml — FRM (CAFD 0000106D, author: ekfxisidF025)

**Module series coverage:** F015,F016,F025

### Flash hazard lights during hard braking
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3050: WB_GB_ENABLE, bit 2, mask 10000000b -> `aktiv`

## ekfxisid.xml — FRM (CAFD 0000106D, author: ekfxisidF025)

**Module series coverage:** F015,F016,F025

### Increase Angel Eye brightness to 30%
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3060: U_EFF_POL, bit 1, mask 11111111b -> `1E`

## ekfxisid.xml — FRM (CAFD 0000106D, author: ekfxisidF025)

**Module series coverage:** F015,F016,F025

### Welcome light fog lamps (hard on)
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3050: WL_FUNKTION_NSW, bit 29, mask 00001100b -> `Hard_on`

## ekfxisid.xml — FRM (CAFD 0000106D, author: ekfxisidF025)

**Module series coverage:** F015,F016,F025

### Welcome light fog lamps (soft on)
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3050: WL_FUNKTION_NSW, bit 29, mask 00001100b -> `Soft_on`

## ekfxisid.xml — FRM (CAFD 0000106D, author: ekfxisidF025)

**Module series coverage:** F015,F016,F025

### Front fog lights -> convert to LED and remove warning
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3090: AUSG_11_NSW_L_WARM_UEBERW_AKTIV, bit 79, mask 00000001b -> `00`
  * Group 3090: AUSG_11_NSW_L_KALT_UEBERW_AKTIV, bit 79, mask 00000010b -> `00`
  * Group 3090: AUSG_11_NSW_L_IS_LED, bit 79, mask 00001000b -> `aktiv`
  * Group 3090: AUSG_12_NSW_R_WARM_UEBERW_AKTIV, bit 83, mask 00000001b -> `00`
  * Group 3090: AUSG_12_NSW_R_KALT_UEBERW_AKTIV, bit 83, mask 00000010b -> `00`
  * Group 3090: AUSG_12_NSW_R_IS_LED, bit 83, mask 00001000b -> `aktiv`

## ekfxisid.xml — FRM (CAFD 0000106D, author: ekfxisidF025)

**Module series coverage:** F015,F016,F025

### Reverse lights -> convert to LED
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3090: AUSG_24_RFS_L_WARM_UEBERW_AKTIV, bit 131, mask 00000001b -> `nicht_aktiv`
  * Group 3090: AUSG_24_RFS_L_KALT_UEBERW_AKTIV, bit 131, mask 00000010b -> `nicht_aktiv`
  * Group 3090: AUSG_24_RFS_L_IS_LED, bit 131, mask 00001000b -> `aktiv`
  * Group 3090: AUSG_25_RFS_R_WARM_UEBERW_AKTIV, bit 135, mask 00000001b -> `nicht_aktiv`
  * Group 3090: AUSG_25_RFS_R_KALT_UEBERW_AKTIV, bit 135, mask 00000010b -> `nicht_aktiv`
  * Group 3090: AUSG_25_RFS_R_IS_LED, bit 135, mask 00001000b -> `aktiv`

## ekfxisid.xml — HU_NBT2 (CAFD 00001EF6, author: ekfxisidF025)

**Module series coverage:** F015,F016,F025,F026

### Unlock DMB/DVD/Navi while driving [Changwon ll Daltanyang]
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3006: SPEEDLOCK_X_KMH_MIN, bit 25, mask 11111111b -> `FF`
  * Group 3006: SPEEDLOCK_X_KMH_MAX, bit 26, mask 11111111b -> `FF`

## ekfxisid.xml — HU_NBT2 (CAFD 00001EF6, author: ekfxisidF025)

**Module series coverage:** F015,F016,F025,F026

### M performance
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3001: STARTUP_EMBLEM, bit 62, mask 01111000b -> `01`

## ekfxisid.xml — HU_NBT2 (CAFD 00001EF6, author: ekfxisidF025)

**Module series coverage:** F015,F016,F025,F026

### X - Drive
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: COMPASS, bit 5, mask 00000001b -> `aktiv`
  * Group 3000: X_VIEW, bit 15, mask 00000001b -> `aktiv`

## ekfxisid.xml — HU_NBT2 (CAFD 00001EF6, author: ekfxisidF025)

**Module series coverage:** F015,F016,F025,F026

### Change warning sound
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3002: SOUND_SIGNAL_SET, bit 26, mask 00111000b -> `rolls_royce`

## ekfxisid.xml — HU_NBT2 (CAFD 00001EF6, author: ekfxisidF025)

**Module series coverage:** F015,F016,F025,F026

### Enable USB video
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: ENT_CODEC_OGG, bit 15, mask 00010000b -> `aktiv`
  * Group 3000: ENT_CODEC_XVID, bit 15, mask 00100000b -> `aktiv`
  * Group 3000: ENT_CODEC_VCD, bit 15, mask 01000000b -> `aktiv`
  * Group 3000: ENT_MC_VIDEO_SUPPORT, bit 13, mask 00000100b -> `aktiv`
  * Group 3003: API_USB_VIDEO, bit 33, mask 00000110b -> `both`
  * Group 3003: API_IPOD_VIEDO, bit 33, mask 00011000b -> `both`

## ekfxisid.xml — HU_NBT2 (CAFD 00001EF6, author: ekfxisidF025)

**Module series coverage:** F015,F016,F025,F026

### Remove all warning messages
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3001: MACRO_CAM_LEGALDISCLAIMER, bit 52, mask 11111111b -> `00`
  * Group 3001: LEGAL_DISCLAIMER_TIME, bit 58, mask 11111111b -> `00`

## ekfxisid.xml — HU_NBT2 (CAFD 00001EF6, author: ekfxisidF025)

**Module series coverage:** F015,F016,F025,F026

### Enable automatic time setting
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: SETTINGS_TIME_AUTOMATIC, bit 19, mask 00000110b -> `navigation`
  * Group 3000: CLOCK_CHANGE_AUTOMATIC, bit 105, mask 00100000b -> `aktiv`

## ekfxisid.xml — HU_NBT2 (CAFD 00001EF6, author: ekfxisidF025)

**Module series coverage:** F015,F016,F025,F026

### Enable rear camera zoom
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3001: MACRO_TRAILER_COUPLING, bit 54, mask 00000001b -> `aktiv`

## ekfxisid.xml — HU_NBT2 (CAFD 00001EF6, author: ekfxisidF025)

**Module series coverage:** F015,F016,F025,F026

### Output ringtone through speakers (iOS only)
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3003: INBAND_RINGING, bit 6, mask 10000000b -> `aktiv`

## ekfxisid.xml — HU_NBT2 (CAFD 00001EF6, author: ekfxisidF025)

**Module series coverage:** F015,F016,F025,F026

### Configure Sport mode
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3009: EFF_DYN_SPORT_CID, bit 9, mask 00010000b -> `aktiv`
  * Group 3009: EFF_DYN_SPORT_UNIT, bit 9, mask 00100000b -> `aktiv`
  * Group 3008: MACRO_FDS, bit 79, mask 11000000b -> `popup_and_config`

## ekfxisid.xml — HU_NBT (CAFD 00000DED, author: ekfxisidF025)

**Module series coverage:** F015,F016,F025

### Unlock DMB/DVD/Navi while driving [Changwon ll Daltanyang]
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: SPEEDLOCK_X_KMH_MAX, bit 72, mask 11111111b -> `FF`
  * Group 3000: SPEEDLOCK_X_KMH_MIN, bit 71, mask 11111111b -> `FF`
  * Group 3000: VIDEO_FRONT_LOCKED, bit 5, mask 00010000b -> `nicht_aktiv`
  * Group 3000: VIDEO_HANDBRAKE, bit 5, mask 00000100b -> `nicht_aktiv`
  * Group 3000: VIDEO_SPEEDLOCK_CONDITION, bit 57, mask 00000111b -> `None`

## ekfxisid.xml — HU_NBT (CAFD 00000DED, author: ekfxisidF025)

**Module series coverage:** F015,F016,F025

### M performance
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3001: STARTUP_EMBLEM, bit 62, mask 01111000b -> `01`

## ekfxisid.xml — HU_NBT (CAFD 00000DED, author: ekfxisidF025)

**Module series coverage:** F015,F016,F025

### X - Drive
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: COMPASS, bit 5, mask 00000001b -> `aktiv`
  * Group 3000: X_VIEW, bit 15, mask 00000001b -> `aktiv`
  * Group 3000: X_VIEW_GRAPHIC_SLOP, bit 26, mask 00110000b -> `trajectory1`
  * Group 3000: X_VIEW_GRAPHIC_ROLL, bit 26, mask 11000000b -> `trajectory1`
  * Group 3000: MOMENTDISTRIBUTION_MENU, bit 110, mask 00000010b -> `aktiv`

## ekfxisid.xml — HU_NBT (CAFD 00000DED, author: ekfxisidF025)

**Module series coverage:** F015,F016,F025

### Change warning sound
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3002: SOUND_SIGNAL_SET, bit 26, mask 00111000b -> `rolls_royce`

## ekfxisid.xml — HU_NBT (CAFD 00000DED, author: ekfxisidF025)

**Module series coverage:** F015,F016,F025

### Enable USB video playback 1/2
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: ENT_CODEC_OGG, bit 15, mask 00010000b -> `aktiv`
  * Group 3000: ENT_CODEC_XVID, bit 15, mask 00100000b -> `aktiv`
  * Group 3000: ENT_CODEC_VCD, bit 15, mask 01000000b -> `aktiv`
  * Group 3000: ENT_MC_VIDEO_SUPPORT, bit 13, mask 00000100b -> `aktiv`

## ekfxisid.xml — HU_NBT (CAFD 00000DED, author: ekfxisidF025)

**Module series coverage:** F015,F016,F025

### Enable USB video playback 2/2
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3003: API_USB_VIDEO, bit 33, mask 00000110b -> `both`
  * Group 3003: API_IPOD_VIEDO, bit 33, mask 00011000b -> `both`

## ekfxisid.xml — HU_NBT (CAFD 00000DED, author: ekfxisidF025)

**Module series coverage:** F015,F016,F025

### Remove all warning messages
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3001: MACRO_CAM_LEGALDISCLAIMER, bit 52, mask 11111111b -> `00`
  * Group 3001: LEGAL_DISCLAIMER_TIME, bit 58, mask 11111111b -> `00`

## ekfxisid.xml — HU_NBT (CAFD 00000DED, author: ekfxisidF025)

**Module series coverage:** F015,F016,F025

### Enable automatic time setting
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: SETTINGS_TIME_AUTOMATIC, bit 19, mask 00000110b -> `navigation`
  * Group 3000: CLOCK_CHANGE_AUTOMATIC, bit 105, mask 00100000b -> `aktiv`

## ekfxisid.xml — HU_NBT (CAFD 00000DED, author: ekfxisidF025)

**Module series coverage:** F015,F016,F025

### Enable rear camera zoom
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3001: MACRO_TRAILER_COUPLING, bit 54, mask 00000001b -> `aktiv`

## ekfxisid.xml — HU_NBT (CAFD 00000DED, author: ekfxisidF025)

**Module series coverage:** F015,F016,F025

### Enable volume adjustment display
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3002: VOLUME_POPUP_DISPLAY, bit 52, mask 01000000b -> `01`

## ekfxisid.xml — HU_NBT (CAFD 00000DED, author: ekfxisidF025)

**Module series coverage:** F015,F016,F025

### Enable daylight running lights
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: DAYDRIVING_LIGHT, bit 92, mask 00011000b -> `02`

## ekfxisid.xml — HU_NBT (CAFD 00000DED, author: ekfxisidF025)

**Module series coverage:** F015,F016,F025

### Output ringtone through speakers (iOS only)
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3003: INBAND_RINGING, bit 6, mask 10000000b -> `aktiv`

## ekfxisid.xml — HU_NBT (CAFD 00000DED, author: ekfxisidF025)

**Module series coverage:** F015,F016,F025

### Configure Sport mode 1/3
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: EFF_DYN_SPORT_CID, bit 101, mask 00010000b -> `aktiv`

## ekfxisid.xml — HU_NBT (CAFD 00000DED, author: ekfxisidF025)

**Module series coverage:** F015,F016,F025

### Configure Sport mode 2/3
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: EFF_DYN_SPORT_UNIT, bit 107, mask 00000100b -> `aktiv`

## ekfxisid.xml — HU_NBT (CAFD 00000DED, author: ekfxisidF025)

**Module series coverage:** F015,F016,F025

### Configure Sport mode 3/3
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3001: MACRO_FDS, bit 55, mask 00011000b -> `popup_and_config`

## ekfxisid.xml — HU_NBT (CAFD 00000DED, author: ekfxisidF025)

**Module series coverage:** F015,F016,F025

### Bang & Olufsen profile
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: HIGH_END_AUDIO_B_UND_W, bit 21, mask 01100000b -> `keine_insz`

## ekfxisid.xml — HU_NBT (CAFD 00000DED, author: ekfxisidF025)

**Module series coverage:** F015,F016,F025

### Enable Logic7 (S667A HiFi vehicles)
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: LOGIC7_SYMBOL, bit 22, mask 00001000b -> `aktiv`

## ekfxisid.xml — HU_NBT (CAFD 00000DED, author: ekfxisidF025)

**Module series coverage:** F015,F016,F025

### Door lock/unlock chime (anti-theft module vehicles except M5)
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: ACOUSTICAL_LOCK_CONFIRM, bit 110, mask 00000001b -> `Aktiv`

## ekfxisid.xml — HU_NBT (CAFD 00000DED, author: ekfxisidF025)

**Module series coverage:** F015,F016,F025

### Enable TPMC tire pressure temperature
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3001: RDC_SAFETY, bit 1, mask 00100000b -> `Aktiv`

## ekfxisid.xml — HU_NBT (CAFD 00000DED, author: ekfxisidF025)

**Module series coverage:** F015,F016,F025

### Change M Sport display cluster colors
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: M_VEHICLE, bit 133, mask 01000000b -> `aktiv`

## ekfxisid.xml — HU_NBT (CAFD 00000DED, author: ekfxisidF025)

**Module series coverage:** F015,F016,F025

### High-beam assistant 4/4 -->> KAFAS2 1/4, FRM 2/4, 3/4
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: HIGH_BEAM_ASSISTANT, bit 109, mask 10000000b -> `01`

## packetpilot.xml — ACSM_4C (CAFD 00000909, author: packetpilot)

**Module series coverage:** F020,F030

### Disable seat-belt chime
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: bit 15, mask 00000010b -> `00`
  * Group 3000: bit 15, mask 00000100b -> `00`

## packetpilot.xml — ACSM_4C (CAFD 00000909, author: packetpilot)

**Module series coverage:** F020,F030

### Enable seat-belt chime
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: bit 15, mask 00000010b -> `00`
  * Group 3000: bit 15, mask 00000100b -> `00`

## packetpilot.xml — FEM_01 (CAFD 00000794, author: packetpilot)

**Module series coverage:** F020,F030

### Fold/Unfold Mirrors, Ctrl Windows: Enable w/ Fob and Comfort Access, Min Delay
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3053: bit 0, mask 01000000b -> `00`
  * Group 3053: bit 0, mask 10000000b -> `00`
  * Group 3053: bit 1, mask 00000001b -> `00`
  * Group 3053: bit 1, mask 00000010b -> `00`
  * Group 3053: bit 8, mask 11111111b -> `0A`
  * Group 3053: bit 9, mask 11111111b -> `00`
  * Group 3110: bit 0, mask 10000000b -> `01`
  * Group 3110: bit 1, mask 00000001b -> `01`
  * Group 3110: bit 7, mask 00000001b -> `01`
  * Group 3110: bit 8, mask 00000001b -> `01`

## packetpilot.xml — FEM_01 (CAFD 00000794, author: packetpilot)

**Module series coverage:** F020,F030

### Fold/Unfold Mirrors, Ctrl Windows: Disable w/ Fob and Comfort Access
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 30530: bit 0, mask 01000000b -> `01`
  * Group 30530: bit 0, mask 10000000b -> `01`
  * Group 30530: bit 1, mask 00000001b -> `01`
  * Group 30530: bit 1, mask 00000010b -> `01`
  * Group 3110: bit 0, mask 10000000b -> `00`
  * Group 3110: bit 1, mask 00000001b -> `00`
  * Group 3110: bit 7, mask 00000001b -> `00`
  * Group 3110: bit 8, mask 00000001b -> `00`

## packetpilot.xml — FEM_01 (CAFD 00000794, author: packetpilot)

**Module series coverage:** F020,F030

### Rear Fog Switch: Enable [dep: switch or blank mod]
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3060: bit 7, mask 00001000b -> `01`

## packetpilot.xml — FEM_01 (CAFD 00000794, author: packetpilot)

**Module series coverage:** F020,F030

### Rear Fog Switch: Disable
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3060: bit 7, mask 00001000b -> `00`

## packetpilot.xml — FEM_01 (CAFD 00000794, author: packetpilot)

**Module series coverage:** F020,F030

### Front Fog-Like VLD: Enable Step 1 [dep: switch or blank mod, VLD]
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3060: bit 13, mask 10000000b -> `01`
  * Group 3064: bit 213, mask 11111111b -> `09`

## packetpilot.xml — FEM_01 (CAFD 00000794, author: packetpilot)

**Module series coverage:** F020,F030

### Front Fog-Like VLD: Disable Step 1
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3060: bit 13, mask 10000000b -> `00`
  * Group 3064: bit 213, mask 11111111b -> `02`

## packetpilot.xml — FEM_01 (CAFD 00000794, author: packetpilot)

**Module series coverage:** F020,F030

### Five-Flash Blinker Tap
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3060: bit 7, mask 00000111b -> `04`

## packetpilot.xml — FEM_01 (CAFD 00000794, author: packetpilot)

**Module series coverage:** F020,F030

### Brake Force Display: Disable Timeout [US/CDN]
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3060: bit 18, mask 11111111b -> `00`

## packetpilot.xml — FEM_01 (CAFD 00000794, author: packetpilot)

**Module series coverage:** F020,F030

### Fog Lights: Disable Hi-Beam Override
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3060: bit 20, mask 00100000b -> `00`

## packetpilot.xml — FEM_01 (CAFD 00000794, author: packetpilot)

**Module series coverage:** F020,F030

### Deploy Hazards upon Heavy Decel [req. manual cancel]
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3060: bit 26, mask 00000001b -> `01`

## packetpilot.xml — FEM_01 (CAFD 00000794, author: packetpilot)

**Module series coverage:** F020,F030

### Fog Lights: Bypass Position 1 Requirement
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3060: bit 29, mask 01000000b -> `01`

## packetpilot.xml — FEM_01 (CAFD 00000794, author: packetpilot)

**Module series coverage:** F020,F030

### Fog Lights: Reinstate Position 1 Requirement
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3060: bit 29, mask 01000000b -> `00`

## packetpilot.xml — FEM_01 (CAFD 00000794, author: packetpilot)

**Module series coverage:** F020,F030

### Headlight Washer: Disable
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3080: WW_SCHEINWERFERREINIGUNG, bit 8, mask 00000001b -> `nicht_aktiv`

## packetpilot.xml — FEM_01 (CAFD 00000794, author: packetpilot)

**Module series coverage:** F020,F030

### Headlight Washer: Enable
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3080: WW_SCHEINWERFERREINIGUNG, bit 8, mask 00000001b -> `aktiv`

## packetpilot.xml — FEM_01 (CAFD 00000794, author: packetpilot)

**Module series coverage:** F020,F030

### Headlight Washer NummerSpritzen: 2 squirts
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3080: WW_ANZAHL_SPRITZIMPULSE_SRA, bit 8, mask 00011000b -> `02`

## packetpilot.xml — FEM_01 (CAFD 00000794, author: packetpilot)

**Module series coverage:** F020,F030

### Headlight Washer NummerSpritzen: 3 squirts
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3080: WW_ANZAHL_SPRITZIMPULSE_SRA, bit 8, mask 00011000b -> `03`

## packetpilot.xml — FEM_01 (CAFD 00000794, author: packetpilot)

**Module series coverage:** F020,F030

### Headlight Washer: Activate Every 2 Windshield Washes
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3080: WW_ANZAHL_WASCHBET_ZUR_SRA, bit 2, mask 00011110b -> `02`

## packetpilot.xml — FEM_01 (CAFD 00000794, author: packetpilot)

**Module series coverage:** F020,F030

### Headlight Washer: Activate Every 4 Windshield Washes
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3080: WW_ANZAHL_WASCHBET_ZUR_SRA, bit 2, mask 00011110b -> `04`

## packetpilot.xml — FEM_01 (CAFD 00000794, author: packetpilot)

**Module series coverage:** F020,F030

### Headlight Washer: Activate Every 8 Windshield Washes
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3080: WW_ANZAHL_WASCHBET_ZUR_SRA, bit 2, mask 00011110b -> `08`

## packetpilot.xml — REM_01 (CAFD 000007A1, author: packetpilot)

**Module series coverage:** F020,F030

### DRL: Enable Outer and Inner Tails
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3062: bit 200, mask 00111111b -> `14`
  * Group 3062: bit 210, mask 00111111b -> `15`
  * Group 3062: bit 220, mask 00111111b -> `16`
  * Group 3062: bit 230, mask 00111111b -> `17`

## packetpilot.xml — REM_01 (CAFD 000007A1, author: packetpilot)

**Module series coverage:** F020,F030

### DRL: Enable Outer Tails Only
*Applies to:* F020,F030
*Implementation details:*
  * Group 3062: bit 200, mask 00111111b -> `14`
  * Group 3062: bit 210, mask 00111111b -> `15`
  * Group 3062: bit 220, mask 00111111b -> `00`
  * Group 3062: bit 230, mask 00111111b -> `00`

## packetpilot.xml — REM_01 (CAFD 000007A1, author: packetpilot)

**Module series coverage:** F020,F030

### DRL: Disable Tails
*Applies to:* F020,F030
*Implementation details:*
  * Group 3062: bit 200, mask 00111111b -> `00`
  * Group 3062: bit 210, mask 00111111b -> `00`
  * Group 3062: bit 220, mask 00111111b -> `00`
  * Group 3062: bit 230, mask 00111111b -> `00`

## packetpilot.xml — REM_01 (CAFD 000007A1, author: packetpilot)

**Module series coverage:** F020,F030

### Rear Fog: Enable Both Lamps [dep: switch activation in FEM_Body]
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3063: bit 40, mask 00111111b -> `1C`
  * Group 3063: bit 50, mask 00111111b -> `1D`

## packetpilot.xml — REM_01 (CAFD 000007A1, author: packetpilot)

**Module series coverage:** F020,F030

### Rear Fog: Enable Left Lamp [dep: switch activation in FEM_Body]
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3063: bit 40, mask 00111111b -> `1C`
  * Group 3063: bit 50, mask 00111111b -> `00`

## packetpilot.xml — REM_01 (CAFD 000007A1, author: packetpilot)

**Module series coverage:** F020,F030

### Rear Fog: Enable Right Lamp [dep: switch activation in FEM_Body]
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3063: bit 40, mask 00111111b -> `00`
  * Group 3063: bit 50, mask 00111111b -> `1D`

## packetpilot.xml — LHM2 (CAFD 000010BA, author: packetpilot)

**Module series coverage:** F020,F030

### Front Fog-Like VLD noGFHB: Enable Step 2a [dep: step 1 in FEM_Body, no GFHB, LED pkg]
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: bits 0-6, mask 11111111b -> `FA, FA, 00, FA, C8, C8, 00`
  * Group 3000: bits 7-13, mask 11111111b -> `FA, FA, 00, FA, C8, C8, 00`

## packetpilot.xml — LHM2 (CAFD 000010BA, author: packetpilot)

**Module series coverage:** F020,F030

### Front Fog-Like VLD noGFHB: Disable Step 2a [reco: revert Step 1 in FEM_Body, req: no GFHB]
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: bits 0-6, mask 11111111b -> `FA, FA, 00, 00, C8, C8, 00`
  * Group 3000: bits 7-13, mask 11111111b -> `FA, FA, 00, 00, C8, C8, 00`

## packetpilot.xml — LHM2 (CAFD 000010BA, author: packetpilot)

**Module series coverage:** F020,F030

### Front Fog-Like VLD w/ GFHB: Enable Step 2a [dep: step 1 in FEM_Body, GFHB, LED pkg]
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: bits 0-6, mask 11111111b -> `FA, 64, 00, FA, FA, FA, 00`
  * Group 3000: bits 7-13, mask 11111111b -> `FA, 64, 00, FA, FA, FA, 00`

## packetpilot.xml — LHM2 (CAFD 000010BA, author: packetpilot)

**Module series coverage:** F020,F030

### Front Fog-Like VLD w/ GFHB: Disable Step 2a [reco: revert Step 1 in FEM_Body, req: GFHB ]
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: bits 0-6, mask 11111111b -> `FA, 64, 00, 00, FA, FA, 00`
  * Group 3000: bits 7-13, mask 11111111b -> `FA, 64, 00, 00, FA, FA, 00`

## packetpilot.xml — LHM2 (CAFD 000016BF, author: packetpilot)

**Module series coverage:** F020,F030

### Front Fog-Like VLD noGFHB: Enable Step 2b [dep: step 1 in FEM_Body]
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: bits 0-6, mask 11111111b -> `FA, FA, 00, FA, C8, C8, 00`
  * Group 3000: bits 7-13, mask 11111111b -> `FA, FA, 00, FA, C8, C8, 00`

## packetpilot.xml — LHM2 (CAFD 000016BF, author: packetpilot)

**Module series coverage:** F020,F030

### Front Fog-Like VLD noGFHB: Disable Step 2b [reco: revert Step 1 in FEM_Body]
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: bits 0-6, mask 11111111b -> `FA, FA, 00, 00, C8, C8, 00`
  * Group 3000: bits 7-13, mask 11111111b -> `FA, FA, 00, 00, C8, C8, 00`

## packetpilot.xml — LHM2 (CAFD 000016BF, author: packetpilot)

**Module series coverage:** F020,F030

### Front Fog-Like VLD w/ GFHB: Enable Step 2b [dep: step 1 in FEM_Body, GFHB, LED pkg]
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: bits 0-6, mask 11111111b -> `FA, 64, 00, FA, FA, FA, 00`
  * Group 3000: bits 7-13, mask 11111111b -> `FA, 64, 00, FA, FA, FA, 00`

## packetpilot.xml — LHM2 (CAFD 000016BF, author: packetpilot)

**Module series coverage:** F020,F030

### Front Fog-Like VLD w/ GFHB: Disable Step 2b [reco: revert Step 1 in FEM_Body, req: GFHB ]
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: bits 0-6, mask 11111111b -> `FA, 64, 00, 00, FA, FA, 00`
  * Group 3000: bits 7-13, mask 11111111b -> `FA, 64, 00, 00, FA, FA, 00`

## packetpilot.xml — TMS_03 (CAFD 00001082, author: packetpilot)

**Module series coverage:** F020,F030

### DRL Headlamp Settings: Eyebrow Off, AngelEyes On [Drv]
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3005: bits 0-15, mask 11111111b -> `00, 03, 00, 00, 00, 04, 00, 00, 00, 04, 00, 00, 64, 24, 00, 00`

## packetpilot.xml — TMS_03 (CAFD 00001082, author: packetpilot)

**Module series coverage:** F020,F030

### DRL Headlamp Settings: Eyebrow On, AngelEyes Off [Drv]
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3005: bits 0-15, mask 11111111b -> `00, 03, 00, 00, 00, 04, 00, 00, 64, 04, 00, 00, 00, 24, 00, 00`

## packetpilot.xml — TMS_03 (CAFD 00001082, author: packetpilot)

**Module series coverage:** F020,F030

### DRL Headlamp Settings: Eyebrow AND Angel Eyes On [Drv]
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3005: bits 0-15, mask 11111111b -> `00, 03, 00, 00, 00, 04, 00, 00, 64, 04, 00, 00, 64, 24, 00, 00`

## packetpilot.xml — TMS_03 (CAFD 00001083, author: packetpilot)

**Module series coverage:** F020,F030

### DRL Headlamp Settings: Eyebrow Off, AngelEyes On [Pass]
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3005: bits 0-15, mask 11111111b -> `00, 03, 00, 00, 00, 04, 00, 00, 00, 04, 00, 00, 64, 24, 00, 00`

## packetpilot.xml — TMS_03 (CAFD 00001083, author: packetpilot)

**Module series coverage:** F020,F030

### DRL Headlamp Settings: Eyebrow On, AngelEyes Off [Pass]
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3005: bits 0-15, mask 11111111b -> `00, 03, 00, 00, 00, 04, 00, 00, 64, 04, 00, 00, 00, 24, 00, 00`

## packetpilot.xml — TMS_03 (CAFD 00001083, author: packetpilot)

**Module series coverage:** F020,F030

### DRL Headlamp Settings: Eyebrow AND Angel Eyes On [Pass]
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3005: bits 0-15, mask 11111111b -> `00, 03, 00, 00, 00, 04, 00, 00, 64, 04, 00, 00, 64, 24, 00, 00`

## packetpilot.xml — SM2 (CAFD 000000B5, author: packetpilot)

**Module series coverage:** F020,F030

### Easy Entry: Enable
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3000: EINAUSSTIEGSHILFE, bit 0, mask 00011100b -> `Modus_FA_SLV`

## packetpilot.xml — SM2 (CAFD 000000B5, author: packetpilot)

**Module series coverage:** F020,F030

### Easy Entry: Set Max Rearward Auto-Travel (mm from limit?)
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3012: EAH_SCHUTZFREIRAUM_HINTEN_SLV_PHYS, bits 4-5, mask 11111111b -> `00, 32`

## packetpilot.xml — SM2 (CAFD 000000B5, author: packetpilot)

**Module series coverage:** F020,F030

### Easy Entry: Set Desired Rearward Travel (mm?)
*Applies to:* Inherits module coverage
*Implementation details:*
  * Group 3012: EAH_VERFAHRWEG_SLV_PHYS, bits 0-1, mask 11111111b -> `00, 32`

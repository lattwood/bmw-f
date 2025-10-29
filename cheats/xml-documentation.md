# BMW F-Chassis Cheat XML Documentation

This document catalogs the coding snippets stored in the XML cheat files. For each file the BMW module (CAFD) that the coding touches is listed along with every preset and the bit or value that the preset manipulates.

## `Almaretto.xml`

**Modules touched:** BDC_01 (CAFD 000017BE, author Almaretto, series F015), IHKA_CBF (CAFD 00000092, author Almaretto, series F015,F010), IHKA2 (CAFD 000047D6, author Almaretto, series F015), IHKA_VA02 (CAFD 000016EE, author Almaretto, series F020,F020,I001), PMA_PDC (CAFD 00001AB7, author Almaretto, series F015), PMA_PDC (CAFD 0000146B, author Almaretto, series F015,I001), iCAM (CAFD 0000163C, author Almaretto, series F015), KAFAS2 (CAFD 00001148, author Almaretto, series F010,F015), HKFM (CAFD 000007C8, author Almaretto, series F001,F010,F015,F025,F030,F045), HU_NBT (CAFD 00000DED, author Almaretto), HU_CICHB (CAFD 000000F9, author Almaretto), Combbox_Media (CAFD 000005B6, author Almaretto), KOMBI (CAFD 00000069, author Almaretto, series F010,F015), KOMBI L7_MID (CAFD 000009C8, author Almaretto, series F020,F030), KOMBI FPK_I12 (CAFD 00001060, author Almaretto, series I001), KOMBI_I01_F56 (CAFD 0000141F, author Almaretto, series I001), NIVI2 (CAFD 0000004C, author Almaretto, series F010), ICMQL (CAFD 000013D8, author Almaretto, series F015), ICMQL (CAFD 0000067B, author Almaretto, series F010), ICMQL (CAFD 00000052, author Almaretto), FRM_03CT (CAFD 0000106D, author Almaretto, series F010), FRM_03CT (CAFD 0000106D, author Almaretto, series F025), FRM_O3CT (CAFD 0000012F, author Almaretto, series F010), CAS_04 (CAFD 0000000F, author Almaretto, series F010), DSC_Premium (CAFD 00000C18, author Almaretto, series F010), EMF_03TRW (CAFD 0000029B, author Almaretto, series F010), CFAS-PLX_1 (CAFD 000000B5, author Almaretto, series F010,F015,F030,F80), SZL_LWS_03 (CAFD 0000033D, author Almaretto, series F010), JBBFE (CAFD 00000014, author Almaretto, series F010), JBBF_E3_PDC (CAFD 00000018, author Almaretto, series F010), TRSVC (CAFD 00000223, author Almaretto, series F010,F030,F080), ACSM_4C (CAFD 00000909, author Almaretto, series F010,F015), ACSM_3 (CAFD 0000009C, author Almaretto, series F010), ACSM_4i (CAFD 000011AB, author Almaretto, series I001), ASD01 (CAFD 00000F9B, author Almaretto, series F010,F080), FLE_02 (CAFD 000024C3, author Almaretto, series F015), FLE_02 (CAFD 000024C3, author Almaretto, series F030), LHM2 (CAFD 000010BA, author Almaretto, series F015), LHM2 (CAFD 000010BA, author Almaretto, series F025), LHM2 (CAFD 000010BA, author Almaretto, series F030,F080), LHM2 (CAFD 000016BF, author Almaretto, series F015), LHM2 (CAFD 000016BF, author Almaretto, series F025), LHM2 (CAFD 000016BF, author Almaretto, series F030,F080), TMS_03 (CAFD 00001082, author Almaretto, series F010), TMS_03 (CAFD 00001082, author Almaretto, series F030,F080), TMS_03 (CAFD 00001083, author Almaretto, series F010), TMS_03 (CAFD 00001083, author Almaretto, series F030,F080), FEM_BODY (CAFD 00000794, author Almaretto, series F030,F080), REM_01 (CAFD 000007A1, author Almaretto, series F030), DSC (CAFD 00001A33, author Almaretto, series F080), BDC_01 (CAFD 000017BC, author Almaretto, series G011,G030), BDC_01 (CAFD 00001DF7, author Almaretto, series G011,G030), HKFM_2015 (CAFD 00002098, author Almaretto, series F015,G001,G011,G030,RR11), HKFM_2015 (CAFD 0000570E, author Almaretto, series F015,G001,G011,G030,RR11), HKFM_2015 (CAFD 00005710, author Almaretto, series F015,G001,G011,G030,RR11), IHKA_PR01 (CAFD 000022D3, author Almaretto, series G011,G030), ACSM_5 (CAFD 00001B29, author Almaretto, series G011,G030), HU_NBT_EVO (CAFD 00001EF6, author Almaretto, series F015,F030,G011), KAFAS3 (CAFD 00002089, author Almaretto, series G011), HU_MGU (CAFD 00003E52, author Almaretto, series G005, G007, G020, G015, G030, G011), SAS3 (CAFD 000042C1, author Almaretto, series G005, G007, G020, G015, G030, G011), DSC_VIP (CAFD 00003D14, author Almaretto, series G005, G007, G020, G015, G011), DSC_VIP (CAFD 00003D78, author Almaretto, series G005, G007, G020)

### BDC_01 (CAFD 000017BE) — authored by Almaretto | Series: F015

* **ENABLE  Electronic (Radio and Nav) SHUTOFF when drivers door opened**
  * Group `3020`
    * `aktiv` (start=9, mask=00000001b, comment=TCM_LOGIC_R_OFF_DOOR)

* **DISABLE Electronic (Radio and Nav) SHUTOFF when drivers door opened**
  * Group `3020`
    * `nicht_aktiv` (start=9, mask=00000001b, comment=TCM_LOGIC_R_OFF_DOOR)

* **ENABLE Door Handle LED Lights while in reverse**
  * Group `3070`
    * `aktiv` (start=128, mask=00000001b)

* **ENABLE FRONT driver/passenger window Roll Up when doors opened**
  * Group `3050`
    * `nicht_aktiv` (start=0, mask=00000001b)

* **ENABLE REAR driver/passenger window Roll Up when doors opened**
  * Group `3051`
    * `nicht_aktiv` (start=0, mask=00000001b)

* **ENABLE Open/Close windows and mirrors via keyFOB - CA (NA Cars)**
  * Group `3056`
    * `aktiv` (start=0, mask=01000000b)
    * `aktiv` (start=0, mask=10000000b)
    * `aktiv` (start=1, mask=00000100b)
    * `aktiv` (start=1, mask=00000001b)
    * `aktiv` (start=1, mask=00000010b)
  * Group `3110`
    * `aktiv` (start=0, mask=10000000b)
    * `aktiv` (start=7, mask=00000001b)

* **Remove open/close window and mirror initiation delay**
  * Group `3056`
    * `00` (start=10, mask=11111111b)

* **Unlock doors when STOP engine (Older I-Step)**
  * Group `3040`
    * `aktiv` (start=2, mask=00001000b)

* **Unlock doors when STOP engine - auto-locked (Newer I-Step)**
  * Group `3041`
    * `nur_nach_v_verriegeln` (start=40, mask=00000011b, comment=CLI_DEFAULT_UNLOCK_AFTER_END_OF_DRIVING)

* **Unlock doors when STOP engine - auto or manual lock (Newer I-Step)**
  * Group `3041`
    * `aktiv` (start=40, mask=00000011b, comment=CLI_DEFAULT_UNLOCK_AFTER_END_OF_DRIVING)

* **ENABLE Engine Start Without Holding Brake) (EXCLUDES I3)**
  * Group `3020`
    * `nicht_aktiv` (start=8, mask=00000001b, comment=TCM_STARTLOCK_BRAKE)
    * `nicht_aktiv` (start=8, mask=00010000b, comment=TCM_STARTLOCK_DRIVINGREADINESS)

* **ENABLE Front and Rear DRL (8TL)**
  * Group `3068`
    * `drl_s` (start=31, mask=00110000b)
  * Group `3064`
    * `sl_l` (start=221, mask=00111111b)
    * `sl_r` (start=234, mask=00111111b)
  * Group `3065`
    * `sl_2_l` (start=78, mask=00111111b)
    * `sl_2_r` (start=91, mask=00111111b)

* **F15 - ENABLE Variable Light Distribution (VLD)**
  * Group `3073`
    * `9C, 9C, 9C` (start=40, end=42, mask=11111111b)
    * `F015ENABLE` (start=152, mask=00000001b)

* **DISABLE Auto Start/Stop (ASS) at every startup (Comfort Mode)**
  * Group `3023`
    * `aktiv` (start=0, mask=00010000b)

* **DISABLE Auto Start/Stop (ASS) at every startup (Eco Pro Mode)**
  * Group `3023`
    * `nicht_aktiv` (start=1, mask=00001100b)

* **ENABLE Auto Start/Stop (ASS) Remembers Last Setting (ON or OFF)**
  * Group `3023`
    * `aktiv` (start=0, mask=00100000b)

* **ENABLE Reduced Rain HeadLight Sensor Sensitivity (Insensitive)**
  * Group `3130`
    * `unempfindlich` (start=5, mask=00000111b)

* **DISABLE Horn Lock Confirmation with Engine On**
  * Group `3040`
    * `nicht_aktiv` (start=0, mask=00000100b)

* **ENABLE Horn Lock Confirmation with Engine On**
  * Group `3040`
    * `aktiv` (start=0, mask=00000100b)

* **Change Number of Soft Turn Signal Blinks to 5 (Old I-STEP, Less than 3.59)**
  * Group `3068`
    * `04` (start=7, mask=00000111b, comment=See Newer Coding if F025-16-07-501)

* **Change Number of Soft Turn Signal Blinks to 5 (New I-STEP, Greater then 3.59.x)**
  * Group `3069`
    * `02` (start=215, mask=00011000b, comment=Firmware F025-16-07-501, 00 = 1, 01 = 3, 02 =5)

* **ENABLE Increased Passenger Mirror Tilt (Curb View) in Reverse**
  * Group `3110`
    * `5A` (start=1, mask=11111111b)

* **Removes Trunk Open Delay (Instant) via KeyFOB**
  * Group `30D0`
    * `wert_00` (start=18, mask=11111111b)

* **ENABLE Increased Side Mirror Dimming (Tinted Windows)**
  * Group `3120`
    * `39` (start=23, mask=11111100b, comment=left mirror)
    * `39` (start=30, mask=11111100b, comment=right mirror)

* **F015 - ENABLE EU Brake Force Display (BFD) Light Behavior (Blink)**
  * Group `3068`
    * `02` (start=16, mask=00000011b, comment=Default USA = glow brighter and wider)
  * Group `3064`
    * `18` (start=156, mask=00111111b, comment=MAPPING_BRAKEFORCED_1_L_OUTPUT)
    * `19` (start=169, mask=00111111b, comment=MAPPING_BRAKEFORCED_1_R_OUTPUT)
  * Group `3065`
    * `14` (start=52, mask=00111111b, comment=MAPPING_BRAKEFORCED_2_L_OUTPUT)
    * `15` (start=65, mask=00111111b, comment=MAPPING_BRAKEFORCED_2_R_OUTPUT)

* **F015 - ENABLE EU Brake Force Display (BFD) (Additional Settings) (TESTING)**
  * Group `3064`
    * `01` (start=158, mask=11100000b, comment=MAPPING_BRAKEFORCED_1_L_PRIORITY)
    * `64` (start=159, mask=11111111b, comment=MAPPING_BRAKEFORCED_1_L_PWM_1_BFD)
    * `00` (start=162, mask=11111111b, comment=MAPPING_BRAKEFORCED_1_L_PWM_4)
    * `00` (start=165, mask=00011111b, comment=MAPPING_BRAKEFORCED_1_L_DEPENDENCY_FUNC)
    * `01` (start=171, mask=11100000b, comment=MAPPING_BRAKEFORCED_1_R_PRIORITY)
    * `64` (start=172, mask=11111111b, comment=MAPPING_BRAKEFORCED_1_R_PWM_1_BFD)
    * `00` (start=175, mask=11111111b, comment=MAPPING_BRAKEFORCED_1_R_PWM_4)
    * `00` (start=178, mask=00011111b, comment=MAPPING_BRAKEFORCED_1_R_DEPENDENCY_FUNC)
  * Group `3065`
    * `01` (start=54, mask=11100000b, comment=MAPPING_BRAKEFORCED_2_L_PRIORITY)
    * `64` (start=55, mask=11111111b, comment=MAPPING_BRAKEFORCED_2_L_PWM_1_BFD)
    * `00` (start=56, mask=11111111b, comment=MAPPING_BRAKEFORCED_2_L_PWM_2_ESS_1)
    * `00` (start=57, mask=11111111b, comment=MAPPING_BRAKEFORCED_2_L_PWM_3_ESS_2)
    * `64` (start=58, mask=11111111b, comment=MAPPING_BRAKEFORCED_2_L_PWM_4)
    * `01` (start=67, mask=11100000b, comment=MAPPING_BRAKEFORCED_2_R_PRIORITY)
    * `64` (start=68, mask=11111111b, comment=MAPPING_BRAKEFORCED_2_R_PWM_1_BFD)
    * `00` (start=69, mask=11111111b, comment=MAPPING_BRAKEFORCED_2_R_PWM_2_ESS_1)
    * `00` (start=70, mask=00111111b, comment=MAPPING_BRAKEFORCED_2_R_PWM_3_ESS_2)
    * `64` (start=71, mask=00011111b, comment=MAPPING_BRAKEFORCED_2_R_PWM_4)

* **Change Behavior of keyFOB 3RD Button (Short Press = No Action)**
  * Group `30D0`
    * `00` (start=13, mask=00001111b, comment=RC_DEFAULT_IDG_3RD_BUTTON_SHORT)

* **Change Behavior of keyFOB 3RD Button (Short Press = Open Trunk)**
  * Group `30D0`
    * `02` (start=13, mask=00001111b, comment=RC_DEFAULT_IDG_3RD_BUTTON_SHORT)

* **Change Behavior of keyFOB 3RD Button (Short Press = Panic Alarm)**
  * Group `30D0`
    * `03` (start=13, mask=00001111b, comment=RC_DEFAULT_IDG_3RD_BUTTON_SHORT)

* **Change Behavior of keyFOB 3RD Button (Short Press = Follow-Me-Home)**
  * Group `30D0`
    * `04` (start=13, mask=00001111b, comment=RC_DEFAULT_IDG_3RD_BUTTON_SHORT)

* **Change Behavior of keyFOB 3RD Button (Short Press = Open Frunk - Front Boot)**
  * Group `30D0`
    * `05` (start=13, mask=00001111b, comment=RC_DEFAULT_IDG_3RD_BUTTON_SHORT)

* **Change Behavior of keyFOB 3RD Button (Short Press = Auxillary Cooling)**
  * Group `30D0`
    * `07` (start=13, mask=00001111b, comment=RC_DEFAULT_IDG_3RD_BUTTON_SHORT)

* **Change Behavior of keyFOB 3RD Button (Medium Press = No Action)**
  * Group `30D0`
    * `00` (start=13, mask=11110000b, comment=RC_DEFAULT_IDG_3RD_BUTTON_MID)

* **Change Behavior of keyFOB 3RD Button (Medium Press = Open Trunk)**
  * Group `30D0`
    * `02` (start=13, mask=11110000b, comment=RC_DEFAULT_IDG_3RD_BUTTON_MID)

* **Change Behavior of keyFOB 3RD Button (Medium Press = Panic Alarm)**
  * Group `30D0`
    * `03` (start=13, mask=11110000b, comment=RC_DEFAULT_IDG_3RD_BUTTON_MID)

* **Change Behavior of keyFOB 3RD Button (Medium Press = Follow-Me-Home)**
  * Group `30D0`
    * `04` (start=13, mask=11110000b, comment=RC_DEFAULT_IDG_3RD_BUTTON_MID)

* **Change Behavior of keyFOB 3RD Button (Medium Press = Open Frunk - Front Boot)**
  * Group `30D0`
    * `05` (start=13, mask=11110000b, comment=RC_DEFAULT_IDG_3RD_BUTTON_MID)

* **Change Behavior of keyFOB 3RD Button (Medium Press = Auxillary Cooling)**
  * Group `30D0`
    * `07` (start=13, mask=11110000b, comment=RC_DEFAULT_IDG_3RD_BUTTON_MID)

* **Change Behavior of keyFOB 3RD Button (Long Press = No Action)**
  * Group `30D0`
    * `00` (start=14, mask=00001111b, comment=RC_DEFAULT_IDG_3RD_BUTTON_LONG)

* **Change Behavior of keyFOB 3RD Button (Long Press = Open Trunk)**
  * Group `30D0`
    * `02` (start=14, mask=00001111b, comment=RC_DEFAULT_IDG_3RD_BUTTON_LONG)

* **Change Behavior of keyFOB 3RD Button (Long Press = Panic Alarm)**
  * Group `30D0`
    * `03` (start=14, mask=00001111b, comment=RC_DEFAULT_IDG_3RD_BUTTON_LONG)

* **Change Behavior of keyFOB 3RD Button (Long Press = Follow-Me-Home)**
  * Group `30D0`
    * `04` (start=14, mask=00001111b, comment=RC_DEFAULT_IDG_3RD_BUTTON_LONG)

* **Change Behavior of keyFOB 3RD Button (Long Press = Open Frunk - Front Boot)**
  * Group `30D0`
    * `05` (start=14, mask=00001111b, comment=RC_DEFAULT_IDG_3RD_BUTTON_LONG)

* **Change Behavior of keyFOB 3RD Button (Long Press = Auxillary Cooling)**
  * Group `30D0`
    * `07` (start=14, mask=00001111b, comment=RC_DEFAULT_IDG_3RD_BUTTON_LONG)

* **Change Behavior of keyFOB 4TH Button (Short Press = No Action)**
  * Group `30D0`
    * `00` (start=14, mask=11110000b, comment=RC_DEFAULT_IDG_4TH_BUTTON_SHORT)

* **Change Behavior of keyFOB 4TH Button (Short Press = Open Trunk)**
  * Group `30D0`
    * `02` (start=14, mask=11110000b, comment=RC_DEFAULT_IDG_4TH_BUTTON_SHORT)

* **Change Behavior of keyFOB 4TH Button (Short Press = Panic Alarm)**
  * Group `30D0`
    * `03` (start=14, mask=11110000b, comment=RC_DEFAULT_IDG_4TH_BUTTON_SHORT)

* **Change Behavior of keyFOB 4TH Button (Short Press = Follow-Me-Home)**
  * Group `30D0`
    * `04` (start=14, mask=11110000b, comment=RC_DEFAULT_IDG_4TH_BUTTON_SHORT)

* **Change Behavior of keyFOB 4TH Button (Short Press = Open Frunk - Front Boot)**
  * Group `30D0`
    * `05` (start=14, mask=11110000b, comment=RC_DEFAULT_IDG_4TH_BUTTON_SHORT)

* **Change Behavior of keyFOB 4TH Button (Short Press = Auxillary Cooling)**
  * Group `30D0`
    * `07` (start=14, mask=11110000b, comment=RC_DEFAULT_IDG_4TH_BUTTON_SHORT)

* **Change Behavior of keyFOB 4TH Button (Medium Press = No Action)**
  * Group `30D0`
    * `00` (start=15, mask=00001111b, comment=RC_DEFAULT_IDG_4TH_BUTTON_MID)

* **Change Behavior of keyFOB 4TH Button (Medium Press = Open Trunk)**
  * Group `30D0`
    * `02` (start=15, mask=00001111b, comment=RC_DEFAULT_IDG_4TH_BUTTON_MID)

* **Change Behavior of keyFOB 4TH Button (Medium Press = Panic Alarm)**
  * Group `30D0`
    * `03` (start=15, mask=00001111b, comment=RC_DEFAULT_IDG_4TH_BUTTON_MID)

* **Change Behavior of keyFOB 4TH Button (Medium Press = Follow-Me-Home)**
  * Group `30D0`
    * `04` (start=15, mask=00001111b, comment=RC_DEFAULT_IDG_4TH_BUTTON_MID)

* **Change Behavior of keyFOB 4TH Button (Medium Press = Open Frunk - Front Boot)**
  * Group `30D0`
    * `05` (start=15, mask=00001111b, comment=RC_DEFAULT_IDG_4TH_BUTTON_MID)

* **Change Behavior of keyFOB 4TH Button (Medium Press = Auxillary Cooling)**
  * Group `30D0`
    * `07` (start=15, mask=00001111b, comment=RC_DEFAULT_IDG_4TH_BUTTON_MID)

* **Change Behavior of keyFOB 4TH Button (Long Press = No Action)**
  * Group `30D0`
    * `00` (start=15, mask=11110000b, comment=RC_DEFAULT_IDG_4TH_BUTTON_LONG)

* **Change Behavior of keyFOB 4TH Button (Long Press = Open Trunk)**
  * Group `30D0`
    * `02` (start=15, mask=11110000b, comment=RC_DEFAULT_IDG_4TH_BUTTON_LONG)

* **Change Behavior of keyFOB 4TH Button (Long Press = Panic Alarm)**
  * Group `30D0`
    * `03` (start=15, mask=11110000b, comment=RC_DEFAULT_IDG_4TH_BUTTON_LONG)

* **Change Behavior of keyFOB 4TH Button (Long Press = Follow-Me-Home)**
  * Group `30D0`
    * `04` (start=15, mask=11110000b, comment=RC_DEFAULT_IDG_4TH_BUTTON_LONG)

* **Change Behavior of keyFOB 4TH Button (Long Press = Open Frunk - Front Boot)**
  * Group `30D0`
    * `05` (start=15, mask=11110000b, comment=RC_DEFAULT_IDG_4TH_BUTTON_LONG)

* **Change Behavior of keyFOB 4TH Button (Long Press = Auxillary Cooling)**
  * Group `30D0`
    * `07` (start=15, mask=11110000b, comment=RC_DEFAULT_IDG_4TH_BUTTON_LONG)

* **ENABLE Ambiance Lighting controlled independent from Dimmer Switch**
  * Group `3070`
    * `nicht_aktiv` (start=135, mask=10000000b, comment=AMBIENTE_NACHFUEHRUNG)

* **DISABLE Ambiance Lighting controlled independent from Dimmer Switch**
  * Group `3070`
    * `01` (start=135, mask=10000000b, comment=AMBIENTE_NACHFUEHRUNG)

* **Turn on Fog Lights with Welcome Lights - SOFT ON**
  * Group `3063`
    * `01` (start=66, mask=11111111b, comment=MAPPING_NEBELSCHW_L_PART_OF)
    * `01` (start=79, mask=11111111b, comment=MAPPING_NEBELSCHW_R_PART_OF)

* **Turn on Fog Lights with Follow-Me-Home, or Alarm - HARD ON**
  * Group `3063`
    * `10` (start=66, mask=11111111b, comment=MAPPING_NEBELSCHW_L_PART_OF)
    * `10` (start=79, mask=11111111b, comment=MAPPING_NEBELSCHW_R_PART_OF)

* **ENABLE Heated Steering Wheel Instrument Cluster Status**
  * Group `3140`
    * `01` (start=18, mask=01000000b, comment=LHZ_CCM)

* **ENABLE DARK REAR WINDOW - MIRROR DIMMING**
  * Group `3120`
    * `01` (start=3, mask=00000110b, comment=ISP_HECKSCHEIBE)

* **ENABLE LIGHT REAR WINDOW - MIRROR DIMMING**
  * Group `3120`
    * `00` (start=3, mask=00000110b, comment=ISP_HECKSCHEIBE)

### IHKA_CBF (CAFD 00000092) — authored by Almaretto | Series: F015,F010

* **ENABLE HVAC memory - A/C stay OFF if OFF at vehicle shutdown**
  * Group `3000`
    * `aktiv` (start=5, mask=00010000b)

* **ENABLE Air Re-Circulation memory - Remembers shutdown Setting**
  * Group `3000`
    * `aktiv` (start=0, mask=00000100b)

* **DISABLE A/C from turning ON if Auto Button is pressed**
  * Group `3000`
    * `aktiv` (start=5, mask=00001000b)

### IHKA2 (CAFD 000047D6) — authored by Almaretto | Series: F015

* **ENABLE HVAC memory - A/C stay OFF if OFF at vehicle shutdown**
  * Group `3000`
    * `aktiv` (start=5, mask=00010000b)

* **ENABLE Air Re-Circulation memory - Remembers shutdown Setting**
  * Group `3000`
    * `aktiv` (start=0, mask=00000100b)

* **DISABLE A/C from turning ON if Auto Button is pressed**
  * Group `3000`
    * `aktiv` (start=5, mask=00001000b)

### IHKA_VA02 (CAFD 000016EE) — authored by Almaretto | Series: F020,F020,I001

* **ENABLE HVAC memory - A/C stay OFF if OFF at vehicle shutdown**
  * Group `3003`
    * `aktiv` (start=0, mask=00000010b, comment=MEMORY_OFF)

* **ENABLE Air Re-Circulation memory - Remembers shutdown Setting**
  * Group `3003`
    * `aktiv` (start=0, mask=00000001b, comment=MEMORY_UMLUFT)

* **DISABLE A/C from turning ON if Auto Button is pressed**
  * Group `3003`
    * `aktiv` (start=0, mask=00000100b)

### PMA_PDC (CAFD 00001AB7) — authored by Almaretto | Series: F015

* **ENABLE Top/Rearview Cameras at ALL speeds. See iCAM for Sideview**
  * Group `300B`
    * `FF` (start=8, mask=11111111b, comment=speed when auto disables top view)
    * `FF` (start=9, mask=11111111b, comment=speed when auto disables rear view)
    * `FF` (start=10, mask=11111111b, comment=distance when auto disables top view)
    * `FF` (start=11, mask=11111111b, comment=distance when auto disables rear view)

### PMA_PDC (CAFD 0000146B) — authored by Almaretto | Series: F015,I001

* **ENABLE Top/Rear Camera at All Speeds. Part 1 of 2. See icam for Side**
  * Group `300D`
    * `FF` (start=8, mask=11111111b, comment=max speed to disables top camera view)
    * `FF` (start=9, mask=11111111b, comment=max speed to disables rear camera view)
    * `FF` (start=10, mask=11111111b, comment=max distance to disables top camera view)
    * `FF` (start=11, mask=11111111b, comment=max distance to disables rear camera view)

### iCAM (CAFD 0000163C) — authored by Almaretto | Series: F015

* **ENABLE Sideview Cameras at ALL speeds**
  * Group `3006`
    * `FF` (start=1, mask=11111111b, comment=Activate SV at any speed - part 1)
    * `FF` (start=2, mask=11111111b, comment=Activate SV at any speed - part 2)

### KAFAS2 (CAFD 00001148) — authored by Almaretto | Series: F010,F015

* **ENABLE Grass/Roadside Edge detection to Lane Departure**
  * Group `3020`
    * `detection_for_grass_edge_and_curb_stone` (start=2, mask=00000011b)

* **ENABLE EU SLI sign (White circle with Red outline)**
  * Group `3010`
    * `ECE_white` (start=1, mask=01111000b)

* **ENABLE HUD Distance Info (Part 3 of 3. See KOMBI and KAFAS2)**
  * Group `3060`
    * `IBRAKE_STAT_on_F010` (start=1, mask=00000010b, comment=werte=01)
    * `F010` (start=1, mask=00000100b, comment=werte=01)
    * `01` (start=1, mask=00011000b, comment=werte=01)

* **DISABLE HUD Distance Info (Part 3 of 3. See KOMBI and KAFAS2)**
  * Group `3060`
    * `00` (start=1, mask=00000010b, comment=SEND_STATUS_IBRAKE)
    * `01` (start=1, mask=00000100b, comment=SEND_PARAM_IBRAKE)
    * `00` (start=1, mask=00011000b, comment=DISPLAY_HEADWAY_DISTANCE)

* **ENABLE HUD Do Not Pass/Pass with care. Part 2 of 2. See KOMBI**
  * Group `3010`
    * `01` (start=1, mask=00000010b, comment=NPI_ON_OFF)

### HKFM (CAFD 000007C8) — authored by Almaretto | Series: F001,F010,F015,F025,F030,F045

* **ENABLE Trunk Close via keyFOB/Footwell button (NA vehicles)**
  * Group `3010`
    * `aktiv` (start=0, mask=00001000b)
    * `aktiv` (start=2, mask=00000100b)
    * `aktiv` (start=2, mask=00001000b)

### HU_NBT (CAFD 00000DED) — authored by Almaretto

* **ENABLE Call Log Timestamp**
  * Group `3003`
    * `aktiv` (start=1, mask=01000000b)

* **ENABLE Entire text (SMS) message display on iDrive**
  * Group `3000`
    * `07` (start=34, mask=00011100b, comment=MYINFO_DRIVING_TEXT_LENGTH)
    * `07` (start=34, mask=11100000b, comment=AKD_DRIVING_TEXT_LENGTH)
    * `07` (start=35, mask=00000111b, comment=BMWINFO_DRIVING_TEXT_LENGTH)
  * Group `3003`
    * `07` (start=11, mask=00000111b, comment=PIM_DRIVING_TEXT_LENGTH)

* **ENABLE HUD Turnsignal. Part 1 of 2 - See KOMBI (Excludes 6WB DKOMBI)**
  * Group `3001`
    * `aktiv` (start=55, mask=10000000b)

* **DISABLE Lock/Unlock Sound Confirm Checkbox With alarm only**
  * Group `3000`
    * `nicht_aktiv` (start=110, mask=00000001b)

* **ENABLE Lock/Unlock Sound Confirm Checkbox With alarm only**
  * Group `3000`
    * `aktiv` (start=110, mask=00000001b)

* **ENABLE Sports Displays. Part 1 of 2. See KOMBI**
  * Group `3000`
    * `aktiv` (start=101, mask=00010000b)
    * `aktiv` (start=107, mask=00000100b)

* **ENABLE AM Radio on Hybrid Vehicles (F15-40e/I012/I001)**
  * Group `3002`
    * `aktiv` (start=52, mask=00001000b, comment=RADIO_BAND_KW)

* **ENABLE British Voice on Navigation**
  * Group `3000`
    * `master` (start=139, mask=00001100b)
    * `nicht_aktiv` (start=139, mask=00110000b)
    * `english_uk` (start=75, mask=11111111b)
    * `nicht_aktiv` (start=21, mask=00000001b)

* **ENABLE HUD Distance Info (Part 1 of 3 - See KOMBI and KAFAS2)**
  * Group `3000`
    * `aktiv` (start=97, mask=00001000b)

* **Changes Default Time settings to 24H**
  * Group `3004`
    * `24h` (start=8, mask=00010000b)

* **ENABLE HUD Entertainment Details. Part 2 of 2. See KOMBI**
  * Group `3000`
    * `aktiv` (start=21, mask=10000000b, comment=hud_entertainmentlist)

* **ENABLE Additional Menu Item (Current Position) in Navigation System**
  * Group `3000`
    * `aktiv` (start=96, mask=10000000b)

* **DISABLE Active Sound Design (M5 only). Part 2 of 2. See ASD**
  * Group `3000`
    * `aktiv` (start=57, mask=00001000b, comment=ASD_SOUND_OFF)

* **ENABLE Active Sound Design Configuration Menu (M5 only). Part 2 of 2. See ASD**
  * Group `3000`
    * `aktiv` (start=105, mask=00000001b, comment=ASD_CONFIGURATION)
    * `aktiv` (start=105, mask=00010000b, comment=ASD_SOUND_4)

* **ENABLE Volume to be retained up to 50% rather than startup at 25%**
  * Group `3002`
    * `32` (start=3, mask=11111111b, comment=VOL_MAX_ON)

* **ENABLE 'Route Info' (Turn-by-Turn list of route)**
  * Group `3000`
    * `aktiv` (start=59, mask=00100000b, comment=NAVI_ROAD_PREVIEW)

* **Removes Speedlock for Office/Service Messages**
  * Group `3000`
    * `00` (start=35, mask=00111000b, comment=SERVICES_MESSAGES_SPEEDLOCK_CONDITION)
    * `00` (start=56, mask=00001110b, comment=OFFICE_MESSAGES_SPEEDLOCK_CONDITION)

* **ENABLE Owners Manual in Motion (Removes Speedlock)**
  * Group `3000`
    * `nicht_aktiv` (start=0, mask=00100000b, comment=SL06_IBA_1)
    * `nicht_aktiv` (start=0, mask=01000000b, comment=SL07_IBA_2)
    * `nicht_aktiv` (start=2, mask=00010000b, comment=SL21_IBA_3)

* **ENABLE Album Cover Scale to Full-Size**
  * Group `3000`
    * `aktiv` (start=14, mask=00100000b, comment=ENT_MC_COVER_SCALE)

* **DISABLE Bluetooth Device Pairing Speedlock**
  * Group `3000`
    * `nicht_aktiv` (start=1, mask=10000000b, comment=SL16_ADD_CEDEVICE)

* **ENABLE Real-Time Traffic Info**
  * Group `3000`
    * `aktiv` (start=59, mask=00010000b, comment=NAVI_TRAFFIC_INFO_MAP)
  * Group `3002`
    * `aktiv` (start=23, mask=00000100b, comment=TI_CA_TMC)
    * `aktiv` (start=24, mask=00000010b, comment=TI_VINFO)
    * `aktiv` (start=23, mask=00100000b, comment=TI_TMC_REGIONAL)
    * `aktiv` (start=23, mask=01000000b, comment=TI_FALLBACK_DISABLED)

* **ENABLE Rear Camera Zoom -Trailer Mode-**
  * Group `3001`
    * `aktiv` (start=54, mask=00000001b, comment=MACRO_TRAILER_COUPLING)

* **ENABLE Hold-Mode for Range Extender (I001/1012)**
  * Group `3000`
    * `rex` (start=12, mask=00001100b, comment=EV_MENU_AVAILABLE)

* **ENABLE Compass**
  * Group `3000`
    * `aktiv` (start=5, mask=00000001b, comment=COMPASS)

* **ENABLE Eco Pro Display info in KOMBI**
  * Group `3000`
    * `aktiv` (start=6, mask=10000000b, comment=ECO_INFO_DISPLAY)

* **ENABLE Bookmark of current playback position**
  * Group `3000`
    * `aktiv` (start=14, mask=00000100b, comment=ENT_MC_SONG_BOOKMARK)

* **ENABLE Gracenote DB Installed AND Lookup via USB and PC**
  * Group `3000`
    * `aktiv` (start=14, mask=01000000b, comment=ENT_GRACENOTE_INSTALLED)
    * `aktiv` (start=15, mask=00000010b, comment=ENT_GRACENOTE_USB)

* **ENABLE Traffic Info Category**
  * Group `3000`
    * `aktiv` (start=16, mask=00000010b, comment=TRAFFIC_CATEGORIES)

* **ENABLE Follow-Me-Home Key Setting**
  * Group `3000`
    * `aktiv` (start=26, mask=00001000b, comment=KEY_CONF_COMFORT_HOMELIGHT)

* **ENABLE NAVI Map Arrow View**
  * Group `3000`
    * `aktiv` (start=62, mask=00000100b, comment=NAVI_MAP_ARROWVIEW)

* **ENABLE NAVI SPLIT AND FULL Guiding Popup**
  * Group `3000`
    * `aktiv` (start=62, mask=00001000b, comment=NAVI_SPLIT_GUIDINGPOPUP)
    * `aktiv` (start=62, mask=00010000b, comment=NAVI_FULL_GUIDINGPOPUP)

* **ENABLE IPhone Ringtone**
  * Group `3003`
    * `01` (start=6, mask=10000000b, comment=INBAND_RINGING)

### HU_CICHB (CAFD 000000F9) — authored by Almaretto

* **ENABLE Weather Band Radio**
  * Group `3002`
    * `aktiv` (start=2, mask=00001000b, comment=RADIO_WEATHERBAND)

* **High-Beam Assistant – Auto-On**
  * Group `3000`
    * `aktiv` (start=0, mask=00000010b, comment=HIGH_BEAM_ASSISTANT)

* **ENABLE Cell Phone Ringer (Iphone Only)**
  * Group `3003`
    * `aktiv` (start=6, mask=10000000b, comment=INBAND_RINGING)

* **ENABLE Sports Displays. Part 1 of 2. See KOMBI**
  * Group `3000`
    * `aktiv` (start=47, mask=00010000b, comment=EFF_DYN_SPORT_CID)
    * `aktiv` (start=61, mask=00000100b, comment=EFF_DYN_SPORT_UNIT)
    * `popup_and_config` (start=7, mask=00110000b, comment=MACRO_FDS)

* **ENABLE Turn Signals in HUD. Part 1 of 2. See KOMBI**
  * Group `3000`
    * `aktiv` (start=22, mask=00001000b, comment=HUD_TURNSIGNAL)

* **ENABLE Video in Motion**
  * Group `3000`
    * `nicht_aktiv` (start=8, mask=01000000b, comment=VIDEO_NUR_MIT_HANDBREMSE)
    * `FF` (start=23, mask=11111111b, comment=SPEEDLOCK_X_KMH_MIN)
    * `FF` (start=24, mask=11111111b, comment=SPEEDLOCK_X_KMH_MAX)

* **ENABLE Full Text Lines in Office While Driving**
  * Group `3003`
    * `whole_text` (start=19, mask=00000111b, comment=PIM_DRIVING_TEXT_LENGTH)

* **DISABLE Audible Chirp/Beep When Locking Car**
  * Group `3000`
    * `nicht_aktiv` (start=8, mask=00100000b, comment=ACOUSTICAL_LOCK_CONFIRM)

* **ENABLE Audible Chirp/Beep When Locking Car**
  * Group `3000`
    * `aktiv` (start=8, mask=00100000b, comment=ACOUSTICAL_LOCK_CONFIRM)

* **Add Temperature and PSI to tire monitor screen**
  * Group `3001`
    * `aktiv` (start=20, mask=01000000b, comment=RDC_SAFETY)

* **DISABLE Legal Disclaimers**
  * Group `3001`
    * `kein_ld` (start=27, mask=11111111b, comment=LEGAL_DISCLAIMER_TIME)
    * `kein_ld` (start=28, mask=11111111b, comment=MACRO_CAM_LEGALDISCLAIMER)
    * `kein_ld` (start=29, mask=11111111b, comment=MACRO_NVICAM_LDISCLAIMER)

* **ENABLE volume to be retained up to 100% rather than startup at 25%**
  * Group `3002`
    * `32` (start=23, mask=11111111b, comment=VOL_MAX_ON)

* **ENABLE Real-Time Traffic Info**
  * Group `3000`
    * `aktiv` (start=6, mask=00010000b, comment=NAVI_TRAFFIC_INFO_MAP)
  * Group `3002`
    * `aktiv` (start=13, mask=00000010b, comment=TI_CA_TMC)
    * `aktiv` (start=14, mask=00000100b, comment=TI_VINFO)
    * `aktiv` (start=13, mask=00010000b, comment=TI_TMC_REGIONAL)
    * `aktiv` (start=13, mask=00100000b, comment=TI_FALLBACK_DISABLED)

* **ENABLE Rear Camera Zoom -Trailer Mode-**
  * Group `3001`
    * `aktiv` (start=23, mask=00000001b, comment=MACRO_TRAILER_COUPLING)

### Combbox_Media (CAFD 000005B6) — authored by Almaretto

* **ENABLE Iphone Ringtone over vehicle speakers**
  * Group `3001`
    * `aktiv` (start=1, mask=10000000b, comment=INBAND_RINGING)

* **Max amount of messages/addresses stored in vehicle, max 50 (HU_CIC only)**
  * Group `3006`
    * `wert_50` (start=1, mask=00111111b, comment=MY_INFO_SUPPORTED_POIS)

* **ENABLE Basic Voice Recognition**
  * Group `3000`
    * `aktiv` (start=3, mask=00000100b, comment=SVS_EIN_AUS)

### KOMBI (CAFD 00000069) — authored by Almaretto | Series: F010,F015

* **ENABLE Sports Displays (ft lb and hp). Part 2 of 2. See HU_NBT**
  * Group `3008`
    * `lb_ft` (start=8, mask=11110000b)
    * `PS` (start=9, mask=00001111b)

* **ENABLE HUD Turnsignal. Part 2 of 2. See HU_NBT (Excludes 6WB)**
  * Group `3008`
    * `aktiv` (start=5, mask=00000001b)
  * Group `3000`
    * `aktiv` (start=42, mask=00100000b)

* **DISABLE 1st fuel warning at 50 miles**
  * Group `3000`
    * `inaktiv` (start=49, mask=11111111b)

* **ENABLE Digital Speed in MPH (New BC Option)**
  * Group `3000`
    * `aktiv` (start=1, mask=00000010b)

* **ENABLE Efficient Dynamics Graph Direction (Left to Right)**
  * Group `3003`
    * `nicht_aktiv` (start=3, mask=00100000b, comment=On the Left)

* **ENABLE Efficient Dynamics Graph Direction (Right to Left)**
  * Group `3003`
    * `aktiv` (start=3, mask=00100000b, comment=On the Right)

* **ENABLE Daytime Instrument Cluster at Night (Stays White)**
  * Group `3007`
    * `FF` (start=10, mask=11111111b, comment=Does not work on LCI's)

* **ENABLE Nighttime Instrument Cluster at Day (Stays Orange)**
  * Group `3007`
    * `FF` (start=11, mask=11111111b, comment=Does not work on LCI's)

* **ENABLE Orange Decorative Lines on Instrument Cluster**
  * Group `3000`
    * `orange` (start=41, mask=00000010b)

* **ENABLE Grey Decorative Lines on Instrument Cluster**
  * Group `3000`
    * `grau` (start=41, mask=00000010b)

* **DISABLE Trip Computer Auto Reset**
  * Group `3000`
    * `FF` (start=44, mask=11111111b, comment=BC_AUTORESET_ZEIT)

* **ENABLE Trip Computer Auto Reset (0 Hours)**
  * Group `3000`
    * `00` (start=44, mask=11111111b, comment=BC_AUTORESET_ZEIT)

* **ENABLE HUD Do Not Pass/Pass with care. Part 1 of 2. See KAFAS**
  * Group `3000`
    * `sli_gen_2_npi` (start=13, mask=00110000b, comment=SPEED_LIMIT_GENERATION)
    * `aktiv` (start=45, mask=00100000b, comment=HUD_NPI_ENABLE)

* **ENABLE HUD Distance Info (Part 2 of 3. See HU_NBT and KAFAS2)**
  * Group `3000`
    * `aktiv` (start=1, mask=00000001b)
  * Group `3008`
    * `aktiv` (start=6, mask=00100000b)

* **Activate LIM Function in North American Cars (Part 1 of 2. See ICMQL)**
  * Group `3003`
    * `aktiv` (start=3, mask=00000001b)

* **ENABLE HUD Entertainment Details. Part 1 of 2. See HU_NBT**
  * Group `3000`
    * `aktiv` (start=41, mask=00001000b)

* **ENABLE HUD Telephone Details**
  * Group `3000`
    * `aktiv` (start=41, mask=00010000b)
    * `aktiv` (start=41, mask=00100000b)

* **ENABLE GPS Sync For Clock**
  * Group `3000`
    * `aktiv` (start=1, mask=10000000b)

* **ENABLE RED/WHITE Navigation Graphics in the Instrument Cluster**
  * Group `3000`
    * `neue_farbtabelle` (start=40, mask=00100000b)

* **ENABLE ALL WHITE Change of the Navigation Graphics in the Instrument Cluster**
  * Group `3000`
    * `alte_farbtabelle` (start=40, mask=00100000b)

* **DISABLE Auto Start Stop notification in Cluster**
  * Group `3000`
    * `nicht_aktiv` (start=41, mask=10000000b)

* **ENABLE Auto Start Stop notification in Cluster**
  * Group `3000`
    * `aktiv` (start=41, mask=10000000b)

* **ENABLE Night Vision with Background Pedestrian Detection. Part 1 of 2. See NIVI**
  * Group `3003`
    * `aktiv` (start=4, mask=00000001b, comment=FGS_NIVI_KI_ENABLE)

### KOMBI L7_MID (CAFD 000009C8) — authored by Almaretto | Series: F020,F030

* **Trip Computer Auto Reset (Never)**
  * Group `3000`
    * `FF` (start=44, mask=11111111b, comment=BC_AUTORESET_ZEIT)

* **Trip Computer Auto Reset (0 Hours)**
  * Group `3000`
    * `00` (start=44, mask=11111111b, comment=BC_AUTORESET_ZEIT)

* **DISABLE Digital Speed Display in Cluster**
  * Group `3000`
    * `nicht_aktiv` (start=1, mask=00000010b, comment=BC_DIGITAL_V)

* **ENABLE Digital Speed Display in Cluster**
  * Group `3000`
    * `aktiv` (start=1, mask=00000010b, comment=BC_DIGITAL_V)

* **ENABLE Speed Correction**
  * Group `3000`
    * `Aktiv` (start=1, mask=01000000b)

* **DISABLE Speed Correction**
  * Group `3000`
    * `nicht_aktiv` (start=1, mask=01000000b)

* **DISABLE Auto Start Stop notificaiton in Cluster**
  * Group `3003`
    * `nicht_aktiv` (start=6, mask=00001000b)

* **ENABLE Day White Instrument Cluster at night**
  * Group `3007`
    * `FF` (start=10, mask=11111111b)

* **ENABLE LIM Function. Part 1 of 2. See ICM**
  * Group `3003`
    * `aktiv` (start=3, mask=00000001b)

* **Changes M3/M4 Instrument Cluster Startup Logo to GTS**
  * Group `3000`
    * `0C` (start=0, mask=11110000b)

* **ENABLE Night Vision with Background Pedestrian Detection. Part 1 of 2. See NIVI**
  * Group `3003`
    * `aktiv` (start=7, mask=00001000b, comment=FGS_NIVI_KI_ENABLE)

### KOMBI FPK_I12 (CAFD 00001060) — authored by Almaretto | Series: I001

* **ENABLE HUD Turnsignal Blinkers (NOT with 6WB Digital Cluster). Part 1 of 2. See HU_NBT**
  * Group `3008`
    * `aktiv` (start=5, mask=00000001b, comment=HUD_PIA_BLINKER)
  * Group `3003`
    * `aktiv` (start=11, mask=00000001b, comment=HUD_BLINKER_ENABLE)

* **ENABLE Night Vision with Background Pedestrian Detection. Part 1 of 2. See NIVI**
  * Group `3003`
    * `aktiv` (start=4, mask=00000001b, comment=FGS_NIVI_KI_ENABLE)

* **ENABLE Range Extender Activation Battery Capacity (12%)**
  * Group `3000`
    * `18` (start=46, mask=11111111b, comment=SOC_HOLD_POS)

### KOMBI_I01_F56 (CAFD 0000141F) — authored by Almaretto | Series: I001

* **ENABLE HUD Turnsignal Blinkers (NOT with 6WB Digital Cluster). Part 1 of 2. See HU_NBT**
  * Group `3008`
    * `aktiv` (start=7, mask=00000001b, comment=HUD_PIA_BLINKER)
  * Group `3003`
    * `aktiv` (start=4, mask=00000001b, comment=HUD_BLINKER_ENABLE)

* **ENABLE Night Vision with Background Pedestrian Detection. Part 1 of 2. See NIVI**
  * Group `3000`
    * `aktiv` (start=43, mask=00000001b, comment=FGS_NIVI_KI_ENABLE)

* **Increase Computer-limited fuel tank capacity of REX to full 2.4 US Gal (NOT 17-18)**
  * Group `3005`
    * `8_liter` (start=7, mask=11111111b, comment=TNK_VOLL_ANZEIGE)
    * `mcv_rex_liter_kl_rechts` (start=8, end=17, mask=11111111b, comment=TNK_LITER_RECHTS)
    * `mcv_rex_ohm_kl_rechts_us` (start=28, end=47, mask=11111111b, comment=TNK_OHM_RECHTS)

### NIVI2 (CAFD 0000004C) — authored by Almaretto | Series: F010

* **ENABLE Night Vision with Background Pedestrian Detection. Part 1 of 2. See KOMBI**
  * Group `3000`
    * `ACTIVE_NV2P_BD` (start=20, mask=00000001b, comment=CC_Messages)
  * Group `3240`
    * `FF` (start=21, mask=11111111b, comment=DTC_ENABLE_13)
  * Group `3250`
    * `AW_ON` (start=0, mask=00010000b, comment=USE_ACUTE_WARNING)
    * `AW_ON` (start=0, mask=10000000b, comment=USE_ACUTE_SOUND)
  * Group `3252`
    * `AW_ON` (start=0, mask=00000001b, comment=R1_ACTIVE)
  * Group `3253`
    * `ON` (start=50, mask=00100001b, comment=PED_DET_IN_BACKGROUND)

* **ENABLE Night Vision Pedestrian Detection at ANY speed (Default is at 8 mph)**
  * Group `3252`
    * `00` (start=89, mask=00111111b, comment=BD_MINIMUM_SPEED)

* **ENABLE Night Vision Camera on – Standby (Default when dark outside)**
  * Group `3000`
    * `ON_WITH_PWR_ON` (start=23, mask=00110000b, comment=Light_Sensor)

### ICMQL (CAFD 000013D8) — authored by Almaretto | Series: F015

* **ENABLE Blind Spot Detection at 20km/h (13mph)**
  * Group `3000`
    * `20 kmh` (start=190, mask=00111111b)

* **ENABLE default ACC distance at ONE (1) blocks**
  * Group `3000`
    * `Stufe_1` (start=184, mask=00000111b)

* **ENABLE default ACC distance at TWO (2) blocks**
  * Group `3000`
    * `Stufe_2` (start=184, mask=00000111b)

* **ENABLE default ACC distance at THREE (3) blocks**
  * Group `3000`
    * `Stufe_3` (start=184, mask=00000111b)

* **ENABLE default ACC distance at FOUR (4) blocks**
  * Group `3000`
    * `Stufe_4` (start=184, mask=00000111b)

* **F15 - ENABLE Comfort Drive Mode**
  * Group `300A`
    * `aktiv` (start=62, mask=00000001b, comment=feshasmode1 - Comfort)

* **F15 - ENABLE Comfort+ Drive Mode**
  * Group `300A`
    * `aktiv` (start=62, mask=00000010b, comment=feshasmode2 - Comfort+)

* **F15 - ENABLE Unknown1 Drive Mode**
  * Group `300A`
    * `aktiv` (start=62, mask=00000100b, comment=feshasmode3 - Unknown1)

* **F15 - ENABLE Sport Drive Mode**
  * Group `300A`
    * `aktiv` (start=62, mask=00001000b, comment=feshasmode4 - Sport)

* **F15 - ENABLE Sport+ Drive Mode**
  * Group `300A`
    * `aktiv` (start=62, mask=00010000b, comment=feshasmode5 - Sport+)

* **F15 - ENABLE Unknown2 Drive Mode**
  * Group `300A`
    * `aktiv` (start=62, mask=00100000b, comment=feshasmode6 - Unknown2)

* **F15 - ENABLE EcoPro Drive Mode**
  * Group `300A`
    * `aktiv` (start=62, mask=01000000b, comment=feshasmode7 - EcoPro)

* **F15 - ENABLE Edrive Drive Mode**
  * Group `300A`
    * `aktiv` (start=62, mask=10000000b, comment=feshasmode8 - Edrive)

* **ENABLE Remember Comfort+ Drive Mode When Shutdown - F15**
  * Group `300A`
    * `aktiv` (start=63, mask=00000100b, comment=fesallowmode2lastfunction - Comfort+)
    * `FF` (start=79, mask=11111111b, comment=feslastfunctioninterval - Prevent Reset)

* **ENABLE Remember Sport Drive Mode When Shutdown - F15**
  * Group `300A`
    * `aktiv` (start=63, mask=00001000b, comment=fesallowmode4lastfunction - Sport)
    * `FF` (start=79, mask=11111111b, comment=feslastfunctioninterval - Prevent Reset)

* **ENABLE Remember Sport+ Drive Mode When Shutdown - F15**
  * Group `300A`
    * `aktiv` (start=63, mask=00010000b, comment=fesallowmode7lastfunction - EcoPro)
    * `FF` (start=79, mask=11111111b, comment=feslastfunctioninterval - Prevent Reset)

* **ENABLE Remember Edrive Drive Mode When Shutdown - F15**
  * Group `300A`
    * `aktiv` (start=63, mask=00100000b, comment=fesallowmode8lastfunction - Edrive)
    * `FF` (start=79, mask=11111111b, comment=feslastfunctioninterval - Prevent Reset)

* **ENABLE Increased Traffic Jam Assistant (TJA) Max Speed - MPH**
  * Group `3000`
    * `3F` (start=191, mask=00111111b, comment=C_QalcgRel_v_Tacho_aktiv_mph)

* **ENABLE Increased Traffic Jam Assistant (TJA) Max Speed - KMH**
  * Group `3000`
    * `63` (start=208, mask=11111111b, comment=C_QalcgRel_v_Tacho_aktiv_kmh)

* **ENABLE Traffic Jam Assistant (TJA) on ALL ROADS**
  * Group `3000`
    * `00` (start=97, mask=11100000b, comment=C_STA_Einschraenkung)

### ICMQL (CAFD 0000067B) — authored by Almaretto | Series: F010

* **Activate LIM Function in North American Cars (Part 2 of 2. See KOMBI)**
  * Group `3000`
    * `aktiv` (start=173, mask=00000001b)
    * `zugelassen` (start=197, mask=11100000b)

* **ENABLE Blindspot Detection at 20kmh (13 mph)**
  * Group `3000`
    * `20 kmh` (start=190, mask=00111111b)

* **ENABLE default ACC distance at ONE (1) block**
  * Group `3000`
    * `Stufe_1` (start=184, mask=00000111b)

* **ENABLE default ACC distance at TWO (2) blocks**
  * Group `3000`
    * `Stufe_2` (start=184, mask=00000111b)

* **ENABLE default ACC distance at THREE (3) blocks**
  * Group `3000`
    * `Stufe_3` (start=184, mask=00000111b)

* **ENABLE default ACC distance at FOUR (4) blocks**
  * Group `3000`
    * `Stufe_4` (start=184, mask=00000111b)

* **ENABLE Default ECO PRO drive mode startup**
  * Group `3000`
    * `verbaut` (start=36, mask=00001000b, comment=ICMKOD_B_InitEco)

* **ENABLE Default COMFORT drive mode startup**
  * Group `3000`
    * `nicht_verbaut` (start=36, mask=00001000b, comment=ICMKOD_B_InitEco)

* **ENABLE Increased Traffic Jam Assistant (TJA) Max Speed - MPH**
  * Group `3000`
    * `3F` (start=191, mask=00111111b, comment=C_QalcgRel_v_Tacho_aktiv_mph)

* **ENABLE Increased Traffic Jam Assistant (TJA) Max Speed - KMH**
  * Group `3000`
    * `63` (start=208, mask=11111111b, comment=C_QalcgRel_v_Tacho_aktiv_kmh)

* **ENABLE Traffic Jam Assistant (TJA) on ALL ROADS**
  * Group `3000`
    * `00` (start=97, mask=11100000b, comment=C_STA_Einschraenkung)

### ICMQL (CAFD 00000052) — authored by Almaretto

* **ENABLE Blindspot Detection at 25kmh (15.5 mph)**
  * Group `3000`
    * `25 kmh` (start=65, mask=11111111b, comment=Hc2_i_CPar_Aktiv_v_low)

### FRM_03CT (CAFD 0000106D) — authored by Almaretto | Series: F010

* **ENABLE Open/Close windows and mirrors via keyFOB - CA. Part 1 of 2. See CAS (NA Cars)**
  * Group `3020`
    * `aktiv` (start=0, mask=10000000b)

* **ENABLE Auto-Activate Hazard Warning System (Emergency Lights)**
  * Group `3050`
    * `aktiv` (start=2, mask=10000000b, comment=Sudden Stops at 70 km/h (~43 mph))

* **ENABLE Welcome Fog Lights - Soft LED**
  * Group `3050`
    * `soft_on_LED` (start=29, mask=00001100b)

* **ENABLE EU Brake Light Behavior (Blink)**
  * Group `3050`
    * `02` (start=23, mask=01110000b, comment=Default = glow brighter and wider)

* **ENABLE Increased Passenger Mirror Tilt (Curb View) in Reverse**
  * Group `3020`
    * `5A` (start=1, mask=11111111b)

* **ENABLE Fog Lights with High Beams**
  * Group `3050`
    * `nicht_aktiv` (start=16, mask=00000100b)

* **ENABLE Front and Rear DRL (8TL)**
  * Group `3050`
    * `DRL_S` (start=20, mask=00001110b)

* **ENABLE Automatic High Beams Assistant (HBA)**
  * Group `3050`
    * `automatisch` (start=20, mask=00100000b)

* **ENABLE FRONT driver/passenger window Roll Up when doors opened (JBBFE for Rear)**
  * Group `3030`
    * `nicht_aktiv` (start=1, mask=00000100b)

* **Easy Entry/Exit Steering Wheel and Driver Seat (Tilt First). Step 1 of 2. See SM**
  * Group `30A0`
    * `aktiv` (start=9, mask=10000000b)
    * `aktiv` (start=10, mask=10000000b)
    * `02` (start=1, mask=11000000b, comment=Tilt Adjust 1st)

* **Easy Entry/Exit Steering Wheel and Driver Seat (Longitudinal 1st). Step 1 of 2. See SM**
  * Group `30A0`
    * `aktiv` (start=9, mask=10000000b)
    * `aktiv` (start=10, mask=10000000b)
    * `01` (start=1, mask=11000000b, comment=Tilt Adjust 1st)

### FRM_03CT (CAFD 0000106D) — authored by Almaretto | Series: F025

* **F25 NGHB. Part 3 of 3. See LHM43/LHM44. Step 3 of PDF**
  * Group `3080`
    * `00, 00, 00, 00` (start=32, end=35, mask=11111111b, comment=LAMP_MAP_PARA_SATZ_09)
    * `00, 00, 00, 00` (start=36, end=39, mask=11111111b, comment=LAMP_MAP_PARA_SATZ_10)

### FRM_O3CT (CAFD 0000012F) — authored by Almaretto | Series: F010

* **ENABLE Folding Mirrors/Window Rollup. Part 1 of 2. See CAS**
  * Group `3020`
    * `aktiv` (start=0, mask=10000000b, comment=ASP_BEIKLAPPEN_BEI_KOMFORTSCHLIESSEN)

* **ENABLE Increased Passenger Mirror Tilt (Curb View) in Reverse**
  * Group `3020`
    * `5A` (start=1, mask=11111111b, comment=ASP_BORDSTEINAUTOMATIK_DELTA)

* **ENABLE Variable Light Distribution (VLD)**
  * Group `3400`
    * `aktiv` (start=2, mask=00100000b, comment=AHL2_ENABLE)

* **ENABLE Auto-Activate Hazard Warning System (Emergency Lights)**
  * Group `3050`
    * `aktiv` (start=2, mask=10000000b, comment=Sudden Stops at 70 km/h (~43 mph))

* **ENABLE Welcome Fog Lights - Soft LED**
  * Group `3050`
    * `soft_on_LED` (start=29, mask=00001100b)

* **ENABLE EU Brake Light Behavior (Blink)**
  * Group `3050`
    * `02` (start=23, mask=01110000b, comment=Default = glow brighter and wider)

* **ENABLE Fog Lights with High Beams**
  * Group `3050`
    * `nicht_aktiv` (start=16, mask=00000100b)

* **ENABLE Front and Rear DRL (8TL)**
  * Group `3050`
    * `DRL_S` (start=20, mask=00001110b)

* **ENABLE Automatic High Beams Assistant (HBA)**
  * Group `3050`
    * `automatisch` (start=20, mask=00100000b)

* **ENABLE FRONT driver/passenger window Roll Up when doors opened (JBBFE for Rear)**
  * Group `3030`
    * `00` (start=1, mask=00000100b)

* **Easy Entry/Exit Steering Wheel and Driver Seat (Tilt First). Step 1 of 2. See SM**
  * Group `30A0`
    * `aktiv` (start=9, mask=10000000b)
    * `aktiv` (start=10, mask=10000000b)
    * `02` (start=1, mask=11000000b, comment=Tilt Adjust 1st)

* **Easy Entry/Exit Steering Wheel and Driver Seat (Longitudinal 1st). Step 1 of 2. See SM**
  * Group `30A0`
    * `aktiv` (start=9, mask=10000000b)
    * `aktiv` (start=10, mask=10000000b)
    * `01` (start=1, mask=11000000b, comment=Longitude Adjust 1st)

### CAS_04 (CAFD 0000000F) — authored by Almaretto | Series: F010

* **DISABLE Auto Start Stop (ASS) by Default**
  * Group `3000`
    * `aktiv` (start=3, mask=00010000b)

* **ENABLE Auto Start Stop (ASS) Memory - Shutdown Setting**
  * Group `3000`
    * `aktiv` (start=3, mask=00100000b)

* **ENABLE Open/Close windows and mirrors via keyFOB - CA (NA Cars). Part 2 of 2. See FRM**
  * Group `3003`
    * `aktiv` (start=2, mask=00000001b)
    * `aktiv` (start=2, mask=00000010b)
    * `aktiv` (start=2, mask=00000100b)
    * `aktiv` (start=2, mask=00001000b)
    * `aktiv` (start=2, mask=00100000b)

* **Removes Initiation Delay for Mirrors/Windows**
  * Group `3003`
    * `00` (start=12, mask=11111111b)

* **ENABLE Auto Unlock doors when engine stopped (Requires Auto-Lock)**
  * Group `3002`
    * `aktiv` (start=1, mask=10000000b, comment=Single pull to open)

* **DISABLE Auto Unlock doors when engine stopped (Requires Auto-Lock)**
  * Group `3002`
    * `nicht_aktiv` (start=1, mask=10000000b, comment=Single pull to open)

* **DISABLE Horn Lock Confirmation while engine running**
  * Group `3002`
    * `nicht_aktiv` (start=0, mask=00100000b, comment=CLM_HORN_AT_SECURE)

* **ENABLE Horn Lock Confirmation while engine running**
  * Group `3002`
    * `aktiv` (start=0, mask=00100000b, comment=CLM_HORN_AT_SECURE)

* **ENABLE Follow Me Home Lighting with Short Press of Panic Button**
  * Group `3002`
    * `aktiv` (start=1, mask=00000010b, comment=REMOTE_KEY_SPECIAL_FCT)

* **DISABLE Follow Me Home Lighting with Short Press of Panic Button**
  * Group `3002`
    * `nicht_aktiv` (start=1, mask=00000010b, comment=REMOTE_KEY_SPECIAL_FCT)

* **ENABLE Engine Start without Brake Pedal (Press Start Twice with Second Hold)**
  * Group `3000`
    * `nicht_aktiv` (start=1, mask=00000001b, comment=TC_STARTLOCK_BRAKE)
    * `nicht_aktiv` (start=1, mask=00010000b, comment=TC_STARTLOCK_DRIVINGREADINESS)

* **DISABLE Engine Start without Brake Pedal (Press Start Twice with Second Hold)**
  * Group `3000`
    * `aktiv` (start=1, mask=00000001b, comment=TC_STARTLOCK_BRAKE)
    * `aktiv` (start=1, mask=00010000b, comment=TC_STARTLOCK_DRIVINGREADINESS)

* **ENABLE  Radio and Nav Off when drivers door opened**
  * Group `3000`
    * `aktiv` (start=2, mask=00000001b, comment=TC_LOGIC_KLR_OFF_DOOR)

### DSC_Premium (CAFD 00000C18) — authored by Almaretto | Series: F010

* **ENABLE Auto-Parking Brake Release (Only 2010-2012 cars). Part 1 of 2. See EMF**
  * Group `3000`
    * `aktiv` (start=27, mask=00100000b, comment=Funktion_AutomaticDriveawayRelease_aktiv)

### EMF_03TRW (CAFD 0000029B) — authored by Almaretto | Series: F010

* **ENABLE Auto-Parking Brake Release (Only 2010-2012 cars). Part 2 of 2. See DSC**
  * Group `3000`
    * `ADR_Ein` (start=0, mask=00001000b, comment=ADR_ein)

### CFAS-PLX_1 (CAFD 000000B5) — authored by Almaretto | Series: F010,F015,F030,F80

* **Time Period Seats will Remember heating/cooling/massage settings (0 minutes)**
  * Group `3000`
    * `00` (start=4, mask=00000011b, comment=0 minutes)

* **Time Period Seats will Remember heating/cooling/massage settings (15 minutes)**
  * Group `3000`
    * `01` (start=4, mask=00000011b, comment=15 minutes)

* **Time Period Seats will Remember heating/cooling/massage settings (24 hours)**
  * Group `3000`
    * `02` (start=4, mask=00000011b, comment=24 hours)

* **Time Period Seats will Remember heating/cooling/massage settings (Infinity)**
  * Group `3000`
    * `03` (start=4, mask=00000011b, comment=Infinity)

* **Easy Entry/Exit Steering Wheel and Driver Seat. Step 1 of 2. See FRM for F10**
  * Group `3000`
    * `Modus_FA_SLV` (start=0, mask=00011100b)
  * Group `3012`
    * `00, 28` (start=0, end=1, mask=11111111b)
    * `00, 32` (start=4, end=5, mask=11111111b)

### SZL_LWS_03 (CAFD 0000033D) — authored by Almaretto | Series: F010

* **ENABLE Steering Paddle Shifters**
  * Group `3000`
    * `aktiv` (start=0, mask=00000100b, comment=Lenkrad_Schaltpaddles)

* **DISABLE Steering Paddle Shifters**
  * Group `3000`
    * `nicht_aktiv` (start=0, mask=00000100b, comment=Lenkrad_Schaltpaddles)

### JBBFE (CAFD 00000014) — authored by Almaretto | Series: F010

* **ENABLE REAR driver/passenger window Roll Up when doors opened FRM for Front)**
  * Group `3070`
    * `nicht_aktiv` (start=0, mask=00000100b)

* **ENABLE Reduced Rain HeadLight Sensor Sensitivity (Insensitive)**
  * Group `3530`
    * `unempfindlich` (start=5, mask=00000111b)
    * `unempfindlich` (start=5, mask=00111000b)

* **Adjust Rear and Side Mirror Dimming for Dark Windows**
  * Group `3080`
    * `Dunkel` (start=1, mask=00000110b)
    * `39` (start=20, mask=11111100b)
    * `39` (start=28, mask=11111100b)

### JBBF_E3_PDC (CAFD 00000018) — authored by Almaretto | Series: F010

* **ENABLE Top/Rear Camera at All Speeds. Part 1 of 2. See TRSVC for Side**
  * Group `3009`
    * `FF` (start=15, mask=11111111b, comment=max speed to disable top camera view)
    * `FF` (start=16, mask=11111111b, comment=max speed to disable rear camera view)
    * `FF` (start=17, mask=11111111b, comment=max distance to disable top camera view)
    * `FF` (start=18, mask=11111111b, comment=max distance to disable rear camera view)

### TRSVC (CAFD 00000223) — authored by Almaretto | Series: F010,F030,F080

* **Side Camera at All Speeds. Part 1 of 2. See PDC for Top/Rear**
  * Group `3000`
    * `FF` (start=114, mask=11111111b, comment=Maximum speed side view can activate)
    * `FF` (start=115, mask=11111111b, comment=Auto-deactivate side view speed)

### ACSM_4C (CAFD 00000909) — authored by Almaretto | Series: F010,F015

* **DISABLE Seat Belt Instrument Cluster Status (Passenger)**
  * Group `3000`
    * `nicht_aktiv` (start=15, mask=00010000b)

* **DISABLE Seat Belt Instrument Cluster Status (Driver)**
  * Group `3000`
    * `nicht_aktiv` (start=15, mask=00001000b)

* **DISABLE Seat Belt Reminder Chime (Driver)**
  * Group `3000`
    * `nicht_aktiv` (start=15, mask=00000010b)

* **DISABLE Seat Belt Reminder Chime(Passenger)**
  * Group `3000`
    * `nicht_aktiv` (start=15, mask=00000100b)

* **DISABLE Initial Belt Warning Chime (845 Acoustic Belt Warning)**
  * Group `3000`
    * `nicht_aktiv` (start=15, mask=00000001b)

* **DISABLE Seat Belt Reminder PreWarning Chime (Driver)**
  * Group `3000`
    * `nicht_aktiv` (start=16, mask=00000001b)

* **DISABLE Seat Belt Reminder PreWarning Chime (Passenger)**
  * Group `3000`
    * `nicht_aktiv` (start=16, mask=00000010b)

### ACSM_3 (CAFD 0000009C) — authored by Almaretto | Series: F010

* **DISABLE Seat Belt Instrument Cluster Status (Passenger)**
  * Group `3000`
    * `nicht_aktiv` (start=11, mask=00010000b, comment=Gurtzustandsanzeige_Beifahrer_GWF_GZA_BF)

* **DISABLE Seat Belt Instrument Cluster Status (Driver)**
  * Group `3000`
    * `nicht_aktiv` (start=11, mask=00001000b, comment=Gurtzustandsanzeige_Fahrer_GWF_GZA_FA)

* **DISABLE Seat Belt Reminder Chime (Driver)**
  * Group `3000`
    * `nicht_aktiv` (start=11, mask=00000010b, comment=SBR_FA_GWF_SBR_FA)

* **DISABLE Seat Belt Reminder Chime Passenger)**
  * Group `3000`
    * `nicht_aktiv` (start=11, mask=00000100b, comment=SBR_BF_GWF_SBR_BF)

* **DISABLE Initial Belt Warning Chime (845 Acoustic Belt Warning)**
  * Group `3000`
    * `nicht_aktiv` (start=11, mask=00000001b, comment=Initialwarnung_GWF_IW)

### ACSM_4i (CAFD 000011AB) — authored by Almaretto | Series: I001

* **DISABLE Seat Belt Reminder (Driver) - Old Firmware**
  * Group `3001`
    * `nicht_aktiv` (start=1, mask=00000001b, comment=SeatBeltReminder_Fahrer)

* **DISABLE Seat Belt Reminder (Passenger) - Old Firmware**
  * Group `3001`
    * `nicht_aktiv` (start=2, mask=00000001b, comment=SeatBeltReminder_Beifahrer)

* **DISABLE Seat Belt Disconnected Reminder Sound (Driver) - Old Firmware**
  * Group `3001`
    * `nicht_aktiv` (start=3, mask=00000001b, comment=SBR_PreWarning_Fahrer)

* **DISABLE Seat Belt Disconnected Reminder Sound (Passenger) - Old Firmware**
  * Group `3001`
    * `nicht_aktiv` (start=4, mask=00000001b, comment=SBR_PreWarning_Beifahrer)

* **DISABLE Initial Belt Warning Gong - Old Firmware**
  * Group `3001`
    * `nicht_aktiv` (start=0, mask=00000001b, comment=Initialwarnung)

### ASD01 (CAFD 00000F9B) — authored by Almaretto | Series: F010,F080

* **DISABLE Active Sound Design (M5 only). Part 1 of 2. See HU_NBT**
  * Group `3000`
    * `0D` (start=0, mask=11111111b, comment=Model Range)
    * `08` (start=1, mask=11111111b, comment=Model Range)

### FLE_02 (CAFD 000024C3) — authored by Almaretto | Series: F015

* **F15 - Turn off Front DRL Headlight dim (Stay 100 Percent). Do Both FLEs**
  * Group `3004`
    * `01, 01, 0A, 01, 01, 01, 01, 01, 01, 0B` (start=10, end=19, mask=11111111b)
    * `01, 01, 0A, 01, 01, 01, 01, 01, 01, 0B` (start=20, end=29, mask=11111111b)
    * `01, 01, 0A, 01, 01, 01, 01, 01, 01, 0B` (start=30, end=39, mask=11111111b)

* **F15 - Turn off Amber Sidemarker on Headlights**
  * Group `3006`
    * `00` (start=41, mask=11110000b)
    * `00` (start=49, mask=11111111b)

* **F15 (After July 1 2015) - NGHB. Apply to Both FLEs. Step 2 of PDF**
  * Group `3003`
    * `04, 01, 01, 01, 02, 03, 01, 01, 05, 01` (start=20, end=29, mask=11111111b, comment=Stadt_V_Idx)
    * `04, 01, 01, 01, 02, 03, 01, 01, 01, 01` (start=30, end=39, mask=11111111b, comment=SAE_Idx)
    * `04, 01, 01, 01, 02, 03, 01, 01, 01, 01` (start=120, end=129, mask=11111111b, comment=H_plus4_Idx)
    * `01, 06, 01, 01, 06, 06, 01, 01, 01, 01` (start=130, end=139, mask=11111111b, comment=Blendfreies_Fernlicht_Idx)
    * `07, 07, 01, 01, 07, 07, 07, 01, 01, 01` (start=140, end=149, mask=11111111b, comment=Volles_Fernlicht_)
  * Group `3004`
    * `01, 01, 0A, 01, 01, 01, 01, 01, 01, 0B` (start=0, end=9, mask=11111111b, comment=DRL_Idx)
    * `01, 01, 0C, 01, 01, 01, 01, 01, 01, 0B` (start=10, end=19, mask=11111111b, comment=POLI1_Idx)
    * `01, 01, 0C, 01, 01, 01, 01, 01, 01, 0B` (start=20, end=29, mask=11111111b, comment=POLI2_Idx)
    * `01, 01, 0C, 01, 01, 01, 01, 01, 01, 0B` (start=30, end=39, mask=11111111b, comment=POLI3_Idx)
    * `01, 01, 0C, 01, 01, 01, 01, 01, 01, 0B` (start=40, end=49, mask=11111111b, comment=PLI_Idx)
    * `01, 01, 0E, 01, 01, 01, 01, 01, 01, 0B` (start=60, end=69, mask=11111111b, comment=WELL1_Idx)
    * `01, 01, 0E, 01, 01, 01, 01, 01, 01, 0B` (start=70, end=79, mask=11111111b, comment=WELL2_Idx)
    * `01, 0F, 01, 01, 01, 01, 01, 01, 01, 0B` (start=80, end=89, mask=11111111b, comment=WELL3_Idx)
    * `01, 0F, 01, 01, 01, 01, 0F, 01, 01, 0B` (start=90, end=99, mask=11111111b, comment=WELL4_Idx)
    * `10, 01, 0E, 01, 10, 10, 01, 01, 01, 0B` (start=100, end=109, mask=11111111b, comment=FMH_Idx)
    * `10, 01, 0E, 01, 10, 10, 01, 01, 01, 0B` (start=110, end=119, mask=11111111b, comment=REMLI_Idx)
    * `0F, 08, 0F, 01, 0F, 0F, 08, 01, 01, 0B` (start=120, end=129, mask=11111111b, comment=HBBLINK_Idx)
    * `01, 01, 01, 01, 01, 01, 01, 0F, 01, 01` (start=130, end=139, mask=11111111b, comment=DWABLINK_Idx)
    * `01, 01, 01, 01, 01, 01, 01, 01, 01, 01` (start=140, end=149, mask=11111111b, comment=PANICMODE_Idx)
    * `01, 08, 0F, 01, 01, 01, 08, 0F, 01, 11` (start=150, end=159, mask=11111111b, comment=RAIDALARM_Idx)
    * `01, 01, 01, 01, 01, 01, 01, 0F, 01, 11` (start=160, end=169, mask=11111111b, comment=BLINKEN_Idx)
    * `01, 01, 01, 0F, 01, 01, 01, 01, 01, 01` (start=180, end=189, mask=11111111b, comment=SIDEMRKLGT_Idx)
  * Group `3000`
    * `0A` (start=4, mask=11110000b, comment=HlPrjLabel_HlType)
  * Group `3005`
    * `00` (start=3, mask=01000000b, comment=LmmIdx00_ErrorImpact)
    * `00` (start=11, mask=01000000b, comment=LmmIdx02_ErrorImpact)
    * `00` (start=15, mask=01000000b, comment=LmmIdx03_ErrorImpact)
    * `00` (start=16, mask=11111111b, comment=LmmIdx04_Intensity)
    * `04` (start=17, mask=11111111b, comment=LmmIdx04_TimeOn)
    * `04` (start=18, mask=11111111b, comment=LmmIdx04_TimeOff)
    * `00` (start=19, mask=01000000b, comment=LmmIdx04_ErrorImpact)
    * `2E` (start=20, mask=11111111b, comment=LmmIdx05_Intensity)
    * `04` (start=21, mask=11111111b, comment=LmmIdx05_TimeOn)
    * `04` (start=22, mask=11111111b, comment=LmmIdx05_TimeOff)
    * `00` (start=23, mask=01000000b, comment=LmmIdx05_ErrorImpact)
    * `64` (start=24, mask=11111111b, comment=LmmIdx06_Intensity)
    * `04` (start=25, mask=11111111b, comment=LmmIdx06_TimeOn)
    * `00` (start=27, mask=01000000b, comment=LmmIdx06_ErrorImpact)
    * `01` (start=31, mask=00001111b, comment=LmmIdx07_Priority)
    * `00` (start=31, mask=01000000b, comment=LmmIdx07_ErrorImpact)
    * `2E` (start=36, mask=11111111b, comment=LmmIdx09_Intensity)
    * `03` (start=39, mask=00001111b, comment=LmmIdx09_Priority)
    * `00` (start=39, mask=01000000b, comment=LmmIdx09_ErrorImpact)
    * `64` (start=40, mask=11111111b, comment=LmmIdx10_Intensity)
    * `02` (start=43, mask=00001111b, comment=LmmIdx10_Priority)
    * `64` (start=44, mask=11111111b, comment=LmmIdx11_Intensity)
    * `03` (start=47, mask=00001111b, comment=LmmIdx11_Priority)
    * `00` (start=47, mask=01000000b, comment=LmmIdx11_ErrorImpact)
    * `29` (start=48, mask=11111111b, comment=LmmIdx12_Intensity)
    * `03` (start=51, mask=00001111b, comment=LmmIdx12_Priority)
    * `01` (start=51, mask=01000000b, comment=LmmIdx12_ErrorImpact)
    * `08` (start=53, mask=11111111b, comment=LmmIdx13_TimeOn)
    * `19` (start=54, mask=11111111b, comment=LmmIdx13_TimeOff)
    * `01` (start=55, mask=00001111b, comment=LmmIdx13_Priority)
    * `29` (start=56, mask=11111111b, comment=LmmIdx14_Intensity)
    * `00` (start=57, mask=11111111b, comment=LmmIdx14_TimeOn)
    * `00` (start=58, mask=11111111b, comment=LmmIdx14_TimeOff)
    * `04` (start=59, mask=00001111b, comment=LmmIdx14_Priority)
    * `01` (start=59, mask=01000000b, comment=LmmIdx14_ErrorImpact)
    * `64` (start=60, mask=11111111b, comment=LmmIdx15_Intensity)
    * `00` (start=63, mask=10000000b, comment=LmmIdx15_Active)
    * `64` (start=64, mask=11111111b, comment=LmmIdx16_Intensity)
    * `04` (start=65, mask=11111111b, comment=LmmIdx16_TimeOn)
    * `04` (start=66, mask=11111111b, comment=LmmIdx16_TimeOff)
    * `0A` (start=67, mask=00001111b, comment=LmmIdx16_Priority)
    * `01` (start=71, mask=00001111b, comment=LmmIdx17_Priority)
    * `01` (start=71, mask=10000000b, comment=LmmIdx17_Active)
    * `5B` (start=72, mask=11111111b, comment=LmmIdx18_Intensity)
    * `04` (start=73, mask=11111111b, comment=LmmIdx18_TimeOn)
    * `04` (start=74, mask=11111111b, comment=LmmIdx18_TimeOff)
    * `01` (start=75, mask=00001111b, comment=LmmIdx18_Priority)
    * `01` (start=134, mask=00111111b, comment=LmmReLut_LgtFct0)
    * `01` (start=134, mask=11000000b, comment=LmmReLut_LogLmpLow0)
    * `03` (start=135, mask=11111100b, comment=LmmReLut_Idx0)
    * `02` (start=136, mask=00111111b, comment=LmmReLut_LgtFct1)
    * `01` (start=136, mask=11000000b, comment=LmmReLut_LogLmpLow1)
    * `03` (start=137, mask=11111100b, comment=LmmReLut_Idx1)
    * `03` (start=138, mask=00111111b, comment=LmmReLut_LgtFct2)
    * `01` (start=138, mask=11000000b, comment=LmmReLut_LogLmpLow2)
    * `12` (start=139, mask=11111100b, comment=LmmReLut_Idx2)
    * `0D` (start=140, mask=00111111b, comment=LmmReLut_LgtFct3)
    * `01` (start=140, mask=11000000b, comment=LmmReLut_LogLmpLow3)
    * `03` (start=141, mask=11111100b, comment=LmmReLut_Idx3)
    * `0E` (start=142, mask=00111111b, comment=LmmReLut_LgtFct4)
    * `01` (start=142, mask=11000000b, comment=LmmReLut_LogLmpLow4)
    * `0F` (start=143, mask=11111100b, comment=LmmReLut_Idx4)
    * `06` (start=144, mask=00111111b, comment=LmmReLut_LgtFct5)
    * `01` (start=144, mask=11000000b, comment=LmmReLut_LogLmpLow5)
    * `01` (start=145, mask=00000011b, comment=LmmReLut_LogLmpHigh5)
    * `03` (start=145, mask=11111100b, comment=LmmReLut_Idx5)
    * `07` (start=146, mask=00111111b, comment=LmmReLut_LgtFct6)
    * `01` (start=146, mask=11000000b, comment=LmmReLut_LogLmpLow6)
    * `01` (start=147, mask=00000011b, comment=LmmReLut_LogLmpHigh6)
    * `03` (start=147, mask=11111100b, comment=LmmReLut_Idx6)
    * `08` (start=148, mask=00111111b, comment=LmmReLut_LgtFct7)
    * `01` (start=148, mask=11000000b, comment=LmmReLut_LogLmpLow7)
    * `01` (start=149, mask=00000011b, comment=LmmReLut_LogLmpHigh7)
    * `03` (start=149, mask=11111100b, comment=LmmReLut_Idx7)
    * `09` (start=150, mask=00111111b, comment=LmmReLut_LgtFct8)
    * `01` (start=150, mask=11000000b, comment=LmmReLut_LogLmpLow8)
    * `01` (start=151, mask=00000011b, comment=LmmReLut_LogLmpHigh8)
    * `03` (start=151, mask=11111100b, comment=LmmReLut_Idx8)

### FLE_02 (CAFD 000024C3) — authored by Almaretto | Series: F030

* **F30LCI - HALO Brightness 100% with Non-Adaptive LED lowbeams. Do Both FLEs**
  * Group `3004`
    * `00, 00, 00, 00, 00, 00, 04, 00, 00, 00` (start=10, end=19, mask=11111111b)
    * `00, 00, 00, 00, 00, 00, 04, 00, 00, 00` (start=20, end=29, mask=11111111b)
    * `00, 00, 00, 00, 00, 00, 04, 00, 00, 00` (start=30, end=39, mask=11111111b)

### LHM2 (CAFD 000010BA) — authored by Almaretto | Series: F015

* **F15 (Before July 1 2015) - NGHB. Part 1 of 2. See LHM44**
  * Group `3000`
    * `FA, 64, 00, 00, 00, FA, 00` (start=0, end=6, mask=11111111b, comment=M1. Step 2 of PDF)
    * `FA, 64, 00, 00, 00, FA, 00` (start=7, end=13, mask=11111111b, comment=M2. Step 2 of PDF)
    * `FA, 00, 00, 00, 00, FA, 00` (start=14, end=20, mask=11111111b, comment=M3. Step 2 of PDF)
    * `FA, 00, 00, 00, 00, C8, 00` (start=21, end=27, mask=11111111b, comment=M4. Step 2 of PDF)
    * `FA, 00, FA, 00, 00, FA, 00` (start=91, end=97, mask=11111111b, comment=M14. Step 2 of PDF)
    * `FA, FA, FA, 00, 00, FA, FA` (start=98, end=104, mask=11111111b, comment=M15. Step 2 of PDF)

### LHM2 (CAFD 000010BA) — authored by Almaretto | Series: F025

* **F25 NGHB. Part 1 of 3. See LHM44/FRM. Step 2 of PDF**
  * Group `3000`
    * `FA, 64, 00, 00, FA, FA, 00` (start=0, end=6, mask=11111111b, comment=M1)
    * `FA, 64, 00, 00, FA, FA, 00` (start=7, end=13, mask=11111111b, comment=M2)
    * `FA, 00, 00, 00, FA, FA, 00` (start=14, end=20, mask=11111111b, comment=M3)
    * `FA, 00, 00, 00, C8, C8, 00` (start=21, end=27, mask=11111111b, comment=M4)
    * `FA, 00, 00, FA, FA, FA, 00` (start=91, end=97, mask=11111111b, comment=M14)
    * `FA, FA, 00, FA, FA, FA, FA` (start=98, end=104, mask=11111111b, comment=M15)

### LHM2 (CAFD 000010BA) — authored by Almaretto | Series: F030,F080

* **F3x and F8x NGHB. Step 1 of 3 - Driver side. See LHM44/FEM_Body**
  * Group `3000`
    * `FA, 64, 00, 00, FA, FA, 00` (start=0, end=6, mask=11111111b, comment=NGHB PDF Step 2)
    * `FA, 64, 00, 00, FA, FA, 00` (start=7, end=13, mask=11111111b, comment=NGHB PDF Step 2)
    * `FA, 00, 00, 19, FA, FA, 00` (start=14, end=20, mask=11111111b, comment=NGHB PDF Step 2)
    * `FA, 00, 00, 00, C8, C8, 00` (start=21, end=27, mask=11111111b, comment=NGHB PDF Step 2)
    * `FA, 00, FA, 00, FA, FA, 00` (start=91, end=97, mask=11111111b, comment=NGHB PDF Step 2)
    * `FA, FA, FA, 00, FA, FA, FA` (start=98, end=104, mask=11111111b, comment=NGHB PDF Step 2)

### LHM2 (CAFD 000016BF) — authored by Almaretto | Series: F015

* **F15 (Before July 1 2015) - NGHB. Part 2 of 2. See LHM43**
  * Group `3000`
    * `FA, FA, 00, 00, 00, FA, 00` (start=0, end=6, mask=11111111b, comment=M1. Step 2 of PDF)
    * `FA, FA, 00, 00, 00, FA, 00` (start=7, end=13, mask=11111111b, comment=M2. Step 2 of PDF)
    * `FA, BB, 00, 00, 00, FA, 00` (start=14, end=20, mask=11111111b, comment=M3. Step 2 of PDF)
    * `FA, 00, 00, 00, 00, C8, 00` (start=21, end=27, mask=11111111b, comment=M4. Step 2 of PDF)
    * `FA, FA, 00, 00, 00, FA, 00` (start=35, end=41, mask=11111111b, comment=M6. Step 2 of PDF)
    * `FA, FA, 00, 00, 00, FA, 00` (start=42, end=48, mask=11111111b, comment=M7. Step 2 of PDF)
    * `FA, FA, 00, 00, 00, FA, 00` (start=49, end=55, mask=11111111b, comment=M8. Step 2 of PDF)
    * `FA, FA, 00, 00, 00, FA, 00` (start=56, end=62, mask=11111111b, comment=M9. Step 2 of PDF)
    * `FA, FA, FA, 00, 00, FA, 00` (start=91, end=97, mask=11111111b, comment=M14. Step 2 of PDF)
    * `FA, FA, FA, 00, 00, FA, FA` (start=98, end=104, mask=11111111b, comment=M15. Step 2 of PDF)

### LHM2 (CAFD 000016BF) — authored by Almaretto | Series: F025

* **F25 NGHB. Part 2 of 3. See LHM43/FRM. Step 2 of PDF**
  * Group `3000`
    * `FA, FA, 00, 00, FA, FA, 00` (start=0, end=6, mask=11111111b, comment=M1)
    * `FA, FA, 00, 00, FA, FA, 00` (start=7, end=13, mask=11111111b, comment=M2)
    * `FA, FA, 00, 00, FA, FA, 00` (start=14, end=20, mask=11111111b, comment=M3)
    * `FA, 00, 00, 00, C8, C8, 00` (start=21, end=27, mask=11111111b, comment=M4)
    * `FA, FA, 00, 00, FA, FA, 00` (start=35, end=41, mask=11111111b, comment=M6)
    * `FA, FA, 00, 00, FA, FA, 00` (start=42, end=48, mask=11111111b, comment=M7)
    * `FA, FA, 00, 00, FA, FA, 00` (start=49, end=55, mask=11111111b, comment=M8)
    * `FA, FA, 00, 00, FA, FA, 00` (start=56, end=62, mask=11111111b, comment=M9)
    * `FA, FA, 00, FA, FA, FA, 00` (start=91, end=97, mask=11111111b, comment=M14)
    * `FA, FA, 00, FA, FA, FA, FA` (start=98, end=104, mask=11111111b, comment=M15)

### LHM2 (CAFD 000016BF) — authored by Almaretto | Series: F030,F080

* **F3x and F8x NGHB. Step 2 of 3- Passenger side. See LHM43/FEM_Body**
  * Group `3000`
    * `FA, FA, 00, 00, FA, FA, 00` (start=0, end=6, mask=11111111b, comment=NGHB PDF Step 2)
    * `FA, FA, 00, 00, FA, FA, 00` (start=7, end=13, mask=11111111b, comment=NGHB PDF Step 2)
    * `FA, FA, 00, 19, FA, FA, 00` (start=14, end=20, mask=11111111b, comment=NGHB PDF Step 2)
    * `FA, 00, 00, 00, C8, C8, 00` (start=21, end=27, mask=11111111b, comment=NGHB PDF Step 2)
    * `FA, FA, 00, 00, FA, FA, 00` (start=35, end=41, mask=11111111b, comment=NGHB PDF Step 2)
    * `FA, FA, 00, 00, FA, FA, 00` (start=42, end=48, mask=11111111b, comment=NGHB PDF Step 2)
    * `FA, FA, 00, 00, FA, FA, 00` (start=49, end=55, mask=11111111b, comment=NGHB PDF Step 2)
    * `FA, FA, 00, 00, FA, FA, 00` (start=56, end=62, mask=11111111b, comment=NGHB PDF Step 2)
    * `FA, FA, FA, 00, FA, FA, 00` (start=91, end=97, mask=11111111b, comment=NGHB PDF Step 2)
    * `FA, FA, FA, 00, FA, FA, FA` (start=98, end=104, mask=11111111b, comment=NGHB PDF Step 2)

### TMS_03 (CAFD 00001082) — authored by Almaretto | Series: F010

* **Turn OFF Amber sidemarker lights. Part 1 of 2. See TMS42. (F10 LCI Xenon)**
  * Group `3005`
    * `F10_524_ECE` (start=16, end=31, mask=11111111b, comment=Standlicht Modus 1)
    * `F10_524_ECE` (start=32, end=47, mask=11111111b, comment=Standlicht Modus 2)
    * `F10_524_ECE` (start=48, end=63, mask=11111111b, comment=Standlicht Modus 3)
    * `F10_524_ECE` (start=80, end=95, mask=11111111b, comment=Welcome Light 1)
    * `F10_524_ECE` (start=144, end=159, mask=11111111b, comment=Follow Me Home)
    * `F10_524_ECE` (start=160, end=175, mask=11111111b, comment=Remote Light)
  * Group `3006`
    * `F10_524_ECE` (start=16, end=31, mask=11111111b, comment=Seitenmarkierungsleuchte)

### TMS_03 (CAFD 00001082) — authored by Almaretto | Series: F030,F080

* **Turn sidemarker LEDs OFF - Driver side. Step 1 of 2. See TMS-1083 (F3x and F8x)**
  * Group `3005`
    * `00, 03, 00, 00, 00, 03, 00, 00, 64, 03, 00, 00, 2B, 04, 00, 00` (start=16, end=31, mask=11111111b, comment=Turn sidemarker LEDs OFF)
    * `00, 03, 00, 00, 00, 03, 00, 00, 64, 03, 00, 00, 2B, 04, 00, 00` (start=32, end=47, mask=11111111b, comment=Turn sidemarker LEDs OFF)
    * `00, 03, 00, 00, 00, 03, 00, 00, 64, 03, 00, 00, 2E, 04, 00, 00` (start=80, end=95, mask=11111111b, comment=Turn sidemarker LEDs OFF)

* **Turn sidemarker LEDs ON - Driver side. Step 1 of 2. See TMS-1083 (F3x and F8x)**
  * Group `3005`
    * `00, 03, 00, 00, 64, 03, 00, 00, 64, 03, 00, 00, 2B, 04, 00, 00` (start=16, end=31, mask=11111111b, comment=Turn sidemarker LEDs ON)
    * `00, 03, 00, 00, 64, 03, 00, 00, 64, 03, 00, 00, 2B, 04, 00, 00` (start=32, end=47, mask=11111111b, comment=Turn sidemarker LEDs ON)
    * `00, 03, 00, 00, 64, 03, 00, 00, 64, 03, 00, 00, 2E, 04, 00, 00` (start=80, end=95, mask=11111111b, comment=Turn sidemarker LEDs ON)

### TMS_03 (CAFD 00001083) — authored by Almaretto | Series: F010

* **Turn OFF Amber sidemarker lights. Part 2 of 2. See TMS41. (F10 LCI Bi-Xenon)**
  * Group `3005`
    * `F10_524_ECE` (start=16, end=31, mask=11111111b, comment=Standlicht Modus 1)
    * `F10_524_ECE` (start=32, end=47, mask=11111111b, comment=Standlicht Modus 2)
    * `F10_524_ECE` (start=48, end=63, mask=11111111b, comment=Standlicht Modus 3)
    * `F10_524_ECE` (start=80, end=95, mask=11111111b, comment=Welcome Light 1)
    * `F10_524_ECE` (start=144, end=159, mask=11111111b, comment=Follow Me Home)
    * `F10_524_ECE` (start=160, end=175, mask=11111111b, comment=Remote Light)
  * Group `3006`
    * `F10_524_ECE` (start=16, end=31, mask=11111111b, comment=Seitenmarkierungsleuchte)

### TMS_03 (CAFD 00001083) — authored by Almaretto | Series: F030,F080

* **Turn sidemarker LEDs OFF - Passenger side. Step 2 of 2. See TMS-1082 (F3x and F8x)**
  * Group `3005`
    * `00, 03, 00, 00, 00, 03, 00, 00, 64, 03, 00, 00, 2B, 04, 00, 00` (start=16, end=31, mask=11111111b, comment=Turn sidemarker LEDs OFF)
    * `00, 03, 00, 00, 00, 03, 00, 00, 64, 03, 00, 00, 2B, 04, 00, 00` (start=32, end=47, mask=11111111b, comment=Turn sidemarker LEDs OFF)
    * `00, 03, 00, 00, 00, 03, 00, 00, 64, 03, 00, 00, 2E, 04, 00, 00` (start=80, end=95, mask=11111111b, comment=Turn sidemarker LEDs OFF)

* **Turn sidemarker LEDs ON - Passenger side. Step 2 of 2. See TMS-1082 (F3x and F8x)**
  * Group `3005`
    * `00, 03, 00, 00, 64, 03, 00, 00, 64, 03, 00, 00, 2B, 04, 00, 00` (start=16, end=31, mask=11111111b, comment=Turn sidemarker LEDs ON)
    * `00, 03, 00, 00, 64, 03, 00, 00, 64, 03, 00, 00, 2B, 04, 00, 00` (start=32, end=47, mask=11111111b, comment=Turn sidemarker LEDs ON)
    * `00, 03, 00, 00, 64, 03, 00, 00, 64, 03, 00, 00, 2E, 04, 00, 00` (start=80, end=95, mask=11111111b, comment=Turn sidemarker LEDs ON)

### FEM_BODY (CAFD 00000794) — authored by Almaretto | Series: F030,F080

* **F3x and F8x NGHB. Step 3 of 3. See LHM43/44.**
  * Group `3073`
    * `00, 00, 00, 15, 00, 00, 0A, 15, 1F` (start=176, end=184, mask=11111111b, comment=NGHB PDF Step 3)
  * Group `3074`
    * `2E, 3B, 00, 00, 00, 00` (start=81, end=86, mask=11111111b, comment=NGHB PDF Step 3)
    * `2E, 3B, 00, 00, 00, 00` (start=87, end=92, mask=11111111b, comment=NGHB PDF Step 3)
    * `00, 00, 00, 00, 00, 00` (start=93, end=98, mask=11111111b, comment=NGHB PDF Step 3)
    * `00, 00, 00, 00, 00, 00` (start=99, end=104, mask=11111111b, comment=NGHB PDF Step 3)
    * `27` (start=60, mask=11111111b, comment=P3.59 improvement)
    * `1F` (start=61, mask=11111111b, comment=P3.59 improvement)
    * `E1` (start=63, mask=11111111b, comment=P3.59 improvement)

* **ENABLE Unlock doors when STOP engine – if auto-locked**
  * Group `3040`
    * `aktiv` (start=1, mask=00000010b, comment=CLM_UNLOCK_KL15OFF_AFTER_PIA_AUTO_LOCK)

* **DISABLE FRONT Window Safety (Continued movement when doors opened). REM for Rear**
  * Group `3050`
    * `nicht_aktiv` (start=0, mask=00000001b, comment=FH_TUERAUF_STOP_MAUT)

* **ENABLE Rear Tail-light with DRL (8TL). Part 1 of 2. See REM**
  * Group `3060`
    * `TFL_S` (start=31, mask=00110000b)

* **Reduce Automatic Headlamp Sensitivity**
  * Group `3130`
    * `unempfindlich` (start=5, mask=00000111b)

* **Increase Soft Triple Blinker to Five (5) (EXCLUDES P3.61.x)**
  * Group `3060`
    * `04` (start=7, mask=00000111b)

* **ENABLE EU Brake Light Behavior (Blink)**
  * Group `3060`
    * `bremslicht_blinkend` (start=16, mask=00000011b)

* **ENABLE Door Handle LED Lights while in reverse**
  * Group `3070`
    * `aktiv` (start=11, mask=00010000b)

* **ENABLE Fog Lights with High Beams**
  * Group `3060`
    * `nicht_aktiv` (start=20, mask=00100000b)

* **ENABLE Fog Lights with Parking Lights**
  * Group `3060`
    * `aktiv` (start=29, mask=01000000b)

* **Separates Ambient Light Level and Instrument Cluster Light Level**
  * Group `3070`
    * `nicht_aktiv` (start=4, mask=10000000b, comment=AMBIENTE_NACHFUEHRUNG (default : aktiv))

* **Open Windows/Fold Mirrors with Keyfob or CA (Newer I-Step)**
  * Group `3110`
    * `aktiv` (start=8, mask=00000001b, comment=ASP_AUSKLAPPEN_NACH_KOMFORTSCHLIESSEN)
    * `aktiv` (start=1, mask=00000001b, comment=ASP_BEIKLAPPEN_BEI_KOMFORTSCHLIESSEN)
  * Group `3053`
    * `aktiv` (start=0, mask=10000000b, comment=KOMFORTSCHLIESSUNG_FB)
    * `aktiv` (start=0, mask=01000000b, comment=KOMFORTOEFFNUNG_FB)
    * `aktiv` (start=1, mask=00000001b, comment=KOMFORTOEFFNUNG)
    * `aktiv` (start=1, mask=00000010b, comment=KOMFORTSCHLIESSUNG)
    * `aktiv` (start=1, mask=00000100b, comment=KOMFORTSCHLIESSUNG_PA)

* **Open Windows/Fold Mirrors with Keyfob or CA (Older I-Step)**
  * Group `3110`
    * `aktiv` (start=7, mask=00000001b, comment=ASP_AUSKLAPPEN_NACH_KOMFORTSCHLIESSEN)
    * `aktiv` (start=0, mask=10000000b, comment=ASP_BEIKLAPPEN_BEI_KOMFORTSCHLIESSEN)
  * Group `3053`
    * `aktiv` (start=0, mask=10000000b, comment=KOMFORTSCHLIESSUNG_FB)
    * `aktiv` (start=0, mask=01000000b, comment=KOMFORTOEFFNUNG_FB)
    * `aktiv` (start=1, mask=00000001b, comment=KOMFORTOEFFNUNG)
    * `aktiv` (start=1, mask=00000010b, comment=KOMFORTSCHLIESSUNG)
    * `aktiv` (start=1, mask=00000100b, comment=KOMFORTSCHLIESSUNG_PA)

* **Remove open/close window and mirror initiation delay**
  * Group `3053`
    * `00` (start=9, mask=11111111b, comment=KOMFORT_SCHLIESSEN)

* **Removes Trunk Opening Delay - 0 seconds (Older I-Step)**
  * Group `3040`
    * `00` (start=10, mask=11111111b, comment=CLM_TIMEOUT_HK_SMO)

* **Removes Trunk Opening Delay - 0 seconds (Newer I-Step)**
  * Group `3040`
    * `00` (start=6, mask=11111111b, comment=CLM_TIME_DELAY_BOOTLID)

* **Turn off taillight flashing when opening trunk via Comfort Access**
  * Group `3040`
    * `nicht_aktiv` (start=2, mask=00000100b, comment=CLM_SMO_INDICATOR)

* **Turn On LED Fog Lights with Welcome Lights**
  * Group `3063`
    * `01` (start=55, mask=11000000b, comment=MAPPING_NEBELSCHW_L_PART_OF_WL)
    * `01` (start=66, mask=11000000b, comment=MAPPING_NEBELSCHW_R_PART_OF_WL)

* **ENABLE Increased Passenger Mirror Tilt (Curb View) in Reverse (OLD FIRMWARE)**
  * Group `3110`
    * `5A` (start=1, mask=11111111b, comment=ASP_BORDSTEINAUTOMATIK_DELTA)

* **ENABLE Increased Passenger Mirror Tilt (Curb View) in Reverse (P3.61.2)**
  * Group `3110`
    * `5A` (start=2, mask=11111111b, comment=ASP_BORDSTEINAUTOMATIK_DELTA)

* **ENABLE Smart Trunk Closing (Requires 322, 316, and 11-14 Prod Date**
  * Group `3030`
    * `01` (start=5, mask=00000110b, comment=CAM_SMART_CLOSER)

### REM_01 (CAFD 000007A1) — authored by Almaretto | Series: F030

* **ENABLE Rear Tail-light with DRL. Part 2 of 2. See FEM_BODY**
  * Group `3062`
    * `sl_2_l` (start=220, mask=00111111b, comment=Turns On Left Tail-light (Inner Part) on with DRL)
    * `sl_2_r` (start=230, mask=00111111b, comment=Turns On Right Tail-light (Inner Part) on with DRL)
    * `sl_l` (start=200, mask=00111111b, comment=Turns On Left Tail-light (Outer Part) on with DRL)
    * `sl_r` (start=210, mask=00111111b, comment=Turns On Right Tail-light (Outer Part) on with DRL)

* **ENABLE REAR windows roll up while doors opened. FEM for Front**
  * Group `3050`
    * `nicht_aktiv` (start=0, mask=00000001b, comment=FH_TUERAUF_STOP_MAUT)

* **ENABLE Top/Rear camera at any speed. See TRSVC for Side View**
  * Group `3203`
    * `FF` (start=7, mask=11111111b, comment=The speed when it auto disables top camera view)
    * `FF` (start=8, mask=11111111b, comment=The speed when it auto disables rear camera view)
    * `FF` (start=9, mask=11111111b, comment=The distance when it auto disables top camera view)
    * `FF` (start=10, mask=11111111b, comment=The distance when it auto disables rear camera view)

* **ENABLE Outer Light Flashing with EU Brake Force - LED Only**
  * Group `3062`
    * `bl_l` (start=110, mask=00111111b, comment=MAPPING_BRAKEFORCED_L_OUTPUT)
    * `bl_r` (start=120, mask=00111111b, comment=MAPPING_BRAKEFORCED_R_OUTPUT)

* **Increase Outer Light Flashing with EU Brake Force - LED Only**
  * Group `3064`
    * `05` (start=17, mask=00001110b, comment=ESS_BLINKFREQ_1)
    * `05` (start=17, mask=01110000b, comment=ESS_BLINKFREQ_2)

### DSC (CAFD 00001A33) — authored by Almaretto | Series: F080

* **Euro MDM (P3.59.2 Settings): Coding US Spec Cars (F80/F82)**
  * Group `3000`
    * `ECE` (start=12, mask=00000011b, comment=C_Laenderkennung. ONLY Needed Change)
  * Group `3004`
    * `00` (start=14, mask=11110000b, comment=C_AMR_2_c)
    * `00` (start=15, mask=00001111b, comment=C_AMR_3_c)
  * Group `3008`
    * `01` (start=3, mask=00000010b, comment=CTpmsMarket)
    * `00` (start=3, mask=00000010b, comment=CPrewarnENABLE)
    * `00` (start=3, mask=00010000b, comment=CPrewarnIgnition)
    * `50` (start=4, mask=11111111b, comment=MinRcpf)
    * `50` (start=5, mask=11111111b, comment=MinRcpr)
    * `28` (start=6, mask=11111111b, comment=CalLrPDevMax)
    * `50` (start=7, mask=11111111b, comment=CPInitRangeMax)
    * `19` (start=8, mask=11111111b, comment=UiaSetLevelPc)
    * `14` (start=11, mask=11111111b, comment=UiwSetLevelPc)
    * `0C` (start=13, mask=11111111b, comment=UiwSetLevelDistMin)
    * `0A` (start=16, mask=11111111b, comment=CalTimeConfUiw)
    * `0A` (start=17, mask=11111111b, comment=CDtAmbPrewarn)
    * `00` (start=19, mask=11111111b, comment=CTRefShift)

### BDC_01 (CAFD 000017BC) — authored by Almaretto | Series: G011,G030

* **ENABLE Mirrors Fold/Windows Roll Up with CA and KeyFOB. Part 1 of 2. See IDF7**
  * Group `3110`
    * `aktiv` (start=0, mask=00000010b, comment=ASP_AUSKLAPPEN_NACH_KOMFORTSCHLIESSEN)
    * `aktiv` (start=0, mask=00001000b, comment=ASP_BEIKLAPPEN_BEI_KOMFORTSCHLIESSEN)

* **Unlock doors when STOP engine - auto or manual lock**
  * Group `3041`
    * `aktiv` (start=42, mask=00001100b, comment=CLI_DEFAULT_UNLOCK_AFTER_END_OF_DRIVING)

* **Unlock doors when STOP engine - auto lock**
  * Group `3041`
    * `nur_nach_v_verriegeln` (start=42, mask=00001100b, comment=CLI_DEFAULT_UNLOCK_AFTER_END_OF_DRIVING)

* **ENABLE Fog Lights with High Beams**
  * Group `3075`
    * `nicht_aktiv` (start=12, mask=00000001b, comment=NSW_AUS_BEI_FL)

* **ENABLE Fog Lights with Parking Lights and High Beams**
  * Group `3075`
    * `nicht_aktiv` (start=12, mask=00000001b, comment=NSW_AUS_BEI_FL)
    * `aktiv` (start=12, mask=00000010b, comment=NSW_EIN_AUF_LDS_STL)

### BDC_01 (CAFD 00001DF7) — authored by Almaretto | Series: G011,G030

* **ENABLE Front Window Roll Up when doors opened**
  * Group `3510`
    * `nicht_aktiv` (start=0, mask=00000001b, comment=FH_TUERAUF_STOP_MAUT)

* **Allow Rear Window Roll Up when doors opened**
  * Group `3511`
    * `nicht_aktiv` (start=0, mask=00000001b, comment=FH_TUERAUF_STOP_MAUT_REAR)

* **ENABLE Mirrors Fold/Windows Roll Up with CA and KeyFOB. Part 2 of 2. See 17BC**
  * Group `3514`
    * `aktiv` (start=0, mask=01000000b, comment=KOMFORTOEFFNUG_FB)
    * `aktiv` (start=0, mask=10000000b, comment=KOMFORTSCHLIESSUNG_FB)
    * `aktiv` (start=1, mask=00000001b, comment=KOMFORTOEFFNUG)
    * `aktiv` (start=1, mask=00000010b, comment=KOMFORTSCHLIESSUNG)
    * `aktiv` (start=1, mask=00000100b, comment=KOMFORTSCHLIESSUNG_PA)

* **Remove Mirror/Window Initiation Delay with CA and KeyFOB**
  * Group `3514`
    * `00` (start=10, mask=11111111b, comment=KOMFORT_SCHLIESSEN)

### HKFM_2015 (CAFD 00002098) — authored by Almaretto | Series: F015,G001,G011,G030,RR11

* **ENABLE  Trunk or Tailgate CLOSE with KeyFOB or RockerSwitch (No HOLD)**
  * Group `300B`
    * `05` (start=1, mask=11111111b, comment=HKL_REMOTECONTROLLIFTGATEBUTTON_BUTTON_TYPE)
  * Group `3008`
    * `05` (start=1, mask=11111111b, comment=HKL_ROCKERSWITCHPOS1_BUTTON_TYPE)

* **ENABLE Long Press (HOLD) While Close Trunk with RockerSwitch**
  * Group `3008`
    * `01` (start=0, mask=00001000b, comment=HKL_ROCKERSWITCHPOS1_LONGPRESS_CLOSE)

* **DISABLE Long Press (HOLD) While Close Trunk with RockerSwitch**
  * Group `3008`
    * `00` (start=0, mask=00001000b, comment=HKL_ROCKERSWITCHPOS1_LONGPRESS_CLOSE)

* **ENABLE Long Press (HOLD) Close Trunk with KeyFOB**
  * Group `300B`
    * `01` (start=0, mask=00001000b, comment=HKL_REMOTECONTROLLIFTGATEBUTTON_LONGPRESS_CLOSE)

* **DISABLE Long Press (HOLD) Close Trunk with KeyFOB**
  * Group `300B`
    * `00` (start=0, mask=00001000b, comment=HKL_REMOTECONTROLLIFTGATEBUTTON_LONGPRESS_CLOSE)

### HKFM_2015 (CAFD 0000570E) — authored by Almaretto | Series: F015,G001,G011,G030,RR11

* **ENABLE  Trunk or Tailgate CLOSE with KeyFOB or RockerSwitch (No HOLD)**
  * Group `300B`
    * `05` (start=1, mask=11111111b, comment=HKL_REMOTECONTROLLIFTGATEBUTTON_BUTTON_TYPE)
  * Group `3008`
    * `05` (start=1, mask=11111111b, comment=HKL_ROCKERSWITCHPOS1_BUTTON_TYPE)

* **ENABLE Long Press (HOLD) While Close Trunk with RockerSwitch**
  * Group `3008`
    * `01` (start=0, mask=00001000b, comment=HKL_ROCKERSWITCHPOS1_LONGPRESS_CLOSE)

* **DISABLE Long Press (HOLD) While Close Trunk with RockerSwitch**
  * Group `3008`
    * `00` (start=0, mask=00001000b, comment=HKL_ROCKERSWITCHPOS1_LONGPRESS_CLOSE)

* **ENABLE Long Press (HOLD) Close Trunk with KeyFOB**
  * Group `300B`
    * `01` (start=0, mask=00001000b, comment=HKL_REMOTECONTROLLIFTGATEBUTTON_LONGPRESS_CLOSE)

* **DISABLE Long Press (HOLD) Close Trunk with KeyFOB**
  * Group `300B`
    * `00` (start=0, mask=00001000b, comment=HKL_REMOTECONTROLLIFTGATEBUTTON_LONGPRESS_CLOSE)

### HKFM_2015 (CAFD 00005710) — authored by Almaretto | Series: F015,G001,G011,G030,RR11

* **ENABLE  Trunk or Tailgate CLOSE with KeyFOB or RockerSwitch (No HOLD)**
  * Group `300B`
    * `05` (start=1, mask=11111111b, comment=HKL_REMOTECONTROLLIFTGATEBUTTON_BUTTON_TYPE)
  * Group `3008`
    * `05` (start=1, mask=11111111b, comment=HKL_ROCKERSWITCHPOS1_BUTTON_TYPE)

* **ENABLE Long Press (HOLD) While Close Trunk with RockerSwitch**
  * Group `3008`
    * `01` (start=0, mask=00001000b, comment=HKL_ROCKERSWITCHPOS1_LONGPRESS_CLOSE)

* **DISABLE Long Press (HOLD) While Close Trunk with RockerSwitch**
  * Group `3008`
    * `00` (start=0, mask=00001000b, comment=HKL_ROCKERSWITCHPOS1_LONGPRESS_CLOSE)

* **ENABLE Long Press (HOLD) Close Trunk with KeyFOB**
  * Group `300B`
    * `01` (start=0, mask=00001000b, comment=HKL_REMOTECONTROLLIFTGATEBUTTON_LONGPRESS_CLOSE)

* **DISABLE Long Press (HOLD) Close Trunk with KeyFOB**
  * Group `300B`
    * `00` (start=0, mask=00001000b, comment=HKL_REMOTECONTROLLIFTGATEBUTTON_LONGPRESS_CLOSE)

### IHKA_PR01 (CAFD 000022D3) — authored by Almaretto | Series: G011,G030

* **ENABLE HVAC memory - A/C stay OFF if OFF at vehicle shutdown**
  * Group `3003`
    * `aktiv` (start=0, mask=00000001b, comment=OFF_MEMORY)

* **ENABLE Air Re-Circulation memory - Remembers shutdown Setting**
  * Group `3003`
    * `aktiv` (start=0, mask=00000010b, comment=MEMORY_UMLUFT)

* **DISABLE A/C from turning ON if Auto Button is pressed **
  * Group `3003`
    * `nicht_aktiv` (start=0, mask=00000100b, comment=AC_ON_WITH_AUTO)

### ACSM_5 (CAFD 00001B29) — authored by Almaretto | Series: G011,G030

* **DISABLE Seat Belt Status in Cluster (Passenger) - 2016 Firmware**
  * Group `3001`
    * `nicht_aktiv` (start=6, mask=00000001b, comment=Gurtzustandsanzeige_Beifahrer)

* **DISABLE Seat Belt Status in Cluster (Driver) - 2016 Firmware**
  * Group `3001`
    * `nicht_aktiv` (start=5, mask=00000001b, comment=Gurtzustandsanzeige_Fahrer)

* **DISABLE Seat Belt Reminder Chime (Driver) - 2016 Firmware**
  * Group `3001`
    * `nicht_aktiv` (start=1, mask=00000001b, comment=SeatBeltReminder_Fahrer)

* **DISABLE Seat Belt Reminder (Passenger) - 2016 Firmware**
  * Group `3001`
    * `nicht_aktiv` (start=2, mask=00000001b, comment=SeatBeltReminder_Beifahrer)

* **DISABLE Seat Belt Disconnected Reminder Sound (Driver) - 2016 Firmware**
  * Group `3001`
    * `nicht_aktiv` (start=3, mask=00000001b, comment=SBR_PreWarning_Fahrer)

* **DISABLE Seat Belt Disconnected Reminder Sound (Passenger) - 2016 Firmware**
  * Group `3001`
    * `nicht_aktiv` (start=4, mask=00000001b, comment=SBR_PreWarning_Beifahrer)

* **DISABLE Initial Belt Warning Gong - 2016 Firmware**
  * Group `3001`
    * `nicht_aktiv` (start=0, mask=00000001b, comment=Initialwarnung)

### HU_NBT_EVO (CAFD 00001EF6) — authored by Almaretto | Series: F015,F030,G011

* **ENABLE Video in Motion (VIM) - Only ID4 (Any Speed)**
  * Group `3000`
    * `nicht_aktiv` (start=5, mask=00000100b, comment=VIDEO_HANDBRAKE)
    * `nicht_aktiv` (start=5, mask=00010000b, comment=VIDEO_FRONT_LOCKED)
    * `none` (start=2, mask=00000111b, comment=VIDEO_SPEEDLOCK_CONDITION)
    * `nicht_aktiv` (start=146, mask=00011111b, comment=SPEEDLOCK_SPEEDVALUE_MIN)
    * `nicht_aktiv` (start=147, mask=00111111b, comment=SPEEDLOCK_SPEEDVALUE_MAX)
  * Group `3006`
    * `FF` (start=25, mask=11111111b, comment=SPEEDLOCK_X_KMH_MIN)
    * `FF` (start=26, mask=11111111b, comment=SPEEDLOCK_X_KMH_MAX)

* **ENABLE Video in Motion (VIM) - only 1D5 (Up to 63 kph)**
  * Group `3000`
    * `nicht_aktiv` (start=5, mask=00000100b, comment=VIDEO_HANDBRAKE)
    * `nicht_aktiv` (start=5, mask=00010000b, comment=VIDEO_FRONT_LOCKED)
    * `none` (start=2, mask=00000111b, comment=VIDEO_SPEEDLOCK_CONDITION)
    * `1F` (start=146, mask=00011111b, comment=SPEEDLOCK_SPEEDVALUE_MIN)
    * `3F` (start=147, mask=00111111b, comment=SPEEDLOCK_SPEEDVALUE_MAX)
  * Group `3006`
    * `FF` (start=25, mask=11111111b, comment=SPEEDLOCK_X_KMH_MIN)
    * `FF` (start=26, mask=11111111b, comment=SPEEDLOCK_X_KMH_MAX)

* **ENABLE Call Log Timestamp**
  * Group `3003`
    * `aktiv` (start=1, mask=01000000b, comment=TIMESTAMP_DISPLAY)

* **Displays entire text (SMS) message on iDrive**
  * Group `3003`
    * `whole_text` (start=11, mask=00000111b, comment=PIM_Driving_Text_Length)
  * Group `3000`
    * `whole_text` (start=31, mask=00111000b, comment=SPEEDLOCK_TEXT_LENGTH)
    * `whole_text` (start=137, mask=00011100b, comment=MYINFO_DRIVING_TEXT_LENGTH)
    * `whole_text` (start=137, mask=11100000b, comment=AKD_DRIVING_TEXT_LENGTH)
    * `whole_text` (start=138, mask=00000111b, comment=BMWINFO_DRIVING_TEXT_LENGTH)

* **ENABLE HUD Turnsignal. Part 1 of 2. Go to KOMBI. (Excludes 6WB)**
  * Group `300C`
    * `aktiv` (start=0, mask=01000000b, comment=HUD_TURNSIGNAL)

* **DISABLE Lock/Unlock Sound Confirm Checkbox With alarm only**
  * Group `3000`
    * `nicht_aktiv` (start=110, mask=00000001b, comment=Acoustical_lock_confirm)

* **ENABLE Lock/Unlock Sound Confirm Checkbox With alarm only**
  * Group `3000`
    * `aktiv` (start=110, mask=00000001b, comment=Acoustical_lock_confirm)

* **ENABLE Sports Displays - Red/Silver.**
  * Group `3000`
    * `aktiv` (start=133, mask=01000000b, comment=M_VEHICLE)
  * Group `3009`
    * `aktiv` (start=9, mask=00010000b, comment=EFF_DYN_SPORT_UNIT)
    * `aktiv` (start=9, mask=00100000b, comment=EFF_DYN_SPORT_CID)

* **ENABLE Sports Displays - Amber Standard.**
  * Group `3000`
    * `nicht_aktiv` (start=133, mask=01000000b, comment=M_VEHICLE)
  * Group `3009`
    * `aktiv` (start=9, mask=00010000b, comment=EFF_DYN_SPORT_UNIT)
    * `aktiv` (start=9, mask=00100000b, comment=EFF_DYN_SPORT_CID)

* **DISABLE Office/Service Message Function Speed Lock-Out**
  * Group `3000`
    * `none` (start=136, mask=00111000b, comment=OFFICE_MESSAGES_SPEEDLOCK_CONDITION)
    * `none` (start=138, mask=00111000b, comment=SERVICES_MESSAGES_SPEEDLOCK_CONDITION)

* **ENABLE IDrive DRL-selectable menu item (8TN US Typecode)**
  * Group `3000`
    * `standard` (start=92, mask=00011000b, comment=DAYDRIVING_LIGHT)

* **ENABLE British Voice on Navigation. Part 1 of 2. See KOMBI (ID4 ONLY)**
  * Group `3007`
    * `master` (start=0, mask=00001100b, comment=LANGUAGE_ENGLISH_UK)
    * `nicht_aktiv` (start=0, mask=00110000b, comment=LANGUAGE_ENGLISH_US)
  * Group `3006`
    * `nicht_aktiv` (start=0, mask=00000100b, comment=NAVI_DESTINATION_INPUT_US)

* **ENABLE Default Time settings to 24H**
  * Group `3004`
    * `24h` (start=8, mask=00010000b, comment=DEFAULT_ZEIT_EINHEIT)

* **Allows volume to be retained up to 100% rather than startup at 25%**
  * Group `3002`
    * `32` (start=3, mask=11111111b, comment=VOL_MAX_ON)

* **ENABLE Owners Manual in Motion (ID4 ONLY)**
  * Group `3000`
    * `nicht_aktiv` (start=0, mask=00100000b, comment=SL06_IBA_1)
    * `nicht_aktiv` (start=0, mask=01000000b, comment=SL07_IBA_2)
    * `nicht_aktiv` (start=2, mask=00010000b, comment=SL21_IBA_3)

* **ENABLE All Video Codecs and Video Import**
  * Group `3000`
    * `aktiv` (start=15, mask=00010000b, comment=ENT_CODEC_OGG)
    * `aktiv` (start=15, mask=00100000b, comment=ENT_CODEC_XVID)
    * `aktiv` (start=15, mask=01000000b, comment=ENT_CODEC_VCD)
    * `Aktiv` (start=13, mask=00000100b, comment=ENT_MC_VIDEO_SUPPORT)
    * `both` (start=32, mask=00000110b, comment=API_USB_VIDEO)

* **M Performance Start Animation of HMI**
  * Group `3001`
    * `animation` (start=62, mask=00000110b, comment=STARTUP_TYPE)
    * `variant_01` (start=62, mask=01111000b, comment=STARTUP_EMBLEM)

* **DISABLE STARTUP/CAMERA Legal Disclaimers**
  * Group `3001`
    * `00` (start=58, mask=11111111b, comment=LEGAL_DISCLAIMER_TIME)
    * `00` (start=52, mask=11111111b, comment=MACRO_CAM_LEGALDISCLAIMER)
    * `00` (start=53, mask=11111111b, comment=MACRO_NIVICAM_LDISCLAIMER)

* **Show Tire Pressure and Temperature in iDrive**
  * Group `3001`
    * `aktiv` (start=1, mask=00100000b, comment=RDC_SAFETY)
    * `druck_und_temperatur` (start=66, mask=00001100b, comment=RDC_DRUCK_TEMP)

* **ENABLE Trip Import via USB**
  * Group `3006`
    * `aktiv` (start=3, mask=00000001b, comment=navi_trip_import)
    * `aktiv` (start=3, mask=00000100b, comment=navi_dest_import)
    * `aktiv` (start=3, mask=00010000b, comment=navi_mypoi_import)

* **ENABLE Rear Camera Zoom -Trailer Mode-**
  * Group `3001`
    * `Aktiv` (start=54, mask=00000001b, comment=macro_trailer_coupling)

* **ENABLE Transfer of Phone Ringtone to Vehicle (Iphone Only)**
  * Group `3003`
    * `aktiv` (start=6, mask=10000000b, comment=INBAND_RINGING)

* **ENABLE AM Radio on Hybrid Vehicles (F15/I12/I01)**
  * Group `3002`
    * `aktiv` (start=52, mask=00001000b, comment=RADIO_BAND_KW)

* **ENABLE Bluetooth Device and NFC Pairing and Beam Speedlock**
  * Group `3000`
    * `nicht_aktiv` (start=12, mask=00001000b, comment=NFC_BT_PAIRING_SPEEDLOCK)
    * `nicht_aktiv` (start=12, mask=00010000b, comment=NFC_BEAM_SPEEDLOCK)
    * `nicht_aktiv` (start=1, mask=10000000b, comment=SL16_ADD_CEDEVICE)

* **DISABLE Bluetooth Device and NFC Pairing and Beam Speedlock (Untested)**
  * Group `3000`
    * `aktiv` (start=12, mask=00001000b, comment=NFC_BT_PAIRING_SPEEDLOCK)
    * `aktiv` (start=12, mask=00010000b, comment=NFC_BEAM_SPEEDLOCK)
    * `aktiv` (start=1, mask=10000000b, comment=SL16_ADD_CEDEVICE)

* **DISABLE Speller Touchpad Speedlock**
  * Group `3000`
    * `none_locked` (start=31, mask=00000111b, comment=SPEEDLOCK_SPELLER_INPUT)

* **ENABLE MIRACAST Function. See WLAN**
  * Group `3000`
    * `aktiv` (start=6, mask=10000000b, comment=ENT_MIRACAST)
    * `aktiv` (start=13, mask=10000000b, comment=ENT_MC_WLAN_STREAM_DMP)
    * `aktiv` (start=30, mask=00001000b, comment=ENT_MIRACAST_DISPLAY_SETTINGS)
  * Group `3003`
    * `aktiv` (start=21, mask=00000010b, comment=WLAN_WIFI_DIRECT)
    * `aktiv` (start=20, mask=10000000b, comment=WLAN_STATUS)

* **DISABLE MIRACAST Display Settings**
  * Group `3000`
    * `nicht_aktiv` (start=30, mask=00001000b, comment=ENT_MIRACAST_DISPLAY_SETTINGS)

* **ENABLE Album Cover Scale to Full-Size**
  * Group `3000`
    * `aktiv` (start=14, mask=00100000b, comment=ENT_MC_COVER_SCALE)

* **ENABLE Hold-Mode for Range Extender (I001/1012)**
  * Group `3009`
    * `rex` (start=4, mask=01100000b, comment=EV_MENU_AVAILABLE)

* **DISABLE Radio Tuner Speedlock**
  * Group `3000`
    * `00` (start=109, mask=00000001b, comment=SPEEDLOCK_HMI_TUNER)

* **Changes Fueling POI to ONLY CHARGING Station (Default = Petrol + Diesel)**
  * Group `3006`
    * `00` (start=30, mask=00000011b, comment=CAR_TYPE_POI = Charge)

* **Changes Fueling POI to ONLY GAS and Diesel (iDefault = Also Charge Station)**
  * Group `3006`
    * `01` (start=30, mask=00000011b, comment=CAR_TYPE_POI = Petrol + Gas)

* **ENABLE Automatic Time Setting by NAV GPS (Fixes Time Zone Adjustment)**
  * Group `3000`
    * `02` (start=19, mask=00000110b, comment=Default = BMW Online)

* **ENABLE IDrive Configurable Mirror Folding (G12 and G30 Only. Req 11-16 Firmware)**
  * Group `3000`
    * `01` (start=36, mask=10000000b, comment=SETTINGS_AUTOMATIC_EXT_MIRROR_FOLDING)

* **ENABLE 6NW Wireless Charge Forgot Phone Warning Reminder (IDrive Configured. Testing)**
  * Group `3000`
    * `01` (start=23, mask=00001000b, comment=WCA)

* **DISABLE 6NW Wireless Charge Forgot Phone Warning Reminder (IDrive Configured)**
  * Group `3000`
    * `00` (start=23, mask=00001000b, comment=WCA)

* **Change Played Sound Signal Set (BMW)**
  * Group `3002`
    * `00` (start=26, mask=00111000b, comment=SOUND_SIGNAL_SET)

* **Change Played Sound Signal Set (mini)**
  * Group `3002`
    * `01` (start=26, mask=00111000b, comment=SOUND_SIGNAL_SET)

* **Change Played Sound Signal Set (Rolls Royce)**
  * Group `3002`
    * `02` (start=26, mask=00111000b, comment=SOUND_SIGNAL_SET)

* **Change Played Sound Signal Set (BMW_i)**
  * Group `3002`
    * `03` (start=26, mask=00111000b, comment=SOUND_SIGNAL_SET)

### KAFAS3 (CAFD 00002089) — authored by Almaretto | Series: G011

* **ENABLE EU SLI sign (White circle with Red outline)**
  * Group `3010`
    * `00` (start=4, mask=11111111b, comment=COUNTRY_CODING_DISPLAY)

### HU_MGU (CAFD 00003E52) — authored by Almaretto | Series: G005, G007, G020, G015, G030, G011

* **ENABLE Auto Speed Limit Assist (aSLA). Req ID7 and 11-20 I-Step. See 7083, SAS3 42C1, DSC 3D14 (2/4)**
  * Group `300A`
    * `01` (start=10, mask=10000000b, comment=STRECKENVERLAUF - gen_01)
    * `01` (start=13, mask=00001100b, comment=VORAUSSCHAU - gen_01)
    * `01` (start=14, mask=00110000b, comment=SLAAUTOMATISCH - gen_01)
    * `01` (start=14, mask=11000000b, comment=VOFFSET - gen_1)
    * `01` (start=15, mask=11000000b, comment=VOFFSET_LANGSAM - gen_1)
    * `01` (start=18, mask=00000011b, comment=STRECKENVERLAUF_GENERATION - gen_1)

* **DISABLE Auto Speed Limit Assist (aSLA). See 7083, SAS3 42C1, DSC 3D14 (2/4)**
  * Group `300A`
    * `01` (start=10, mask=10000000b, comment=STRECKENVERLAUF - gen_01)
    * `00` (start=13, mask=00001100b, comment=VORAUSSCHAU - gen_01)
    * `00` (start=14, mask=00110000b, comment=SLAAUTOMATISCH - gen_01)
    * `00` (start=14, mask=11000000b, comment=VOFFSET - gen_1)
    * `00` (start=15, mask=11000000b, comment=VOFFSET_LANGSAM - gen_1)
    * `01` (start=18, mask=00000011b, comment=STRECKENVERLAUF_GENERATION - gen_1)

* **ENABLE Traffic Light Assistant (TLA). Req ID7, 11-20 I-Step, and aSLA. See 7083, SAS3 42C1, DSC 3D14 (2/4)**
  * Group `300A`
    * `01` (start=16, mask=01100000b, comment=AMPELN - gen_01)
    * `01` (start=17, mask=00110000b, comment=AMPELASSISTENT - gen_01)
    * `01` (start=17, mask=11000000b, comment=ANFAHRERINNERUNG - gen_01)

* **DISABLE Traffic Light Assistant (TLA). See 7083, SAS3 42C1, DSC 3D14 (2/4)**
  * Group `300A`
    * `00` (start=16, mask=01100000b, comment=AMPELN - gen_01)
    * `00` (start=17, mask=00110000b, comment=AMPELASSISTENT - gen_01)
    * `00` (start=17, mask=11000000b, comment=ANFAHRERINNERUNG - gen_01)

* **ENABLE Driver Assistant Pro (DAP) - New Features. See BDC, SAS3 (2/3)**
  * Group `300A`
    * `01` (start=14, mask=00000011b, comment=EINSEITIGVORBEIFAHREN - Undertaking gen_1)
    * `01` (start=19, mask=00000100b, comment=RETTUNGSGASSE - Emergency Lane Formation aktiv)
    * `01` (start=16, mask=00000110b, comment=SITUATIVERABSTAND - Adjust Distance Menu gen_1)

* **DISABLE Driver Assistant Pro (DAP) - New Features. See BDC, SAS3 (2/3)**
  * Group `300A`
    * `00` (start=14, mask=00000011b, comment=EINSEITIGVORBEIFAHREN - Undertaking gen_1)
    * `00` (start=19, mask=00000100b, comment=RETTUNGSGASSE - Emergency Lane Formation aktiv)
    * `01` (start=16, mask=00000110b, comment=SITUATIVERABSTAND - Adjust Distance Menu gen_1)

### SAS3 (CAFD 000042C1) — authored by Almaretto | Series: G005, G007, G020, G015, G030, G011

* **ENABLE Auto Speed Limit Assist (aSLA). Req ID7 and 11-20 I-Step. See 7083, MGU, DSC 3D14 (3/4)**
  * Group `3001`
    * `01` (start=167, mask=11111111b, comment=C_SLA_Anzeige_Zusatztexte - Nr001_aktiviert)
  * Group `3000`
    * `02` (start=93, mask=11111111b, comment=C_SLA_Streckenregelung_vorhanden - NR_002_vorhanden_SLA_entkoppelt)
    * `FF, FF, FF, FF` (start=112, end=115, mask=11111111b, comment=C_SLA_aSLA_Land_Aktiv - 0xFFFFFFFF)
    * `FF, FF, FF, FF` (start=116, end=119, mask=11111111b, comment=C_SLA_Vorausschau_Land_Aktiv - 0xFFFFFFFF)
    * `01` (start=130, mask=11111111b, comment=C_SLA_aSLA_vorhanden - Nr001_vorhanden)
    * `FF, FF, FF, FF` (start=131, end=134, mask=11111111b, comment=C_SLA_Streckenregelung_Land_Aktiv - 0xFFFFFFFF)

* **DISABLE Auto Speed Limit Assist (aSLA). See 7083, MGU, DSC 3D14 (3/4)**
  * Group `3001`
    * `01` (start=167, mask=11111111b, comment=C_SLA_Anzeige_Zusatztexte - Nr001_aktiviert)
  * Group `3000`
    * `02` (start=93, mask=11111111b, comment=C_SLA_Streckenregelung_vorhanden - NR_002_vorhanden_SLA_entkoppelt)
    * `F9, 0F, 86, 00` (start=112, end=115, mask=11111111b, comment=C_SLA_aSLA_Land_Aktiv - 0xFFFFFFFF)
    * `FB, DF, A7, C0` (start=116, end=119, mask=11111111b, comment=C_SLA_Vorausschau_Land_Aktiv - 0xFFFFFFFF)
    * `00` (start=130, mask=11111111b, comment=C_SLA_aSLA_vorhanden - Nr001_vorhanden)
    * `FF, CF, 9F, F8` (start=131, end=134, mask=11111111b, comment=C_SLA_Streckenregelung_Land_Aktiv - 0xFFFFFFFF)

* **ENABLE Traffic Light Assistant (TLA). Req ID7, 11-20 I-Step, and aSLA. See 7083, MGU, DSC 3D14 (3/4)**
  * Group `3000`
    * `01` (start=178, mask=11111111b, comment=C_UCC_vorhanden - Nr001_vorhanden)
    * `FF, FF, FF, FF` (start=179, end=182, mask=11111111b, comment=C_SLA_UCC_Land_aktiv - 0xFFFFFFFF)
    * `FF, FF, FF, FF` (start=188, end=191, mask=11111111b, comment=C_SLA_aUCC_Land_aktiv - 0xFFFFFFFF)

* **DISABLE Traffic Light Assistant (TLA). See 7083, MGU, DSC 3D14 (3/4)**
  * Group `3000`
    * `00` (start=178, mask=11111111b, comment=C_UCC_vorhanden - Nr000_nicht_vorhanden)
    * `08, 00, 00, 00` (start=179, end=182, mask=11111111b, comment=C_SLA_UCC_Land_aktiv - 0xFFFFFFFF)
    * `08, 00, 00, 00` (start=188, end=191, mask=11111111b, comment=C_SLA_aUCC_Land_aktiv - 0xFFFFFFFF)

* **ENABLE Driver Assistant Pro (DAP) - Unsupported Highway Exit Assistant. See BDC, MGU (3/3)**
  * Group `3000`
    * `00` (start=183, mask=11111111b, comment=C_QmaN_Vorhanden - nr001_vorhanden)
    * `FA, C3, 81, F8` (start=184, end=187, mask=11111111b, comment=C_SLA_QmaN_Land_aktiv - FFFFFFFF)

* **DISABLE Driver Assistant Pro (DAP) - Unsupported Highway Exit Assistant. See BDC, MGU (3/3)**
  * Group `3000`
    * `00` (start=183, mask=11111111b, comment=C_QmaN_Vorhanden - nr001_vorhanden)
    * `FA, C3, 81, F8` (start=184, end=187, mask=11111111b, comment=C_SLA_QmaN_Land_aktiv - FFFFFFFF)

* **ENABLE Driver Assistant Pro (DAP) - Option to form emergency lane. See BDC, MGU (3/3)**
  * Group `3000`
    * `01` (start=192, mask=11111111b, comment=C_RGA_Funktion - Nr001_aktiviert)
    * `FF, FF, FF, FF` (start=193, end=196, mask=11111111b, comment=C_RGA_Land_aktiv - FFFFFFFF)
    * `FF, FF, FF, FF` (start=197, end=200, mask=11111111b, comment=C_RGA_Seitenwahl_links_Land_aktiv - FFFFFFFF)

* **DISABLE Driver Assistant Pro (DAP) - Option to form emergency lane. See BDC, MGU (3/3)**
  * Group `3000`
    * `00` (start=192, mask=11111111b, comment=C_RGA_Funktion - Nr001_aktiviert)
    * `88, 88, 01, 70` (start=193, end=196, mask=11111111b, comment=C_RGA_Land_aktiv - FFFFFFFF)
    * `88, 88, 01, 70` (start=197, end=200, mask=11111111b, comment=C_RGA_Seitenwahl_links_Land_aktiv - FFFFFFFF)

* **ENABLE Driver Assistant Pro (DAP) - Undertaking. See BDC, MGU (3/3)**
  * Group `3001`
    * `01` (start=160, mask=11111111b, comment=C_Rechtsueberholen_verbieten - Nr001_aktiviert)

* **DISABLE Driver Assistant Pro (DAP) - Undertaking. See BDC, MGU (3/3)**
  * Group `3001`
    * `00` (start=160, mask=11111111b, comment=C_Rechtsueberholen_verbieten - Nr000_deaktiviert)

### DSC_VIP (CAFD 00003D14) — authored by Almaretto | Series: G005, G007, G020, G015, G011

* **ENABLE Speed Limit Assist (aSLA). Req ID7 and 11-20 I-Step. See 7083, MGU, DSC 3D14 (4/4)**
  * Group `3020`
    * `FF, FF, FF, FF` (start=111, end=114, mask=11111111b, comment=C_SLA_aSLA_Land_Aktiv - 0xFFFFFFFF)
    * `01` (start=117, mask=11111111b, comment=C_SLA_aSLA_vorhanden - Nr001_vorhanden)
    * `01` (start=144, mask=11111111b, comment=C_SLA_Anzeige_Zusatztexte - Nr001_aktiviert)
    * `FF, FF, FF, FF` (start=210, end=213, mask=11111111b, comment=C_SLA_Vorausschau_Land_Aktiv - 0xFFFFFFFF)
    * `02` (start=215, mask=11111111b, comment=C_SLA_Streckenregelung_vorhanden - NR_002_vorhanden_SLA_entkoppelt)
    * `FF, FF, FF, FF` (start=216, end=219, mask=11111111b, comment=C_SLA_Streckenregelung_Land_Aktiv - 0xFFFFFFFF)

* **DISABLE Speed Limit Assist (aSLA). See 7083, MGU, DSC 3D14 (4/4)**
  * Group `3020`
    * `F9, 0F, 86, 00` (start=111, end=114, mask=11111111b, comment=C_SLA_aSLA_Land_Aktiv - 0xFFFFFFFF)
    * `00` (start=117, mask=11111111b, comment=C_SLA_aSLA_vorhanden - Nr001_vorhanden)
    * `01` (start=144, mask=11111111b, comment=C_SLA_Anzeige_Zusatztexte - Nr001_aktiviert)
    * `FB, DF, AF, C0` (start=210, end=213, mask=11111111b, comment=C_SLA_Vorausschau_Land_Aktiv - 0xFFFFFFFF)
    * `00` (start=215, mask=11111111b, comment=C_SLA_Streckenregelung_vorhanden - NR_002_vorhanden_SLA_entkoppelt)
    * `F9, 0F, 86, 00` (start=216, end=219, mask=11111111b, comment=C_SLA_Streckenregelung_Land_Aktiv - 0xFFFFFFFF)

* **ENABLE Traffic Light Assistant (TLA). Req ID7, 11-20 I-Step, and aSLA. See 7083, MGU, DSC 3D14 (4/4)**
  * Group `3020`
    * `FF, FF, FF, FF` (start=179, end=182, mask=11111111b, comment=C_SLA_UCC_Land_aktiv - 0xFFFFFFFF)

* **DISABLE Traffic Light Assistant (TLA). See 7083, MGU, DSC 3D14 (4/4)**
  * Group `3020`
    * `00, 00, 00, 00` (start=179, end=182, mask=11111111b, comment=C_SLA_UCC_Land_aktiv - Nr000_Bausteinpartitionierung)

### DSC_VIP (CAFD 00003D78) — authored by Almaretto | Series: G005, G007, G020

* **ENABLE Speed Limit Assist (aSLA). Req ID7 and 11-20 I-Step. See 7083, MGU, DSC 3D14 (4/4)**
  * Group `3020`
    * `FF, FF, FF, FF` (start=111, end=114, mask=11111111b, comment=C_SLA_aSLA_Land_Aktiv - 0xFFFFFFFF)
    * `01` (start=117, mask=11111111b, comment=C_SLA_aSLA_vorhanden - Nr001_vorhanden)
    * `01` (start=144, mask=11111111b, comment=C_SLA_Anzeige_Zusatztexte - Nr001_aktiviert)
    * `FF, FF, FF, FF` (start=210, end=213, mask=11111111b, comment=C_SLA_Vorausschau_Land_Aktiv - 0xFFFFFFFF)
    * `02` (start=215, mask=11111111b, comment=C_SLA_Streckenregelung_vorhanden - NR_002_vorhanden_SLA_entkoppelt)
    * `FF, FF, FF, FF` (start=216, end=219, mask=11111111b, comment=C_SLA_Streckenregelung_Land_Aktiv - 0xFFFFFFFF)

* **DISABLE Speed Limit Assist (aSLA). See 7083, MGU, DSC 3D14 (4/4)**
  * Group `3020`
    * `F9, 0F, 86, 00` (start=111, end=114, mask=11111111b, comment=C_SLA_aSLA_Land_Aktiv - 0xFFFFFFFF)
    * `00` (start=117, mask=11111111b, comment=C_SLA_aSLA_vorhanden - Nr001_vorhanden)
    * `01` (start=144, mask=11111111b, comment=C_SLA_Anzeige_Zusatztexte - Nr001_aktiviert)
    * `FB, DF, AF, C0` (start=210, end=213, mask=11111111b, comment=C_SLA_Vorausschau_Land_Aktiv - 0xFFFFFFFF)
    * `00` (start=215, mask=11111111b, comment=C_SLA_Streckenregelung_vorhanden - NR_002_vorhanden_SLA_entkoppelt)
    * `F9, 0F, 86, 00` (start=216, end=219, mask=11111111b, comment=C_SLA_Streckenregelung_Land_Aktiv - 0xFFFFFFFF)

* **ENABLE Traffic Light Assistant (TLA). Req ID7, 11-20 I-Step, and aSLA. See 7083, MGU, DSC 3D14 (4/4)**
  * Group `3020`
    * `FF, FF, FF, FF` (start=179, end=182, mask=11111111b, comment=C_SLA_UCC_Land_aktiv - 0xFFFFFFFF)

* **DISABLE Traffic Light Assistant (TLA). See 7083, MGU, DSC 3D14 (4/4)**
  * Group `3020`
    * `00, 00, 00, 00` (start=179, end=182, mask=11111111b, comment=C_SLA_UCC_Land_aktiv - Nr000_Bausteinpartitionierung)


## `Botho.xml`

**Modules touched:** ACSM_4B (CAFD 00000911, author Botho (public), series F020,F030), GKEB23 (CAFD 0000023F, author Botho (public), series F020,F030), FEM_01 (CAFD 00000794, author Botho (public), series F020,F030), FZD__07 (CAFD 00000A07, author Botho (public), series F020,F030), ICMQL (CAFD 0000067B, author Botho (public), series F020,F030), IHKA_VA02 (CAFD 000016EE, author Botho (public), series F020,F030), KAFAS2 (CAFD 00001148, author Botho (public), series F020,F030), HKFM (CAFD 000007C8, author Botho (public), series F020,F030), HU_NBT (CAFD 00000DED, author Botho (public), series F020,F030), KOMBI L7_MID (CAFD 000009C8, author Botho (public), series F020,F030), REM_01 (CAFD 000007A1, author Botho (public), series F020,F030), CFAS_PLX_1 (CAFD 000000B5, author Botho (public), series F020,F030), TRSVC (CAFD 00000223, author Botho (public), series F020,F030)

### ACSM_4B (CAFD 00000911) — authored by Botho (public) | Series: F020,F030

* **Seat belt: reminder duration set to 10s (default: 100s)**
  * Group `3001`
    * `0A` (start=3, mask=11111111b, comment=GWF_SBR_WARNDAUER (default: 64))

* **Seat belt: disable reminder chime**
  * Group `3000`
    * `nicht_aktiv` (start=15, mask=00000100b, comment=SeatBeltReminder_SBR_Fahrer (default: aktiv))
    * `nicht_aktiv` (start=15, mask=00000010b, comment=SeatBeltReminder_SBR_Beifahrer (default: aktiv))

* **Seat belt: disable indicator in instrument cluster**
  * Group `3000`
    * `nicht_aktiv` (start=15, mask=00010000b, comment=Gurtzustandsanzeige_Fahrer_GWF_GZA_FA (default: aktiv))
    * `nicht_aktiv` (start=15, mask=00001000b, comment=Gurtzustandsanzeige_Beifahrer_GWF_GZA_BF (default: aktiv))

* **Seat belt: disable chime when belt is unlatched**
  * Group `3000`
    * `nicht_aktiv` (start=16, mask=00000001b, comment=SBR_PreWarning_Fahrer (default: aktiv))
    * `nicht_aktiv` (start=16, mask=00000010b, comment=SBR_PreWarning_Beifahrer (default: aktiv))

### GKEB23 (CAFD 0000023F) — authored by Botho (public) | Series: F020,F030

* **Activation Launch Control (default: aktiv)**
  * Group `3000`
    * `01` (start=1, mask=10000000b, comment=LC (default: 01))

### FEM_01 (CAFD 00000794) — authored by Botho (public) | Series: F020,F030

* **Vitres avant: actives lors de l'ouverture des portes avant**
  * Group `3050`
    * `nicht_aktiv` (start=0, mask=00000001b, comment=FH_TUERAUF_STOP_MAUT (default: aktiv))

* **Comfort access: auto-lock delay to 30s without door action (default: 120s)**
  * Group `3040`
    * `03` (start=7, mask=11111111b, comment=CLM_TIME_PIA_LOCK_AT_TIMEOUT (default: 0C))

* **Comfort access: enable panic alarm and set remote hold time to 500ms (SHORT=Follow-Me-Home; MID=Trunk; LONG=Panic Alarm)**
  * Group `30D0`
    * `aktiv` (start=2, mask=00000100b, comment=RC_PANIC_ALARM (default: nicht_aktiv))
    * `04` (start=3, mask=00001111b, comment=RC_DEFAULT_IDG_3RD_BUTTON_SHORT (default: 00))
    * `02` (start=3, mask=11110000b, comment=RC_DEFAULT_IDG_3RD_BUTTON_MID (default: 02))
    * `03` (start=4, mask=00001111b, comment=RC_DEFAULT_IDG_3RD_BUTTON_LONG (default: 02))
    * `14` (start=8, mask=11111111b, comment=RC_TIME_DELAY_BOOTLID (default: 05))
    * `28` (start=9, mask=11111111b, comment=RC_TIME_DELAY_PANIC (default: 14))

* **Comfort access: open flash count = 3 (default: 2)**
  * Group `3060`
    * `03` (start=6, mask=00001100b, comment=QUITTBLK_ENTSCHAERFEN_ANZAHL (default: 02))

* **Comfort access: close flash count = 2 (default: 1)**
  * Group `3060`
    * `02` (start=6, mask=00000011b, comment=QUITTBLK_SICHERN_ANZAHL (default: 01))

* **Comfort access: enable comfort closing after 1s (default: 1.5s)**
  * Group `3053`
    * `0A` (start=9, mask=11111111b, comment=KOMFORT_SCHLIESSEN (default: 0F))

* **Comfort access: enable comfort opening after 2s (default: 2.5s)**
  * Group `3053`
    * `14` (start=8, mask=11111111b, comment=KOMFORT_OEFFNEN (default: 19))

* **Comfort access: close trunk with foot (requires 322, 316) (step 1 of 2 - see HKFM)**
  * Group `3030`
    * `aktiv` (start=5, mask=00000110b, comment=CAM_SMART_CLOSER (default: aktiv si production date après 0315))

* **Comfort access: trunk opening delay (smart opening only) to 0.3s (default 0.7s)**
  * Group `3040`
    * `wert_02` (start=12, mask=11111111b, comment=CLM_TIMEOUT_HK_SMO (default: wert_03))

* **Comfort access: trunk opening delay (no smart opening) to 0.1s (default 0.3s)**
  * Group `3040`
    * `wert_01` (start=6, mask=11111111b, comment=CLM_TIME_DELAY_BOOTLID (default: wert_02))

* **Comfort access: disable turn signals when opening trunk (default: enabled)**
  * Group `3040`
    * `nicht_aktiv` (start=2, mask=00000100b, comment=CLM_SMO_INDICATOR (default: aktiv))

* **Door locking: speed threshold to 8 km/h (only if auto-lock enabled - default 16 km/h)**
  * Group `3040`
    * `wert_03` (start=8, mask=11111111b, comment=CLM_SPEED_LIMIT_PIA_AUTO_LOCK (default: wert_04))

* **Unlock doors when engine stops (only if auto-lock enabled)**
  * Group `3040`
    * `aktiv` (start=1, mask=00000010b, comment=CLM_UNLOCK_KL15OFF_AFTER_PIA_AUTO_LOCK (default: aktiv))

* **Angel Eyes (DRL): Activation des feux de jour (Step 1 sur 3 - voir HU-NBT and REM)**
  * Group `3060`
    * `02` (start=31, mask=00110000b, comment=TFL_MODUS (default: 02))

* **Angel Eyes (DRL): set DRL brightness to 50% when xenons are on**
  * Group `3062`
    * `32` (start=46, mask=11111111b, comment=MAPPING_STANDL_V_L_PWM_LEVEL_STANDARD (default: 8))
    * `32` (start=57, mask=11111111b, comment=MAPPING_STANDL_V_R_PWM_LEVEL_STANDARD (default: 8))

* **Angel Eyes (DRL): set DRL brightness to 100% when xenons are on**
  * Group `3062`
    * `64` (start=46, mask=11111111b, comment=MAPPING_STANDL_V_L_PWM_LEVEL_STANDARD (default: 8))
    * `64` (start=57, mask=11111111b, comment=MAPPING_STANDL_V_R_PWM_LEVEL_STANDARD (default: 8))

* **Angel Eyes (DRL): set DRL brightness to 50% when DRLs are on**
  * Group `3062`
    * `32` (start=90, mask=11111111b, comment=MAPPING_TAGFAHRL_V_L_PWM_LEVEL_1 (default: 64))
    * `32` (start=101, mask=11111111b, comment=MAPPING_TAGFAHRL_V_R_PWM_LEVEL_1 (default: 64))

* **Angel Eyes (DRL): set DRL brightness to 100% when DRLs are on**
  * Group `3062`
    * `64` (start=90, mask=11111111b, comment=MAPPING_TAGFAHRL_V_L_PWM_LEVEL_1 (default: 64))
    * `64` (start=101, mask=11111111b, comment=MAPPING_TAGFAHRL_V_R_PWM_LEVEL_1 (default: 64))

* **Xenon: enable cornering lights (fog lights required)**
  * Group `3073`
    * `01` (start=218, mask=00000010b, comment=C_CLC_ENA (default: 01))
    * `01` (start=66, mask=00000001b, comment=C_BLC_ENA (default: 01))
  * Group `3066`
    * `01` (start=0, mask=00000001b, comment=KL_ENABLE_LI (default: 01))
    * `01` (start=80, mask=00000001b, comment=KL_ENABLE_RE (default: 01))
  * Group `3062`
    * `0B` (start=110, mask=00111111b, comment=MAPPING_ABBIEGEL_L_OUTPUT (default: 0B))
    * `0C` (start=121, mask=00111111b, comment=MAPPING_ABBIEGEL_R_OUTPUT (default: 0C))

* **Xenon: enable US daytime running sidemarkers**
  * Group `3063`
    * `fra_v_l` (start=11, mask=00111111b, comment=MAPPING_SIDEMARKER_L_OUTPUT (default: off))
    * `fra_v_r` (start=22, mask=00111111b, comment=MAPPING_SIDEMARKER_R_OUTPUT (default: off))
    * `04` (start=12, mask=00011111b, comment=MAPPING_SIDEMARKER_L_FUNCTION (default: 01))
    * `04` (start=23, mask=00011111b, comment=MAPPING_SIDEMARKER_R_FUNCTION (default: 01))
    * `8.2V` (start=13, mask=11111111b, comment=MAPPING_SIDEMARKER_L_PWM_LEVEL_STANDARD (default: off))
    * `8.2V` (start=24, mask=11111111b, comment=MAPPING_SIDEMARKER_R_PWM_LEVEL_STANDARD (default: off))

* **Front light cleaning (Disable)**
  * Group `3080`
    * `nicht_aktiv` (start=8, mask=00000001b, comment=WW_SCHEINWERFERREINIGUNG (default: aktiv))

* **Front light cleaning (Enable - Default)**
  * Group `3080`
    * `aktiv` (start=8, mask=00000001b, comment=WW_SCHEINWERFERREINIGUNG (default: aktiv))

* **Front light cleaning: Sprays number (2 - Default)**
  * Group `3080`
    * `02` (start=8, mask=00011000b, comment=WW_ANZAHL_SPRITZIMPULSE_SRA (default: 02))

* **Front light cleaning: Sprays number (3)**
  * Group `3080`
    * `03` (start=8, mask=00011000b, comment=WW_ANZAHL_SPRITZIMPULSE_SRA (default: 02))

* **Front light cleaning: Wash cycles to enable next washing (10 - Default)**
  * Group `3080`
    * `0A` (start=2, mask=00011110b, comment=WW_ANZAHL_WASCHBET_ZUR_SRA (default: 0A))

* **Front light cleaning: Wash cycles to enable next washing (5)**
  * Group `3080`
    * `05` (start=2, mask=00011110b, comment=WW_ANZAHL_WASCHBET_ZUR_SRA (default: 0A))

* **Front light cleaning: Time to wait before next washing (10 mins - Default)**
  * Group `3080`
    * `0A` (start=10, mask=00001111b, comment=WW_SRA_SPERRZEIT (default: 0A))

* **Front light cleaning: Time to wait before next washing (3 mins)**
  * Group `3080`
    * `03` (start=10, mask=00001111b, comment=WW_SRA_SPERRZEIT (default: 0A))

* **Front light cleaning: Time to wait before next washing (5 mins)**
  * Group `3080`
    * `05` (start=10, mask=00001111b, comment=WW_SRA_SPERRZEIT (default: 0A))

* **Automatic rear wiper in reverse (Enable - Default)**
  * Group `3080`
    * `aktiv` (start=0, mask=10000000b, comment=WW_HECKWISCHER_EIN_RUECKWGANG (default: aktiv))

* **Automatic rear wiper in reverse (Disable)**
  * Group `3080`
    * `nicht_aktiv` (start=0, mask=10000000b, comment=WW_HECKWISCHER_EIN_RUECKWGANG (default: aktiv))

* **Rear wiper: Wipe cycles after washing (1)**
  * Group `3080`
    * `01` (start=8, mask=11100000b, comment=WW_ANZAHL_NACHWISCHZ_HECK (default: 02))

* **Rear wiper: Wipe cycles after washing (2 - Default)**
  * Group `3080`
    * `02` (start=8, mask=11100000b, comment=WW_ANZAHL_NACHWISCHZ_HECK (default: 02))

* **Rear wiper: Wipe cycles after washing (3)**
  * Group `3080`
    * `03` (start=8, mask=11100000b, comment=WW_ANZAHL_NACHWISCHZ_HECK (default: 02))

* **Rear wiper: Wipe cycles after washing (4)**
  * Group `3080`
    * `04` (start=8, mask=11100000b, comment=WW_ANZAHL_NACHWISCHZ_HECK (default: 02))

* **Front wiper: Wipe cycles after rear washing (1)**
  * Group `3080`
    * `01` (start=18, mask=01110000b, comment=WW_ANZAHL_NACHWISCHZ_FRONT (default: 03))

* **Front wiper: Wipe cycles after rear washing (2)**
  * Group `3080`
    * `02` (start=18, mask=01110000b, comment=WW_ANZAHL_NACHWISCHZ_FRONT (default: 03))

* **Front wiper: Wipe cycles after washing (3 - Default)**
  * Group `3080`
    * `03` (start=18, mask=01110000b, comment=WW_ANZAHL_NACHWISCHZ_FRONT (default: 03))

* **Front wiper: Wipe cycles after rear washing (4)**
  * Group `3080`
    * `04` (start=18, mask=01110000b, comment=WW_ANZAHL_NACHWISCHZ_FRONT (default: 03))

* **Mirrors: allow folding below 49 km/h (default: 20 km/h)**
  * Group `3110`
    * `31` (start=9, mask=11111111b, comment=ASP_MAX_GESCHWINDIGKEIT_BEIKLAPPEN (default: 14))

* **Mirrors: auto unfold from 50 km/h (default: 40 km/h)**
  * Group `3110`
    * `32` (start=10, mask=11111111b, comment=ASP_GESCHWINDIGKEIT_AUTO_AUSKLAPPEN (default: 28))

* **Passenger mirror: increase reverse tilt to 70 digits (default: 59 digits - I-Step after 3.61.x)**
  * Group `3110`
    * `46` (start=2, mask=11111111b, comment=ASP_BORDSTEINAUTOMATIK_DELTA (default: 3B))

* **Passenger mirror: restore reverse tilt to 59 digits (default: 59 digits - I-Step after 3.61.x)**
  * Group `3110`
    * `3B` (start=2, mask=11111111b, comment=ASP_BORDSTEINAUTOMATIK_DELTA (default: 3B))

* **Turn signals: set flash count to 5 (default: 00 - I-Step before 3.61.x)**
  * Group `3060`
    * `04` (start=7, mask=00000111b, comment=BLINKZYKLEN_ANZAHL_TIPP (default: 00))

* **-- Don't work -- Turn signals: set flash count to 5 (00 = 1, 01 = 3, 02 = 5; default: 01 - I-Step after 3.61.x)**
  * Group `3064`
    * `02` (start=215, mask=00000001b, comment=PIA_DEFAULT_TIPPBLINKEN (default: 01))

* **Turn signals: single flash when opening tailgate (default: double)**
  * Group `3060`
    * `00` (start=6, mask=10000000b, comment=HECKKLAPPE_REVERSIEREN_BLINKEN (default: 01))

* **Rear fog lights: activation (step 2 of 2 - see REM_01)**
  * Group `3060`
    * `01` (start=7, mask=00001000b, comment=NSL_VERBAUT (default: 01))

* **Rear fog lights: deactivation (step 2 of 2 - see REM_01)**
  * Group `3060`
    * `00` (start=7, mask=00001000b, comment=NSL_VERBAUT (default: 01))

* **Fog lights: allow fogs to stay on with high beams**
  * Group `3060`
    * `00` (start=20, mask=00100000b, comment=NSW_AUS_BEI_FL (default: 00))

* **Fog lights: allow fogs to stay on with parking lights**
  * Group `3060`
    * `01` (start=29, mask=01000000b, comment=NSW_EIN_AUF_LDS_STL (default: 00 dans certains pays comme les USA))

* **Feux anti-brouillard: active cornering lights**
  * Group `3073`
    * `F020_enable` (start=218, mask=00000010b, comment=C_CLC_ENA (default: F020_enable))
    * `F020_enable` (start=66, mask=00000001b, comment=C_BLC_ENA (default: F020_enable))
  * Group `3066`
    * `KL_Ein` (start=0, mask=00000001b, comment=KL_ENABLE_LI (default: KL_Ein))
    * `KL_Ein` (start=80, mask=00000001b, comment=KL_ENABLE_RE (default: KL_Ein))
  * Group `3062`
    * `nsw_l` (start=110, mask=00111111b, comment=MAPPING_ABBIEGEL_L_OUTPUT (default: nsw_l))
    * `nsw_r` (start=121, mask=00111111b, comment=MAPPING_ABBIEGEL_R_OUTPUT (default: nsw_r))

* **High-Beam Assistant motorway (HBA): activate immediately from 120 km/h (default: 140 km/h) or between 90-110 km/h for 15s (default: 30s)**
  * Group `3074`
    * `5A` (start=5, mask=11111111b, comment=C_HBA_HGWY_V_LO (default: 5A - 90 km/h))
    * `82` (start=6, mask=11111111b, comment=C_HBA_HGWY_V_HI (default: 8C - 140 km/h))
    * `6E` (start=7, mask=11111111b, comment=C_HBA_HGWY_V_MIN (default: 6E - 110 km/h))
    * `0F` (start=8, mask=11111111b, comment=C_HBA_HGWY_T_MIN (default: 1E - 30 sec))

* **High-Beam Assistant motorway (HBA): activate immediately from 140 km/h or between 90-110 km/h for 30s (default)**
  * Group `3074`
    * `5A` (start=5, mask=11111111b, comment=C_HBA_HGWY_V_LO (default: 5A - 90 km/h))
    * `8C` (start=6, mask=11111111b, comment=C_HBA_HGWY_V_HI (default: 8C - 140 km/h))
    * `6E` (start=7, mask=11111111b, comment=C_HBA_HGWY_V_MIN (default: 6E - 110 km/h))
    * `1E` (start=8, mask=11111111b, comment=C_HBA_HGWY_T_MIN (default: 1E - 30 sec))

* **High-Beam Assistant (HBA): anti-glare tunnel activate at 50 km/h and deactivate at 45 km/h (default: 70-60 km/h)**
  * Group `3074`
    * `2D` (start=0, mask=11111111b, comment=C_HBA_ENA_V_LO (default: 3C - 60 km/h))
    * `32` (start=1, mask=11111111b, comment=C_HBA_ENA_V_HI (default: 46 - 70 km/h))

* **High-Beam Assistant (HBA): anti-glare tunnel activate at 70 km/h and deactivate at 60 km/h (default)**
  * Group `3074`
    * `3C` (start=0, mask=11111111b, comment=C_HBA_ENA_V_LO (default: 3C - 60 km/h))
    * `46` (start=1, mask=11111111b, comment=C_HBA_ENA_V_HI (default: 46 - 70 km/h))

* **High-Beam Assistant (HBA): activate via light switch to the right (default: no)**
  * Group `3060`
    * `LDS_in_A_oder_2` (start=22, mask=11000000b, comment=FLA_AKTIVIERUNG (default: LDS_in_A))

* **High-Beam Assistant (HBA): deactivate via light switch to the right (default)**
  * Group `3060`
    * `LDS_in_A` (start=22, mask=11000000b, comment=FLA_AKTIVIERUNG (default: LDS_in_A))

* **Fog lights: disable cornering lights**
  * Group `3073`
    * `F020_disable` (start=218, mask=00000010b, comment=C_CLC_ENA (default: F020_enable))
    * `F020_disable` (start=66, mask=00000001b, comment=C_BLC_ENA (default: F020_enable))
  * Group `3066`
    * `KL_Aus` (start=0, mask=00000001b, comment=KL_ENABLE_LI (default: KL_Ein))
    * `KL_Aus` (start=80, mask=00000001b, comment=KL_ENABLE_RE (default: KL_Ein))
  * Group `3062`
    * `off` (start=110, mask=00111111b, comment=MAPPING_ABBIEGEL_L_OUTPUT (default: nsw_l))
    * `off` (start=121, mask=00111111b, comment=MAPPING_ABBIEGEL_R_OUTPUT (default: nsw_r))

* **Fog lights: allow fogs to turn on in reverse**
  * Group `3073`
    * `01` (start=218, mask=00000100b, comment=C_CLC_REV_ALWAYS_ON (default: 01))
    * `01` (start=218, mask=00010000b, comment=C_CLC_REV_CURV_BOTH_ON (default: 01))

* **Welcome lighting: activate door lights when reversing**
  * Group `3070`
    * `aktiv` (start=11, mask=00010000b, comment=OVT_BEI_RUECKFAHRLICHT (default: nicht_aktiv))

* **Eclairage d'accueil: Activation des anti-brouillard**
  * Group `3063`
    * `01` (start=55, mask=11000000b, comment=MAPPING_NEBELSCHW_L_PART_OF_WL (default: 00))
    * `01` (start=66, mask=11000000b, comment=MAPPING_NEBELSCHW_R_PART_OF_WL (default: 00))

* **Welcome lighting: set DRL brightness to 50% (default 100%)**
  * Group `3070`
    * `32` (start=14, mask=11111111b, comment=WL_HELLIGKEIT (default: 64))

* **Welcome lighting: duration 60s (default: 20s)**
  * Group `3060`
    * `3C` (start=15, mask=11111111b, comment=WL_TIMEOUT (default: 14))

* **Lighting: reduce automatic light sensor sensitivity**
  * Group `3130`
    * `03` (start=5, mask=00000111b, comment=RLS_DEF_FLC_SCHWELLWERT_SATZ (default: 00))

* **Door puddle lighting (FollowMeHome step 1 of 2 - see HU-NBT) - 4th button or quick third press (default: inactive)**
  * Group `3060`
    * `aktiv` (start=14, mask=00000010b, comment=FOLLOWMEHOME_VIA_FFB (default: nicht_aktiv))

* **Door puddle lighting (FollowMeHome): duration 30s (default: 20s)**
  * Group `3064`
    * `1E` (start=216, mask=11111111b, comment=PIA_DEFAULT_FMH (default: 14))

* **Ambient lighting: activate when unlocking**
  * Group `3070`
    * `aktiv` (start=1, mask=10000000b, comment=WELCOME_AMBIENTE (default: nicht_aktiv))

* **Ambient lighting: stay on 60s after unlocking (default: 20s)**
  * Group `3070`
    * `3C` (start=9, mask=00011111b, comment=IB_EINSCHALT_BEGR_ULOK (default: 14))

* **Ambient lighting: stay on 20s after locking (default: 8s)**
  * Group `3070`
    * `14` (start=10, mask=00011111b, comment=IB_EINSCHALT_BEGR_LOK (default: 08))

* **Separate brightness control for cluster and ambient lighting**
  * Group `3070`
    * `nicht_aktiv` (start=4, mask=10000000b, comment=AMBIENTE_NACHFUEHRUNG (default: aktiv))

* **Feux freinage d'urgence: activation mode clignotement**
  * Group `3060`
    * `bremslicht_blinkend` (start=16, mask=00000011b, comment=ESS_AKTIVIERBARER_AUSGANG (default: bremslicht_blinkend))

* **Emergency brake lights: lower deceleration threshold to 3 m/s^2 (default: 7 m/s^2)**
  * Group `3060`
    * `06` (start=20, mask=00011111b, comment=ESS_AKTIVIERUNG_REALE_VERZ (default: 0E))

* **Emergency brake lights: minimum speed above 20 km/h (default: 50 km/h)**
  * Group `3060`
    * `14` (start=17, mask=11111110b, comment=ESS_AKTIVIERUNG_GESCHW (default: 32))

* **Auto Start/Stop: disable by default**
  * Group `3023`
    * `aktiv` (start=0, mask=00010000b, comment=TCM_MSA_DEFAULT_OFF (default: nicht_aktiv))

* **Auto Start/Stop: disable in Eco Pro mode**
  * Group `3023`
    * `nicht_aktiv` (start=0, mask=10000000b, comment=TCM_MSA_ECO_MODE (default: aktiv))

* **Auto Start/Stop: remember last state (after restart)**
  * Group `3023`
    * `aktiv` (start=0, mask=00100000b, comment=TCM_MSA_MEMORY (default: nicht_aktiv))

* **Double horn when locking with engine running**
  * Group `3040`
    * `aktiv` (start=1, mask=00100000b, comment=CLM_HORN_AT_SECURE (default: aktiv))

* **Turn off radio/navigation when driver's door opens (default: disabled)**
  * Group `3020`
    * `aktiv` (start=1, mask=00000001b, comment=TCM_LOGIC_R_OFF_DOOR (default: nicht_aktiv))

* **Turn on radio/navigation when driver's door opens (default: disabled)**
  * Group `3020`
    * `nicht_aktiv` (start=1, mask=00000001b, comment=TCM_LOGIC_R_OFF_DOOR (default: nicht_aktiv))

* **Engine: start without pressing brake pedal (automatic)**
  * Group `3020`
    * `nicht_aktiv` (start=0, mask=00000001b, comment=TCM_STARTLOCK_BRAKE (default: aktiv))
    * `nicht_aktiv` (start=0, mask=00010000b, comment=TCM_STARTLOCK_DRIVINGREADINESS (default: aktiv))

### FZD__07 (CAFD 00000A07) — authored by Botho (public) | Series: F020,F030

* **Acoustical lock/unlock confirmation Buzzer level low (level 2 - default)**
  * Group `3001`
    * `level_2` (start=33, mask=11111111b, comment=Buzzer level low (default: level_2))

* **Acoustical lock/unlock confirmation Buzzer level low (level 3)**
  * Group `3001`
    * `level_3` (start=33, mask=11111111b, comment=Buzzer level low (default: level_2))

* **Acoustical lock/unlock confirmation Buzzer level low (level 4)**
  * Group `3001`
    * `level_4` (start=33, mask=11111111b, comment=Buzzer level low (default: level_2))

* **Acoustical lock/unlock confirmation Buzzer level low (level 5)**
  * Group `3001`
    * `level_5` (start=33, mask=11111111b, comment=Buzzer level low (default: level_2))

* **Acoustical lock/unlock confirmation Buzzer level low (level 6)**
  * Group `3001`
    * `level_6` (start=33, mask=11111111b, comment=Buzzer level low (default: level_2))

* **Acoustical lock/unlock confirmation Buzzer level low (level 7)**
  * Group `3001`
    * `level_7` (start=33, mask=11111111b, comment=Buzzer level low (default: level_2))

* **Acoustical lock/unlock confirmation Buzzer level low (level 8)**
  * Group `3001`
    * `level_8` (start=33, mask=11111111b, comment=Buzzer level low (default: level_2))

* **Acoustical lock/unlock confirmation Buzzer level low (level 9)**
  * Group `3001`
    * `level_9` (start=33, mask=11111111b, comment=Buzzer level low (default: level_2))

* **Acoustical lock/unlock confirmation Buzzer level low (level 10)**
  * Group `3001`
    * `level_10` (start=33, mask=11111111b, comment=Buzzer level low (default: level_2))

* **Acoustical lock/unlock confirmation Buzzer level high (level 2)**
  * Group `3001`
    * `level_2` (start=34, mask=11111111b, comment=Buzzer level high (default: level_3))

* **Acoustical lock/unlock confirmation Buzzer level high (level 3 - default)**
  * Group `3001`
    * `level_3` (start=34, mask=11111111b, comment=Buzzer level high (default: level_3))

* **Acoustical lock/unlock confirmation Buzzer level high (level 4)**
  * Group `3001`
    * `level_4` (start=34, mask=11111111b, comment=Buzzer level high (default: level_3))

* **Acoustical lock/unlock confirmation Buzzer level high (level 5)**
  * Group `3001`
    * `level_5` (start=34, mask=11111111b, comment=Buzzer level high (default: level_3))

* **Acoustical lock/unlock confirmation Buzzer level high (level 6)**
  * Group `3001`
    * `level_6` (start=34, mask=11111111b, comment=Buzzer level high (default: level_3))

* **Acoustical lock/unlock confirmation Buzzer level high (level 7)**
  * Group `3001`
    * `level_7` (start=34, mask=11111111b, comment=Buzzer level high (default: level_3))

* **Acoustical lock/unlock confirmation Buzzer level high (level 8)**
  * Group `3001`
    * `level_8` (start=34, mask=11111111b, comment=Buzzer level high (default: level_3))

* **Acoustical lock/unlock confirmation Buzzer level high (level 9)**
  * Group `3001`
    * `level_9` (start=34, mask=11111111b, comment=Buzzer level high (default: level_3))

* **Acoustical lock/unlock confirmation Buzzer level high (level 10)**
  * Group `3001`
    * `level_10` (start=34, mask=11111111b, comment=Buzzer level high (default: level_3))

* **Acoustical lock/unlock confirmation sound frequency (Low)**
  * Group `3001`
    * `8F` (start=35, mask=11111111b, comment=Buzzer frequency (default: 8F))

* **Acoustical lock/unlock confirmation sound frequency (Normal - Default)**
  * Group `3001`
    * `8F` (start=35, mask=11111111b, comment=Buzzer frequency (default: 8F))

* **Acoustical lock/unlock confirmation sound frequency (High)**
  * Group `3001`
    * `8F` (start=35, mask=11111111b, comment=Buzzer frequency (default: 8F))

* **Acoustical lock/unlock confirmation sound duration (Short)**
  * Group `3001`
    * `05` (start=36, mask=11111111b, comment=Buzzer duration (default: 0A))

* **Acoustical lock/unlock confirmation sound duration (Normal - Default)**
  * Group `3001`
    * `0A` (start=36, mask=11111111b, comment=Buzzer duration (default: 0A))

* **Acoustical lock/unlock confirmation sound duration (Long)**
  * Group `3001`
    * `0F` (start=36, mask=11111111b, comment=Buzzer duration (default: 0A))

* **Acoustical lock/unlock confirmation sound duration (Very Long)**
  * Group `3001`
    * `14` (start=36, mask=11111111b, comment=Buzzer duration (default: 0A))

* **Alarm type Europe (Default)**
  * Group `3001`
    * `ece` (start=17, mask=11111111b, comment=Alarm type Europe (default: ece))

* **Alarm type GB**
  * Group `3001`
    * `gb` (start=17, mask=11111111b, comment=Alarm type GB (default: ece))

* **Alarm type US**
  * Group `3001`
    * `08` (start=17, mask=11111111b, comment=Alarm type US (default: ece))

* **Alarm Arming delay time (30 sec - Default)**
  * Group `3001`
    * `3C` (start=15, mask=11111111b, comment=Arming time (default: 30s))

* **Alarm Arming delay time (60 sec)**
  * Group `3001`
    * `78` (start=15, mask=11111111b, comment=Arming time (default: 30s))

* **Panic Alarm - Active**
  * Group `3002`
    * `aktiv` (start=0, mask=00000100b, comment=Panikalarm (default: nicht_aktiv))

* **Panic Alarm - Not active**
  * Group `3002`
    * `nicht_aktiv` (start=0, mask=00000100b, comment=Panikalarm (default: nicht_aktiv))

* **Alarm: delay to disable volumetric sensor after arming - normal (10s - Default)**
  * Group `3002`
    * `0A` (start=2, mask=00001111b, comment=Zeitfenster Deaktivierung NG-US (default: 0A))

* **Alarm: delay to disable volumetric sensor after arming - long (20s)**
  * Group `3002`
    * `14` (start=2, mask=00001111b, comment=Zeitfenster Deaktivierung NG-US (default: 0A))

* **Alarm: Disable Acoustic acknowledgment when arming, regardless of door status (Default)**
  * Group `3002`
    * `00` (start=7, mask=00000001b, comment=Akustische Quittierung Schaerfen (default: 00))

* **Alarm: Enable Acoustic acknowledgment when arming, regardless of door status)**
  * Group `3002`
    * `01` (start=7, mask=00000001b, comment=Akustische Quittierung Schaerfen (default: 00))

### ICMQL (CAFD 0000067B) — authored by Botho (public) | Series: F020,F030

* **Active Cruise Control default distance (Level 1 - la plus faible)**
  * Group `3000`
    * `01` (start=184, mask=00000111b, comment=C_Abstandsstufe_init (default: 03))

* **Active Cruise Control default distance (Level 2)**
  * Group `3000`
    * `02` (start=184, mask=00000111b, comment=C_Abstandsstufe_init (default: 03))

* **Active Cruise Control default distance (Level 3 - Default)**
  * Group `3000`
    * `03` (start=184, mask=00000111b, comment=C_Abstandsstufe_init (default: 03))

* **Active Cruise Control default distance (Level 4)**
  * Group `3000`
    * `04` (start=184, mask=00000111b, comment=C_Abstandsstufe_init (default: 03))

* **Active Cruise Control: Enable from 10 km/h (30 km/h ou 20 mph par default)**
  * Group `3000`
    * `0A` (start=142, mask=11111111b, comment=C_Wunschgeschw_min_kmh (default: 1E))
    * `06` (start=143, mask=11111111b, comment=C_Wunschgeschw_min_mph (default: 14))

* **Active Cruise Control: Enable from 30 km/h (Default)**
  * Group `3000`
    * `1E` (start=142, mask=11111111b, comment=C_Wunschgeschw_min_kmh (default: 1E))
    * `14` (start=143, mask=11111111b, comment=C_Wunschgeschw_min_mph (default: 14))

* **Mode de conduite: Enable default ECO PRO when startup**
  * Group `3000`
    * `01` (start=36, mask=00001000b, comment=IcmKod_B_InitEco (default: 00))

* **Mode de conduite: Enable default CONFORT when startup (Default)**
  * Group `3000`
    * `00` (start=36, mask=00001000b, comment=IcmKod_B_InitEco (default: 00))

* **Blindspot detection: Enable from 10km/h**
  * Group `3000`
    * `00` (start=190, mask=00111111b, comment=C_ZSW_Aktivierunggeschwindigkeit_Funktion_low (default: 01))

* **Blindspot detection: Enable from 20km/h (Default)**
  * Group `3000`
    * `01` (start=190, mask=00111111b, comment=C_ZSW_Aktivierunggeschwindigkeit_Funktion_low (default: 01))

* **Blindspot detection: Enable from 30km/h**
  * Group `3000`
    * `02` (start=190, mask=00111111b, comment=C_ZSW_Aktivierunggeschwindigkeit_Funktion_low (default: 01))

* **Blindspot detection: Enable from 50km/h**
  * Group `3000`
    * `03` (start=190, mask=00111111b, comment=C_ZSW_Aktivierunggeschwindigkeit_Funktion_low (default: 01))

### IHKA_VA02 (CAFD 000016EE) — authored by Botho (public) | Series: F020,F030

* **Climate control: remember last on/off state**
  * Group `3003`
    * `aktiv` (start=0, mask=00000010b, comment=MEMORY_OFF (default: aktiv))

* **Climate control: remember last airflow position (default: 15 minutes after shutdown)**
  * Group `3003`
    * `aktiv` (start=0, mask=00000001b, comment=MEMORY_UMLUFT (default: nicht_aktiv))

* **Climatisation: AC off en mode AUTO**
  * Group `3003`
    * `nicht_aktiv` (start=0, mask=00000100b, comment=AC_ON_WITH_AUTO (default: aktiv))

* **Climate control: disable automatic recirculation restart (HO-Words: DAUE)**
  * Group `3003`
    * `aktiv` (start=1, mask=00010000b, comment=AC_ON_WITH_RECIRC (default: nicht_aktiv))
    * `nicht_aktiv` (start=0, mask=10000000b, comment=UMLUFT_AUTO_AUS (default: aktiv))

### KAFAS2 (CAFD 00001148) — authored by Botho (public) | Series: F020,F030

* **HUD: display distance control assistant (step 3 of 3 - see KOMBI and HU_NBT - requires Active Cruise Control)**
  * Group `3060`
    * `01` (start=1, mask=00011000b, comment=DISPLAY_HEADWAY_DISTANCE (default: 00))
    * `01` (start=1, mask=00000010b, comment=SEND_STATUS_IBRAKE (default: 00))
    * `01` (start=1, mask=00000100b, comment=SEND_PARAM_IBRAKE (default: 01))

* **Lane departure warning: enable edge detection without road markings**
  * Group `3020`
    * `detection_for_grass_edge_and_curb_stone` (start=2, mask=00000011b, comment=ROAD_EDGE_WARNING_ENABLED (defaut: 02))

* **Lane departure warning: activate from 55 km/h (default: 70) and deactivate below 50 km/h (default: 65)**
  * Group `3020`
    * `37` (start=3, mask=11111111b, comment=THRV_AVAI_TLC_HIGH (default: 46))
    * `32` (start=4, mask=11111111b, comment=THRV_AVAI_TLC_LOW (default: 41))

* **-- Don't work -- High-Beam Assistant (HBA): enable sensitivity adjustment (default: no_sensitivity_change)**
  * Group `3050`
    * `01` (start=1, mask=00010000b, comment=ALLOW_SENS_CHANGE (default: 00))

* **-- Don't work -- High-Beam Assistant (HBA): disable sensitivity adjustment (default)**
  * Group `3050`
    * `00` (start=1, mask=00010000b, comment=ALLOW_SENS_CHANGE (default: 00))

* **High-Beam Assistant (HBA): activate at 30 km/h and deactivate at 25 km/h (default: 40-30 km/h)**
  * Group `3050`
    * `1E` (start=6, mask=11111111b, comment=SPEED_SWITCHING_HIGH_BEAMS_ON (default: 28))
    * `19` (start=7, mask=11111111b, comment=SPEED_SWITCHING_HIGH_BEAMS_OFF (default: 1E))

* **High-Beam Assistant (HBA): activate at 40 km/h and deactivate at 30 km/h (default)**
  * Group `3050`
    * `28` (start=6, mask=11111111b, comment=SPEED_SWITCHING_HIGH_BEAMS_ON (default: 28))
    * `1E` (start=7, mask=11111111b, comment=SPEED_SWITCHING_HIGH_BEAMS_OFF (default: 1E))

* **High-Beam Assistant (HBA): faster anti-glare tunnel reaction times**
  * Group `3050`
    * `03` (start=8, mask=11111111b, comment=DELAY_AFTER_ONCOMING (default: 06 - 6 sec))
    * `04` (start=10, mask=11111111b, comment=ONCOMING_HIGH_SPEED_DELAY (default: 0F - 15 sec))
    * `07` (start=11, mask=11111111b, comment=DELAY_AFTER_PRECEDING (default: 1E - 30 sec))
    * `14` (start=12, mask=11111111b, comment=DELAY_AFTER_SLOW_OVERTAKING (default: 50 - 80 sec))

* **High-Beam Assistant (HBA): anti-glare tunnel reaction times default**
  * Group `3050`
    * `06` (start=8, mask=11111111b, comment=DELAY_AFTER_ONCOMING (default: 06 - 6 sec))
    * `0F` (start=10, mask=11111111b, comment=ONCOMING_HIGH_SPEED_DELAY (default: 0F - 15 sec))
    * `1E` (start=11, mask=11111111b, comment=DELAY_AFTER_PRECEDING (default: 1E - 30 sec))
    * `50` (start=12, mask=11111111b, comment=DELAY_AFTER_SLOW_OVERTAKING (default: 50 - 80 sec))

* **High-Beam Assistant (HBA): set urban activation threshold to 75 km/h (default: 85 km/h)**
  * Group `3050`
    * `4B` (start=24, mask=11111111b, comment=HIGH_SPEED_SWITCHING_HIGH_BEAMS (default: 55 - 85 km/h))

* **High-Beam Assistant (HBA): urban activation threshold 85 km/h (default)**
  * Group `3050`
    * `55` (start=24, mask=11111111b, comment=HIGH_SPEED_SWITCHING_HIGH_BEAMS (default: 55- 85 km/h))

### HKFM (CAFD 000007C8) — authored by Botho (public) | Series: F020,F030

* **Hayon: Activation fermeture via bouton au tableau de bord**
  * Group `3010`
    * `aktiv` (start=2, mask=00001000b, comment=SCH_FBD (default: aktiv))
    * `aktiv` (start=2, mask=00000100b, comment=SCH_TOEHKI (default: nicht_aktiv))
    * `aktiv` (start=0, mask=00001000b, comment=TASTER_FBD (default: nicht_aktiv))

* **Tailgate: opening speed (fast with braking before stop - segments bottom to top)**
  * Group `3020`
    * `1B, 1B, 26, 26, 26, 26, 26, 1B, 13` (start=2, end=10, mask=11111111b, comment=DREHZAL_SEGMENT_OEFF (default: 1B, 1B, 1B, 1B, 1B, 1B, 1B, 1B, 1B))
    * `1B` (start=21, mask=11111111b, comment=DEFAULT_DREHZ_OEF (default: 1B))

* **Hayon: Vitesse d'ouverture (par default)**
  * Group `3020`
    * `1B, 1B, 1B, 1B, 1B, 1B, 1B, 1B, 1B` (start=2, end=10, mask=11111111b, comment=DREHZAL_SEGMENT_OEFF (default: 1B, 1B, 1B, 1B, 1B, 1B, 1B, 1B, 1B))
    * `1B` (start=21, mask=11111111b, comment=DEFAULT_DREHZ_OEF (default: 1B))

* **Tailgate: closing speed (fast with braking at close - segments bottom to top)**
  * Group `3020`
    * `0A, 13, 26, 26, 26, 26, 26, 1E, 1B` (start=11, end=19, mask=11111111b, comment=DREHZAL_SEGMENT_SCHL (default: 13, 1B, 1B, 1B, 1B, 1B, 1B, 1B, 1B))
    * `1B` (start=20, mask=11111111b, comment=DEFAULT_DREHZ_SCHL (default: 1B))

* **Hayon: Vitesse de fermeture (par default)**
  * Group `3020`
    * `13, 1B, 1B, 1B, 1B, 1B, 1B, 1B, 1B` (start=11, end=19, mask=11111111b, comment=DREHZAL_SEGMENT_SCHL (default: 13, 1B, 1B, 1B, 1B, 1B, 1B, 1B, 1B))
    * `1B` (start=20, mask=11111111b, comment=DEFAULT_DREHZ_SCHL (default: 1B))

* **Hayon: Activation fermeture sur pression de la main (exercer une pression pour fermer au moins 5% du hayon en moins de 2s)**
  * Group `3010`
    * `aktiv` (start=2, mask=00000010b, comment=MECH_DRUK_AUTO_SCH (default: nicht_aktiv))
    * `14` (start=4, mask=11111111b, comment=MECH_DRUCK_AUTO_ZEIT (default: 0A) - Duréee x 100ms de la pression à exercer)
    * `01` (start=5, mask=11111111b, comment=MECH_DRUCK_AUTO_WINKEL (default: 02) - Angle x 5% minimum pour enclecncher la fermeture automatique)

* **Tailgate: disable close-on-hand pressure (default)**
  * Group `3010`
    * `nicht_aktiv` (start=2, mask=00000010b, comment=MECH_DRUK_AUTO_SCH (default: nicht_aktiv))
    * `0A` (start=4, mask=11111111b, comment=MECH_DRUCK_AUTO_ZEIT (default: 0A) - Duréee x 100ms de la pression à exercer)
    * `02` (start=5, mask=11111111b, comment=MECH_DRUCK_AUTO_WINKEL (default: 02) - Angle x 5% minimum pour enclecncher la fermeture automatique)

* **Hayon: Activation ouverture sur pression de la main (exercer une pression pour ouvrir au moins 5% du hayon en moins de 2s)**
  * Group `3010`
    * `aktiv` (start=2, mask=00000001b, comment=MECH_DRUCK_AUTO_OEF (default: nicht_aktiv))
    * `14` (start=4, mask=11111111b, comment=MECH_DRUCK_AUTO_ZEIT (default: 0A) - Duréee x 100ms de la pression à exercer)
    * `01` (start=5, mask=11111111b, comment=MECH_DRUCK_AUTO_WINKEL (default: 02) - Angle x 5% minimum pour enclecncher la fermeture automatique)

* **Tailgate: disable open-on-hand pressure (default)**
  * Group `3010`
    * `nicht_aktiv` (start=2, mask=00000001b, comment=MECH_DRUCK_AUTO_OEF (default: nicht_aktiv))
    * `0A` (start=4, mask=11111111b, comment=MECH_DRUCK_AUTO_ZEIT (default: 0A) - Duréee x 100ms de la pression à exercer)
    * `02` (start=5, mask=11111111b, comment=MECH_DRUCK_AUTO_WINKEL (default: 02) - Angle x 5% minimum pour enclecncher la fermeture automatique)

* **Tailgate: activate smart closing (step 2 of 2 - see FEM_BODY) enabled by default for production 03/15 onwards**
  * Group `3120`
    * `wert_F31` (start=0, mask=00100000b, comment=FUNC_SMO (default: 00))
    * `wert_F31` (start=0, mask=01000000b, comment=FUNC_BUZZER_SMO (default: 00))

### HU_NBT (CAFD 00000DED) — authored by Botho (public) | Series: F020,F030

* **Media: startup volume at 25% (default value)**
  * Group `3002`
    * `19` (start=3, mask=11111111b, comment=VOL_MAX_ON (default: 19))

* **Media: startup volume at 30% (default 25%)**
  * Group `3002`
    * `1E` (start=3, mask=11111111b, comment=VOL_MAX_ON (default: 19))

* **Media: startup volume at 40% (default 25%)**
  * Group `3002`
    * `28` (start=3, mask=11111111b, comment=VOL_MAX_ON (default: 19))

* **Media: show next track for music (KOMBI_LOW only)**
  * Group `3000`
    * `aktiv` (start=110, mask=00100000b, comment=BASIS_KOMBI_MMI_LIST (fonctionne que si KOMBI_CIC=kombi_low) (default: nicht_aktiv))

* **Media: enable OGG, XVID, XVCD and USB playback**
  * Group `3000`
    * `aktiv` (start=15, mask=00010000b, comment=ENT_CODEC_OGG (default: nicht_aktiv))
    * `aktiv` (start=15, mask=00100000b, comment=ENT_CODEC_XVID (default: nicht_aktiv))
    * `aktiv` (start=15, mask=01000000b, comment=ENT_CODEC_VCD (default: nicht_aktiv))
    * `aktiv` (start=13, mask=00000100b, comment=ENT_MC_VIDEO_SUPPORT (default: nicht_aktiv))

* **Media: enable DVD in motion**
  * Group `3000`
    * `FF` (start=72, mask=11111111b, comment=SPEEDLOCK_X_KMH_MAX (default: 03))
    * `FF` (start=71, mask=11111111b, comment=SPEEDLOCK_X_KMH_MIN (default: 03))
    * `nicht_aktiv` (start=5, mask=00010000b, comment=VIDEO_FRONT_LOCKED (default: nicht_aktiv))
    * `nicht_aktiv` (start=5, mask=00000100b, comment=VIDEO_HANDBRAKE (default: nicht_aktiv))
    * `none` (start=57, mask=00000111b, comment=VIDEO_SPEEDLOCK_CONDITION (default: none))

* **Media: use Gracenote dB full-size album art**
  * Group `3000`
    * `aktiv` (start=14, mask=00100000b, comment=ENT_MC_COVER_SCALE (default: nicht_aktiv))

* **Media: enable bookmarks in music collection**
  * Group `3000`
    * `aktiv` (start=14, mask=00000100b, comment=ENT_MC_SONG_BOOKMARKS (default: nicht_aktiv))

* **HUD: display distance control assistant (step 2 of 3 - see KOMBI and KAFAS2 - requires Active Cruise Control)**
  * Group `3000`
    * `aktiv` (start=97, mask=00001000b, comment=HUD_DISTANCE_INFO (default: nicht_aktiv))

* **HUD: display multimedia info for 2.5s (default 4s)**
  * Group `3000`
    * `03` (start=106, mask=00000111b, comment=DISPLAYTIME_LIST_HUD_KOMBI (default: 05))

* **HUD: show Sport option (shift indicator - M vehicles only)**
  * Group `3000`
    * `aktiv` (start=18, mask=00000001b, comment=HUD_SPORTANZEIGE_ENABLE (default: nicht_aktiv))
    * `aktiv` (start=18, mask=00000100b, comment=HUD_SPORTANZEIGE_MS_GASSE_ENABLE (default: nicht_aktiv))

* **Doors: Checkbox acoustical lock confirmation**
  * Group `3000`
    * `aktiv` (start=110, mask=00000001b, comment=ACOUSTICAL_LOCK_CONFIRM (default: nicht_aktiv))

* **Eclairage: Ajout feux de jour (Step 2 sur 3 - voir FEM_BODY et REM)**
  * Group `3000`
    * `02` (start=92, mask=00011000b, comment=DAYDRIVING_LIGHT (default: 00))

* **Status: display tire temperature and pressure**
  * Group `3001`
    * `aktiv` (start=1, mask=00100000b, comment=RDC_SAFETY (default: nicht_aktiv))
    * `02` (start=66, mask=00001100b, comment=RDC_DRUCK_TEMP (default: 01/druck))

* **Statut: Affichage du carnet d'entretien**
  * Group `3000`
    * `aktiv` (start=2, mask=00100000b, comment=SERVICE_HISTORY (default: aktiv))

* **Notice: Utilisation de la notice et jumelage BT en roulant**
  * Group `3000`
    * `nicht_aktiv` (start=0, mask=00100000b, comment=SL06_IBA_1 (default: aktiv))
    * `nicht_aktiv` (start=0, mask=01000000b, comment=SL07_IBA_2 (default: nicht_aktiv))
    * `nicht_aktiv` (start=2, mask=00010000b, comment=SL21_IBA_3 (default: nicht_aktiv))
    * `nicht_aktiv` (start=1, mask=10000000b, comment=SL16_ADD_CEDEVICE (default: nicht_aktiv))

* **Messages: Affichage des SMS, BMW Info, My Info and AKD en entier (default: 3 lignes)**
  * Group `3000`
    * `whole_text` (start=34, mask=00011100b, comment=MYINFO_DRIVING_TEXT_LENGTH (default: whole_text))
    * `whole_text` (start=34, mask=11100000b, comment=AKD_DRIVING_TEXT_LENGTH (default: whole_text))
    * `whole_text` (start=35, mask=00000111b, comment=BMWINFO_DRIVING_TEXT_LENGTH (default: whole_text))
    * `none` (start=35, mask=00111000b, comment=SERVICES_MESSAGES_SPEEDLOCK_CONDITION (default: none))
  * Group `3003`
    * `07` (start=11, mask=00000111b, comment=PIM_DRIVING_TEXT_LENGTH (default: 01))

* **Sport: Affichage mode M Sport (Rouge et Argent)**
  * Group `3000`
    * `aktiv` (start=133, mask=01000000b, comment=M_VEHICLE (default: nicht_aktiv))

* **Tableau de bord: Affichage du point de commutation (Step 2 sur 2 - voir KOMBI)**
  * Group `3001`
    * `aktiv` (start=66, mask=00010000b, comment=SPA_CHECKBOX (default: nicht_aktiv))

* **Navigation: Alerte quand proche du POI**
  * Group `3000`
    * `aktiv` (start=111, mask=10000000b, comment=NAVI_ALERT_POI (default: nicht_aktiv))

* **Navigation: add route preview option**
  * Group `3000`
    * `aktiv` (start=59, mask=00100000b, comment=NAVI_ROAD_PREVIEW (default: nicht_aktiv))

* **Navigation: Ajoute la position GPS en fin de menu**
  * Group `3000`
    * `aktiv` (start=96, mask=10000000b, comment=NAVI_POSITION_MENU (default: nicht_aktiv))

* **Navigation: add route calculation preference for BMW servers**
  * Group `3000`
    * `aktiv` (start=112, mask=00000010b, comment=NAVI_ONLINE_OPTIMIZATION_BUTTON (default: nicht_aktiv))

* **Navigation: Active Real-Time Traffic Info**
  * Group `3000`
    * `aktiv` (start=59, mask=00010000b, comment=NAVI_TRAFFIC_INFO_MAP)
  * Group `3002`
    * `aktiv` (start=23, mask=00000100b, comment=TI_CA_TMC)
    * `aktiv` (start=24, mask=00000010b, comment=TI_VINFO)
    * `aktiv` (start=23, mask=00100000b, comment=TI_TMC_REGIONAL)
    * `aktiv` (start=23, mask=01000000b, comment=TI_FALLBACK_DISABLED)

* **Navigation: Active la boussole**
  * Group `3000`
    * `aktiv` (start=5, mask=00000001b, comment=COMPASS)

* **Navigation: Affichage de la vue sortie autoroute dans HUD**
  * Group `3000`
    * `aktiv` (start=65, mask=00001000b, comment=JUNCTION_VIEW_HUD (default: nicht_aktiv. Aktiv si production date après 1114))

* **Navigation: enable demo route mode**
  * Group `3000`
    * `aktiv` (start=135, mask=00001000b, comment=ROUTE_FLIGHT (default: aktiv))
    * `aktiv` (start=111, mask=00001000b, comment=NAVI_SCROLLING_ALONG_ROUTE (default: nicht_aktiv))

* **Navigation: suggest fuel stop when needed**
  * Group `3000`
    * `aktiv` (start=60, mask=00100000b, comment=NAVI_FUELSTOP_PROPOSAL (default: aktiv))

* **Navigation: add traffic info categories to options**
  * Group `3000`
    * `aktiv` (start=16, mask=00000010b, comment=TRAFFIC_CATEGORIES (default: nicht_aktiv))

* **Navigation: add waypoint (magnet function)**
  * Group `3000`
    * `aktiv` (start=111, mask=00010000b, comment=NAVI_ROUTENMAGNET (default: nicht_aktiv))

* **Navigation: add express route menu to guidance preferences**
  * Group `3000`
    * `aktiv` (start=108, mask=00000100b, comment=NAVI_EXPRESS_ROADS (default: nicht_aktiv))

* **Navigation: active les popup de guidage SPLIT et FULL**
  * Group `3000`
    * `aktiv` (start=62, mask=00001000b, comment=NAVI_SPLIT_GUIDINGPOPUP (default: nicht_aktiv))
    * `aktiv` (start=62, mask=00010000b, comment=NAVI_FULL_GUIDINGPOPUP (default: nicht_aktiv))

* **Navigation: Voix femme (par default)**
  * Group `3000`
    * `weiblich` (start=73, mask=00001111b, comment=SPRECHERWAHL1 (default: weiblich))
    * `weiblich` (start=73, mask=11110000b, comment=SPRECHERWAHL2 (default: weiblich))
    * `weiblich` (start=74, mask=00001111b, comment=SPRECHERWAHL3 (default: weiblich))

* **Navigation: Voix homme**
  * Group `3000`
    * `maennlich` (start=73, mask=00001111b, comment=SPRECHERWAHL1 (default: weiblich))
    * `maennlich` (start=73, mask=11110000b, comment=SPRECHERWAHL2 (default: weiblich))
    * `maennlich` (start=74, mask=00001111b, comment=SPRECHERWAHL3 (default: weiblich))

* **Office: speech to text (email or SMS) requires Nuance subscription**
  * Group `3003`
    * `aktiv` (start=1, mask=00010000b, comment=SPEECH_2_TEXT (default: nicht_aktiv))

* **Cameras: remove legal messages**
  * Group `3001`
    * `00` (start=52, mask=11111111b, comment=MACRO_CAM_LEGALDISCLAIMER (default: 06))
    * `00` (start=58, mask=11111111b, comment=LEGAL_DISCLAIMER_TIME (default: 00))

* **Settings: enable developer menu**
  * Group `3000`
    * `aktiv` (start=74, mask=01000000b, comment=ENTWICKLER_MENUE (default: nicht_aktiv))

* **Phone: iOS ringtone**
  * Group `3003`
    * `aktiv` (start=6, mask=10000000b, comment=INBAND_RINGING (default: nicht_aktiv))

* **Phone: BMW ringtone (default: BMW)**
  * Group `3003`
    * `00` (start=8, mask=00000011b, comment=RINGTONE (default: 00))

* **Phone: MINI ringtone (default: BMW)**
  * Group `3003`
    * `01` (start=8, mask=00000011b, comment=RINGTONE (default: 00))

* **Phone: BMW i ringtone (default: BMW)**
  * Group `3003`
    * `02` (start=8, mask=00000011b, comment=RINGTONE (default: 00))

* **Phone: Rolls-Royce ringtone (default: BMW)**
  * Group `3003`
    * `03` (start=8, mask=00000011b, comment=RINGTONE (default: 00))

* **Phone: enable Siri Eyes Free (default: aktiv)**
  * Group `3003`
    * `01` (start=3, mask=00001000b, comment=CE_DEVICE_SPEECH_RECOGNITION (default: 01))

* **Settings: BMW gong sound (default: BMW)**
  * Group `3002`
    * `00` (start=26, mask=00111000b, comment=SOUND_SIGNAL_SET (default: 00))

* **Settings: MINI gong sound (default: BMW)**
  * Group `3002`
    * `01` (start=26, mask=00111000b, comment=SOUND_SIGNAL_SET (default: 00))

* **Settings: Rolls-Royce gong sound (default: BMW)**
  * Group `3002`
    * `02` (start=26, mask=00111000b, comment=SOUND_SIGNAL_SET (default: 00))

* **Settings: BMW i gong sound (default: BMW)**
  * Group `3002`
    * `03` (start=26, mask=00111000b, comment=SOUND_SIGNAL_SET (default: 00))

* **Settings: startup screen BMW ConnectedDrive 1 (default: BMW)**
  * Group `3001`
    * `00` (start=62, mask=01111000b, comment=STARTUP_EMBLEM (default: 00))

* **Settings: startup screen M Performance (default: BMW)**
  * Group `3001`
    * `01` (start=62, mask=01111000b, comment=STARTUP_EMBLEM (default: 00))

* **Settings: startup screen BMW ConnectedDrive 2 (default: BMW)**
  * Group `3001`
    * `02` (start=62, mask=01111000b, comment=STARTUP_EMBLEM (default: 00))

* **Settings: startup screen BMW i (default: BMW)**
  * Group `3001`
    * `03` (start=62, mask=01111000b, comment=STARTUP_EMBLEM (default: 00))

* **Settings: startup screen MINI (default: BMW)**
  * Group `3001`
    * `04` (start=62, mask=01111000b, comment=STARTUP_EMBLEM (default: 00))

* **Settings: startup screen Rolls-Royce (default: BMW)**
  * Group `3001`
    * `05` (start=62, mask=01111000b, comment=STARTUP_EMBLEM (default: 00))

* **Settings: startup screen BMW ConnectedDrive 3 (default: BMW)**
  * Group `3001`
    * `06` (start=62, mask=01111000b, comment=STARTUP_EMBLEM (default: 00))

* **Settings: startup screen BMW White (default: BMW)**
  * Group `3001`
    * `07` (start=62, mask=01111000b, comment=STARTUP_EMBLEM (default: 00))

* **Settings: startup screen BMW Brown (default: BMW)**
  * Group `3001`
    * `08` (start=62, mask=01111000b, comment=STARTUP_EMBLEM (default: 00))

* **Settings: startup screen BMW Christmas and New Year (default: BMW)**
  * Group `3001`
    * `09` (start=62, mask=01111000b, comment=STARTUP_EMBLEM (default: 00))

* **Settings: enable GPS tracking (appears to require subscription)**
  * Group `3003`
    * `aktiv` (start=15, mask=00000001b, comment=ASSIST_SVR_SHOW (default: nicht_aktiv))
    * `aktiv` (start=14, mask=10000000b, comment=ASSIST_VEHICLEFINDER_SHOW (default: aktiv))

* **Settings (expert): enable Bluetooth tethering - requires modifying provisioning XML via Tool32**
  * Group `3003`
    * `01` (start=3, mask=00000010b, comment=DUN_PROFILE (default: 00))
    * `01` (start=3, mask=00000100b, comment=PAN_PROFILE (default: 00))

* **-- TESTING -- Navigation: enable guided tours**
  * Group `3000`
    * `aktiv` (start=60, mask=00000010b, comment=GUIDED_TOURS (default: nicht_aktiv))
    * `aktiv` (start=60, mask=00010000b, comment=ROUTEN_ID_GUIDEDTOURS (default: nicht_aktiv))

* **-- Don't work -- Settings: traction control configuration (menu present but inactive)**
  * Group `3000`
    * `aktiv` (start=134, mask=00001000b, comment=TRACTION_DEMAND_CONTROL (default: nicht_aktiv))

* **-- Don't work -- Phone: show contacts icon**
  * Group `3003`
    * `aktiv` (start=12, mask=00001000b, comment=CONTACTS_ICON (default: nicht_aktiv))

* **-- Don't work -- Settings: enable parking exit assistant (requires specific hardware)**
  * Group `3001`
    * `aktiv` (start=13, mask=10000000b, comment=MACRO_PMA_AUSPARKEN (default: nicht_aktiv))

* **-- Don't work -- Settings: enable automatic PDC (requires specific hardware)**
  * Group `3001`
    * `aktiv` (start=64, mask=00010000b, comment=ACTIVE_PDC (default: nicht_aktiv))
    * `aktiv` (start=65, mask=01000000b, comment=AUTO_PDC (default: nicht_aktiv))

* **-- Don't work -- HUD: Affichage clignotants (Step 1 sur 2 - voir KOMBI)**
  * Group `3001`
    * `aktiv` (start=55, mask=10000000b, comment=HUD_TURNSIGNAL (default: nicht_aktiv))

* **-- Don't work -- Lighting: ambient light (F4x only)**
  * Group `3000`
    * `01` (start=35, mask=11000000b, comment=DEAKTIVIERUNGSMOEGLICHKEIT_AMBILIGHT (default: 00))

* **-- Don't work -- Eclairage: Affichage High-Beam Assistant (HBA)**
  * Group `3000`
    * `aktiv` (start=109, mask=10000000b, comment=HIGH_BEAM_ASSISTANT (default: nicht_aktiv))

* **-- TESTING -- Lighting: add door puddle light (Follow-Me-Home step 2 of 2 - see FEM)**
  * Group `3000`
    * `aktiv` (start=26, mask=00001000b, comment=KEY_CONF_COMFORT_HOMELIGHT (default: nicht_aktiv))

* **-- Don't work -- Statut: Affichage informations de la batterie**
  * Group `3000`
    * `aktiv` (start=134, mask=00000001b, comment=KI_SELECTION_SOC (default: nicht_aktiv))

* ***** TESTING *** Doors: comfort opening (double remote click lowers windows to 75% - useful for coupes)**
  * Group `3000`
    * `aktiv` (start=100, mask=01000000b, comment=COMFORT_OPENING (default: nicht_aktiv))

* **-- Don't work -- Navigation: Zoom automatique aux intersections**
  * Group `3000`
    * `aktiv` (start=111, mask=00000100b, comment=NAVI_AUTOZOOM (default: nicht_aktiv))

* **-- Don't work -- Navigation: Zoom automatique de la carte**
  * Group `3000`
    * `aktiv` (start=16, mask=00001000b, comment=AUTO_MAP_ZOOM (default: nicht_aktiv))

* **-- Don't work -- Navigation: Active le guidage en 2 etapes ?? No difference**
  * Group `3000`
    * `aktiv` (start=111, mask=00000010b, comment=NAVI_VIOCE_OUTPUT_2_STEP (default: nicht_aktiv))

### KOMBI L7_MID (CAFD 000009C8) — authored by Botho (public) | Series: F020,F030

* **Tableau de bord: Affichage de la vitesse digitale**
  * Group `3000`
    * `aktiv` (start=1, mask=00000010b, comment=BC_DIGITAL_V (default: nicht_aktiv))

* **Instrument cluster: show actual speed**
  * Group `3000`
    * `nicht_aktiv` (start=1, mask=01000000b, comment=BC_V_KORREKTUR (default: aktiv))

* **Instrument cluster: first fuel reserve warning at 70 km (default: 90 km)**
  * Group `3000`
    * `46` (start=35, mask=11111111b, comment=CC_RW_WARNUNG_2 (default: 5A))

* **Instrument cluster: first fuel reserve warning at 90 km (default: 90 km)**
  * Group `3000`
    * `5A` (start=35, mask=11111111b, comment=CC_RW_WARNUNG_2 (default: 5A))

* **Instrument cluster: second fuel reserve warning at 30 km (default: 50 km)**
  * Group `3000`
    * `1E` (start=29, mask=11111111b, comment=CC_RW_WARNUNG (default: 32))

* **Instrument cluster: second fuel reserve warning at 50 km (default: 50 km)**
  * Group `3000`
    * `32` (start=29, mask=11111111b, comment=CC_RW_WARNUNG (default: 32))

* **Instrument cluster: disable automatic trip reset (default: 4h)**
  * Group `3000`
    * `FF` (start=44, mask=11111111b, comment=BC_AUTORESET_ZEIT (default: 04))

* **Instrument cluster: keep daytime lights active at night**
  * Group `3007`
    * `FF` (start=10, mask=11111111b, comment=DIM_NACHT_EIN (default: 08))

* **Instrument cluster: permanent M Performance logo bottom right (1/2)**
  * Group `3003`
    * `aktiv` (start=7, mask=00000100b, comment=MPM_ENABLE (default: nicht_aktiv))

* **Tableau de bord: Choix Logo M performance M50d (2/2)**
  * Group `3000`
    * `50d` (start=43, mask=11110000b, comment=MPM_LOGO (default: ag))

* **Tableau de bord: Choix Logo M performance 135i (2/2)**
  * Group `3000`
    * `135i` (start=43, mask=11110000b, comment=MPM_LOGO (default: ag))

* **Tableau de bord: Choix Logo M performance 140i (2/2)**
  * Group `3000`
    * `140i` (start=43, mask=11110000b, comment=MPM_LOGO (default: ag))

* **Tableau de bord: Choix Logo M performance 235i (2/2)**
  * Group `3000`
    * `235i` (start=43, mask=11110000b, comment=MPM_LOGO (default: ag))

* **Tableau de bord: Choix Logo M performance 240i (2/2)**
  * Group `3000`
    * `240i` (start=43, mask=11110000b, comment=MPM_LOGO (default: ag))

* **Tableau de bord: Choix Logo M performance 340i (2/2)**
  * Group `3000`
    * `340i` (start=43, mask=11110000b, comment=MPM_LOGO (default: ag))

* **Tableau de bord: Choix Logo M performance 550d (2/2)**
  * Group `3000`
    * `550d` (start=43, mask=11110000b, comment=MPM_LOGO (default: ag))

* **Tableau de bord: Choix Logo M performance hybride (2/2)**
  * Group `3000`
    * `phev` (start=43, mask=11110000b, comment=MPM_LOGO (default: ag))

* **Cluster and HUD: default startup logo**
  * Group `3000`
    * `ag` (start=0, mask=11110000b, comment=BMW_LOGO (default: ag))

* **Cluster and HUD: M Performance startup logo**
  * Group `3000`
    * `m_performance` (start=0, mask=11110000b, comment=BMW_LOGO (default: ag))

* **Cluster and HUD: M Performance startup logo 135i**
  * Group `3000`
    * `135i` (start=0, mask=11110000b, comment=BMW_LOGO (default: ag))

* **Cluster and HUD: M Performance startup logo 140i**
  * Group `3000`
    * `140i` (start=0, mask=11110000b, comment=BMW_LOGO (default: ag))

* **Cluster and HUD: M Performance startup logo 235i**
  * Group `3000`
    * `235i` (start=0, mask=11110000b, comment=BMW_LOGO (default: ag))

* **Cluster and HUD: M Performance startup logo 240i**
  * Group `3000`
    * `240i` (start=0, mask=11110000b, comment=BMW_LOGO (default: ag))

* **Cluster and HUD: M Performance startup logo 340i**
  * Group `3000`
    * `340i` (start=0, mask=11110000b, comment=BMW_LOGO (default: ag))

* **Cluster and HUD: M Performance startup logo 50d**
  * Group `3000`
    * `50d` (start=0, mask=11110000b, comment=BMW_LOGO (default: ag))

* **Cluster and HUD: M Performance startup logo M2**
  * Group `3000`
    * `M2` (start=0, mask=11110000b, comment=BMW_LOGO (default: ag))

* **Cluster and HUD: M Performance startup logo M3**
  * Group `3000`
    * `M4` (start=0, mask=11110000b, comment=BMW_LOGO (default: ag))

* **Cluster and HUD: M Performance startup logo M4 GTS**
  * Group `3000`
    * `M4 GTS` (start=0, mask=11110000b, comment=BMW_LOGO (default: ag))

* **Cluster and HUD: M Performance startup logo hybride**
  * Group `3000`
    * `phev` (start=0, mask=11110000b, comment=BMW_LOGO (default: ag))

* **Instrument cluster: show time bottom right (I-Step after 3.54.3)**
  * Group `3000`
    * `aktiv` (start=53, mask=01000000b, comment=BASISANZEIGE_VARIANTE (default: nicht_aktiv. Aktiv si production date après 0315))

* **Instrument cluster: show gear in Sport mode (S1-S8 instead of DS)**
  * Group `3000`
    * `aktiv` (start=41, mask=00010000b, comment=SPA_SPORT_ENABLE (default: nicht_aktiv. Aktiv si production date après 0315))

* **Tableau de bord: Affichage du point de commutation (Step 1 sur 2 - voir HU_NBT)**
  * Group `3003`
    * `nicht_aktiv` (start=0, mask=00100000b, comment=SPA_KOMBISELECT_DISABLE (default: nicht_aktiv))

* **Tableau de bord: Affichage rapports au compteur**
  * Group `3003`
    * `aktiv` (start=0, mask=00010000b, comment=SPA_IST_GANG_ENABLE (default: nicht_aktiv))

* **Tableau de bord: Volume clignotant moins fort**
  * Group `300B`
    * `A0, B0, C0, FF` (start=4, mask=11111111b, comment=BLINKER_VOLUME_CONTI (default: E0, F0, FF, FF))

* **Tableau de bord: Volume clignotant par defaut**
  * Group `300B`
    * `E0, F0, FF, FF` (start=4, mask=11111111b, comment=BLINKER_VOLUME_CONTI (default: E0, F0, FF, FF))

* **Instrument cluster: DTS separation (value to verify - see http://www.bimmerfest.com/forums/showthread.php?p=10034327)**
  * Group `3000`
    * `aktiv` (start=43, mask=00000010b, comment=DSC_OFF_ENTFLECHTUNG_ENABLE (default: nicht_aktiv))

* **HUD: extend startup duration to 10s to display logo longer (default: 4s)**
  * Group `300B`
    * `0A` (start=20, mask=11111111b, comment=HUD_STARTUP_TIME (default: 28. 32 si production date après 0315))

* **HUD: display distance control assistant (step 1 of 3 - see KAFAS2 and HU_NBT - requires Active Cruise Control)**
  * Group `3000`
    * `aktiv` (start=1, mask=00000001b, comment=IBRAKE_ABSTAND_ENABLE (default: nicht_aktiv))
  * Group `3003`
    * `aktiv` (start=3, mask=00000100b, comment=IBRAKE_VERBAUT (default: aktiv))
    * `aktiv` (start=4, mask=00100000b, comment=HUD_IBRAKE_ENABLE (default: aktiv))
  * Group `3008`
    * `aktiv` (start=6, mask=00100000b, comment=HUD_PIA_IBRAKE (default: nicht_aktiv))

* **-- Don't work -- HUD: Affichage clignotants (Step 1 sur 2 - voir HU_NBT)**
  * Group `3003`
    * `aktiv` (start=4, mask=00000001b, comment=HUD_BLINKER_ENABLE (default: nicht_aktiv))
  * Group `3008`
    * `aktiv` (start=5, mask=00000001b, comment=HUD_PIA_BLINKER (default: nicht_aktiv))

* **-- TESTING -- HUD: HUD_POSITIONCHANGE_ENABLE**
  * Group `3000`
    * `aktiv` (start=53, mask=10000000b, comment=HUD_POSITIONCHANGE_ENABLE (défaut : nicht_aktiv))

* **-- TESTING -- HUD: SPA_ENABLE**
  * Group `3003`
    * `aktiv` (start=0, mask=0001000b, comment=SPA_ENABLE - Active l'affichage du point de commutation (défaut : nicht_aktiv))

### REM_01 (CAFD 000007A1) — authored by Botho (public) | Series: F020,F030

* **Rear windows: enable when rear doors open**
  * Group `3050`
    * `nicht_aktiv` (start=0, mask=00000001b, comment=FH_TUERAUF_STOP_MAUT (default: aktiv))

* **Angel Eyes (DRL): enable tailgate DRLs (step 3 of 3 - see HU-NBT and FEM_BODY)**
  * Group `3062`
    * `16` (start=220, mask=00111111b, comment=MAPPING_TAGFAHRL_H2_L_OUTPUT LED hayon intérieur gauche (default: 00))
    * `17` (start=230, mask=00111111b, comment=MAPPING_TAGFAHRL_H2_R_OUTPUT LED hayon intérieur droit (default: 00))
    * `14` (start=200, mask=00111111b, comment=MAPPING_TAGFAHRL_H_L_OUTPUT LED hayon exterieur gauche (default: 00))
    * `15` (start=210, mask=00111111b, comment=MAPPING_TAGFAHRL_H_R_OUTPUT LED hayon exterieur droit (default: 00))

* **Rear fog lights: activation (step 1 of 2 - see FEM_BODY)**
  * Group `3063`
    * `1C` (start=40, mask=00111111b, comment=Mapping_Nebelschlussl_L_output lampe hayon gauche (default: 1C))
    * `0E` (start=41, mask=00011111b, comment=Mapping_Nebelschlussl_L_Function lampe hayon gauche (default: 0E))
    * `1D` (start=50, mask=00111111b, comment=Mapping_Nebelschlussl_R_output lampe hayon droit (default: 1D))
    * `0E` (start=51, mask=00011111b, comment=Mapping_Nebelschlussl_R_Function lampe hayon droit (default: 0E))

* **Rear fog lights: deactivation (step 1 of 2 - see FEM_BODY)**
  * Group `3063`
    * `00` (start=40, mask=00111111b, comment=Mapping_Nebelschlussl_L_output lampe hayon gauche (default: 1C))
    * `0E` (start=41, mask=00011111b, comment=Mapping_Nebelschlussl_L_Function lampe hayon gauche (default: 0E))
    * `00` (start=50, mask=00111111b, comment=Mapping_Nebelschlussl_R_output lampe hayon droit (default: 1D))
    * `0E` (start=51, mask=00011111b, comment=Mapping_Nebelschlussl_R_Function lampe hayon droit (default: 0E))

* **Rear camera: remove speed limit (side cameras see TRSVC)**
  * Group `3203`
    * `FF` (start=7, mask=11111111b, comment=V_SCHWELLE_1: vitesse de désactivation caméras rétroviseurs (default: 0F))
    * `FF` (start=8, mask=11111111b, comment=V_SCHWELLE_2: vitesse de désactivation caméra arrière (default: 0F))
    * `FF` (start=9, mask=11111111b, comment=D_SCHWELLE_1: distance de désactivation caméras rétroviseurs (default: 32))
    * `FF` (start=10, mask=11111111b, comment=D_SCHWELLE_2: distance de désactivation caméra arrière (default: 0A))

* **Emergency brake lights: enable rear LEDs (default: enabled)**
  * Group `3062`
    * `bl_l` (start=110, mask=00111111b, comment=MAPPING_BRAKEFORCED_L_OUTPUT (default: bl_l))
    * `bl_r` (start=120, mask=00111111b, comment=MAPPING_BRAKEFORCED_R_OUTPUT (default: bl_r))

* **Emergency brake lights: increase rear LED flash frequency (default: 03)**
  * Group `3064`
    * `05` (start=17, mask=00001110b, comment=ESS_BLINKFREQ_1 (default: 03))
    * `05` (start=17, mask=01110000b, comment=ESS_BLINKFREQ_2 (default: 03))

### CFAS_PLX_1 (CAFD 000000B5) — authored by Botho (public) | Series: F020,F030

* **Power seats: chime when storing position**
  * Group `3000`
    * `aktiv` (start=2, mask=00001000b, comment=MEMORY_GONG (default: nicht_aktiv. Aktiv si production date après 0714))

* **Power seats (Easy Entry): enable Easy Entry**
  * Group `3000`
    * `Modus_FA_SLV` (start=0, mask=00011100b, comment=EINAUSSTIEGSHILFE (default: nicht_aktiv))

* **Power seats (Easy Entry): minimum seat distance from rear stop**
  * Group `3012`
    * `00, 32` (start=4, end=5, mask=11111111b, comment=EAH_SCHUTZFREIRAUM_HINTEN_SLV_PHYS (default: 00, 64))

* **Power seats (Easy Entry): seat travel distance**
  * Group `3012`
    * `00, 32` (start=0, end=1, mask=11111111b, comment=EAH_VERFAHRWEG_SLV_PHYS (default: 00, 3C))

### TRSVC (CAFD 00000223) — authored by Botho (public) | Series: F020,F030

* **Side cameras: remove speed limit (rear camera see REM_01)**
  * Group `3000`
    * `FF` (start=114, mask=11111111b, comment=SV_Activate_Speed_Limit (default: 0F))
    * `FF` (start=115, mask=11111111b, comment=SV_Deactivate_Speed (default: 0F))


## `Bundang_Thunder.xml`

**Modules touched:** ACSM_5 (CAFD 00001B29, author Bundang Thunder G Series, series G11, G30), BDC_01 (CAFD 00001DF7, author Bundang Thunder G Series, series G11, G30), BDC_01 (CAFD 000017BC, author Bundang Thunder G Series, series G11, G30), DME_DDE8xx (CAFD 000029B7, author Bundang Thunder G Series, series G11, G30), FZD__35 (CAFD 00001D92, author Bundang Thunder G Series, series G11, G30), HKFM_2015 (CAFD 00002098, author Bundang Thunder G Series, series G11, G30), HU_NBT_EVO (CAFD 00001EF6, author Bundang Thunder G Series, series G11, G30), DSC_EBS460 (CAFD 00002060, author Bundang Thunder G Series, series G11, G30), KAFAS (CAFD 00002089, author Bundang Thunder G Series, series G11, G30), EGS_ZFB_CC (CAFD 00002458, author Bundang Thunder G Series, series G11, G30), IHKA_PR01 (CAFD 000022D3, author Bundang Thunder G Series, series G11, G30), Kombi (CAFD 00002660, author Bundang Thunder G Series, series G11, G30), CBFS_S15 (CAFD 0000225A, author Bundang Thunder G Series, series G11, G30), CFAS_S15 (CAFD 00002259, author Bundang Thunder G Series, series G11, G30), CBFS_S15 (CAFD 0000225A, author Bundang Thunder G Series, series G11, G30), ACSM_4i (CAFD 000011AB, author Bundang Thunder i3, series I001), BDC_01 (CAFD 000017BE, author Bundang Thunder i3, series I001), HU_NBT (CAFD 00000DED, author Bundang Thunder i3, series I001), IHKA_VA02 (CAFD 000016EE, author Bundang Thunder i3, series I001), ACSM_4i (CAFD 000011AB, author Bundang Thunder Mini, series F64,F55,F56,F57,F45), ASD01 (CAFD 00000F9B, author Bundang Thunder Mini, series F64,F55,F56,F57,F45), BDC_01 (CAFD 000017BE, author Bundang Thunder Mini, series F64,F55,F56,F57,F45), HU_NBT_EVO (CAFD 00001EF6, author Bundang Thunder Mini, series F64,F55,F56,F57,F45), PMA_PDC (CAFD 00001AB7, author Bundang Thunder Mini, series F64,F55,F56,F57,F45), DSC_CT02 (CAFD 0000297A, author Bundang Thunder Mini, series F64,F55,F56,F57,F45), KOMBI_I01_F56 (CAFD 0000141F, author Bundang Thunder Mini, series F64,F55,F56,F57,F45), CFAS_PLX_1 (CAFD 000000B5, author Bundang Thunder Mini, series F64,F55,F56,F57,F45), ACSM_4B (CAFD 00000911, author Bundang Thunder 1 Series, series F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83), DSC_CT01 (CAFD 000019CC, author Bundang Thunder 1 Series, series F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83), GKEB23 (CAFD 0000023F, author Bundang Thunder 1 Series, series F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83), FEM_01 (CAFD 00000794, author Bundang Thunder 1 Series, series F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83), HU_NBT (CAFD 00000DED, author Bundang Thunder 1 Series, series F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83), ICMQL (CAFD 0000067B, author Bundang Thunder 1 Series, series F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83), IHKA_VA02 (CAFD 000016EE, author Bundang Thunder 1 Series, series F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83), KAFAS2 (CAFD 00001148, author Bundang Thunder 1 Series, series F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83), KOMBI L7_BASIS (CAFD 00000760, author Bundang Thunder 1 Series, series F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83), CFAS_PLX_1 (CAFD 000000B5, author Bundang Thunder 1 Series, series F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83), TRSVC (CAFD 00000223, author Bundang Thunder 1 Series, series F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83), ACSM_4i (CAFD 000011AB, author Bundang Thunder 2 Series, series F64,F55,F56,F57,F45), DSC_CT02 (CAFD 0000297A, author Bundang Thunder 2 Series, series F64,F55,F56,F57,F45), GSAW01 (CAFD 0000114B, author Bundang Thunder 2 Series, series F64,F55,F56,F57,F45), BDC_01 (CAFD 000017BE, author Bundang Thunder 2 Series, series F64,F55,F56,F57,F45), HU_NBT (CAFD 00000DED, author Bundang Thunder 2 Series, series F64,F55,F56,F57,F45), IHKA_VA02 (CAFD 000016EE, author Bundang Thunder 2 Series, series F64,F55,F56,F57,F45), KAFAS2 (CAFD 00001148, author Bundang Thunder 2 Series, series F64,F55,F56,F57,F45), KOMBI L7_BASIS (CAFD 00000760, author Bundang Thunder 2 Series, series F64,F55,F56,F57,F45), CFAS_PLX_1 (CAFD 000000B5, author Bundang Thunder 2 Series, series F64,F55,F56,F57,F45), ACSM_4B (CAFD 00000911, author Bundang Thunder 3 Series, series F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83), ASD01 (CAFD 00000F9B, author Bundang Thunder 3 Series, series F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83), DSC_CT01 (CAFD 000019CC, author Bundang Thunder 3 Series, series F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83), GKEB23 (CAFD 0000023F, author Bundang Thunder 3 Series, series F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83), FEM_01 (CAFD 00000794, author Bundang Thunder 3 Series, series F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83), HU_NBT (CAFD 00000DED, author Bundang Thunder 3 Series, series F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83), ICMQL (CAFD 0000067B, author Bundang Thunder 3 Series, series F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83), IHKA_VA02 (CAFD 000016EE, author Bundang Thunder 3 Series, series F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83), KAFAS2 (CAFD 00001148, author Bundang Thunder 3 Series, series F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83), KOMBI FPK_I12 (CAFD 000009C8, author Bundang Thunder 3 Series, series F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83), CFAS_PLX_1 (CAFD 000000B5, author Bundang Thunder 3 Series, series F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83), TRSVC (CAFD 00000223, author Bundang Thunder 3 Series, series F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83), ACSM_4B (CAFD 00000911, author Bundang Thunder 4 Series, series F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83), ASD01 (CAFD 00000F9B, author Bundang Thunder 4 Series, series F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83), DSC_CT01 (CAFD 000019CC, author Bundang Thunder 4 Series, series F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83), GKEB23 (CAFD 0000023F, author Bundang Thunder 4 Series, series F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83), FEM_01 (CAFD 00000794, author Bundang Thunder 4 Series, series F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83), HU_NBT (CAFD 00000DED, author Bundang Thunder 4 Series, series F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83), ICMQL (CAFD 0000067B, author Bundang Thunder 4 Series, series F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83), IHKA_VA02 (CAFD 000016EE, author Bundang Thunder 4 Series, series F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83), KAFAS2 (CAFD 00001148, author Bundang Thunder 4 Series, series F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83), KOMBI L7_MID (CAFD 000009C8, author Bundang Thunder 4 Series, series F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83), CFAS_PLX_1 (CAFD 000000B5, author Bundang Thunder 4 Series, series F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83), TRSVC (CAFD 00000223, author Bundang Thunder 4 Series, series F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83), ACSM_4C (CAFD 00000909, author Bundang Thunder 5 Series, series F06,F10,F11,F12,F13,F18), ASD01 (CAFD 00000F9B, author Bundang Thunder 5 Series, series F06,F10,F11,F12,F13,F18), CAS_04 (CAFD 0000000F, author Bundang Thunder 5 Series, series F06,F10,F11,F12,F13,F18), DSC_Premium (CAFD 00000C18, author Bundang Thunder 5 Series, series F06,F10,F11,F12,F13,F18), GKEB23 (CAFD 0000023F, author Bundang Thunder 5 Series, series F06,F10,F11,F12,F13,F18), FRM__03CT (CAFD 0000106D, author Bundang Thunder 5 Series, series F06,F10,F11,F12,F13,F18), FRM_03CT (CAFD 0000012F, author Bundang Thunder 5 Series, series F06,F10,F11,F12,F13,F18), FZD__04 (CAFD 00000552, author Bundang Thunder 5 Series, series F06,F10,F11,F12,F13,F18), HKFM (CAFD 000007C8, author Bundang Thunder 5 Series, series F06,F10,F11,F12,F13,F18), HU_CICHB (CAFD 000000F9, author Bundang Thunder 5 Series, series F06,F10,F11,F12,F13,F18), HU_NBT (CAFD 00000DED, author Bundang Thunder 5 Series, series F06,F10,F11,F12,F13,F18), ICMQL (CAFD 0000067B, author Bundang Thunder 5 Series, series F06,F10,F11,F12,F13,F18), IHKA_CBF (CAFD 00000092, author Bundang Thunder 5 Series, series F06,F10,F11,F12,F13,F18), JBBFE (CAFD 00000014, author Bundang Thunder 5 Series, series F06,F10,F11,F12,F13,F18), KAFAS2 (CAFD 00001148, author Bundang Thunder 5 Series, series F06,F10,F11,F12,F13,F18), KOMBI FPK_I12 (CAFD 00001060, author Bundang Thunder 5 Series, series F06,F10,F11,F12,F13,F18), KOMBI L6 BO (CAFD 00000069, author Bundang Thunder 5 Series, series F06,F10,F11,F12,F13,F18), JBBF_E3_PDC (CAFD 00000018, author Bundang Thunder 5 Series, series F06,F10,F11,F12,F13,F18), ? (CAFD , author unknown, series F06,F10,F11,F12,F13,F18), CBFS_PLX_1 (CAFD 000000B6, author Bundang Thunder 5 Series, series F06,F10,F11,F12,F13,F18), SZL_LWS_03 (CAFD 0000033D, author Bundang Thunder 5 Series, series F06,F10,F11,F12,F13,F18), TRSVC (CAFD 00000223, author Bundang Thunder 5 Series, series F06,F10,F11,F12,F13,F18), ACSM_4B (CAFD 00000911, author Bundang Thunder 3GT, series F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83), DSC_CT01 (CAFD 000019CC, author Bundang Thunder 3GT, series F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83), GKEB23 (CAFD 0000023F, author Bundang Thunder 3GT, series F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83), FEM_01 (CAFD 00000794, author Bundang Thunder 3GT, series F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83), HKFM (CAFD 0000157F, author Bundang Thunder 3GT, series F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83), HU_NBT_EVO (CAFD 00001EF6, author Bundang Thunder 3GT, series F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83), ICMQL (CAFD 0000067B, author Bundang Thunder 3GT, series F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83), IHKA_VA02 (CAFD 000016EE, author Bundang Thunder 3GT, series F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83), Kafas2 (CAFD 00001148, author Bundang Thunder 3GT, series F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83), KOMBI L7_MID (CAFD 000009C8, author Bundang Thunder 3GT, series F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83), CFAS_PLX_1 (CAFD 000000B5, author Bundang Thunder 3GT, series F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83), CBFS_PLX_1 (CAFD 000000B6, author Bundang Thunder 3GT, series F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83), TRSVC (CAFD 00000223, author Bundang Thunder 3GT, series F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83), ACSM_4C (CAFD 00000909, author Bundang Thunder 5GT, series F01,F02,F03,F04,F07), CAS_04 (CAFD 0000000F, author Bundang Thunder 5GT, series F01,F02,F03,F04,F07), DSC_Premium (CAFD 00000C18, author Bundang Thunder 5GT, series F01,F02,F03,F04,F07), GKEB23 (CAFD 0000023F, author Bundang Thunder 5GT, series F01,F02,F03,F04,F07), FRM_03CT (CAFD 0000106D, author Bundang Thunder 5GT, series F01,F02,F03,F04,F07), FZD__04 (CAFD 00000552, author Bundang Thunder 5GT, series F01,F02,F03,F04,F07), HKFM (CAFD 000007C8, author Bundang Thunder 5GT, series F01,F02,F03,F04,F07), HU_NBT (CAFD 00000DED, author Bundang Thunder 5GT, series F01,F02,F03,F04,F07), ICMQL (CAFD 0000067B, author Bundang Thunder 5GT, series F01,F02,F03,F04,F07), IHKA_CBF (CAFD 00000092, author Bundang Thunder 5GT, series F01,F02,F03,F04,F07), JBBFE (CAFD 00000014, author Bundang Thunder 5GT, series F01,F02,F03,F04,F07), Kafas2 (CAFD 00001148, author Bundang Thunder 5GT, series F01,F02,F03,F04,F07), KOMBI FPK_I12 (CAFD 00001060, author Bundang Thunder 5GT, series F01,F02,F03,F04,F07), KOMBI L6 BO (CAFD 00000069, author Bundang Thunder 5GT, series F01,F02,F03,F04,F07), JBBF_E3_PDC (CAFD 00000018, author Bundang Thunder 5GT, series F01,F02,F03,F04,F07), CFAS_PLX_1 (CAFD 000000B5, author Bundang Thunder 5GT, series F01,F02,F03,F04,F07), CBFS_PLX_1 (CAFD 000000B6, author Bundang Thunder 5GT, series F01,F02,F03,F04,F07), CFAS_PLX_1 (CAFD 000000B5, author Bundang Thunder 5GT, series F01,F02,F03,F04,F07), SZL_LWS_03 (CAFD 0000033D, author Bundang Thunder 5GT, series F01,F02,F03,F04,F07), TRSVC (CAFD 00000223, author Bundang Thunder 5GT, series F01,F02,F03,F04,F07), ACSM_4C (CAFD 00000909, author Bundang Thunder X3, series F15,F16,F25,F26,F48,F85,F86), CAS_04 (CAFD 0000000F, author Bundang Thunder X3, series F15,F16,F25,F26,F48,F85,F86), DXC_CT01 (CAFD 00000629, author Bundang Thunder X3, series F15,F16,F25,F26,F48,F85,F86), FRM__03CT (CAFD 0000106D, author Bundang Thunder X3, series F15,F16,F25,F26,F48,F85,F86), HKFM (CAFD 000007C8, author Bundang Thunder X3, series F15,F16,F25,F26,F48,F85,F86), HU_NBT_EVO (CAFD 00001EF6, author Bundang Thunder X3, series F15,F16,F25,F26,F48,F85,F86), ICMQL (CAFD 0000067B, author Bundang Thunder X3, series F15,F16,F25,F26,F48,F85,F86), IHKA_HIGH (CAFD 000006DE, author Bundang Thunder X3, series F15,F16,F25,F26,F48,F85,F86), JBBFE (CAFD 00000014, author Bundang Thunder X3, series F15,F16,F25,F26,F48,F85,F86), KAFAS2 (CAFD 00001148, author Bundang Thunder X3, series F15,F16,F25,F26,F48,F85,F86), KOMBI L6 BO (CAFD 00000069, author Bundang Thunder X3, series F15,F16,F25,F26,F48,F85,F86), CFAS_PLX_1 (CAFD 000000B5, author Bundang Thunder X3, series F15,F16,F25,F26,F48,F85,F86), CBFS_PLX_1 (CAFD 000000B6, author Bundang Thunder X3, series F15,F16,F25,F26,F48,F85,F86), CFAS_PLX_1 (CAFD 000000B5, author Bundang Thunder X3, series F15,F16,F25,F26,F48,F85,F86), ACSM_4C (CAFD 00000909, author Bundang Thunder X5, series F15,F16,F25,F26,F48,F85,F86), BDC_01 (CAFD 000017BE, author Bundang Thunder X5, series F15,F16,F25,F26,F48,F85,F86), HKFM (CAFD 000007C8, author Bundang Thunder X5, series F15,F16,F25,F26,F48,F85,F86), HU_NBT (CAFD 00000DED, author Bundang Thunder X5, series F15,F16,F25,F26,F48,F85,F86), ICMQL (CAFD 0000067B, author Bundang Thunder X5, series F15,F16,F25,F26,F48,F85,F86), IHKA_CBF (CAFD 000047D6, author Bundang Thunder X5, series F15,F16,F25,F26,F48,F85,F86), JBBFE (CAFD 00000014, author Bundang Thunder X5, series F15,F16,F25,F26,F48,F85,F86), KAFAS2 (CAFD 00001148, author Bundang Thunder X5, series F15,F16,F25,F26,F48,F85,F86), KOMBI FPK_I12 (CAFD 00001060, author Bundang Thunder X5, series F15,F16,F25,F26,F48,F85,F86), CFAS_PLX_1 (CAFD 000000B5, author Bundang Thunder X5, series F15,F16,F25,F26,F48,F85,F86), CBFS_PLX_1 (CAFD 000000B6, author Bundang Thunder X5, series F15,F16,F25,F26,F48,F85,F86), ACSM_4C (CAFD 00000909, author Bundang Thunder X6, series F15,F16,F25,F26,F48,F85,F86), BDC_01 (CAFD 000017BE, author Bundang Thunder X6, series F15,F16,F25,F26,F48,F85,F86), HKFM (CAFD 000007C8, author Bundang Thunder X6, series F15,F16,F25,F26,F48,F85,F86), HU_NBT (CAFD 00000DED, author Bundang Thunder X6, series F15,F16,F25,F26,F48,F85,F86), ICMQL (CAFD 0000067B, author Bundang Thunder X6, series F15,F16,F25,F26,F48,F85,F86), IHKA_CBF (CAFD 000047D6, author Bundang Thunder X6, series F15,F16,F25,F26,F48,F85,F86), JBBFE (CAFD 00000014, author Bundang Thunder X6, series F15,F16,F25,F26,F48,F85,F86), KAFAS2 (CAFD 00001148, author Bundang Thunder X6, series F15,F16,F25,F26,F48,F85,F86), KOMBI FPK_I12 (CAFD 00001060, author Bundang Thunder X6, series F15,F16,F25,F26,F48,F85,F86), CFAS_PLX_1 (CAFD 000000B5, author Bundang Thunder X6, series F15,F16,F25,F26,F48,F85,F86), CBFS_PLX_1 (CAFD 000000B6, author Bundang Thunder X6, series F15,F16,F25,F26,F48,F85,F86), ACSM_3 (CAFD 0000009C, author Bundang Thunder 7 Series, series F01,F02,F03,F04,F07), CAS_04 (CAFD 0000000F, author Bundang Thunder 7 Series, series F01,F02,F03,F04,F07), DSC_Premium (CAFD 000000D8, author Bundang Thunder 7 Series, series F01,F02,F03,F04,F07), FRM__03CT (CAFD 0000012F, author Bundang Thunder 7 Series, series F01,F02,F03,F04,F07), FZD__04 (CAFD 00000552, author Bundang Thunder 7 Series, series F01,F02,F03,F04,F07), HKFM (CAFD 000007C8, author Bundang Thunder 7 Series, series F01,F02,F03,F04,F07), FZD__04 (CAFD 00000552, author Bundang Thunder 7 Series, series F01,F02,F03,F04,F07), HU_CICHB (CAFD 000000F9, author Bundang Thunder 7 Series, series F01,F02,F03,F04,F07), HU_NBT (CAFD 00000DED, author Bundang Thunder 7 Series, series F01,F02,F03,F04,F07), ICMQL (CAFD 00000052, author Bundang Thunder 7 Series, series F01,F02,F03,F04,F07), IHKA_CBF (CAFD 00000092, author Bundang Thunder 7 Series, series F01,F02,F03,F04,F07), JBBFE (CAFD 00000014, author Bundang Thunder 7 Series, series F01,F02,F03,F04,F07), JBBF_E3_PDC (CAFD 00000018, author Bundang Thunder 7 Series, series F01,F02,F03,F04,F07), KOMBI L6 BO (CAFD 00000069, author Bundang Thunder 7 Series, series F01,F02,F03,F04,F07), SZL_LWS_03 (CAFD 0000033D, author Bundang Thunder 7 Series, series F01,F02,F03,F04,F07), TRSVC (CAFD 00000223, author Bundang Thunder 7 Series, series F01,F02,F03,F04,F07), CFAS_PLX_1 (CAFD 000000B5, author Bundang Thunder 7 Series, series F01,F02,F03,F04,F07), CBFS_PLX_1 (CAFD 000000B6, author Bundang Thunder 7 Series, series F01,F02,F03,F04,F07)

### ACSM_5 (CAFD 00001B29) — authored by Bundang Thunder G Series | Series: G11, G30

* **Seat belt warning chime for only 5 seconds                                                                                 --** by Bundang Thunder ^^**
  * Group `3001`
    * `05` (start=11, mask=11111111b, comment=GWF_SBR_WARNDAUER)

* **Delete driver seat belt warning light**
  * Group `3001`
    * `00` (start=3, mask=00000001b, comment=SBR_PreWarning_Fahrer)

* **Delete passenger seat belt warning light**
  * Group `3001`
    * `00` (start=4, mask=00000001b, comment=SBR_PreWarning_Beifahrer)

* **Disable driver seat belt warning chime**
  * Group `3001`
    * `00` (start=1, mask=00000001b, comment=SeatBeltReminder_Fahrer)

* **Disable passenger seat belt warning chime**
  * Group `3001`
    * `00` (start=2, mask=00000001b, comment=SeatBeltReminder_Beifahrer)

### BDC_01 (CAFD 00001DF7) — authored by Bundang Thunder G Series | Series: G11, G30

* **Allow front windows to keep closing with door open --** by Bundang Thunder ^^**
  * Group `3510`
    * `00` (start=0, mask=00000001b, comment=FH_TUERAUF_STOP_MAUT)

* **Allow rear windows to keep closing with door open**
  * Group `3511`
    * `00` (start=0, mask=00000001b, comment=FH_TUERAUF_STOP_MAUT_REAR)

* **Fold mirrors immediately when locking (lock folding)**
  * Group `3514`
    * `00` (start=10, mask=11111111b, comment=KOMFORT_SCHLIESSEN)

### BDC_01 (CAFD 000017BC) — authored by Bundang Thunder G Series | Series: G11, G30

* **Double horn when locking with engine running - enable                                                  --** by Bundang Thunder ^^**
  * Group `3040`
    * `01` (start=1, mask=00000001b, comment=VAM_HORN_AT_SECURE)

* **Double horn when locking with engine running - disable**
  * Group `3040`
    * `00` (start=1, mask=00000001b, comment=VAM_HORN_AT_SECURE)

* **Limit passenger mirror tilt to 30 degrees in reverse**
  * Group `3110`
    * `1E` (start=1, mask=11111111b, comment=ASP_BORDSTEINAUTOMATIK_DELTA)

* **Door lock speed: 16 km/h**
  * Group `3040`
    * `10` (start=11, mask=11111111b, comment=VAM_SPEED_LIMIT_PIA_AUTO_LOCK)

### DME_DDE8xx (CAFD 000029B7) — authored by Bundang Thunder G Series | Series: G11, G30

* **Remember last auto start/stop state                                                                             --** by Bundang Thunder ^^**
  * Group `3020`
    * `01` (start=39, mask=00000011b, comment=TCM_MSA_MEMORY)

### FZD__35 (CAFD 00001D92) — authored by Bundang Thunder G Series | Series: G11, G30

* **Door open/close chime --** by Bundang Thunder ^^**
  * Group `3002`
    * `01` (start=5, mask=00110000b, comment=Akkustische Quittierung Schaerfen)
    * `01` (start=5, mask=01000000b, comment=Akkustische Quittierung Entschaerfen)

### HKFM_2015 (CAFD 00002098) — authored by Bundang Thunder G Series | Series: G11, G30

* **Footwell switch: auto-close trunk --** by Bundang Thunder ^^**
  * Group `3009`
    * `00` (start=0, mask=00001000b, comment=HKL_ROCKERSWITCHPOS2_LONGPRESS_CLOSE)
    * `00, 00` (start=2, end=3, mask=11111111b, comment=HKL_ROCKERSWITCHPOS2_DELAY_CLOSE)

* **Remote: auto-close trunk**
  * Group `300B`
    * `00` (start=0, mask=00001000b, comment=HKL_REMOTECONTROLLIFTGATEBUTTON_LONGPRESS_CLOSE)
    * `00, 00` (start=2, end=3, mask=11111111b, comment=HKL_REMOTECONTROLLIFTGATEBUTTON_DELAY_CLOSE)

### HU_NBT_EVO (CAFD 00001EF6) — authored by Bundang Thunder G Series | Series: G11, G30

* **Set time automatically                                                                                         --** by Bundang Thunder ^^**
  * Group `3000`
    * `navigation` (start=19, mask=00000110b, comment=SETTINGS_TIME_AUTOMATIC)
    * `01` (start=105, mask=00100000b, comment=CLOCK_CHANGE_AUTOMATIC)

* **Watch video/DMB/navigation while driving (up to 63 km/h)**
  * Group `3006`
    * `1F` (start=26, mask=11111111b, comment=SPEEDLOCK_X_KMH_MAX)
    * `3F` (start=25, mask=11111111b, comment=SPEEDLOCK_X_KMH_MIN)
  * Group `3000`
    * `3F` (start=147, mask=00111111b, comment=SPEEDLOCK_SPEEDVALUE_MAX)
    * `1F` (start=146, mask=00011111b, comment=SPEEDLOCK_SPEEDVALUE_MIN)
    * `00` (start=5, mask=00010000b, comment=VIDEO_FRONT_LOCKED)
    * `00` (start=5, mask=00000100b, comment=VIDEO_HANDBRAKE)
    * `None` (start=2, mask=00000111b, comment=VIDEO_SPEEDLOCK_CONDITION)

* **Suppress all warning messages**
  * Group `3001`
    * `kein_ld` (start=58, mask=11111111b, comment=LEGAL_DISCLAIMER_TIME)
    * `kein_ld` (start=52, mask=11111111b, comment=MACRO_CAM_LEGALDISCLAIMER)

* **Enable trailer zoom menu when reversing**
  * Group `3001`
    * `01` (start=54, mask=00000001b, comment=MACRO_TRAILER_COUPLING)

* **Close windows when it rains**
  * Group `3000`
    * `01` (start=19, mask=00001000b, comment=REGEN_SCHLIESSEN)

* **X-Drive**
  * Group `3000`
    * `01` (start=5, mask=00000001b, comment=COMPASS)
    * `01` (start=15, mask=00000001b, comment=X_VIEW)
    * `trajectory1` (start=26, mask=00110000b, comment=X_VIEW_GRAPHIC_SLOP)
    * `trajectory1` (start=26, mask=11000000b, comment=X_VIEW_GRAPHIC_ROLL)
    * `01` (start=110, mask=00000010b, comment=MOMENTDISTRIBUTION_MENU)

* **Enable USB video playback 1/2**
  * Group `3000`
    * `01` (start=15, mask=00010000b, comment=ENT_CODEC_OGG)
    * `01` (start=15, mask=00100000b, comment=ENT_CODEC_XVID)
    * `01` (start=15, mask=01000000b, comment=ENT_CODEC_VCD)
    * `01` (start=13, mask=00000100b, comment=ENT_MC_VIDEO_SUPPORT)

* **Enable USB video playback 2/2**
  * Group `3003`
    * `both` (start=32, mask=00000110b, comment=API_USB_VIDEO)
    * `both` (start=32, mask=00011000b, comment=API_IPOD_VIDEO)

* **USB hub settings**
  * Group `3001`
    * `both` (start=20, mask=00000011b, comment=USB_HUB_AVAIL)

* **Change warning chime to Rolls-Royce sound**
  * Group `3002`
    * `rolls_royce` (start=26, mask=00111000b, comment=SOUND_SIGNAL_SET)

* **Configure Sport mode**
  * Group `3008`
    * `popup_and_config` (start=79, mask=11000000b, comment=MACRO_FDS)
  * Group `3009`
    * `01` (start=9, mask=00010000b, comment=EFF_DYN_SPORT_CID)
    * `01` (start=9, mask=00100000b, comment=EFF_DYN_SPORT_UNIT)

* **Startup animation**
  * Group `3001`
    * `animation` (start=62, mask=00000110b, comment=STARTUP_TYPE)
    * `variant_01` (start=62, mask=01111000b, comment=STARTUP_EMBLEM)

* **Volume adjustment bar**
  * Group `3002`
    * `01` (start=52, mask=01000000b, comment=VOLUME_POPUP_DISPLAY)
    * `01` (start=52, mask=10000000b, comment=VOLUME_POPUP_REJECTION)
    * `01` (start=53, mask=00000001b, comment=VOLUME_POPUP_EXCEPTION)

* **Show currently playing album art in iDrive**
  * Group `3000`
    * `01` (start=9, mask=00000100b, comment=ENT_BTAS_IAP_COVERART)
  * Group `3003`
    * `01` (start=19, mask=00000100b, comment=ENT_BTAS_METADATA)
    * `01` (start=19, mask=00001000b, comment=ENT_BTAS_BROWSING)

* **Adjust audio CD album art size**
  * Group `3000`
    * `01` (start=14, mask=00100000b, comment=ENT_MC_COVER_SCALE)

* **Display Sport mode**
  * Group `3009`
    * `01` (start=9, mask=00010000b, comment=EFF_DYN_SPORT_CID)

* **Show phone, entertainment, and voice prompts in HUD**
  * Group `300C`
    * `01` (start=0, mask=00001000b, comment=HUD_ENTERTAINMENTLIST)
    * `01` (start=0, mask=10000000b, comment=HUD_VZA)

* **Configure WLAN streaming audio album art**
  * Group `3000`
    * `01` (start=9, mask=00000001b, comment=ENT_MC_WLAN_STREAM_DMP_COVERART)

* **Configure WLAN video streaming**
  * Group `300C`
    * `01` (start=9, mask=00000010b, comment=ENT_MC_WLAN_STREAM_DMP_VIDEO)

* **Install Gracenote database**
  * Group `3000`
    * `01` (start=14, mask=010000010, comment=ENT_GRACENOTE_INSTALLED)

* **Install Gracenote database via PC or USB**
  * Group `3000`
    * `01` (start=15, mask=00000010b, comment=ENT_GRACENOTE_USB)

* **Show M logo in HUD**
  * Group `300C`
    * `01` (start=0, mask=00100000b, comment=HUD_M)

* **Show turn signals in HUD**
  * Group `300C`
    * `01` (start=0, mask=01000000b, comment=HUD_TURNSIGNAL)

* **Show TPMC tire pressure temperature**
  * Group `3001`
    * `druck_und_temperatur` (start=66, mask=00001100b, comment=RDC_DRUCK_TEMP)

* **TPMC tire pressure monitor**
  * Group `3001`
    * `01` (start=1, mask=00100000b, comment=RDC_SAFETY)

* **Output ringtone through speakers (iPhone only)**
  * Group `3003`
    * `01` (start=6, mask=10000000b, comment=INBAND_RINGING)

* **Show time in incoming call list**
  * Group `3003`
    * `01` (start=1, mask=01000000b, comment=TIMESTAMP_DISPLAY)

* **Send email or text via voice**
  * Group `3003`
    * `01` (start=1, mask=00010000b, comment=SPEECH_2_TEXT)

* **Mirroring**
  * Group `3004`
    * `01` (start=15, mask=01000000b, comment=MIRRORING)

* **Mirroring settings**
  * Group `3000`
    * `01` (start=6, mask=10000000b, comment=ENT_MIRACAST)

* **Mirroring: display settings**
  * Group `3000`
    * `01` (start=30, mask=10000000b, comment=ENT_MIRACAST_DISPLAY_SETTINGS)

* **Mirroring: Wi-Fi Direct mode settings**
  * Group `3003`
    * `01` (start=21, mask=00000010b, comment=WLAN_WIFI_DIRECT)

* **Mirroring: Wi-Fi on/off mode settings**
  * Group `3003`
    * `01` (start=20, mask=10000000b, comment=WLAN_STATUS)

* **Mirroring: Wi-Fi on/off mode settings**
  * Group `3003`
    * `01` (start=9, mask=00000001b, comment=ENT_MC_WLAN_STREAM_DMP)

* **Office message length in menu: hide details**
  * Group `3003`
    * `00` (start=11, mask=00000111b, comment=PIM_DRIVING_TEXT_LENGTH)

* **Office message length in menu: up to one page**
  * Group `3003`
    * `01` (start=11, mask=00000111b, comment=PIM_DRIVING_TEXT_LENGTH)

* **Office message length in menu: up to three pages**
  * Group `3003`
    * `02` (start=11, mask=00000111b, comment=PIM_DRIVING_TEXT_LENGTH)

* **Office message length in menu: show entire message**
  * Group `3003`
    * `07` (start=11, mask=00000111b, comment=PIM_DRIVING_TEXT_LENGTH)

* **Lock/unlock confirmation chime (requires piezo buzzer sensor)**
  * Group `3000`
    * `01` (start=110, mask=00000001b, comment=ACOUSTICAL_LOCK_CONFIRM)

* **Change M Sport display cluster colors**
  * Group `3000`
    * `01` (start=133, mask=01000000b, comment=M_VEHICLE)

* **Adjust high-beam assistant in iDrive**
  * Group `3000`
    * `01` (start=109, mask=10000000b, comment=HIGH_BEAM_ASSISTANT)

* **Adjust DRL menu display in iDrive**
  * Group `3000`
    * `02` (start=92, mask=00011000b, comment=DAYDRIVING_LIGHT)

* **Unlock DVD region code**
  * Group `3000`
    * `alle_anderen` (start=7, mask=11111111b, comment=ENT_VIDEO_DVD_AREA_CODE)

* **Set sound system to Bang & Olufsen**
  * Group `3000`
    * `keine_insz` (start=21, mask=01100000b, comment=HIGH_END_AUDIO_B_UND_W)

* **Enable Logic7 (S667A HiFi vehicles)**
  * Group `3000`
    * `01` (start=22, mask=00001000b, comment=LOGIC7_SYMBOL)

* **Enhance audio mid-bass**
  * Group `3002`
    * `highpremium` (start=29, mask=00111100b, comment=AUDIO_SYSTEM)
    * `variant3` (start=21, mask=00000011b, comment=AUDIO_SYSTEM_VAR)

* **Change equalizer**
  * Group `3002`
    * `variant8` (start=31, mask=00000111b, comment=EQ_VARIANT)

* **Navigation auto zoom**
  * Group `3006`
    * `01` (start=6, mask=00000010b, comment=EQ_VARIANT)

* **Load navigation route log from USB**
  * Group `3006`
    * `01` (start=3, mask=01000000b, comment=NAVI_ROUTE_RECORD)

* **Send navigation route log to USB**
  * Group `3006`
    * `01` (start=7, mask=00000100b, comment=NAVI_ROUTE_RECORD)

* **Adjust ambient lighting independently**
  * Group `3000`
    * `01` (start=107, mask=00000100b, comment=INDIVIDUAL_AMBIENTELICHT)

* **Ambient lighting: set to Sport**
  * Group `3000`
    * `01` (start=109, mask=01110000b, comment=COLOUR_SWITCH_LINES)

* **Ambient lighting: set to Urban**
  * Group `3000`
    * `02` (start=109, mask=01110000b, comment=COLOUR_SWITCH_LINES)

* **Ambient lighting: set to Modern**
  * Group `3000`
    * `03` (start=109, mask=01110000b, comment=COLOUR_SWITCH_LINES)

* **Ambient lighting: set to Luxury**
  * Group `3000`
    * `04` (start=109, mask=01110000b, comment=COLOUR_SWITCH_LINES)

* **Enable NFC beam**
  * Group `3000`
    * `01` (start=12, mask=00010000b, comment=NFC_BEAM_SPEEDLOCK)

* **Show instantaneous fuel economy in instrument cluster**
  * Group `3000`
    * `01` (start=10, mask=00100000b, comment=MOMENTANVERBRAUCHSANZEIGE)

### DSC_EBS460 (CAFD 00002060) — authored by Bundang Thunder G Series | Series: G11, G30

* **Release parking brake by pressing accelerator only --** by Bundang Thunder ^^**
  * Group `3000`
    * `01` (start=20, mask=00010000b, comment=C_Funktion_AutomaticDriveawayRelease_01_l)

* **Enable launch control (also enables EGS)**
  * Group `3000`
    * `01` (start=26, mask=00001000b, comment=C_Funktion_LaunchControl_01_l)

### KAFAS (CAFD 00002089) — authored by Bundang Thunder G Series | Series: G11, G30

* **Automatic high-beam assistant                                                                                --** by Bundang Thunder ^^**
  * Group `3001`
    * `FLA_on` (start=0, mask=11111111b, comment=C_FLA_ON_OFF)

### EGS_ZFB_CC (CAFD 00002458) — authored by Bundang Thunder G Series | Series: G11, G30

* **Display gear number in Dynamic Sport mode                                                                  --** by Bundang Thunder ^^**
  * Group `3000`
    * `01` (start=3, mask=00000001b, comment=SPORTSCHALTER)

### IHKA_PR01 (CAFD 000022D3) — authored by Bundang Thunder G Series | Series: G11, G30

* **Remember last air conditioning state                                                                               --** by Bundang Thunder ^^**
  * Group `3003`
    * `01` (start=0, mask=00000010b, comment=MEMORY_OFF)

* **Prevent AUTO button from turning on A/C**
  * Group `3003`
    * `00` (start=0, mask=00000100b, comment=AC_ON_WITH_AUTO)

* **Remember HVAC recirculation mode**
  * Group `3003`
    * `01` (start=0, mask=00000001b, comment=MEMORY_UMLUFT)

### Kombi (CAFD 00002660) — authored by Bundang Thunder G Series | Series: G11, G30

* **Show phone, entertainment, and voice prompts in HUD                                                               --** by Bundang Thunder ^^**
  * Group `3000`
    * `01` (start=45, mask=00001000b, comment=HUD_ENTERTAINMENT_ENABLE)
    * `01` (start=43, mask=10000000b, comment=HUD_STARTUP_LOGO_ENABLE)
    * `01` (start=4, mask=00100000b, comment=TLC_ENABLE)
    * `01` (start=44, mask=10000000b, comment=HUD_VZA_ENABLE)

* **Instrument cluster logo: none**
  * Group `3001`
    * `00` (start=18, mask=11111111b, comment=LOGO_SCHRIFTZUG)

* **Instrument cluster logo: e-drive**
  * Group `3001`
    * `01` (start=18, mask=11111111b, comment=LOGO_SCHRIFTZUG)

* **Instrument cluster logo: msp**
  * Group `3001`
    * `02` (start=18, mask=11111111b, comment=LOGO_SCHRIFTZUG)

* **Instrument cluster logo: m550i**
  * Group `3001`
    * `03` (start=18, mask=11111111b, comment=LOGO_SCHRIFTZUG)

* **Instrument cluster logo: m550d**
  * Group `3001`
    * `04` (start=18, mask=11111111b, comment=LOGO_SCHRIFTZUG)

* **Instrument cluster logo: m40d**
  * Group `3001`
    * `05` (start=18, mask=11111111b, comment=LOGO_SCHRIFTZUG)

* **Instrument cluster logo: m760i**
  * Group `3001`
    * `06` (start=18, mask=11111111b, comment=LOGO_SCHRIFTZUG)

* **Instrument cluster logo: m760li**
  * Group `3001`
    * `07` (start=18, mask=11111111b, comment=LOGO_SCHRIFTZUG)

* **Instrument cluster logo: b7_biturbo**
  * Group `3001`
    * `08` (start=18, mask=11111111b, comment=LOGO_SCHRIFTZUG)

* **Instrument cluster logo: b7**
  * Group `3001`
    * `09` (start=18, mask=11111111b, comment=LOGO_SCHRIFTZUG)

* **Instrument cluster logo: b6_biturbo**
  * Group `3001`
    * `0A` (start=18, mask=11111111b, comment=LOGO_SCHRIFTZUG)

* **Instrument cluster logo: b6**
  * Group `3001`
    * `0B` (start=18, mask=11111111b, comment=LOGO_SCHRIFTZUG)

* **Instrument cluster logo: b5_biturbo**
  * Group `3001`
    * `0C` (start=18, mask=11111111b, comment=LOGO_SCHRIFTZUG)

* **Instrument cluster logo: d5_biturbo**
  * Group `3001`
    * `0D` (start=18, mask=11111111b, comment=LOGO_SCHRIFTZUG)

* **Instrument cluster logo: xd3_biturbo**
  * Group `3001`
    * `0E` (start=18, mask=11111111b, comment=LOGO_SCHRIFTZUG)

* **Instrument cluster logo: m750_ld**
  * Group `3001`
    * `0F` (start=18, mask=11111111b, comment=LOGO_SCHRIFTZUG)

* **Instrument cluster logo: m750_d**
  * Group `3001`
    * `10` (start=18, mask=11111111b, comment=LOGO_SCHRIFTZUG)

* **Instrument cluster logo: v12**
  * Group `3001`
    * `11` (start=18, mask=11111111b, comment=LOGO_SCHRIFTZUG)

* **Show compass in instrument cluster**
  * Group `3000`
    * `01` (start=89, mask=10000000b, comment=KOMPASS_ENABLE)

* **Disable warning chime below 3 degrees**
  * Group `3000`
    * `00` (start=94, mask=00010000b, comment=TEMPERATURWARNUNG)

* **Sound warning when reverse gear engages**
  * Group `3000`
    * `01` (start=1, mask=00010000b, comment=R_GANG_AKUSTIK_ENABLE)

* **Fuel low warning threshold: 6 liters**
  * Group `3006`
    * `18` (start=0, mask=11111111b, comment=TNK_SCHWELLE_RESERVE)

* **Fuel low warning threshold: 8 liters**
  * Group `3006`
    * `20` (start=0, mask=11111111b, comment=TNK_SCHWELLE_RESERVE)

* **Fuel low warning threshold: 9 liters**
  * Group `3006`
    * `24` (start=0, mask=11111111b, comment=TNK_SCHWELLE_RESERVE)

* **Fuel low warning threshold: 10 liters**
  * Group `3006`
    * `28` (start=0, mask=11111111b, comment=TNK_SCHWELLE_RESERVE)

* **Fuel low warning threshold: 12 liters**
  * Group `3006`
    * `30` (start=0, mask=11111111b, comment=TNK_SCHWELLE_RESERVE)

### CBFS_S15 (CAFD 0000225A) — authored by Bundang Thunder G Series | Series: G11, G30

* **Enable Easy Access                                                                         --** by Bundang Thunder ^^**
  * Group `3000`
    * `01` (start=0, mask=00011100b, comment=EINAUSSTIEGSHILFE)

* **Easy Access seat starts moving from end position**
  * Group `3012`
    * `00, 01` (start=4, end=5, mask=11111111b, comment=EAH_SCHUTZFREIRAUM_HINTEN_SLV_PHYS)

* **Easy Access seat starts moving with 1 cm remaining**
  * Group `3012`
    * `00, 0A` (start=4, end=5, mask=11111111b, comment=EAH_SCHUTZFREIRAUM_HINTEN_SLV_PHYS)

* **Easy Access seat starts moving with 2 cm remaining**
  * Group `3012`
    * `00, 14` (start=4, end=5, mask=11111111b, comment=EAH_SCHUTZFREIRAUM_HINTEN_SLV_PHYS)

* **Easy Access seat starts moving with 3 cm remaining**
  * Group `3012`
    * `00, 1E` (start=4, end=5, mask=11111111b, comment=EAH_SCHUTZFREIRAUM_HINTEN_SLV_PHYS)

* **Easy Access seat travel distance: 4 cm**
  * Group `3012`
    * `00, 28` (start=0, end=1, mask=11111111b, comment=EAH_VERFAHRWEG_SLV_PHYS)

* **Easy Access seat travel distance: 5 cm**
  * Group `3012`
    * `00, 32` (start=0, end=1, mask=11111111b, comment=EAH_VERFAHRWEG_SLV_PHYS)

* **Easy Access seat travel distance: 6 cm**
  * Group `3012`
    * `00, 3C` (start=0, end=1, mask=11111111b, comment=EAH_VERFAHRWEG_SLV_PHYS)

* **Easy Access seat travel distance: 7 cm**
  * Group `3012`
    * `00, 46` (start=0, end=1, mask=11111111b, comment=EAH_VERFAHRWEG_SLV_PHYS)

* **Gentleman**
  * Group `3000`
    * `01` (start=1, mask=00000001b, comment=GENTLEMAN)
    * `01` (start=0, mask=00000001b, comment=MEMORY)

* **Set gong when saving seat position**
  * Group `3000`
    * `01` (start=2, mask=00100000b, comment=MEMORY_GONG)

### CFAS_S15 (CAFD 00002259) — authored by Bundang Thunder G Series | Series: G11, G30

* **Enable Easy Access                                                                         --** by Bundang Thunder ^^**
  * Group `3000`
    * `01` (start=0, mask=00011100b, comment=EINAUSSTIEGSHILFE)

* **Easy Access seat starts moving from end position**
  * Group `3012`
    * `00, 01` (start=4, end=5, mask=11111111b, comment=EAH_SCHUTZFREIRAUM_HINTEN_SLV_PHYS)

* **Easy Access seat starts moving with 1 cm remaining**
  * Group `3012`
    * `00, 0A` (start=4, end=5, mask=11111111b, comment=EAH_SCHUTZFREIRAUM_HINTEN_SLV_PHYS)

* **Easy Access seat starts moving with 2 cm remaining**
  * Group `3012`
    * `00, 14` (start=4, end=5, mask=11111111b, comment=EAH_SCHUTZFREIRAUM_HINTEN_SLV_PHYS)

* **Easy Access seat starts moving with 3 cm remaining**
  * Group `3012`
    * `00, 1E` (start=4, end=5, mask=11111111b, comment=EAH_SCHUTZFREIRAUM_HINTEN_SLV_PHYS)

* **Easy Access seat travel distance: 4 cm**
  * Group `3012`
    * `00, 28` (start=0, end=1, mask=11111111b, comment=EAH_VERFAHRWEG_SLV_PHYS)

* **Easy Access seat travel distance: 5 cm**
  * Group `3012`
    * `00, 32` (start=0, end=1, mask=11111111b, comment=EAH_VERFAHRWEG_SLV_PHYS)

* **Easy Access seat travel distance: 6 cm**
  * Group `3012`
    * `00, 3C` (start=0, end=1, mask=11111111b, comment=EAH_VERFAHRWEG_SLV_PHYS)

* **Easy Access seat travel distance: 7 cm**
  * Group `3012`
    * `00, 46` (start=0, end=1, mask=11111111b, comment=EAH_VERFAHRWEG_SLV_PHYS)

* **Gentleman**
  * Group `3000`
    * `01` (start=1, mask=00000001b, comment=GENTLEMAN)
    * `01` (start=0, mask=00000001b, comment=MEMORY)

* **Set gong when saving seat position**
  * Group `3000`
    * `01` (start=2, mask=00100000b, comment=MEMORY_GONG)

### CBFS_S15 (CAFD 0000225A) — authored by Bundang Thunder G Series | Series: G11, G30

* **Passenger seat Gentleman                                                                                         --** by Bundang Thunder ^^**
  * Group `3000`
    * `01` (start=1, mask=00000001b, comment=GENTLEMAN)
    * `01` (start=0, mask=00000001b, comment=MEMORY)

### ACSM_4i (CAFD 000011AB) — authored by Bundang Thunder i3 | Series: I001

* **Seat belt warning chime for only 5 seconds                                                                                 --** by Bundang Thunder ^^**
  * Group `3001`
    * `05` (start=11, mask=11111111b, comment=GWF_SBR_WARNDAUER)

* **Delete driver seat belt warning light**
  * Group `3001`
    * `00` (start=3, mask=00000001b, comment=SBR-Prewarning_Fahrer)

* **Delete passenger seat belt warning light**
  * Group `3001`
    * `00` (start=4, mask=00000010b, comment=SBR-Prewarning_Beifahrer)

* **Disable driver seat belt warning chime**
  * Group `3001`
    * `00` (start=1, mask=000000010b, comment=SeatBeltReminder_Fahrer)

* **Disable passenger seat belt warning chime**
  * Group `3001`
    * `00` (start=2, mask=00000001b, comment=SeatBeltReminder_Beifahrer)

### BDC_01 (CAFD 000017BE) — authored by Bundang Thunder i3 | Series: I001

* **Activate hazard lights during hard braking                                                                                   --** by Bundang Thunder ^^**
  * Group `3068`
    * `01` (start=26, mask=00000001b, comment=WB_GB_ENABLE)

* **Turn off audio when engine stops**
  * Group `3020`
    * `01` (start=9, mask=00000001b, comment=TCM_LOGIC_R_OFF_DOOR)

* **Double horn when locking with engine running - enable**
  * Group `3040`
    * `01` (start=0, mask=00000100b, comment=VAM_HORN_AT_SECURE)

* **Double horn when locking with engine running - disable**
  * Group `3040`
    * `00` (start=0, mask=00000100b, comment=VAM_HORN_AT_SECURE)

* **Fold mirrors immediately when locking (lock folding)**
  * Group `3056`
    * `00` (start=10, mask=11111111b, comment=KOMFORT_SCHLIESSEN)

* **Allow engine start in park**
  * Group `3020`
    * `00` (start=8, mask=00000010b, comment=TCM_STARTLOCK_PARK)
    * `00` (start=8, mask=00010000b, comment=TCM_STARTLOCK_DRIVINGREADINESS)

* **Turn on catch lights when reversing**
  * Group `3070`
    * `01` (start=128, mask=00000001b, comment=OVT_BEI_RUECKFAHRLICHT)

* **Door lock speed: 16 km/h**
  * Group `3040`
    * `01` (start=10, mask=11111111b, comment=VAM_SPEED_LIMIT_PIA_AUTO_LOCK)

* **Allow windows to keep closing with door open**
  * Group `3050`
    * `00` (start=0, mask=00000001b, comment=FH_TUERAUF_STOP_MAUT)

* **Limit passenger mirror tilt to 30 degrees in reverse**
  * Group `3110`
    * `1E` (start=1, mask=11111111b, comment=ASP_BORDSTEINAUTOMATIK_DELTA)

### HU_NBT (CAFD 00000DED) — authored by Bundang Thunder i3 | Series: I001

* **Set time automatically                                                                                         --** by Bundang Thunder ^^**
  * Group `3000`
    * `navigation` (start=19, mask=00000110b, comment=SETTINGS_TIME_AUTOMATIC)
    * `01` (start=105, mask=00100000b, comment=CLOCK_CHANGE_AUTOMATIC)

* **Watch video/DMB/navigation while driving**
  * Group `3000`
    * `FF` (start=72, mask=11111111b, comment=SPEEDLOCK_X_KMH_MAX)
    * `FF` (start=71, mask=11111111b, comment=SPEEDLOCK_X_KMH_MIN)
    * `00` (start=5, mask=00010000b, comment=VIDEO_FRONT_LOCKED)
    * `00` (start=5, mask=00000100b, comment=VIDEO_HANDBRAKE)
    * `None` (start=57, mask=00000111b, comment=VIDEO_SPEEDLOCK_CONDITION)

* **Suppress all warning messages**
  * Group `3001`
    * `kein_ld` (start=58, mask=11111111b, comment=LEGAL_DISCLAIMER_TIME)
    * `kein_ld` (start=52, mask=11111111b, comment=MACRO_CAM_LEGALDISCLAIMER)

* **Enable trailer zoom menu when reversing**
  * Group `3001`
    * `01` (start=54, mask=00000001b, comment=MACRO_TRAILER_COUPLING)

* **Close windows when it rains**
  * Group `3000`
    * `01` (start=19, mask=00001000b, comment=REGEN_SCHLIESSEN)

* **Change warning chime to Rolls-Royce sound**
  * Group `3002`
    * `rolls_royce` (start=26, mask=00111000b, comment=SOUND_SIGNAL_SET)

* **Show TPMC tire pressure temperature**
  * Group `3001`
    * `druck_und_temperatur` (start=66, mask=00001100b, comment=RDC_DRUCK_TEMP)

* **Output ringtone through speakers (iPhone only)**
  * Group `3003`
    * `01` (start=6, mask=10000000b, comment=INBAND_RINGING)

* **Lock/unlock confirmation chime (requires piezo buzzer sensor)**
  * Group `3000`
    * `01` (start=110, mask=00000001b, comment=ACOUSTICAL_LOCK_CONFIRM)

* **Adjust high-beam assistant in iDrive**
  * Group `3000`
    * `01` (start=109, mask=10000000b, comment=HIGH_BEAM_ASSISTANT)

* **Set sound system to Bang & Olufsen**
  * Group `3000`
    * `keine_insz` (start=21, mask=01100000b, comment=HIGH_END_AUDIO_B_UND_W)

* **Enable Logic7 (S667A HiFi vehicles)**
  * Group `3000`
    * `01` (start=22, mask=00001000b, comment=LOGIC7_SYMBOL)

* **Enhance audio mid-bass**
  * Group `3002`
    * `highpremium` (start=29, mask=00111100b, comment=AUDIO_SYSTEM)
    * `variant3` (start=21, mask=00000011b, comment=AUDIO_SYSTEM_VAR)

### IHKA_VA02 (CAFD 000016EE) — authored by Bundang Thunder i3 | Series: I001

* **Remember last air conditioning state                                                                               --** by Bundang Thunder ^^**
  * Group `3003`
    * `01` (start=0, mask=00000010b, comment=MEMORY_OFF)

* **Prevent AUTO button from turning on A/C**
  * Group `3003`
    * `00` (start=0, mask=00000100b, comment=AC_ON_WITH_AUTO)

* **Remember HVAC recirculation mode**
  * Group `3003`
    * `01` (start=0, mask=00000001b, comment=MEMORY_UMLUFT)

### ACSM_4i (CAFD 000011AB) — authored by Bundang Thunder Mini | Series: F64,F55,F56,F57,F45

* **Seat belt warning chime for only 5 seconds                                                                                 --** by Bundang Thunder ^^**
  * Group `3001`
    * `05` (start=11, mask=11111111b, comment=GWF_SBR_WARNDAUER)

* **Delete driver seat belt warning light**
  * Group `3001`
    * `00` (start=3, mask=00000001b, comment=SBR-Prewarning_Fahrer)

* **Delete passenger seat belt warning light**
  * Group `3001`
    * `00` (start=4, mask=00000010b, comment=SBR-Prewarning_Beifahrer)

* **Disable driver seat belt warning chime**
  * Group `3001`
    * `00` (start=1, mask=000000010b, comment=SeatBeltReminder_Fahrer)

* **Disable passenger seat belt warning chime**
  * Group `3001`
    * `00` (start=2, mask=00000001b, comment=SeatBeltReminder_Beifahrer)

### ASD01 (CAFD 00000F9B) — authored by Bundang Thunder Mini | Series: F64,F55,F56,F57,F45

* **Set exhaust sound to M4 engine                                                                                       --** by Bundang Thunder ^^**
  * Group `3000`
    * `16` (start=0, mask=11111111b, comment=Model Range)
    * `0A` (start=1, mask=11111111b, comment=Engine)

* **ASD audio level**
  * Group `3000`
    * `01` (start=2, mask=11111111b, comment=Audio Level)

* **ASD power class maximum**
  * Group `3000`
    * `03` (start=3, mask=11111111b, comment=Power Class)

* **ASD power class medium**
  * Group `3000`
    * `00` (start=3, mask=11111111b, comment=Power Class)

### BDC_01 (CAFD 000017BE) — authored by Bundang Thunder Mini | Series: F64,F55,F56,F57,F45

* **Activate hazard lights during hard braking                                                                                   --** by Bundang Thunder ^^**
  * Group `3068`
    * `01` (start=26, mask=00000001b, comment=WB_GB_ENABLE)

* **Set auto start/stop off by default**
  * Group `3023`
    * `01` (start=0, mask=00010000b, comment=TCM_MSA_DEFAULT_OFF)

* **Remember last auto start/stop state**
  * Group `3023`
    * `01` (start=0, mask=00100000b, comment=TCM_MSA_MEMORY)

* **Turn off audio when engine stops**
  * Group `3020`
    * `01` (start=9, mask=00000001b, comment=TCM_LOGIC_R_OFF_DOOR)

* **Double horn when locking with engine running - enable**
  * Group `3040`
    * `01` (start=0, mask=00000100b, comment=VAM_HORN_AT_SECURE)

* **Double horn when locking with engine running - disable**
  * Group `3040`
    * `00` (start=0, mask=00000100b, comment=VAM_HORN_AT_SECURE)

* **Fold mirrors immediately when locking (lock folding)**
  * Group `3056`
    * `00` (start=10, mask=11111111b, comment=KOMFORT_SCHLIESSEN)

* **Start engine without pressing brake**
  * Group `3020`
    * `00` (start=8, mask=00000001b, comment=TCM_STARTLOCK_BRAKE)

* **Start engine without pressing clutch**
  * Group `3020`
    * `00` (start=8, mask=00000100b, comment=TCM_STARTLOCK_CLUTCH)

* **Allow engine start in park**
  * Group `3020`
    * `00` (start=8, mask=00000010b, comment=TCM_STARTLOCK_PARK)
    * `00` (start=8, mask=00010000b, comment=TCM_STARTLOCK_DRIVINGREADINESS)

* **One-touch turn signal flashes five times**
  * Group `3068`
    * `04` (start=7, mask=00000111b, comment=BLINKZYKLEN_ANZAHL_TIPP)

* **Welcome fog lights (hard on)**
  * Group `3063`
    * `hard_On` (start=66, mask=11111111b, comment=MAPPING_NEBELSCHW_L_PART_OF)
    * `hard_On` (start=79, mask=11111111b, comment=MAPPING_NEBELSCHW_R_PART_OF)

* **Welcome fog lights (soft on)**
  * Group `3063`
    * `soft_On` (start=66, mask=11111111b, comment=MAPPING_NEBELSCHW_L_PART_OF)
    * `soft_On` (start=79, mask=11111111b, comment=MAPPING_NEBELSCHW_R_PART_OF)

* **Cornering fog lights**
  * Group `3073`
    * `01` (start=218, mask=00000010b, comment=C_CLC_ENA)
    * `01` (start=66, mask=00000001b, comment=C_BLC_ENA)
  * Group `3066`
    * `01` (start=0, mask=00000001b, comment=KL_ENABLE_LI)
    * `01` (start=80, mask=00000001b, comment=KL_ENABLE_RE)
  * Group `3062`
    * `0B` (start=130, mask=00111111b, comment=MAPPING_abbiegel_L_output)
    * `0C` (start=143, mask=00111111b, comment=MAPPING_abbiegel_R_output)

* **Turn on catch lights when reversing**
  * Group `3070`
    * `01` (start=128, mask=00000001b, comment=OVT_BEI_RUECKFAHRLICHT)

* **Door lock speed: 16 km/h**
  * Group `3040`
    * `01` (start=10, mask=11111111b, comment=VAM_SPEED_LIMIT_PIA_AUTO_LOCK)

* **Enable paddle shifter operation**
  * Group `3190`
    * `01` (start=0, mask=00000001b, comment=PADDLES_VERBAUT)

* **Allow windows to keep closing with door open**
  * Group `3050`
    * `00` (start=0, mask=00000001b, comment=FH_TUERAUF_STOP_MAUT)

* **Limit passenger mirror tilt to 30 degrees in reverse**
  * Group `3110`
    * `1E` (start=1, mask=11111111b, comment=ASP_BORDSTEINAUTOMATIK_DELTA)

### HU_NBT_EVO (CAFD 00001EF6) — authored by Bundang Thunder Mini | Series: F64,F55,F56,F57,F45

* **Set time automatically                                                                                         --** by Bundang Thunder ^^**
  * Group `3000`
    * `navigation` (start=19, mask=00000110b, comment=SETTINGS_TIME_AUTOMATIC)
    * `01` (start=105, mask=00100000b, comment=CLOCK_CHANGE_AUTOMATIC)

* **Watch video/DMB/navigation while driving (up to 63 km/h)**
  * Group `3006`
    * `1F` (start=26, mask=11111111b, comment=SPEEDLOCK_X_KMH_MAX)
    * `3F` (start=25, mask=11111111b, comment=SPEEDLOCK_X_KMH_MIN)
    * `00` (start=5, mask=00010000b, comment=VIDEO_FRONT_LOCKED)
    * `00` (start=5, mask=00000100b, comment=VIDEO_HANDBRAKE)
    * `None` (start=2, mask=00000111b, comment=VIDEO_SPEEDLOCK_CONDITION)

* **Suppress all warning messages**
  * Group `3001`
    * `kein_ld` (start=58, mask=11111111b, comment=LEGAL_DISCLAIMER_TIME)
    * `kein_ld` (start=52, mask=11111111b, comment=MACRO_CAM_LEGALDISCLAIMER)

* **Enable trailer zoom menu when reversing**
  * Group `3001`
    * `01` (start=54, mask=00000001b, comment=MACRO_TRAILER_COUPLING)

* **Close windows when it rains**
  * Group `3000`
    * `01` (start=19, mask=00001000b, comment=REGEN_SCHLIESSEN)

* **X-Drive**
  * Group `3000`
    * `01` (start=5, mask=00000001b, comment=COMPASS)
    * `01` (start=15, mask=00000001b, comment=X_VIEW)
    * `trajectory1` (start=26, mask=00110000b, comment=X_VIEW_GRAPHIC_SLOP)
    * `trajectory1` (start=26, mask=11000000b, comment=X_VIEW_GRAPHIC_ROLL)
    * `01` (start=110, mask=00000010b, comment=MOMENTDISTRIBUTION_MENU)

* **Enable USB video playback 1/2**
  * Group `3000`
    * `01` (start=15, mask=00010000b, comment=ENT_CODEC_OGG)
    * `01` (start=15, mask=00100000b, comment=ENT_CODEC_XVID)
    * `01` (start=15, mask=01000000b, comment=ENT_CODEC_VCD)
    * `01` (start=13, mask=00000100b, comment=ENT_MC_VIDEO_SUPPORT)

* **Enable USB video playback 2/2**
  * Group `3003`
    * `both` (start=32, mask=00000110b, comment=API_USB_VIDEO)
    * `both` (start=32, mask=00011000b, comment=API_IPOD_VIDEO)

* **Change warning chime to Rolls-Royce sound**
  * Group `3002`
    * `rolls_royce` (start=26, mask=00111000b, comment=SOUND_SIGNAL_SET)

* **Configure Sport mode**
  * Group `3008`
    * `popup_and_config` (start=79, mask=11000000b, comment=MACRO_FDS)
  * Group `3009`
    * `01` (start=9, mask=00010000b, comment=EFF_DYN_SPORT_CID)
    * `01` (start=9, mask=00100000b, comment=EFF_DYN_SPORT_UNIT)

* **Startup animation**
  * Group `3001`
    * `animation` (start=62, mask=00000110b, comment=STARTUP_TYPE)
    * `variant_02` (start=62, mask=01111000b, comment=STARTUP_EMBLEM)

* **Volume adjustment bar**
  * Group `3002`
    * `01` (start=52, mask=01000000b, comment=VOLUME_POPUP_DISPLAY)
    * `01` (start=52, mask=10000000b, comment=VOLUME_POPUP_REJECTION)
    * `01` (start=53, mask=00000001b, comment=VOLUME_POPUP_EXCEPTION)

* **Show TPMC tire pressure temperature**
  * Group `3001`
    * `druck_und_temperatur` (start=66, mask=00001100b, comment=RDC_DRUCK_TEMP)

* **Output ringtone through speakers (iPhone only)**
  * Group `3003`
    * `01` (start=6, mask=10000000b, comment=INBAND_RINGING)

* **Lock/unlock confirmation chime (requires piezo buzzer sensor)**
  * Group `3000`
    * `01` (start=110, mask=00000001b, comment=ACOUSTICAL_LOCK_CONFIRM)

* **Change M Sport display cluster colors**
  * Group `3000`
    * `01` (start=133, mask=01000000b, comment=M_VEHICLE)

* **Adjust high-beam assistant in iDrive**
  * Group `3000`
    * `01` (start=109, mask=10000000b, comment=HIGH_BEAM_ASSISTANT)

* **Show currently playing album art in iDrive**
  * Group `3000`
    * `01` (start=9, mask=00000100b, comment=ENT_BTAS_IAP_COVERART)
  * Group `3003`
    * `01` (start=19, mask=00000100b, comment=ENT_BTAS_METADATA)
    * `01` (start=19, mask=00001000b, comment=ENT_BTAS_BROWSING)

* **Unlock DVD region code**
  * Group `3000`
    * `alle_anderen` (start=7, mask=11111111b, comment=ENT_VIDEO_DVD_AREA_CODE)

* **Show turn signals in HUD**
  * Group `300C`
    * `01` (start=0, mask=01000000b, comment=HUD_TURNSIGNAL)

* **Set sound system to Bang & Olufsen**
  * Group `3000`
    * `keine_insz` (start=21, mask=01100000b, comment=HIGH_END_AUDIO_B_UND_W)

* **Enable Logic7 (S667A HiFi vehicles)**
  * Group `3000`
    * `01` (start=22, mask=00001000b, comment=LOGIC7_SYMBOL)

* **Enhance audio mid-bass**
  * Group `3002`
    * `highpremium` (start=29, mask=00111100b, comment=AUDIO_SYSTEM)
    * `variant3` (start=21, mask=00000011b, comment=AUDIO_SYSTEM_VAR)

### PMA_PDC (CAFD 00001AB7) — authored by Bundang Thunder Mini | Series: F64,F55,F56,F57,F45

* **Allow around view to turn on at any time --** by Bundang Thunder ^^**
  * Group `300B`
    * `FF` (start=23, mask=11111111b, comment=V_SCHWELLE_1)
    * `FF` (start=9, mask=11111111b, comment=V_SCHWELLE_2)
    * `FF` (start=10, mask=11111111b, comment=D_SCHWELLE_1)
    * `FF` (start=11, mask=11111111b, comment=D_SCHWELLE_2)

### DSC_CT02 (CAFD 0000297A) — authored by Bundang Thunder Mini | Series: F64,F55,F56,F57,F45

* **Enable dynamic brake lights (activates EGS as well) --** by Bundang Thunder ^^**
  * Group `3000`
    * `01` (start=26, mask=00000100b, comment=C_Funktion_DynamicBrakeControl_aktiv_I)

### KOMBI_I01_F56 (CAFD 0000141F) — authored by Bundang Thunder Mini | Series: F64,F55,F56,F57,F45

* **Show logo on instrument cluster                                                                                    --** by Bundang Thunder ^^**
  * Group `3000`
    * `00` (start=9, mask=00001111b, comment=BMW_LOGO)

* **Digital speed readout in cluster**
  * Group `3000`
    * `01` (start=1, mask=00000010b, comment=BC_DIGITAL_V)

* **Disable warning chime below 3 degrees**
  * Group `3000`
    * `00` (start=43, mask=10000000b, comment=CC_TEMPERATURWARNUNG)

* **Show auto start/stop status in cluster**
  * Group `3003`
    * `01` (start=6, mask=01000000b, comment=MSA_VERFUEGBARANZEIGE_ENABLE)

* **Use GPS time**
  * Group `3000`
    * `01` (start=1, mask=10000000b, comment=GPS_UHR)

* **Display gear number in Dynamic Sport mode**
  * Group `3000`
    * `01` (start=41, mask=00010000b, comment=SPA_SPORT_ENABLE)

* **Enable Sport+ menu in cluster**
  * Group `300C`
    * `menue_3` (start=0, mask=00001111b, comment=FDS_MENUE_TEXT_1)
    * `menue_3` (start=0, mask=11110000b, comment=FDS_MENUE_SIGNAL_1)
    * `menue_3` (start=1, mask=00001111b, comment=FDS_MENUE_TEXT_2)
    * `menue_3` (start=1, mask=11110000b, comment=FDS_MENUE_SIGNAL_2)
    * `menue_3` (start=2, mask=00001111b, comment=FDS_MENUE_TEXT_3)
    * `menue_3` (start=2, mask=11110000b, comment=FDS_MENUE_SIGNAL_3)
    * `menue_3` (start=3, mask=00001111b, comment=FDS_MENUE_TEXT_4)
    * `menue_3` (start=3, mask=11110000b, comment=FDS_MENUE_SIGNAL_4)

### CFAS_PLX_1 (CAFD 000000B5) — authored by Bundang Thunder Mini | Series: F64,F55,F56,F57,F45

* **Enable Easy Access                                                                         --** by Bundang Thunder ^^**
  * Group `3000`
    * `Modus_FA_SLV` (start=0, mask=00011100b, comment=EINAUSSTIEGSHILFE)

* **Easy Access seat starts moving from end position**
  * Group `3012`
    * `00, 01` (start=4, end=5, mask=11111111b, comment=EAH_SCHUTZFREIRAUM_HINTEN_SLV_PHYS)

* **Easy Access seat starts moving with 1 cm remaining**
  * Group `3012`
    * `00, 0A` (start=4, end=5, mask=11111111b, comment=EAH_SCHUTZFREIRAUM_HINTEN_SLV_PHYS)

* **Easy Access seat starts moving with 2 cm remaining**
  * Group `3012`
    * `00, 14` (start=4, end=5, mask=11111111b, comment=EAH_SCHUTZFREIRAUM_HINTEN_SLV_PHYS)

* **Easy Access seat starts moving with 3 cm remaining**
  * Group `3012`
    * `00, 1E` (start=4, end=5, mask=11111111b, comment=EAH_SCHUTZFREIRAUM_HINTEN_SLV_PHYS)

* **Easy Access seat travel distance: 4 cm**
  * Group `3012`
    * `00, 28` (start=0, end=1, mask=11111111b, comment=EAH_VERFAHRWEG_SLV_PHYS)

* **Easy Access seat travel distance: 5 cm**
  * Group `3012`
    * `00, 32` (start=0, end=1, mask=11111111b, comment=EAH_VERFAHRWEG_SLV_PHYS)

* **Easy Access seat travel distance: 6 cm**
  * Group `3012`
    * `00, 3C` (start=0, end=1, mask=11111111b, comment=EAH_VERFAHRWEG_SLV_PHYS)

* **Easy Access seat travel distance: 7 cm**
  * Group `3012`
    * `00, 46` (start=0, end=1, mask=11111111b, comment=EAH_VERFAHRWEG_SLV_PHYS)

* **Set gong when saving seat position**
  * Group `3000`
    * `01` (start=2, mask=00001000b, comment=MEMORY_GONG)

### ACSM_4B (CAFD 00000911) — authored by Bundang Thunder 1 Series | Series: F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

* **Seat belt warning chime for only 5 seconds                                                                                 --** by Bundang Thunder ^^**
  * Group `3001`
    * `05` (start=3, mask=11111111b, comment=GWF_SBR_WARNDAUER)

* **Delete driver seat belt warning light**
  * Group `3000`
    * `00` (start=16, mask=00000001b, comment=SBR_PreWarning_Fahrer)

* **Delete passenger seat belt warning light**
  * Group `3000`
    * `00` (start=16, mask=00000010b, comment=SBR_PreWarning_Beifahrer)

* **Disable driver seat belt warning chime**
  * Group `3000`
    * `00` (start=15, mask=00000010b, comment=SeatBeltReminder_SBR_Fahrer)

* **Disable passenger seat belt warning chime**
  * Group `3000`
    * `00` (start=15, mask=00000100b, comment=SeatBeltReminder_SBR_Beifahrer)

### DSC_CT01 (CAFD 000019CC) — authored by Bundang Thunder 1 Series | Series: F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

* **Enable launch control (also enables EGS)                                                                     --** by Bundang Thunder ^^**
  * Group `3000`
    * `01` (start=26, mask=00010000b, comment=C_Funktion_LaunchControl)

### GKEB23 (CAFD 0000023F) — authored by Bundang Thunder 1 Series | Series: F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

* **Enable launch control (also enables DSC)                                                                     --** by Bundang Thunder ^^**
  * Group `3000`
    * `01` (start=1, mask=10000000b, comment=LC)

* **Show gear number in Dynamic Sport mode**
  * Group `3000`
    * `01` (start=1, mask=00000001b, comment=Sportschalter)
    * `01` (start=0, mask=01000000b, comment=Sportschalter_alt)

### FEM_01 (CAFD 00000794) — authored by Bundang Thunder 1 Series | Series: F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

* **Activate hazard lights during hard braking**
  * Group `3060`
    * `01` (start=26, mask=00000001b, comment=WB_GB_ENABLE)

* **Set auto start/stop off by default**
  * Group `3023`
    * `01` (start=0, mask=00010000b, comment=TCM_MSA_DEFAULT_OFF)

* **Remember last auto start/stop state**
  * Group `3023`
    * `01` (start=0, mask=00100000b, comment=TCM_MSA_MEMORY)

* **Turn off audio when engine stops**
  * Group `3020`
    * `01` (start=1, mask=00000001b, comment=TCM_LOGIC_R_OFF_DOOR)

* **Double horn when locking with engine running - enable**
  * Group `3040`
    * `01` (start=1, mask=00100000b, comment=CLM_HORN_AT_SECURE)

* **Double horn when locking with engine running - disable**
  * Group `3040`
    * `00` (start=1, mask=00100000b, comment=CLM_HORN_AT_SECURE)

* **Fold mirrors immediately when locking (lock folding)**
  * Group `3053`
    * `00` (start=9, mask=11111111b, comment=KOMFORT_SCHLIESSEN)

* **Start engine without pressing brake**
  * Group `3020`
    * `00` (start=0, mask=00000001b, comment=TCM_STARTLOCK_BRAKE)

* **Start engine without pressing clutch**
  * Group `3020`
    * `00` (start=0, mask=00000100b, comment=TCM_STARTLOCK_CLUTCH)

* **Allow engine start in park**
  * Group `3020`
    * `00` (start=0, mask=00000010b, comment=TCM_STARTLOCK_PARK)
    * `00` (start=1, mask=00010000b, comment=TCM_STARTLOCK_DRIVINGREADINESS)

* **One-touch turn signal flashes five times**
  * Group `3060`
    * `04` (start=7, mask=00000111b, comment=BLINKZYKLEN_ANZAHL_TIPP)

* **Welcome fog lights (hard on)**
  * Group `3063`
    * `hard_On` (start=55, mask=11000000b, comment=MAPPING_NEBELSCHW_L_PART_OF_WL)
    * `hard_On` (start=66, mask=11000000b, comment=MAPPING_NEBELSCHW_R_PART_OF_WL)

* **Welcome fog lights (soft on)**
  * Group `3063`
    * `soft_On` (start=55, mask=11000000b, comment=MAPPING_NEBELSCHW_L_PART_OF_WL)
    * `soft_On` (start=66, mask=11000000b, comment=MAPPING_NEBELSCHW_R_PART_OF_WL)

* **Cornering fog lights**
  * Group `3073`
    * `01` (start=218, mask=00000010b, comment=C_CLC_ENA)
    * `01` (start=66, mask=00000001b, comment=C_BLC_ENA)
  * Group `3066`
    * `01` (start=0, mask=00000001b, comment=KL_ENABLE_LI)
    * `01` (start=80, mask=00000001b, comment=KL_ENABLE_RE)
  * Group `3062`
    * `0B` (start=110, mask=00111111b, comment=MAPPING_abbiegel_L_output)
    * `0C` (start=121, mask=00111111b, comment=MAPPING_abbiegel_R_output)

* **Turn on catch lights when reversing**
  * Group `3070`
    * `01` (start=11, mask=00010000b, comment=OVT_BEI_RUECKFAHRLICHT)

* **Unlock doors automatically when engine off**
  * Group `3040`
    * `01` (start=1, mask=00000010b, comment=CLM_UNLOCK_KL15OFF_AFTER_PIA_AUTO_LOCK)

* **Enable paddle shifter operation**
  * Group `3190`
    * `01` (start=9, mask=00000001b, comment=PADDLES_VERBAUT)

* **Allow windows to keep closing with door open**
  * Group `3050`
    * `00` (start=0, mask=00000001b, comment=FH_TUERAUF_STOP_MAUT)

* **Limit passenger mirror tilt to 30 degrees in reverse**
  * Group `3110`
    * `1E` (start=2, mask=11111111b, comment=ASP_BORDSTEINAUTOMATIK_DELTA)

### HU_NBT (CAFD 00000DED) — authored by Bundang Thunder 1 Series | Series: F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

* **Set time automatically                                                                                         --** by Bundang Thunder ^^**
  * Group `3000`
    * `navigation` (start=19, mask=00000110b, comment=SETTINGS_TIME_AUTOMATIC)
    * `01` (start=105, mask=00100000b, comment=CLOCK_CHANGE_AUTOMATIC)

* **Watch video/DMB/navigation while driving**
  * Group `3000`
    * `FF` (start=72, mask=11111111b, comment=SPEEDLOCK_X_KMH_MAX)
    * `FF` (start=71, mask=11111111b, comment=SPEEDLOCK_X_KMH_MIN)
    * `00` (start=5, mask=00010000b, comment=VIDEO_FRONT_LOCKED)
    * `00` (start=5, mask=00000100b, comment=VIDEO_HANDBRAKE)
    * `None` (start=57, mask=00000111b, comment=VIDEO_SPEEDLOCK_CONDITION)

* **Suppress all warning messages**
  * Group `3001`
    * `kein_ld` (start=58, mask=11111111b, comment=LEGAL_DISCLAIMER_TIME)
    * `kein_ld` (start=52, mask=11111111b, comment=MACRO_CAM_LEGALDISCLAIMER)

* **Enable trailer zoom menu when reversing**
  * Group `3001`
    * `01` (start=54, mask=00000001b, comment=MACRO_TRAILER_COUPLING)

* **Close windows when it rains**
  * Group `3000`
    * `01` (start=19, mask=00001000b, comment=REGEN_SCHLIESSEN)

* **X-Drive**
  * Group `3000`
    * `01` (start=5, mask=00000001b, comment=COMPASS)
    * `01` (start=15, mask=00000001b, comment=X_VIEW)
    * `trajectory1` (start=26, mask=00110000b, comment=X_VIEW_GRAPHIC_SLOP)
    * `trajectory1` (start=26, mask=11000000b, comment=X_VIEW_GRAPHIC_ROLL)
    * `01` (start=110, mask=00000010b, comment=MOMENTDISTRIBUTION_MENU)

* **Enable USB video playback 1/2**
  * Group `3000`
    * `01` (start=15, mask=00010000b, comment=ENT_CODEC_OGG)
    * `01` (start=15, mask=00100000b, comment=ENT_CODEC_XVID)
    * `01` (start=15, mask=01000000b, comment=ENT_CODEC_VCD)
    * `01` (start=13, mask=00000100b, comment=ENT_MC_VIDEO_SUPPORT)

* **Enable USB video playback 2/2**
  * Group `3003`
    * `both` (start=33, mask=00000110b, comment=API_USB_VIDEO)
    * `both` (start=33, mask=00011000b, comment=API_IPOD_VIDEO)

* **Change warning chime to Rolls-Royce sound**
  * Group `3002`
    * `rolls_royce` (start=26, mask=00111000b, comment=SOUND_SIGNAL_SET)

* **Configure Sport mode**
  * Group `3001`
    * `popup_and_config` (start=55, mask=00011000b, comment=MACRO_FDS)
  * Group `3000`
    * `01` (start=101, mask=00010000b, comment=EFF_DYN_SPORT_CID)
    * `01` (start=107, mask=00000100b, comment=EFF_DYN_SPORT_UNIT)

* **Startup animation**
  * Group `3001`
    * `animation` (start=62, mask=00000110b, comment=STARTUP_TYPE)
    * `variant_01` (start=62, mask=01111000b, comment=STARTUP_EMBLEM)

* **Volume adjustment bar**
  * Group `3002`
    * `01` (start=52, mask=01000000b, comment=VOLUME_POPUP_DISPLAY)
    * `01` (start=52, mask=10000000b, comment=VOLUME_POPUP_REJECTION)
    * `01` (start=53, mask=00000001b, comment=VOLUME_POPUP_EXCEPTION)

* **Show TPMC tire pressure temperature**
  * Group `3001`
    * `druck_und_temperatur` (start=66, mask=00001100b, comment=RDC_DRUCK_TEMP)

* **Output ringtone through speakers (iPhone only)**
  * Group `3003`
    * `01` (start=6, mask=10000000b, comment=INBAND_RINGING)

* **Lock/unlock confirmation chime (requires piezo buzzer sensor)**
  * Group `3000`
    * `01` (start=110, mask=00000001b, comment=ACOUSTICAL_LOCK_CONFIRM)

* **Change M Sport display cluster colors**
  * Group `3000`
    * `01` (start=133, mask=01000000b, comment=M_VEHICLE)

* **Adjust high-beam assistant in iDrive**
  * Group `3000`
    * `01` (start=109, mask=10000000b, comment=HIGH_BEAM_ASSISTANT)

* **Show currently playing album art in iDrive**
  * Group `3000`
    * `01` (start=9, mask=00000100b, comment=ENT_BTAS_IAP_COVERART)
  * Group `3003`
    * `01` (start=19, mask=00000100b, comment=ENT_BTAS_METADATA)
    * `01` (start=19, mask=00001000b, comment=ENT_BTAS_BROWSING)

* **Unlock DVD region code**
  * Group `3000`
    * `alle_anderen` (start=7, mask=11111111b, comment=ENT_VIDEO_DVD_AREA_CODE)

* **Show turn signals in HUD**
  * Group `3001`
    * `01` (start=55, mask=10000000b, comment=HUD_TURNSIGNAL)

* **Set sound system to Bang & Olufsen**
  * Group `3000`
    * `keine_insz` (start=21, mask=01100000b, comment=HIGH_END_AUDIO_B_UND_W)

* **Enable Logic7 (S667A HiFi vehicles)**
  * Group `3000`
    * `01` (start=22, mask=00001000b, comment=LOGIC7_SYMBOL)

* **Enhance audio mid-bass**
  * Group `3002`
    * `highpremium` (start=29, mask=00111100b, comment=AUDIO_SYSTEM)
    * `variant3` (start=21, mask=00000011b, comment=AUDIO_SYSTEM_VAR)

### ICMQL (CAFD 0000067B) — authored by Bundang Thunder 1 Series | Series: F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

* **Default to Eco mode at start                                                                              --** by Bundang Thunder ^^**
  * Group `3000`
    * `verbaut` (start=36, mask=00001000b, comment=IcmKod_B_InitEco)

* **Enable cruise control**
  * Group `3000`
    * `01` (start=128, mask=00001110b, comment=C_Fahrfunktion)

* **Enable Sport+ mode**
  * Group `3000`
    * `verbaut` (start=18, mask=11111111b, comment=IcmKod_B_S2TBA)

### IHKA_VA02 (CAFD 000016EE) — authored by Bundang Thunder 1 Series | Series: F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

* **Remember last air conditioning state                                                                               --** by Bundang Thunder ^^**
  * Group `3003`
    * `01` (start=0, mask=00000010b, comment=MEMORY_OFF)

* **Prevent AUTO button from turning on A/C**
  * Group `3003`
    * `00` (start=0, mask=00000100b, comment=AC_ON_WITH_AUTO)

* **Remember HVAC recirculation mode**
  * Group `3003`
    * `01` (start=0, mask=00000001b, comment=MEMORY_UMLUFT)

### KAFAS2 (CAFD 00001148) — authored by Bundang Thunder 1 Series | Series: F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

* **Automatic high-beam assistant**
  * Group `3050`
    * `FLA_on` (start=1, mask=00000001b, comment=FLA_ON_OFF)
    * `CN` (start=6, mask=11111111b, comment=SPEED_SWITCHING_HIGH_BEAMS_ON)
    * `China` (start=7, mask=11111111b, comment=SPEED_SWITCHING_HIGH_BEAMS_OFF)

### KOMBI L7_BASIS (CAFD 00000760) — authored by Bundang Thunder 1 Series | Series: F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

* **Show logo on instrument cluster                                                                                    --** by Bundang Thunder ^^**
  * Group `3000`
    * `mpm` (start=0, mask=11110000b, comment=BMW_LOGO)

* **Digital speed readout in cluster**
  * Group `3000`
    * `01` (start=1, mask=00000010b, comment=BC_DIGITAL_V)

* **Disable warning chime below 3 degrees**
  * Group `3000`
    * `00` (start=19, mask=00000001b, comment=CC_TEMPERATURWARNUNG)

* **Show auto start/stop status in cluster**
  * Group `3003`
    * `01` (start=3, mask=00001000b, comment=MSA_VERFUEGBARANZEIGE_ENABLE)

* **Use GPS time**
  * Group `3000`
    * `01` (start=1, mask=10000000b, comment=GPS_UHR)

* **Display gear number in Dynamic Sport mode**
  * Group `3000`
    * `01` (start=41, mask=00010000b, comment=SPA_SPORT_ENABLE)

* **Enable Sport+ menu in cluster**
  * Group `300C`
    * `menue_3` (start=0, mask=00001111b, comment=FDS_MENUE_TEXT_1)
    * `menue_3` (start=0, mask=11110000b, comment=FDS_MENUE_SIGNAL_1)
    * `menue_3` (start=1, mask=00001111b, comment=FDS_MENUE_TEXT_2)
    * `menue_3` (start=1, mask=11110000b, comment=FDS_MENUE_SIGNAL_2)
    * `menue_3` (start=2, mask=00001111b, comment=FDS_MENUE_TEXT_3)
    * `menue_3` (start=2, mask=11110000b, comment=FDS_MENUE_SIGNAL_3)
    * `menue_3` (start=3, mask=00001111b, comment=FDS_MENUE_TEXT_4)
    * `menue_3` (start=3, mask=11110000b, comment=FDS_MENUE_SIGNAL_4)
    * `menue_3` (start=54, mask=11111111b, comment=FDS_MENUE)

### CFAS_PLX_1 (CAFD 000000B5) — authored by Bundang Thunder 1 Series | Series: F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

* **Enable Easy Access                                                                         --** by Bundang Thunder ^^**
  * Group `3000`
    * `Modus_FA_SLV` (start=0, mask=00011100b, comment=EINAUSSTIEGSHILFE)

* **Easy Access seat starts moving from end position**
  * Group `3012`
    * `00, 01` (start=4, end=5, mask=11111111b, comment=EAH_SCHUTZFREIRAUM_HINTEN_SLV_PHYS)

* **Easy Access seat starts moving with 1 cm remaining**
  * Group `3012`
    * `00, 0A` (start=4, end=5, mask=11111111b, comment=EAH_SCHUTZFREIRAUM_HINTEN_SLV_PHYS)

* **Easy Access seat starts moving with 2 cm remaining**
  * Group `3012`
    * `00, 14` (start=4, end=5, mask=11111111b, comment=EAH_SCHUTZFREIRAUM_HINTEN_SLV_PHYS)

* **Easy Access seat starts moving with 3 cm remaining**
  * Group `3012`
    * `00, 1E` (start=4, end=5, mask=11111111b, comment=EAH_SCHUTZFREIRAUM_HINTEN_SLV_PHYS)

* **Easy Access seat travel distance: 4 cm**
  * Group `3012`
    * `00, 28` (start=0, end=1, mask=11111111b, comment=EAH_VERFAHRWEG_SLV_PHYS)

* **Easy Access seat travel distance: 5 cm**
  * Group `3012`
    * `00, 32` (start=0, end=1, mask=11111111b, comment=EAH_VERFAHRWEG_SLV_PHYS)

* **Easy Access seat travel distance: 6 cm**
  * Group `3012`
    * `00, 3C` (start=0, end=1, mask=11111111b, comment=EAH_VERFAHRWEG_SLV_PHYS)

* **Easy Access seat travel distance: 7 cm**
  * Group `3012`
    * `00, 46` (start=0, end=1, mask=11111111b, comment=EAH_VERFAHRWEG_SLV_PHYS)

* **Set gong when saving seat position**
  * Group `3000`
    * `01` (start=2, mask=00001000b, comment=MEMORY_GONG)

### TRSVC (CAFD 00000223) — authored by Bundang Thunder 1 Series | Series: F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

* **Allow side view at any time                                                                   --** by Bundang Thunder ^^**
  * Group `3000`
    * `FF` (start=114, mask=11111111b, comment=SV_Activate_Speed_Limit)
    * `FF` (start=115, mask=11111111b, comment=SV_Deactivate_Speed)

### ACSM_4i (CAFD 000011AB) — authored by Bundang Thunder 2 Series | Series: F64,F55,F56,F57,F45

* **Seat belt warning chime for only 5 seconds                                                                                 --** by Bundang Thunder ^^**
  * Group `3001`
    * `05` (start=11, mask=11111111b, comment=GWF_SBR_WARNDAUER)

* **Delete driver seat belt warning light**
  * Group `3001`
    * `00` (start=3, mask=00000001b, comment=SBR-Prewarning_Fahrer)

* **Delete passenger seat belt warning light**
  * Group `3001`
    * `00` (start=4, mask=00000001b, comment=SBR-Prewarning_Beifahrer)

* **Disable driver seat belt warning chime**
  * Group `3001`
    * `00` (start=1, mask=00000001b, comment=SeatBeltReminder_Fahrer)

* **Disable passenger seat belt warning chime**
  * Group `3000`
    * `00` (start=2, mask=00000001b, comment=SeatBeltReminder_Beifahrer)

### DSC_CT02 (CAFD 0000297A) — authored by Bundang Thunder 2 Series | Series: F64,F55,F56,F57,F45

* **Enable dynamic brake lights (activates EGS as well) --** by Bundang Thunder ^^**
  * Group `3000`
    * `01` (start=26, mask=00000100b, comment=C_Funktion_DynamicBrakeControl_aktiv_I)

### GSAW01 (CAFD 0000114B) — authored by Bundang Thunder 2 Series | Series: F64,F55,F56,F57,F45

* **Enable launch control (also enables DSC)                                                                     --** by Bundang Thunder ^^**
  * Group `3000`
    * `01` (start=1, mask=10000000b, comment=LC)

### BDC_01 (CAFD 000017BE) — authored by Bundang Thunder 2 Series | Series: F64,F55,F56,F57,F45

* **Activate hazard lights during hard braking                                                                                   --** by Bundang Thunder ^^**
  * Group `3068`
    * `01` (start=26, mask=00000001b, comment=WB_GB_ENABLE)

* **Set auto start/stop off by default**
  * Group `3023`
    * `01` (start=0, mask=00010000b, comment=TCM_MSA_DEFAULT_OFF)

* **Remember last auto start/stop state**
  * Group `3023`
    * `01` (start=0, mask=00100000b, comment=TCM_MSA_MEMORY)

* **Turn off audio when engine stops**
  * Group `3020`
    * `01` (start=9, mask=00000001b, comment=TCM_LOGIC_R_OFF_DOOR)

* **Double horn when locking with engine running - enable**
  * Group `3040`
    * `01` (start=0, mask=00000100b, comment=VAM_HORN_AT_SECURE)

* **Double horn when locking with engine running - disable**
  * Group `3040`
    * `00` (start=0, mask=00000100b, comment=VAM_HORN_AT_SECURE)

* **Fold mirrors immediately when locking (lock folding)**
  * Group `3056`
    * `00` (start=10, mask=11111111b, comment=KOMFORT_SCHLIESSEN)

* **Start engine without pressing brake**
  * Group `3020`
    * `00` (start=8, mask=00000001b, comment=TCM_STARTLOCK_BRAKE)

* **Start engine without pressing clutch**
  * Group `3020`
    * `00` (start=8, mask=00000100b, comment=TCM_STARTLOCK_CLUTCH)

* **Allow engine start in park**
  * Group `3020`
    * `00` (start=8, mask=00000010b, comment=TCM_STARTLOCK_PARK)
    * `00` (start=8, mask=00010000b, comment=TCM_STARTLOCK_DRIVINGREADINESS)

* **One-touch turn signal flashes five times**
  * Group `3068`
    * `04` (start=7, mask=00000111b, comment=BLINKZYKLEN_ANZAHL_TIPP)

* **Welcome fog lights**
  * Group `3063`
    * `0B` (start=65, mask=00111111b, comment=MAPPING_NEBELSCHW_L_OUTPUT)
    * `0C` (start=78, mask=11000000b, comment=MAPPING_NEBELSCHW_R_OUTPUT)

* **Cornering fog lights**
  * Group `3073`
    * `01` (start=218, mask=00000010b, comment=C_CLC_ENA)
    * `01` (start=66, mask=00000001b, comment=C_BLC_ENA)
  * Group `3066`
    * `01` (start=0, mask=00000001b, comment=KL_ENABLE_LI)
    * `01` (start=80, mask=00000001b, comment=KL_ENABLE_RE)
  * Group `3062`
    * `0B` (start=130, mask=00111111b, comment=MAPPING_abbiegel_L_output)
    * `0C` (start=143, mask=00111111b, comment=MAPPING_abbiegel_R_output)

* **Turn on catch lights when reversing**
  * Group `3070`
    * `01` (start=128, mask=00000001b, comment=OVT_BEI_RUECKFAHRLICHT)

* **Enable paddle shifter operation**
  * Group `3190`
    * `01` (start=0, mask=00000001b, comment=PADDLES_VERBAUT)

* **Allow windows to keep closing with door open**
  * Group `3050`
    * `00` (start=0, mask=00000001b, comment=FH_TUERAUF_STOP_MAUT)

* **Limit passenger mirror tilt to 30 degrees in reverse**
  * Group `3110`
    * `1E` (start=1, mask=11111111b, comment=ASP_BORDSTEINAUTOMATIK_DELTA)

### HU_NBT (CAFD 00000DED) — authored by Bundang Thunder 2 Series | Series: F64,F55,F56,F57,F45

* **Set time automatically                                                                                         --** by Bundang Thunder ^^**
  * Group `3000`
    * `navigation` (start=19, mask=00000110b, comment=SETTINGS_TIME_AUTOMATIC)
    * `01` (start=105, mask=00100000b, comment=CLOCK_CHANGE_AUTOMATIC)

* **Watch video/DMB/navigation while driving**
  * Group `3000`
    * `FF` (start=72, mask=11111111b, comment=SPEEDLOCK_X_KMH_MAX)
    * `FF` (start=71, mask=11111111b, comment=SPEEDLOCK_X_KMH_MIN)
    * `00` (start=5, mask=00010000b, comment=VIDEO_FRONT_LOCKED)
    * `00` (start=5, mask=00000100b, comment=VIDEO_HANDBRAKE)
    * `None` (start=57, mask=00000111b, comment=VIDEO_SPEEDLOCK_CONDITION)

* **Suppress all warning messages**
  * Group `3001`
    * `kein_ld` (start=58, mask=11111111b, comment=LEGAL_DISCLAIMER_TIME)
    * `kein_ld` (start=52, mask=11111111b, comment=MACRO_CAM_LEGALDISCLAIMER)

* **Enable trailer zoom menu when reversing**
  * Group `3001`
    * `01` (start=54, mask=00000001b, comment=MACRO_TRAILER_COUPLING)

* **Close windows when it rains**
  * Group `3000`
    * `01` (start=19, mask=00001000b, comment=REGEN_SCHLIESSEN)

* **X-Drive**
  * Group `3000`
    * `01` (start=5, mask=00000001b, comment=COMPASS)
    * `01` (start=15, mask=00000001b, comment=X_VIEW)
    * `trajectory1` (start=26, mask=00110000b, comment=X_VIEW_GRAPHIC_SLOP)
    * `trajectory1` (start=26, mask=11000000b, comment=X_VIEW_GRAPHIC_ROLL)
    * `01` (start=110, mask=00000010b, comment=MOMENTDISTRIBUTION_MENU)

* **Enable USB video playback 1/2**
  * Group `3000`
    * `01` (start=15, mask=00010000b, comment=ENT_CODEC_OGG)
    * `01` (start=15, mask=00100000b, comment=ENT_CODEC_XVID)
    * `01` (start=15, mask=01000000b, comment=ENT_CODEC_VCD)
    * `01` (start=13, mask=00000100b, comment=ENT_MC_VIDEO_SUPPORT)

* **Enable USB video playback 2/2**
  * Group `3003`
    * `both` (start=33, mask=00000110b, comment=API_USB_VIDEO)
    * `both` (start=33, mask=00011000b, comment=API_IPOD_VIDEO)

* **Change warning chime to Rolls-Royce sound**
  * Group `3002`
    * `rolls_royce` (start=26, mask=00111000b, comment=SOUND_SIGNAL_SET)

* **Configure Sport mode**
  * Group `3001`
    * `popup_and_config` (start=55, mask=00011000b, comment=MACRO_FDS)
  * Group `3000`
    * `01` (start=101, mask=00010000b, comment=EFF_DYN_SPORT_CID)
    * `01` (start=107, mask=00000100b, comment=EFF_DYN_SPORT_UNIT)

* **Startup animation**
  * Group `3001`
    * `animation` (start=62, mask=00000110b, comment=STARTUP_TYPE)
    * `variant_01` (start=62, mask=01111000b, comment=STARTUP_EMBLEM)

* **Volume adjustment bar**
  * Group `3002`
    * `01` (start=52, mask=01000000b, comment=VOLUME_POPUP_DISPLAY)
    * `01` (start=52, mask=10000000b, comment=VOLUME_POPUP_REJECTION)
    * `01` (start=53, mask=00000001b, comment=VOLUME_POPUP_EXCEPTION)

* **Show TPMC tire pressure temperature**
  * Group `3001`
    * `druck_und_temperatur` (start=66, mask=00001100b, comment=RDC_DRUCK_TEMP)

* **Output ringtone through speakers (iPhone only)**
  * Group `3003`
    * `01` (start=6, mask=10000000b, comment=INBAND_RINGING)

* **Lock/unlock confirmation chime (requires piezo buzzer sensor)**
  * Group `3000`
    * `01` (start=110, mask=00000001b, comment=ACOUSTICAL_LOCK_CONFIRM)

* **Change M Sport display cluster colors**
  * Group `3000`
    * `01` (start=133, mask=01000000b, comment=M_VEHICLE)

* **Adjust high-beam assistant in iDrive**
  * Group `3000`
    * `01` (start=109, mask=10000000b, comment=HIGH_BEAM_ASSISTANT)

* **Show currently playing album art in iDrive**
  * Group `3000`
    * `01` (start=9, mask=00000100b, comment=ENT_BTAS_IAP_COVERART)
  * Group `3003`
    * `01` (start=19, mask=00000100b, comment=ENT_BTAS_METADATA)
    * `01` (start=19, mask=00001000b, comment=ENT_BTAS_BROWSING)

* **Unlock DVD region code**
  * Group `3000`
    * `alle_anderen` (start=7, mask=11111111b, comment=ENT_VIDEO_DVD_AREA_CODE)

* **Show turn signals in HUD**
  * Group `3001`
    * `01` (start=55, mask=10000000b, comment=HUD_TURNSIGNAL)

* **Set sound system to Bang & Olufsen**
  * Group `3000`
    * `keine_insz` (start=21, mask=01100000b, comment=HIGH_END_AUDIO_B_UND_W)

* **Enable Logic7 (S667A HiFi vehicles)**
  * Group `3000`
    * `01` (start=22, mask=00001000b, comment=LOGIC7_SYMBOL)

* **Enhance audio mid-bass**
  * Group `3002`
    * `highpremium` (start=29, mask=00111100b, comment=AUDIO_SYSTEM)
    * `variant3` (start=21, mask=00000011b, comment=AUDIO_SYSTEM_VAR)

### IHKA_VA02 (CAFD 000016EE) — authored by Bundang Thunder 2 Series | Series: F64,F55,F56,F57,F45

* **Remember last air conditioning state                                                                               --** by Bundang Thunder ^^**
  * Group `3003`
    * `01` (start=0, mask=00000010b, comment=MEMORY_OFF)

* **Prevent AUTO button from turning on A/C**
  * Group `3003`
    * `00` (start=0, mask=00000100b, comment=AC_ON_WITH_AUTO)

* **Remember HVAC recirculation mode**
  * Group `3003`
    * `01` (start=0, mask=00000001b, comment=MEMORY_UMLUFT)

### KAFAS2 (CAFD 00001148) — authored by Bundang Thunder 2 Series | Series: F64,F55,F56,F57,F45

* **Automatic high-beam assistant                                                                                --** by Bundang Thunder ^^**
  * Group `3050`
    * `FLA_on` (start=1, mask=00000001b, comment=FLA_ON_OFF)
    * `CN` (start=6, mask=11111111b, comment=SPEED_SWITCHING_HIGH_BEAMS_ON)
    * `China` (start=7, mask=11111111b, comment=SPEED_SWITCHING_HIGH_BEAMS_OFF)

### KOMBI L7_BASIS (CAFD 00000760) — authored by Bundang Thunder 2 Series | Series: F64,F55,F56,F57,F45

* **Show logo on instrument cluster                                                                                    --** by Bundang Thunder ^^**
  * Group `3000`
    * `mpm` (start=0, mask=11110000b, comment=BMW_LOGO)

* **Digital speed readout in cluster**
  * Group `3000`
    * `01` (start=1, mask=00000010b, comment=BC_DIGITAL_V)

* **Disable warning chime below 3 degrees**
  * Group `3000`
    * `00` (start=19, mask=00000001b, comment=CC_TEMPERATURWARNUNG)

* **Show auto start/stop status in cluster**
  * Group `3003`
    * `01` (start=3, mask=00001000b, comment=MSA_VERFUEGBARANZEIGE_ENABLE)

* **Use GPS time**
  * Group `3000`
    * `01` (start=1, mask=10000000b, comment=GPS_UHR)

* **Display gear number in Dynamic Sport mode**
  * Group `3000`
    * `01` (start=41, mask=00010000b, comment=SPA_SPORT_ENABLE)

* **Enable Sport+ menu in cluster**
  * Group `300C`
    * `menue_3` (start=0, mask=00001111b, comment=FDS_MENUE_TEXT_1)
    * `menue_3` (start=0, mask=11110000b, comment=FDS_MENUE_SIGNAL_1)
    * `menue_3` (start=1, mask=00001111b, comment=FDS_MENUE_TEXT_2)
    * `menue_3` (start=1, mask=11110000b, comment=FDS_MENUE_SIGNAL_2)
    * `menue_3` (start=2, mask=00001111b, comment=FDS_MENUE_TEXT_3)
    * `menue_3` (start=2, mask=11110000b, comment=FDS_MENUE_SIGNAL_3)
    * `menue_3` (start=3, mask=00001111b, comment=FDS_MENUE_TEXT_4)
    * `menue_3` (start=3, mask=11110000b, comment=FDS_MENUE_SIGNAL_4)
    * `menue_3` (start=54, mask=11111111b, comment=FDS_MENUE)

### CFAS_PLX_1 (CAFD 000000B5) — authored by Bundang Thunder 2 Series | Series: F64,F55,F56,F57,F45

* **Enable Easy Access                                                                         --** by Bundang Thunder ^^**
  * Group `3000`
    * `Modus_FA_SLV` (start=0, mask=00011100b, comment=EINAUSSTIEGSHILFE)

* **Easy Access seat starts moving from end position**
  * Group `3012`
    * `00, 01` (start=4, end=5, mask=11111111b, comment=EAH_SCHUTZFREIRAUM_HINTEN_SLV_PHYS)

* **Easy Access seat starts moving with 1 cm remaining**
  * Group `3012`
    * `00, 0A` (start=4, end=5, mask=11111111b, comment=EAH_SCHUTZFREIRAUM_HINTEN_SLV_PHYS)

* **Easy Access seat starts moving with 2 cm remaining**
  * Group `3012`
    * `00, 14` (start=4, end=5, mask=11111111b, comment=EAH_SCHUTZFREIRAUM_HINTEN_SLV_PHYS)

* **Easy Access seat starts moving with 3 cm remaining**
  * Group `3012`
    * `00, 1E` (start=4, end=5, mask=11111111b, comment=EAH_SCHUTZFREIRAUM_HINTEN_SLV_PHYS)

* **Easy Access seat travel distance: 4 cm**
  * Group `3012`
    * `00, 28` (start=0, end=1, mask=11111111b, comment=EAH_VERFAHRWEG_SLV_PHYS)

* **Easy Access seat travel distance: 5 cm**
  * Group `3012`
    * `00, 32` (start=0, end=1, mask=11111111b, comment=EAH_VERFAHRWEG_SLV_PHYS)

* **Easy Access seat travel distance: 6 cm**
  * Group `3012`
    * `00, 3C` (start=0, end=1, mask=11111111b, comment=EAH_VERFAHRWEG_SLV_PHYS)

* **Easy Access seat travel distance: 7 cm**
  * Group `3012`
    * `00, 46` (start=0, end=1, mask=11111111b, comment=EAH_VERFAHRWEG_SLV_PHYS)

* **Gentleman**
  * Group `3000`
    * `01` (start=1, mask=00000001b, comment=GENTLEMAN)
    * `01` (start=0, mask=00000001b, comment=MEMORY)

* **Set gong when saving seat position**
  * Group `3000`
    * `01` (start=2, mask=00001000b, comment=MEMORY_GONG)

### ACSM_4B (CAFD 00000911) — authored by Bundang Thunder 3 Series | Series: F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

* **Seat belt warning chime for only 5 seconds                                                                                 --** by Bundang Thunder ^^**
  * Group `3001`
    * `05` (start=3, mask=11111111b, comment=GWF_SBR_WARNDAUER)

* **Delete driver seat belt warning light**
  * Group `3000`
    * `00` (start=16, mask=00000001b, comment=SBR_PreWarning_Fahrer)

* **Delete passenger seat belt warning light**
  * Group `3000`
    * `00` (start=16, mask=00000010b, comment=SBR_PreWarning_Beifahrer)

* **Disable driver seat belt warning chime**
  * Group `3000`
    * `00` (start=15, mask=00000010b, comment=SeatBeltReminder_SBR_Fahrer)

* **Disable passenger seat belt warning chime**
  * Group `3000`
    * `00` (start=15, mask=00000100b, comment=SeatBeltReminder_SBR_Beifahrer)

### ASD01 (CAFD 00000F9B) — authored by Bundang Thunder 3 Series | Series: F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

* **Set exhaust sound to M4 engine                                                                                       --** by Bundang Thunder ^^**
  * Group `3000`
    * `16` (start=0, mask=11111111b, comment=Model Range)
    * `0A` (start=1, mask=11111111b, comment=Engine)

* **ASD audio level**
  * Group `3000`
    * `01` (start=2, mask=11111111b, comment=Audio Level)

* **ASD power class maximum**
  * Group `3000`
    * `03` (start=3, mask=11111111b, comment=Power Class)

* **ASD power class medium**
  * Group `3000`
    * `00` (start=3, mask=11111111b, comment=Power Class)

### DSC_CT01 (CAFD 000019CC) — authored by Bundang Thunder 3 Series | Series: F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

* **Enable launch control (also enables EGS)                                                                     --** by Bundang Thunder ^^**
  * Group `3000`
    * `01` (start=26, mask=00010000b, comment=C_Funktion_LaunchControl)

### GKEB23 (CAFD 0000023F) — authored by Bundang Thunder 3 Series | Series: F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

* **Enable launch control (also enables DSC)                                                                     --** by Bundang Thunder ^^**
  * Group `3000`
    * `01` (start=1, mask=10000000b, comment=LC)

* **Show gear number in Dynamic Sport mode**
  * Group `3000`
    * `01` (start=1, mask=00000001b, comment=Sportschalter)
    * `01` (start=0, mask=01000000b, comment=Sportschalter_alt)

### FEM_01 (CAFD 00000794) — authored by Bundang Thunder 3 Series | Series: F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

* **Activate hazard lights during hard braking                                                                                   --** by Bundang Thunder ^^**
  * Group `3060`
    * `01` (start=26, mask=00000001b, comment=WB_GB_ENABLE)

* **Set auto start/stop off by default**
  * Group `3023`
    * `01` (start=0, mask=00010000b, comment=TCM_MSA_DEFAULT_OFF)

* **Remember last auto start/stop state**
  * Group `3023`
    * `01` (start=0, mask=00100000b, comment=TCM_MSA_MEMORY)

* **Turn off audio when engine stops**
  * Group `3020`
    * `01` (start=1, mask=00000001b, comment=TCM_LOGIC_R_OFF_DOOR)

* **Double horn when locking with engine running - enable**
  * Group `3040`
    * `01` (start=1, mask=00100000b, comment=CLM_HORN_AT_SECURE)

* **Double horn when locking with engine running - disable**
  * Group `3040`
    * `00` (start=1, mask=00100000b, comment=CLM_HORN_AT_SECURE)

* **Fold mirrors immediately when locking (lock folding)**
  * Group `3053`
    * `00` (start=9, mask=11111111b, comment=KOMFORT_SCHLIESSEN)

* **Start engine without pressing brake**
  * Group `3020`
    * `00` (start=0, mask=00000001b, comment=TCM_STARTLOCK_BRAKE)

* **Start engine without pressing clutch**
  * Group `3020`
    * `00` (start=0, mask=00000100b, comment=TCM_STARTLOCK_CLUTCH)

* **Allow engine start in park**
  * Group `3020`
    * `00` (start=0, mask=00000010b, comment=TCM_STARTLOCK_PARK)
    * `00` (start=1, mask=00010000b, comment=TCM_STARTLOCK_DRIVINGREADINESS)

* **One-touch turn signal flashes five times**
  * Group `3060`
    * `04` (start=7, mask=00000111b, comment=BLINKZYKLEN_ANZAHL_TIPP)

* **Welcome fog lights (hard on)**
  * Group `3063`
    * `hard_On` (start=55, mask=11000000b, comment=MAPPING_NEBELSCHW_L_PART_OF_WL)
    * `hard_On` (start=66, mask=11000000b, comment=MAPPING_NEBELSCHW_R_PART_OF_WL)

* **Welcome fog lights (soft on)**
  * Group `3063`
    * `soft_On` (start=55, mask=11000000b, comment=MAPPING_NEBELSCHW_L_PART_OF_WL)
    * `soft_On` (start=66, mask=11000000b, comment=MAPPING_NEBELSCHW_R_PART_OF_WL)

* **Cornering fog lights**
  * Group `3073`
    * `01` (start=218, mask=00000010b, comment=C_CLC_ENA)
    * `01` (start=66, mask=00000001b, comment=C_BLC_ENA)
  * Group `3066`
    * `01` (start=0, mask=00000001b, comment=KL_ENABLE_LI)
    * `01` (start=80, mask=00000001b, comment=KL_ENABLE_RE)
  * Group `3062`
    * `0B` (start=110, mask=00111111b, comment=MAPPING_abbiegel_L_output)
    * `0C` (start=121, mask=00111111b, comment=MAPPING_abbiegel_R_output)

* **Turn on catch lights when reversing**
  * Group `3070`
    * `01` (start=11, mask=00010000b, comment=OVT_BEI_RUECKFAHRLICHT)

* **Unlock doors automatically when engine off**
  * Group `3040`
    * `01` (start=1, mask=00000010b, comment=CLM_UNLOCK_KL15OFF_AFTER_PIA_AUTO_LOCK)

* **Enable paddle shifter operation**
  * Group `3190`
    * `01` (start=0, mask=00000001b, comment=PADDLES_VERBAUT)

* **Allow windows to keep closing with door open**
  * Group `3050`
    * `00` (start=0, mask=00000001b, comment=FH_TUERAUF_STOP_MAUT)

* **Limit passenger mirror tilt to 30 degrees in reverse**
  * Group `3110`
    * `1E` (start=1, mask=11111111b, comment=ASP_BORDSTEINAUTOMATIK_DELTA)

### HU_NBT (CAFD 00000DED) — authored by Bundang Thunder 3 Series | Series: F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

* **Set time automatically                                                                                         --** by Bundang Thunder ^^**
  * Group `3000`
    * `navigation` (start=19, mask=00000110b, comment=SETTINGS_TIME_AUTOMATIC)
    * `01` (start=105, mask=00100000b, comment=CLOCK_CHANGE_AUTOMATIC)

* **Watch video/DMB/navigation while driving**
  * Group `3000`
    * `FF` (start=72, mask=11111111b, comment=SPEEDLOCK_X_KMH_MAX)
    * `FF` (start=71, mask=11111111b, comment=SPEEDLOCK_X_KMH_MIN)
    * `00` (start=5, mask=00010000b, comment=VIDEO_FRONT_LOCKED)
    * `00` (start=5, mask=00000100b, comment=VIDEO_HANDBRAKE)
    * `None` (start=57, mask=00000111b, comment=VIDEO_SPEEDLOCK_CONDITION)

* **Suppress all warning messages**
  * Group `3001`
    * `kein_ld` (start=58, mask=11111111b, comment=LEGAL_DISCLAIMER_TIME)
    * `kein_ld` (start=52, mask=11111111b, comment=MACRO_CAM_LEGALDISCLAIMER)

* **Enable trailer zoom menu when reversing**
  * Group `3001`
    * `01` (start=54, mask=00000001b, comment=MACRO_TRAILER_COUPLING)

* **Close windows when it rains**
  * Group `3000`
    * `01` (start=19, mask=00001000b, comment=REGEN_SCHLIESSEN)

* **X-Drive**
  * Group `3000`
    * `01` (start=5, mask=00000001b, comment=COMPASS)
    * `01` (start=15, mask=00000001b, comment=X_VIEW)
    * `trajectory1` (start=26, mask=00110000b, comment=X_VIEW_GRAPHIC_SLOP)
    * `trajectory1` (start=26, mask=11000000b, comment=X_VIEW_GRAPHIC_ROLL)
    * `01` (start=110, mask=00000010b, comment=MOMENTDISTRIBUTION_MENU)

* **Enable USB video playback 1/2**
  * Group `3000`
    * `01` (start=15, mask=00010000b, comment=ENT_CODEC_OGG)
    * `01` (start=15, mask=00100000b, comment=ENT_CODEC_XVID)
    * `01` (start=15, mask=01000000b, comment=ENT_CODEC_VCD)
    * `01` (start=13, mask=00000100b, comment=ENT_MC_VIDEO_SUPPORT)

* **Enable USB video playback 2/2**
  * Group `3003`
    * `both` (start=33, mask=00000110b, comment=API_USB_VIDEO)
    * `both` (start=33, mask=00011000b, comment=API_IPOD_VIDEO)

* **Change warning chime to Rolls-Royce sound**
  * Group `3002`
    * `rolls_royce` (start=26, mask=00111000b, comment=SOUND_SIGNAL_SET)

* **Configure Sport mode**
  * Group `3001`
    * `popup_and_config` (start=55, mask=00011000b, comment=MACRO_FDS)
  * Group `3000`
    * `01` (start=101, mask=00010000b, comment=EFF_DYN_SPORT_CID)
    * `01` (start=107, mask=00000100b, comment=EFF_DYN_SPORT_UNIT)

* **Startup animation**
  * Group `3001`
    * `animation` (start=62, mask=00000110b, comment=STARTUP_TYPE)
    * `variant_01` (start=62, mask=01111000b, comment=STARTUP_EMBLEM)

* **Volume adjustment bar**
  * Group `3002`
    * `01` (start=52, mask=01000000b, comment=VOLUME_POPUP_DISPLAY)
    * `01` (start=52, mask=10000000b, comment=VOLUME_POPUP_REJECTION)
    * `01` (start=53, mask=00000001b, comment=VOLUME_POPUP_EXCEPTION)

* **Show TPMC tire pressure temperature**
  * Group `3001`
    * `druck_und_temperatur` (start=66, mask=00001100b, comment=RDC_DRUCK_TEMP)

* **Output ringtone through speakers (iPhone only)**
  * Group `3003`
    * `01` (start=6, mask=10000000b, comment=INBAND_RINGING)

* **Lock/unlock confirmation chime (requires piezo buzzer sensor)**
  * Group `3000`
    * `01` (start=110, mask=00000001b, comment=ACOUSTICAL_LOCK_CONFIRM)

* **Change M Sport display cluster colors**
  * Group `3000`
    * `01` (start=133, mask=01000000b, comment=M_VEHICLE)

* **Adjust high-beam assistant in iDrive**
  * Group `3000`
    * `01` (start=109, mask=10000000b, comment=HIGH_BEAM_ASSISTANT)

* **Show currently playing album art in iDrive**
  * Group `3000`
    * `01` (start=9, mask=00000100b, comment=ENT_BTAS_IAP_COVERART)
  * Group `3003`
    * `01` (start=19, mask=00000100b, comment=ENT_BTAS_METADATA)
    * `01` (start=19, mask=00001000b, comment=ENT_BTAS_BROWSING)

* **Unlock DVD region code**
  * Group `3000`
    * `alle_anderen` (start=7, mask=11111111b, comment=ENT_VIDEO_DVD_AREA_CODE)

* **Show turn signals in HUD**
  * Group `3001`
    * `01` (start=55, mask=10000000b, comment=HUD_TURNSIGNAL)

* **Set sound system to Bang & Olufsen**
  * Group `3000`
    * `keine_insz` (start=21, mask=01100000b, comment=HIGH_END_AUDIO_B_UND_W)

* **Enable Logic7 (S667A HiFi vehicles)**
  * Group `3000`
    * `01` (start=22, mask=00001000b, comment=LOGIC7_SYMBOL)

* **Enhance audio mid-bass**
  * Group `3002`
    * `highpremium` (start=29, mask=00111100b, comment=AUDIO_SYSTEM)
    * `variant3` (start=21, mask=00000011b, comment=AUDIO_SYSTEM_VAR)

### ICMQL (CAFD 0000067B) — authored by Bundang Thunder 3 Series | Series: F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

* **Default to Eco mode at start**
  * Group `3000`
    * `verbaut` (start=36, mask=00001000b, comment=IcmKod_B_InitEco)

* **Enable cruise control**
  * Group `3000`
    * `01` (start=128, mask=00001110b, comment=C_Fahrfunktion)

* **Enable Sport+ mode**
  * Group `3000`
    * `verbaut` (start=18, mask=11111111b, comment=IcmKod_B_S2TBA)

### IHKA_VA02 (CAFD 000016EE) — authored by Bundang Thunder 3 Series | Series: F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

* **Remember last air conditioning state                                                                               --** by Bundang Thunder ^^**
  * Group `3003`
    * `01` (start=0, mask=00000010b, comment=MEMORY_OFF)

* **Prevent AUTO button from turning on A/C**
  * Group `3003`
    * `00` (start=0, mask=00000100b, comment=AC_ON_WITH_AUTO)

* **Remember HVAC recirculation mode**
  * Group `3003`
    * `01` (start=0, mask=00000001b, comment=MEMORY_UMLUFT)

### KAFAS2 (CAFD 00001148) — authored by Bundang Thunder 3 Series | Series: F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

* **Automatic high-beam assistant                                                                                --** by Bundang Thunder ^^**
  * Group `3050`
    * `FLA_on` (start=1, mask=00000001b, comment=FLA_ON_OFF)
    * `CN` (start=6, mask=11111111b, comment=SPEED_SWITCHING_HIGH_BEAMS_ON)
    * `China` (start=7, mask=11111111b, comment=SPEED_SWITCHING_HIGH_BEAMS_OFF)

### KOMBI FPK_I12 (CAFD 000009C8) — authored by Bundang Thunder 3 Series | Series: F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

* **Show phone, entertainment, and voice prompts in HUD                                                               --** by Bundang Thunder ^^**
  * Group `3003`
    * `01` (start=10, mask=00000001b, comment=HUD_ENTERTAINMENT_ENABLE)
    * `01` (start=5, mask=00000010b, comment=HUD_STARTUP_ENABLE)
  * Group `3000`
    * `01` (start=41, mask=00000001b, comment=HUD_TLC_ENABLE)
    * `01` (start=40, mask=10000000b, comment=HUD_VZA_ENABLE)

* **Show turn signals in HUD**
  * Group `3003`
    * `01` (start=4, mask=00000001b, comment=HUD_BLINKER_ENABLE)
  * Group `3008`
    * `01` (start=5, mask=00000001b, comment=HUD_PIA_BLINKER)

* **Show logo on instrument cluster**
  * Group `3003`
    * `01` (start=7, mask=00000010b, comment=MPM_ENABLE)
  * Group `3000`
    * `bmw` (start=43, mask=11110000b, comment=MPM_LOGO)
    * `mpm` (start=0, mask=00001111b, comment=BMW_LOGO)

* **Digital speed readout in cluster**
  * Group `3000`
    * `01` (start=1, mask=00000010b, comment=BC_DIGITAL_V)

* **Disable warning chime below 3 degrees**
  * Group `3000`
    * `00` (start=30, mask=00000001b, comment=CC_TEMPERATURWARNUNG)

* **Show auto start/stop status in cluster**
  * Group `3003`
    * `01` (start=6, mask=00001000b, comment=MSA_VERFUEGBARANZEIGE_ENABLE)

* **Use GPS time**
  * Group `3000`
    * `01` (start=1, mask=10000000b, comment=GPS_UHR)

* **Display gear number in Dynamic Sport mode**
  * Group `3000`
    * `01` (start=41, mask=00010000b, comment=SPA_SPORT_ENABLE)

* **Enable Sport+ menu in cluster**
  * Group `300C`
    * `menue_3` (start=0, mask=00001111b, comment=FDS_MENUE_TEXT_1)
    * `menue_3` (start=0, mask=11110000b, comment=FDS_MENUE_SIGNAL_1)
    * `menue_3` (start=1, mask=00001111b, comment=FDS_MENUE_TEXT_2)
    * `menue_3` (start=1, mask=11110000b, comment=FDS_MENUE_SIGNAL_2)
    * `menue_3` (start=2, mask=00001111b, comment=FDS_MENUE_TEXT_3)
    * `menue_3` (start=2, mask=11110000b, comment=FDS_MENUE_SIGNAL_3)
    * `menue_3` (start=3, mask=00001111b, comment=FDS_MENUE_TEXT_4)
    * `menue_3` (start=3, mask=11110000b, comment=FDS_MENUE_SIGNAL_4)
    * `menue_3` (start=54, mask=11111111b, comment=FDS_MENUE)

### CFAS_PLX_1 (CAFD 000000B5) — authored by Bundang Thunder 3 Series | Series: F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

* **Enable Easy Access                                                                         --** by Bundang Thunder ^^**
  * Group `3000`
    * `Modus_FA_SLV` (start=0, mask=00011100b, comment=EINAUSSTIEGSHILFE)

* **Easy Access seat starts moving from end position**
  * Group `3012`
    * `00, 01` (start=4, end=5, mask=11111111b, comment=EAH_SCHUTZFREIRAUM_HINTEN_SLV_PHYS)

* **Easy Access seat starts moving with 1 cm remaining**
  * Group `3012`
    * `00, 0A` (start=4, end=5, mask=11111111b, comment=EAH_SCHUTZFREIRAUM_HINTEN_SLV_PHYS)

* **Easy Access seat starts moving with 2 cm remaining**
  * Group `3012`
    * `00, 14` (start=4, end=5, mask=11111111b, comment=EAH_SCHUTZFREIRAUM_HINTEN_SLV_PHYS)

* **Easy Access seat starts moving with 3 cm remaining**
  * Group `3012`
    * `00, 1E` (start=4, end=5, mask=11111111b, comment=EAH_SCHUTZFREIRAUM_HINTEN_SLV_PHYS)

* **Easy Access seat travel distance: 4 cm**
  * Group `3012`
    * `00, 28` (start=0, end=1, mask=11111111b, comment=EAH_VERFAHRWEG_SLV_PHYS)

* **Easy Access seat travel distance: 5 cm**
  * Group `3012`
    * `00, 32` (start=0, end=1, mask=11111111b, comment=EAH_VERFAHRWEG_SLV_PHYS)

* **Easy Access seat travel distance: 6 cm**
  * Group `3012`
    * `00, 3C` (start=0, end=1, mask=11111111b, comment=EAH_VERFAHRWEG_SLV_PHYS)

* **Easy Access seat travel distance: 7 cm**
  * Group `3012`
    * `00, 46` (start=0, end=1, mask=11111111b, comment=EAH_VERFAHRWEG_SLV_PHYS)

* **Gentleman**
  * Group `3000`
    * `01` (start=1, mask=00000001b, comment=GENTLEMAN)
    * `01` (start=0, mask=00000001b, comment=MEMORY)

* **Set gong when saving seat position**
  * Group `3000`
    * `01` (start=2, mask=00001000b, comment=MEMORY_GONG)

### TRSVC (CAFD 00000223) — authored by Bundang Thunder 3 Series | Series: F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

* **Allow side view at any time                                                                   --** by Bundang Thunder ^^**
  * Group `3000`
    * `FF` (start=114, mask=11111111b, comment=SV_Activate_Speed_Limit)
    * `FF` (start=115, mask=11111111b, comment=SV_Deactivate_Speed)

### ACSM_4B (CAFD 00000911) — authored by Bundang Thunder 4 Series | Series: F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

* **Seat belt warning chime for only 5 seconds                                                                                 --** by Bundang Thunder ^^**
  * Group `3001`
    * `05` (start=3, mask=11111111b, comment=GWF_SBR_WARNDAUER)

* **Delete driver seat belt warning light**
  * Group `3000`
    * `00` (start=16, mask=00000001b, comment=SBR_PreWarning_Fahrer)

* **Delete passenger seat belt warning light**
  * Group `3000`
    * `00` (start=16, mask=00000010b, comment=SBR_PreWarning_Beifahrer)

* **Disable driver seat belt warning chime**
  * Group `3000`
    * `00` (start=15, mask=00000010b, comment=SeatBeltReminder_SBR_Fahrer)

* **Disable passenger seat belt warning chime**
  * Group `3000`
    * `00` (start=15, mask=00000100b, comment=SeatBeltReminder_SBR_Beifahrer)

### ASD01 (CAFD 00000F9B) — authored by Bundang Thunder 4 Series | Series: F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

* **Set exhaust sound to M4 engine                                                                                       --** by Bundang Thunder ^^**
  * Group `3000`
    * `16` (start=0, mask=11111111b, comment=Model Range)
    * `0A` (start=1, mask=11111111b, comment=Engine)

* **ASD audio level**
  * Group `3000`
    * `01` (start=2, mask=11111111b, comment=Audio Level)

* **ASD power class maximum**
  * Group `3000`
    * `03` (start=3, mask=11111111b, comment=Power Class)

* **ASD power class medium**
  * Group `3000`
    * `00` (start=3, mask=11111111b, comment=Power Class)

### DSC_CT01 (CAFD 000019CC) — authored by Bundang Thunder 4 Series | Series: F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

* **Enable launch control (also enables EGS)                                                                     --** by Bundang Thunder ^^**
  * Group `3000`
    * `01` (start=26, mask=00010000b, comment=C_Funktion_LaunchControl)

### GKEB23 (CAFD 0000023F) — authored by Bundang Thunder 4 Series | Series: F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

* **Enable launch control (also enables DSC)                                                                     --** by Bundang Thunder ^^**
  * Group `3000`
    * `01` (start=1, mask=10000000b, comment=LC)

* **Show gear number in Dynamic Sport mode**
  * Group `3000`
    * `01` (start=1, mask=00000001b, comment=Sportschalter)
    * `01` (start=0, mask=01000000b, comment=Sportschalter_alt)

### FEM_01 (CAFD 00000794) — authored by Bundang Thunder 4 Series | Series: F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

* **Activate hazard lights during hard braking                                                                                   --** by Bundang Thunder ^^**
  * Group `3060`
    * `01` (start=26, mask=00000001b, comment=WB_GB_ENABLE)

* **Set auto start/stop off by default**
  * Group `3023`
    * `01` (start=0, mask=00010000b, comment=TCM_MSA_DEFAULT_OFF)

* **Remember last auto start/stop state**
  * Group `3023`
    * `01` (start=0, mask=00100000b, comment=TCM_MSA_MEMORY)

* **Turn off audio when engine stops**
  * Group `3020`
    * `01` (start=1, mask=00000001b, comment=TCM_LOGIC_R_OFF_DOOR)

* **Double horn when locking with engine running - enable**
  * Group `3040`
    * `01` (start=1, mask=00100000b, comment=CLM_HORN_AT_SECURE)

* **Double horn when locking with engine running - disable**
  * Group `3040`
    * `00` (start=1, mask=00100000b, comment=CLM_HORN_AT_SECURE)

* **Fold mirrors immediately when locking (lock folding)**
  * Group `3053`
    * `00` (start=9, mask=11111111b, comment=KOMFORT_SCHLIESSEN)

* **Start engine without pressing brake**
  * Group `3020`
    * `00` (start=0, mask=00000001b, comment=TCM_STARTLOCK_BRAKE)

* **Start engine without pressing clutch**
  * Group `3020`
    * `00` (start=0, mask=00000100b, comment=TCM_STARTLOCK_CLUTCH)

* **Allow engine start in park**
  * Group `3020`
    * `00` (start=0, mask=00000010b, comment=TCM_STARTLOCK_PARK)
    * `00` (start=1, mask=00010000b, comment=TCM_STARTLOCK_DRIVINGREADINESS)

* **One-touch turn signal flashes five times**
  * Group `3060`
    * `04` (start=7, mask=00000111b, comment=BLINKZYKLEN_ANZAHL_TIPP)

* **Welcome fog lights (hard on)**
  * Group `3063`
    * `hard_On` (start=55, mask=11000000b, comment=MAPPING_NEBELSCHW_L_PART_OF_WL)
    * `hard_On` (start=66, mask=11000000b, comment=MAPPING_NEBELSCHW_R_PART_OF_WL)

* **Welcome fog lights (soft on)**
  * Group `3063`
    * `soft_On` (start=55, mask=11000000b, comment=MAPPING_NEBELSCHW_L_PART_OF_WL)
    * `soft_On` (start=66, mask=11000000b, comment=MAPPING_NEBELSCHW_R_PART_OF_WL)

* **Cornering fog lights**
  * Group `3073`
    * `01` (start=218, mask=00000010b, comment=C_CLC_ENA)
    * `01` (start=66, mask=00000001b, comment=C_BLC_ENA)
  * Group `3066`
    * `KL_Ein` (start=0, mask=00000001b, comment=KL_ENABLE_LI)
    * `KL_Ein` (start=80, mask=00000001b, comment=KL_ENABLE_RE)
  * Group `3062`
    * `0B` (start=110, mask=00111111b, comment=MAPPING_abbiegel_L_output)
    * `0C` (start=121, mask=00111111b, comment=MAPPING_abbiegel_R_output)

* **Turn on catch lights when reversing**
  * Group `3070`
    * `01` (start=11, mask=00010000b, comment=OVT_BEI_RUECKFAHRLICHT)

* **Unlock doors automatically when engine off**
  * Group `3040`
    * `01` (start=1, mask=00000010b, comment=CLM_UNLOCK_KL15OFF_AFTER_PIA_AUTO_LOCK)

* **Enable paddle shifter operation**
  * Group `3190`
    * `01` (start=0, mask=00000001b, comment=PADDLES_VERBAUT)

* **Allow windows to keep closing with door open**
  * Group `3050`
    * `00` (start=0, mask=00000001b, comment=FH_TUERAUF_STOP_MAUT)

* **Limit passenger mirror tilt to 30 degrees in reverse**
  * Group `3110`
    * `1E` (start=1, mask=11111111b, comment=ASP_BORDSTEINAUTOMATIK_DELTA)

### HU_NBT (CAFD 00000DED) — authored by Bundang Thunder 4 Series | Series: F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

* **Set time automatically                                                                                         --** by Bundang Thunder ^^**
  * Group `3000`
    * `navigation` (start=19, mask=00000110b, comment=SETTINGS_TIME_AUTOMATIC)
    * `01` (start=105, mask=00100000b, comment=CLOCK_CHANGE_AUTOMATIC)

* **Watch video/DMB/navigation while driving**
  * Group `3000`
    * `FF` (start=72, mask=11111111b, comment=SPEEDLOCK_X_KMH_MAX)
    * `FF` (start=71, mask=11111111b, comment=SPEEDLOCK_X_KMH_MIN)
    * `00` (start=5, mask=00010000b, comment=VIDEO_FRONT_LOCKED)
    * `00` (start=5, mask=00000100b, comment=VIDEO_HANDBRAKE)
    * `None` (start=57, mask=00000111b, comment=VIDEO_SPEEDLOCK_CONDITION)

* **Suppress all warning messages**
  * Group `3001`
    * `kein_ld` (start=58, mask=11111111b, comment=LEGAL_DISCLAIMER_TIME)
    * `kein_ld` (start=52, mask=11111111b, comment=MACRO_CAM_LEGALDISCLAIMER)

* **Enable trailer zoom menu when reversing**
  * Group `3001`
    * `01` (start=54, mask=00000001b, comment=MACRO_TRAILER_COUPLING)

* **Close windows when it rains**
  * Group `3000`
    * `01` (start=19, mask=00001000b, comment=REGEN_SCHLIESSEN)

* **X-Drive**
  * Group `3000`
    * `01` (start=5, mask=00000001b, comment=COMPASS)
    * `01` (start=15, mask=00000001b, comment=X_VIEW)
    * `trajectory1` (start=26, mask=00110000b, comment=X_VIEW_GRAPHIC_SLOP)
    * `trajectory1` (start=26, mask=11000000b, comment=X_VIEW_GRAPHIC_ROLL)
    * `01` (start=110, mask=00000010b, comment=MOMENTDISTRIBUTION_MENU)

* **Enable USB video playback 1/2**
  * Group `3000`
    * `01` (start=15, mask=00010000b, comment=ENT_CODEC_OGG)
    * `01` (start=15, mask=00100000b, comment=ENT_CODEC_XVID)
    * `01` (start=15, mask=01000000b, comment=ENT_CODEC_VCD)
    * `01` (start=13, mask=00000100b, comment=ENT_MC_VIDEO_SUPPORT)

* **Enable USB video playback 2/2**
  * Group `3003`
    * `both` (start=33, mask=00000110b, comment=API_USB_VIDEO)
    * `both` (start=33, mask=00011000b, comment=API_IPOD_VIDEO)

* **Change warning chime to Rolls-Royce sound**
  * Group `3002`
    * `rolls_royce` (start=26, mask=00111000b, comment=SOUND_SIGNAL_SET)

* **Configure Sport mode**
  * Group `3001`
    * `popup_and_config` (start=55, mask=00011000b, comment=MACRO_FDS)
  * Group `3000`
    * `01` (start=101, mask=00010000b, comment=EFF_DYN_SPORT_CID)
    * `01` (start=107, mask=00000100b, comment=EFF_DYN_SPORT_UNIT)

* **Startup animation**
  * Group `3001`
    * `animation` (start=62, mask=00000110b, comment=STARTUP_TYPE)
    * `variant_01` (start=62, mask=01111000b, comment=STARTUP_EMBLEM)

* **Volume adjustment bar**
  * Group `3002`
    * `01` (start=52, mask=01000000b, comment=VOLUME_POPUP_DISPLAY)
    * `01` (start=52, mask=10000000b, comment=VOLUME_POPUP_REJECTION)
    * `01` (start=53, mask=00000001b, comment=VOLUME_POPUP_EXCEPTION)

* **Show TPMC tire pressure temperature**
  * Group `3001`
    * `druck_und_temperatur` (start=66, mask=00001100b, comment=RDC_DRUCK_TEMP)

* **Output ringtone through speakers (iPhone only)**
  * Group `3003`
    * `01` (start=6, mask=10000000b, comment=INBAND_RINGING)

* **Lock/unlock confirmation chime (requires piezo buzzer sensor)**
  * Group `3000`
    * `01` (start=110, mask=00000001b, comment=ACOUSTICAL_LOCK_CONFIRM)

* **Change M Sport display cluster colors**
  * Group `3000`
    * `01` (start=133, mask=01000000b, comment=M_VEHICLE)

* **Adjust high-beam assistant in iDrive**
  * Group `3000`
    * `01` (start=109, mask=10000000b, comment=HIGH_BEAM_ASSISTANT)

* **Show currently playing album art in iDrive**
  * Group `3000`
    * `01` (start=9, mask=00000100b, comment=ENT_BTAS_IAP_COVERART)
  * Group `3003`
    * `01` (start=19, mask=00000100b, comment=ENT_BTAS_METADATA)
    * `01` (start=19, mask=00001000b, comment=ENT_BTAS_BROWSING)

* **Unlock DVD region code**
  * Group `3000`
    * `alle_anderen` (start=7, mask=11111111b, comment=ENT_VIDEO_DVD_AREA_CODE)

* **Show turn signals in HUD**
  * Group `3001`
    * `01` (start=55, mask=10000000b, comment=HUD_TURNSIGNAL)

* **Set sound system to Bang & Olufsen**
  * Group `3000`
    * `keine_insz` (start=21, mask=01100000b, comment=HIGH_END_AUDIO_B_UND_W)

* **Enable Logic7 (S667A HiFi vehicles)**
  * Group `3000`
    * `01` (start=22, mask=00001000b, comment=LOGIC7_SYMBOL)

* **Enhance audio mid-bass**
  * Group `3002`
    * `highpremium` (start=29, mask=00111100b, comment=AUDIO_SYSTEM)
    * `variant3` (start=21, mask=00000011b, comment=AUDIO_SYSTEM_VAR)

### ICMQL (CAFD 0000067B) — authored by Bundang Thunder 4 Series | Series: F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

* **Default to Eco mode at start                                                                              --** by Bundang Thunder ^^**
  * Group `3000`
    * `verbaut` (start=36, mask=00001000b, comment=IcmKod_B_InitEco)

* **Enable cruise control**
  * Group `3000`
    * `01` (start=128, mask=00001110b, comment=C_Fahrfunktion)

* **Enable Sport+ mode**
  * Group `3000`
    * `verbaut` (start=18, mask=11111111b, comment=IcmKod_B_S2TBA)

### IHKA_VA02 (CAFD 000016EE) — authored by Bundang Thunder 4 Series | Series: F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

* **Remember last air conditioning state                                                                               --** by Bundang Thunder ^^**
  * Group `3003`
    * `01` (start=0, mask=00000010b, comment=MEMORY_OFF)

* **Prevent AUTO button from turning on A/C**
  * Group `3003`
    * `00` (start=0, mask=00000100b, comment=AC_ON_WITH_AUTO)

* **Remember HVAC recirculation mode**
  * Group `3003`
    * `01` (start=0, mask=00000001b, comment=MEMORY_UMLUFT)

### KAFAS2 (CAFD 00001148) — authored by Bundang Thunder 4 Series | Series: F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

* **Automatic high-beam assistant                                                                                --** by Bundang Thunder ^^**
  * Group `3050`
    * `FLA_on` (start=1, mask=00000001b, comment=FLA_ON_OFF)
    * `CN` (start=6, mask=11111111b, comment=SPEED_SWITCHING_HIGH_BEAMS_ON)
    * `China` (start=7, mask=11111111b, comment=SPEED_SWITCHING_HIGH_BEAMS_OFF)

### KOMBI L7_MID (CAFD 000009C8) — authored by Bundang Thunder 4 Series | Series: F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

* **Show phone, entertainment, and voice prompts in HUD                                                               --** by Bundang Thunder ^^**
  * Group `3003`
    * `01` (start=4, mask=00010000b, comment=HUD_ENTERTAINMENT_ENABLE)
    * `01` (start=5, mask=00000010b, comment=HUD_STARTUP_ENABLE)
  * Group `3000`
    * `01` (start=41, mask=00000001b, comment=HUD_TLC_ENABLE)
    * `01` (start=42, mask=00001000b, comment=HUD_VZA_ENABLE)

* **Show turn signals in HUD**
  * Group `3003`
    * `01` (start=4, mask=00000001b, comment=HUD_BLINKER_ENABLE)
  * Group `3008`
    * `01` (start=5, mask=00000001b, comment=HUD_PIA_BLINKER)

* **Show logo on instrument cluster**
  * Group `3003`
    * `01` (start=7, mask=00000100b, comment=MPM_ENABLE)
  * Group `3000`
    * `ag` (start=43, mask=11110000b, comment=MPM_LOGO)
    * `m_performance` (start=0, mask=11110000b, comment=BMW_LOGO)

* **Digital speed readout in cluster**
  * Group `3000`
    * `01` (start=1, mask=00000010b, comment=BC_DIGITAL_V)

* **Disable warning chime below 3 degrees**
  * Group `3000`
    * `00` (start=30, mask=00000001b, comment=CC_TEMPERATURWARNUNG)

* **Show auto start/stop status in cluster**
  * Group `3003`
    * `01` (start=6, mask=00001000b, comment=MSA_VERFUEGBARANZEIGE_ENABLE)

* **Use GPS time**
  * Group `3000`
    * `01` (start=1, mask=10000000b, comment=GPS_UHR)

* **Display gear number in Dynamic Sport mode**
  * Group `3000`
    * `01` (start=41, mask=00010000b, comment=SPA_SPORT_ENABLE)

* **Enable Sport+ menu in cluster**
  * Group `300C`
    * `menue_3` (start=0, mask=00001111b, comment=FDS_MENUE_TEXT_1)
    * `menue_3` (start=0, mask=11110000b, comment=FDS_MENUE_SIGNAL_1)
    * `menue_3` (start=1, mask=00001111b, comment=FDS_MENUE_TEXT_2)
    * `menue_3` (start=1, mask=11110000b, comment=FDS_MENUE_SIGNAL_2)
    * `menue_3` (start=2, mask=00001111b, comment=FDS_MENUE_TEXT_3)
    * `menue_3` (start=2, mask=11110000b, comment=FDS_MENUE_SIGNAL_3)
    * `menue_3` (start=3, mask=00001111b, comment=FDS_MENUE_TEXT_4)
    * `menue_3` (start=3, mask=11110000b, comment=FDS_MENUE_SIGNAL_4)
    * `menue_3` (start=54, mask=11111111b, comment=FDS_MENUE)

### CFAS_PLX_1 (CAFD 000000B5) — authored by Bundang Thunder 4 Series | Series: F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

* **Enable Easy Access                                                                         --** by Bundang Thunder ^^**
  * Group `3000`
    * `Modus_FA_SLV` (start=0, mask=00011100b, comment=EINAUSSTIEGSHILFE)

* **Easy Access seat starts moving from end position**
  * Group `3012`
    * `00, 01` (start=4, end=5, mask=11111111b, comment=EAH_SCHUTZFREIRAUM_HINTEN_SLV_PHYS)

* **Easy Access seat starts moving with 1 cm remaining**
  * Group `3012`
    * `00, 0A` (start=4, end=5, mask=11111111b, comment=EAH_SCHUTZFREIRAUM_HINTEN_SLV_PHYS)

* **Easy Access seat starts moving with 2 cm remaining**
  * Group `3012`
    * `00, 14` (start=4, end=5, mask=11111111b, comment=EAH_SCHUTZFREIRAUM_HINTEN_SLV_PHYS)

* **Easy Access seat starts moving with 3 cm remaining**
  * Group `3012`
    * `00, 1E` (start=4, end=5, mask=11111111b, comment=EAH_SCHUTZFREIRAUM_HINTEN_SLV_PHYS)

* **Easy Access seat travel distance: 4 cm**
  * Group `3012`
    * `00, 28` (start=0, end=1, mask=11111111b, comment=EAH_VERFAHRWEG_SLV_PHYS)

* **Easy Access seat travel distance: 5 cm**
  * Group `3012`
    * `00, 32` (start=0, end=1, mask=11111111b, comment=EAH_VERFAHRWEG_SLV_PHYS)

* **Easy Access seat travel distance: 6 cm**
  * Group `3012`
    * `00, 3C` (start=0, end=1, mask=11111111b, comment=EAH_VERFAHRWEG_SLV_PHYS)

* **Easy Access seat travel distance: 7 cm**
  * Group `3012`
    * `00, 46` (start=0, end=1, mask=11111111b, comment=EAH_VERFAHRWEG_SLV_PHYS)

* **Gentleman**
  * Group `3000`
    * `01` (start=1, mask=00000001b, comment=GENTLEMAN)
    * `01` (start=0, mask=00000001b, comment=MEMORY)

* **Set gong when saving seat position**
  * Group `3000`
    * `01` (start=2, mask=00001000b, comment=MEMORY_GONG)

### TRSVC (CAFD 00000223) — authored by Bundang Thunder 4 Series | Series: F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

* **Allow side view at any time                                                                   --** by Bundang Thunder ^^**
  * Group `3000`
    * `FF` (start=114, mask=11111111b, comment=SV_Activate_Speed_Limit)
    * `FF` (start=115, mask=11111111b, comment=SV_Deactivate_Speed)

### ACSM_4C (CAFD 00000909) — authored by Bundang Thunder 5 Series | Series: F06,F10,F11,F12,F13,F18

* **Seat belt warning chime for only 5 seconds                                                                                 --** by Bundang Thunder ^^**
  * Group `3001`
    * `05` (start=3, mask=11111111b, comment=GWF_SBR_WARNDAUER)

* **Delete driver seat belt warning light**
  * Group `3000`
    * `00` (start=16, mask=00000001b, comment=SBR_PreWarning_Fahrer)

* **Delete passenger seat belt warning light**
  * Group `3000`
    * `00` (start=16, mask=00000010b, comment=SBR_PreWarning_Beifahrer)

* **Disable driver seat belt warning chime**
  * Group `3000`
    * `00` (start=15, mask=00000010b, comment=SeatBeltReminder_SBR_Fahrer)

* **Disable passenger seat belt warning chime**
  * Group `3000`
    * `00` (start=15, mask=00000100b, comment=SeatBeltReminder_SBR_Beifahrer)

### ASD01 (CAFD 00000F9B) — authored by Bundang Thunder 5 Series | Series: F06,F10,F11,F12,F13,F18

* **Set exhaust sound to M5 engine --** by Bundang Thunder ^^**
  * Group `3000`
    * `00` (start=0, mask=11111111b, comment=Model Range)
    * `01` (start=1, mask=11111111b, comment=Engine)

* **ASD audio level**
  * Group `3000`
    * `01` (start=2, mask=11111111b, comment=Audio Level)

* **ASD power class maximum**
  * Group `3000`
    * `03` (start=3, mask=11111111b, comment=Power Class)

* **ASD power class medium**
  * Group `3000`
    * `00` (start=3, mask=11111111b, comment=Power Class)

### CAS_04 (CAFD 0000000F) — authored by Bundang Thunder 5 Series | Series: F06,F10,F11,F12,F13,F18

* **Turn off audio when engine stops                                                                                  --** by Bundang Thunder ^^**
  * Group `3000`
    * `01` (start=2, mask=00000001b, comment=TC_LOGIC_KLR_OFF_DOOR)

* **Unlock doors when engine turns off**
  * Group `3002`
    * `01` (start=1, mask=10000000b, comment=ER_KEYOUT_AUTOVR)

* **Double horn when locking with engine running - enable**
  * Group `3002`
    * `01` (start=0, mask=00100000b, comment=CLM_HORN_AT_SECURE)

* **Double horn when locking with engine running - disable**
  * Group `3002`
    * `00` (start=0, mask=00100000b, comment=CLM_HORN_AT_SECURE)

* **Set auto start/stop off by default**
  * Group `3000`
    * `01` (start=3, mask=00010000b, comment=TC_MSA_DEFAULT_OFF)

* **Remember last auto start/stop state**
  * Group `3000`
    * `01` (start=3, mask=00100000b, comment=TC_MSA_MEMORY)

* **Fold mirrors immediately when locking (lock folding)**
  * Group `3003`
    * `00` (start=12, mask=11111111b, comment=KMFRT_SCHLIESSEN)

* **Start engine without pressing brake**
  * Group `3000`
    * `00` (start=1, mask=00000001b, comment=TC_STARTLOCK_BRAKE)

* **Start engine without pressing clutch**
  * Group `3000`
    * `00` (start=1, mask=00000100b, comment=TC_STARTLOCK_CLUTCH)

* **Allow engine start in park**
  * Group `3000`
    * `00` (start=1, mask=00000010b, comment=TC_STARTLOCK_PARK)
    * `00` (start=1, mask=00010000b, comment=TC_STARTLOCK_DRIVINGREADINESS)

* **Sound horn with remote**
  * Group `3002`
    * `01` (start=1, mask=00000010b, comment=REMOTE_KEY_SPECIAL_FCT)

### DSC_Premium (CAFD 00000C18) — authored by Bundang Thunder 5 Series | Series: F06,F10,F11,F12,F13,F18

* **Release parking brake by pressing accelerator only --** by Bundang Thunder ^^**
  * Group `3000`
    * `01` (start=27, mask=00100000b, comment=Funktion_AutomaticDriveawayRelease_aktiv)

* **Enable launch control (also enables EGS)**
  * Group `3000`
    * `01` (start=31, mask=00001000b, comment=Funktion_LaunchControl_aktiv)

### GKEB23 (CAFD 0000023F) — authored by Bundang Thunder 5 Series | Series: F06,F10,F11,F12,F13,F18

* **Enable launch control (also enables DSC)                                                                     --** by Bundang Thunder ^^**
  * Group `3000`
    * `01` (start=1, mask=10000000b, comment=LC)

* **Show gear number in Dynamic Sport mode**
  * Group `3000`
    * `01` (start=1, mask=00000001b, comment=Sportschalter)
    * `01` (start=0, mask=01000000b, comment=Sportschalter_alt)

### FRM__03CT (CAFD 0000106D) — authored by Bundang Thunder 5 Series | Series: F06,F10,F11,F12,F13,F18

* **Activate hazard lights during hard braking                                                                                   --** by Bundang Thunder ^^**
  * Group `3050`
    * `01` (start=2, mask=10000000b, comment=WB_GB_ENABLE)

* **Turn on fog lights in welcome lighting**
  * Group `3050`
    * `soft_on_LED` (start=29, mask=00001100b, comment=WL_FUNKTION_NSW)

* **Turn on headlights in welcome lighting**
  * Group `3050`
    * `soft_on_LED` (start=30, mask=00001100b, comment=WL_FUNKTION_AL)

* **Automatic high-beam assistant**
  * Group `3050`
    * `automatisch` (start=20, mask=00100000b, comment=FLA_AUTO_01)
    * `01` (start=20, mask=00010000b, comment=FLA_VERBAUT)

* **Allow front windows to keep closing with door open**
  * Group `3030`
    * `00` (start=1, mask=00000100b, comment=FH_TUER_AUF_STOP_MAUT)

* **Limit passenger mirror tilt to 30 degrees in reverse**
  * Group `3020`
    * `1E` (start=1, mask=11111111b, comment=ASP_BORDSTEINAUTOMATIK_DELTA)

* **One-touch turn signal flashes five times**
  * Group `3050`
    * `04` (start=1, mask=00000111b, comment=BLINKZYKLEN_ANZAHL_TIPP)

### FRM_03CT (CAFD 0000012F) — authored by Bundang Thunder 5 Series | Series: F06,F10,F11,F12,F13,F18

* **Activate hazard lights during hard braking                                                                                   --** by Bundang Thunder ^^**
  * Group `3050`
    * `01` (start=2, mask=10000000b, comment=WB_GB_ENABLE)

* **Turn on fog lights in welcome lighting**
  * Group `3050`
    * `soft_on_LED` (start=29, mask=00001100b, comment=WL_FUNKTION_NSW)

* **Turn on headlights in welcome lighting**
  * Group `3050`
    * `soft_on_LED` (start=30, mask=00001100b, comment=WL_FUNKTION_AL)

* **Allow front windows to keep closing with door open**
  * Group `3030`
    * `00` (start=1, mask=00000100b, comment=FH_TUER_AUF_STOP_MAUT)

* **Limit passenger mirror tilt to 30 degrees in reverse**
  * Group `3020`
    * `1E` (start=1, mask=11111111b, comment=ASP_BORDSTEINAUTOMATIK_DELTA)

### FZD__04 (CAFD 00000552) — authored by Bundang Thunder 5 Series | Series: F06,F10,F11,F12,F13,F18

* **Door open/close chime --** by Bundang Thunder ^^**
  * Group `3002`
    * `01` (start=4, mask=00001000b, comment=Akkustische Quittierung Schaerfen)
    * `01` (start=4, mask=00010000b, comment=Akkustische Quittierung Schaerfen mit Klappenbeachtung)
    * `01` (start=4, mask=00100000b, comment=Akkustische Quittierung Entschaerfen)
    * `01` (start=2, mask=00010000b, comment=Lautstaerke Akkustische Quittterung tageszeitabhaengig)

### HKFM (CAFD 000007C8) — authored by Bundang Thunder 5 Series | Series: F06,F10,F11,F12,F13,F18

* **Auto-close trunk (footwell switch + remote)                                                                   --** by Bundang Thunder ^^**
  * Group `3010`
    * `01` (start=0, mask=00001000b, comment=TASTER_FBD)
    * `01` (start=2, mask=00000100b, comment=SCH_TOEHKI)
    * `01` (start=2, mask=00001000b, comment=SCH_FBD)

### HU_CICHB (CAFD 000000F9) — authored by Bundang Thunder 5 Series | Series: F06,F10,F11,F12,F13,F18

* **Watch video/DMB/navigation while driving                                                                          --** by Bundang Thunder ^^**
  * Group `3000`
    * `FF` (start=24, mask=11111111b, comment=SPEEDLOCK_X_KMH_MAX)
    * `FF` (start=23, mask=11111111b, comment=SPEEDLOCK_X_KMH_MIN)
    * `00` (start=8, mask=00000000b, comment=VIDEO_NUR_MIT_HANDBREMSE)
    * `00` (start=9, mask=10000000b, comment=ENT_VIDEO_VORNE_GESPERRT)

* **Suppress all warning messages**
  * Group `3001`
    * `kein_ld` (start=27, mask=11111111b, comment=LEGAL_DISCLAIMER_TIME)
    * `kein_ld` (start=28, mask=11111111b, comment=MACRO_CAM_LEGALDISCLAIMER)

* **Enable trailer zoom menu when reversing**
  * Group `3001`
    * `01` (start=23, mask=00000001b, comment=MACRO_TRAILER_COUPLING)

* **Configure Sport mode**
  * Group `3000`
    * `popup_and_config` (start=7, mask=00110000b, comment=MACRO_FDS)
  * Group `3000`
    * `01` (start=47, mask=00010000b, comment=EFF_DYN_SPORT_CID)
    * `01` (start=61, mask=00000100b, comment=EFF_DYN_SPORT_UNIT)

* **Output ringtone through speakers (iPhone only)**
  * Group `3003`
    * `01` (start=6, mask=10000000b, comment=INBAND_RINGING)

* **Lock/unlock confirmation chime (requires piezo buzzer sensor)**
  * Group `3000`
    * `01` (start=8, mask=00100000b, comment=ACOUSTICAL_LOCK_CONFIRM)

* **Adjust high-beam assistant in iDrive**
  * Group `3000`
    * `01` (start=0, mask=00000010b, comment=HIGH_BEAM_ASSISTANT)

* **Show turn signals in HUD**
  * Group `3000`
    * `01` (start=22, end=2, mask=00001000b, comment=HUD_TURNSIGNAL)

* **Enable Logic7 (S667A HiFi vehicles)**
  * Group `3000`
    * `01` (start=4, mask=10000000b, comment=LOGIC7_SYMBOL)

* **Enhance audio mid-bass**
  * Group `3002`
    * `03` (start=0, mask=00000111b, comment=AUDIO_SYSTEM_CIC)
    * `03` (start=5, mask=00001100b, comment=AUDIO_SYSTEM_VAR)

### HU_NBT (CAFD 00000DED) — authored by Bundang Thunder 5 Series | Series: F06,F10,F11,F12,F13,F18

* **Set time automatically                                                                                         --** by Bundang Thunder ^^**
  * Group `3000`
    * `navigation` (start=19, mask=00000110b, comment=SETTINGS_TIME_AUTOMATIC)
    * `01` (start=105, mask=00100000b, comment=CLOCK_CHANGE_AUTOMATIC)

* **Watch video/DMB/navigation while driving**
  * Group `3000`
    * `FF` (start=72, mask=11111111b, comment=SPEEDLOCK_X_KMH_MAX)
    * `FF` (start=71, mask=11111111b, comment=SPEEDLOCK_X_KMH_MIN)
    * `00` (start=5, mask=00010000b, comment=VIDEO_FRONT_LOCKED)
    * `00` (start=5, mask=00000100b, comment=VIDEO_HANDBRAKE)
    * `None` (start=57, mask=00000111b, comment=VIDEO_SPEEDLOCK_CONDITION)

* **Suppress all warning messages**
  * Group `3001`
    * `kein_ld` (start=58, mask=11111111b, comment=LEGAL_DISCLAIMER_TIME)
    * `kein_ld` (start=52, mask=11111111b, comment=MACRO_CAM_LEGALDISCLAIMER)

* **Enable trailer zoom menu when reversing**
  * Group `3001`
    * `01` (start=54, mask=00000001b, comment=MACRO_TRAILER_COUPLING)

* **Close windows when it rains**
  * Group `3000`
    * `01` (start=19, mask=00001000b, comment=REGEN_SCHLIESSEN)

* **X-Drive**
  * Group `3000`
    * `01` (start=5, mask=00000001b, comment=COMPASS)
    * `01` (start=15, mask=00000001b, comment=X_VIEW)
    * `trajectory1` (start=26, mask=00110000b, comment=X_VIEW_GRAPHIC_SLOP)
    * `trajectory1` (start=26, mask=11000000b, comment=X_VIEW_GRAPHIC_ROLL)
    * `01` (start=110, mask=00000010b, comment=MOMENTDISTRIBUTION_MENU)

* **Enable USB video playback 1/2**
  * Group `3000`
    * `01` (start=15, mask=00010000b, comment=ENT_CODEC_OGG)
    * `01` (start=15, mask=00100000b, comment=ENT_CODEC_XVID)
    * `01` (start=15, mask=01000000b, comment=ENT_CODEC_VCD)
    * `01` (start=13, mask=00000100b, comment=ENT_MC_VIDEO_SUPPORT)

* **Enable USB video playback 2/2**
  * Group `3003`
    * `both` (start=33, mask=00000110b, comment=API_USB_VIDEO)
    * `both` (start=33, mask=00011000b, comment=API_IPOD_VIDEO)

* **Change warning chime to Rolls-Royce sound**
  * Group `3002`
    * `rolls_royce` (start=26, mask=00111000b, comment=SOUND_SIGNAL_SET)

* **Configure Sport mode**
  * Group `3001`
    * `popup_and_config` (start=55, mask=00011000b, comment=MACRO_FDS)
  * Group `3000`
    * `01` (start=101, mask=00010000b, comment=EFF_DYN_SPORT_CID)
    * `01` (start=107, mask=00000100b, comment=EFF_DYN_SPORT_UNIT)

* **Startup animation**
  * Group `3001`
    * `animation` (start=62, mask=00000110b, comment=STARTUP_TYPE)
    * `variant_01` (start=62, mask=01111000b, comment=STARTUP_EMBLEM)

* **Volume adjustment bar**
  * Group `3002`
    * `01` (start=52, mask=01000000b, comment=VOLUME_POPUP_DISPLAY)
    * `01` (start=52, mask=10000000b, comment=VOLUME_POPUP_REJECTION)
    * `01` (start=53, mask=00000001b, comment=VOLUME_POPUP_EXCEPTION)

* **Show TPMC tire pressure temperature**
  * Group `3001`
    * `druck_und_temperatur` (start=66, mask=00001100b, comment=RDC_DRUCK_TEMP)

* **Output ringtone through speakers (iPhone only)**
  * Group `3003`
    * `01` (start=6, mask=10000000b, comment=INBAND_RINGING)

* **Lock/unlock confirmation chime (requires piezo buzzer sensor)**
  * Group `3000`
    * `01` (start=110, mask=00000001b, comment=ACOUSTICAL_LOCK_CONFIRM)

* **Change M Sport display cluster colors**
  * Group `3000`
    * `01` (start=133, mask=01000000b, comment=M_VEHICLE)

* **Adjust high-beam assistant in iDrive**
  * Group `3000`
    * `01` (start=109, mask=10000000b, comment=HIGH_BEAM_ASSISTANT)

* **Show currently playing album art in iDrive**
  * Group `3000`
    * `01` (start=9, mask=00000100b, comment=ENT_BTAS_IAP_COVERART)
  * Group `3003`
    * `01` (start=19, mask=00000100b, comment=ENT_BTAS_METADATA)
    * `01` (start=19, mask=00001000b, comment=ENT_BTAS_BROWSING)

* **Unlock DVD region code**
  * Group `3000`
    * `alle_anderen` (start=7, mask=11111111b, comment=ENT_VIDEO_DVD_AREA_CODE)

* **Show turn signals in HUD**
  * Group `3001`
    * `01` (start=55, mask=10000000b, comment=HUD_TURNSIGNAL)

* **Set sound system to Bang & Olufsen**
  * Group `3000`
    * `keine_insz` (start=21, mask=01100000b, comment=HIGH_END_AUDIO_B_UND_W)

* **Enable Logic7 (S667A HiFi vehicles)**
  * Group `3000`
    * `01` (start=22, mask=00001000b, comment=LOGIC7_SYMBOL)

* **Enhance audio mid-bass**
  * Group `3002`
    * `highpremium` (start=29, mask=00111100b, comment=AUDIO_SYSTEM)
    * `variant3` (start=21, mask=00000011b, comment=AUDIO_SYSTEM_VAR)

### ICMQL (CAFD 0000067B) — authored by Bundang Thunder 5 Series | Series: F06,F10,F11,F12,F13,F18

* **Default to Eco mode at start                                                                              --** by Bundang Thunder ^^**
  * Group `3000`
    * `verbaut` (start=36, mask=00001000b, comment=IcmKod_B_InitEco)

* **Enable cruise control**
  * Group `3000`
    * `01` (start=128, mask=00001110b, comment=C_Fahrfunktion)

* **Enable cruise control**
  * Group `3000`
    * `04` (start=128, mask=00001110b, comment=C_Fahrfunktion)

* **Enable Sport+ mode**
  * Group `3000`
    * `verbaut` (start=18, mask=11111111b, comment=IcmKod_B_S2TBA)

* **Configure standard Sport mode to disable DCS**
  * Group `3000`
    * `verbaut` (start=19, mask=11111111b, comment=IcmKod_B_S205A)

### IHKA_CBF (CAFD 00000092) — authored by Bundang Thunder 5 Series | Series: F06,F10,F11,F12,F13,F18

* **Remember last air conditioning state                                                                               --** by Bundang Thunder ^^**
  * Group `3000`
    * `01` (start=5, mask=00010000b, comment=OFF_MEMORY)

* **Prevent AUTO button from turning on A/C**
  * Group `3000`
    * `01` (start=5, mask=00001000b, comment=AC_NICHT_EIN_BEI_AUTO)

* **Remember HVAC recirculation mode**
  * Group `3000`
    * `01` (start=0, mask=00000100b, comment=MEMORY_UMLUFT)

### JBBFE (CAFD 00000014) — authored by Bundang Thunder 5 Series | Series: F06,F10,F11,F12,F13,F18

* **Allow rear windows to keep closing with door open --** by Bundang Thunder ^^**
  * Group `3070`
    * `00` (start=0, mask=00000100b, comment=FH_TUERAUF_STOP_MAUT)

* **Disable headlight washer**
  * Group `3000`
    * `00` (start=8, mask=00000001b, comment=SCHEINWERFERREINIGUNG)

### KAFAS2 (CAFD 00001148) — authored by Bundang Thunder 5 Series | Series: F06,F10,F11,F12,F13,F18

* **Automatic high-beam assistant                                                                                --** by Bundang Thunder ^^**
  * Group `3050`
    * `FLA_on` (start=1, mask=00000001b, comment=FLA_ON_OFF)
    * `CN` (start=6, mask=11111111b, comment=SPEED_SWITCHING_HIGH_BEAMS_ON)
    * `China` (start=7, mask=11111111b, comment=SPEED_SWITCHING_HIGH_BEAMS_OFF)

### KOMBI FPK_I12 (CAFD 00001060) — authored by Bundang Thunder 5 Series | Series: F06,F10,F11,F12,F13,F18

* **Show phone, entertainment, and voice prompts in HUD                                                               --** by Bundang Thunder ^^**
  * Group `3003`
    * `01` (start=10, mask=00000001b, comment=HUD_ENTERTAINMENT_ENABLE)
    * `01` (start=9, mask=00100000b, comment=HUD_STARTUP_ENABLE)
  * Group `3000`
    * `01` (start=41, mask=00000001b, comment=HUD_TLC_ENABLE)
    * `01` (start=40, mask=10000000b, comment=HUD_VZA_ENABLE)

* **Show turn signals in HUD**
  * Group `3003`
    * `01` (start=11, mask=00000001b, comment=HUD_BLINKER_ENABLE)
  * Group `3008`
    * `01` (start=5, mask=00000001b, comment=HUD_PIA_BLINKER)

* **Show M Performance logo in instrument cluster**
  * Group `3003`
    * `01` (start=3, mask=00000010b, comment=MPM_ENABLE)
  * Group `3000`
    * `bmw` (start=44, mask=11110000b, comment=MPM_LOGO)
    * `mpm` (start=44, mask=00001111b, comment=BMW_LOGO)

* **Show 550d logo in instrument cluster**
  * Group `3003`
    * `01` (start=3, mask=00000010b, comment=MPM_ENABLE)
  * Group `3000`
    * `mpm` (start=44, mask=11110000b, comment=MPM_LOGO)
    * `mpm` (start=44, mask=00001111b, comment=BMW_LOGO)

* **Show compass in instrument cluster**
  * Group `3003`
    * `01` (start=12, mask=00010000b, comment=KOMPASS_GRAPH_ENABLE)

* **Disable warning chime below 3 degrees**
  * Group `3000`
    * `00` (start=50, mask=00000001b, comment=CC_TEMPERATURWARNUNG)

* **Show power output in instrument cluster**
  * Group `3003`
    * `01` (start=11, mask=00000010b, comment=MOTORLEISTUNG_ENABLE)

* **Enable Sport+ menu in cluster**
  * Group `300C`
    * `menue_3` (start=0, mask=00001111b, comment=FDS_MENUE_TEXT_1)
    * `menue_3` (start=0, mask=11110000b, comment=FDS_MENUE_SIGNAL_1)
    * `menue_3` (start=1, mask=00001111b, comment=FDS_MENUE_TEXT_2)
    * `menue_3` (start=1, mask=11110000b, comment=FDS_MENUE_SIGNAL_2)
    * `menue_3` (start=2, mask=00001111b, comment=FDS_MENUE_TEXT_3)
    * `menue_3` (start=2, mask=11110000b, comment=FDS_MENUE_SIGNAL_3)
    * `menue_3` (start=3, mask=00001111b, comment=FDS_MENUE_TEXT_4)
    * `menue_3` (start=3, mask=11110000b, comment=FDS_MENUE_SIGNAL_4)
    * `menue_3` (start=51, mask=11111111b, comment=FDS_MENUE)

### KOMBI L6 BO (CAFD 00000069) — authored by Bundang Thunder 5 Series | Series: F06,F10,F11,F12,F13,F18

* **Show phone, entertainment, and voice prompts in HUD                                                               --** by Bundang Thunder ^^**
  * Group `3000`
    * `01` (start=41, mask=00001000b, comment=HUD_ENTERTAINMENT_ENABLE)
    * `01` (start=40, mask=10000000b, comment=HUD_VZA_ENABLE)
    * `01` (start=41, mask=00000001b, comment=HUD_TLC_ENABLE)
  * Group `3003`
    * `01` (start=9, mask=00100000b, comment=HUD_STARTUP_ENABLE)

* **Show turn signals in HUD**
  * Group `3000`
    * `01` (start=42, mask=00100000b, comment=BLINKER_HUD_ENABLE)
  * Group `3008`
    * `01` (start=5, mask=00000001b, comment=HUD_PIA_BLINKER)

* **Disable warning chime below 3 degrees**
  * Group `3000`
    * `00` (start=42, mask=00000100b, comment=CC_TEMPERATURWARNUNG)

* **Enable Sport+ menu in cluster**
  * Group `300C`
    * `menue_3` (start=0, mask=00001111b, comment=FDS_MENUE_TEXT_1)
    * `menue_3` (start=0, mask=11110000b, comment=FDS_MENUE_SIGNAL_1)
    * `menue_3` (start=1, mask=00001111b, comment=FDS_MENUE_TEXT_2)
    * `menue_3` (start=1, mask=11110000b, comment=FDS_MENUE_SIGNAL_2)
    * `menue_3` (start=2, mask=00001111b, comment=FDS_MENUE_TEXT_3)
    * `menue_3` (start=2, mask=11110000b, comment=FDS_MENUE_SIGNAL_3)
    * `menue_3` (start=3, mask=00001111b, comment=FDS_MENUE_TEXT_4)
    * `menue_3` (start=3, mask=11110000b, comment=FDS_MENUE_SIGNAL_4)

* **Instrument cluster daytime lower color: gray**
  * Group `3000`
    * `01` (start=41, mask=00000010b, comment=HINTERGRUND_FARBE_TAG)

* **Instrument cluster daytime lower color: orange**
  * Group `3000`
    * `00` (start=41, mask=00000010b, comment=HINTERGRUND_FARBE_TAG)

* **Instrument cluster nighttime lower color: gray**
  * Group `3000`
    * `01` (start=41, mask=00000100b, comment=HINTERGRUND_FARBE_NACHT)

* **Instrument cluster nighttime lower color: orange**
  * Group `3000`
    * `00` (start=41, mask=00000100b, comment=HINTERGRUND_FARBE_NACHT)

### JBBF_E3_PDC (CAFD 00000018) — authored by Bundang Thunder 5 Series | Series: F06,F10,F11,F12,F13,F18

* **Allow around view to turn on at any time --** by Bundang Thunder ^^**
  * Group `3009`
    * `FF` (start=15, mask=11111111b, comment=V_SCHWELLE_1)
    * `FF` (start=16, mask=11111111b, comment=V_SCHWELLE_2)
    * `FF` (start=17, mask=11111111b, comment=D_SCHWELLE_1)
    * `FF` (start=18, mask=11111111b, comment=D_SCHWELLE_2)

### ? (CAFD ) — authored by unknown | Series: F06,F10,F11,F12,F13,F18

* **Enable Easy Access                                                                         --** by Bundang Thunder ^^**
  * Group `3000`
    * `Modus_FA_SLV` (start=0, mask=00011100b, comment=EINAUSSTIEGSHILFE)

* **Easy Access seat starts moving from end position**
  * Group `3012`
    * `00, 01` (start=4, end=5, mask=11111111b, comment=EAH_SCHUTZFREIRAUM_HINTEN_SLV_PHYS)

* **Easy Access seat starts moving with 1 cm remaining**
  * Group `3012`
    * `00, 0A` (start=4, end=5, mask=11111111b, comment=EAH_SCHUTZFREIRAUM_HINTEN_SLV_PHYS)

* **Easy Access seat starts moving with 2 cm remaining**
  * Group `3012`
    * `00, 14` (start=4, end=5, mask=11111111b, comment=EAH_SCHUTZFREIRAUM_HINTEN_SLV_PHYS)

* **Easy Access seat starts moving with 3 cm remaining**
  * Group `3012`
    * `00, 1E` (start=4, end=5, mask=11111111b, comment=EAH_SCHUTZFREIRAUM_HINTEN_SLV_PHYS)

* **Easy Access seat travel distance: 4 cm**
  * Group `3012`
    * `00, 28` (start=0, end=1, mask=11111111b, comment=EAH_VERFAHRWEG_SLV_PHYS)

* **Easy Access seat travel distance: 5 cm**
  * Group `3012`
    * `00, 32` (start=0, end=1, mask=11111111b, comment=EAH_VERFAHRWEG_SLV_PHYS)

* **Easy Access seat travel distance: 6 cm**
  * Group `3012`
    * `00, 3C` (start=0, end=1, mask=11111111b, comment=EAH_VERFAHRWEG_SLV_PHYS)

* **Easy Access seat travel distance: 7 cm**
  * Group `3012`
    * `00, 46` (start=0, end=1, mask=11111111b, comment=EAH_VERFAHRWEG_SLV_PHYS)

* **Gentleman**
  * Group `3000`
    * `01` (start=1, mask=00000001b, comment=GENTLEMAN)
    * `01` (start=0, mask=00000001b, comment=MEMORY)

* **Set gong when saving seat position**
  * Group `3000`
    * `01` (start=2, mask=00001000b, comment=MEMORY_GONG)

### CBFS_PLX_1 (CAFD 000000B6) — authored by Bundang Thunder 5 Series | Series: F06,F10,F11,F12,F13,F18

* **Passenger seat Gentleman                                                                                         --** by Bundang Thunder ^^**
  * Group `3000`
    * `01` (start=1, mask=00000001b, comment=GENTLEMAN)
    * `01` (start=0, mask=00000001b, comment=MEMORY)

### SZL_LWS_03 (CAFD 0000033D) — authored by Bundang Thunder 5 Series | Series: F06,F10,F11,F12,F13,F18

* **Enable paddle shifters --** by Bundang Thunder ^^**
  * Group `3000`
    * `01` (start=2, mask=00000001b, comment=Lenkrad_Schaltpaddles)

* **Enable paddle shifters**
  * Group `3000`
    * `01` (start=0, mask=00000100b, comment=Lenkrad_Schaltpaddles)

### TRSVC (CAFD 00000223) — authored by Bundang Thunder 5 Series | Series: F06,F10,F11,F12,F13,F18

* **Allow side view at any time                                                                   --** by Bundang Thunder ^^**
  * Group `3000`
    * `FF` (start=114, mask=11111111b, comment=SV_Activate_Speed_Limit)
    * `FF` (start=115, mask=11111111b, comment=SV_Deactivate_Speed)

### ACSM_4B (CAFD 00000911) — authored by Bundang Thunder 3GT | Series: F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

* **Seat belt warning chime for only 5 seconds                                                                                 --** by Bundang Thunder ^^**
  * Group `3001`
    * `05` (start=3, mask=11111111b, comment=GWF_SBR_WARNDAUER)

* **Delete driver seat belt warning light**
  * Group `3000`
    * `00` (start=16, mask=00000001b, comment=SBR_PreWarning_Fahrer)

* **Delete passenger seat belt warning light**
  * Group `3000`
    * `00` (start=16, mask=00000010b, comment=SBR_PreWarning_Beifahrer)

* **Disable driver seat belt warning chime**
  * Group `3000`
    * `00` (start=15, mask=00000010b, comment=SeatBeltReminder_SBR_Fahrer)

* **Disable passenger seat belt warning chime**
  * Group `3000`
    * `00` (start=15, mask=00000100b, comment=SeatBeltReminder_SBR_Beifahrer)

### DSC_CT01 (CAFD 000019CC) — authored by Bundang Thunder 3GT | Series: F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

* **Enable launch control (also enables EGS)                                                                     --** by Bundang Thunder ^^**
  * Group `3000`
    * `01` (start=26, mask=00010000b, comment=C_Funktion_LaunchControl)

### GKEB23 (CAFD 0000023F) — authored by Bundang Thunder 3GT | Series: F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

* **Enable launch control (also enables DSC)                                                                     --** by Bundang Thunder ^^**
  * Group `3000`
    * `01` (start=1, mask=10000000b, comment=LC)

* **Show gear number in Dynamic Sport mode**
  * Group `3000`
    * `01` (start=1, mask=00000001b, comment=Sportschalter)
    * `01` (start=0, mask=01000000b, comment=Sportschalter_alt)

### FEM_01 (CAFD 00000794) — authored by Bundang Thunder 3GT | Series: F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

* **Activate hazard lights during hard braking                                                                                   --** by Bundang Thunder ^^**
  * Group `3060`
    * `01` (start=26, mask=00000001b, comment=WB_GB_ENABLE)

* **Set auto start/stop off by default**
  * Group `3023`
    * `01` (start=0, mask=00010000b, comment=TCM_MSA_DEFAULT_OFF)

* **Remember last auto start/stop state**
  * Group `3023`
    * `01` (start=0, mask=00100000b, comment=TCM_MSA_MEMORY)

* **Turn off audio when engine stops**
  * Group `3020`
    * `01` (start=1, mask=00000001b, comment=TCM_LOGIC_R_OFF_DOOR)

* **Double horn when locking with engine running - enable**
  * Group `3040`
    * `01` (start=1, mask=00100000b, comment=CLM_HORN_AT_SECURE)

* **Double horn when locking with engine running - disable**
  * Group `3040`
    * `00` (start=1, mask=00100000b, comment=CLM_HORN_AT_SECURE)

* **Fold mirrors immediately when locking (lock folding)**
  * Group `3053`
    * `00` (start=9, mask=11111111b, comment=KOMFORT_SCHLIESSEN)

* **Start engine without pressing brake**
  * Group `3020`
    * `00` (start=0, mask=00000001b, comment=TCM_STARTLOCK_BRAKE)

* **Start engine without pressing clutch**
  * Group `3020`
    * `00` (start=0, mask=00000100b, comment=TCM_STARTLOCK_CLUTCH)

* **Allow engine start in park**
  * Group `3020`
    * `00` (start=0, mask=00000010b, comment=TCM_STARTLOCK_PARK)
    * `00` (start=1, mask=00010000b, comment=TCM_STARTLOCK_DRIVINGREADINESS)

* **One-touch turn signal flashes five times**
  * Group `3060`
    * `04` (start=7, mask=00000111b, comment=BLINKZYKLEN_ANZAHL_TIPP)

* **Welcome fog lights (hard on)**
  * Group `3063`
    * `hard_On` (start=55, mask=11000000b, comment=MAPPING_NEBELSCHW_L_PART_OF_WL)
    * `hard_On` (start=66, mask=11000000b, comment=MAPPING_NEBELSCHW_R_PART_OF_WL)

* **Welcome fog lights (soft on)**
  * Group `3063`
    * `soft_On` (start=55, mask=11000000b, comment=MAPPING_NEBELSCHW_L_PART_OF_WL)
    * `soft_On` (start=66, mask=11000000b, comment=MAPPING_NEBELSCHW_R_PART_OF_WL)

* **Cornering fog lights**
  * Group `3073`
    * `01` (start=218, mask=00000010b, comment=C_CLC_ENA)
    * `01` (start=66, mask=00000001b, comment=C_BLC_ENA)
  * Group `3066`
    * `01` (start=0, mask=00000001b, comment=KL_ENABLE_LI)
    * `01` (start=80, mask=00000001b, comment=KL_ENABLE_RE)
  * Group `3062`
    * `0B` (start=110, mask=00111111b, comment=MAPPING_ABBIEGEL_L_OUTPUT)
    * `0C` (start=121, mask=00111111b, comment=MAPPING_ABBIEGEL_R_OUTPUT)

* **Turn on catch lights when reversing**
  * Group `3070`
    * `01` (start=11, mask=00010000b, comment=OVT_BEI_RUECKFAHRLICHT)

* **Unlock doors automatically when engine off**
  * Group `3040`
    * `01` (start=1, mask=00000010b, comment=CLM_UNLOCK_KL15OFF_AFTER_PIA_AUTO_LOCK)

* **Enable paddle shifter operation**
  * Group `3190`
    * `01` (start=0, mask=00000001b, comment=PADDLES_VERBAUT)

* **Allow windows to keep closing with door open**
  * Group `3050`
    * `00` (start=0, mask=00000001b, comment=FH_TUERAUF_STOP_MAUT)

* **Limit passenger mirror tilt to 30 degrees in reverse**
  * Group `3110`
    * `1E` (start=2, mask=11111111b, comment=ASP_BORDSTEINAUTOMATIK_DELTA)

### HKFM (CAFD 0000157F) — authored by Bundang Thunder 3GT | Series: F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

* **Auto-close trunk (footwell switch + remote)                                                                   --** by Bundang Thunder ^^**
  * Group `3010`
    * `01` (start=0, mask=00001000b, comment=TASTER_FBD)
    * `01` (start=2, mask=00000100b, comment=SCH_TOEHKI)
    * `01` (start=2, mask=00001000b, comment=SCH_FBD)

* **Spoiler deployment speed: 70 km/h**
  * Group `3100`
    * `00, 46` (start=0, end=1, mask=11111111b, comment=V_ASP_OUT)

* **Spoiler deployment speed: 80 km/h**
  * Group `3100`
    * `00, 50` (start=0, end=1, mask=11111111b, comment=V_ASP_OUT)

* **Spoiler deployment speed: 90 km/h**
  * Group `3100`
    * `00, 5A` (start=0, end=1, mask=11111111b, comment=V_ASP_OUT)

* **Spoiler deployment speed: 100 km/h**
  * Group `3100`
    * `00, 64` (start=0, end=1, mask=11111111b, comment=V_ASP_OUT)

* **Spoiler retract speed: 80 km/h**
  * Group `3100`
    * `00, 50` (start=2, end=3, mask=11111111b, comment=V_ASP_IN)

* **Spoiler retract speed: 70 km/h**
  * Group `3100`
    * `00, 46` (start=2, end=3, mask=11111111b, comment=V_ASP_IN)

* **Spoiler retract speed: 60 km/h**
  * Group `3100`
    * `00, 3C` (start=2, end=3, mask=11111111b, comment=V_ASP_IN)

* **Spoiler retract speed: 50 km/h**
  * Group `3100`
    * `00, 32` (start=2, end=3, mask=11111111b, comment=V_ASP_IN)

### HU_NBT_EVO (CAFD 00001EF6) — authored by Bundang Thunder 3GT | Series: F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

* **Set time automatically                                                                                         --** by Bundang Thunder ^^**
  * Group `3000`
    * `navigation` (start=19, mask=00000110b, comment=SETTINGS_TIME_AUTOMATIC)
    * `01` (start=105, mask=00100000b, comment=CLOCK_CHANGE_AUTOMATIC)

* **Watch video/DMB/navigation while driving (up to 63 km/h)**
  * Group `3006`
    * `1F` (start=26, mask=11111111b, comment=SPEEDLOCK_X_KMH_MAX)
    * `3F` (start=25, mask=11111111b, comment=SPEEDLOCK_X_KMH_MIN)

* **Watch video/DMB/navigation while driving 2**
  * Group `3000`
    * `00` (start=5, mask=00010000b, comment=VIDEO_FRONT_LOCKED)
    * `00` (start=5, mask=00000100b, comment=VIDEO_HANDBRAKE)
    * `None` (start=2, mask=00000111b, comment=VIDEO_SPEEDLOCK_CONDITION)

* **Suppress all warning messages**
  * Group `3001`
    * `kein_ld` (start=58, mask=11111111b, comment=LEGAL_DISCLAIMER_TIME)
    * `kein_ld` (start=52, mask=11111111b, comment=MACRO_CAM_LEGALDISCLAIMER)

* **Enable trailer zoom menu when reversing**
  * Group `3001`
    * `01` (start=54, mask=00000001b, comment=MACRO_TRAILER_COUPLING)

* **Close windows when it rains**
  * Group `3000`
    * `01` (start=19, mask=00001000b, comment=REGEN_SCHLIESSEN)

* **X-Drive**
  * Group `3000`
    * `01` (start=5, mask=00000001b, comment=COMPASS)
    * `01` (start=15, mask=00000001b, comment=X_VIEW)
    * `trajectory1` (start=26, mask=00110000b, comment=X_VIEW_GRAPHIC_SLOP)
    * `trajectory1` (start=26, mask=11000000b, comment=X_VIEW_GRAPHIC_ROLL)
    * `01` (start=110, mask=00000010b, comment=MOMENTDISTRIBUTION_MENU)

* **Enable USB video playback 1/2**
  * Group `3000`
    * `01` (start=15, mask=00010000b, comment=ENT_CODEC_OGG)
    * `01` (start=15, mask=00100000b, comment=ENT_CODEC_XVID)
    * `01` (start=15, mask=01000000b, comment=ENT_CODEC_VCD)
    * `01` (start=13, mask=00000100b, comment=ENT_MC_VIDEO_SUPPORT)

* **Enable USB video playback 2/2**
  * Group `3003`
    * `both` (start=32, mask=00000110b, comment=API_USB_VIDEO)
    * `both` (start=32, mask=00011000b, comment=API_IPOD_VIDEO)

* **Change warning chime to Rolls-Royce sound**
  * Group `3002`
    * `rolls_royce` (start=26, mask=00111000b, comment=SOUND_SIGNAL_SET)

* **Configure Sport mode**
  * Group `3008`
    * `popup_and_config` (start=79, mask=11000000b, comment=MACRO_FDS)
  * Group `3009`
    * `01` (start=9, mask=00010000b, comment=EFF_DYN_SPORT_CID)
    * `01` (start=9, mask=00100000b, comment=EFF_DYN_SPORT_UNIT)

* **Startup animation**
  * Group `3001`
    * `animation` (start=62, mask=00000110b, comment=STARTUP_TYPE)
    * `variant_01` (start=62, mask=01111000b, comment=STARTUP_EMBLEM)

* **Volume adjustment bar**
  * Group `3002`
    * `01` (start=52, mask=01000000b, comment=VOLUME_POPUP_DISPLAY)
    * `01` (start=52, mask=10000000b, comment=VOLUME_POPUP_REJECTION)
    * `01` (start=53, mask=00000001b, comment=VOLUME_POPUP_EXCEPTION)

* **Show TPMC tire pressure temperature**
  * Group `3001`
    * `druck_und_temperatur` (start=66, mask=00001100b, comment=RDC_DRUCK_TEMP)

* **Output ringtone through speakers (iPhone only)**
  * Group `3003`
    * `01` (start=6, mask=10000000b, comment=INBAND_RINGING)

* **Lock/unlock confirmation chime (requires piezo buzzer sensor)**
  * Group `3000`
    * `01` (start=110, mask=00000001b, comment=ACOUSTICAL_LOCK_CONFIRM)

* **Change M Sport display cluster colors**
  * Group `3000`
    * `01` (start=33, mask=01000000b, comment=M_VEHICLE)

* **Adjust high-beam assistant in iDrive**
  * Group `3000`
    * `01` (start=109, mask=10000000b, comment=HIGH_BEAM_ASSISTANT)

* **Show currently playing album art in iDrive**
  * Group `3000`
    * `01` (start=9, mask=00000100b, comment=ENT_BTAS_IAP_COVERART)
  * Group `3003`
    * `01` (start=19, mask=00000100b, comment=ENT_BTAS_METADATA)
    * `01` (start=19, mask=00001000b, comment=ENT_BTAS_BROWSING)

* **Unlock DVD region code**
  * Group `3000`
    * `alle_anderen` (start=7, mask=11111111b, comment=ENT_VIDEO_DVD_AREA_CODE)

* **Show turn signals in HUD**
  * Group `300C`
    * `01` (start=0, mask=01000000b, comment=HUD_TURNSIGNAL)

* **Set sound system to Bang & Olufsen**
  * Group `3000`
    * `keine_insz` (start=21, mask=01100000b, comment=HIGH_END_AUDIO_B_UND_W)

* **Enable Logic7 (S667A HiFi vehicles)**
  * Group `3000`
    * `01` (start=22, mask=00001000b, comment=LOGIC7_SYMBOL)

* **Enhance audio mid-bass**
  * Group `3002`
    * `highpremium` (start=29, mask=00111100b, comment=AUDIO_SYSTEM)
    * `variant3` (start=21, mask=00000011b, comment=AUDIO_SYSTEM_VAR)

### ICMQL (CAFD 0000067B) — authored by Bundang Thunder 3GT | Series: F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

* **Default to Eco mode at start                                                                              --** by Bundang Thunder ^^**
  * Group `3000`
    * `verbaut` (start=36, mask=00001000b, comment=IcmKod_B_InitEco)

* **Enable cruise control**
  * Group `3000`
    * `01` (start=128, mask=00001110b, comment=C_Fahrfunktion)

* **Enable Sport+ mode**
  * Group `3000`
    * `verbaut` (start=18, mask=11111111b, comment=IcmKod_B_S2TBA)

### IHKA_VA02 (CAFD 000016EE) — authored by Bundang Thunder 3GT | Series: F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

* **Remember last air conditioning state                                                                               --** by Bundang Thunder ^^**
  * Group `3003`
    * `01` (start=0, mask=00000010b, comment=MEMORY_OFF)

* **Prevent AUTO button from turning on A/C**
  * Group `3003`
    * `00` (start=0, mask=00000100b, comment=AC_ON_WITH_AUTO)

* **Remember HVAC recirculation mode**
  * Group `3003`
    * `01` (start=0, mask=00000001b, comment=MEMORY_UMLUFT)

### Kafas2 (CAFD 00001148) — authored by Bundang Thunder 3GT | Series: F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

* **Automatic high-beam assistant                                                                                --** by Bundang Thunder ^^**
  * Group `3050`
    * `FLA_on` (start=1, mask=00000001b, comment=FLA_ON_OFF)
    * `CN` (start=6, mask=11111111b, comment=SPEED_SWITCHING_HIGH_BEAMS_ON)
    * `China` (start=7, mask=11111111b, comment=SPEED_SWITCHING_HIGH_BEAMS_OFF)

### KOMBI L7_MID (CAFD 000009C8) — authored by Bundang Thunder 3GT | Series: F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

* **Show phone, entertainment, and voice prompts in HUD                                                               --** by Bundang Thunder ^^**
  * Group `3003`
    * `01` (start=4, mask=00000001b, comment=HUD_ENTERTAINMENT_ENABLE)
    * `01` (start=5, mask=00000010b, comment=HUD_STARTUP_ENABLE)
  * Group `3000`
    * `01` (start=42, mask=00001000b, comment=HUD_VZA_ENABLE)

* **Show turn signals in HUD**
  * Group `3003`
    * `01` (start=4, mask=00000001b, comment=HUD_BLINKER_ENABLE)
  * Group `3008`
    * `01` (start=5, mask=00000001b, comment=HUD_PIA_BLINKER)

* **Show logo on instrument cluster**
  * Group `3003`
    * `01` (start=7, mask=00000010b, comment=MPM_ENABLE)
  * Group `3000`
    * `bmw` (start=43, mask=11110000b, comment=MPM_LOGO)
    * `01` (start=0, mask=00001111b, comment=BMW_LOGO)

* **Digital speed readout in cluster**
  * Group `3000`
    * `01` (start=1, mask=00000010b, comment=BC_DIGITAL_V)

* **Disable warning chime below 3 degrees**
  * Group `3000`
    * `00` (start=30, mask=00000001b, comment=CC_TEMPERATURWARNUNG)

* **Show auto start/stop status in cluster**
  * Group `3003`
    * `01` (start=6, mask=00001000b, comment=MSA_VERFUEGBARANZEIGE_ENABLE)

* **Use GPS time**
  * Group `3000`
    * `01` (start=1, mask=10000000b, comment=GPS_UHR)

* **Display gear number in Dynamic Sport mode**
  * Group `3000`
    * `01` (start=41, mask=00010000b, comment=SPA_SPORT_ENABLE)

* **Enable Sport+ menu in cluster**
  * Group `300C`
    * `menue_3` (start=0, mask=00001111b, comment=FDS_MENUE_TEXT_1)
    * `menue_3` (start=0, mask=11110000b, comment=FDS_MENUE_SIGNAL_1)
    * `menue_3` (start=1, mask=00001111b, comment=FDS_MENUE_TEXT_2)
    * `menue_3` (start=1, mask=11110000b, comment=FDS_MENUE_SIGNAL_2)
    * `menue_3` (start=2, mask=00001111b, comment=FDS_MENUE_TEXT_3)
    * `menue_3` (start=2, mask=11110000b, comment=FDS_MENUE_SIGNAL_3)
    * `menue_3` (start=3, mask=00001111b, comment=FDS_MENUE_TEXT_4)
    * `menue_3` (start=3, mask=11110000b, comment=FDS_MENUE_SIGNAL_4)
    * `menue_3` (start=54, mask=11111111b, comment=FDS_MENUE)

### CFAS_PLX_1 (CAFD 000000B5) — authored by Bundang Thunder 3GT | Series: F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

* **Enable Easy Access                                                                         --** by Bundang Thunder ^^**
  * Group `3000`
    * `Modus_FA_SLV` (start=0, mask=00011100b, comment=EINAUSSTIEGSHILFE)

* **Easy Access seat starts moving from end position**
  * Group `3012`
    * `00, 01` (start=4, end=5, mask=11111111b, comment=EAH_SCHUTZFREIRAUM_HINTEN_SLV_PHYS)

* **Easy Access seat starts moving with 1 cm remaining**
  * Group `3012`
    * `00, 0A` (start=4, end=5, mask=11111111b, comment=EAH_SCHUTZFREIRAUM_HINTEN_SLV_PHYS)

* **Easy Access seat starts moving with 2 cm remaining**
  * Group `3012`
    * `00, 14` (start=4, end=5, mask=11111111b, comment=EAH_SCHUTZFREIRAUM_HINTEN_SLV_PHYS)

* **Easy Access seat starts moving with 3 cm remaining**
  * Group `3012`
    * `00, 1E` (start=4, end=5, mask=11111111b, comment=EAH_SCHUTZFREIRAUM_HINTEN_SLV_PHYS)

* **Easy Access seat travel distance: 4 cm**
  * Group `3012`
    * `00, 28` (start=2, end=3, mask=11111111b, comment=EAH_VERFAHRWEG_SLV_PHYS)

* **Easy Access seat travel distance: 5 cm**
  * Group `3012`
    * `00, 32` (start=2, end=3, mask=11111111b, comment=EAH_VERFAHRWEG_SLV_PHYS)

* **Easy Access seat travel distance: 6 cm**
  * Group `3012`
    * `00, 3C` (start=2, end=3, mask=11111111b, comment=EAH_VERFAHRWEG_SLV_PHYS)

* **Easy Access seat travel distance: 7 cm**
  * Group `3012`
    * `00, 46` (start=2, end=3, mask=11111111b, comment=EAH_VERFAHRWEG_SLV_PHYS)

* **Gentleman**
  * Group `3000`
    * `01` (start=1, mask=00000001b, comment=GENTLEMAN)
    * `01` (start=0, mask=00000001b, comment=MEMORY)

* **Set gong when saving seat position**
  * Group `3000`
    * `01` (start=2, mask=00001000b, comment=MEMORY_GONG)

### CBFS_PLX_1 (CAFD 000000B6) — authored by Bundang Thunder 3GT | Series: F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

* **Gentleman                                                                                                --** by Bundang Thunder ^^**
  * Group `3000`
    * `01` (start=1, mask=00000001b, comment=GENTLEMAN)
    * `01` (start=0, mask=00000001b, comment=MEMORY)

### TRSVC (CAFD 00000223) — authored by Bundang Thunder 3GT | Series: F20,F21,F22,F23,F30,F31,F32,F33,F3,F34,F35,F36,F80,F82,F83

* **Allow side view at any time                                                                   --** by Bundang Thunder ^^**
  * Group `3000`
    * `FF` (start=114, mask=11111111b, comment=SV_Activate_Speed_Limit)
    * `FF` (start=115, mask=11111111b, comment=SV_Deactivate_Speed)

### ACSM_4C (CAFD 00000909) — authored by Bundang Thunder 5GT | Series: F01,F02,F03,F04,F07

* **Seat belt warning chime for only 5 seconds                                                                                 --** by Bundang Thunder ^^**
  * Group `3001`
    * `05` (start=3, mask=11111111b, comment=GWF_SBR_WARNDAUER)

* **Delete driver seat belt warning light**
  * Group `3000`
    * `00` (start=16, mask=00000001b, comment=SBR_PreWarning_Fahrer)

* **Delete passenger seat belt warning light**
  * Group `3000`
    * `00` (start=16, mask=00000010b, comment=SBR_PreWarning_Beifahrer)

* **Disable driver seat belt warning chime**
  * Group `3000`
    * `00` (start=15, mask=00000010b, comment=SeatBeltReminder_SBR_Fahrer)

* **Disable passenger seat belt warning chime**
  * Group `3000`
    * `00` (start=15, mask=00000100b, comment=SeatBeltReminder_SBR_Beifahrer)

### CAS_04 (CAFD 0000000F) — authored by Bundang Thunder 5GT | Series: F01,F02,F03,F04,F07

* **Turn off audio when engine stops                                                                                  --** by Bundang Thunder ^^**
  * Group `3000`
    * `01` (start=2, mask=00000001b, comment=TC_LOGIC_KLR_OFF_DOOR)

* **Unlock doors when engine turns off**
  * Group `3002`
    * `01` (start=1, mask=10000000b, comment=ER_KEYOUT_AUTOVR)

* **Double horn when locking with engine running - enable**
  * Group `3002`
    * `01` (start=0, mask=00100000b, comment=CLM_HORN_AT_SECURE)

* **Double horn when locking with engine running - disable**
  * Group `3002`
    * `00` (start=0, mask=00100000b, comment=CLM_HORN_AT_SECURE)

* **Set auto start/stop off by default**
  * Group `3000`
    * `01` (start=3, mask=00010000b, comment=TC_MSA_DEFAULT_OFF)

* **Remember last auto start/stop state**
  * Group `3000`
    * `01` (start=3, mask=00100000b, comment=TC_MSA_MEMORY)

* **Fold mirrors immediately when locking (lock folding)**
  * Group `3003`
    * `00` (start=12, mask=11111111b, comment=KMFRT_SCHLIESSEN)

* **Start engine without pressing brake**
  * Group `3000`
    * `00` (start=1, mask=00000001b, comment=TC_STARTLOCK_BRAKE)

* **Start engine without pressing clutch**
  * Group `3000`
    * `00` (start=1, mask=00000100b, comment=TC_STARTLOCK_CLUTCH)

* **Allow engine start in park**
  * Group `3000`
    * `00` (start=1, mask=00000010b, comment=TC_STARTLOCK_PARK)
    * `00` (start=1, mask=00010000b, comment=TC_STARTLOCK_DRIVINGREADINESS)

* **Sound horn with remote**
  * Group `3002`
    * `01` (start=1, mask=00000010b, comment=REMOTE_KEY_SPECIAL_FCT)

### DSC_Premium (CAFD 00000C18) — authored by Bundang Thunder 5GT | Series: F01,F02,F03,F04,F07

* **Release parking brake by pressing accelerator only --** by Bundang Thunder ^^**
  * Group `3000`
    * `01` (start=27, mask=00100000b, comment=Funktion_AutomaticDriveawayRelease_aktiv)

* **Enable launch control (also enables EGS)**
  * Group `3000`
    * `01` (start=31, mask=00001000b, comment=Funktion_LaunchControl_aktiv)

### GKEB23 (CAFD 0000023F) — authored by Bundang Thunder 5GT | Series: F01,F02,F03,F04,F07

* **Enable launch control (also enables DSC)                                                                     --** by Bundang Thunder ^^**
  * Group `3000`
    * `01` (start=1, mask=10000000b, comment=LC)

* **Show gear number in Dynamic Sport mode**
  * Group `3000`
    * `01` (start=1, mask=00000001b, comment=Sportschalter)
    * `01` (start=0, mask=01000000b, comment=Sportschalter_alt)

### FRM_03CT (CAFD 0000106D) — authored by Bundang Thunder 5GT | Series: F01,F02,F03,F04,F07

* **Activate hazard lights during hard braking                                                                                   --** by Bundang Thunder ^^**
  * Group `3050`
    * `01` (start=2, mask=10000000b, comment=WB_GB_ENABLE)

* **Turn on fog lights in welcome lighting**
  * Group `3050`
    * `soft_on_LED` (start=29, mask=00001100b, comment=WL_FUNKTION_NSW)

* **Turn on headlights in welcome lighting**
  * Group `3050`
    * `soft_on_LED` (start=30, mask=00001100b, comment=WL_FUNKTION_AL)

* **Automatic high-beam assistant**
  * Group `3050`
    * `automatisch` (start=20, mask=00100000b, comment=FLA_AUTO_AKTIV)
    * `01` (start=20, mask=00010000b, comment=FLA_VERBAUT)

* **Allow front windows to keep closing with door open**
  * Group `3030`
    * `00` (start=1, mask=00000100b, comment=FH_TUER_AUF_STOP_MAUT)

* **Limit passenger mirror tilt to 30 degrees in reverse**
  * Group `3020`
    * `1E` (start=1, mask=11111111b, comment=ASP_BORDSTEINAUTOMATIK_DELTA)

* **One-touch turn signal flashes five times**
  * Group `3050`
    * `04` (start=1, mask=00000111b, comment=BLINKZYKLEN_ANZAHL_TIPP)

### FZD__04 (CAFD 00000552) — authored by Bundang Thunder 5GT | Series: F01,F02,F03,F04,F07

* **Door open/close chime --** by Bundang Thunder ^^**
  * Group `3002`
    * `01` (start=4, mask=00001000b, comment=Akkustische Quittierung Schaerfen)
    * `01` (start=4, mask=00010000b, comment=Akkustische Quittierung Schaerfen mit Klappenbeachtung)
    * `01` (start=4, mask=00100000b, comment=Akkustische Quittierung Entschaerfen)
    * `01` (start=2, mask=00010000b, comment=Lautstaerke Akkustische Quittterung tageszeitabhaengig)

### HKFM (CAFD 000007C8) — authored by Bundang Thunder 5GT | Series: F01,F02,F03,F04,F07

* **Auto-close trunk (footwell switch + remote)                                                                   --** by Bundang Thunder ^^**
  * Group `3010`
    * `01` (start=0, mask=00001000b, comment=TASTER_FBD)
    * `01` (start=2, mask=00000100b, comment=SCH_TOEHKI)
    * `01` (start=2, mask=00001000b, comment=SCH_FBD)

### HU_NBT (CAFD 00000DED) — authored by Bundang Thunder 5GT | Series: F01,F02,F03,F04,F07

* **Set time automatically                                                                                         --** by Bundang Thunder ^^**
  * Group `3000`
    * `navigation` (start=19, mask=00000110b, comment=SETTINGS_TIME_AUTOMATIC)
    * `01` (start=105, mask=00100000b, comment=CLOCK_CHANGE_AUTOMATIC)

* **Watch video/DMB/navigation while driving**
  * Group `3000`
    * `FF` (start=72, mask=11111111b, comment=SPEEDLOCK_X_KMH_MAX)
    * `FF` (start=71, mask=11111111b, comment=SPEEDLOCK_X_KMH_MIN)
    * `00` (start=5, mask=00010000b, comment=VIDEO_FRONT_LOCKED)
    * `00` (start=5, mask=00000100b, comment=VIDEO_HANDBRAKE)
    * `None` (start=57, mask=00000111b, comment=VIDEO_SPEEDLOCK_CONDITION)

* **Suppress all warning messages**
  * Group `3001`
    * `kein_ld` (start=58, mask=11111111b, comment=LEGAL_DISCLAIMER_TIME)
    * `kein_ld` (start=52, mask=11111111b, comment=MACRO_CAM_LEGALDISCLAIMER)

* **Enable trailer zoom menu when reversing**
  * Group `3001`
    * `01` (start=54, mask=00000001b, comment=MACRO_TRAILER_COUPLING)

* **Close windows when it rains**
  * Group `3000`
    * `01` (start=19, mask=00001000b, comment=REGEN_SCHLIESSEN)

* **X-Drive**
  * Group `3000`
    * `01` (start=5, mask=00000001b, comment=COMPASS)
    * `01` (start=15, mask=00000001b, comment=X_VIEW)
    * `trajectory1` (start=26, mask=00110000b, comment=X_VIEW_GRAPHIC_SLOP)
    * `trajectory1` (start=26, mask=11000000b, comment=X_VIEW_GRAPHIC_ROLL)
    * `01` (start=110, mask=00000010b, comment=MOMENTDISTRIBUTION_MENU)

* **Enable USB video playback 1/2**
  * Group `3000`
    * `01` (start=15, mask=00010000b, comment=ENT_CODEC_OGG)
    * `01` (start=15, mask=00100000b, comment=ENT_CODEC_XVID)
    * `01` (start=15, mask=01000000b, comment=ENT_CODEC_VCD)
    * `01` (start=13, mask=00000100b, comment=ENT_MC_VIDEO_SUPPORT)

* **Enable USB video playback 2/2**
  * Group `3003`
    * `both` (start=33, mask=00000110b, comment=API_USB_VIDEO)
    * `both` (start=33, mask=00011000b, comment=API_IPOD_VIDEO)

* **Change warning chime to Rolls-Royce sound**
  * Group `3002`
    * `rolls_royce` (start=26, mask=00111000b, comment=SOUND_SIGNAL_SET)

* **Configure Sport mode**
  * Group `3001`
    * `popup_and_config` (start=55, mask=00011000b, comment=MACRO_FDS)
  * Group `3000`
    * `01` (start=101, mask=00010000b, comment=EFF_DYN_SPORT_CID)
    * `01` (start=107, mask=00000100b, comment=EFF_DYN_SPORT_UNIT)

* **Startup animation**
  * Group `3001`
    * `animation` (start=62, mask=00000110b, comment=STARTUP_TYPE)
    * `variant_01` (start=62, mask=01111000b, comment=STARTUP_EMBLEM)

* **Volume adjustment bar**
  * Group `3002`
    * `01` (start=52, mask=01000000b, comment=VOLUME_POPUP_DISPLAY)
    * `01` (start=52, mask=10000000b, comment=VOLUME_POPUP_REJECTION)
    * `01` (start=53, mask=00000001b, comment=VOLUME_POPUP_EXCEPTION)

* **Show TPMC tire pressure temperature**
  * Group `3001`
    * `druck_und_temperatur` (start=66, mask=00001100b, comment=RDC_DRUCK_TEMP)

* **Output ringtone through speakers (iPhone only)**
  * Group `3003`
    * `01` (start=6, mask=10000000b, comment=INBAND_RINGING)

* **Lock/unlock confirmation chime (requires piezo buzzer sensor)**
  * Group `3000`
    * `01` (start=110, mask=00000001b, comment=ACOUSTICAL_LOCK_CONFIRM)

* **Change M Sport display cluster colors**
  * Group `3000`
    * `01` (start=133, mask=01000000b, comment=M_VEHICLE)

* **Adjust high-beam assistant in iDrive**
  * Group `3000`
    * `01` (start=109, mask=10000000b, comment=HIGH_BEAM_ASSISTANT)

* **Show currently playing album art in iDrive**
  * Group `3000`
    * `01` (start=9, mask=00000100b, comment=ENT_BTAS_IAP_COVERART)
  * Group `3003`
    * `01` (start=19, mask=00000100b, comment=ENT_BTAS_METADATA)
    * `01` (start=19, mask=00001000b, comment=ENT_BTAS_BROWSING)

* **Unlock DVD region code**
  * Group `3000`
    * `alle_anderen` (start=7, mask=11111111b, comment=ENT_VIDEO_DVD_AREA_CODE)

* **Show turn signals in HUD**
  * Group `3001`
    * `01` (start=55, mask=10000000b, comment=HUD_TURNSIGNAL)

* **Set sound system to Bang & Olufsen**
  * Group `3000`
    * `keine_insz` (start=21, mask=01100000b, comment=HIGH_END_AUDIO_B_UND_W)

* **Enable Logic7 (S667A HiFi vehicles)**
  * Group `3000`
    * `01` (start=22, mask=00001000b, comment=LOGIC7_SYMBOL)

* **Enhance audio mid-bass**
  * Group `3002`
    * `highpremium` (start=29, mask=00111100b, comment=AUDIO_SYSTEM)
    * `variant3` (start=21, mask=00000011b, comment=AUDIO_SYSTEM_VAR)

### ICMQL (CAFD 0000067B) — authored by Bundang Thunder 5GT | Series: F01,F02,F03,F04,F07

* **Default to Eco mode at start                                                                              --** by Bundang Thunder ^^**
  * Group `3000`
    * `verbaut` (start=36, mask=00001000b, comment=IcmKod_B_InitEco)

* **Enable cruise control**
  * Group `3000`
    * `01` (start=128, mask=00001110b, comment=C_Fahrfunktion)

* **Enable cruise control**
  * Group `3000`
    * `04` (start=128, mask=00001110b, comment=C_Fahrfunktion)

* **Enable Sport+ mode**
  * Group `3000`
    * `verbaut` (start=18, mask=11111111b, comment=IcmKod_B_S2TBA)

* **Configure standard Sport mode to disable DCS**
  * Group `3000`
    * `verbaut` (start=19, mask=11111111b, comment=IcmKod_B_S205A)

### IHKA_CBF (CAFD 00000092) — authored by Bundang Thunder 5GT | Series: F01,F02,F03,F04,F07

* **Remember last air conditioning state                                                                               --** by Bundang Thunder ^^**
  * Group `3000`
    * `01` (start=5, mask=00010000b, comment=OFF_MEMORY)

* **Prevent AUTO button from turning on A/C**
  * Group `3000`
    * `01` (start=5, mask=00001000b, comment=AC_NICHT_EIN_BEI_AUTO)

* **Remember HVAC recirculation mode**
  * Group `3000`
    * `01` (start=0, mask=00000100b, comment=MEMORY_UMLUFT)

### JBBFE (CAFD 00000014) — authored by Bundang Thunder 5GT | Series: F01,F02,F03,F04,F07

* **Allow rear windows to keep closing with door open --** by Bundang Thunder ^^**
  * Group `3070`
    * `00` (start=0, mask=00000100b, comment=FH_TUERAUF_STOP_MAUT)

* **Disable headlight washer**
  * Group `3000`
    * `00` (start=8, mask=00000001b, comment=SCHEINWERFERREINIGUNG)

### Kafas2 (CAFD 00001148) — authored by Bundang Thunder 5GT | Series: F01,F02,F03,F04,F07

* **Automatic high-beam assistant                                                                                --** by Bundang Thunder ^^**
  * Group `3050`
    * `FLA_on` (start=1, mask=00000001b, comment=FLA_ON_OFF)
    * `CN` (start=6, mask=11111111b, comment=SPEED_SWITCHING_HIGH_BEAMS_ON)
    * `China` (start=7, mask=11111111b, comment=SPEED_SWITCHING_HIGH_BEAMS_OFF)

### KOMBI FPK_I12 (CAFD 00001060) — authored by Bundang Thunder 5GT | Series: F01,F02,F03,F04,F07

* **Show phone, entertainment, and voice prompts in HUD                                                               --** by Bundang Thunder ^^**
  * Group `3003`
    * `01` (start=10, mask=00000001b, comment=HUD_ENTERTAINMENT_ENABLE)
    * `01` (start=9, mask=00100000b, comment=HUD_STARTUP_ENABLE)
  * Group `3000`
    * `01` (start=41, mask=00000001b, comment=HUD_TLC_ENABLE)
    * `01` (start=40, mask=10000000b, comment=HUD_VZA_ENABLE)

* **Show turn signals in HUD**
  * Group `3003`
    * `01` (start=11, mask=00000001b, comment=HUD_BLINKER_ENABLE)
  * Group `3008`
    * `01` (start=5, mask=00000001b, comment=HUD_PIA_BLINKER)

* **Show logo on instrument cluster**
  * Group `3003`
    * `01` (start=3, mask=00000010b, comment=MPM_ENABLE)
  * Group `3000`
    * `bmw` (start=44, mask=11110000b, comment=MPM_LOGO)
    * `mpm` (start=44, mask=00001111b, comment=BMW_LOGO)

* **Show compass in instrument cluster**
  * Group `3003`
    * `01` (start=12, mask=00010000b, comment=KOMPASS_GRAPH_ENABLE)

* **Disable warning chime below 3 degrees**
  * Group `3000`
    * `00` (start=50, mask=00000001b, comment=CC_TEMPERATURWARNUNG)

* **Show power output in instrument cluster**
  * Group `3003`
    * `01` (start=11, mask=00000010b, comment=MOTORLEISTUNG_ENABLE)

* **Enable Sport+ menu in cluster**
  * Group `300C`
    * `menue_3` (start=0, mask=00001111b, comment=FDS_MENUE_TEXT_1)
    * `menue_3` (start=0, mask=11110000b, comment=FDS_MENUE_SIGNAL_1)
    * `menue_3` (start=1, mask=00001111b, comment=FDS_MENUE_TEXT_2)
    * `menue_3` (start=1, mask=11110000b, comment=FDS_MENUE_SIGNAL_2)
    * `menue_3` (start=2, mask=00001111b, comment=FDS_MENUE_TEXT_3)
    * `menue_3` (start=2, mask=11110000b, comment=FDS_MENUE_SIGNAL_3)
    * `menue_3` (start=3, mask=00001111b, comment=FDS_MENUE_TEXT_4)
    * `menue_3` (start=3, mask=11110000b, comment=FDS_MENUE_SIGNAL_4)
    * `menue_3` (start=51, mask=11111111b, comment=FDS_MENUE)

### KOMBI L6 BO (CAFD 00000069) — authored by Bundang Thunder 5GT | Series: F01,F02,F03,F04,F07

* **Show phone, entertainment, and voice prompts in HUD                                                               --** by Bundang Thunder ^^**
  * Group `3000`
    * `01` (start=41, mask=00001000b, comment=HUD_ENTERTAINMENT_ENABLE)
    * `01` (start=40, mask=10000000b, comment=HUD_VZA_ENABLE)
    * `01` (start=41, mask=00000001b, comment=HUD_TLC_ENABLE)
  * Group `3003`
    * `01` (start=9, mask=00100000b, comment=HUD_STARTUP_ENABLE)

* **Show turn signals in HUD**
  * Group `3000`
    * `01` (start=42, mask=00100000b, comment=BLINKER_HUD_ENABLE)
  * Group `3008`
    * `01` (start=5, mask=00000001b, comment=HUD_PIA_BLINKER)

* **Disable warning chime below 3 degrees**
  * Group `3000`
    * `00` (start=42, mask=00000100b, comment=CC_TEMPERATURWARNUNG)

* **Enable Sport+ menu in cluster**
  * Group `300C`
    * `menue_3` (start=0, mask=00001111b, comment=FDS_MENUE_TEXT_1)
    * `menue_3` (start=0, mask=11110000b, comment=FDS_MENUE_SIGNAL_1)
    * `menue_3` (start=1, mask=00001111b, comment=FDS_MENUE_TEXT_2)
    * `menue_3` (start=1, mask=11110000b, comment=FDS_MENUE_SIGNAL_2)
    * `menue_3` (start=2, mask=00001111b, comment=FDS_MENUE_TEXT_3)
    * `menue_3` (start=2, mask=11110000b, comment=FDS_MENUE_SIGNAL_3)
    * `menue_3` (start=3, mask=00001111b, comment=FDS_MENUE_TEXT_4)
    * `menue_3` (start=3, mask=11110000b, comment=FDS_MENUE_SIGNAL_4)

* **Instrument cluster daytime lower color: gray**
  * Group `3000`
    * `01` (start=41, mask=00000010b, comment=HINTERGRUND_FARBE_TAG)

* **Instrument cluster daytime lower color: orange**
  * Group `3000`
    * `00` (start=41, mask=00000010b, comment=HINTERGRUND_FARBE_TAG)

* **Instrument cluster nighttime lower color: gray**
  * Group `3000`
    * `01` (start=41, mask=00000100b, comment=HINTERGRUND_FARBE_NACHT)

* **Instrument cluster nighttime lower color: orange**
  * Group `3000`
    * `00` (start=41, mask=00000100b, comment=HINTERGRUND_FARBE_NACHT)

### JBBF_E3_PDC (CAFD 00000018) — authored by Bundang Thunder 5GT | Series: F01,F02,F03,F04,F07

* **Allow around view to turn on at any time --** by Bundang Thunder ^^**
  * Group `3009`
    * `FF` (start=15, mask=11111111b, comment=V_SCHWELLE_1)
    * `FF` (start=16, mask=11111111b, comment=V_SCHWELLE_2)
    * `FF` (start=17, mask=11111111b, comment=D_SCHWELLE_1)
    * `FF` (start=18, mask=11111111b, comment=D_SCHWELLE_2)

### CFAS_PLX_1 (CAFD 000000B5) — authored by Bundang Thunder 5GT | Series: F01,F02,F03,F04,F07

* **Enable Easy Access                                                                         --** by Bundang Thunder ^^**
  * Group `3000`
    * `Modus_FA_SLV` (start=0, mask=00011100b, comment=EINAUSSTIEGSHILFE)

* **Easy Access seat starts moving from end position**
  * Group `3012`
    * `00, 01` (start=4, end=5, mask=11111111b, comment=EAH_SCHUTZFREIRAUM_HINTEN_SLV_PHYS)

* **Easy Access seat starts moving with 1 cm remaining**
  * Group `3012`
    * `00, 0A` (start=4, end=5, mask=11111111b, comment=EAH_SCHUTZFREIRAUM_HINTEN_SLV_PHYS)

* **Easy Access seat starts moving with 2 cm remaining**
  * Group `3012`
    * `00, 14` (start=4, end=5, mask=11111111b, comment=EAH_SCHUTZFREIRAUM_HINTEN_SLV_PHYS)

* **Easy Access seat starts moving with 3 cm remaining**
  * Group `3012`
    * `00, 1E` (start=4, end=5, mask=11111111b, comment=EAH_SCHUTZFREIRAUM_HINTEN_SLV_PHYS)

* **Easy Access seat travel distance: 4 cm**
  * Group `3012`
    * `00, 28` (start=0, end=1, mask=11111111b, comment=EAH_VERFAHRWEG_SLV_PHYS)

* **Easy Access seat travel distance: 5 cm**
  * Group `3012`
    * `00, 32` (start=0, end=1, mask=11111111b, comment=EAH_VERFAHRWEG_SLV_PHYS)

* **Easy Access seat travel distance: 6 cm**
  * Group `3012`
    * `00, 3C` (start=0, end=1, mask=11111111b, comment=EAH_VERFAHRWEG_SLV_PHYS)

* **Easy Access seat travel distance: 7 cm**
  * Group `3012`
    * `00, 46` (start=0, end=1, mask=11111111b, comment=EAH_VERFAHRWEG_SLV_PHYS)

* **Gentleman**
  * Group `3000`
    * `01` (start=1, mask=00000001b, comment=GENTLEMAN)
    * `01` (start=0, mask=00000001b, comment=MEMORY)

* **Set gong when saving seat position**
  * Group `3000`
    * `01` (start=2, mask=00001000b, comment=MEMORY_GONG)

### CBFS_PLX_1 (CAFD 000000B6) — authored by Bundang Thunder 5GT | Series: F01,F02,F03,F04,F07

* **Passenger seat Gentleman                                                                                         --** by Bundang Thunder ^^**
  * Group `3000`
    * `01` (start=1, mask=00000001b, comment=GENTLEMAN)
    * `01` (start=0, mask=00000001b, comment=MEMORY)

### CFAS_PLX_1 (CAFD 000000B5) — authored by Bundang Thunder 5GT | Series: F01,F02,F03,F04,F07

* **Link Gentleman function to SM2                                                                                 --** by Bundang Thunder ^^**
  * Group `3000`
    * `01` (start=1, mask=00000001b, comment=GENTLEMAN)
    * `01` (start=0, mask=00000001b, comment=MEMORY)

### SZL_LWS_03 (CAFD 0000033D) — authored by Bundang Thunder 5GT | Series: F01,F02,F03,F04,F07

* **Enable paddle shifters --** by Bundang Thunder ^^**
  * Group `3000`
    * `01` (start=0, mask=00000100b, comment=Lenkrad_Schaltpaddles)

### TRSVC (CAFD 00000223) — authored by Bundang Thunder 5GT | Series: F01,F02,F03,F04,F07

* **Allow side view at any time                                                                   --** by Bundang Thunder ^^**
  * Group `3000`
    * `FF` (start=114, mask=11111111b, comment=SV_Activate_Speed_Limit)
    * `FF` (start=115, mask=11111111b, comment=SV_Deactivate_Speed)

### ACSM_4C (CAFD 00000909) — authored by Bundang Thunder X3 | Series: F15,F16,F25,F26,F48,F85,F86

* **Seat belt warning chime for only 5 seconds                                                                                 --** by Bundang Thunder ^^**
  * Group `3000`
    * `05` (start=3, mask=11111111b, comment=GWF_SBR_WARNDAUER)

* **Delete driver seat belt warning light**
  * Group `3000`
    * `00` (start=16, mask=00000001b, comment=SBR_PreWarning_Fahrer)

* **Delete passenger seat belt warning light**
  * Group `3000`
    * `00` (start=16, mask=00000010b, comment=SBR_PreWarning_Beifahrer)

* **Disable driver seat belt warning chime**
  * Group `3000`
    * `00` (start=15, mask=00000010b, comment=SeatBeltReminder_SBR_Fahrer)

* **Disable passenger seat belt warning chime**
  * Group `3000`
    * `00` (start=15, mask=00000100b, comment=SeatBeltReminder_SBR_Beifahrer)

### CAS_04 (CAFD 0000000F) — authored by Bundang Thunder X3 | Series: F15,F16,F25,F26,F48,F85,F86

* **Turn off audio automatically when engine stops                                                                             --** by Bundang Thunder ^^**
  * Group `30D0`
    * `01` (start=2, mask=111111!1b, comment=TC_LOGIC_KLR_OFF_DOOR)

* **Double horn when locking with engine running - enable**
  * Group `3002`
    * `01` (start=0, mask=00100000b, comment=CLM_HORN_AT_SECURE)

* **Double horn when locking with engine running - disable**
  * Group `3002`
    * `00` (start=0, mask=00100000b, comment=CLM_HORN_AT_SECURE)

* **Set auto start/stop off by default**
  * Group `3000`
    * `01` (start=3, mask=00010000b, comment=TC_MSA_DEFAULT_OFF)

* **Remember last auto start/stop state**
  * Group `3000`
    * `01` (start=3, mask=00100000b, comment=TC_MSA_MEMORY)

* **Fold mirrors immediately when locking (lock folding)**
  * Group `3003`
    * `00` (start=12, mask=11111111b, comment=KMFRT_SCHLIESSEN)

* **Change battery capacity to 90 Ah**
  * Group `3702`
    * `01` (start=0, mask=11111111b, comment=VCM_BATTERY_CLASS)

### DXC_CT01 (CAFD 00000629) — authored by Bundang Thunder X3 | Series: F15,F16,F25,F26,F48,F85,F86

* **Enable launch control (EGS coding also required)                                                                     --** by Bundang Thunder ^^**
  * Group `3000`
    * `01` (start=26, mask=10000001b, comment=C_Funktion_LaunchControl_aktiv_I)

### FRM__03CT (CAFD 0000106D) — authored by Bundang Thunder X3 | Series: F15,F16,F25,F26,F48,F85,F86

* **Welcome fog lights                                                                                            --** by Bundang Thunder ^^**
  * Group `3050`
    * `soft_on_LED` (start=30, mask=00001100b, comment=WL_FUNKTION_AL)

* **Activate hazard lights during hard braking flashing**
  * Group `3050`
    * `01` (start=2, mask=10000000b, comment=WB_GB_ENABLE)

* **Limit passenger mirror tilt to 30 degrees in reverse**
  * Group `3020`
    * `1E` (start=1, mask=11111111b, comment=ASP_BORDSTEINAUTOMATIK_DELTA)

* **VLD**
  * Group `3073`
    * `F015_ohne_AFS` (start=40, end=42, mask=11111111b, comment=LUT_FLC_FORWARDLIGHTING_Y)
    * `F015_enable` (start=152, mask=00000001b, comment=C_AFS_ENA)

* **Allow windows to keep closing with door open**
  * Group `3030`
    * `00` (start=1, mask=00000100b, comment=FH_TUER_AUF_STOP_MAUT)

* **Automatic high-beam assistant**
  * Group `3050`
    * `automatisch` (start=20, mask=00100000b, comment=FLA_AUTO_AKTIV)
    * `01` (start=20, mask=00010000b, comment=FLA_VERBAUT)

* **Turn on fog lights in welcome lighting**
  * Group `3050`
    * `soft_on_LED` (start=29, mask=00001100b, comment=WL_FUNKTION_NSW)

* **Turn on headlights in welcome lighting**
  * Group `3050`
    * `soft_on_LED` (start=30, mask=00001100b, comment=WL_FUNKTION_AL)

* **Activate hazard lights during hard braking**
  * Group `3050`
    * `02` (start=23, mask=01110000b, comment=ESS_ERSCHEINUNGSBILD)

* **One-touch turn signal flashes five times**
  * Group `3050`
    * `04` (start=1, mask=00000111b, comment=BLINKZYKLEN_ANZAHL_TIPP)

### HKFM (CAFD 000007C8) — authored by Bundang Thunder X3 | Series: F15,F16,F25,F26,F48,F85,F86

* **Auto-close trunk (footwell switch + remote)                                                                   --** by Bundang Thunder ^^**
  * Group `3010`
    * `01` (start=0, mask=00001000b, comment=TASTER_FBD)
    * `01` (start=2, mask=00000100b, comment=SCH_TOEHKI)
    * `01` (start=2, mask=00001000b, comment=SCH_FBD)

### HU_NBT_EVO (CAFD 00001EF6) — authored by Bundang Thunder X3 | Series: F15,F16,F25,F26,F48,F85,F86

* **Set time automatically                                                                                         --** by Bundang Thunder ^^**
  * Group `3000`
    * `navigation` (start=19, mask=00000110b, comment=SETTINGS_TIME_AUTOMATIC)
    * `01` (start=105, mask=00100000b, comment=CLOCK_CHANGE_AUTOMATIC)

* **Watch video/DMB/navigation while driving (up to 63 km/h)**
  * Group `3006`
    * `1F` (start=26, mask=11111111b, comment=SPEEDLOCK_X_KMH_MAX)
    * `3F` (start=25, mask=11111111b, comment=SPEEDLOCK_X_KMH_MIN)
  * Group `3000`
    * `00` (start=5, mask=00010000b, comment=VIDEO_FRONT_LOCKED)
    * `00` (start=5, mask=00000100b, comment=VIDEO_HANDBRAKE)
    * `None` (start=2, mask=00000111b, comment=VIDEO_SPEEDLOCK_CONDITION)

* **Suppress all warning messages**
  * Group `3001`
    * `kein_ld` (start=58, mask=11111111b, comment=LEGAL_DISCLAIMER_TIME)
    * `kein_ld` (start=52, mask=11111111b, comment=MACRO_CAM_LEGALDISCLAIMER)

* **Enable trailer zoom menu when reversing**
  * Group `3001`
    * `01` (start=54, mask=00000001b, comment=MACRO_TRAILER_COUPLING)

* **Close windows when it rains**
  * Group `3000`
    * `01` (start=19, mask=00001000b, comment=REGEN_SCHLIESSEN)

* **X-Drive**
  * Group `3000`
    * `01` (start=5, mask=00000001b, comment=COMPASS)
    * `01` (start=15, mask=00000001b, comment=X_VIEW)
    * `trajectory1` (start=26, mask=00110000b, comment=X_VIEW_GRAPHIC_SLOP)
    * `trajectory1` (start=26, mask=11000000b, comment=X_VIEW_GRAPHIC_ROLL)
    * `01` (start=110, mask=00000010b, comment=MOMENTDISTRIBUTION_MENU)

* **Enable USB video playback 1/2**
  * Group `3000`
    * `01` (start=15, mask=00010000b, comment=ENT_CODEC_OGG)
    * `01` (start=15, mask=00100000b, comment=ENT_CODEC_XVID)
    * `01` (start=15, mask=01000000b, comment=ENT_CODEC_VCD)
    * `01` (start=33, mask=00000100b, comment=ENT_MC_VIDEO_SUPPORT)

* **Enable USB video playback 2/2**
  * Group `3003`
    * `both` (start=32, mask=00000110b, comment=API_USB_VIDEO)
    * `both` (start=32, mask=00011000b, comment=API_IPOD_VIDEO)

* **Change warning chime to Rolls-Royce sound**
  * Group `3002`
    * `rolls_royce` (start=26, mask=00111000b, comment=SOUND_SIGNAL_SET)

* **Configure Sport mode**
  * Group `3008`
    * `popup_and_config` (start=79, mask=11000000b, comment=MACRO_FDS)
  * Group `3009`
    * `01` (start=9, mask=00010000b, comment=EFF_DYN_SPORT_CID)
    * `01` (start=9, mask=00100000b, comment=EFF_DYN_SPORT_UNIT)

* **Startup animation**
  * Group `3001`
    * `animation` (start=62, mask=00000110b, comment=STARTUP_TYPE)
    * `variant_01` (start=62, mask=01111000b, comment=STARTUP_EMBLEM)

* **Volume adjustment bar**
  * Group `3002`
    * `01` (start=52, mask=01000000b, comment=VOLUME_POPUP_DISPLAY)
    * `01` (start=52, mask=10000000b, comment=VOLUME_POPUP_REJECTION)
    * `01` (start=53, mask=00000001b, comment=VOLUME_POPUP_EXCEPTION)

* **Show currently playing album art in iDrive**
  * Group `3000`
    * `01` (start=9, mask=00000100b, comment=ENT_BTAS_IAP_COVERART)
  * Group `3003`
    * `01` (start=19, mask=00000100b, comment=ENT_BTAS_METADATA)
    * `01` (start=19, mask=00001000b, comment=ENT_BTAS_BROWSING)

* **Display Sport mode**
  * Group `3009`
    * `01` (start=9, mask=00010000b, comment=EFF_DYN_SPORT_CID)

* **Show phone, entertainment, and voice prompts in HUD**
  * Group `300C`
    * `01` (start=0, mask=00001000b, comment=HUD_ENTERTAINMENTLIST)
    * `01` (start=0, mask=10000000b, comment=HUD_VZA)

* **Show M logo in HUD**
  * Group `300C`
    * `01` (start=0, mask=00100000b, comment=HUD_M)

* **Show turn signals in HUD**
  * Group `300C`
    * `01` (start=0, mask=01000000b, comment=HUD_TURNSIGNAL)

* **Show TPMC tire pressure temperature**
  * Group `3001`
    * `druck_und_temperatur` (start=66, mask=00001100b, comment=RDC_DRUCK_TEMP)

* **Output ringtone through speakers (iPhone only)**
  * Group `3003`
    * `01` (start=6, mask=10000000b, comment=INBAND_RINGING)

* **Lock/unlock confirmation chime (requires piezo buzzer sensor)**
  * Group `3000`
    * `01` (start=110, mask=00000001b, comment=ACOUSTICAL_LOCK_CONFIRM)

* **Change M Sport display cluster colors**
  * Group `3000`
    * `01` (start=33, mask=01000000b, comment=M_VEHICLE)

* **Adjust high-beam assistant in iDrive**
  * Group `3000`
    * `01` (start=109, mask=10000000b, comment=HIGH_BEAM_ASSISTANT)

* **Unlock DVD region code**
  * Group `3000`
    * `alle_anderen` (start=7, mask=11111111b, comment=ENT_VIDEO_DVD_AREA_CODE)

* **Set sound system to Bang & Olufsen**
  * Group `3000`
    * `keine_insz` (start=21, mask=01100000b, comment=HIGH_END_AUDIO_B_UND_W)

* **Enable Logic7 (S667A HiFi vehicles)**
  * Group `3000`
    * `01` (start=22, mask=00001000b, comment=LOGIC7_SYMBOL)

* **Enhance audio mid-bass**
  * Group `3002`
    * `highpremium` (start=29, mask=00111100b, comment=AUDIO_SYSTEM)
    * `variant3` (start=21, mask=00000011b, comment=AUDIO_SYSTEM_VAR)

### ICMQL (CAFD 0000067B) — authored by Bundang Thunder X3 | Series: F15,F16,F25,F26,F48,F85,F86

* **Default to Eco mode at start                                                                              --** by Bundang Thunder ^^**
  * Group `3000`
    * `verbaut` (start=36, mask=00001000b, comment=IcmKod_B_InitEco)

* **Enable cruise control**
  * Group `3000`
    * `01` (start=128, mask=00001110b, comment=C_Fahrfunktion)

* **Enable Sport+ mode**
  * Group `3000`
    * `verbaut` (start=18, mask=11111111b, comment=IcmKod_B_S2TBA)

### IHKA_HIGH (CAFD 000006DE) — authored by Bundang Thunder X3 | Series: F15,F16,F25,F26,F48,F85,F86

* **Remember last air conditioning state                                                                               --** by Bundang Thunder ^^**
  * Group `3000`
    * `01` (start=0, mask=00000001b, comment=OFF_MEMORY)

* **Prevent AUTO button from turning on A/C**
  * Group `3000`
    * `01` (start=18, mask=00100000b, comment=AC_NICHT_EIN_BEI_UMLUFT)

* **Remember HVAC recirculation mode**
  * Group `3000`
    * `01` (start=0, mask=00000010b, comment=UMLUFT_MEMORY)

### JBBFE (CAFD 00000014) — authored by Bundang Thunder X3 | Series: F15,F16,F25,F26,F48,F85,F86

* **Allow rear windows to keep closing with door open                                                                --** by Bundang Thunder ^^**
  * Group `3070`
    * `00` (start=0, mask=00000100b, comment=FH_TUERAUF_STOP_MAUT)

* **Disable headlight washer**
  * Group `3000`
    * `00` (start=8, mask=00000001b, comment=SCHEINWERFERREINIGUNG)

### KAFAS2 (CAFD 00001148) — authored by Bundang Thunder X3 | Series: F15,F16,F25,F26,F48,F85,F86

* **High-beam assistant                                                                                     --** by Bundang Thunder ^^**
  * Group `3050`
    * `FLA_on` (start=1, mask=00000001b, comment=FLA_ON_OFF)
    * `CN` (start=6, mask=11111111b, comment=SPEED_SWITCHING_HIGH_BEAMS_ON)
    * `China` (start=7, mask=11111111b, comment=SPEED_SWITCHING_HIGH_BEAMS_OFF)

* **Lane departure warning**
  * Group `3020`
    * `detection_for_grass_edge_and_curb_stone` (start=2, mask=00000011b, comment=FLA_ON_OFF)

* **Show speed limit info using camera only**
  * Group `3010`
    * `camera_only` (start=1, mask=10000000b, comment=COD_CAM_ONLY)

### KOMBI L6 BO (CAFD 00000069) — authored by Bundang Thunder X3 | Series: F15,F16,F25,F26,F48,F85,F86

* **Show phone, entertainment, and voice prompts in HUD                                                               --** by Bundang Thunder ^^**
  * Group `3000`
    * `01` (start=41, mask=00001000b, comment=HUD_ENTERTAINMENT_ENABLE)
    * `01` (start=41, mask=00000001b, comment=HUD_TLC_ENABLE)
    * `01` (start=40, mask=10000000b, comment=HUD_VZA_ENABLE)

* **Show turn signals in HUD**
  * Group `3000`
    * `01` (start=42, mask=00100000b, comment=BLINKER_HUD_ENABLE)
  * Group `3008`
    * `01` (start=5, mask=00000001b, comment=HUD_PIA_BLINKER)

* **Show logo on instrument cluster**
  * Group `3003`
    * `01` (start=9, mask=00000001b, comment=MPM_ENABLE)
  * Group `3000`
    * `bmw` (start=53, mask=11110000b, comment=MPM_LOGO)
    * `mpm` (start=53, mask=00001111b, comment=BMW_LOGO)

* **Show compass in instrument cluster**
  * Group `3003`
    * `01` (start=9, mask=01000000b, comment=KOMPASS_GRAPH_ENABLE)

* **Disable warning chime below 3 degrees**
  * Group `3000`
    * `00` (start=42, mask=00000100b, comment=CC_TEMPERATURWARNUNG)

* **Enable Sport+ menu in cluster**
  * Group `300C`
    * `menue_3` (start=0, mask=00001111b, comment=FDS_MENUE_TEXT_1)
    * `menue_3` (start=0, mask=11110000b, comment=FDS_MENUE_SIGNAL_1)
    * `menue_3` (start=1, mask=00001111b, comment=FDS_MENUE_TEXT_2)
    * `menue_3` (start=1, mask=11110000b, comment=FDS_MENUE_SIGNAL_2)
    * `menue_3` (start=2, mask=00001111b, comment=FDS_MENUE_TEXT_3)
    * `menue_3` (start=2, mask=11110000b, comment=FDS_MENUE_SIGNAL_3)
    * `menue_3` (start=3, mask=00001111b, comment=FDS_MENUE_TEXT_4)
    * `menue_3` (start=3, mask=11110000b, comment=FDS_MENUE_SIGNAL_4)
  * Group `3007`
    * `menue_3` (start=35, mask=11111111b, comment=FDS_MENUE)

* **Instrument cluster daytime lower color: gray**
  * Group `3000`
    * `01` (start=41, mask=00000010b, comment=HINTERGRUND_FARBE_TAG)

* **Instrument cluster daytime lower color: orange**
  * Group `3000`
    * `00` (start=41, mask=00000010b, comment=HINTERGRUND_FARBE_TAG)

* **Instrument cluster nighttime lower color: gray**
  * Group `3000`
    * `01` (start=41, mask=00000100b, comment=HINTERGRUND_FARBE_NACHT)

* **Instrument cluster nighttime lower color: orange**
  * Group `3000`
    * `00` (start=41, mask=00000100b, comment=HINTERGRUND_FARBE_NACHT)

### CFAS_PLX_1 (CAFD 000000B5) — authored by Bundang Thunder X3 | Series: F15,F16,F25,F26,F48,F85,F86

* **Enable Easy Access                                                                         --** by Bundang Thunder ^^**
  * Group `3000`
    * `Modus_FA_SLV` (start=0, mask=00011100b, comment=EINAUSSTIEGSHILFE)

* **Easy Access seat starts moving from end position**
  * Group `3012`
    * `00, 01` (start=4, end=5, mask=11111111b, comment=EAH_SCHUTZFREIRAUM_HINTEN_SLV_PHYS)

* **Easy Access seat starts moving with 1 cm remaining**
  * Group `3012`
    * `00, 0A` (start=4, end=5, mask=11111111b, comment=EAH_SCHUTZFREIRAUM_HINTEN_SLV_PHYS)

* **Easy Access seat starts moving with 2 cm remaining**
  * Group `3012`
    * `00, 14` (start=4, end=5, mask=11111111b, comment=EAH_SCHUTZFREIRAUM_HINTEN_SLV_PHYS)

* **Easy Access seat starts moving with 3 cm remaining**
  * Group `3012`
    * `00, 1E` (start=4, end=5, mask=11111111b, comment=EAH_SCHUTZFREIRAUM_HINTEN_SLV_PHYS)

* **Easy Access seat travel distance: 4 cm**
  * Group `3012`
    * `00, 28` (start=0, end=1, mask=11111111b, comment=EAH_VERFAHRWEG_SLV_PHYS)

* **Easy Access seat travel distance: 5 cm**
  * Group `3012`
    * `00, 32` (start=0, end=1, mask=11111111b, comment=EAH_VERFAHRWEG_SLV_PHYS)

* **Easy Access seat travel distance: 6 cm**
  * Group `3012`
    * `00, 3C` (start=0, end=1, mask=11111111b, comment=EAH_VERFAHRWEG_SLV_PHYS)

* **Easy Access seat travel distance: 7 cm**
  * Group `3012`
    * `00, 46` (start=0, end=1, mask=11111111b, comment=EAH_VERFAHRWEG_SLV_PHYS)

* **Gentleman**
  * Group `3000`
    * `01` (start=1, mask=00000001b, comment=GENTLEMAN)
    * `01` (start=0, mask=00000001b, comment=MEMORY)

* **Set gong when saving seat position**
  * Group `3000`
    * `01` (start=2, mask=00001000b, comment=MEMORY_GONG)

### CBFS_PLX_1 (CAFD 000000B6) — authored by Bundang Thunder X3 | Series: F15,F16,F25,F26,F48,F85,F86

* **Passenger seat Gentleman                                                                                         --** by Bundang Thunder ^^**
  * Group `3000`
    * `01` (start=1, mask=00000001b, comment=GENTLEMAN)
    * `01` (start=0, mask=00000001b, comment=MEMORY)

### CFAS_PLX_1 (CAFD 000000B5) — authored by Bundang Thunder X3 | Series: F15,F16,F25,F26,F48,F85,F86

* **Link Gentleman function to SM2                                                                                 --** by Bundang Thunder ^^**
  * Group `3000`
    * `01` (start=1, mask=00000001b, comment=GENTLEMAN)
    * `01` (start=0, mask=00000001b, comment=MEMORY)

### ACSM_4C (CAFD 00000909) — authored by Bundang Thunder X5 | Series: F15,F16,F25,F26,F48,F85,F86

* **Seat belt warning chime for only 5 seconds                                                                                 --** by Bundang Thunder ^^**
  * Group `3000`
    * `05` (start=3, mask=11111111b, comment=GWF_SBR_WARNDAUER)

* **Delete driver seat belt warning light**
  * Group `3000`
    * `00` (start=16, mask=00000001b, comment=SBR_PreWarning_Fahrer)

* **Delete passenger seat belt warning light**
  * Group `3000`
    * `00` (start=16, mask=00000010b, comment=SBR_PreWarning_Beifahrer)

* **Disable driver seat belt warning chime**
  * Group `3000`
    * `00` (start=15, mask=00000010b, comment=SeatBeltReminder_SBR_Fahrer)

* **Disable passenger seat belt warning chime**
  * Group `3000`
    * `00` (start=15, mask=00000100b, comment=SeatBeltReminder_SBR_Beifahrer)

### BDC_01 (CAFD 000017BE) — authored by Bundang Thunder X5 | Series: F15,F16,F25,F26,F48,F85,F86

* **Activate hazard lights during hard braking                                                                                   --** by Bundang Thunder ^^**
  * Group `3068`
    * `01` (start=26, mask=00000001b, comment=WB_GB_ENABLE)

* **Limit passenger mirror tilt to 30 degrees in reverse**
  * Group `3110`
    * `1E` (start=1, mask=11111111b, comment=ASP_BORDSTEINAUTOMATIK_DELTA)

* **One-touch turn signal flashes five times**
  * Group `3069`
    * `Tippblinken_fuenfmal` (start=215, mask=00011000b, comment=PIA_DEFAULT_TIPPBLINKEN)

* **Enable welcome lights**
  * Group `3068`
    * `01` (start=13, mask=00100000b, comment=WL_WIEDERHOLSPERRE_01)

* **Enable follow me home**
  * Group `3068`
    * `01` (start=13, mask=01000000b, comment=FMH_WIEDERHOLSPERRE_01)

* **Close trunk immediately via remote**
  * Group `30D0`
    * `01` (start=18, mask=111111!1b, comment=RC_TIME_DELAY_BOOTLID)

* **Open and close windows with remote**
  * Group `3056`
    * `01` (start=0, mask=01000000b, comment=KOMFORTOEFFNUNG_FB)

* **Fold mirrors immediately when locking (lock folding)**
  * Group `3056`
    * `00` (start=10, mask=11111111b, comment=KOMFORT_SCHLIESSEN)

* **Allow windows to keep closing with doors open (front and rear)**
  * Group `3050`
    * `00` (start=0, mask=00000001b, comment=FH_TUERAUF_STOP_MAUT)
  * Group `3051`
    * `00` (start=0, mask=00000001b, comment=FH_TUERAUF_STOP_MAUT_REAR)

* **VLD**
  * Group `3073`
    * `F015_ohne_AFS` (start=40, end=42, mask=11111111b, comment=LUT_FLC_FORWARDLIGHTING_Y)
    * `F015_enable` (start=152, mask=00000001b, comment=C_AFS_ENA)

* **Turn on door handle lights when reversing**
  * Group `3070`
    * `F015_ohne_AFS` (start=128, mask=00000001b, comment=OVT_BEI_RUECKFAHRLICHT)

* **Disable auto start/stop in Comfort mode**
  * Group `3023`
    * `01` (start=0, mask=00010000b, comment=TCM_MSA_DEFAULT_OFF)

* **Disable auto start/stop in Eco Pro mode**
  * Group `3023`
    * `00` (start=1, mask=00001100b, comment=TCM_MSA_ECO_MODE)

* **Remember last auto start/stop state**
  * Group `3023`
    * `01` (start=0, mask=00100000b, comment=TCM_MSA_MEMORY)

* **Double horn when locking with engine running - enable**
  * Group `3040`
    * `01` (start=0, mask=00000100b, comment=VAM_HORN_AT_SECURE)

* **Double horn when locking with engine running - disable**
  * Group `3040`
    * `00` (start=0, mask=00000100b, comment=VAM_HORN_AT_SECURE)

### HKFM (CAFD 000007C8) — authored by Bundang Thunder X5 | Series: F15,F16,F25,F26,F48,F85,F86

* **Auto-close trunk (footwell switch + remote)                                                                   --** by Bundang Thunder ^^**
  * Group `3010`
    * `01` (start=0, mask=00001000b, comment=TASTER_FBD)
    * `01` (start=2, mask=00000100b, comment=SCH_TOEHKI)
    * `01` (start=2, mask=00001000b, comment=SCH_FBD)

### HU_NBT (CAFD 00000DED) — authored by Bundang Thunder X5 | Series: F15,F16,F25,F26,F48,F85,F86

* **Set time automatically                                                                                         --** by Bundang Thunder ^^**
  * Group `3000`
    * `navigation` (start=19, mask=00000110b, comment=SETTINGS_TIME_AUTOMATIC)
    * `01` (start=105, mask=00100000b, comment=CLOCK_CHANGE_AUTOMATIC)

* **Watch video/DMB/navigation while driving**
  * Group `3000`
    * `FF` (start=72, mask=11111111b, comment=SPEEDLOCK_X_KMH_MAX)
    * `FF` (start=71, mask=11111111b, comment=SPEEDLOCK_X_KMH_MIN)
    * `00` (start=5, mask=00010000b, comment=VIDEO_FRONT_LOCKED)
    * `00` (start=5, mask=00000100b, comment=VIDEO_HANDBRAKE)
    * `None` (start=57, mask=00000111b, comment=VIDEO_SPEEDLOCK_CONDITION)

* **Suppress all warning messages**
  * Group `3001`
    * `kein_ld` (start=58, mask=11111111b, comment=LEGAL_DISCLAIMER_TIME)
    * `kein_ld` (start=52, mask=11111111b, comment=MACRO_CAM_LEGALDISCLAIMER)

* **Enable trailer zoom menu when reversing**
  * Group `3001`
    * `01` (start=54, mask=00000001b, comment=MACRO_TRAILER_COUPLING)

* **Close windows when it rains**
  * Group `3000`
    * `01` (start=19, mask=00001000b, comment=REGEN_SCHLIESSEN)

* **X-Drive**
  * Group `3000`
    * `01` (start=5, mask=00000001b, comment=COMPASS)
    * `01` (start=15, mask=00000001b, comment=X_VIEW)
    * `trajectory1` (start=26, mask=00110000b, comment=X_VIEW_GRAPHIC_SLOP)
    * `trajectory1` (start=26, mask=11000000b, comment=X_VIEW_GRAPHIC_ROLL)
    * `01` (start=110, mask=00000010b, comment=MOMENTDISTRIBUTION_MENU)

* **Enable USB video playback 1/2**
  * Group `3000`
    * `01` (start=15, mask=00010000b, comment=ENT_CODEC_OGG)
    * `01` (start=15, mask=00100000b, comment=ENT_CODEC_XVID)
    * `01` (start=15, mask=01000000b, comment=ENT_CODEC_VCD)
    * `01` (start=13, mask=00000100b, comment=ENT_MC_VIDEO_SUPPORT)

* **Enable USB video playback 2/2**
  * Group `3003`
    * `both` (start=33, mask=00000110b, comment=API_USB_VIDEO)
    * `both` (start=33, mask=00011000b, comment=API_IPOD_VIDEO)

* **Change warning chime to Rolls-Royce sound**
  * Group `3002`
    * `rolls_royce` (start=26, mask=00111000b, comment=SOUND_SIGNAL_SET)

* **Configure Sport mode**
  * Group `3001`
    * `popup_and_config` (start=55, mask=00011000b, comment=MACRO_FDS)
  * Group `3000`
    * `01` (start=101, mask=00010000b, comment=EFF_DYN_SPORT_CID)
    * `01` (start=107, mask=00000100b, comment=EFF_DYN_SPORT_UNIT)

* **Startup animation**
  * Group `3001`
    * `animation` (start=62, mask=00000110b, comment=STARTUP_TYPE)
    * `variant_01` (start=62, mask=01111000b, comment=STARTUP_EMBLEM)

* **Volume adjustment bar**
  * Group `3002`
    * `01` (start=52, mask=01000000b, comment=VOLUME_POPUP_DISPLAY)
    * `01` (start=52, mask=10000000b, comment=VOLUME_POPUP_REJECTION)
    * `01` (start=53, mask=00000001b, comment=VOLUME_POPUP_EXCEPTION)

* **Show TPMC tire pressure temperature**
  * Group `3001`
    * `druck_und_temperatur` (start=66, mask=00001100b, comment=RDC_DRUCK_TEMP)

* **Output ringtone through speakers (iPhone only)**
  * Group `3003`
    * `01` (start=6, mask=10000000b, comment=INBAND_RINGING)

* **Lock/unlock confirmation chime (requires piezo buzzer sensor)**
  * Group `3000`
    * `01` (start=110, mask=00000001b, comment=ACOUSTICAL_LOCK_CONFIRM)

* **Change M Sport display cluster colors**
  * Group `3000`
    * `01` (start=133, mask=01000000b, comment=M_VEHICLE)

* **Adjust high-beam assistant in iDrive**
  * Group `3000`
    * `01` (start=109, mask=10000000b, comment=HIGH_BEAM_ASSISTANT)

* **Show currently playing album art in iDrive**
  * Group `3000`
    * `01` (start=9, mask=00000100b, comment=ENT_BTAS_IAP_COVERART)
  * Group `3003`
    * `01` (start=19, mask=00000100b, comment=ENT_BTAS_METADATA)
    * `01` (start=19, mask=00001000b, comment=ENT_BTAS_BROWSING)

* **Unlock DVD region code**
  * Group `3000`
    * `alle_anderen` (start=7, mask=11111111b, comment=ENT_VIDEO_DVD_AREA_CODE)

* **Show turn signals in HUD**
  * Group `3001`
    * `01` (start=55, mask=10000000b, comment=HUD_TURNSIGNAL)

* **Set sound system to Bang & Olufsen**
  * Group `3000`
    * `keine_insz` (start=21, mask=01100000b, comment=HIGH_END_AUDIO_B_UND_W)

* **Enable Logic7 (S667A HiFi vehicles)**
  * Group `3000`
    * `01` (start=22, mask=00001000b, comment=LOGIC7_SYMBOL)

* **Enhance audio mid-bass**
  * Group `3002`
    * `highpremium` (start=29, mask=00111100b, comment=AUDIO_SYSTEM)
    * `variant3` (start=21, mask=00000011b, comment=AUDIO_SYSTEM_VAR)

### ICMQL (CAFD 0000067B) — authored by Bundang Thunder X5 | Series: F15,F16,F25,F26,F48,F85,F86

* **Default to Eco mode at start                                                                              --** by Bundang Thunder ^^**
  * Group `3000`
    * `verbaut` (start=36, mask=00001000b, comment=IcmKod_B_InitEco)

* **Enable cruise control**
  * Group `3000`
    * `01` (start=128, mask=00001110b, comment=C_Fahrfunktion)

* **Enable cruise control**
  * Group `3000`
    * `04` (start=128, mask=00001110b, comment=C_Fahrfunktion)

* **Enable Sport+ mode**
  * Group `3000`
    * `verbaut` (start=18, mask=11111111b, comment=IcmKod_B_S2TBA)

* **ACC distance**
  * Group `3000`
    * `01` (start=184, mask=00000111b, comment=C_Abstandsstufe_init)

* **Adjust active blind spot activation speed by -20 km/h**
  * Group `3000`
    * `01` (start=190, mask=00111111b, comment=C_ZSW_01ierunggeschwindigkeit_Funktion_low)

* **Enable coasting mode**
  * Group `3000`
    * `01` (start=120, mask=11000000b, comment=C_Segeln_vorhanden)

### IHKA_CBF (CAFD 000047D6) — authored by Bundang Thunder X5 | Series: F15,F16,F25,F26,F48,F85,F86

* **Remember last air conditioning state                                                                               --** by Bundang Thunder ^^**
  * Group `3000`
    * `01` (start=5, mask=00010000b, comment=OFF_MEMORY)

* **Prevent AUTO button from turning on A/C**
  * Group `3000`
    * `01` (start=5, mask=00001000b, comment=AC_NICHT_EIN_BEI_AUTO)

* **Remember HVAC recirculation mode**
  * Group `3000`
    * `01` (start=0, mask=00000100b, comment=MEMORY_UMLUFT)

### JBBFE (CAFD 00000014) — authored by Bundang Thunder X5 | Series: F15,F16,F25,F26,F48,F85,F86

* **Disable headlight washer                                                                                --** by Bundang Thunder ^^**
  * Group `3000`
    * `00` (start=8, mask=00000001b, comment=SCHEINWERFERREINIGUNG)

### KAFAS2 (CAFD 00001148) — authored by Bundang Thunder X5 | Series: F15,F16,F25,F26,F48,F85,F86

* **Automatic high-beam assistant                                                                                --** by Bundang Thunder ^^**
  * Group `3050`
    * `FLA_on` (start=1, mask=00000001b, comment=FLA_ON_OFF)
    * `CN` (start=6, mask=11111111b, comment=SPEED_SWITCHING_HIGH_BEAMS_ON)
    * `China` (start=7, mask=11111111b, comment=SPEED_SWITCHING_HIGH_BEAMS_OFF)

### KOMBI FPK_I12 (CAFD 00001060) — authored by Bundang Thunder X5 | Series: F15,F16,F25,F26,F48,F85,F86

* **Show phone, entertainment, and voice prompts in HUD                                                               --** by Bundang Thunder ^^**
  * Group `3003`
    * `01` (start=10, mask=00000001b, comment=HUD_ENTERTAINMENT_ENABLE)
    * `01` (start=9, mask=00100000b, comment=HUD_STARTUP_ENABLE)
  * Group `3000`
    * `01` (start=41, mask=00000001b, comment=HUD_TLC_ENABLE)
    * `01` (start=40, mask=10000000b, comment=HUD_VZA_ENABLE)

* **Show turn signals in HUD**
  * Group `3003`
    * `01` (start=11, mask=00000001b, comment=HUD_BLINKER_ENABLE)
  * Group `3008`
    * `01` (start=5, mask=00000001b, comment=HUD_PIA_BLINKER)

* **Show logo on instrument cluster**
  * Group `3003`
    * `01` (start=3, mask=00000010b, comment=MPM_ENABLE)
  * Group `3000`
    * `mpm_x5` (start=44, mask=11110000b, comment=MPM_LOGO)
    * `mpm_x5` (start=44, mask=00001111b, comment=BMW_LOGO)

* **Show compass in instrument cluster**
  * Group `3003`
    * `01` (start=12, mask=00010000b, comment=KOMPASS_GRAPH_ENABLE)

* **Disable warning chime below 3 degrees**
  * Group `3000`
    * `00` (start=50, mask=00000001b, comment=CC_TEMPERATURWARNUNG)

* **Show power output in instrument cluster**
  * Group `3003`
    * `01` (start=11, mask=00000010b, comment=MOTORLEISTUNG_ENABLE)

* **Enable Sport+ menu in cluster**
  * Group `300C`
    * `menue_3` (start=0, mask=00001111b, comment=FDS_MENUE_TEXT_1)
    * `menue_3` (start=0, mask=11110000b, comment=FDS_MENUE_SIGNAL_1)
    * `menue_3` (start=1, mask=00001111b, comment=FDS_MENUE_TEXT_2)
    * `menue_3` (start=1, mask=11110000b, comment=FDS_MENUE_SIGNAL_2)
    * `menue_3` (start=2, mask=00001111b, comment=FDS_MENUE_TEXT_3)
    * `menue_3` (start=2, mask=11110000b, comment=FDS_MENUE_SIGNAL_3)
    * `menue_3` (start=3, mask=00001111b, comment=FDS_MENUE_TEXT_4)
    * `menue_3` (start=3, mask=11110000b, comment=FDS_MENUE_SIGNAL_4)
    * `menue_3` (start=51, mask=11111111b, comment=FDS_MENUE)

### CFAS_PLX_1 (CAFD 000000B5) — authored by Bundang Thunder X5 | Series: F15,F16,F25,F26,F48,F85,F86

* **Enable Easy Access                                                                         --** by Bundang Thunder ^^**
  * Group `3000`
    * `Modus_FA_SLV` (start=0, mask=00011100b, comment=EINAUSSTIEGSHILFE)

* **Easy Access seat starts moving from end position**
  * Group `3012`
    * `00, 01` (start=4, end=5, mask=11111111b, comment=EAH_SCHUTZFREIRAUM_HINTEN_SLV_PHYS)

* **Easy Access seat starts moving with 1 cm remaining**
  * Group `3012`
    * `00, 0A` (start=4, end=5, mask=11111111b, comment=EAH_SCHUTZFREIRAUM_HINTEN_SLV_PHYS)

* **Easy Access seat starts moving with 2 cm remaining**
  * Group `3012`
    * `00, 14` (start=4, end=5, mask=11111111b, comment=EAH_SCHUTZFREIRAUM_HINTEN_SLV_PHYS)

* **Easy Access seat starts moving with 3 cm remaining**
  * Group `3012`
    * `00, 1E` (start=4, end=5, mask=11111111b, comment=EAH_SCHUTZFREIRAUM_HINTEN_SLV_PHYS)

* **Easy Access seat travel distance: 4 cm**
  * Group `3012`
    * `00, 28` (start=0, end=1, mask=11111111b, comment=EAH_VERFAHRWEG_SLV_PHYS)

* **Easy Access seat travel distance: 5 cm**
  * Group `3012`
    * `00, 32` (start=0, end=1, mask=11111111b, comment=EAH_VERFAHRWEG_SLV_PHYS)

* **Easy Access seat travel distance: 6 cm**
  * Group `3012`
    * `00, 3C` (start=0, end=1, mask=11111111b, comment=EAH_VERFAHRWEG_SLV_PHYS)

* **Easy Access seat travel distance: 7 cm**
  * Group `3012`
    * `00, 46` (start=0, end=1, mask=11111111b, comment=EAH_VERFAHRWEG_SLV_PHYS)

* **Gentleman**
  * Group `3000`
    * `01` (start=1, mask=00000001b, comment=GENTLEMAN)
    * `01` (start=0, mask=00000001b, comment=MEMORY)

* **Set gong when saving seat position**
  * Group `3000`
    * `01` (start=2, mask=00001000b, comment=MEMORY_GONG)

### CBFS_PLX_1 (CAFD 000000B6) — authored by Bundang Thunder X5 | Series: F15,F16,F25,F26,F48,F85,F86

* **Passenger seat Gentleman                                                                                         --** by Bundang Thunder ^^**
  * Group `3000`
    * `01` (start=1, mask=00000001b, comment=GENTLEMAN)
    * `01` (start=0, mask=00000001b, comment=MEMORY)

### ACSM_4C (CAFD 00000909) — authored by Bundang Thunder X6 | Series: F15,F16,F25,F26,F48,F85,F86

* **Seat belt warning chime for only 5 seconds                                                                                 --** by Bundang Thunder ^^**
  * Group `3000`
    * `05` (start=3, mask=11111111b, comment=GWF_SBR_WARNDAUER)

* **Delete driver seat belt warning light**
  * Group `3000`
    * `00` (start=16, mask=00000001b, comment=SBR_PreWarning_Fahrer)

* **Delete passenger seat belt warning light**
  * Group `3000`
    * `00` (start=16, mask=00000010b, comment=SBR_PreWarning_Beifahrer)

* **Disable driver seat belt warning chime**
  * Group `3000`
    * `00` (start=15, mask=00000010b, comment=SeatBeltReminder_SBR_Fahrer)

* **Disable passenger seat belt warning chime**
  * Group `3000`
    * `00` (start=15, mask=00000100b, comment=SeatBeltReminder_SBR_Beifahrer)

### BDC_01 (CAFD 000017BE) — authored by Bundang Thunder X6 | Series: F15,F16,F25,F26,F48,F85,F86

* **Activate hazard lights during hard braking                                                                                   --** by Bundang Thunder ^^**
  * Group `3068`
    * `01` (start=26, mask=00000001b, comment=WB_GB_ENABLE)

* **Limit passenger mirror tilt to 30 degrees in reverse**
  * Group `3110`
    * `1E` (start=1, mask=11111111b, comment=ASP_BORDSTEINAUTOMATIK_DELTA)

* **One-touch turn signal flashes five times**
  * Group `3069`
    * `Tippblinken_fuenfmal` (start=215, mask=00011000b, comment=PIA_DEFAULT_TIPPBLINKEN)

* **Enable welcome lights**
  * Group `3068`
    * `01` (start=13, mask=00100000b, comment=WL_WIEDERHOLSPERRE_AKTIV)

* **Enable follow me home**
  * Group `3068`
    * `01` (start=13, mask=01000000b, comment=FMH_WIEDERHOLSPERRE_AKTIV)

* **Close trunk immediately via remote**
  * Group `30D0`
    * `01` (start=18, mask=111111!1b, comment=RC_TIME_DELAY_BOOTLID)

* **Open and close windows with remote**
  * Group `3056`
    * `01` (start=0, mask=01000000b, comment=KOMFORTOEFFNUNG_FB)

* **Fold mirrors immediately when locking (lock folding)**
  * Group `3056`
    * `00` (start=10, mask=11111111b, comment=KOMFORT_SCHLIESSEN)

* **Allow windows to keep closing with doors open (front and rear)**
  * Group `3050`
    * `00` (start=0, mask=00000001b, comment=FH_TUERAUF_STOP_MAUT)
  * Group `3051`
    * `00` (start=0, mask=00000001b, comment=FH_TUERAUF_STOP_MAUT_REAR)

* **VLD**
  * Group `3073`
    * `F015_ohne_AFS` (start=40, end=42, mask=11111111b, comment=LUT_FLC_FORWARDLIGHTING_Y)
    * `F015_enable` (start=152, mask=00000001b, comment=C_AFS_ENA)

* **Turn on door handle lights when reversing**
  * Group `3070`
    * `F015_ohne_AFS` (start=128, mask=00000001b, comment=OVT_BEI_RUECKFAHRLICHT)

* **Disable auto start/stop in Comfort mode**
  * Group `3023`
    * `01` (start=0, mask=00010000b, comment=TCM_MSA_DEFAULT_OFF)

* **Disable auto start/stop in Eco Pro mode**
  * Group `3023`
    * `00` (start=1, mask=00001100b, comment=TCM_MSA_ECO_MODE)

* **Remember last auto start/stop state**
  * Group `3023`
    * `01` (start=0, mask=00100000b, comment=TCM_MSA_MEMORY)

* **Double horn when locking with engine running - enable**
  * Group `3040`
    * `01` (start=0, mask=00000100b, comment=VAM_HORN_AT_SECURE)

* **Double horn when locking with engine running - disable**
  * Group `3040`
    * `00` (start=0, mask=00000100b, comment=VAM_HORN_AT_SECURE)

### HKFM (CAFD 000007C8) — authored by Bundang Thunder X6 | Series: F15,F16,F25,F26,F48,F85,F86

* **Auto-close trunk (footwell switch + remote)**
  * Group `3010`
    * `01` (start=0, mask=00001000b, comment=TASTER_FBD)
    * `01` (start=2, mask=00000100b, comment=SCH_TOEHKI)
    * `01` (start=2, mask=00001000b, comment=SCH_FBD)

### HU_NBT (CAFD 00000DED) — authored by Bundang Thunder X6 | Series: F15,F16,F25,F26,F48,F85,F86

* **Set time automatically                                                                                         --** by Bundang Thunder ^^**
  * Group `3000`
    * `navigation` (start=19, mask=00000110b, comment=SETTINGS_TIME_AUTOMATIC)
    * `01` (start=105, mask=00100000b, comment=CLOCK_CHANGE_AUTOMATIC)

* **Watch video/DMB/navigation while driving**
  * Group `3000`
    * `FF` (start=72, mask=11111111b, comment=SPEEDLOCK_X_KMH_MAX)
    * `FF` (start=71, mask=11111111b, comment=SPEEDLOCK_X_KMH_MIN)
    * `00` (start=5, mask=00010000b, comment=VIDEO_FRONT_LOCKED)
    * `00` (start=5, mask=00000100b, comment=VIDEO_HANDBRAKE)
    * `None` (start=57, mask=00000111b, comment=VIDEO_SPEEDLOCK_CONDITION)

* **Suppress all warning messages**
  * Group `3001`
    * `kein_ld` (start=58, mask=11111111b, comment=LEGAL_DISCLAIMER_TIME)
    * `kein_ld` (start=52, mask=11111111b, comment=MACRO_CAM_LEGALDISCLAIMER)

* **Enable trailer zoom menu when reversing**
  * Group `3001`
    * `01` (start=54, mask=00000001b, comment=MACRO_TRAILER_COUPLING)

* **Close windows when it rains**
  * Group `3000`
    * `01` (start=19, mask=00001000b, comment=REGEN_SCHLIESSEN)

* **X-Drive**
  * Group `3000`
    * `01` (start=5, mask=00000001b, comment=COMPASS)
    * `01` (start=15, mask=00000001b, comment=X_VIEW)
    * `trajectory1` (start=26, mask=00110000b, comment=X_VIEW_GRAPHIC_SLOP)
    * `trajectory1` (start=26, mask=11000000b, comment=X_VIEW_GRAPHIC_ROLL)
    * `01` (start=110, mask=00000010b, comment=MOMENTDISTRIBUTION_MENU)

* **Enable USB video playback 1/2**
  * Group `3000`
    * `01` (start=15, mask=00010000b, comment=ENT_CODEC_OGG)
    * `01` (start=15, mask=00100000b, comment=ENT_CODEC_XVID)
    * `01` (start=15, mask=01000000b, comment=ENT_CODEC_VCD)
    * `01` (start=13, mask=00000100b, comment=ENT_MC_VIDEO_SUPPORT)

* **Enable USB video playback 2/2**
  * Group `3003`
    * `both` (start=33, mask=00000110b, comment=API_USB_VIDEO)
    * `both` (start=33, mask=00011000b, comment=API_IPOD_VIDEO)

* **Change warning chime to Rolls-Royce sound**
  * Group `3002`
    * `rolls_royce` (start=26, mask=00111000b, comment=SOUND_SIGNAL_SET)

* **Configure Sport mode**
  * Group `3001`
    * `popup_and_config` (start=55, mask=00011000b, comment=MACRO_FDS)
  * Group `3000`
    * `01` (start=101, mask=00010000b, comment=EFF_DYN_SPORT_CID)
    * `01` (start=107, mask=00000100b, comment=EFF_DYN_SPORT_UNIT)

* **Startup animation**
  * Group `3001`
    * `animation` (start=62, mask=00000110b, comment=STARTUP_TYPE)
    * `variant_01` (start=62, mask=01111000b, comment=STARTUP_EMBLEM)

* **Volume adjustment bar**
  * Group `3002`
    * `01` (start=52, mask=01000000b, comment=VOLUME_POPUP_DISPLAY)
    * `01` (start=52, mask=10000000b, comment=VOLUME_POPUP_REJECTION)
    * `01` (start=53, mask=00000001b, comment=VOLUME_POPUP_EXCEPTION)

* **Show TPMC tire pressure temperature**
  * Group `3001`
    * `druck_und_temperatur` (start=66, mask=00001100b, comment=RDC_DRUCK_TEMP)

* **Output ringtone through speakers (iPhone only)**
  * Group `3003`
    * `01` (start=6, mask=10000000b, comment=INBAND_RINGING)

* **Lock/unlock confirmation chime (requires piezo buzzer sensor)**
  * Group `3000`
    * `01` (start=110, mask=00000001b, comment=ACOUSTICAL_LOCK_CONFIRM)

* **Change M Sport display cluster colors**
  * Group `3000`
    * `01` (start=133, mask=01000000b, comment=M_VEHICLE)

* **Adjust high-beam assistant in iDrive**
  * Group `3000`
    * `01` (start=109, mask=10000000b, comment=HIGH_BEAM_ASSISTANT)

* **Show currently playing album art in iDrive**
  * Group `3000`
    * `01` (start=9, mask=00000100b, comment=ENT_BTAS_IAP_COVERART)
  * Group `3003`
    * `01` (start=19, mask=00000100b, comment=ENT_BTAS_METADATA)
    * `01` (start=19, mask=00001000b, comment=ENT_BTAS_BROWSING)

* **Unlock DVD region code**
  * Group `3000`
    * `alle_anderen` (start=7, mask=11111111b, comment=ENT_VIDEO_DVD_AREA_CODE)

* **Show turn signals in HUD**
  * Group `3001`
    * `01` (start=55, mask=10000000b, comment=HUD_TURNSIGNAL)

* **Set sound system to Bang & Olufsen**
  * Group `3000`
    * `keine_insz` (start=21, mask=01100000b, comment=HIGH_END_AUDIO_B_UND_W)

* **Enable Logic7 (S667A HiFi vehicles)**
  * Group `3000`
    * `01` (start=22, mask=00001000b, comment=LOGIC7_SYMBOL)

* **Enhance audio mid-bass**
  * Group `3002`
    * `highpremium` (start=29, mask=00111100b, comment=AUDIO_SYSTEM)
    * `variant3` (start=21, mask=00000011b, comment=AUDIO_SYSTEM_VAR)

### ICMQL (CAFD 0000067B) — authored by Bundang Thunder X6 | Series: F15,F16,F25,F26,F48,F85,F86

* **Default to Eco mode at start                                                                              --** by Bundang Thunder ^^**
  * Group `3000`
    * `verbaut` (start=36, mask=00001000b, comment=IcmKod_B_InitEco)

* **Enable cruise control**
  * Group `3000`
    * `01` (start=128, mask=00001110b, comment=C_Fahrfunktion)

* **Enable cruise control**
  * Group `3000`
    * `04` (start=128, mask=00001110b, comment=C_Fahrfunktion)

* **Enable Sport+ mode**
  * Group `3000`
    * `verbaut` (start=18, mask=11111111b, comment=IcmKod_B_S2TBA)

* **ACC distance**
  * Group `3000`
    * `01` (start=184, mask=00000111b, comment=C_Abstandsstufe_init)

* **Adjust active blind spot activation speed by -20 km/h**
  * Group `3000`
    * `01` (start=190, mask=00111111b, comment=C_ZSW_Aktivierunggeschwindigkeit_Funktion_low)

* **Enable coasting mode**
  * Group `3000`
    * `01` (start=120, mask=11000000b, comment=C_Segeln_vorhanden)

### IHKA_CBF (CAFD 000047D6) — authored by Bundang Thunder X6 | Series: F15,F16,F25,F26,F48,F85,F86

* **Remember last air conditioning state                                                                               --** by Bundang Thunder ^^**
  * Group `3000`
    * `01` (start=5, mask=00010000b, comment=OFF_MEMORY)

* **Prevent AUTO button from turning on A/C**
  * Group `3000`
    * `01` (start=5, mask=00001000b, comment=AC_NICHT_EIN_BEI_AUTO)

* **Remember HVAC recirculation mode**
  * Group `3000`
    * `01` (start=0, mask=00000100b, comment=MEMORY_UMLUFT)

### JBBFE (CAFD 00000014) — authored by Bundang Thunder X6 | Series: F15,F16,F25,F26,F48,F85,F86

* **Disable headlight washer                                                                                --** by Bundang Thunder ^^**
  * Group `3000`
    * `00` (start=8, mask=00000001b, comment=SCHEINWERFERREINIGUNG)

### KAFAS2 (CAFD 00001148) — authored by Bundang Thunder X6 | Series: F15,F16,F25,F26,F48,F85,F86

* **Automatic high-beam assistant                                                                                --** by Bundang Thunder ^^**
  * Group `3050`
    * `FLA_on` (start=1, mask=00000001b, comment=FLA_ON_OFF)
    * `CN` (start=6, mask=11111111b, comment=SPEED_SWITCHING_HIGH_BEAMS_ON)
    * `China` (start=7, mask=11111111b, comment=SPEED_SWITCHING_HIGH_BEAMS_OFF)

### KOMBI FPK_I12 (CAFD 00001060) — authored by Bundang Thunder X6 | Series: F15,F16,F25,F26,F48,F85,F86

* **Show phone, entertainment, and voice prompts in HUD                                                               --** by Bundang Thunder ^^**
  * Group `3003`
    * `01` (start=10, mask=00000001b, comment=HUD_ENTERTAINMENT_ENABLE)
    * `01` (start=9, mask=00100000b, comment=HUD_STARTUP_ENABLE)
  * Group `3000`
    * `01` (start=41, mask=00000001b, comment=HUD_TLC_ENABLE)
    * `01` (start=40, mask=10000000b, comment=HUD_VZA_ENABLE)

* **Show turn signals in HUD**
  * Group `3003`
    * `01` (start=11, mask=00000001b, comment=HUD_BLINKER_ENABLE)
  * Group `3008`
    * `01` (start=5, mask=00000001b, comment=HUD_PIA_BLINKER)

* **Show logo on instrument cluster**
  * Group `3003`
    * `01` (start=3, mask=00000010b, comment=MPM_ENABLE)
  * Group `3000`
    * `mpm_x6` (start=44, mask=11110000b, comment=MPM_LOGO)
    * `mpm_x6` (start=44, mask=00001111b, comment=BMW_LOGO)

* **Show compass in instrument cluster**
  * Group `3003`
    * `01` (start=12, mask=00010000b, comment=KOMPASS_GRAPH_ENABLE)

* **Disable warning chime below 3 degrees**
  * Group `3000`
    * `00` (start=50, mask=00000001b, comment=CC_TEMPERATURWARNUNG)

* **Show power output in instrument cluster**
  * Group `3003`
    * `01` (start=11, mask=00000010b, comment=MOTORLEISTUNG_ENABLE)

* **Enable Sport+ menu in cluster**
  * Group `300C`
    * `menue_3` (start=0, mask=00001111b, comment=FDS_MENUE_TEXT_1)
    * `menue_3` (start=0, mask=11110000b, comment=FDS_MENUE_SIGNAL_1)
    * `menue_3` (start=1, mask=00001111b, comment=FDS_MENUE_TEXT_2)
    * `menue_3` (start=1, mask=11110000b, comment=FDS_MENUE_SIGNAL_2)
    * `menue_3` (start=2, mask=00001111b, comment=FDS_MENUE_TEXT_3)
    * `menue_3` (start=2, mask=11110000b, comment=FDS_MENUE_SIGNAL_3)
    * `menue_3` (start=3, mask=00001111b, comment=FDS_MENUE_TEXT_4)
    * `menue_3` (start=3, mask=11110000b, comment=FDS_MENUE_SIGNAL_4)
    * `menue_3` (start=51, mask=11111111b, comment=FDS_MENUE)

### CFAS_PLX_1 (CAFD 000000B5) — authored by Bundang Thunder X6 | Series: F15,F16,F25,F26,F48,F85,F86

* **Enable Easy Access                                                                         --** by Bundang Thunder ^^**
  * Group `3000`
    * `Modus_FA_SLV` (start=0, mask=00011100b, comment=EINAUSSTIEGSHILFE)

* **Easy Access seat starts moving from end position**
  * Group `3012`
    * `00, 01` (start=4, end=5, mask=11111111b, comment=EAH_SCHUTZFREIRAUM_HINTEN_SLV_PHYS)

* **Easy Access seat starts moving with 1 cm remaining**
  * Group `3012`
    * `00, 0A` (start=4, end=5, mask=11111111b, comment=EAH_SCHUTZFREIRAUM_HINTEN_SLV_PHYS)

* **Easy Access seat starts moving with 2 cm remaining**
  * Group `3012`
    * `00, 14` (start=4, end=5, mask=11111111b, comment=EAH_SCHUTZFREIRAUM_HINTEN_SLV_PHYS)

* **Easy Access seat starts moving with 3 cm remaining**
  * Group `3012`
    * `00, 1E` (start=4, end=5, mask=11111111b, comment=EAH_SCHUTZFREIRAUM_HINTEN_SLV_PHYS)

* **Easy Access seat travel distance: 4 cm**
  * Group `3012`
    * `00, 28` (start=0, end=1, mask=11111111b, comment=EAH_VERFAHRWEG_SLV_PHYS)

* **Easy Access seat travel distance: 5 cm**
  * Group `3012`
    * `00, 32` (start=0, end=1, mask=11111111b, comment=EAH_VERFAHRWEG_SLV_PHYS)

* **Easy Access seat travel distance: 6 cm**
  * Group `3012`
    * `00, 3C` (start=0, end=1, mask=11111111b, comment=EAH_VERFAHRWEG_SLV_PHYS)

* **Easy Access seat travel distance: 7 cm**
  * Group `3012`
    * `00, 46` (start=0, end=1, mask=11111111b, comment=EAH_VERFAHRWEG_SLV_PHYS)

* **Gentleman**
  * Group `3000`
    * `01` (start=1, mask=00000001b, comment=GENTLEMAN)
    * `01` (start=0, mask=00000001b, comment=MEMORY)

* **Set gong when saving seat position**
  * Group `3000`
    * `01` (start=2, mask=00001000b, comment=MEMORY_GONG)

### CBFS_PLX_1 (CAFD 000000B6) — authored by Bundang Thunder X6 | Series: F15,F16,F25,F26,F48,F85,F86

* **Passenger seat Gentleman                                                                                         --** by Bundang Thunder ^^**
  * Group `3000`
    * `01` (start=1, mask=00000001b, comment=GENTLEMAN)
    * `01` (start=0, mask=00000001b, comment=MEMORY)

### ACSM_3 (CAFD 0000009C) — authored by Bundang Thunder 7 Series | Series: F01,F02,F03,F04,F07

* **Seat belt warning chime for only 5 seconds                                                                                 --** by Bundang Thunder ^^**
  * Group `3001`
    * `05` (start=3, mask=11111111b, comment=GWF_SBR_WARNDAUER)

* **Delete driver seat belt warning light**
  * Group `3000`
    * `00` (start=12, mask=00000010b, comment=SPW_FA)

* **Delete passenger seat belt warning light**
  * Group `3000`
    * `00` (start=12, mask=00000010b, comment=SPW_BF)

* **Disable driver seat belt warning chime**
  * Group `3000`
    * `00` (start=11, mask=00000010b, comment=SBR_FA_GWF_SBR_FA)

* **Disable passenger seat belt warning chime**
  * Group `3000`
    * `00` (start=11, mask=00000100b, comment=SBR_BF_GWF_SBR_BF)

### CAS_04 (CAFD 0000000F) — authored by Bundang Thunder 7 Series | Series: F01,F02,F03,F04,F07

* **Turn off audio when engine stops                                                                                  --** by Bundang Thunder ^^**
  * Group `3000`
    * `01` (start=2, mask=00000001b, comment=TC_LOGIC_KLR_OFF_DOOR)

* **Unlock doors when engine turns off**
  * Group `3002`
    * `01` (start=1, mask=10000000b, comment=ER_KEYOUT_AUTOVR)

* **Fold mirrors immediately when locking (lock folding)**
  * Group `3003`
    * `00` (start=12, mask=11111111b, comment=KMFRT_SCHLIESSEN)

* **Start engine without pressing brake**
  * Group `3000`
    * `00` (start=1, mask=00000001b, comment=TC_STARTLOCK_BRAKE)

* **Start engine without pressing clutch**
  * Group `3000`
    * `00` (start=1, mask=00000100b, comment=TC_STARTLOCK_CLUTCH)

* **Allow engine start in park**
  * Group `3000`
    * `00` (start=1, mask=00000010b, comment=TC_STARTLOCK_PARK)
    * `00` (start=1, mask=00010000b, comment=TC_STARTLOCK_DRIVINGREADINESS)

* **Sound horn with remote**
  * Group `3002`
    * `01` (start=1, mask=00000010b, comment=REMOTE_KEY_SPECIAL_FCT)

### DSC_Premium (CAFD 000000D8) — authored by Bundang Thunder 7 Series | Series: F01,F02,F03,F04,F07

* **Release parking brake by pressing accelerator only --** by Bundang Thunder ^^**
  * Group `3000`
    * `01` (start=27, mask=00100000b, comment=Funktion_AutomaticDriveawayRelease_aktiv)

### FRM__03CT (CAFD 0000012F) — authored by Bundang Thunder 7 Series | Series: F01,F02,F03,F04,F07

* **Activate hazard lights during hard braking                                                                                   --** by Bundang Thunder ^^**
  * Group `3050`
    * `01` (start=2, mask=10000000b, comment=WB_GB_ENABLE)

* **Turn on fog lights in welcome lighting**
  * Group `3050`
    * `soft_on_LED` (start=29, mask=00001100b, comment=WL_FUNKTION_NSW)

* **Turn on headlights in welcome lighting**
  * Group `3050`
    * `soft_on_LED` (start=30, mask=00001100b, comment=WL_FUNKTION_AL)

* **Automatic high-beam assistant**
  * Group `3050`
    * `automatisch` (start=20, mask=00100000b, comment=FLA_AUTO_AKTIV)
    * `01` (start=20, mask=00010000b, comment=FLA_VERBAUT)

* **Allow front windows to keep closing with door open**
  * Group `3030`
    * `00` (start=1, mask=00000100b, comment=FH_TUER_AUF_STOP_MAUT)

* **Limit passenger mirror tilt to 30 degrees in reverse**
  * Group `3020`
    * `1E` (start=1, mask=11111111b, comment=ASP_BORDSTEINAUTOMATIK_DELTA)

* **One-touch turn signal flashes five times**
  * Group `3050`
    * `04` (start=1, mask=00000111b, comment=BLINKZYKLEN_ANZAHL_TIPP)

### FZD__04 (CAFD 00000552) — authored by Bundang Thunder 7 Series | Series: F01,F02,F03,F04,F07

* **Door open/close chime --** by Bundang Thunder ^^**
  * Group `3002`
    * `01` (start=4, mask=00001000b, comment=Akkustische Quittierung Schaerfen)
    * `01` (start=4, mask=00010000b, comment=Akkustische Quittierung Schaerfen mit Klappenbeachtung)
    * `01` (start=4, mask=00100000b, comment=Akkustische Quittierung Entschaerfen)
    * `01` (start=2, mask=00010000b, comment=Lautstaerke Akkustische Quittterung tageszeitabhaengig)

### HKFM (CAFD 000007C8) — authored by Bundang Thunder 7 Series | Series: F01,F02,F03,F04,F07

* **Auto-close trunk (footwell switch + remote)                                                                   --** by Bundang Thunder ^^**
  * Group `3010`
    * `01` (start=0, mask=00001000b, comment=TASTER_FBD)
    * `01` (start=2, mask=00000100b, comment=SCH_TOEHKI)
    * `01` (start=2, mask=00001000b, comment=SCH_FBD)

### FZD__04 (CAFD 00000552) — authored by Bundang Thunder 7 Series | Series: F01,F02,F03,F04,F07

* **Door open/close chime --** by Bundang Thunder ^^**
  * Group `3002`
    * `01` (start=4, mask=00001000b, comment=Akkustische Quittierung Schaerfen)
    * `01` (start=4, mask=00100000b, comment=Akkustische Quittierung Entschaerfen)

### HU_CICHB (CAFD 000000F9) — authored by Bundang Thunder 7 Series | Series: F01,F02,F03,F04,F07

* **Watch video/DMB/navigation while driving                                                                          --** by Bundang Thunder ^^**
  * Group `3000`
    * `FF` (start=24, mask=11111111b, comment=SPEEDLOCK_X_KMH_MAX)
    * `FF` (start=23, mask=11111111b, comment=SPEEDLOCK_X_KMH_MIN)
    * `00` (start=8, mask=00000000b, comment=VIDEO_NUR_MIT_HANDBREMSE)
    * `00` (start=9, mask=10000000b, comment=ENT_VIDEO_VORNE_GESPERRT)

* **Suppress all warning messages**
  * Group `3001`
    * `kein_ld` (start=27, mask=11111111b, comment=LEGAL_DISCLAIMER_TIME)
    * `kein_ld` (start=28, mask=11111111b, comment=MACRO_CAM_LEGALDISCLAIMER)

* **Enable trailer zoom menu when reversing**
  * Group `3001`
    * `01` (start=23, mask=00000001b, comment=MACRO_TRAILER_COUPLING)

* **Configure Sport mode**
  * Group `3000`
    * `popup_and_config` (start=7, mask=00110000b, comment=MACRO_FDS)
  * Group `3000`
    * `01` (start=47, mask=00010000b, comment=EFF_DYN_SPORT_CID)
    * `01` (start=61, mask=00000100b, comment=EFF_DYN_SPORT_UNIT)

* **Output ringtone through speakers (iPhone only)**
  * Group `3003`
    * `01` (start=6, mask=10000000b, comment=INBAND_RINGING)

* **Lock/unlock confirmation chime (requires piezo buzzer sensor)**
  * Group `3000`
    * `01` (start=8, mask=00100000b, comment=ACOUSTICAL_LOCK_CONFIRM)

* **Adjust high-beam assistant in iDrive**
  * Group `3000`
    * `01` (start=0, mask=00000010b, comment=HIGH_BEAM_ASSISTANT)

* **Show turn signals in HUD**
  * Group `3000`
    * `01` (start=22, end=2, mask=00001000b, comment=HUD_TURNSIGNAL)

* **Enable Logic7 (S667A HiFi vehicles)**
  * Group `3000`
    * `01` (start=4, mask=10000000b, comment=LOGIC7_SYMBOL)

* **Enhance audio mid-bass**
  * Group `3002`
    * `03` (start=0, mask=00000111b, comment=AUDIO_SYSTEM_CIC)
    * `03` (start=5, mask=00001100b, comment=AUDIO_SYSTEM_VAR)

### HU_NBT (CAFD 00000DED) — authored by Bundang Thunder 7 Series | Series: F01,F02,F03,F04,F07

* **Set time automatically                                                                                         --** by Bundang Thunder ^^**
  * Group `3000`
    * `navigation` (start=19, mask=00000110b, comment=SETTINGS_TIME_AUTOMATIC)
    * `01` (start=105, mask=00100000b, comment=CLOCK_CHANGE_AUTOMATIC)

* **Watch video/DMB/navigation while driving**
  * Group `3000`
    * `FF` (start=72, mask=11111111b, comment=SPEEDLOCK_X_KMH_MAX)
    * `FF` (start=71, mask=11111111b, comment=SPEEDLOCK_X_KMH_MIN)
    * `00` (start=5, mask=00010000b, comment=VIDEO_FRONT_LOCKED)
    * `00` (start=5, mask=00000100b, comment=VIDEO_HANDBRAKE)
    * `None` (start=57, mask=00000111b, comment=VIDEO_SPEEDLOCK_CONDITION)

* **Suppress all warning messages**
  * Group `3001`
    * `kein_ld` (start=58, mask=11111111b, comment=LEGAL_DISCLAIMER_TIME)
    * `kein_ld` (start=52, mask=11111111b, comment=MACRO_CAM_LEGALDISCLAIMER)

* **Enable trailer zoom menu when reversing**
  * Group `3001`
    * `01` (start=54, mask=00000001b, comment=MACRO_TRAILER_COUPLING)

* **Close windows when it rains**
  * Group `3000`
    * `01` (start=19, mask=00001000b, comment=REGEN_SCHLIESSEN)

* **X-Drive**
  * Group `3000`
    * `01` (start=5, mask=00000001b, comment=COMPASS)
    * `01` (start=15, mask=00000001b, comment=X_VIEW)
    * `trajectory1` (start=26, mask=00110000b, comment=X_VIEW_GRAPHIC_SLOP)
    * `trajectory1` (start=26, mask=11000000b, comment=X_VIEW_GRAPHIC_ROLL)
    * `01` (start=110, mask=00000010b, comment=MOMENTDISTRIBUTION_MENU)

* **Enable USB video playback 1/2**
  * Group `3000`
    * `01` (start=15, mask=00010000b, comment=ENT_CODEC_OGG)
    * `01` (start=15, mask=00100000b, comment=ENT_CODEC_XVID)
    * `01` (start=15, mask=01000000b, comment=ENT_CODEC_VCD)
    * `01` (start=13, mask=00000100b, comment=ENT_MC_VIDEO_SUPPORT)

* **Enable USB video playback 2/2**
  * Group `3003`
    * `both` (start=33, mask=00000110b, comment=API_USB_VIDEO)
    * `both` (start=33, mask=00011000b, comment=API_IPOD_VIDEO)

* **Change warning chime to Rolls-Royce sound**
  * Group `3002`
    * `rolls_royce` (start=26, mask=00111000b, comment=SOUND_SIGNAL_SET)

* **Configure Sport mode**
  * Group `3001`
    * `popup_and_config` (start=55, mask=00011000b, comment=MACRO_FDS)
  * Group `3000`
    * `01` (start=101, mask=00010000b, comment=EFF_DYN_SPORT_CID)
    * `01` (start=107, mask=00000100b, comment=EFF_DYN_SPORT_UNIT)

* **Startup animation**
  * Group `3001`
    * `animation` (start=62, mask=00000110b, comment=STARTUP_TYPE)
    * `variant_01` (start=62, mask=01111000b, comment=STARTUP_EMBLEM)

* **Volume adjustment bar**
  * Group `3002`
    * `01` (start=52, mask=01000000b, comment=VOLUME_POPUP_DISPLAY)
    * `01` (start=52, mask=10000000b, comment=VOLUME_POPUP_REJECTION)
    * `01` (start=53, mask=00000001b, comment=VOLUME_POPUP_EXCEPTION)

* **Show TPMC tire pressure temperature**
  * Group `3001`
    * `druck_und_temperatur` (start=66, mask=00001100b, comment=RDC_DRUCK_TEMP)

* **Output ringtone through speakers (iPhone only)**
  * Group `3003`
    * `01` (start=6, mask=10000000b, comment=INBAND_RINGING)

* **Lock/unlock confirmation chime (requires piezo buzzer sensor)**
  * Group `3000`
    * `01` (start=110, mask=00000001b, comment=ACOUSTICAL_LOCK_CONFIRM)

* **Change M Sport display cluster colors**
  * Group `3000`
    * `01` (start=133, mask=01000000b, comment=M_VEHICLE)

* **Adjust high-beam assistant in iDrive**
  * Group `3000`
    * `01` (start=109, mask=10000000b, comment=HIGH_BEAM_ASSISTANT)

* **Show currently playing album art in iDrive**
  * Group `3000`
    * `01` (start=9, mask=00000100b, comment=ENT_BTAS_IAP_COVERART)
  * Group `3003`
    * `01` (start=19, mask=00000100b, comment=ENT_BTAS_METADATA)
    * `01` (start=19, mask=00001000b, comment=ENT_BTAS_BROWSING)

* **Unlock DVD region code**
  * Group `3000`
    * `alle_anderen` (start=7, mask=11111111b, comment=ENT_VIDEO_DVD_AREA_CODE)

* **Show turn signals in HUD**
  * Group `3001`
    * `01` (start=55, mask=10000000b, comment=HUD_TURNSIGNAL)

* **Set sound system to Bang & Olufsen**
  * Group `3000`
    * `keine_insz` (start=21, mask=01100000b, comment=HIGH_END_AUDIO_B_UND_W)

* **Enable Logic7 (S667A HiFi vehicles)**
  * Group `3000`
    * `01` (start=22, mask=00001000b, comment=LOGIC7_SYMBOL)

* **Enhance audio mid-bass**
  * Group `3002`
    * `highpremium` (start=29, mask=00111100b, comment=AUDIO_SYSTEM)
    * `variant3` (start=21, mask=00000011b, comment=AUDIO_SYSTEM_VAR)

### ICMQL (CAFD 00000052) — authored by Bundang Thunder 7 Series | Series: F01,F02,F03,F04,F07

* **Enable Sport+ mode                                                                                     --** by Bundang Thunder ^^**
  * Group `3000`
    * `verbaut` (start=18, mask=11111111b, comment=IcmKod_B_S2TBA)

* **Configure standard Sport mode to disable DCS**
  * Group `3000`
    * `verbaut` (start=19, mask=11111111b, comment=IcmKod_B_S205A)

### IHKA_CBF (CAFD 00000092) — authored by Bundang Thunder 7 Series | Series: F01,F02,F03,F04,F07

* **Remember last air conditioning state                                                                               --** by Bundang Thunder ^^**
  * Group `3000`
    * `01` (start=5, mask=00010000b, comment=OFF_MEMORY)

* **Prevent AUTO button from turning on A/C**
  * Group `3000`
    * `01` (start=5, mask=00001000b, comment=AC_NICHT_EIN_BEI_AUTO)

* **Remember HVAC recirculation mode**
  * Group `3000`
    * `01` (start=0, mask=00000100b, comment=MEMORY_UMLUFT)

### JBBFE (CAFD 00000014) — authored by Bundang Thunder 7 Series | Series: F01,F02,F03,F04,F07

* **Allow rear windows to keep closing with door open --** by Bundang Thunder ^^**
  * Group `3070`
    * `00` (start=0, mask=00000100b, comment=FH_TUERAUF_STOP_MAUT)

* **Disable headlight washer**
  * Group `3000`
    * `00` (start=8, mask=00000001b, comment=SCHEINWERFERREINIGUNG)

### JBBF_E3_PDC (CAFD 00000018) — authored by Bundang Thunder 7 Series | Series: F01,F02,F03,F04,F07

* **Allow around view to turn on at any time --** by Bundang Thunder ^^**
  * Group `3009`
    * `FF` (start=15, mask=11111111b, comment=V_SCHWELLE_1)
    * `FF` (start=16, mask=11111111b, comment=V_SCHWELLE_2)
    * `FF` (start=17, mask=11111111b, comment=D_SCHWELLE_1)
    * `FF` (start=18, mask=11111111b, comment=D_SCHWELLE_2)

### KOMBI L6 BO (CAFD 00000069) — authored by Bundang Thunder 7 Series | Series: F01,F02,F03,F04,F07

* **Show phone, entertainment, and voice prompts in HUD                                                               --** by Bundang Thunder ^^**
  * Group `3000`
    * `01` (start=41, mask=00001000b, comment=HUD_ENTERTAINMENT_ENABLE)
  * Group `3003`
    * `01` (start=9, mask=00100000b, comment=HUD_STARTUP_ENABLE)
  * Group `3000`
    * `01` (start=41, mask=00000001b, comment=HUD_TLC_ENABLE)
    * `01` (start=40, mask=10000000b, comment=HUD_VZA_ENABLE)

* **Show turn signals in HUD**
  * Group `3000`
    * `01` (start=42, mask=00100000b, comment=BLINKER_HUD_ENABLE)
  * Group `3008`
    * `01` (start=5, mask=00000001b, comment=HUD_PIA_BLINKER)

* **Disable warning chime below 3 degrees**
  * Group `3000`
    * `00` (start=42, mask=00000100b, comment=CC_TEMPERATURWARNUNG)

* **Enable Sport+ menu in cluster**
  * Group `300C`
    * `menue_3` (start=0, mask=00001111b, comment=FDS_MENUE_TEXT_1)
    * `menue_3` (start=0, mask=11110000b, comment=FDS_MENUE_SIGNAL_1)
    * `menue_3` (start=1, mask=00001111b, comment=FDS_MENUE_TEXT_2)
    * `menue_3` (start=1, mask=11110000b, comment=FDS_MENUE_SIGNAL_2)
    * `menue_3` (start=2, mask=00001111b, comment=FDS_MENUE_TEXT_3)
    * `menue_3` (start=2, mask=11110000b, comment=FDS_MENUE_SIGNAL_3)
    * `menue_3` (start=3, mask=00001111b, comment=FDS_MENUE_TEXT_4)
    * `menue_3` (start=3, mask=11110000b, comment=FDS_MENUE_SIGNAL_4)

* **Instrument cluster daytime lower color: gray**
  * Group `3000`
    * `01` (start=41, mask=00000010b, comment=HINTERGRUND_FARBE_TAG)

* **Instrument cluster daytime lower color: orange**
  * Group `3000`
    * `00` (start=41, mask=00000010b, comment=HINTERGRUND_FARBE_TAG)

* **Instrument cluster nighttime lower color: gray**
  * Group `3000`
    * `01` (start=41, mask=00000100b, comment=HINTERGRUND_FARBE_NACHT)

* **Instrument cluster nighttime lower color: orange**
  * Group `3000`
    * `00` (start=41, mask=00000100b, comment=HINTERGRUND_FARBE_NACHT)

### SZL_LWS_03 (CAFD 0000033D) — authored by Bundang Thunder 7 Series | Series: F01,F02,F03,F04,F07

* **Enable paddle shifters --** by Bundang Thunder ^^**
  * Group `3000`
    * `01` (start=2, mask=00000001b, comment=Lenkrad_Schaltpaddles)

### TRSVC (CAFD 00000223) — authored by Bundang Thunder 7 Series | Series: F01,F02,F03,F04,F07

* **Allow side view at any time                                                                   --** by Bundang Thunder ^^**
  * Group `3000`
    * `FF` (start=114, mask=11111111b, comment=SV_Activate_Speed_Limit)
    * `FF` (start=115, mask=11111111b, comment=SV_Deactivate_Speed)

### CFAS_PLX_1 (CAFD 000000B5) — authored by Bundang Thunder 7 Series | Series: F01,F02,F03,F04,F07

* **Driver Enable Easy Access: testing --** by Bundang Thunder ^^**
  * Group `3000`
    * `01` (start=0, mask=00011100b, comment=EA_Hilfe)

* **Gentleman**
  * Group `3000`
    * `01` (start=2, mask=00010000b, comment=GENTLEMAN)

### CBFS_PLX_1 (CAFD 000000B6) — authored by Bundang Thunder 7 Series | Series: F01,F02,F03,F04,F07

* **Passenger Enable Easy Access: testing --** by Bundang Thunder ^^**
  * Group `3000`
    * `02` (start=2, mask=00000111b, comment=EA_Hilfe)

* **Passenger seat Gentleman**
  * Group `3000`
    * `01` (start=3, mask=00010000b, comment=GENTLEMAN)


## `FDLCodes.xml`

**Modules touched:** FEM_BODY (CAFD 00000794, author unknown), IHKA (CAFD 00000A3F, author unknown), KOMBI (CAFD 000009C8, author unknown), NBT (CAFD 00000DED, author unknown)

### FEM_BODY (CAFD 00000794) — authored by unknown

* **Angel Eyes Parking Light Brightness 50%**
  * Group `3062`
    * `32` (start=68, mask=11111111b)
    * `32` (start=80, mask=11111111b)

* **Angel Eyes Parking Light Brightness 100%**
  * Group `3062`
    * `64` (start=68, mask=11111111b)
    * `64` (start=80, mask=11111111b)

* **Angel Eyes Brightness 50% Headlamp On**
  * Group `3062`
    * `32` (start=46, mask=11111111b)
    * `32` (start=57, mask=11111111b)

* **Angel Eyes Brightness 100% Headlamp On**
  * Group `3062`
    * `64` (start=46, mask=11111111b)
    * `64` (start=57, mask=11111111b)

* **Angel Eyes Brightness 50% DRL**
  * Group `3062`
    * `32` (start=90, mask=11111111b)
    * `32` (start=101, mask=11111111b)

* **Angel Eyes Brightness 100% DRL**
  * Group `3062`
    * `64` (start=90, mask=11111111b)
    * `64` (start=101, mask=11111111b)

* **Enable DRL**
  * Group `3060`
    * `TFL_S` (start=31, mask=00110000b)

* **Cornering Lights**
  * Group `3073`
    * `01` (start=218, mask=00000010b)
    * `01` (start=66, mask=00000001b)
  * Group `3066`
    * `01` (start=80, mask=00000001b)
    * `01` (start=0, mask=00000001b)
  * Group `3062`
    * `0B` (start=121, mask=00111111b)
    * `0B` (start=110, mask=00111111b)

* **Fog Lamps Welcome Light**
  * Group `3063`
    * `Soft_On` (start=55, mask=11000000b)
    * `Soft_On` (start=66, mask=11000000b)

* **Auto Start/Stop Always Off**
  * Group `3023`
    * `Aktiv` (start=0, mask=00010000b)

* **Auto Start/Stop Remember Last Setting**
  * Group `3023`
    * `Aktiv` (start=0, mask=00100000b)

* **Turn off Radio/Navigation with Opening Driver Door**
  * Group `3020`
    * `Aktiv` (start=1, mask=00000001b)

### IHKA (CAFD 00000A3F) — authored by unknown

* **AC Last Settings Memory**
  * Group `3002`
    * `Aktiv` (start=0, mask=00000010b)

* **AC Recirc Last Settings Memory**
  * Group `3002`
    * `Aktiv` (start=0, mask=00000001b)

### KOMBI (CAFD 000009C8) — authored by unknown

* **Digital Speed Display**
  * Group `3000`
    * `Aktiv` (start=1, mask=00000010b)

* **Disable Speed Correction**
  * Group `3000`
    * `Nicht_Aktiv` (start=1, mask=01000000b)

* **M Performance Logo**
  * Group `3000`
    * `01` (start=0, mask=11110000b)

* **Clock Synchronization via GPS**
  * Group `3000`
    * `Aktiv` (start=1, mask=10000000b)

### NBT (CAFD 00000DED) — authored by unknown

* **Disable Legal Disclaimer**
  * Group `3001`
    * `00` (start=58, mask=11111111b)

* **Disable Camera/PDC Legal Disclaimer**
  * Group `3001`
    * `00` (start=52, mask=11111111b)

* **Show DRL Option in iDrive**
  * Group `3000`
    * `perm_on` (start=92, mask=00011000b)

* **Sports Mode Configuration Option in iDrive (STEP 2 Go to ICM for Part 1)**
  * Group `3001`
    * `popup_and_config` (start=55, mask=00011000b)

* **Show Tire Pressure and Temperature in iDrive**
  * Group `3001`
    * `Aktiv` (start=1, mask=00100000b)
    * `02` (start=66, mask=00001100b)

* **Show Volume Popup Display**
  * Group `3002`
    * `Aktiv` (start=52, mask=01000000b)

* **Enable Route Preview**
  * Group `3000`
    * `Aktiv` (start=135, mask=00001000b)
    * `Aktiv` (start=111, mask=00001000b)

* **Enable Road Preview**
  * Group `3000`
    * `Aktiv` (start=59, mask=00100000b)

* **Enable Trip Import via USB**
  * Group `3000`
    * `Aktiv` (start=61, mask=00000001b)

* **Activate Siri Eyes-Free**
  * Group `3003`
    * `Aktiv` (start=3, mask=00001000b)

* **Enable Traffic Information via TMC**
  * Group `3000`
    * `Aktiv` (start=59, mask=00010000b)
  * Group `3002`
    * `Aktiv` (start=23, mask=00000100b)
    * `Aktiv` (start=24, mask=00000010b)
    * `Aktiv` (start=23, mask=00100000b)

* **Online Entertainment**
  * Group `3000`
    * `01` (start=10, mask=00001000b)
    * `01` (start=10, mask=00010000b)

* **Enable Import of Customer Playlists Through the Optical Drive**
  * Group `3000`
    * `01` (start=13, mask=00001000b)

* **Enable Function to Bookmark Current Playback Position of Music File From the Music Collection**
  * Group `3000`
    * `01` (start=14, mask=00000100b)

* **Enables Scaling of Album-Cover from Gracenote for Audio-CDs to full-size**
  * Group `3000`
    * `01` (start=14, mask=00100000b)

* **Gracenote Installed**
  * Group `3000`
    * `01` (start=14, mask=01000000b)

* **Gracenote via USB Enable**
  * Group `3000`
    * `01` (start=15, mask=00000010b)

* **Traffic Info Categories in the HMI enable**
  * Group `3000`
    * `01` (start=16, mask=00000010b)

* **Auto Map ZOOM enable**
  * Group `3000`
    * `01` (start=16, mask=00001000b)

* **Apple Enhancements**
  * Group `3000`
    * `01` (start=22, mask=10000000b)

* **Online Entertainment Login Speedlimit Disable**
  * Group `3000`
    * `00` (start=33, mask=10000000b)

* **Display Full Messages While Driving**
  * Group `3000`
    * `00` (start=56, mask=00001110b)
  * Group `3003`
    * `07` (start=11, mask=00000111b)

* **Enable Destination Import via USB**
  * Group `3000`
    * `01` (start=61, mask=00000100b)

* **Enable Destination Export via USB**
  * Group `3000`
    * `01` (start=61, mask=00001000b)

* **Enable MyPOI Import via USB**
  * Group `3000`
    * `01` (start=61, mask=00010000b)

* **Enable MyPOI Export via USB**
  * Group `3000`
    * `01` (start=61, mask=00100000b)

* **Map Arrow View**
  * Group `3000`
    * `01` (start=62, mask=00000100b)

* **Route Study**
  * Group `3000`
    * `01` (start=62, mask=00100000b)

* **Distance Unit Km Only**
  * Group `3000`
    * `03` (start=65, mask=01110000b)

* **Enable DVD/Video in motion**
  * Group `3000`
    * `FF` (start=71, mask=11111111b)
    * `FF` (start=72, mask=11111111b)
    * `00` (start=5, mask=00000100b)
    * `00` (start=5, mask=00010000b)
    * `00` (start=57, mask=00000111b)

* **NAVI Position menu**
  * Group `3000`
    * `01` (start=96, mask=10000000b)

* **Menu Express roads**
  * Group `3000`
    * `01` (start=108, mask=00000100b)

* **High Beam Assistant**
  * Group `3000`
    * `01` (start=109, mask=10000000b)

* **Lock/Unlock Sound Confirm Checkbox With alarm only**
  * Group `3000`
    * `01` (start=110, mask=00000001b)

* **NAVI Enable the 2 Step Guiding Advice Output**
  * Group `3000`
    * `01` (start=111, mask=00000010b)

* **NAVI Autozoom**
  * Group `3000`
    * `01` (start=111, mask=00000100b)

* **Enable NAVI Route Management**
  * Group `3000`
    * `01` (start=111, mask=00010000b)

* **Enable POI Alert**
  * Group `3000`
    * `01` (start=111, mask=10000000b)

* **Startup Animation - Black**
  * Group `3001`
    * `00` (start=62, mask=00000110b)

* **Startup Animation - Splash**
  * Group `3001`
    * `01` (start=62, mask=00000110b)

* **Startup Animation - Animation**
  * Group `3001`
    * `02` (start=62, mask=00000110b)

* **Startup Emblem BMW ConnectedDrive**
  * Group `3001`
    * `00` (start=62, mask=01111000b)

* **Startup Emblem ///M**
  * Group `3001`
    * `01` (start=62, mask=01111000b)

* **Startup Emblem Alpina**
  * Group `3001`
    * `02` (start=62, mask=01111000b)

* **Startup Emblem BMW i**
  * Group `3001`
    * `03` (start=62, mask=01111000b)

* **Startup Emblem MINI**
  * Group `3001`
    * `04` (start=62, mask=01111000b)

* **Startup Emblem RollsRoyce**
  * Group `3001`
    * `05` (start=62, mask=01111000b)

* **Startup Emblem BMW ConnectedDrive**
  * Group `3001`
    * `06` (start=62, mask=01111000b)

* **Startup Emblem BMW (smaller)**
  * Group `3001`
    * `07` (start=62, mask=01111000b)

* **Startup Emblem BMW (bigger)**
  * Group `3001`
    * `08` (start=62, mask=01111000b)

* **Startup Emblem Merry Christmas**
  * Group `3001`
    * `09` (start=62, mask=01111000b)

* **One microphone**
  * Group `3002`
    * `01` (start=55, mask=00110000b)

* **Ringtone from phone**
  * Group `3003`
    * `01` (start=6, mask=10000000b)

* **Contacts Phone/NAVI separated**
  * Group `3003`
    * `01` (start=8, mask=00000100b)

* **ringtone BMW**
  * Group `3003`
    * `00` (start=8, mask=00000011b)

* **ringtone MINI**
  * Group `3003`
    * `01` (start=8, mask=00000011b)

* **ringtone BMW i**
  * Group `3003`
    * `02` (start=8, mask=00000011b)

* **ringtone RR**
  * Group `3003`
    * `03` (start=8, mask=00000011b)

* **API USB read-write**
  * Group `3003`
    * `01` (start=22, mask=10000000b)


## `Kip_M3.xml`

**Modules touched:** ACSM (CAFD 00000909, author Kip_M3, series F080,F082), ASD01 (CAFD 00000F9B, author Kip_M3, series F080,F082), DSC (CAFD 00001a33, author Kip_M3, series F080,F082), FEM_BODY (CAFD 00000794, author Kip_M3, series F080,F082), HU_NBT2 (CAFD 00001EF6, author Kip_M3, series F080,F082), SM2 (CAFD 000000B5, author Kip_M3, series F080,F082), KAFAS2 (CAFD 00001148, author Kip_M3, series F080,F082), IHKA3 (CAFD 000016EE, author Kip_M3, series F080,F082), ICMQL (CAFD 0000067B, author Kip_M3, series F808,F082), KOMBI L7_MID (CAFD 000009C8, author Kip_M3, series F080,F082), FLE 43/44 (CAFD 000024C3, author Kip_M3, series F080,F082), REM_01 (CAFD 000007A1, author Kip_M3, series F080,F082), TMS_03 (CAFD 00001082, author Kip_M3, series F03X,F08X), TMS_03 (CAFD 00001083, author Kip_M3, series F03X,F08X)

### ACSM (CAFD 00000909) — authored by Kip_M3 | Series: F080,F082

* **Disable seatbelt reminders**
  * Group `3000`
    * `nicht_aktiv` (start=15, mask=0000010b, comment=SeatBeltReminder_SBR_Fahrer)
    * `nicht_aktiv` (start=15, mask=00000100b, comment=SeatBeltReminder_SBR_Beifahrer)
    * `nicht_aktiv` (start=16, mask=00000001b, comment=SBR_PreWarning_Fahrer)
    * `nicht_aktiv` (start=16, mask=00000010b, comment=SBR_PreWarning_Beifahrer)
    * `nicht_aktiv` (start=15, mask=0000001b, comment=Initialwarnung_GWF_IW)
    * `nicht_aktiv` (start=15, mask=00001000b, comment=Gurtzustandsanzeige_Fahrer_GWF_GZA_FA)
    * `nicht_aktiv` (start=15, mask=00010000b, comment=Gurtzustandsanzeige_Beifahrer_GWF_GZA_BF)

* **Seatbelt reminder sound duration (0 secs)**
  * Group `3001`
    * `00` (start=3, mask=11111111b, comment=GWF_SBR_WARNDAUER)

### ASD01 (CAFD 00000F9B) — authored by Kip_M3 | Series: F080,F082

* **DISABLE Active Sound Design (also need to code HU_NBT2)**
  * Group `3000`
    * `0D` (start=0, mask=11111111b, comment=Model Range)
    * `01` (start=1, mask=11111111b, comment=Model Range)

### DSC (CAFD 00001a33) — authored by Kip_M3 | Series: F080,F082

* **EURO MDM on US Spec Cars**
  * Group `3000`
    * `ECE` (start=12, mask=00000011b, comment=C_Laenderkennung)

### FEM_BODY (CAFD 00000794) — authored by Kip_M3 | Series: F080,F082

* **Radio and Navigation off when opening door**
  * Group `3020`
    * `aktiv` (start=1, mask=00000001b, comment=TCM_LOGIC_R_OFF_DOOR)

* **ENABLE Rear Tail-light with DRL (8TL). Part 1 of 2. See REM**
  * Group `3060`
    * `TFL_S` (start=31, mask=00110000b, comment=TFL_MODUS)

* **Disable Horn Honk While Locking and Engine Running**
  * Group `3040`
    * `nicht_aktiv` (start=1, mask=00100000b, comment=CLM_HORN_AT_SECURE)

* **Reduce Automatic Headlamp Sensitivity**
  * Group `3130`
    * `unempfindlich` (start=5, mask=00000111b, comment=RLS_DEF_FLC_SCHWELLWERT_SATZ)

* **Increase Soft Triple Blinker to Five (5) (EXCLUDES P3.61.x)**
  * Group `3060`
    * `04` (start=7, mask=00000111b, comment=BLINKZYKLEN_ANZAHL_TIPP)

* **Turn on brake force flashing with hard braking**
  * Group `3060`
    * `bremslicht_blinkend` (start=16, mask=00000011b, comment=ESS_AKTIVIERBARER_AUSGANG)

* **Enable parking lights**
  * Group `3060`
    * `aktiv` (start=11, mask=01000000b, comment=PARKLICHT_MOEGLICH)

* **Control ambient light level from menu (independent from cluster dimmer)**
  * Group `3070`
    * `nicht_aktiv` (start=4, mask=10000000b, comment=AMBIENTE_NACHFUEHRUNG)

* **Turn on hazard flashers at 20kmph with hard braking**
  * Group `3060`
    * `aktiv` (start=26, mask=00000001b, comment=WB_GB_ENABLE)

* **Remove trunk kick delay, don't blink upon opening**
  * Group `3040`
    * `nicht_aktiv` (start=2, mask=00000100b, comment=CLM_SMO_INDICATOR)
    * `wert_01` (start=12, mask=11111111b, comment=CLM_TIMEOUT_HK_SMO (default wert_04))

* **Remember steering wheel heat (always)**
  * Group `3040`
    * `03` (start=4, mask=00001100b, comment=NACHLAUFZEIT_LENKRADHEIZUNG)

* **Doors unlock when engine off**
  * Group `3040`
    * `aktiv` (start=1, mask=00000010b, comment=CLM_UNLOCK_KL15OFF_AFTER_PIA_AUTO_LOCK)

* **Window rolling up or down not interrupted by door opening**
  * Group `3050`
    * `nicht_aktiv` (start=0, mask=00000001b, comment=FH_Tuerauf_stop_maut)

* **Open/Close windows/mirror/roof from FOB and comfort access(open after 2 sec, close immediately)**
  * Group `3053`
    * `aktiv` (start=0, mask=01000000b, comment=KOMFORTOEFFNUNG_FB)
    * `aktiv` (start=0, mask=10000000b, comment=KOMFORTSCHLIESSUNG_FB)
    * `10` (start=8, mask=11111111b, comment=KOMFORT_OEFFNEN (default=19 2.5sec))
    * `00` (start=9, mask=11111111b, comment=KOMFORT_SCHLIESSEN (default=0F 1.6sec))
  * Group `3053`
    * `aktiv` (start=1, mask=00000010b, comment=KOMFORTSCHLIESSUNG)
    * `aktiv` (start=1, mask=00000001b, comment=KOMFORTOEFFNUNG)
    * `aktiv` (start=1, mask=00000100b, comment=KOMFORTSCHLIESSUNG_PA)

* **Enable rear fog lights (also need to code REM)**
  * Group `3060`
    * `verbaut` (start=7, mask=00001000b, comment=NSL_VERBAUT)

* **Enable illumination of exterior door handle LEDs when in reverse**
  * Group `3070`
    * `aktiv` (start=11, mask=00010000b, comment=OVT_BEI_RUECKFAHRLICHT)

* **Fold side mirrors from key fob and comfort access; unfold @ 25kmph**
  * Group `3110`
    * `aktiv` (start=0, mask=00001000b, comment=ASP_BEIKLAPPEN)
    * `aktiv` (start=1, mask=00000001b, comment=ASP_BEIKLAPPEN_BEI_KOMFORTSCHLIESSEN)
    * `aktiv` (start=8, mask=00000001b, comment=ASP_AUSKLAPPEN_NACH_KOMFORTSCHLIESSEN)
    * `19` (start=10, mask=11111111b, comment=ASP_GESCHWINDIGKEIT_AUTO_AUSKLAPPEN (default=28))

* **Tilt passenger mirror farther down when in reverse**
  * Group `3110`
    * `5A` (start=2, mask=11111111b, comment=ASP_BORDSTEINAUTOMATIK_DELTA (default=3B))

* **F3x and F8x NGHB. Step 3 of 3. Also code LHM43/44.**
  * Group `3073`
    * `00, 00, 00, 15, 00, 00, 0A, 15, 1F` (start=176, end=184, mask=11111111b, comment=NGHB PDF Step 3)
  * Group `3074`
    * `2E, 3B, 00, 00, 00, 00` (start=81, end=86, mask=11111111b, comment=NGHB PDF Step 3)
    * `2E, 3B, 00, 00, 00, 00` (start=87, end=92, mask=11111111b, comment=NGHB PDF Step 3)
    * `00, 00, 00, 00, 00, 00` (start=93, end=98, mask=11111111b, comment=NGHB PDF Step 3)
    * `00, 00, 00, 00, 00, 00` (start=99, end=104, mask=11111111b, comment=NGHB PDF Step 3)
    * `27` (start=60, mask=11111111b, comment=P3.59 improvement)
    * `1F` (start=61, mask=11111111b, comment=P3.59 improvement)
    * `E1` (start=63, mask=11111111b, comment=P3.59 improvement)

### HU_NBT2 (CAFD 00001EF6) — authored by Kip_M3 | Series: F080,F082

* **Enable video files from USB**
  * Group `3000`
    * `aktiv` (start=15, mask=00010000b, comment=ENT_CODEC_OGG)
    * `aktiv` (start=15, mask=00100000b, comment=ENT_CODEC_XVID)
    * `aktiv` (start=15, mask=01000000b, comment=ENT_CODEC_XVCD)

* ****
  * Group `3006`
    * `aktiv` (start=2, mask=00100000b, comment=NAVI_FUELSTOP_PROPOSAL)

* **Disable Active Sound Design**
  * Group `3009`
    * `aktiv` (start=1, mask=00000010b, comment=ASD_SOUND_OFF)

* **Enable B and O Sound**
  * Group `3000`
    * `03` (start=57, mask=00110000b, comment=HIGH_END_AUDIO_MENUE)

* **Enable Logic7 Sound**
  * Group `3000`
    * `00` (start=57, mask=00110000b, comment=HIGH_END_AUDIO_MENUE)

* **Enable Enhanced Bluetooth and Contact Pics**
  * Group `3003`
    * `aktiv` (start=3, mask=00010000b, comment=TWO_PHONES_PARALLEL)
    * `aktiv` (start=8, mask=00100000b, comment=CONTACT_BOOK_PICTURES)
    * `aktiv` (start=10, mask=00000001b, comment=BLUETOOTH_2ND_HFP)
    * `aktiv` (start=10, mask=00001000b, comment=MACRO_PIM)
    * `aktiv` (start=19, mask=00100000b, comment=PIM_BILDER_EIN_AUS)

* **Enable whole text messages**
  * Group `3003`
    * `Whole_Text` (start=11, mask=00000111b, comment=PIM_DRIVING_TEXT_LENGTH)
  * Group `3000`
    * `whole_text` (start=31, mask=00011100b, comment=SPEEDLOCK_TEXT_LENGTH)
    * `whole_text` (start=137, mask=00011100b, comment=MYINFO_DRIVING_TEXT_LENGTH)
    * `whole_text` (start=137, mask=11100000b, comment=AKD_DRIVING_TEXT_LENGTH)
    * `whole_text` (start=138, mask=00000111b, comment=BMWINFO_DRIVING_TEXT_LENGTH)

* **Disable speed lock for Owner’s Manual, Bluetooth Pairing, Touchpad, DVD, Tuner and messages**
  * Group `3000`
    * `nicht_aktiv` (start=0, mask=00100000b, comment=SL06_IBA_1)
    * `nicht_aktiv` (start=0, mask=01000000b, comment=SL07_IBA_2)
    * `nicht_aktiv` (start=1, mask=10000000b, comment=SL16_ADD_CEDEVICE)
    * `nicht_aktiv` (start=2, mask=00010000b, comment=SL21_IBA_3)
    * `none` (start=2, mask=00000111b, comment=VIDEO_SPEEDLOCK_CONDITION)
    * `nicht_aktiv` (start=5, mask=00000100b, comment=VIDEO_HANDBRAKE)
    * `nicht_aktiv` (start=5, mask=00010000b, comment=VIDEO_FRONT_LOCKED)
    * `none_locked` (start=31, mask=00000111b, comment=SPEEDLOCK_SPELLER_INPUT)
    * `whole_text` (start=31, mask=00111000b, comment=SPEEDLOCK_TEXT_LENGTH)
    * `nicht_aktiv` (start=32, mask=00000100b, comment=SPEEDLOCK_IBA_ACCESS_CCM)
    * `nicht_aktiv` (start=32, mask=00001000b, comment=SPEEDLOCK_IBA_SHORT)
    * `nicht_aktiv` (start=109, mask=00000001b, comment=SPEEDLOCK_HMI_TUNER)
    * `none` (start=136, mask=00111000b, comment=OFFICE_MESSAGES_SPEEDLOCK_CONDITION)
    * `whole_text` (start=137, mask=00011100b, comment=MYINFO_DRIVING_TEXT_LENGTH)
    * `whole_text` (start=137, mask=11100000b, comment=AKD_DRIVING_TEXT_LENGTH)
    * `whole_text` (start=138, mask=00000111b, comment=BMWINFO_DRIVING_TEXT_LENGTH)
    * `nicht_aktiv` (start=146, mask=00011111b, comment=SPEEDLOCK_SPEEDVALUE_MIN)
    * `nicht_aktiv` (start=147, mask=00111111b, comment=SPEEDLOCK_SPEEDVALUE_MAX)

* **Remove legal disclaimers**
  * Group `3001`
    * `kein_ld` (start=52, mask=11111111b, comment=MACRO_CAM_LEGALDISCLAIMER)
    * `kein_ld` (start=58, mask=11111111b, comment=LEGAL_DISCLAIMER_TIME)

* **Allow media volume to be retained up to 35% (default 25%)**
  * Group `3002`
    * `23` (start=3, mask=11111111b, comment=VOL_MAX_ON)

### SM2 (CAFD 000000B5) — authored by Kip_M3 | Series: F080,F082

* **Enable seat heating memory infinity**
  * Group `3000`
    * `03` (start=4, mask=00000011b, comment=SA_MEMORY_ZEIT)

### KAFAS2 (CAFD 00001148) — authored by Kip_M3 | Series: F080,F082

* **Enable detection of grass/curb road edge**
  * Group `3020`
    * `detection_for_grass_edge_and_curb_stone` (start=2, mask=00000011b, comment=ROAD_EDGE_WARNING_ENABLED)

### IHKA3 (CAFD 000016EE) — authored by Kip_M3 | Series: F080,F082

* **Disable AC from turning ON if Auto Button is pressed**
  * Group `3003`
    * `nicht_aktiv` (start=0, mask=00000100b, comment=AC_ON_WITH_AUTO)

### ICMQL (CAFD 0000067B) — authored by Kip_M3 | Series: F808,F082

* **Enable speed limiter (also need to code KOMBI)**
  * Group `3000`
    * `aktiv` (start=173, mask=00000001b, comment=C_SLD_Funktion)
    * `zugelassen` (start=197, mask=11100000b, comment=C_Umschaltung_ACC_DCC)

### KOMBI L7_MID (CAFD 000009C8) — authored by Kip_M3 | Series: F080,F082

* **Enable speed limiter (also need to code ICM)**
  * Group `3003`
    * `aktiv` (start=3, mask=00000001b, comment=SLD_ENABLE)

### FLE 43/44 (CAFD 000024C3) — authored by Kip_M3 | Series: F080,F082

* **F080,F082 - No Amber Enable GFHB/antidazzle high beams - Euro settings**
  * Group `3000`
    * `01_Value` (start=4, mask=11110000b, comment=HlPrjLabel_HIType)
  * Group `3003`
    * `07_Value` (start=0, end=9, mask=11111111b, comment=SchlechtWetter_C1_Idx)
    * `07_Value` (start=10, end=19, mask=11111111b, comment=SchlechtWetter_C2_Idx)
    * `07_Value` (start=20, end=29, mask=11111111b, comment=Stadt_V_Idx)
    * `07_Value` (start=30, end=39, mask=11111111b, comment=SAE_Idx)
    * `07_Value` (start=40, end=49, mask=11111111b, comment=H10_Landstrasse_C_Idx)
    * `07_Value` (start=50, end=59, mask=11111111b, comment=H8_Autobahn_E3_Idx)
    * `07_Value` (start=60, end=69, mask=11111111b, comment=H6_Autobahn_E2_Idx)
    * `07_Value` (start=70, end=79, mask=11111111b, comment=H5_Autobahn_E1_Idx)
    * `07_Value` (start=80, end=89, mask=11111111b, comment=H4_Autobahn_E_Idx)
    * `08_Value` (start=90, end=99, mask=11111111b, comment=H_2_Idx)
    * `08_Value` (start=100, end=109, mask=11111111b, comment=H_0_Idx)
    * `07_Value` (start=110, end=119, mask=11111111b, comment=H_Plus2_Idx)
    * `08_Value` (start=120, end=129, mask=11111111b, comment=H_Plus4_Idx)
    * `10_Value` (start=130, end=139, mask=11111111b, comment=Blendfreies_Fernlicht_Idx)
    * `09_Value` (start=140, end=149, mask=11111111b, comment=Volles_Fernlicht__Lichthupe_Idx)
  * Group `3004`
    * `08_Value` (start=0, end=9, mask=11111111b, comment=DRL_Idx)
    * `00, 00, 00, 04, 00, 00, 08, 00, 00, 00` (start=10, end=19, mask=11111111b, comment=POLI1_Idx)
    * `00, 00, 00, 04, 00, 00, 08, 00, 00, 00` (start=20, end=29, mask=11111111b, comment=POLI2_Idx)
    * `00, 00, 00, 04, 00, 00, 08, 00, 00, 00` (start=30, end=39, mask=11111111b, comment=POLI3_IDX)
    * `10_Value` (start=40, end=49, mask=11111111b, comment=PLI_Idx)
    * `00, 09, 09, 04, 00, 00, 0A, 00, 00, 00` (start=60, end=69, mask=11111111b, comment=WELL1_Idx)
    * `00, 00, 00, 04, 00, 00, 0B, 00, 00, 00` (start=70, end=79, mask=11111111b, comment=WELL2_Idx)
    * `00, 00, 00, 04, 00, 00, 0B, 00, 00, 00` (start=80, end=89, mask=11111111b, comment=WELL3_Idx)
    * `00, 00, 00, 04, 00, 00, 0B, 00, 00, 00` (start=90, end=99, mask=11111111b, comment=WELL4_IDX)
    * `00, 02, 02, 04, 00, 00, 0B, 00, 00, 00` (start=100, end=109, mask=11111111b, comment=FMH_Idx)
    * `00, 02, 02, 04, 00, 00, 0B, 00, 00, 00` (start=110, end=119, mask=11111111b, comment=REMLI_Idx)
    * `11_Value` (start=120, end=129, mask=11111111b, comment=HBBLINK_Idx)
    * `07_Value` (start=130, end=139, mask=11111111b, comment=DWABLINK_Idx)
    * `07_Value` (start=140, end=149, mask=11111111b, comment=PanicMode_Idx)
    * `11_Value` (start=150, end=159, mask=11111111b, comment=RaidAlarm_Idx)
    * `10_Value` (start=160, end=169, mask=11111111b, comment=Blinken_Idx)
    * `00, 00, 00, 04, 00, 00, 00, 00, 00, 00` (start=180, end=189, mask=11111111b, comment=SIDEMRKLGT_Idx)
    * `10_Value` (start=190, end=199, mask=11111111b, comment=BLINKEN_PO_Idx)
  * Group `3005`
    * `04_Value` (start=4, mask=11111111b, comment=LmmIdx01_Intensity)
    * `01_Value` (start=7, mask=01000000b, comment=LmmIdx01_ErrorImpact)
    * `02_Value` (start=9, mask=11111111b, comment=LmmIdx02_TimeOn)
    * `02_Value` (start=10, mask=11111111b, comment=LmmIdx02_TimeOff)
    * `03_Value` (start=11, mask=00001111b, comment=LmmIdx02_Priority)
    * `01_Value` (start=11, mask=01000000b, comment=LmmIdx02_ErrorImpact)
    * `04_Value` (start=12, mask=11111111b, comment=LmmIdx03_Intensity)
    * `02_Value` (start=13, mask=11111111b, comment=LmmIdx03_TimeOn)
    * `02_Value` (start=14, mask=11111111b, comment=LmmIdx03_TimeOff)
    * `05_Value` (start=15, mask=00001111b, comment=LmmIdx03_Priority)
    * `03_Value` (start=16, mask=11111111b, comment=LmmIdx04_Intensity)
    * `03_Value` (start=17, mask=11111111b, comment=LmmIdx04_TimeOn)
    * `03_Value` (start=18, mask=11111111b, comment=LmmIdx04_TimeOff)
    * `04_Value` (start=19, mask=00001111b, comment=LmmIdx04_Priority)
    * `03_Value` (start=20, mask=11111111b, comment=LmmIdx05_Intensity)
    * `03_Value` (start=21, mask=11111111b, comment=LmmIdx05_TimeOn)
    * `03_Value` (start=22, mask=11111111b, comment=LmmIdx05_TimeOff)
    * `01_Value` (start=23, mask=00001111b, comment=LmmIdx05_Priority)
    * `03_Value` (start=24, mask=11111111b, comment=LmmIdx06_Intensity)
    * `01_Value` (start=25, mask=11111111b, comment=LmmIdx06_TimeOn)
    * `03_Value` (start=26, mask=11111111b, comment=LmmIdx06_TimeOff)
    * `06_Value` (start=27, mask=00001111b, comment=LmmIdx06_Priority)
    * `02_Value` (start=27, mask=00110000b, comment=LmmIdx06_RampType)
    * `01_Value` (start=27, mask=01000000b, comment=LmmIdx06_ErrorImpact)
    * `03_Value` (start=28, mask=11111111b, comment=LmmIdx07_Intensity)
    * `06_Value` (start=31, mask=00001111b, comment=LmmIdx07_Priority)
    * `02_Value` (start=31, mask=00110000b, comment=LmmIdx07_RampType)
    * `03_Value` (start=35, mask=00001111b, comment=LmmIdx08_Priority)
    * `05_Value` (start=39, mask=00001111b, comment=LmmIdx09_Priority)
    * `02_Value` (start=39, mask=00110000b, comment=LmmIdx09_RampType)
    * `02_Value` (start=40, mask=11111111b, comment=LmmIdx10_Intensity)
    * `02_Value` (start=43, mask=00001111b, comment=LmmIdx10_Priority)
    * `02_Value` (start=43, mask=00110000b, comment=LmmIdx10_RampType)
    * `03_Value` (start=44, mask=11111111b, comment=LmmIdx11_Intensity)
    * `04_Value` (start=47, mask=00001111b, comment=LmmIdx11_Priority)
    * `03_Value` (start=48, mask=11111111b, comment=LmmIdx12_Intensity)
    * `04_Value` (start=51, mask=00001111b, comment=LmmIdx12_Priority)
    * `03_Value` (start=134, mask=00111111b, comment=LmmReLut_LgtFct0)
    * `03_Value` (start=134, mask=11000000b, comment=LmmReLut_LogLmpLow0)
    * `02_Value` (start=135, mask=11111100b, comment=LmmReLut_Idx0)
    * `03_Value` (start=136, mask=00111111b, comment=LmmReLut_LgtFct1)
    * `03_Value` (start=136, mask=11000000b, comment=LmmReLut_LogLmpLow1)
    * `02_Value` (start=137, mask=11111100b, comment=LmmReLut_Idx1)
    * `03_Value` (start=138, mask=00111111b, comment=LmmReLut_LgtFct2)
    * `03_Value` (start=138, mask=11000000b, comment=LmmReLut_LogLmpLow2)
    * `02_Value` (start=139, mask=11111100b, comment=LmmReLut_Idx2)

* **F080,F082 - Enable GFHB and Ambers/antidazzle high beams - Euro settings**
  * Group `3000`
    * `01_Value` (start=4, mask=11110000b, comment=HlPrjLabel_HIType)
  * Group `3003`
    * `07_Value` (start=0, end=9, mask=11111111b, comment=SchlechtWetter_C1_Idx)
    * `07_Value` (start=10, end=19, mask=11111111b, comment=SchlechtWetter_C2_Idx)
    * `07_Value` (start=20, end=29, mask=11111111b, comment=Stadt_V_Idx)
    * `07_Value` (start=30, end=39, mask=11111111b, comment=SAE_Idx)
    * `07_Value` (start=40, end=49, mask=11111111b, comment=H10_Landstrasse_C_Idx)
    * `07_Value` (start=50, end=59, mask=11111111b, comment=H8_Autobahn_E3_Idx)
    * `07_Value` (start=60, end=69, mask=11111111b, comment=H6_Autobahn_E2_Idx)
    * `07_Value` (start=70, end=79, mask=11111111b, comment=H5_Autobahn_E1_Idx)
    * `07_Value` (start=80, end=89, mask=11111111b, comment=H4_Autobahn_E_Idx)
    * `08_Value` (start=90, end=99, mask=11111111b, comment=H_2_Idx)
    * `08_Value` (start=100, end=109, mask=11111111b, comment=H_0_Idx)
    * `07_Value` (start=110, end=119, mask=11111111b, comment=H_Plus2_Idx)
    * `08_Value` (start=120, end=129, mask=11111111b, comment=H_Plus4_Idx)
    * `10_Value` (start=130, end=139, mask=11111111b, comment=Blendfreies_Fernlicht_Idx)
    * `09_Value` (start=140, end=149, mask=11111111b, comment=Volles_Fernlicht__Lichthupe_Idx)
  * Group `3004`
    * `08_Value` (start=0, end=9, mask=11111111b, comment=DRL_Idx)
    * `00, 00, 00, 0C, 00, 00, 08, 00, 00, 00` (start=10, end=19, mask=11111111b, comment=POLI1_Idx)
    * `00, 00, 00, 0C, 00, 00, 08, 00, 00, 00` (start=20, end=29, mask=11111111b, comment=POLI2_Idx)
    * `00, 00, 00, 0C, 00, 00, 08, 00, 00, 00` (start=30, end=39, mask=11111111b, comment=POLI3_IDX)
    * `10_Value` (start=40, end=49, mask=11111111b, comment=PLI_Idx)
    * `00, 09, 09, 0C, 00, 00, 0A, 00, 00, 00` (start=60, end=69, mask=11111111b, comment=WELL1_Idx)
    * `00, 00, 00, 0C, 00, 00, 0B, 00, 00, 00` (start=70, end=79, mask=11111111b, comment=WELL2_Idx)
    * `00, 00, 00, 0C, 00, 00, 0B, 00, 00, 00` (start=80, end=89, mask=11111111b, comment=WELL3_Idx)
    * `00, 00, 00, 0C, 00, 00, 0B, 00, 00, 00` (start=90, end=99, mask=11111111b, comment=WELL4_IDX)
    * `00, 02, 02, 0C, 00, 00, 0B, 00, 00, 00` (start=100, end=109, mask=11111111b, comment=FMH_Idx)
    * `00, 02, 02, 0C, 00, 00, 0B, 00, 00, 00` (start=110, end=119, mask=11111111b, comment=REMLI_Idx)
    * `11_Value` (start=120, end=129, mask=11111111b, comment=HBBLINK_Idx)
    * `07_Value` (start=130, end=139, mask=11111111b, comment=DWABLINK_Idx)
    * `07_Value` (start=140, end=149, mask=11111111b, comment=PanicMode_Idx)
    * `11_Value` (start=150, end=159, mask=11111111b, comment=RaidAlarm_Idx)
    * `10_Value` (start=160, end=169, mask=11111111b, comment=Blinken_Idx)
    * `00, 00, 00, 0C, 00, 00, 00, 00, 00, 00` (start=180, end=189, mask=11111111b, comment=SIDEMRKLGT_Idx)
    * `10_Value` (start=190, end=199, mask=11111111b, comment=BLINKEN_PO_Idx)
  * Group `3005`
    * `04_Value` (start=4, mask=11111111b, comment=LmmIdx01_Intensity)
    * `01_Value` (start=7, mask=01000000b, comment=LmmIdx01_ErrorImpact)
    * `02_Value` (start=9, mask=11111111b, comment=LmmIdx02_TimeOn)
    * `02_Value` (start=10, mask=11111111b, comment=LmmIdx02_TimeOff)
    * `03_Value` (start=11, mask=00001111b, comment=LmmIdx02_Priority)
    * `01_Value` (start=11, mask=01000000b, comment=LmmIdx02_ErrorImpact)
    * `04_Value` (start=12, mask=11111111b, comment=LmmIdx03_Intensity)
    * `02_Value` (start=13, mask=11111111b, comment=LmmIdx03_TimeOn)
    * `02_Value` (start=14, mask=11111111b, comment=LmmIdx03_TimeOff)
    * `05_Value` (start=15, mask=00001111b, comment=LmmIdx03_Priority)
    * `03_Value` (start=16, mask=11111111b, comment=LmmIdx04_Intensity)
    * `03_Value` (start=17, mask=11111111b, comment=LmmIdx04_TimeOn)
    * `03_Value` (start=18, mask=11111111b, comment=LmmIdx04_TimeOff)
    * `04_Value` (start=19, mask=00001111b, comment=LmmIdx04_Priority)
    * `03_Value` (start=20, mask=11111111b, comment=LmmIdx05_Intensity)
    * `03_Value` (start=21, mask=11111111b, comment=LmmIdx05_TimeOn)
    * `03_Value` (start=22, mask=11111111b, comment=LmmIdx05_TimeOff)
    * `01_Value` (start=23, mask=00001111b, comment=LmmIdx05_Priority)
    * `03_Value` (start=24, mask=11111111b, comment=LmmIdx06_Intensity)
    * `01_Value` (start=25, mask=11111111b, comment=LmmIdx06_TimeOn)
    * `03_Value` (start=26, mask=11111111b, comment=LmmIdx06_TimeOff)
    * `06_Value` (start=27, mask=00001111b, comment=LmmIdx06_Priority)
    * `02_Value` (start=27, mask=00110000b, comment=LmmIdx06_RampType)
    * `01_Value` (start=27, mask=01000000b, comment=LmmIdx06_ErrorImpact)
    * `03_Value` (start=28, mask=11111111b, comment=LmmIdx07_Intensity)
    * `06_Value` (start=31, mask=00001111b, comment=LmmIdx07_Priority)
    * `02_Value` (start=31, mask=00110000b, comment=LmmIdx07_RampType)
    * `03_Value` (start=35, mask=00001111b, comment=LmmIdx08_Priority)
    * `05_Value` (start=39, mask=00001111b, comment=LmmIdx09_Priority)
    * `02_Value` (start=39, mask=00110000b, comment=LmmIdx09_RampType)
    * `02_Value` (start=40, mask=11111111b, comment=LmmIdx10_Intensity)
    * `02_Value` (start=43, mask=00001111b, comment=LmmIdx10_Priority)
    * `02_Value` (start=43, mask=00110000b, comment=LmmIdx10_RampType)
    * `03_Value` (start=44, mask=11111111b, comment=LmmIdx11_Intensity)
    * `04_Value` (start=47, mask=00001111b, comment=LmmIdx11_Priority)
    * `03_Value` (start=48, mask=11111111b, comment=LmmIdx12_Intensity)
    * `04_Value` (start=51, mask=00001111b, comment=LmmIdx12_Priority)
    * `03_Value` (start=134, mask=00111111b, comment=LmmReLut_LgtFct0)
    * `03_Value` (start=134, mask=11000000b, comment=LmmReLut_LogLmpLow0)
    * `02_Value` (start=135, mask=11111100b, comment=LmmReLut_Idx0)
    * `03_Value` (start=136, mask=00111111b, comment=LmmReLut_LgtFct1)
    * `03_Value` (start=136, mask=11000000b, comment=LmmReLut_LogLmpLow1)
    * `02_Value` (start=137, mask=11111100b, comment=LmmReLut_Idx1)
    * `03_Value` (start=138, mask=00111111b, comment=LmmReLut_LgtFct2)
    * `03_Value` (start=138, mask=11000000b, comment=LmmReLut_LogLmpLow2)
    * `02_Value` (start=139, mask=11111100b, comment=LmmReLut_Idx2)

### REM_01 (CAFD 000007A1) — authored by Kip_M3 | Series: F080,F082

* **ENABLE REAR windows roll up while doors opened**
  * Group `3050`
    * `nicht_aktiv` (start=0, mask=00000001b, comment=FH_TUERAUF_STOP_MAUT)

* **ENABLE Outer Light Flashing with EU Brake Force - LED Only**
  * Group `3062`
    * `bl_l` (start=110, mask=00111111b, comment=MAPPING_BRAKEFORCED_L_OUTPUT)
    * `bl_r` (start=120, mask=00111111b, comment=MAPPING_BRAKEFORCED_R_OUTPUT)

* **Increase Outer Light Flashing with EU Brake Force - LED Only**
  * Group `3064`
    * `05` (start=17, mask=00001110b, comment=ESS_BLINKFREQ_1)
    * `05` (start=17, mask=01110000b, comment=ESS_BLINKFREQ_2)

* **Rear Fog: Enable Both Lamps (also need to code FEM)**
  * Group `3063`
    * `1C` (start=40, mask=00111111b, comment=Mapping_Nebelschlussl_L_output)
    * `1D` (start=50, mask=00111111b, comment=Mapping_Nebelschlussl_R_output)

### TMS_03 (CAFD 00001082) — authored by Kip_M3 | Series: F03X,F08X

* **Turn sidemarker LEDs OFF - Driver side. Step 1 of 2(need to test)**
  * Group `3005`
    * `00, 03, 00, 00, 00, 03, 00, 00, 64, 03, 00, 00, 2B, 04, 00, 00` (start=16, end=31, mask=11111111b, comment=Turn sidemarker LEDs OFF)
    * `00, 03, 00, 00, 00, 03, 00, 00, 64, 03, 00, 00, 2B, 04, 00, 00` (start=32, end=47, mask=11111111b, comment=Turn sidemarker LEDs OFF)
    * `00, 03, 00, 00, 00, 03, 00, 00, 64, 03, 00, 00, 2E, 04, 00, 00` (start=80, end=95, mask=11111111b, comment=Turn sidemarker LEDs OFF)

* **Turn sidemarker LEDs ON - Driver side. Step 1 of 2(need to test)**
  * Group `3005`
    * `00, 03, 00, 00, 64, 03, 00, 00, 64, 03, 00, 00, 2B, 04, 00, 00` (start=16, end=31, mask=11111111b, comment=Turn sidemarker LEDs ON)
    * `00, 03, 00, 00, 64, 03, 00, 00, 64, 03, 00, 00, 2B, 04, 00, 00` (start=32, end=47, mask=11111111b, comment=Turn sidemarker LEDs ON)
    * `00, 03, 00, 00, 64, 03, 00, 00, 64, 03, 00, 00, 2E, 04, 00, 00` (start=80, end=95, mask=11111111b, comment=Turn sidemarker LEDs ON)

### TMS_03 (CAFD 00001083) — authored by Kip_M3 | Series: F03X,F08X

* **Turn sidemarker LEDs OFF - Passenger side. Step 2 of 2(need to test)**
  * Group `3005`
    * `00, 03, 00, 00, 00, 03, 00, 00, 64, 03, 00, 00, 2B, 04, 00, 00` (start=16, end=31, mask=11111111b, comment=Turn sidemarker LEDs OFF)
    * `00, 03, 00, 00, 00, 03, 00, 00, 64, 03, 00, 00, 2B, 04, 00, 00` (start=32, end=47, mask=11111111b, comment=Turn sidemarker LEDs OFF)
    * `00, 03, 00, 00, 00, 03, 00, 00, 64, 03, 00, 00, 2E, 04, 00, 00` (start=80, end=95, mask=11111111b, comment=Turn sidemarker LEDs OFF)

* **Turn sidemarker LEDs ON - Passenger side. Step 2 of 2(need to test)**
  * Group `3005`
    * `00, 03, 00, 00, 64, 03, 00, 00, 64, 03, 00, 00, 2B, 04, 00, 00` (start=16, end=31, mask=11111111b, comment=Turn sidemarker LEDs ON)
    * `00, 03, 00, 00, 64, 03, 00, 00, 64, 03, 00, 00, 2B, 04, 00, 00` (start=32, end=47, mask=11111111b, comment=Turn sidemarker LEDs ON)
    * `00, 03, 00, 00, 64, 03, 00, 00, 64, 03, 00, 00, 2E, 04, 00, 00` (start=80, end=95, mask=11111111b, comment=Turn sidemarker LEDs ON)


## `PerryGunn.xml`

**Modules touched:** CAS_04 (CAFD 0000000F, author PerryGunn, series F025)

### CAS_04 (CAFD 0000000F) — authored by PerryGunn | Series: F025

* **Unlock/open the tailgate from fob only if the vehicle is unlocked**
  * Group `3002`
    * `aktiv` (start=9, mask=00010000b, comment=HK_GESPERRT_IN_GESICHERT)

* **Unlock/open the tailgate from fob if the vehicle is locked or unlocked**
  * Group `3002`
    * `nicht_aktiv` (start=9, mask=00010000b, comment=HK_GESPERRT_IN_GESICHERT)


## `SergAA.xml`

**Modules touched:** DKOMBI 6WB (CAFD 00001060, author SergAA, series F010), CAS_04 (CAFD 0000000F, author SergAA, series F010), DME DDE (CAFD 000001A7, author SergAA, series F010), IHKA (CAFD 00000092, author SergAA, series F010), KAFAS2 (CAFD 00001148, author SergAA, series F010), Night Vision 2 (CAFD 0000004C, author SergAA, series F010), ACSM (CAFD 00000909, author SergAA, series F010), FRM (CAFD 0000106D, author SergAA, series F010)

### DKOMBI 6WB (CAFD 00001060) — authored by SergAA | Series: F010

* **Startup screen - BMW (standard)**
  * Group `3000`
    * `00` (start=44, mask=00001111b)

* **Startup screen - M**
  * Group `3000`
    * `01` (start=44, mask=00001111b)

* **Startup screen - BMW i**
  * Group `3000`
    * `03` (start=44, mask=00001111b)

* **Startup screen - X5M**
  * Group `3000`
    * `08` (start=44, mask=00001111b)

* **Startup screen - X6M**
  * Group `3000`
    * `09` (start=44, mask=00001111b)

* **ECO Pro sailing display**
  * Group `3003`
    * `01` (start=4, mask=00010000b)

* **Entertainment display in HUD**
  * Group `3003`
    * `01` (start=10, mask=00000001b)

* **HorsePower display on**
  * Group `3003`
    * `01` (start=11, mask=00000010b)

### CAS_04 (CAFD 0000000F) — authored by SergAA | Series: F010

* **Start Stop - default OFF**
  * Group `3000`
    * `01` (start=3, mask=00010000b)

* **Start Stop - memory**
  * Group `3000`
    * `01` (start=3, mask=00100000b)

### DME DDE (CAFD 000001A7) — authored by SergAA | Series: F010

* **Recuperation off - always charge**
  * Group `3701`
    * `00` (start=2, mask=00000001b)

### IHKA (CAFD 00000092) — authored by SergAA | Series: F010

* **Use webasto as additional heater (by default it stops after engine on)**
  * Group `3000`
    * `01` (start=1, mask=00010000b)

### KAFAS2 (CAFD 00001148) — authored by SergAA | Series: F010

* **Detect Road mark (Painted lane markings) + Detect grass and road sides**
  * Group `3020`
    * `02` (start=1, mask=00000011b)

* **Enable High Beam Assistant FLA**
  * Group `3050`
    * `01` (start=0, mask=00000001b)

* **Enable High Beam GlareFree**
  * Group `3050`
    * `01` (start=0, mask=10000000b)

* **Lanes if system is on, arrows side dependant on. No yellow status.**
  * Group `3020`
    * `02` (start=1, mask=11110000b)

### Night Vision 2 (CAFD 0000004C) — authored by SergAA | Series: F010

* **Enable backgroup pedestrian detection**
  * Group `3000`
    * `5F` (start=20, mask=01111111b)
  * Group `3250`
    * `01` (start=0, mask=00010000b)
    * `01` (start=0, mask=10000000b)
  * Group `3252`
    * `01` (start=0, mask=00000001b)
  * Group `3253`
    * `01` (start=50, mask=00100000b)
  * Group `3240`
    * `FF` (start=21, mask=11111111b)

### ACSM (CAFD 00000909) — authored by SergAA | Series: F010

* **Disable initial seatbelt warning**
  * Group `3000`
    * `01` (start=15, mask=00000001b)

### FRM (CAFD 0000106D) — authored by SergAA | Series: F010

* **Set High Beam Assistant Default to Automatic on**
  * Group `3050`
    * `01` (start=20, mask=00100000b)


## `TMD29.xml`

**Modules touched:** REM_01 (CAFD 000007A1, author TMD29)

### REM_01 (CAFD 000007A1) — authored by TMD29

* **Disable Seat belt Assist (Driver Side)**
  * Group `3130`
    * `nicht_aktiv` (start=4, mask=00001000b)

* **Enable Seat belt Assist (Driver Side Default)**
  * Group `3130`
    * `aktiv` (start=4, mask=00001000b)

* **Disable Seat belt Assist (Passenger Side)**
  * Group `3130`
    * `nicht_aktiv` (start=4, mask=00010000b)

* **Enable Seat belt Assist (Passenger Side Default)**
  * Group `3130`
    * `aktiv` (start=4, mask=00010000b)


## `aboulfad.xml`

**Modules touched:** DSC (CAFD 00001A33, author aboulfad, series F030), DSC (CAFD 00001A33, author aboulfad, series F030)

### DSC (CAFD 00001A33) — authored by aboulfad | Series: F030

* **Euro MDM: Euro Coding for US Spec Cars**
  * Group `3000`
    * `00` (start=12, mask=00000011b)

### DSC (CAFD 00001A33) — authored by aboulfad | Series: F030

* **US MDM: Original Coding for US Spec Cars**
  * Group `3000`
    * `01` (start=12, mask=00000011b)


## `aknight720.xml`

**Modules touched:** HU_CICHB (CAFD 000000F9, author aknight720)

### HU_CICHB (CAFD 000000F9) — authored by aknight720

* **FDL Code EBT 6NL**
  * Group `3000`
    * `nicht_aktiv` (start=03, mask=01000000b)
    * `nicht_aktiv` (start=04, mask=00000001b)
    * `aktiv` (start=07, mask=00000010b)
    * `aktiv` (start=18, mask=00000010b)
    * `aktiv` (start=22, mask=00100000b)
    * `browser` (start=49, mask=00100000b)
    * `nicht_aktiv` (start=56, mask=01000000b)
    * `nicht_aktiv` (start=61, mask=00010000b)
  * Group `3002`
    * `aktiv` (start=02, mask=00000001b)
  * Group `3003`
    * `aktiv` (start=02, mask=01000000b)
    * `combox` (start=03, mask=11100000b)
    * `aktiv` (start=20, mask=00010000b)
    * `aktiv` (start=20, mask=00100000b)
    * `aktiv` (start=20, mask=10000000b)
    * `nicht_aktiv` (start=22, mask=00000001b)
    * `aktiv` (start=23, mask=01000000b)
    * `aktiv` (start=23, mask=00000010b)
  * Group `3004`
    * `aktiv` (start=02, mask=00000100b)
    * `aktiv` (start=06, mask=00000001b)
    * `aktiv` (start=10, mask=10000000b)


## `dmnc02.xml`

**Modules touched:** FEM_BODY (CAFD 00000794, author dmnc02), LHM (CAFD 0000010BA, author dmnc02), LHM (CAFD 0000016BF, author dmnc02), TMS (CAFD 000001082, author dmnc02), TMS (CAFD 000001083, author dmnc02)

### FEM_BODY (CAFD 00000794) — authored by dmnc02

* **No-Glare High Beam Assistant (Step 3)**
  * Group `3073`
    * `00, 00, 00, 15, 00, 00, 0A, 15, 1F` (start=176, end=184, mask=11111111b)
  * Group `3074`
    * `2E, 3B, 00, 00, 00, 00` (start=81, end=86, mask=11111111b)
    * `2E, 3B, 00, 00, 00, 00` (start=87, end=92, mask=11111111b)
    * `00, 00, 00, 00, 00, 00` (start=93, end=98, mask=11111111b)
    * `00, 00, 00, 00, 00, 00` (start=99, end=104, mask=11111111b)

### LHM (CAFD 0000010BA) — authored by dmnc02

* **No-Glare High Beam Assistant (Step 2: driver side)**
  * Group `3000`
    * `FA, 64, 00, 00, FA, FA, 00` (start=0, end=6, mask=11111111b)
    * `FA, 64, 00, 00, FA, FA, 00` (start=7, end=13, mask=11111111b)
    * `FA, 00, 00, 19, FA, FA, 00` (start=14, end=20, mask=11111111b)
    * `FA, 00, 00, 00, C8, C8, 00` (start=21, end=27, mask=11111111b)
    * `FA, 00, FA, 00, FA, FA, 00` (start=91, end=97, mask=11111111b)
    * `FA, FA, FA, 00, FA, FA, FA` (start=98, end=104, mask=11111111b)

### LHM (CAFD 0000016BF) — authored by dmnc02

* **No-Glare High Beam Assistant (Step 2: passenger side)**
  * Group `3000`
    * `FA, FA, 00, 00, FA, FA, 00` (start=0, end=6, mask=11111111b)
    * `FA, FA, 00, 00, FA, FA, 00` (start=7, end=13, mask=11111111b)
    * `FA, FA, 00, 19, FA, FA, 00` (start=14, end=20, mask=11111111b)
    * `FA, 00, 00, 00, C8, C8, 00` (start=21, end=27, mask=11111111b)
    * `FA, FA, 00, 00, FA, FA, 00` (start=35, end=41, mask=11111111b)
    * `FA, FA, 00, 00, FA, FA, 00` (start=42, end=48, mask=11111111b)
    * `FA, FA, 00, 00, FA, FA, 00` (start=49, end=55, mask=11111111b)
    * `FA, FA, 00, 00, FA, FA, 00` (start=56, end=62, mask=11111111b)
    * `FA, FA, FA, 00, FA, FA, 00` (start=91, end=97, mask=11111111b)
    * `FA, FA, FA, 00, FA, FA, FA` (start=98, end=104, mask=11111111b)

### TMS (CAFD 000001082) — authored by dmnc02

* **Turn sidemarker LEDs off (driver side)**
  * Group `3005`
    * `00, 03, 00, 00, 00, 03, 00, 00, 64, 03, 00, 00, 2B, 04, 00, 00` (start=16, end=31, mask=11111111b)
    * `00, 03, 00, 00, 00, 03, 00, 00, 64, 03, 00, 00, 2B, 04, 00, 00` (start=32, end=47, mask=11111111b)
    * `00, 03, 00, 00, 00, 03, 00, 00, 64, 03, 00, 00, 2E, 04, 00, 00` (start=80, end=95, mask=11111111b)

* **Turn sidemarker LEDs on (driver side)**
  * Group `3005`
    * `00, 03, 00, 00, 64, 03, 00, 00, 64, 03, 00, 00, 2B, 04, 00, 00` (start=16, end=31, mask=11111111b)
    * `00, 03, 00, 00, 64, 03, 00, 00, 64, 03, 00, 00, 2B, 04, 00, 00` (start=32, end=47, mask=11111111b)
    * `00, 03, 00, 00, 64, 03, 00, 00, 64, 03, 00, 00, 2E, 04, 00, 00` (start=80, end=95, mask=11111111b)

### TMS (CAFD 000001083) — authored by dmnc02

* **Turn sidemarker LEDs off (passenger side)**
  * Group `3005`
    * `00, 03, 00, 00, 00, 03, 00, 00, 64, 03, 00, 00, 2B, 04, 00, 00` (start=16, end=31, mask=11111111b)
    * `00, 03, 00, 00, 00, 03, 00, 00, 64, 03, 00, 00, 2B, 04, 00, 00` (start=32, end=47, mask=11111111b)
    * `00, 03, 00, 00, 00, 03, 00, 00, 64, 03, 00, 00, 2E, 04, 00, 00` (start=80, end=95, mask=11111111b)

* **Turn sidemarker LEDs on (passenger side)**
  * Group `3005`
    * `00, 03, 00, 00, 64, 03, 00, 00, 64, 03, 00, 00, 2B, 04, 00, 00` (start=16, end=31, mask=11111111b)
    * `00, 03, 00, 00, 64, 03, 00, 00, 64, 03, 00, 00, 2B, 04, 00, 00` (start=32, end=47, mask=11111111b)
    * `00, 03, 00, 00, 64, 03, 00, 00, 64, 03, 00, 00, 2E, 04, 00, 00` (start=80, end=95, mask=11111111b)


## `ekfxisid.xml`

**Modules touched:** ACSM_4B (CAFD 00000911, author ekfxisidF030, series F020,F030), ASD01 (CAFD 00000F9B, author ekfxisidF30, series F020,F030), FEM_BODY (CAFD 00000794, author ekfxisidF030, series F020,F030), IHKA3 (CAFD 000016EE, author ekfxisidF030, series F020,F030), IHKA (CAFD 00000A3F, author ekfxisidF030, series F020,F030), HKFM (CAFD 000007C8, author ekfxisidF030, series F020,F030), HKFM (CAFD 0000157F, author ekfxisidF030, series F020,F030), KOMBI (CAFD 000009C8, author ekfxisidF030, series F020,F030), BKOMBI L7_BASIS (CAFD 00000760, author ekfxisidF030, series F020,F030), EGS (CAFD 0000023F, author ekfxisidF030, series F020,F030), REM (CAFD 000007A1, author ekfxisidF030, series F020,F030), ICMQL (CAFD 0000067B, author ekfxisidF030, series F020,F030), SM2 (CAFD 000000B5, author ekfxisidF030, series F020,F030), HU_NBT (CAFD 00000DED, author ekfxisidF030, series F020,F030), HU_NBT2 (CAFD 00001EF6, author ekfxisidF030, series F020,F030), HU_CICHB (CAFD 000000F9, author ekfxisidF030, series F020,F030), CAS_04 (CAFD 0000000F, author ekfxisidF010, series F010,F001,F007), COMBOX (CAFD 000005B6, author ekfxisidF010, series F010,F001,F007), ASD01 (CAFD 00000F9B, author ekfxisidF010, series F010,F001,F007), DKOMBI 6WB (CAFD 00001060, author ekfxisidF010, series F010,F001,F007), KAFAS2 (CAFD 00001148, author ekfxisidF010, series F010,F001,F007), FRM (CAFD 0000106D, author ekfxisidF010, series F010,F001,F007), FRM (CAFD 0000012F, author ekfxisidF010, series F010,F001,F007), JBBFE (CAFD 00000014, author ekfxisidF010, series F010,F001,F007), ACSM_4C (CAFD 00000909, author ekfxisidF010, series F010,F001,F007), ACSM (CAFD 0000009C, author ekfxisidF010, series F010,F001,F007), ACSM (CAFD 000011AB, author ekfxisidF010, series F010,F001,F007), IHKA3 (CAFD 000016EE, author ekfxisidF010, series F010,F001,F007), IHKA (CAFD 00000A3F, author ekfxisidF010, series F010,F001,F007), IHKA (CAFD 00000092, author ekfxisidF010, series F010,F001,F007), HKFM (CAFD 000007C8, author ekfxisidF010, series F010,F001,F007), HKFM (CAFD 00000076, author ekfxisidF010, series F010,F001,F007), KOMBI (CAFD 00000069, author ekfxisidF010, series F010,F001,F007), EGS (CAFD 0000023F, author ekfxisidF010, series F010,F001,F007), ICM (CAFD 0000067B, author ekfxisidF010, series F010,F001,F007), SM(6d) (CAFD 000000B5, author ekfxisidF010, series F010,F001,F007), SM(6e) (CAFD 000000B6, author ekfxisidF010, series F010,F001,F007), HU_NBT (CAFD 00000DED, author ekfxisidF010, series F010,F001,F007), HU_CIC (CAFD 000000F9, author ekfxisidF010, series F010,F001,F007), HU_NBT2 (CAFD 00001EF6, author ekfxisidF010, series F010,F001,F007), BDC_01 (CAFD 000017BE, author ekfxisidF025, series F015,F016,F025), ACSM_4C (CAFD 00000909, author ekfxisidF025, series F015,F016,F025), ACSM (CAFD 000011AB, author ekfxisidF025, series F015,F016,F025,F026), KAFAS2 (CAFD 00001148, author ekfxisidF025, series F015,F016,F025), HKFM (CAFD 000007C8, author ekfxisidF025, series F015,F016,F025), IHKA3 (CAFD 000016EE, author ekfxisidF025, series F015,F016,F025,F026), ICM (CAFD 0000067B, author ekfxisidF025, series F015,F016,F025), KOMBI (CAFD 00000069, author ekfxisidF025, series F015,F016,F025), KOMBI (CAFD 000009C8, author ekfxisidF025, series F015,F016,F025,F026), SM2 (CAFD 000000B5, author ekfxisidF025, series F015,F016,F025), CAS_04 (CAFD 0000000F, author ekfxisidF025, series F015,F016,F025), FRM (CAFD 0000012F, author ekfxisidF025, series F015,F016,F025), JBBFE (CAFD 00000014, author ekfxisidF025, series F015,F016,F025), HU_CIC (CAFD 000000F9, author ekfxisidF025, series F015,F016,F025), FRM (CAFD 0000106D, author ekfxisidF025, series F015,F016,F025), HU_NBT2 (CAFD 00001EF6, author ekfxisidF025, series F015,F016,F025,F026), HU_NBT (CAFD 00000DED, author ekfxisidF025, series F015,F016,F025), BDC_01 (CAFD 000017BE, author ekfxisidF056, series F056), ACSM_4i (CAFD 000011AB, author ekfxisidF056, series F056), IHKA3 (CAFD 000016EE, author ekfxisidF056, series F056), SM2 (CAFD 000000B5, author ekfxisidF056, series F056), HU_NBT2 (CAFD 00001EF6, author ekfxisidF056, series F056), HU_NBT (CAFD 00000DED, author ekfxisidF056, series F056)

### ACSM_4B (CAFD 00000911) — authored by ekfxisidF030 | Series: F020,F030

* **Seat belt warning chime three times (5 seconds) [Changwon ll Daltanyang]**
  * Group `3001`
    * `05` (start=3, mask=11111111b, comment=GWF_SBR_WARNDAUER)

### ASD01 (CAFD 00000F9B) — authored by ekfxisidF30 | Series: F020,F030

* **ASD M4 active sound [Changwon ll Daltanyang]**
  * Group `3000`
    * `F082` (start=0, mask=11111111b, comment=Model Range)
    * `S55B30` (start=1, mask=11111111b, comment=Engine)
    * `Hifi` (start=2, mask=11111111b, comment=Audio Level)
    * `ML` (start=3, mask=11111111b, comment=Power Class)

### FEM_BODY (CAFD 00000794) — authored by ekfxisidF030 | Series: F020,F030

* **Mirror lock folding (one-touch) [Changwon ll Daltanyang]**
  * Group `3053`
    * `00` (start=9, mask=11111111b, comment=KOMFORT_SCHLIESSEN)

* **Allow windows to operate with doors open**
  * Group `3050`
    * `nicht_aktiv` (start=0, mask=00000001b, comment=FH_TUERAUF_STOP_MAUT)

* **Turn signal flashes five times**
  * Group `3060`
    * `04` (start=7, mask=00000111b, comment=BLINKZYKLEN_ANZAHL_TIPP)

* **Passenger mirror angle adjustment 1**
  * Group `3110`
    * `1E` (start=2, mask=11111111b, comment=ASP_BORDSTEINAUTOMAIK_DELTA)

* **Passenger mirror angle adjustment when preset 1 fails**
  * Group `3110`
    * `1E` (start=3, mask=11111111b, comment=ASP_HORIZONTALE_MIN_POS)

* **Xenon: Angel Eye brightness 30% when xenon on**
  * Group `3062`
    * `1E` (start=46, mask=11111111b, comment=MAPPING_STANDL_V_L_PWM_LEVEL_STANDARD)
    * `1E` (start=57, mask=11111111b, comment=MAPPING_STANDL_V_R_PWM_LEVEL_STANDARD)

* **Xenon: Angel Eye brightness 100% when xenon on**
  * Group `3062`
    * `64` (start=46, mask=11111111b, comment=MAPPING_STANDL_V_L_PWM_LEVEL_STANDARD)
    * `64` (start=57, mask=11111111b, comment=MAPPING_STANDL_V_R_PWM_LEVEL_STANDARD)

* **Xenon: Angel Eye brightness 50% with parking lights on**
  * Group `3062`
    * `32` (start=68, mask=11111111b, comment=MAPPING_PARKL_V_L_PWM_1_LEFT)
    * `32` (start=69, mask=11111111b, comment=MAPPING_PARKL_V_L_PWM_2_RIGHT)

* **Xenon: Angel Eye brightness 100% with parking lights on**
  * Group `3062`
    * `64` (start=68, mask=11111111b, comment=MAPPING_PARKL_V_L_PWM_1_LEFT)
    * `64` (start=69, mask=11111111b, comment=MAPPING_PARKL_V_L_PWM_2_RIGHT)

* **Xenon: Angel Eye brightness 50% with DRL on**
  * Group `3062`
    * `32` (start=90, mask=11111111b, comment=MAPPING_TAGFAHRL_V_L_PWM_LEVEL_1)
    * `32` (start=101, mask=11111111b, comment=MAPPING_TAGFAHRL_V_R_PWM_LEVEL_1)

* **Xenon: Angel Eye brightness 100% with DRL on**
  * Group `3062`
    * `64` (start=90, mask=11111111b, comment=MAPPING_TAGFAHRL_V_L_PWM_LEVEL_1)
    * `64` (start=101, mask=11111111b, comment=MAPPING_TAGFAHRL_V_R_PWM_LEVEL_1)

* **Simulate adaptive lights with fog lights 1/3**
  * Group `3073`
    * `01` (start=66, mask=00000001b, comment=C_BLC_ENA)
    * `01` (start=218, mask=00000010b, comment=C_CLC_ENA)

* **Simulate adaptive lights with fog lights 2/3**
  * Group `3066`
    * `KL_Ein` (start=0, mask=00000001b, comment=KL_ENALBE_LI)
    * `KL_Ein` (start=80, mask=00000001b, comment=KL_ENABLE_RE)

* **Simulate adaptive lights with fog lights 3/3**
  * Group `3062`
    * `nsw_l` (start=110, mask=00111111b, comment=MAPPING_ABBIEGEL_L_OUTPUT)
    * `nsw_r` (start=121, mask=00111111b, comment=MAPPING_ABBIEGEL_L_OUTPUT)

* **Toggle headlight washer enablement**
  * Group `3080`
    * `nicht_aktiv` (start=8, mask=00000001b, comment=WW_SCHEINWERFERREINIGUNG)

* **Welcome fog lights (hard on)**
  * Group `3063`
    * `hard_On` (start=55, mask=11000000b, comment=MAPPING_NEBELSCHW_L_PART_OF_WL)
    * `hard_On` (start=66, mask=11000000b, comment=MAPPING_NEBELSCHW_R_PART_OF_WL)

* **Welcome fog lights (soft on)**
  * Group `3063`
    * `soft_On` (start=55, mask=11000000b, comment=MAPPING_NEBELSCHW_L_PART_OF_WL)
    * `soft_On` (start=66, mask=11000000b, comment=MAPPING_NEBELSCHW_R_PART_OF_WL)

* **Auto unfold mirrors above set speed (40 km/h -> 25 km/h)**
  * Group `3110`
    * `19` (start=10, mask=11111111b, comment=ASP_GESCHWINDIGKEIT_AUTO_AUSKLAPPEN)

* **Adjust automatic light sensor**
  * Group `3130`
    * `unempfindlich` (start=5, mask=00000111b, comment=RLS_DEF_FLC_SCHWELLWERT_SATZ)

* **Illuminate door handle lights in reverse**
  * Group `3070`
    * `aktiv` (start=11, mask=00010000b, comment=OVT_BEI_RUECKFAHRLICHT)

* **Welcome ambient lighting**
  * Group `3070`
    * `Aktiv` (start=1, mask=10000000b, comment=WELCOME_AMBIENTE)

* **Ambient lighting maximum brightness**
  * Group `3070`
    * `99` (start=5, mask=11111111b, comment=AMBIENTE_HELLGKELT)

* **Turn off audio and navigation when door opens after engine off**
  * Group `3020`
    * `01` (start=1, mask=00000001b, comment=TCM_LOGIC_R_OFF_DOOR)

* **Enable dynamic brake lights**
  * Group `3060`
    * `bremslicht_blinkend` (start=16, mask=00000011b, comment=ESS_AKTIVIERBARER_AUSGANG)
    * `04` (start=20, mask=00011111b, comment=ESS_AKTIVIERUNG_REALE_VERZ)
    * `04` (start=19, mask=00011111b, comment=ESS_DEAKTIVIERUNG_REALE_VERZ)
    * `0A` (start=17, mask=11111110b, comment=ESS_AKTIVIERUNG_GESCHW)

* **Flash hazard lights during hard braking (50 km/h)**
  * Group `3060`
    * `aktiv` (start=26, mask=00000001b, comment=WB_GB_ENABLE)
    * `00, 32` (start=23, end=24, mask=11111111b, comment=WB_GB_GEFAHRENWERT_MIN)

* **Remember last auto start/stop state**
  * Group `3023`
    * `aktiv` (start=0, mask=00100000b, comment=TCM_MSA_MEMORY)

* **Auto Start/Stop DEFAULT OFF**
  * Group `3023`
    * `aktiv` (start=0, mask=00010000b, comment=TCM_MSA_DEFAULT_OFF)

* **Front fog lights -> convert to LED**
  * Group `3061`
    * `nicht_aktiv` (start=42, mask=00000001b, comment=NSW_L_KALTUEBERWACHUNG)
    * `nicht_aktiv` (start=42, mask=00000010b, comment=NSW_L_WARMUEBERWACHUNG)
    * `aktiv` (start=42, mask=00000100b, comment=NSW_L_KURZSCHLUSS)
    * `aktiv` (start=42, mask=00001000b, comment=NSW_L_IS_LED)
    * `nicht_aktiv` (start=46, mask=00000001b, comment=NSW_R_KALTUEBERWACHUNG)
    * `nicht_aktiv` (start=46, mask=00000010b, comment=NSW_R_WARMUEBERWACHUNG)
    * `aktiv` (start=46, mask=00000100b, comment=NSW_R_KURZSCHLUSS)
    * `aktiv` (start=46, mask=00001000b, comment=NSW_R_IS_LED)

* **Front turn signals -> convert to LED**
  * Group `3061`
    * `nicht_aktiv` (start=50, mask=00000001b, comment=FRA_V_L_KALTUEBERWACHUNG)
    * `nicht_aktiv` (start=50, mask=00000010b, comment=FRA_V_L_WARMUEBERWACHUNG)
    * `aktiv` (start=50, mask=00000100b, comment=FRA_V_L_KURZSCHLUSS)
    * `aktiv` (start=50, mask=00001000b, comment=FRA_V_L_IS_LED)
    * `nicht_aktiv` (start=50, end=54, mask=00000001b, comment=FRA_V_R_KALTUEBERWACHUNG)
    * `nicht_aktiv` (start=50, end=54, mask=00000010b, comment=FRA_V_R_WARMUEBERWACHUNG)
    * `aktiv` (start=50, end=54, mask=00000100b, comment=FRA_V_R_KURZSCHLUSS)
    * `aktiv` (start=50, end=54, mask=00001000b, comment=FRA_V_R_IS_LED)

* **Horn alarm when locking with engine running**
  * Group `3040`
    * `aktiv` (start=1, mask=00100000b, comment=CLM_HORN_AT_SECURE)

* **Auto door lock speed (10 km/h = 0A)**
  * Group `3040`
    * `0A` (start=6, mask=11111111b, comment=CLM_SPEED_LIMIT_PIA_AUTO_LOCK)

* **Auto re-lock if door unopened after unlock (18 seconds)**
  * Group `3040`
    * `12` (start=5, mask=11111111b, comment=CLM_TIME_PIA_LOCK_AT_TIMEOUT)

* **Unlock doors automatically when engine off**
  * Group `3040`
    * `aktiv` (start=1, mask=00000010b, comment=CLM_UNLOCK_KL150OFF_AFTER_PIA_AUTO_LOCK)

* **Enable panic alarm 500 ms (short = welcome; MID = trunk; 3 s = panic)**
  * Group `30D0`
    * `Aktiv` (start=2, mask=00000100b, comment=RC_PANIC_ALARM)
    * `04` (start=3, mask=00001111b, comment=RC_DEFAULT_IDG_3RD_BUTTON_SHORT)
    * `02` (start=3, mask=11110000b, comment=RC_DEFAULT_IDG_3RD_BUTTON_MID)
    * `03` (start=4, mask=00001111b, comment=RC_DEFAULT_IDG_3RD_BUTTON_LONG)
    * `14` (start=8, mask=11111111b, comment=RC_TIME_DELAY_BOOTLID)
    * `28` (start=9, mask=11111111b, comment=RC_TIME_DELAY_PANIC)

* **Enable paddle shifters**
  * Group `3190`
    * `aktiv` (start=0, mask=000000001b, comment=PADDLES_VERBAUT)

### IHKA3 (CAFD 000016EE) — authored by ekfxisidF030 | Series: F020,F030

* **Remember last A/C on/off state [Changwon ll Daltanyang]**
  * Group `3003`
    * `Aktiv` (start=0, mask=00000010b, comment=MEMORY_OFF)

* **Remember air recirculation mode**
  * Group `3003`
    * `Aktiv` (start=0, mask=00000001b, comment=MEMORY_UMLUFT)

* **Prevent AUTO button from turning on A/C**
  * Group `3003`
    * `Aktiv` (start=0, mask=00000001b, comment=AC_NICHT_EIN_BEI_AUTO)

* **Lock air recirculation mode**
  * Group `3003`
    * `disable` (start=0, mask=10000000b, comment=UMLUFT_AUTO_AUS)

### IHKA (CAFD 00000A3F) — authored by ekfxisidF030 | Series: F020,F030

* **Remember last A/C on/off state [Changwon ll Daltanyang]**
  * Group `3002`
    * `Aktiv` (start=0, mask=00000010b, comment=MEMORY_OFF)

* **Remember air recirculation mode**
  * Group `3002`
    * `Aktiv` (start=0, mask=00000001b, comment=MEMORY_UMLUFT)

* **Prevent AUTO button from turning on A/C**
  * Group `3002`
    * `Aktiv` (start=0, mask=00000100b, comment=AC_NICHT_EIN_BEI_AUTO)

### HKFM (CAFD 000007C8) — authored by ekfxisidF030 | Series: F020,F030

* **Operate power trunk from interior button [Changwon ll Daltanyang]**
  * Group `3010`
    * `Aktiv` (start=2, mask=00001000b, comment=SCH_FBD)
    * `Aktiv` (start=2, mask=00000100b, comment=SCH_TOEHKI)
    * `Aktiv` (start=0, mask=00001000b, comment=TASTER_FBD)

### HKFM (CAFD 0000157F) — authored by ekfxisidF030 | Series: F020,F030

* **Operate power trunk from interior button**
  * Group `3010`
    * `Aktiv` (start=2, mask=00001000b, comment=SCH_FBD)
    * `Aktiv` (start=2, mask=00000100b, comment=SCH_TOEHKI)
    * `Aktiv` (start=0, mask=00001000b, comment=TASTER_FBD)

### KOMBI (CAFD 000009C8) — authored by ekfxisidF030 | Series: F020,F030

* **Enable Sport+ menu in cluster       [Changwon ll Daltanyang]**
  * Group `300C`
    * `menue_3` (start=54, mask=11111111b, comment=FDS_MENUE)

* **Digital speedometer in instrument cluster**
  * Group `3000`
    * `Aktiv` (start=1, mask=00000010b, comment=BC_DIGITAL_V)
    * `nicht_aktiv` (start=1, mask=01000000b, comment=BC_V_KORREKTUR)

* **Instrument cluster M Performance logo**
  * Group `3000`
    * `01` (start=0, mask=11110000b, comment=BMW_LOGO)

* **Enable motor temperature display**
  * Group `3000`
    * `aktiv` (start=3, mask=00010000b, comment=BC_MOTORTEMP_ENABLE)

* **Move instrument cluster clock**
  * Group `3000`
    * `Aktiv` (start=53, mask=01000000b, comment=BASISANZEEIGE_VARIANTE)

* **Show manual gear steps M1-M8 in DS mode**
  * Group `3000`
    * `Aktiv` (start=41, mask=00010000b, comment=SPA_SPORT_ENABLE)

* **Enable MPM**
  * Group `3003`
    * `Aktiv` (start=7, mask=00000100b, comment=MPM_ENABLE)

* **MPM logo 550d**
  * Group `3000`
    * `550d` (start=43, mask=11110000b, comment=MPM_LOGO)

* **MPM logo 50d**
  * Group `3000`
    * `550d` (start=43, mask=11110000b, comment=MPM_LOGO)

### BKOMBI L7_BASIS (CAFD 00000760) — authored by ekfxisidF030 | Series: F020,F030

* **Enable Sport+ menu in cluster       [Changwon ll Daltanyang]**
  * Group `300C`
    * `menue_3` (start=54, mask=11111111b, comment=FDS_MENUE)

* **Digital speedometer in instrument cluster**
  * Group `3000`
    * `aktiv` (start=1, mask=00000010b, comment=BC_DIGITAL_V)
    * `nicht_aktiv` (start=1, mask=01000000b, comment=BC_V_KORREKTUR)

* **Enable motor temperature display**
  * Group `3000`
    * `aktiv` (start=3, mask=00010000b, comment=BC_MOTORTEMP_ENABLE)

* **Instrument cluster M Performance logo**
  * Group `3000`
    * `01` (start=0, mask=11110000b, comment=BMW_LOGO)

### EGS (CAFD 0000023F) — authored by ekfxisidF030 | Series: F020,F030

* **Display gear position S1-S8 in DS mode [Changwon ll Daltanyang]**
  * Group `3000`
    * `aktiv` (start=0, mask=01000000b, comment=SPORTSCHALTER_ALT)
    * `aktiv` (start=1, mask=00000001b, comment=SPORTSCHALTER)

### REM (CAFD 000007A1) — authored by ekfxisidF030 | Series: F020,F030

* **Daytime tail lamps synchronized with daytime headlights [Changwon ll Daltanyang]**
  * Group `3062`
    * `sl_l` (start=200, mask=00111111b, comment=MAPPING_TAGFAHRL_H_L_OUTPUT)
    * `sl_r` (start=210, mask=00111111b, comment=MAPPING_TAGFAHRL_H_R_OUTPUT)
    * `sl_2_l` (start=220, mask=00111111b, comment=MAPPING_TAGFAHRL_H2_L_OUTPUT)
    * `sl_2_r` (start=230, mask=00111111b, comment=MAPPING_TAGFAHRL_H2_R_OUTPUT)

* **Keep rear camera always on**
  * Group `3203`
    * `FF` (start=7, mask=11111111b, comment=V_SCHWELLE_1)
    * `FF` (start=8, mask=11111111b, comment=V_SCHWELLE_2)
    * `FF` (start=9, mask=11111111b, comment=D_SCHWELLE_1)
    * `FF` (start=10, mask=11111111b, comment=D_SCHWELLE_2)

* **Brake lights -> convert to LED**
  * Group `3061`
    * `nicht_aktiv` (start=18, mask=00000001b, comment=BL_L_KALTUEBERWCHUNG)
    * `nicht_aktiv` (start=18, mask=00000010b, comment=BL_L_WARMUEBERWCHUNG)
    * `aktiv` (start=18, mask=00001000b, comment=BL_L_IS_LED)
    * `nicht_aktiv` (start=22, mask=00000001b, comment=BL_R_KALTUEBERWCHUNG)
    * `nicht_aktiv` (start=22, mask=00000010b, comment=BL_R_WARMUEBERWCHUNG)
    * `aktiv` (start=22, mask=00001000b, comment=BL_R_IS_LED)

* **Rear fog lights -> convert to LED**
  * Group `3061`
    * `nicht_aktiv` (start=34, mask=00000001b, comment=NSL_L_KALTUEBERWCHUNG)
    * `nicht_aktiv` (start=34, mask=00000010b, comment=NSL_L_WARMTUEBERWCHUNG)
    * `aktiv` (start=34, mask=00001000b, comment=NSL_L_IS_LED)
    * `nicht_aktiv` (start=38, mask=00000001b, comment=NSL_R_KALTUEBERWCHUNG)
    * `nicht_aktiv` (start=38, mask=00000010b, comment=NSL_R_WARMUEBERWCHUNG)
    * `aktiv` (start=38, mask=00001000b, comment=NSL_R_IS_LED)

* **Reverse lights -> convert to LED**
  * Group `3061`
    * `nicht_aktiv` (start=42, mask=00000001b, comment=RFS_L_KALTUEBERWCHUNG)
    * `nicht_aktiv` (start=42, mask=00000010b, comment=RFSL_L_WARMTUEBERWCHUNG)
    * `aktiv` (start=42, mask=00001000b, comment=RFS_L_IS_LED)
    * `nicht_aktiv` (start=46, mask=00000001b, comment=RFS_R_KALTUEBERWCHUNG)
    * `nicht_aktiv` (start=46, mask=00000010b, comment=RFS_R_WARMUEBERWCHUNG)
    * `aktiv` (start=46, mask=00001000b, comment=RFS_R_IS_LED)

* **Rear turn signals -> convert to LED**
  * Group `3061`
    * `nicht_aktiv` (start=50, mask=00000001b, comment=FRAFRA_L_KALTUEBERWCHUNG)
    * `nicht_aktiv` (start=50, mask=00000010b, comment=FRAL_L_WARMTUEBERWCHUNG)
    * `aktiv` (start=50, mask=00001000b, comment=FRA_L_IS_LED)
    * `nicht_aktiv` (start=54, mask=00000001b, comment=FRA_R_KALTUEBERWCHUNG)
    * `nicht_aktiv` (start=54, mask=00000010b, comment=FRA_R_WARMUEBERWCHUNG)
    * `aktiv` (start=54, mask=00001000b, comment=FRA_R_IS_LED)

* **== Convert all rear lights to LED ==**
  * Group `3061`
    * `00` (start=10, mask=00000001b)
    * `00` (start=10, mask=00000010b)
    * `01` (start=10, mask=00001000b)
    * `00` (start=14, mask=00000001b)
    * `00` (start=14, mask=00000010b)
    * `01` (start=14, mask=00001000b)
    * `00` (start=18, mask=00000001b)
    * `00` (start=18, mask=00000010b)
    * `01` (start=18, mask=00001000b)
    * `00` (start=22, mask=00000001b)
    * `00` (start=22, mask=00000010b)
    * `01` (start=22, mask=00001000b)
    * `00` (start=26, mask=00000001b)
    * `00` (start=26, mask=00000010b)
    * `01` (start=26, mask=00001000b)
    * `00` (start=30, mask=00000001b)
    * `00` (start=30, mask=00000010b)
    * `01` (start=30, mask=00001000b)
    * `00` (start=34, mask=00000001b)
    * `00` (start=34, mask=00000010b)
    * `01` (start=34, mask=00001000b)
    * `00` (start=38, mask=00000001b)
    * `00` (start=38, mask=00000010b)
    * `01` (start=38, mask=00001000b)
    * `00` (start=42, mask=00000001b)
    * `00` (start=42, mask=00000010b)
    * `01` (start=42, mask=00001000b)
    * `00` (start=46, mask=00000001b)
    * `00` (start=46, mask=00000010b)
    * `01` (start=46, mask=00001000b)
    * `00` (start=50, mask=00000001b)
    * `00` (start=50, mask=00000010b)
    * `01` (start=50, mask=00001000b)
    * `00` (start=54, mask=00000001b)
    * `00` (start=54, mask=00000010b)
    * `01` (start=54, mask=00001000b)
    * `01` (start=66, mask=00001000b)
    * `01` (start=70, mask=00001000b)

### ICMQL (CAFD 0000067B) — authored by ekfxisidF030 | Series: F020,F030

* **Enable Sport+ mode in cluster -> KOMBI [Changwon ll Daltanyang]**
  * Group `3000`
    * `verbaut` (start=28, mask=11111111b, comment=IcmKod_B_Sportlenkung)

* **Set ECO PRO as default driving mode**
  * Group `3000`
    * `verbaut` (start=36, mask=00001000b, comment=IcmKod_B_InitEco)

* **Enable cruise control -> KOMBI**
  * Group `3000`
    * `verbaut` (start=128, mask=00001110b, comment=C_Fahrfunktion)

### SM2 (CAFD 000000B5) — authored by ekfxisidF030 | Series: F020,F030

* **Easy Access 1/3 (Easy Entry) [Changwon ll Daltanyang]**
  * Group `3000`
    * `Modus_FA_SLV` (start=0, mask=00011100b, comment=EINAUSSTIEGSHILFE)

* **Easy Access 2/3 (Easy Entry)**
  * Group `3012`
    * `00, 1E` (start=4, end=5, mask=11111111b, comment=EAH_SCHUTZFREIRAUM_HINTEN_SLV_PHYS)

* **Easy Access 3/3 (Easy Entry)**
  * Group `3012`
    * `00, 46` (start=0, end=1, mask=11111111b, comment=EAH_VERFAHRWEG_SLV_PHYS)

* **Set memory gong alert sound**
  * Group `3000`
    * `Aktiv` (start=2, mask=00001000b, comment=MEMORY_GONG)

### HU_NBT (CAFD 00000DED) — authored by ekfxisidF030 | Series: F020,F030

* **Unlock DMB/DVD/Navi while driving [Changwon ll Daltanyang]**
  * Group `3000`
    * `FF` (start=72, mask=11111111b, comment=SPEEDLOCK_X_KMH_MAX)
    * `FF` (start=71, mask=11111111b, comment=SPEEDLOCK_X_KMH_MIN)
    * `nicht_aktiv` (start=5, mask=00010000b, comment=VIDEO_FRONT_LOCKED)
    * `nicht_aktiv` (start=5, mask=00000100b, comment=VIDEO_HANDBRAKE)
    * `None` (start=57, mask=00000111b, comment=VIDEO_SPEEDLOCK_CONDITION)

* **M performance**
  * Group `3001`
    * `01` (start=62, mask=01111000b, comment=STARTUP_EMBLEM)

* **X - Drive**
  * Group `3000`
    * `aktiv` (start=5, mask=00000001b, comment=COMPASS)
    * `aktiv` (start=15, mask=00000001b, comment=X_VIEW)
    * `trajectory1` (start=26, mask=00110000b, comment=X_VIEW_GRAPHIC_SLOP)
    * `trajectory1` (start=26, mask=11000000b, comment=X_VIEW_GRAPHIC_ROLL)
    * `aktiv` (start=110, mask=00000010b, comment=MOMENTDISTRIBUTION_MENU)

* **Change warning sound**
  * Group `3002`
    * `rolls_royce` (start=26, mask=00111000b, comment=SOUND_SIGNAL_SET)

* **Enable USB video playback 1/2**
  * Group `3000`
    * `aktiv` (start=15, mask=00010000b, comment=ENT_CODEC_OGG)
    * `aktiv` (start=15, mask=00100000b, comment=ENT_CODEC_XVID)
    * `aktiv` (start=15, mask=01000000b, comment=ENT_CODEC_VCD)
    * `aktiv` (start=13, mask=00000100b, comment=ENT_MC_VIDEO_SUPPORT)

* **Enable USB video playback 2/2**
  * Group `3003`
    * `both` (start=33, mask=00000110b, comment=API_USB_VIDEO)
    * `both` (start=33, mask=00011000b, comment=API_IPOD_VIEDO)

* **Remove all warning messages**
  * Group `3001`
    * `00` (start=52, mask=11111111b, comment=MACRO_CAM_LEGALDISCLAIMER)
    * `00` (start=58, mask=11111111b, comment=LEGAL_DISCLAIMER_TIME)

* **Enable automatic time setting**
  * Group `3000`
    * `navigation` (start=19, mask=00000110b, comment=SETTINGS_TIME_AUTOMATIC)
    * `aktiv` (start=105, mask=00100000b, comment=CLOCK_CHANGE_AUTOMATIC)

* **Enable rear camera zoom**
  * Group `3001`
    * `aktiv` (start=54, mask=00000001b, comment=MACRO_TRAILER_COUPLING)

* **Enable daylight running lights**
  * Group `3000`
    * `02` (start=92, mask=00011000b, comment=DAYDRIVING_LIGHT)

* **Output ringtone through speakers (iOS only)**
  * Group `3003`
    * `aktiv` (start=6, mask=10000000b, comment=INBAND_RINGING)

* **Configure Sport mode 1/3**
  * Group `3000`
    * `aktiv` (start=101, mask=00010000b, comment=EFF_DYN_SPORT_CID)

* **Configure Sport mode 2/3**
  * Group `3000`
    * `aktiv` (start=107, mask=00000100b, comment=EFF_DYN_SPORT_UNIT)

* **Configure Sport mode 3/3**
  * Group `3001`
    * `popup_and_config` (start=55, mask=00011000b, comment=MACRO_FDS)

* **Bang & Olufsen profile**
  * Group `3000`
    * `keine_insz` (start=21, mask=01100000b, comment=HIGH_END_AUDIO_B_UND_W)

* **Enable Logic7 (S667A HiFi vehicles)**
  * Group `3000`
    * `aktiv` (start=22, mask=00001000b, comment=LOGIC7_SYMBOL)

* **Door lock/unlock chime (vehicles with anti-theft module except M5)**
  * Group `3000`
    * `Aktiv` (start=110, mask=00000001b, comment=ACOUSTICAL_LOCK_CONFIRM)

* **Enable TPMC tire pressure temperature**
  * Group `3001`
    * `Aktiv` (start=1, mask=00100000b, comment=RDC_SAFETY)

* **Change M Sport display cluster colors**
  * Group `3000`
    * `aktiv` (start=133, mask=01000000b, comment=M_VEHICLE)

* **High-beam assistant**
  * Group `3000`
    * `01` (start=109, mask=10000000b, comment=HIGH_BEAM_ASSISTANT)

### HU_NBT2 (CAFD 00001EF6) — authored by ekfxisidF030 | Series: F020,F030

* **Unlock DMB/DVD/Navi while driving 1/2 [Changwon ll Daltanyang]**
  * Group `3006`
    * `FF` (start=25, mask=11111111b, comment=SPEEDLOCK_X_KMH_MAX)
    * `FF` (start=26, mask=11111111b, comment=SPEEDLOCK_X_KMH_MIN)

* **Unlock DMB/DVD/Navi while driving 2/2**
  * Group `3000`
    * `nicht_aktiv` (start=5, mask=00010000b, comment=VIDEO_FRONT_LOCKED)
    * `nicht_aktiv` (start=5, mask=00000100b, comment=VIDEO_HANDBRAKE)
    * `None` (start=2, mask=00000111b, comment=VIDEO_SPEEDLOCK_CONDITION)

* **M performance**
  * Group `3001`
    * `01` (start=62, mask=01111000b, comment=STARTUP_EMBLEM)

* **X - Drive**
  * Group `3000`
    * `aktiv` (start=5, mask=00000001b, comment=COMPASS)
    * `aktiv` (start=15, mask=00000001b, comment=X_VIEW)
    * `trajectory1` (start=26, mask=00110000b, comment=X_VIEW_GRAPHIC_SLOP)
    * `trajectory1` (start=26, mask=11000000b, comment=X_VIEW_GRAPHIC_ROLL)
    * `aktiv` (start=110, mask=00000010b, comment=MOMENTDISTRIBUTION_MENU)

* **Change warning sound**
  * Group `3002`
    * `rolls_royce` (start=26, mask=00111000b, comment=SOUND_SIGNAL_SET)

* **Enable USB video playback 1/2**
  * Group `3000`
    * `aktiv` (start=15, mask=00010000b, comment=ENT_CODEC_OGG)
    * `aktiv` (start=15, mask=00100000b, comment=ENT_CODEC_XVID)
    * `aktiv` (start=15, mask=01000000b, comment=ENT_CODEC_VCD)
    * `aktiv` (start=13, mask=00000100b, comment=ENT_MC_VIDEO_SUPPORT)

* **Enable USB video playback 2/2**
  * Group `3003`
    * `both` (start=33, mask=00000110b, comment=API_USB_VIDEO)
    * `both` (start=33, mask=00011000b, comment=API_IPOD_VIEDO)

* **Remove all warning messages**
  * Group `3001`
    * `00` (start=52, mask=11111111b, comment=MACRO_CAM_LEGALDISCLAIMER)
    * `00` (start=58, mask=11111111b, comment=LEGAL_DISCLAIMER_TIME)

* **Enable automatic time setting**
  * Group `3000`
    * `navigation` (start=19, mask=00000110b, comment=SETTINGS_TIME_AUTOMATIC)
    * `aktiv` (start=105, mask=00100000b, comment=CLOCK_CHANGE_AUTOMATIC)

* **Enable rear camera zoom**
  * Group `3001`
    * `aktiv` (start=54, mask=00000001b, comment=MACRO_TRAILER_COUPLING)

* **Enable daylight running lights**
  * Group `3000`
    * `02` (start=92, mask=00011000b, comment=DAYDRIVING_LIGHT)

* **Output ringtone through speakers (iOS only)**
  * Group `3003`
    * `aktiv` (start=6, mask=10000000b, comment=INBAND_RINGING)

* **Configure Sport mode 1/3**
  * Group `3009`
    * `aktiv` (start=9, mask=00010000b, comment=EFF_DYN_SPORT_CID)

* **Configure Sport mode 2/3**
  * Group `3009`
    * `aktiv` (start=9, mask=00100000b, comment=EFF_DYN_SPORT_UNIT)

* **Configure Sport mode 3/3**
  * Group `3008`
    * `popup_and_config` (start=79, mask=11000000b, comment=MACRO_FDS)

* **Bang & Olufsen profile**
  * Group `3000`
    * `keine_insz` (start=21, mask=01100000b, comment=HIGH_END_AUDIO_B_UND_W)

* **Enable Logic7 (S667A HiFi vehicles)**
  * Group `3000`
    * `aktiv` (start=22, mask=00001000b, comment=LOGIC7_SYMBOL)

* **HUD : Affichage de l'assistant collision Step 2 (Step 1 dans KOMBI)**
  * Group `300C`
    * `Aktiv` (start=0, mask=00010000b, comment=HUD_DISTANCE_INFO)

* **Door lock/unlock chime (vehicles with anti-theft module except M5)**
  * Group `3000`
    * `Aktiv` (start=110, mask=00000001b, comment=ACOUSTICAL_LOCK_CONFIRM)

* **Enable TPMC tire pressure temperature**
  * Group `3001`
    * `Aktiv` (start=1, mask=00100000b, comment=RDC_SAFETY)

* **Change M Sport display cluster colors**
  * Group `3000`
    * `aktiv` (start=133, mask=01000000b, comment=M_VEHICLE)

* **High-beam assistant**
  * Group `3000`
    * `01` (start=109, mask=10000000b, comment=HIGH_BEAM_ASSISTANT)

### HU_CICHB (CAFD 000000F9) — authored by ekfxisidF030 | Series: F020,F030

* **Unlock DMB/DVD/Navi while driving [Changwon ll Daltanyang]**
  * Group `3000`
    * `FF` (start=23, mask=11111111b, comment=SPEEDLOCK_X_KMH_MIN)
    * `FF` (start=24, mask=11111111b, comment=SPEEDLOCK_X_KMH_MAX)

* **Enable rear camera zoom**
  * Group `3001`
    * `aktiv` (start=23, mask=00000001b, comment=MACRO_TRAILER_COUPLING)

* **Configure Sport mode 1/3**
  * Group `3000`
    * `aktiv` (start=47, mask=00010000b, comment=EFF_DYN_SPORT_CID)

* **Configure Sport mode 2/3**
  * Group `3000`
    * `aktiv` (start=61, mask=00000100b, comment=EFF_DYN_SPORT_UNIT)

* **Configure Sport mode 3/3**
  * Group `3000`
    * `popup_and_config` (start=7, mask=00110000b, comment=MACRO_FDS)

### CAS_04 (CAFD 0000000F) — authored by ekfxisidF010 | Series: F010,F001,F007

* **1. Auto Start/Stop DEFAULT OFF      [Changwon ll Daltanyang]**
  * Group `3000`
    * `01` (start=3, mask=00010000b, comment=TCM_MSA_DEFAULT_OFF)

* **2. Remember last auto start/stop state**
  * Group `3000`
    * `aktiv` (start=3, mask=00100000b, comment=TCM_MSA_MEMORY)

* **3. Start engine without pressing brake**
  * Group `3000`
    * `nicht_aktiv` (start=1, mask=00000001b, comment=TC_STARTLOCK_BRAKE)
  * Group `3000`
    * `nicht_aktiv` (start=1, mask=00010000b, comment=TC_STARTLOCK_DRIVINGREADINESS)

* **4. Mirror lock folding**
  * Group `3003`
    * `00` (start=12, mask=11111111b, comment=KMFRT_SCHLESSEN)

* **5. Turn off audio/navigation when door opens after shutdown**
  * Group `3000`
    * `aktiv` (start=2, mask=00000001b, comment=TC_LOGIC_KLR_OFF_DOOR)

* **6. Horn alarm when locking with engine running**
  * Group `3002`
    * `aktiv` (start=0, mask=00100000b, comment=CLM_HORN_AT_SECURE)

### COMBOX (CAFD 000005B6) — authored by ekfxisidF010 | Series: F010,F001,F007

* **1. Output ringtone through speakers (iOS only)        [Changwon ll Daltanyang]**
  * Group `3001`
    * `aktiv` (start=1, mask=10000000b, comment=INBAND_RINGING)

### ASD01 (CAFD 00000F9B) — authored by ekfxisidF010 | Series: F010,F001,F007

* **1. ASD M4 active sound [Changwon ll Daltanyang]**
  * Group `3000`
    * `F082` (start=0, mask=11111111b, comment=Model Range)
    * `S55B30` (start=1, mask=11111111b, comment=Engine)
    * `Hifi` (start=2, mask=11111111b, comment=Audio Level)
    * `ML` (start=3, mask=11111111b, comment=Power Class)

### DKOMBI 6WB (CAFD 00001060) — authored by ekfxisidF010 | Series: F010,F001,F007

* **Enable Sport+ menu in cluster [Changwon ll Daltanyang]**
  * Group `300C`
    * `menue_3` (start=51, mask=11111111b, comment=FDS_MENUE)

* **Enable compass in instrument cluster**
  * Group `3003`
    * `aktiv` (start=12, mask=00010000b, comment=KOMPASS_GRAPH_ENABLE)

* **Enable km/mph display in instrument cluster**
  * Group `3000`
    * `kmh_kmh` (start=42, mask=11110000b, comment=DIGITAL_TACHO_ENABLE)

* **Enable M Performance - MPM**
  * Group `3000`
    * `mpm` (start=44, mask=00001111b, comment=BMW_LOGO)

* **M Performance - X5M**
  * Group `3000`
    * `mpm_x5` (start=44, mask=00001111b, comment=BMW_LOGO)

* **M Performance - X6M**
  * Group `3000`
    * `mpm_x6` (start=44, mask=00001111b, comment=BMW_LOGO)

* **Enable MPM**
  * Group `3003`
    * `aktiv` (start=3, mask=00000010b, comment=MPM_ENABLE)

* **MPM logo - BMW**
  * Group `3000`
    * `bmw` (start=44, mask=11110000b, comment=MPM_LOGO)

* **MPM logo - MPM**
  * Group `3000`
    * `mpm` (start=44, mask=11110000b, comment=MPM_LOGO)

* **MPM logo - X5M**
  * Group `3000`
    * `mpm_x5` (start=44, mask=11110000b, comment=MPM_LOGO)

* **MPM logo - X6M**
  * Group `3000`
    * `mpm_x6` (start=44, mask=11110000b, comment=MPM_LOGO)

* **Digital speedometer in instrument cluster**
  * Group `3000`
    * `Aktiv` (start=1, mask=00000010b, comment=BC_DIGITAL_V)
    * `nicht_aktiv` (start=1, mask=01000000b, comment=BC_V_KORREKTUR)

* **Show manual gear steps M1-M8 in DS mode**
  * Group `3000`
    * `Aktiv` (start=39, mask=00010000b, comment=SPA_SPORT_ENABLE)

* **Enable HUD entertainment**
  * Group `3003`
    * `Aktiv` (start=10, mask=00000001b, comment=HUD_ENTERTAINMENT_ENABLE)

* **Disable temperature warning chime below 3 degrees**
  * Group `3000`
    * `nicht_aktiv` (start=50, mask=00000001b, comment=CC_TEMPERATURWARNUNG)

* **Enable power output display in cluster**
  * Group `3003`
    * `aktiv` (start=11, mask=00000010b, comment=MOTORLEISTUNG_ENABLE)

### KAFAS2 (CAFD 00001148) — authored by ekfxisidF010 | Series: F010,F001,F007

* **High-beam assistant 1/4 -> code this first to avoid errors**
  * Group `3050`
    * `FLA_on` (start=1, mask=00000001b, comment=FLA_ON_OFF)

### FRM (CAFD 0000106D) — authored by ekfxisidF010 | Series: F010,F001,F007

* **High-beam assistant 2/4 -> code KAFAS2 1/4 first**
  * Group `3050`
    * `aktiv` (start=20, mask=00010000b, comment=FLA_VERBAUT)

* **High-beam assistant 3/4 -> code HU_NBT 4/4 last**
  * Group `3050`
    * `automatisch` (start=20, mask=00100000b, comment=FLA_AUTO_AKTIV)

* **Passenger mirror angle adjustment**
  * Group `3020`
    * `1E` (start=1, mask=11111111b, comment=ASP_BORDSTEINAUTOMAIK_DELTA)

* **Auto unfold mirrors above set speed (40 km/h -> 25 km/h)**
  * Group `3020`
    * `19` (start=9, mask=11111111b, comment=ASP_GESCHWINDIGKEIT_AUTO_AUSKLAPPEN)

* **Allow windows to operate with doors open 1/2 (front) -> JBBF 2/2 (rear)**
  * Group `3030`
    * `nicht aktiv` (start=1, mask=00000100b, comment=FH_TUER_AUF_STOP_MAUT)

* **Daytime tail lamps**
  * Group `3050`
    * `drl_s` (start=20, mask=00001110b, comment=DRL_MODUS)

* **Enable dynamic brake lights**
  * Group `3050`
    * `02` (start=23, mask=01110000b, comment=ESS_ERSCHEINUNGSBILD)
    * `US` (start=24, mask=01111111b, comment=ESS_GESCHW_SCHWELLE)
    * `04` (start=21, mask=00011111b, comment=ESS_ON_VERZ)
    * `04` (start=22, mask=00011111b, comment=ESS_OFF_VERZ)

* **Flash hazard lights during hard braking**
  * Group `3050`
    * `aktiv` (start=2, mask=10000000b, comment=WB_GB_ENABLE)

* **Increase Angel Eye brightness to 30%**
  * Group `3060`
    * `1E` (start=1, mask=11111111b, comment=U_EFF_POL)

* **Welcome light fog lamps (hard on)**
  * Group `3050`
    * `Hard_on` (start=29, mask=00001100b, comment=WL_FUNKTION_NSW)

* **Welcome light fog lamps (soft on)**
  * Group `3050`
    * `Soft_on` (start=29, mask=00001100b, comment=WL_FUNKTION_NSW)

* **Front fog lights -> convert to LED and remove warning**
  * Group `3090`
    * `00` (start=79, mask=00000001b, comment=AUSG_11_NSW_L_WARM_UEBERW_AKTIV)
    * `00` (start=79, mask=00000010b, comment=AUSG_11_NSW_L_KALT_UEBERW_AKTIV)
    * `aktiv` (start=79, mask=00001000b, comment=AUSG_11_NSW_L_IS_LED)
    * `00` (start=83, mask=00000001b, comment=AUSG_12_NSW_R_WARM_UEBERW_AKTIV)
    * `00` (start=83, mask=00000010b, comment=AUSG_12_NSW_R_KALT_UEBERW_AKTIV)
    * `aktiv` (start=83, mask=00001000b, comment=AUSG_12_NSW_R_IS_LED)

* **Reverse lights -> convert to LED**
  * Group `3090`
    * `nicht_aktiv` (start=131, mask=00000001b, comment=AUSG_24_RFS_L_WARM_UEBERW_AKTIV)
    * `nicht_aktiv` (start=131, mask=00000010b, comment=AUSG_24_RFS_L_KALT_UEBERW_AKTIV)
    * `aktiv` (start=131, mask=00001000b, comment=AUSG_24_RFS_L_IS_LED)
    * `nicht_aktiv` (start=135, mask=00000001b, comment=AUSG_25_RFS_R_WARM_UEBERW_AKTIV)
    * `nicht_aktiv` (start=135, mask=00000010b, comment=AUSG_25_RFS_R_KALT_UEBERW_AKTIV)
    * `aktiv` (start=135, mask=00001000b, comment=AUSG_25_RFS_R_IS_LED)

### FRM (CAFD 0000012F) — authored by ekfxisidF010 | Series: F010,F001,F007

* **High-beam assistant 2/4 -> code KAFAS2 1/4 first**
  * Group `3050`
    * `aktiv` (start=20, mask=00010000b, comment=FLA_VERBAUT)

* **High-beam assistant 3/4 -> code HU_NBT 4/4 last**
  * Group `3050`
    * `automatisch` (start=20, mask=00100000b, comment=FLA_AUTO_AKTIV)

* **Passenger mirror angle adjustment**
  * Group `3020`
    * `1E` (start=1, mask=11111111b, comment=ASP_BORDSTEINAUTOMAIK_DELTA)

* **Auto unfold mirrors above set speed (40 km/h -> 25 km/h)**
  * Group `3020`
    * `19` (start=9, mask=11111111b, comment=ASP_GESCHWINDIGKEIT_AUTO_AUSKLAPPEN)

* **Allow windows to operate with doors open 1/2 (front) -> JBBF 2/2 (rear)**
  * Group `3030`
    * `nicht aktiv` (start=1, mask=00000100b, comment=FH_TUER_AUF_STOP_MAUT)

* **Daytime tail lamps**
  * Group `3050`
    * `drl_s` (start=20, mask=00001110b, comment=DRL_MODUS)

* **Enable dynamic brake lights**
  * Group `3050`
    * `bremslicht_blinkend` (start=23, mask=01110000b, comment=ESS_ERSCHEINUNGSBILD)
    * `US` (start=24, mask=01111111b, comment=ESS_GESCHW_SCHWELLE)
    * `04` (start=21, mask=00011111b, comment=ESS_ON_VERZ)
    * `04` (start=22, mask=00011111b, comment=ESS_OFF_VERZ)

* **Flash hazard lights during hard braking**
  * Group `3050`
    * `aktiv` (start=2, mask=10000000b, comment=WB_GB_ENABLE)

* **Increase Angel Eye brightness to 30%**
  * Group `3060`
    * `1E` (start=1, mask=11111111b, comment=U_EFF_POL)

* **Welcome light fog lamps (hard on)**
  * Group `3050`
    * `Hard_on` (start=29, mask=00001100b, comment=WL_FUNKTION_NSW)

* **Welcome light fog lamps (soft on)**
  * Group `3050`
    * `Soft_on` (start=29, mask=00001100b, comment=WL_FUNKTION_NSW)

* **Front fog lights -> convert to LED and remove warning**
  * Group `3090`
    * `00` (start=79, mask=00000001b, comment=AUSG_11_NSW_L_WARM_UEBERW_AKTIV)
    * `00` (start=79, mask=00000010b, comment=AUSG_11_NSW_L_KALT_UEBERW_AKTIV)
    * `aktiv` (start=79, mask=00001000b, comment=AUSG_11_NSW_L_IS_LED)
    * `00` (start=83, mask=00000001b, comment=AUSG_11_NSW_R_WARM_UEBERW_AKTIV)
    * `00` (start=83, mask=00000010b, comment=AUSG_11_NSW_R_KALT_UEBERW_AKTIV)
    * `aktiv` (start=83, mask=00001000b, comment=AUSG_11_NSW_R_IS_LED)

* **Reverse lights -> convert to LED**
  * Group `3090`
    * `nicht_aktiv` (start=131, mask=00000001b, comment=AUSG_24_RFS_L_WARM_UEBERW_AKTIV)
    * `nicht_aktiv` (start=131, mask=00000010b, comment=AUSG_24_RFS_L_KALT_UEBERW_AKTIV)
    * `aktiv` (start=131, mask=00001000b, comment=AUSG_24_RFS_L_IS_LED)
    * `nicht_aktiv` (start=135, mask=00000001b, comment=AUSG_24_RFS_R_WARM_UEBERW_AKTIV)
    * `nicht_aktiv` (start=135, mask=00000010b, comment=AUSG_24_RFS_R_KALT_UEBERW_AKTIV)
    * `aktiv` (start=135, mask=00001000b, comment=AUSG_24_RFS_R_IS_LED)

### JBBFE (CAFD 00000014) — authored by ekfxisidF010 | Series: F010,F001,F007

* **Disable headlight washer fluid [Changwon ll Daltanyang]**
  * Group `3000`
    * `nicht_aktiv` (start=8, mask=00000001b, comment=SCHEINWERFERREINIGUNG)

* **Allow windows to operate when door open 2/2 (rear)**
  * Group `3070`
    * `nicht_aktiv` (start=0, mask=00000100b, comment=FH_TUERAUF_STOP_MAUT)

* **Adjust automatic light sensor**
  * Group `3530`
    * `unempfindlich` (start=5, mask=00111000b, comment=RLS_FLC_SCHWELLWERT_SATZ)

* **Adjust rain sensor**
  * Group `3530`
    * `unempfindlich` (start=5, mask=00000111b, comment=RLS_DEF_FLC_SCHWELLWERT_SATZ)

### ACSM_4C (CAFD 00000909) — authored by ekfxisidF010 | Series: F010,F001,F007

* **Seat belt warning chime three times (5 seconds) [Changwon ll Daltanyang]**
  * Group `3001`
    * `05` (start=3, mask=11111111b, comment=GWF_SBR_WARNDAUER)

### ACSM (CAFD 0000009C) — authored by ekfxisidF010 | Series: F010,F001,F007

* **Seat belt warning chime three times (5 seconds) [Changwon ll Daltanyang]**
  * Group `3001`
    * `05` (start=3, mask=11111111b, comment=GWF_SBR_WARNDAUER)

### ACSM (CAFD 000011AB) — authored by ekfxisidF010 | Series: F010,F001,F007

* **Seat belt warning chime three times (5 seconds) [Changwon ll Daltanyang]**
  * Group `3001`
    * `05` (start=11, mask=11111111b, comment=GWF_SBR_WARNDAUER)

### IHKA3 (CAFD 000016EE) — authored by ekfxisidF010 | Series: F010,F001,F007

* **Remember last A/C on/off state [Changwon ll Daltanyang]**
  * Group `3003`
    * `Aktiv` (start=0, mask=00000010b, comment=MEMORY_OFF)

* **Remember air recirculation mode**
  * Group `3003`
    * `Aktiv` (start=0, mask=00000001b, comment=MEMORY_UMLUFT)

* **Lock air recirculation mode**
  * Group `3003`
    * `disable` (start=0, mask=10000000b, comment=UMLUFT_AUTO_AUS)

### IHKA (CAFD 00000A3F) — authored by ekfxisidF010 | Series: F010,F001,F007

* **Remember last A/C on/off state [Changwon ll Daltanyang]**
  * Group `3002`
    * `Aktiv` (start=0, mask=00000010b, comment=MEMORY_OFF)

* **Remember air recirculation mode**
  * Group `3002`
    * `Aktiv` (start=0, mask=00000001b, comment=MEMORY_UMLUFT)

* **Prevent AUTO button from turning on A/C**
  * Group `3002`
    * `Aktiv` (start=0, mask=00000100b, comment=AC_NICHT_EIN_BEI_AUTO)

### IHKA (CAFD 00000092) — authored by ekfxisidF010 | Series: F010,F001,F007

* **Remember last A/C on/off state [Changwon ll Daltanyang]**
  * Group `3000`
    * `Aktiv` (start=5, mask=00010000b, comment=OFF_MEMORY)

* **Remember air recirculation mode**
  * Group `3000`
    * `Aktiv` (start=0, mask=00000100b, comment=MEMORY_UMLUFT)

* **Prevent AUTO button from turning on A/C**
  * Group `3000`
    * `Aktiv` (start=5, mask=00001000b, comment=AC_NICHT_EIN_BEI_AUTO)

### HKFM (CAFD 000007C8) — authored by ekfxisidF010 | Series: F010,F001,F007

* **Operate power trunk from interior button [Changwon ll Daltanyang]**
  * Group `3010`
    * `Aktiv` (start=2, mask=00001000b, comment=SCH_FBD)
    * `Aktiv` (start=2, mask=00000100b, comment=SCH_TOEHKI)
    * `Aktiv` (start=0, mask=00001000b, comment=TASTER_FBD)

### HKFM (CAFD 00000076) — authored by ekfxisidF010 | Series: F010,F001,F007

* **Operate power trunk from interior button [Changwon ll Daltanyang]**
  * Group `3010`
    * `Aktiv` (start=2, mask=00001000b, comment=SCH_FBD)
    * `Aktiv` (start=2, mask=00000100b, comment=SCH_TOEHKI)
    * `Aktiv` (start=0, mask=00001000b, comment=TASTER_FBD)

### KOMBI (CAFD 00000069) — authored by ekfxisidF010 | Series: F010,F001,F007

* **Enable Sport+ menu in cluster [Changwon ll Daltanyang]**
  * Group `300C`
    * `menue_3` (start=0, mask=00001111b, comment=FDS_MENUE_TEXT_1)
    * `menue_3` (start=0, mask=11110000b, comment=FDS_MENUE_SIGNAL_1)
    * `menue_3` (start=1, mask=00001111b, comment=FDS_MENUE_TEXT_2)
    * `menue_3` (start=1, mask=11110000b, comment=FDS_MENUE_SIGNAL_2)
    * `menue_3` (start=2, mask=00001111b, comment=FDS_MENUE_TEXT_3)
    * `menue_3` (start=2, mask=11110000b, comment=FDS_MENUE_SIGNAL_3)
    * `menue_3` (start=3, mask=00001111b, comment=FDS_MENUE_TEXT_4)
    * `menue_3` (start=3, mask=11110000b, comment=FDS_MENUE_SIGNAL_4)

* **Digital speedometer in instrument cluster**
  * Group `3000`
    * `Aktiv` (start=1, mask=00000010b, comment=BC_DIGITAL_V)
    * `nicht_aktiv` (start=1, mask=01000000b, comment=BC_V_KORREKTUR)

* **Show manual gear steps M1-M8 in DS mode**
  * Group `3000`
    * `Aktiv` (start=39, mask=00010000b, comment=SPA_SPORT_ENABLE)

* **Enable HUD entertainment**
  * Group `3000`
    * `Aktiv` (start=41, mask=00001000b, comment=HUD_ENTERTAINMENT_ENABLE)

* **Enable HUD phonebook**
  * Group `3000`
    * `Aktiv` (start=41, mask=00010000b, comment=HUD_TELEFONANRUF_ENABLE)
    * `Aktiv` (start=41, mask=00100000b, comment=HUD_TELEFONBUCH_ENABLE)
    * `Aktiv` (start=41, mask=01000000b, comment=HUD_SPRACHEINGABE_ENABLE)

### EGS (CAFD 0000023F) — authored by ekfxisidF010 | Series: F010,F001,F007

* **Display gear position S1-S8 in DS mode [Changwon ll Daltanyang]**
  * Group `3000`
    * `aktiv` (start=0, mask=01000000b, comment=SPORTSCHALTER_ALT)
    * `aktiv` (start=1, mask=00000001b, comment=SPORTSCHALTER)

### ICM (CAFD 0000067B) — authored by ekfxisidF010 | Series: F010,F001,F007

* **Enable Sport+ mode in cluster -> KOMBI [Changwon ll Daltanyang]**
  * Group `3000`
    * `verbaut` (start=18, mask=11111111b, comment=IcmKod_B_S2TBA)

* **Set ECO PRO as default driving mode**
  * Group `3000`
    * `verbaut` (start=36, mask=00001000b, comment=IcmKod_B_InitEco)

* **Enable cruise control -> KOMBI**
  * Group `3000`
    * `verbaut` (start=128, mask=00001110b, comment=C_Fahrfunktion)

### SM(6d) (CAFD 000000B5) — authored by ekfxisidF010 | Series: F010,F001,F007

* **Easy Access 1/3 (Easy Entry) [Changwon ll Daltanyang]**
  * Group `3000`
    * `Modus_FA_SLV` (start=0, mask=00011100b, comment=EINAUSSTIEGSHILFE)

* **Easy Access 2/3 (Easy Entry)**
  * Group `3012`
    * `00, 1E` (start=4, end=5, mask=11111111b, comment=EAH_SCHUTZFREIRAUM_HINTEN_SLV_PHYS)

* **Easy Access 3/3 (Easy Entry)**
  * Group `3012`
    * `00, 46` (start=0, end=1, mask=11111111b, comment=EAH_VERFAHRWEG_SLV_PHYS)

* **Set memory gong alert sound**
  * Group `3000`
    * `Aktiv` (start=2, mask=00001000b, comment=MEMORY_GONG)

* **Gentleman  --> SM(6e)**
  * Group `3000`
    * `aktiv` (start=1, mask=00000001b, comment=GENTELMAN)

### SM(6e) (CAFD 000000B6) — authored by ekfxisidF010 | Series: F010,F001,F007

* **Gentleman -> SM(6d) [Changwon ll Daltanyang]**
  * Group `3000`
    * `aktiv` (start=1, mask=00000001b, comment=GENTELMAN)

### HU_NBT (CAFD 00000DED) — authored by ekfxisidF010 | Series: F010,F001,F007

* **Unlock DMB/DVD/Navi while driving [Changwon ll Daltanyang]**
  * Group `3000`
    * `FF` (start=72, mask=11111111b, comment=SPEEDLOCK_X_KMH_MAX)
    * `FF` (start=71, mask=11111111b, comment=SPEEDLOCK_X_KMH_MIN)
    * `nicht_aktiv` (start=5, mask=00010000b, comment=VIDEO_FRONT_LOCKED)
    * `nicht_aktiv` (start=5, mask=00000100b, comment=VIDEO_HANDBRAKE)
    * `None` (start=57, mask=00000111b, comment=VIDEO_SPEEDLOCK_CONDITION)

* **M performance**
  * Group `3001`
    * `01` (start=62, mask=01111000b, comment=STARTUP_EMBLEM)

* **X - Drive**
  * Group `3000`
    * `aktiv` (start=5, mask=00000001b, comment=COMPASS)
    * `aktiv` (start=15, mask=00000001b, comment=X_VIEW)
    * `trajectory1` (start=26, mask=00110000b, comment=X_VIEW_GRAPHIC_SLOP)
    * `trajectory1` (start=26, mask=11000000b, comment=X_VIEW_GRAPHIC_ROLL)
    * `aktiv` (start=110, mask=00000010b, comment=MOMENTDISTRIBUTION_MENU)

* **Change warning sound**
  * Group `3002`
    * `rolls_royce` (start=26, mask=00111000b, comment=SOUND_SIGNAL_SET)

* **Enable USB video playback 1/2**
  * Group `3000`
    * `aktiv` (start=15, mask=00010000b, comment=ENT_CODEC_OGG)
    * `aktiv` (start=15, mask=00100000b, comment=ENT_CODEC_XVID)
    * `aktiv` (start=15, mask=01000000b, comment=ENT_CODEC_VCD)
    * `aktiv` (start=13, mask=00000100b, comment=ENT_MC_VIDEO_SUPPORT)

* **Enable USB video playback 2/2**
  * Group `3003`
    * `both` (start=33, mask=00000110b, comment=API_USB_VIDEO)
    * `both` (start=33, mask=00011000b, comment=API_IPOD_VIEDO)

* **Remove all warning messages**
  * Group `3001`
    * `00` (start=52, mask=11111111b, comment=MACRO_CAM_LEGALDISCLAIMER)
    * `00` (start=58, mask=11111111b, comment=LEGAL_DISCLAIMER_TIME)

* **Enable automatic time setting**
  * Group `3000`
    * `navigation` (start=19, mask=00000110b, comment=SETTINGS_TIME_AUTOMATIC)
    * `aktiv` (start=105, mask=00100000b, comment=CLOCK_CHANGE_AUTOMATIC)

* **Enable rear camera zoom**
  * Group `3001`
    * `aktiv` (start=54, mask=00000001b, comment=MACRO_TRAILER_COUPLING)

* **Enable volume adjustment display**
  * Group `3002`
    * `01` (start=52, mask=01000000b, comment=VOLUME_POPUP_DISPLAY)

* **Enable daylight running lights**
  * Group `3000`
    * `02` (start=92, mask=00011000b, comment=DAYDRIVING_LIGHT)

* **Output ringtone through speakers (iOS only)**
  * Group `3003`
    * `aktiv` (start=6, mask=10000000b, comment=INBAND_RINGING)

* **Configure Sport mode 1/3**
  * Group `3000`
    * `aktiv` (start=101, mask=00010000b, comment=EFF_DYN_SPORT_CID)

* **Configure Sport mode 2/3**
  * Group `3000`
    * `aktiv` (start=107, mask=00000100b, comment=EFF_DYN_SPORT_UNIT)

* **Configure Sport mode 3/3**
  * Group `3001`
    * `popup_and_config` (start=55, mask=00011000b, comment=MACRO_FDS)

* **Bang & Olufsen profile**
  * Group `3000`
    * `keine_insz` (start=21, mask=01100000b, comment=HIGH_END_AUDIO_B_UND_W)

* **Enable Logic7 (S667A HiFi vehicles)**
  * Group `3000`
    * `aktiv` (start=22, mask=00001000b, comment=LOGIC7_SYMBOL)

* **Door lock/unlock chime (anti-theft module vehicles except M5)**
  * Group `3000`
    * `Aktiv` (start=110, mask=00000001b, comment=ACOUSTICAL_LOCK_CONFIRM)

* **Enable TPMC tire pressure temperature**
  * Group `3001`
    * `Aktiv` (start=1, mask=00100000b, comment=RDC_SAFETY)

* **Change M Sport display cluster colors**
  * Group `3000`
    * `aktiv` (start=133, mask=01000000b, comment=M_VEHICLE)

* **High-beam assistant 4/4 -->> KAFAS2 1/4, FRM 2/4, 3/4**
  * Group `3000`
    * `01` (start=109, mask=10000000b, comment=HIGH_BEAM_ASSISTANT)

### HU_CIC (CAFD 000000F9) — authored by ekfxisidF010 | Series: F010,F001,F007

* **Unlock DMB/DVD/Navi while driving [Changwon ll Daltanyang]**
  * Group `3000`
    * `FF` (start=23, mask=11111111b, comment=SPEEDLOCK_X_KMH_MAX)
    * `FF` (start=24, mask=11111111b, comment=SPEEDLOCK_X_KMH_MIN)
    * `nicht_aktiv` (start=8, mask=01000000b, comment=VIDEO_NUR_MIT_HANDBREMSE)

* **Enable rear camera zoom**
  * Group `3001`
    * `aktiv` (start=23, mask=00000001b, comment=MACRO_TRAILER_COUPLING)

* **Configure Sport mode 1/3**
  * Group `3000`
    * `aktiv` (start=47, mask=00010000b, comment=EFF_DYN_SPORT_CID)

* **Configure Sport mode 2/3**
  * Group `3000`
    * `aktiv` (start=61, mask=00000100b, comment=EFF_DYN_SPORT_UNIT)

* **Configure Sport mode 3/3**
  * Group `3000`
    * `popup_and_config` (start=7, mask=00110000b, comment=MACRO_FDS)

### HU_NBT2 (CAFD 00001EF6) — authored by ekfxisidF010 | Series: F010,F001,F007

* **Unlock DMB/DVD/Navi while driving 1/2 [Changwon ll Daltanyang]**
  * Group `3006`
    * `FF` (start=25, mask=11111111b, comment=SPEEDLOCK_X_KMH_MAX)
    * `FF` (start=26, mask=11111111b, comment=SPEEDLOCK_X_KMH_MIN)

* **Unlock DMB/DVD/Navi while driving 2/2**
  * Group `3000`
    * `nicht_aktiv` (start=5, mask=00010000b, comment=VIDEO_FRONT_LOCKED)
    * `nicht_aktiv` (start=5, mask=00000100b, comment=VIDEO_HANDBRAKE)
    * `None` (start=2, mask=00000111b, comment=VIDEO_SPEEDLOCK_CONDITION)

* **M performance**
  * Group `3001`
    * `01` (start=62, mask=01111000b, comment=STARTUP_EMBLEM)

* **X - Drive**
  * Group `3000`
    * `aktiv` (start=5, mask=00000001b, comment=COMPASS)
    * `aktiv` (start=15, mask=00000001b, comment=X_VIEW)
    * `trajectory1` (start=26, mask=00110000b, comment=X_VIEW_GRAPHIC_SLOP)
    * `trajectory1` (start=26, mask=11000000b, comment=X_VIEW_GRAPHIC_ROLL)
    * `aktiv` (start=110, mask=00000010b, comment=MOMENTDISTRIBUTION_MENU)

* **Change warning sound**
  * Group `3002`
    * `rolls_royce` (start=26, mask=00111000b, comment=SOUND_SIGNAL_SET)

* **Enable USB video playback 1/2**
  * Group `3000`
    * `aktiv` (start=15, mask=00010000b, comment=ENT_CODEC_OGG)
    * `aktiv` (start=15, mask=00100000b, comment=ENT_CODEC_XVID)
    * `aktiv` (start=15, mask=01000000b, comment=ENT_CODEC_VCD)
    * `aktiv` (start=13, mask=00000100b, comment=ENT_MC_VIDEO_SUPPORT)

* **Enable USB video playback 2/2**
  * Group `3003`
    * `both` (start=33, mask=00000110b, comment=API_USB_VIDEO)
    * `both` (start=33, mask=00011000b, comment=API_IPOD_VIEDO)

* **Remove all warning messages**
  * Group `3001`
    * `00` (start=52, mask=11111111b, comment=MACRO_CAM_LEGALDISCLAIMER)
    * `00` (start=58, mask=11111111b, comment=LEGAL_DISCLAIMER_TIME)

* **Enable automatic time setting**
  * Group `3000`
    * `navigation` (start=19, mask=00000110b, comment=SETTINGS_TIME_AUTOMATIC)
    * `aktiv` (start=105, mask=00100000b, comment=CLOCK_CHANGE_AUTOMATIC)

* **Enable rear camera zoom**
  * Group `3001`
    * `aktiv` (start=54, mask=00000001b, comment=MACRO_TRAILER_COUPLING)

* **Enable daylight running lights**
  * Group `3000`
    * `02` (start=92, mask=00011000b, comment=DAYDRIVING_LIGHT)

* **Output ringtone through speakers (iOS only)**
  * Group `3003`
    * `aktiv` (start=6, mask=10000000b, comment=INBAND_RINGING)

* **Configure Sport mode 1/3**
  * Group `3009`
    * `aktiv` (start=9, mask=00010000b, comment=EFF_DYN_SPORT_CID)

* **Configure Sport mode 2/3**
  * Group `3009`
    * `aktiv` (start=9, mask=00100000b, comment=EFF_DYN_SPORT_UNIT)

* **Configure Sport mode 3/3**
  * Group `3008`
    * `popup_and_config` (start=79, mask=11000000b, comment=MACRO_FDS)

* **Bang & Olufsen profile**
  * Group `3000`
    * `keine_insz` (start=21, mask=01100000b, comment=HIGH_END_AUDIO_B_UND_W)

* **Enable Logic7 (S667A HiFi vehicles)**
  * Group `3000`
    * `aktiv` (start=22, mask=00001000b, comment=LOGIC7_SYMBOL)

* **HUD : Affichage de l'assistant collision Step 2 (Step 1 dans KOMBI)**
  * Group `300C`
    * `Aktiv` (start=0, mask=00010000b, comment=HUD_DISTANCE_INFO)

* **Door lock/unlock chime**
  * Group `3000`
    * `Aktiv` (start=110, mask=00000001b, comment=ACOUSTICAL_LOCK_CONFIRM)

* **Enable TPMC tire pressure temperature**
  * Group `3001`
    * `Aktiv` (start=1, mask=00100000b, comment=RDC_SAFETY)

* **Change M Sport display cluster colors**
  * Group `3000`
    * `aktiv` (start=133, mask=01000000b, comment=M_VEHICLE)

* **High-beam assistant 4/4 -->> KAFAS2 1/4, FRM 2/4, 3/4**
  * Group `3000`
    * `01` (start=109, mask=10000000b, comment=HIGH_BEAM_ASSISTANT)

### BDC_01 (CAFD 000017BE) — authored by ekfxisidF025 | Series: F015,F016,F025

* **Turn off audio and navigation when door opens after engine off [Changwon ll Daltanyang]**
  * Group `3020`
    * `aktiv` (start=9, mask=00000001b, comment=TCM_LOGIC_R_OFF_DOOR)

* **Remember last auto start/stop state**
  * Group `3023`
    * `aktiv` (start=0, mask=00100000b, comment=TCM_MSA_MEMORY)

* **Turn off auto start/stop in ECO Pro mode**
  * Group `3023`
    * `nicht_aktiv` (start=1, mask=00000100b, comment=TCM_MSA_ECO_MODE)

* **Turn off auto start/stop in Comfort mode**
  * Group `3023`
    * `aktiv` (start=0, mask=00010000b, comment=TCM_MSA_DEFAULT_OFF)

* **Allow windows to operate with doors open**
  * Group `3050`
    * `nicht_aktiv` (start=0, mask=00000001b, comment=FH_TUERAUF_STOP_MAUT)

* **Mirror lock folding (one-touch)**
  * Group `3056`
    * `00` (start=10, mask=11111111b, comment=KOMFORT_SCHLIESSEN)

* **Passenger mirror angle adjustment**
  * Group `3110`
    * `1E` (start=1, mask=11111111b, comment=ASP_BORDSTEINAUTOMAIK_DELTA)

* **Turn signal flashes five times**
  * Group `3068`
    * `04` (start=7, mask=00000111b, comment=BLINKZYKLEN_ANZAHL_TIPP)

* **Flash hazard lights during hard braking(50km/h)**
  * Group `3068`
    * `aktiv` (start=26, mask=00000001b, comment=WB_GB_ENABLE)
    * `00, 32` (start=23, end=24, mask=11111111b, comment=WB_GB_GEFAHRENWERT_MIN)

* **Enable dynamic brake lights**
  * Group `3068`
    * `bremslicht_blinkend` (start=16, mask=00000011b, comment=ESS_AKTIVIERBARER_AUSGANG)
    * `04` (start=20, mask=00011111b, comment=ESS_AKTIVIERUNG_REALE_VERZ)
    * `04` (start=19, mask=00011111b, comment=ESS_DEAKTIVIERUNG_REALE_VERZ)
    * `05` (start=17, mask=11111110b, comment=ESS_AKTIVIERUNG_GESCHW)

* **Auto unfold mirrors above set speed (40 km/h -> 25 km/h)**
  * Group `3110`
    * `19` (start=9, mask=11111111b, comment=ASP_GESCHWINDIGKEIT_AUTO_AUSKLAPPEN)

* **Illuminate door handle lights in reverse**
  * Group `3070`
    * `aktiv` (start=128, mask=00000001b, comment=OVT_BEI_RUECKFAHRLICHT)

* **Front turn signals -> convert to LED**
  * Group `3060`
    * `nicht_aktiv` (start=98, mask=00000001b, comment=FRA_V_L_KALTUEBERWACHUNG)
    * `nicht_aktiv` (start=98, mask=00000010b, comment=FRA_V_L_WARMUEBERWACHUNG)
    * `aktiv` (start=98, mask=00000100b, comment=FRA_V_L_KURZSCHLUSS)
    * `aktiv` (start=98, mask=00001000b, comment=FRA_V_L_IS_LED)
    * `nicht_aktiv` (start=106, mask=00000001b, comment=FRA_V_R_KALTUEBERWACHUNG)
    * `nicht_aktiv` (start=106, mask=00000010b, comment=FRA_V_R_WARMUEBERWACHUNG)
    * `aktiv` (start=106, mask=00000100b, comment=FRA_V_R_KURZSCHLUSS)
    * `aktiv` (start=106, mask=00001000b, comment=FRA_V_R_IS_LED)

* **Rear turn signals -> convert to LED**
  * Group `3061`
    * `nicht_aktiv` (start=98, mask=00000001b, comment=FRA_H_L_KALTUEBERWACHUNG)
    * `nicht_aktiv` (start=98, mask=00000010b, comment=FRA_H_L_WARMUEBERWACHUNG)
    * `aktiv` (start=98, mask=00000100b, comment=FRA_H_L_KURZSCHLUSS)
    * `aktiv` (start=98, mask=00001000b, comment=FRA_H_L_IS_LED)
    * `nicht_aktiv` (start=106, mask=00000001b, comment=FRA_H_R_KALTUEBERWACHUNG)
    * `nicht_aktiv` (start=106, mask=00000010b, comment=FRA_H_R_WARMUEBERWACHUNG)
    * `aktiv` (start=106, mask=00000100b, comment=FRA_H_R_KURZSCHLUSS)
    * `aktiv` (start=106, mask=00001000b, comment=FRA_H_R_IS_LED)

* **Front fog lights -> convert to LED and remove warning**
  * Group `3060`
    * `nicht_aktiv` (start=82, mask=00000001b, comment=NSW_L_KALTUEBERWACHUNG)
    * `nicht_aktiv` (start=82, mask=00000010b, comment=NSW_L_WARMUEBERWACHUNG)
    * `aktiv` (start=82, mask=00000100b, comment=NSW_L_KURZSCHLUSS)
    * `aktiv` (start=82, mask=00001000b, comment=NSW_L_IS_LED)
    * `nicht_aktiv` (start=90, mask=00000001b, comment=NSW_R_KALTUEBERWACHUNG)
    * `nicht_aktiv` (start=90, mask=00000010b, comment=NSW_R_WARMUEBERWACHUNG)
    * `aktiv` (start=90, mask=00000100b, comment=NSW_R_KURZSCHLUSS)
    * `aktiv` (start=90, mask=00001000b, comment=NSW_R_IS_LED)

* **Daytime tail lamps synchronized with daytime headlights 1/3**
  * Group `3068`
    * `drl_s` (start=31, mask=00110000b, comment=TFL_MODUS)

* **Daytime tail lamps synchronized with daytime headlights 2/3**
  * Group `3064`
    * `sl_l` (start=221, mask=00111111b, comment=MAPPING_TAGFAHRL_1_H_L_OUTPUT)
    * `sl_r` (start=234, mask=00111111b, comment=MAPPING_TAGFAHRL_1_H_R_OUTPUT)

* **Daytime tail lamps synchronized with daytime headlights 3/3**
  * Group `3065`
    * `sl_2_l` (start=78, mask=00111111b, comment=MAPPING_TAGFAHRL_2_H_L_OUTPUT)
    * `sl_2_r` (start=91, mask=00111111b, comment=MAPPING_TAGFAHRL_2_H_R_OUTPUT)

### ACSM_4C (CAFD 00000909) — authored by ekfxisidF025 | Series: F015,F016,F025

* **Seat belt warning chime three times (5 seconds) [Changwon ll Daltanyang]**
  * Group `3001`
    * `05` (start=3, mask=11111111b, comment=GWF_SBR_WARNDAUER)

### ACSM (CAFD 000011AB) — authored by ekfxisidF025 | Series: F015,F016,F025,F026

* **Seat belt warning chime three times (5 seconds) [Changwon ll Daltanyang]**
  * Group `3001`
    * `05` (start=11, mask=11111111b, comment=GWF_SBR_WARNDAUER)

### KAFAS2 (CAFD 00001148) — authored by ekfxisidF025 | Series: F015,F016,F025

* **High-beam assistant 1/4 -> code this first to avoid errors**
  * Group `3050`
    * `FLA_on` (start=1, mask=00000001b, comment=FLA_ON_OFF)

### HKFM (CAFD 000007C8) — authored by ekfxisidF025 | Series: F015,F016,F025

* **Operate power trunk from interior button [Changwon ll Daltanyang]**
  * Group `3010`
    * `Aktiv` (start=2, mask=00001000b, comment=SCH_FBD)
    * `Aktiv` (start=2, mask=00000100b, comment=SCH_TOEHKI)
    * `Aktiv` (start=0, mask=00001000b, comment=TASTER_FBD)

### IHKA3 (CAFD 000016EE) — authored by ekfxisidF025 | Series: F015,F016,F025,F026

* **Remember last A/C on/off state [Changwon ll Daltanyang]**
  * Group `3003`
    * `Aktiv` (start=0, mask=00000010b, comment=MEMORY_OFF)

* **Remember air recirculation mode**
  * Group `3003`
    * `Aktiv` (start=0, mask=00000001b, comment=MEMORY_UMLUFT)

* **Lock air recirculation mode**
  * Group `3003`
    * `disable` (start=0, mask=10000000b, comment=UMLUFT_AUTO_AUS)

### ICM (CAFD 0000067B) — authored by ekfxisidF025 | Series: F015,F016,F025

* **Enable Sport+ mode in cluster -> KOMBI [Changwon ll Daltanyang]**
  * Group `3000`
    * `verbaut` (start=28, mask=11111111b, comment=IcmKod_B_Sportlenkung)

* **Set ECO PRO as default driving mode**
  * Group `3000`
    * `verbaut` (start=36, mask=00001000b, comment=IcmKod_B_InitEco)

* **Enable cruise control -> KOMBI**
  * Group `3000`
    * `verbaut` (start=128, mask=00001110b, comment=C_Fahrfunktion)

### KOMBI (CAFD 00000069) — authored by ekfxisidF025 | Series: F015,F016,F025

* **Enable Sport+ menu in cluster [Changwon ll Daltanyang]**
  * Group `300C`
    * `menue_3` (start=0, mask=00001111b, comment=FDS_MENUE_TEXT_1)
    * `menue_3` (start=0, mask=11110000b, comment=FDS_MENUE_SIGNAL_1)
    * `menue_3` (start=1, mask=00001111b, comment=FDS_MENUE_TEXT_2)
    * `menue_3` (start=1, mask=11110000b, comment=FDS_MENUE_SIGNAL_2)
    * `menue_3` (start=2, mask=00001111b, comment=FDS_MENUE_TEXT_3)
    * `menue_3` (start=2, mask=11110000b, comment=FDS_MENUE_SIGNAL_3)
    * `menue_3` (start=3, mask=00001111b, comment=FDS_MENUE_TEXT_4)
    * `menue_3` (start=3, mask=11110000b, comment=FDS_MENUE_SIGNAL_4)

* **Digital speedometer in instrument cluster**
  * Group `3000`
    * `Aktiv` (start=1, mask=00000010b, comment=BC_DIGITAL_V)
    * `nicht_aktiv` (start=1, mask=01000000b, comment=BC_V_KORREKTUR)

* **Show manual gear steps M1-M8 in DS mode**
  * Group `3000`
    * `Aktiv` (start=39, mask=00010000b, comment=SPA_SPORT_ENABLE)

* **Enable HUD entertainment**
  * Group `3000`
    * `Aktiv` (start=41, mask=00001000b, comment=HUD_ENTERTAINMENT_ENABLE)

* **Enable HUD phonebook**
  * Group `3000`
    * `Aktiv` (start=41, mask=00010000b, comment=HUD_TELEFONANRUF_ENABLE)
    * `Aktiv` (start=41, mask=00100000b, comment=HUD_TELEFONBUCH_ENABLE)
    * `Aktiv` (start=41, mask=01000000b, comment=HUD_SPRACHEINGABE_ENABLE)

### KOMBI (CAFD 000009C8) — authored by ekfxisidF025 | Series: F015,F016,F025,F026

* **Enable Sport+ menu in cluster [Changwon ll Daltanyang]**
  * Group `300C`
    * `menue_3` (start=54, mask=11111111b, comment=FDS_MENUE)

* **Digital speedometer in instrument cluster**
  * Group `3000`
    * `Aktiv` (start=1, mask=00000010b, comment=BC_DIGITAL_V)
    * `nicht_aktiv` (start=1, mask=01000000b, comment=BC_V_KORREKTUR)

* **Logo M performance**
  * Group `3000`
    * `01` (start=0, mask=11110000b, comment=BMW_LOGO)

* **Move instrument cluster clock**
  * Group `3000`
    * `Aktiv` (start=53, mask=01000000b, comment=BASISANZEEIGE_VARIANTE)

### SM2 (CAFD 000000B5) — authored by ekfxisidF025 | Series: F015,F016,F025

* **Easy Access 1/3 (Easy Entry) [Changwon ll Daltanyang]**
  * Group `3000`
    * `Modus_FA_SLV` (start=0, mask=00011100b, comment=EINAUSSTIEGSHILFE)

* **Easy Access 2/3 (Easy Entry)**
  * Group `3012`
    * `00, 1E` (start=4, end=5, mask=11111111b, comment=EAH_SCHUTZFREIRAUM_HINTEN_SLV_PHYS)

* **Easy Access 3/3 (Easy Entry)**
  * Group `3012`
    * `00, 46` (start=0, end=1, mask=11111111b, comment=EAH_VERFAHRWEG_SLV_PHYS)

* **Set memory gong alert sound**
  * Group `3000`
    * `Aktiv` (start=2, mask=00001000b, comment=MEMORY_GONG)

### CAS_04 (CAFD 0000000F) — authored by ekfxisidF025 | Series: F015,F016,F025

* **Auto start/stop default off [Changwon ll Daltanyang]**
  * Group `3000`
    * `01` (start=3, mask=00010000b, comment=TCM_MSA_DEFAULT_OFF)

* **Remember last auto start/stop state**
  * Group `3000`
    * `aktiv` (start=3, mask=00100000b, comment=TCM_MSA_MEMORY)

* **Start engine without pressing brake 1/2**
  * Group `3000`
    * `nicht_aktiv` (start=1, mask=00000001b, comment=TC_STARTLOCK_BRAKE)

* **Start engine without pressing brake 2/2**
  * Group `3000`
    * `nicht_aktiv` (start=1, mask=00010000b, comment=TC_STARTLOCK_DRIVINGREADINESS)

* **Mirror lock folding**
  * Group `3003`
    * `00` (start=12, mask=11111111b, comment=KMFRT_SCHLESSEN)

* **Turn off audio/navigation when door opens after shutdown**
  * Group `3000`
    * `aktiv` (start=2, mask=00000001b, comment=TC_LOGIC_KLR_OFF_DOOR)

* **Horn alarm when locking with engine running**
  * Group `3002`
    * `aktiv` (start=0, mask=00100000b, comment=CLM_HORN_AT_SECURE)

### FRM (CAFD 0000012F) — authored by ekfxisidF025 | Series: F015,F016,F025

* **High-beam assistant 2/4 -> code KAFAS2 1/4 first [Changwon ll Daltanyang]**
  * Group `3050`
    * `aktiv` (start=20, mask=00010000b, comment=FLA_VERBAUT)

* **High-beam assistant 3/4 -> code HU_NBT 4/4 last**
  * Group `3050`
    * `automatisch` (start=20, mask=00100000b, comment=FLA_AUTO_AKTIV)

* **Passenger mirror angle adjustment**
  * Group `3020`
    * `1E` (start=1, mask=11111111b, comment=ASP_BORDSTEINAUTOMAIK_DELTA)

* **Auto unfold mirrors above set speed (40 km/h -> 25 km/h)**
  * Group `3020`
    * `19` (start=9, mask=11111111b, comment=ASP_GESCHWINDIGKEIT_AUTO_AUSKLAPPEN)

* **Allow windows to operate with doors open 1/2 (front) -> JBBF 2/2 (rear)**
  * Group `3030`
    * `nicht aktiv` (start=1, mask=00000100b, comment=FH_TUER_AUF_STOP_MAUT)

* **Daytime tail lamps**
  * Group `3050`
    * `drl_s` (start=20, mask=00001110b, comment=DRL_MODUS)

* **Enable dynamic brake lights**
  * Group `3050`
    * `bremslicht blinkend` (start=23, mask=01110000b, comment=ESS_ERSCHEINUNGSBILD)
    * `US` (start=24, mask=01111111b, comment=ESS_GESCHW_SCHWELLE)
    * `04` (start=21, mask=00011111b, comment=ESS_ON_VERZ)
    * `04` (start=22, mask=00011111b, comment=ESS_OFF_VERZ)

* **Flash hazard lights during hard braking**
  * Group `3050`
    * `aktiv` (start=2, mask=10000000b, comment=WB_GB_ENABLE)

* **Increase Angel Eye brightness to 30%**
  * Group `3060`
    * `1E` (start=1, mask=11111111b, comment=U_EFF_POL)

* **Welcome light fog lamps (hard on)**
  * Group `3050`
    * `Hard_on` (start=29, mask=00001100b, comment=WL_FUNKTION_NSW)

* **Welcome light fog lamps (soft on)**
  * Group `3050`
    * `Soft_on` (start=29, mask=00001100b, comment=WL_FUNKTION_NSW)

* **Front fog lights -> convert to LED and remove warning**
  * Group `3090`
    * `00` (start=79, mask=00000001b, comment=AUSG_11_NSW_L_WARM_UEBERW_AKTIV)
    * `00` (start=79, mask=00000010b, comment=AUSG_11_NSW_L_KALT_UEBERW_AKTIV)
    * `aktiv` (start=79, mask=00001000b, comment=AUSG_11_NSW_L_IS_LED)
    * `00` (start=83, mask=00000001b, comment=AUSG_11_NSW_R_WARM_UEBERW_AKTIV)
    * `00` (start=83, mask=00000010b, comment=AUSG_11_NSW_R_KALT_UEBERW_AKTIV)
    * `aktiv` (start=83, mask=00001000b, comment=AUSG_11_NSW_R_IS_LED)

* **Reverse lights -> convert to LED**
  * Group `3090`
    * `nicht_aktiv` (start=131, mask=00000001b, comment=AUSG_24_RFS_L_WARM_UEBERW_AKTIV)
    * `nicht_aktiv` (start=131, mask=00000010b, comment=AUSG_24_RFS_L_KALT_UEBERW_AKTIV)
    * `aktiv` (start=131, mask=00001000b, comment=AUSG_24_RFS_L_IS_LED)
    * `nicht_aktiv` (start=135, mask=00000001b, comment=AUSG_24_RFS_R_WARM_UEBERW_AKTIV)
    * `nicht_aktiv` (start=135, mask=00000010b, comment=AUSG_24_RFS_R_KALT_UEBERW_AKTIV)
    * `aktiv` (start=135, mask=00001000b, comment=AUSG_24_RFS_R_IS_LED)

### JBBFE (CAFD 00000014) — authored by ekfxisidF025 | Series: F015,F016,F025

* **Disable headlight washer fluid [Changwon ll Daltanyang]**
  * Group `3000`
    * `nicht_aktiv` (start=8, mask=00000001b, comment=SCHEINWERFERREINIGUNG)

* **Allow windows to operate when door open 2/2 (rear)**
  * Group `3070`
    * `nicht_aktiv` (start=0, mask=00000100b, comment=FH_TUERAUF_STOP_MAUT)

* **Adjust automatic light sensor**
  * Group `3530`
    * `unempfindlich` (start=5, mask=00111000b, comment=RLS_FLC_SCHWELLWERT_SATZ)

* **Adjust rain sensor**
  * Group `3530`
    * `unempfindlich` (start=5, mask=00000111b, comment=RLS_DEF_FLC_SCHWELLWERT_SATZ)

### HU_CIC (CAFD 000000F9) — authored by ekfxisidF025 | Series: F015,F016,F025

* **Unlock DMB/DVD/Navi while driving [Changwon ll Daltanyang]**
  * Group `3000`
    * `FF` (start=23, mask=11111111b, comment=SPEEDLOCK_X_KMH_MAX)
    * `FF` (start=24, mask=11111111b, comment=SPEEDLOCK_X_KMH_MIN)
    * `nicht_aktiv` (start=8, mask=01000000b, comment=VIDEO_NUR_MIT_HANDBREMSE)

* **Enable rear camera zoom**
  * Group `3001`
    * `aktiv` (start=23, mask=00000001b, comment=MACRO_TRAILER_COUPLING)

* **Configure Sport mode 1/3**
  * Group `3000`
    * `aktiv` (start=47, mask=00010000b, comment=EFF_DYN_SPORT_CID)

* **Configure Sport mode 2/3**
  * Group `3000`
    * `aktiv` (start=61, mask=00000100b, comment=EFF_DYN_SPORT_UNIT)

* **Configure Sport mode 3/3**
  * Group `3000`
    * `popup_and_config` (start=7, mask=00110000b, comment=MACRO_FDS)

### FRM (CAFD 0000106D) — authored by ekfxisidF025 | Series: F015,F016,F025

* **High-beam assistant 2/4 -> code KAFAS2 1/4 first [Changwon ll Daltanyang]**
  * Group `3050`
    * `aktiv` (start=20, mask=00010000b, comment=FLA_VERBAUT)

* **High-beam assistant 3/4 -> code HU_NBT 4/4 last**
  * Group `3050`
    * `automatisch` (start=20, mask=00100000b, comment=FLA_AUTO_AKTIV)

* **Passenger mirror angle adjustment**
  * Group `3020`
    * `1E` (start=1, mask=11111111b, comment=ASP_BORDSTEINAUTOMAIK_DELTA)

* **Auto unfold mirrors above set speed (40 km/h -> 25 km/h)**
  * Group `3020`
    * `19` (start=9, mask=11111111b, comment=ASP_GESCHWINDIGKEIT_AUTO_AUSKLAPPEN)

* **Allow windows to operate with doors open 1/2 (front) -> JBBF 2/2 (rear)**
  * Group `3030`
    * `nicht aktiv` (start=1, mask=00000100b, comment=FH_TUER_AUF_STOP_MAUT)

* **Daytime tail lamps**
  * Group `3050`
    * `drl_s` (start=20, mask=00001110b, comment=DRL_MODUS)

* **Enable dynamic brake lights**
  * Group `3050`
    * `02` (start=23, mask=01110000b, comment=ESS_ERSCHEINUNGSBILD)
    * `US` (start=24, mask=01111111b, comment=ESS_GESCHW_SCHWELLE)
    * `04` (start=21, mask=00011111b, comment=ESS_ON_VERZ)
    * `04` (start=22, mask=00011111b, comment=ESS_OFF_VERZ)

* **Flash hazard lights during hard braking**
  * Group `3050`
    * `aktiv` (start=2, mask=10000000b, comment=WB_GB_ENABLE)

* **Increase Angel Eye brightness to 30%**
  * Group `3060`
    * `1E` (start=1, mask=11111111b, comment=U_EFF_POL)

* **Welcome light fog lamps (hard on)**
  * Group `3050`
    * `Hard_on` (start=29, mask=00001100b, comment=WL_FUNKTION_NSW)

* **Welcome light fog lamps (soft on)**
  * Group `3050`
    * `Soft_on` (start=29, mask=00001100b, comment=WL_FUNKTION_NSW)

* **Front fog lights -> convert to LED and remove warning**
  * Group `3090`
    * `00` (start=79, mask=00000001b, comment=AUSG_11_NSW_L_WARM_UEBERW_AKTIV)
    * `00` (start=79, mask=00000010b, comment=AUSG_11_NSW_L_KALT_UEBERW_AKTIV)
    * `aktiv` (start=79, mask=00001000b, comment=AUSG_11_NSW_L_IS_LED)
    * `00` (start=83, mask=00000001b, comment=AUSG_12_NSW_R_WARM_UEBERW_AKTIV)
    * `00` (start=83, mask=00000010b, comment=AUSG_12_NSW_R_KALT_UEBERW_AKTIV)
    * `aktiv` (start=83, mask=00001000b, comment=AUSG_12_NSW_R_IS_LED)

* **Reverse lights -> convert to LED**
  * Group `3090`
    * `nicht_aktiv` (start=131, mask=00000001b, comment=AUSG_24_RFS_L_WARM_UEBERW_AKTIV)
    * `nicht_aktiv` (start=131, mask=00000010b, comment=AUSG_24_RFS_L_KALT_UEBERW_AKTIV)
    * `aktiv` (start=131, mask=00001000b, comment=AUSG_24_RFS_L_IS_LED)
    * `nicht_aktiv` (start=135, mask=00000001b, comment=AUSG_25_RFS_R_WARM_UEBERW_AKTIV)
    * `nicht_aktiv` (start=135, mask=00000010b, comment=AUSG_25_RFS_R_KALT_UEBERW_AKTIV)
    * `aktiv` (start=135, mask=00001000b, comment=AUSG_25_RFS_R_IS_LED)

### HU_NBT2 (CAFD 00001EF6) — authored by ekfxisidF025 | Series: F015,F016,F025,F026

* **Unlock DMB/DVD/Navi while driving [Changwon ll Daltanyang]**
  * Group `3006`
    * `FF` (start=25, mask=11111111b, comment=SPEEDLOCK_X_KMH_MIN)
    * `FF` (start=26, mask=11111111b, comment=SPEEDLOCK_X_KMH_MAX)

* **M performance**
  * Group `3001`
    * `01` (start=62, mask=01111000b, comment=STARTUP_EMBLEM)

* **X - Drive**
  * Group `3000`
    * `aktiv` (start=5, mask=00000001b, comment=COMPASS)
    * `aktiv` (start=15, mask=00000001b, comment=X_VIEW)

* **Change warning sound**
  * Group `3002`
    * `rolls_royce` (start=26, mask=00111000b, comment=SOUND_SIGNAL_SET)

* **Enable USB video**
  * Group `3000`
    * `aktiv` (start=15, mask=00010000b, comment=ENT_CODEC_OGG)
    * `aktiv` (start=15, mask=00100000b, comment=ENT_CODEC_XVID)
    * `aktiv` (start=15, mask=01000000b, comment=ENT_CODEC_VCD)
    * `aktiv` (start=13, mask=00000100b, comment=ENT_MC_VIDEO_SUPPORT)
  * Group `3003`
    * `both` (start=33, mask=00000110b, comment=API_USB_VIDEO)
    * `both` (start=33, mask=00011000b, comment=API_IPOD_VIEDO)

* **Remove all warning messages**
  * Group `3001`
    * `00` (start=52, mask=11111111b, comment=MACRO_CAM_LEGALDISCLAIMER)
    * `00` (start=58, mask=11111111b, comment=LEGAL_DISCLAIMER_TIME)

* **Enable automatic time setting**
  * Group `3000`
    * `navigation` (start=19, mask=00000110b, comment=SETTINGS_TIME_AUTOMATIC)
    * `aktiv` (start=105, mask=00100000b, comment=CLOCK_CHANGE_AUTOMATIC)

* **Enable rear camera zoom**
  * Group `3001`
    * `aktiv` (start=54, mask=00000001b, comment=MACRO_TRAILER_COUPLING)

* **Output ringtone through speakers (iOS only)**
  * Group `3003`
    * `aktiv` (start=6, mask=10000000b, comment=INBAND_RINGING)

* **Configure Sport mode**
  * Group `3009`
    * `aktiv` (start=9, mask=00010000b, comment=EFF_DYN_SPORT_CID)
  * Group `3009`
    * `aktiv` (start=9, mask=00100000b, comment=EFF_DYN_SPORT_UNIT)
  * Group `3008`
    * `popup_and_config` (start=79, mask=11000000b, comment=MACRO_FDS)

### HU_NBT (CAFD 00000DED) — authored by ekfxisidF025 | Series: F015,F016,F025

* **Unlock DMB/DVD/Navi while driving [Changwon ll Daltanyang]**
  * Group `3000`
    * `FF` (start=72, mask=11111111b, comment=SPEEDLOCK_X_KMH_MAX)
    * `FF` (start=71, mask=11111111b, comment=SPEEDLOCK_X_KMH_MIN)
    * `nicht_aktiv` (start=5, mask=00010000b, comment=VIDEO_FRONT_LOCKED)
    * `nicht_aktiv` (start=5, mask=00000100b, comment=VIDEO_HANDBRAKE)
    * `None` (start=57, mask=00000111b, comment=VIDEO_SPEEDLOCK_CONDITION)

* **M performance**
  * Group `3001`
    * `01` (start=62, mask=01111000b, comment=STARTUP_EMBLEM)

* **X - Drive**
  * Group `3000`
    * `aktiv` (start=5, mask=00000001b, comment=COMPASS)
    * `aktiv` (start=15, mask=00000001b, comment=X_VIEW)
    * `trajectory1` (start=26, mask=00110000b, comment=X_VIEW_GRAPHIC_SLOP)
    * `trajectory1` (start=26, mask=11000000b, comment=X_VIEW_GRAPHIC_ROLL)
    * `aktiv` (start=110, mask=00000010b, comment=MOMENTDISTRIBUTION_MENU)

* **Change warning sound**
  * Group `3002`
    * `rolls_royce` (start=26, mask=00111000b, comment=SOUND_SIGNAL_SET)

* **Enable USB video playback 1/2**
  * Group `3000`
    * `aktiv` (start=15, mask=00010000b, comment=ENT_CODEC_OGG)
    * `aktiv` (start=15, mask=00100000b, comment=ENT_CODEC_XVID)
    * `aktiv` (start=15, mask=01000000b, comment=ENT_CODEC_VCD)
    * `aktiv` (start=13, mask=00000100b, comment=ENT_MC_VIDEO_SUPPORT)

* **Enable USB video playback 2/2**
  * Group `3003`
    * `both` (start=33, mask=00000110b, comment=API_USB_VIDEO)
    * `both` (start=33, mask=00011000b, comment=API_IPOD_VIEDO)

* **Remove all warning messages**
  * Group `3001`
    * `00` (start=52, mask=11111111b, comment=MACRO_CAM_LEGALDISCLAIMER)
    * `00` (start=58, mask=11111111b, comment=LEGAL_DISCLAIMER_TIME)

* **Enable automatic time setting**
  * Group `3000`
    * `navigation` (start=19, mask=00000110b, comment=SETTINGS_TIME_AUTOMATIC)
    * `aktiv` (start=105, mask=00100000b, comment=CLOCK_CHANGE_AUTOMATIC)

* **Enable rear camera zoom**
  * Group `3001`
    * `aktiv` (start=54, mask=00000001b, comment=MACRO_TRAILER_COUPLING)

* **Enable volume adjustment display**
  * Group `3002`
    * `01` (start=52, mask=01000000b, comment=VOLUME_POPUP_DISPLAY)

* **Enable daylight running lights**
  * Group `3000`
    * `02` (start=92, mask=00011000b, comment=DAYDRIVING_LIGHT)

* **Output ringtone through speakers (iOS only)**
  * Group `3003`
    * `aktiv` (start=6, mask=10000000b, comment=INBAND_RINGING)

* **Configure Sport mode 1/3**
  * Group `3000`
    * `aktiv` (start=101, mask=00010000b, comment=EFF_DYN_SPORT_CID)

* **Configure Sport mode 2/3**
  * Group `3000`
    * `aktiv` (start=107, mask=00000100b, comment=EFF_DYN_SPORT_UNIT)

* **Configure Sport mode 3/3**
  * Group `3001`
    * `popup_and_config` (start=55, mask=00011000b, comment=MACRO_FDS)

* **Bang & Olufsen profile**
  * Group `3000`
    * `keine_insz` (start=21, mask=01100000b, comment=HIGH_END_AUDIO_B_UND_W)

* **Enable Logic7 (S667A HiFi vehicles)**
  * Group `3000`
    * `aktiv` (start=22, mask=00001000b, comment=LOGIC7_SYMBOL)

* **Door lock/unlock chime (anti-theft module vehicles except M5)**
  * Group `3000`
    * `Aktiv` (start=110, mask=00000001b, comment=ACOUSTICAL_LOCK_CONFIRM)

* **Enable TPMC tire pressure temperature**
  * Group `3001`
    * `Aktiv` (start=1, mask=00100000b, comment=RDC_SAFETY)

* **Change M Sport display cluster colors**
  * Group `3000`
    * `aktiv` (start=133, mask=01000000b, comment=M_VEHICLE)

* **High-beam assistant 4/4 -->> KAFAS2 1/4, FRM 2/4, 3/4**
  * Group `3000`
    * `01` (start=109, mask=10000000b, comment=HIGH_BEAM_ASSISTANT)

### BDC_01 (CAFD 000017BE) — authored by ekfxisidF056 | Series: F056

* **Turn off audio and navigation when door opens after engine off [Changwon ll Daltanyang]**
  * Group `3020`
    * `aktiv` (start=9, mask=00000001b, comment=TCM_LOGIC_R_OFF_DOOR)

* **Remember last auto start/stop state**
  * Group `3023`
    * `aktiv` (start=0, mask=00100000b, comment=TCM_MSA_MEMORY)

* **Turn off auto start/stop in Comfort mode**
  * Group `3023`
    * `aktiv` (start=0, mask=00010000b, comment=TCM_MSA_DEFAULT_OFF)

* **Allow windows to operate with doors open**
  * Group `3050`
    * `nicht_aktiv` (start=0, mask=00000001b, comment=FH_TUERAUF_STOP_MAUT)

* **Mirror lock folding (one-touch)**
  * Group `3056`
    * `00` (start=10, mask=11111111b, comment=KOMFORT_SCHLIESSEN)

* **Passenger mirror angle adjustment**
  * Group `3110`
    * `1E` (start=1, mask=11111111b, comment=ASP_BORDSTEINAUTOMAIK_DELTA)

* **Turn signal flashes five times**
  * Group `3068`
    * `04` (start=7, mask=00000111b, comment=BLINKZYKLEN_ANZAHL_TIPP)

* **Flash hazard lights during hard braking(50km/h)**
  * Group `3068`
    * `aktiv` (start=26, mask=00000001b, comment=WB_GB_ENABLE)
    * `00, 32` (start=23, end=24, mask=11111111b, comment=WB_GB_GEFAHRENWERT_MIN)

* **Enable dynamic brake lights**
  * Group `3068`
    * `bremslicht_blinkend` (start=16, mask=00000011b, comment=ESS_AKTIVIERBARER_AUSGANG)
    * `04` (start=20, mask=00011111b, comment=ESS_AKTIVIERUNG_REALE_VERZ)
    * `04` (start=19, mask=00011111b, comment=ESS_DEAKTIVIERUNG_REALE_VERZ)
    * `05` (start=17, mask=11111110b, comment=ESS_AKTIVIERUNG_GESCHW)

* **Auto unfold mirrors above set speed (40 km/h -> 25 km/h)**
  * Group `3110`
    * `19` (start=9, mask=11111111b, comment=ASP_GESCHWINDIGKEIT_AUTO_AUSKLAPPEN)

* **Illuminate door handle lights in reverse**
  * Group `3070`
    * `aktiv` (start=128, mask=00000001b, comment=OVT_BEI_RUECKFAHRLICHT)

* **Front turn signals -> convert to LED**
  * Group `3060`
    * `nicht_aktiv` (start=98, mask=00000001b, comment=FRA_V_L_KALTUEBERWACHUNG)
    * `nicht_aktiv` (start=98, mask=00000010b, comment=FRA_V_L_WARMUEBERWACHUNG)
    * `aktiv` (start=98, mask=00000100b, comment=FRA_V_L_KURZSCHLUSS)
    * `aktiv` (start=98, mask=00001000b, comment=FRA_V_L_IS_LED)
    * `nicht_aktiv` (start=106, mask=00000001b, comment=FRA_V_R_KALTUEBERWACHUNG)
    * `nicht_aktiv` (start=106, mask=00000010b, comment=FRA_V_R_WARMUEBERWACHUNG)
    * `aktiv` (start=106, mask=00000100b, comment=FRA_V_R_KURZSCHLUSS)
    * `aktiv` (start=106, mask=00001000b, comment=FRA_V_R_IS_LED)

* **Rear turn signals -> convert to LED**
  * Group `3061`
    * `nicht_aktiv` (start=98, mask=00000001b, comment=FRA_H_L_KALTUEBERWACHUNG)
    * `nicht_aktiv` (start=98, mask=00000010b, comment=FRA_H_L_WARMUEBERWACHUNG)
    * `aktiv` (start=98, mask=00000100b, comment=FRA_H_L_KURZSCHLUSS)
    * `aktiv` (start=98, mask=00001000b, comment=FRA_H_L_IS_LED)
    * `nicht_aktiv` (start=106, mask=00000001b, comment=FRA_H_R_KALTUEBERWACHUNG)
    * `nicht_aktiv` (start=106, mask=00000010b, comment=FRA_H_R_WARMUEBERWACHUNG)
    * `aktiv` (start=106, mask=00000100b, comment=FRA_H_R_KURZSCHLUSS)
    * `aktiv` (start=106, mask=00001000b, comment=FRA_H_R_IS_LED)

* **Front fog lights -> convert to LED and remove warning**
  * Group `3060`
    * `nicht_aktiv` (start=82, mask=00000001b, comment=NSW_L_KALTUEBERWACHUNG)
    * `nicht_aktiv` (start=82, mask=00000010b, comment=NSW_L_WARMUEBERWACHUNG)
    * `aktiv` (start=82, mask=00000100b, comment=NSW_L_KURZSCHLUSS)
    * `aktiv` (start=82, mask=00001000b, comment=NSW_L_IS_LED)
    * `nicht_aktiv` (start=90, mask=00000001b, comment=NSW_R_KALTUEBERWACHUNG)
    * `nicht_aktiv` (start=90, mask=00000010b, comment=NSW_R_WARMUEBERWACHUNG)
    * `aktiv` (start=90, mask=00000100b, comment=NSW_R_KURZSCHLUSS)
    * `aktiv` (start=90, mask=00001000b, comment=NSW_R_IS_LED)

* **Daytime tail lamps synchronized with daytime headlights 1/3**
  * Group `3068`
    * `drl_s` (start=31, mask=00110000b, comment=TFL_MODUS)

* **Daytime tail lamps synchronized with daytime headlights 2/3**
  * Group `3064`
    * `sl_l` (start=221, mask=00111111b, comment=MAPPING_TAGFAHRL_1_H_L_OUTPUT)
    * `sl_r` (start=234, mask=00111111b, comment=MAPPING_TAGFAHRL_1_H_R_OUTPUT)

* **Daytime tail lamps synchronized with daytime headlights 3/3**
  * Group `3065`
    * `sl_2_l` (start=78, mask=00111111b, comment=MAPPING_TAGFAHRL_2_H_L_OUTPUT)
    * `sl_2_r` (start=91, mask=00111111b, comment=MAPPING_TAGFAHRL_2_H_R_OUTPUT)

### ACSM_4i (CAFD 000011AB) — authored by ekfxisidF056 | Series: F056

* **Seat belt warning chime three times (5 seconds) [Changwon ll Daltanyang]**
  * Group `3001`
    * `05` (start=11, mask=11111111b, comment=GWF_SBR_WARNDAUER)

### IHKA3 (CAFD 000016EE) — authored by ekfxisidF056 | Series: F056

* **Remember last A/C on/off state [Changwon ll Daltanyang]**
  * Group `3003`
    * `Aktiv` (start=0, mask=00000010b, comment=MEMORY_OFF)

* **Remember air recirculation mode**
  * Group `3003`
    * `Aktiv` (start=0, mask=00000001b, comment=MEMORY_UMLUFT)

* **Lock air recirculation mode**
  * Group `3003`
    * `disable` (start=0, mask=10000000b, comment=UMLUFT_AUTO_AUS)

### SM2 (CAFD 000000B5) — authored by ekfxisidF056 | Series: F056

* **Easy Access 1/3 (Easy Entry) [Changwon ll Daltanyang]**
  * Group `3000`
    * `Modus_FA_SLV` (start=0, mask=00011100b, comment=EINAUSSTIEGSHILFE)

* **Easy Access 2/3 (Easy Entry)**
  * Group `3012`
    * `00, 1E` (start=4, end=5, mask=11111111b, comment=EAH_SCHUTZFREIRAUM_HINTEN_SLV_PHYS)

* **Easy Access 3/3 (Easy Entry)**
  * Group `3012`
    * `00, 46` (start=0, end=1, mask=11111111b, comment=EAH_VERFAHRWEG_SLV_PHYS)

* **Set memory gong alert sound**
  * Group `3000`
    * `Aktiv` (start=2, mask=00001000b, comment=MEMORY_GONG)

### HU_NBT2 (CAFD 00001EF6) — authored by ekfxisidF056 | Series: F056

* **Unlock DMB/DVD/Navi while driving 1/2 [Changwon ll Daltanyang]**
  * Group `3006`
    * `FF` (start=25, mask=11111111b, comment=SPEEDLOCK_X_KMH_MAX)
    * `FF` (start=26, mask=11111111b, comment=SPEEDLOCK_X_KMH_MIN)

* **Unlock DMB/DVD/Navi while driving 2/2**
  * Group `3000`
    * `nicht_aktiv` (start=5, mask=00010000b, comment=VIDEO_FRONT_LOCKED)
    * `nicht_aktiv` (start=5, mask=00000100b, comment=VIDEO_HANDBRAKE)
    * `None` (start=2, mask=00000111b, comment=VIDEO_SPEEDLOCK_CONDITION)

* **M performance**
  * Group `3001`
    * `01` (start=62, mask=01111000b, comment=STARTUP_EMBLEM)

* **X - Drive**
  * Group `3000`
    * `aktiv` (start=5, mask=00000001b, comment=COMPASS)
    * `aktiv` (start=15, mask=00000001b, comment=X_VIEW)
    * `trajectory1` (start=26, mask=00110000b, comment=X_VIEW_GRAPHIC_SLOP)
    * `trajectory1` (start=26, mask=11000000b, comment=X_VIEW_GRAPHIC_ROLL)
    * `aktiv` (start=110, mask=00000010b, comment=MOMENTDISTRIBUTION_MENU)

* **Change warning sound**
  * Group `3002`
    * `rolls_royce` (start=26, mask=00111000b, comment=SOUND_SIGNAL_SET)

* **Enable USB video playback 1/2**
  * Group `3000`
    * `aktiv` (start=15, mask=00010000b, comment=ENT_CODEC_OGG)
    * `aktiv` (start=15, mask=00100000b, comment=ENT_CODEC_XVID)
    * `aktiv` (start=15, mask=01000000b, comment=ENT_CODEC_VCD)
    * `aktiv` (start=13, mask=00000100b, comment=ENT_MC_VIDEO_SUPPORT)

* **Enable USB video playback 2/2**
  * Group `3003`
    * `both` (start=32, mask=00000110b, comment=API_USB_VIDEO)
    * `both` (start=32, mask=00011000b, comment=API_IPOD_VIEDO)

* **Remove all warning messages**
  * Group `3001`
    * `00` (start=52, mask=11111111b, comment=MACRO_CAM_LEGALDISCLAIMER)
    * `00` (start=58, mask=11111111b, comment=LEGAL_DISCLAIMER_TIME)

* **Enable automatic time setting**
  * Group `3000`
    * `navigation` (start=19, mask=00000110b, comment=SETTINGS_TIME_AUTOMATIC)
    * `aktiv` (start=105, mask=00100000b, comment=CLOCK_CHANGE_AUTOMATIC)

* **Enable rear camera zoom**
  * Group `3001`
    * `aktiv` (start=54, mask=00000001b, comment=MACRO_TRAILER_COUPLING)

* **Enable daylight running lights**
  * Group `3000`
    * `02` (start=92, mask=00011000b, comment=DAYDRIVING_LIGHT)

* **Output ringtone through speakers (iOS only)**
  * Group `3003`
    * `aktiv` (start=6, mask=10000000b, comment=INBAND_RINGING)

* **Configure Sport mode 1/3**
  * Group `3009`
    * `aktiv` (start=9, mask=00010000b, comment=EFF_DYN_SPORT_CID)

* **Configure Sport mode 2/3**
  * Group `3009`
    * `aktiv` (start=9, mask=00100000b, comment=EFF_DYN_SPORT_UNIT)

* **Configure Sport mode 3/3**
  * Group `3008`
    * `popup_and_config` (start=79, mask=11000000b, comment=MACRO_FDS)

* **Bang & Olufsen profile**
  * Group `3000`
    * `keine_insz` (start=21, mask=01100000b, comment=HIGH_END_AUDIO_B_UND_W)

* **Enable Logic7 (S667A HiFi vehicles)**
  * Group `3000`
    * `aktiv` (start=22, mask=00001000b, comment=LOGIC7_SYMBOL)

* **HUD : Affichage de l'assistant collision Step 2 (Step 1 dans KOMBI)**
  * Group `300C`
    * `Aktiv` (start=0, mask=00010000b, comment=HUD_DISTANCE_INFO)

* **JCW = enable HUD tachometer 1/2 -> KOMBI 2/2**
  * Group `300C`
    * `aktiv` (start=0, mask=00000001b, comment=HUD_SPORTANZEIGE_ENABLE)
    * `aktiv` (start=0, mask=00000010b, comment=HUD_SPORTANZEIGE_FES_ENABLE)
    * `aktiv` (start=0, mask=00000100b, comment=HUD_SPORTANZEIGE_MS_GASSE_ENABLE)

* **Door lock/unlock chime (vehicles with anti-theft module except M5)**
  * Group `3000`
    * `Aktiv` (start=110, mask=00000001b, comment=ACOUSTICAL_LOCK_CONFIRM)

* **Enable TPMC tire pressure temperature**
  * Group `3001`
    * `Aktiv` (start=1, mask=00100000b, comment=RDC_SAFETY)

* **Change M Sport display cluster colors**
  * Group `3000`
    * `aktiv` (start=133, mask=01000000b, comment=M_VEHICLE)

* **High-beam assistant**
  * Group `3000`
    * `01` (start=109, mask=10000000b, comment=HIGH_BEAM_ASSISTANT)

### HU_NBT (CAFD 00000DED) — authored by ekfxisidF056 | Series: F056

* **Unlock DMB/DVD/Navi while driving [Changwon ll Daltanyang]**
  * Group `3000`
    * `FF` (start=72, mask=11111111b, comment=SPEEDLOCK_X_KMH_MAX)
    * `FF` (start=71, mask=11111111b, comment=SPEEDLOCK_X_KMH_MIN)
    * `nicht_aktiv` (start=5, mask=00010000b, comment=VIDEO_FRONT_LOCKED)
    * `nicht_aktiv` (start=5, mask=00000100b, comment=VIDEO_HANDBRAKE)
    * `None` (start=57, mask=00000111b, comment=VIDEO_SPEEDLOCK_CONDITION)

* **M performance**
  * Group `3001`
    * `01` (start=62, mask=01111000b, comment=STARTUP_EMBLEM)

* **X - Drive**
  * Group `3000`
    * `aktiv` (start=5, mask=00000001b, comment=COMPASS)
    * `aktiv` (start=15, mask=00000001b, comment=X_VIEW)
    * `trajectory1` (start=26, mask=00110000b, comment=X_VIEW_GRAPHIC_SLOP)
    * `trajectory1` (start=26, mask=11000000b, comment=X_VIEW_GRAPHIC_ROLL)
    * `aktiv` (start=110, mask=00000010b, comment=MOMENTDISTRIBUTION_MENU)

* **Change warning sound**
  * Group `3002`
    * `rolls_royce` (start=26, mask=00111000b, comment=SOUND_SIGNAL_SET)

* **Enable USB video playback 1/2**
  * Group `3000`
    * `aktiv` (start=15, mask=00010000b, comment=ENT_CODEC_OGG)
    * `aktiv` (start=15, mask=00100000b, comment=ENT_CODEC_XVID)
    * `aktiv` (start=15, mask=01000000b, comment=ENT_CODEC_VCD)
    * `aktiv` (start=13, mask=00000100b, comment=ENT_MC_VIDEO_SUPPORT)

* **Enable USB video playback 2/2**
  * Group `3003`
    * `both` (start=33, mask=00000110b, comment=API_USB_VIDEO)
    * `both` (start=33, mask=00011000b, comment=API_IPOD_VIEDO)

* **Remove all warning messages**
  * Group `3001`
    * `00` (start=52, mask=11111111b, comment=MACRO_CAM_LEGALDISCLAIMER)
    * `00` (start=58, mask=11111111b, comment=LEGAL_DISCLAIMER_TIME)

* **Enable rear camera zoom**
  * Group `3001`
    * `aktiv` (start=54, mask=00000001b, comment=MACRO_TRAILER_COUPLING)

* **Enable daylight running lights**
  * Group `3000`
    * `02` (start=92, mask=00011000b, comment=DAYDRIVING_LIGHT)

* **Enable TPMC tire pressure temperature**
  * Group `3001`
    * `Aktiv` (start=1, mask=00100000b, comment=RDC_SAFETY)

* **JCW = enable HUD tachometer 1/2 -> KOMBI 2/2**
  * Group `3000`
    * `aktiv` (start=18, mask=00000001b, comment=HUD_SPORTANZEIGE_ENABLE)
    * `aktiv` (start=18, mask=00000010b, comment=HUD_SPORTANZEIGE_FES_ENABLE)
    * `aktiv` (start=18, mask=00000100b, comment=HUD_SPORTANZEIGE_MS_GASSE_ENABLE)

* **Output ringtone through speakers (iOS only)**
  * Group `3003`
    * `aktiv` (start=6, mask=10000000b, comment=INBAND_RINGING)

* **Configure Sport mode 1/3**
  * Group `3000`
    * `aktiv` (start=101, mask=00010000b, comment=EFF_DYN_SPORT_CID)

* **Configure Sport mode 2/3**
  * Group `3000`
    * `aktiv` (start=107, mask=00000100b, comment=EFF_DYN_SPORT_UNIT)

* **Configure Sport mode 3/3**
  * Group `3001`
    * `popup_and_config` (start=55, mask=00011000b, comment=MACRO_FDS)

* **Enable automatic time setting**
  * Group `3000`
    * `navigation` (start=19, mask=00000110b, comment=SETTINGS_TIME_AUTOMATIC)
    * `aktiv` (start=105, mask=00100000b, comment=CLOCK_CHANGE_AUTOMATIC)

* **Enable volume adjustment display**
  * Group `3002`
    * `01` (start=52, mask=01000000b, comment=VOLUME_POPUP_DISPLAY)

* **Bang & Olufsen profile**
  * Group `3000`
    * `keine_insz` (start=21, mask=01100000b, comment=HIGH_END_AUDIO_B_UND_W)

* **Enable Logic7 (S667A HiFi vehicles)**
  * Group `3000`
    * `aktiv` (start=22, mask=00001000b, comment=LOGIC7_SYMBOL)

* **Door lock/unlock chime (anti-theft module vehicles except M5)**
  * Group `3000`
    * `Aktiv` (start=110, mask=00000001b, comment=ACOUSTICAL_LOCK_CONFIRM)

* **Change M Sport display cluster colors**
  * Group `3000`
    * `aktiv` (start=133, mask=01000000b, comment=M_VEHICLE)

* **High-beam assistant 4/4 -->> KAFAS2 1/4, FRM 2/4, 3/4**
  * Group `3000`
    * `01` (start=109, mask=10000000b, comment=HIGH_BEAM_ASSISTANT)


## `jokinawa.xml`

**Modules touched:** IHKA4 (CAFD 000051C9, author jokinawa, series S18A), BDC_BODY3 (CAFD 000044ED, author jokinawa, series S18A), BDC_BODY3 (CAFD 00007083, author jokinawa, series S18A), DME_BAC2 (CAFD 00002742, author jokinawa, series S18A), DKOMBI4 (CAFD 00004508, author jokinawa, series S18A), HU_MGU (CAFD 00003E52, author jokinawa, series S18A), FZD2 (CAFD 00001D92, author jokinawa, series S18A), HKFM2 (CAFD 000055D7, author jokinawa, series S18A), SAS2 (CAFD 000042C1, author jokinawa, series S18A)

### IHKA4 (CAFD 000051C9) — authored by jokinawa | Series: S18A

* **[1/2] Enable Colder Air Conditioning**
  * Group `3000`
    * `02` (start=11, mask=00000111b, comment=LAENDERVARIENTE)

* **[2/2] Enable Colder Air Conditioning**
  * Group `3003`
    * `06` (start=1, mask=00001111b, comment=TEMPERATUR_OFFSET)

### BDC_BODY3 (CAFD 000044ED) — authored by jokinawa | Series: S18A

* **Allow closing of windows and sunroof with keyfob**
  * Group `3510`
    * `aktiv` (start=11, mask=00100000b, comment=FH_KOMFORTSCHLIESSUNG_FB)

* **Disable front windows rollup stopping when door opened**
  * Group `3510`
    * `nicht_aktiv` (start=0, mask=00000001b, comment=FH_TUERAUF_STOP_MAUT)

### BDC_BODY3 (CAFD 00007083) — authored by jokinawa | Series: S18A

* **Fog lights flash on alarm - Simultaneous [US Default]**
  * Group `3075`
    * `gleichzeitig` (start=4, mask=10000000b, comment=FERNLICHTBLINKEN_UEBERFALLALARM_BLINKMODUS)

* **Fog lights flash on alarm - Alternating [Europe Default]**
  * Group `3075`
    * `abwechseln` (start=4, mask=10000000b, comment=FERNLICHTBLINKEN_UEBERFALLALARM_BLINKMODUS)

* **Emergency Brake Force Display - Off [US Default]**
  * Group `3075`
    * `nicht_aktiv` (start=1, mask=01100000b, comment=GEFAHRENBREMSLICHT_TYP)

* **Emergency Brake Force Display - Flashing [Europe Default]**
  * Group `3075`
    * `bremslicht_blinkend` (start=1, mask=01100000b, comment=GEFAHRENBREMSLICHT_TYP)

* **Emergency Brake Force Display - Area Enlargement**
  * Group `3075`
    * `flaechenvergroesserung` (start=1, mask=01100000b, comment=GEFAHRENBREMSLICHT_TYP)

* **Disable horn honk when locking doors with engine running**
  * Group `3040`
    * `nicht_aktiv` (start=1, mask=00000010b, comment=VAM_HORN_AT_SECURE)

* **Mirror Tilt Angle 90 [default]**
  * Group `3110`
    * `5A` (start=1, mask=11111111b, comment=ASP_BORDSTEINAUTOMATIK_DELTA)

* **Mirror Tilt Angle 80**
  * Group `3110`
    * `50` (start=1, mask=11111111b, comment=ASP_BORDSTEINAUTOMATIK_DELTA)

* **Mirror Tilt Angle 70**
  * Group `3110`
    * `46` (start=1, mask=11111111b, comment=ASP_BORDSTEINAUTOMATIK_DELTA)

* **Mirror Tilt Angle 59**
  * Group `3110`
    * `3B` (start=1, mask=11111111b, comment=ASP_BORDSTEINAUTOMATIK_DELTA)

* **Change startup mode to Adaptive**
  * Group `3221`
    * `0A` (start=7, mask=11111111b, comment=FesPiaDefaultLastUserMode)

* **Change startup mode to Sport**
  * Group `3221`
    * `01` (start=7, mask=11111111b, comment=FesPiaDefaultLastUserMode)

* **Change startup mode to Sport Individual**
  * Group `3221`
    * `03` (start=7, mask=11111111b, comment=FesPiaDefaultLastUserMode)

* **Change startup mode to Comfort (default)**
  * Group `3221`
    * `04` (start=7, mask=11111111b, comment=FesPiaDefaultLastUserMode)

* **Change startup mode to Eco Pro**
  * Group `3221`
    * `07` (start=7, mask=11111111b, comment=FesPiaDefaultLastUserMode)

* **Change startup mode to Eco Pro Individual**
  * Group `3221`
    * `09` (start=7, mask=11111111b, comment=FesPiaDefaultLastUserMode)

* **[1/2] Enable Sport Plus Mode**
  * Group `3221`
    * `02` (start=9, mask=11111111b, comment=FesSportWorldMode1)

* **[1/2] Enable Comfort Plus Mode**
  * Group `3221`
    * `05` (start=12, mask=11111111b, comment=FesComfortWorldMode1)

* **[WIP][1/3] Enable Automatic Lane Change Assistant**
  * Group `3420`
    * `01` (start=10, mask=00000011b, comment=SPURWECHSEL_ASSISTENT)

* **Enable Comfort Plus Mode options in Eco Pro Individual**
  * Group `3221`
    * `09` (start=5, mask=11111111b, comment=FesPiaDefaultEcoWorldMode)
    * `05` (start=12, mask=11111111b, comment=FesComfortWorldMode1)
    * `05` (start=4, mask=11111111b, comment=FesPiaDefaultComfortWorldMode)

### DME_BAC2 (CAFD 00002742) — authored by jokinawa | Series: S18A

* **[DIAG] Enable Auto Start Stop Memory**
  * Group `3020`
    * `01` (start=19, mask=00000010b, comment=TCM_MSA_MEMORY)

### DKOMBI4 (CAFD 00004508) — authored by jokinawa | Series: S18A

* **Disable Seatbelt Status in Dash**
  * Group `3000`
    * `inaktiv` (start=3, mask=00000111b, comment=FOND_GURTSTATUS_ENABLE)

* **[SAIL] Enable Sailing in Comfort Mode (optional)**
  * Group `3000`
    * `01` (start=15, mask=00001000b, comment=SEGELN_IN_COMFORT_MODUS (optional))

* **Disable Speedometer Correction**
  * Group `3000`
    * `ohne_korrektur` (start=1, mask=01000000b, comment=BC_V_KORREKTUR)

* **Change Dash Layout and Logo to BMW M**
  * Group `3001`
    * `m_logo` (start=18, mask=11111111b, comment=LOGO_SCHRIFTZUG)
  * Group `3000`
    * `m_gmbh` (start=53, mask=11110000b, comment=GLOBAL_LAYOUT_VARIANTE)

* **Change Dash Layout BMW M with no logo**
  * Group `3001`
    * `kein_logo` (start=18, mask=11111111b, comment=LOGO_SCHRIFTZUG)
  * Group `3000`
    * `m_gmbh` (start=53, mask=11110000b, comment=GLOBAL_LAYOUT_VARIANTE)

* **Change Dash Layout and Logo to Alpina [req i-step 2019/07.xx+]**
  * Group `3001`
    * `alpina` (start=18, mask=11111111b, comment=LOGO_SCHRIFTZUG)
  * Group `3000`
    * `alpina` (start=53, mask=11110000b, comment=GLOBAL_LAYOUT_VARIANTE)

* **Change Dash Layout to Alpina with no logo [req i-step 2019/07.xx+]**
  * Group `3001`
    * `kein_logo` (start=18, mask=11111111b, comment=LOGO_SCHRIFTZUG)
  * Group `3000`
    * `alpina` (start=53, mask=11110000b, comment=GLOBAL_LAYOUT_VARIANTE)

* **Enable Assisted Driver View [req 2019/07.xx+]**
  * Group `3000`
    * `01` (start=97, mask=00100000b, comment=SICHT_ABSICHT_ENABLE)
    * `01` (start=112, mask=00100000b, comment=CB_FZG_UMGEBUNG_FAS)
    * `01` (start=112, mask=01000000b, comment=CB_PRESELECT_NAVI_ANSICHT_FZG_UMGEBUNG)
  * Group `3007`
    * `01` (start=29, mask=00000001b, comment=PIA_FZG_UMGEBUNG_FAS)

### HU_MGU (CAFD 00003E52) — authored by jokinawa | Series: S18A

* **Disable Night Vision Legal Disclaimer**
  * Group `300A`
    * `kein_ld` (start=12, mask=11111111b, comment=werte=00)

* **Disable Camera Legal Disclaimer**
  * Group `300B`
    * `kein_ld` (start=1, mask=11111111b, comment=MACRO_CAM_LEGALDISCLAIMER)

* **HUD Distance Info**
  * Group `3000`
    * `aktiv` (start=29, mask=00000001b, comment=HUD_DISTANCE_INFO)

* **Disable Legal Disclaimer Time**
  * Group `3000`
    * `kein_ld` (start=3, mask=11111111b, comment=LEGAL_DISCLAIMER_TIME)

* **[1/2] Enable Video In Motion - must do physical button combo to enable after coding. See Bimmerpost G07 forum in comment.**
  * Group `3000`
    * `none` (start=53, mask=00000111b, comment=VIDEO_SPEEDLOCK_CONDITION)
    * `aktiv` (start=49, mask=10000000b, comment=SPEEDLOCK_FREISCHALTMENU)
    * `nicht_aktiv` (start=40, mask=00011111b, comment=SPEEDLOCK_SPEEDVALUE_MIN)
    * `nicht_aktiv` (start=39, mask=00111111b, comment=SPEEDLOCK_SPEEDVALUE_MAX)

* **[2/2] Enable Video In Motion - must do physical button combo to enable after coding. See Bimmerpost G07 forum in comment.**
  * Group `3006`
    * `nicht_aktiv` (start=14, mask=11111111b, comment=SPEEDLOCK_X_KMH_MIN)
    * `nicht_aktiv` (start=13, mask=11111111b, comment=SPEEDLOCK_X_KMH_MAX)

* **Enable 5 click blinker option in Exterior Lighting settings**
  * Group `3000`
    * `aktiv` (start=0, mask=00000100b, comment=5_FACH_TIPPBLINKEN)

* **Change Startup Emblem to BMW M**
  * Group `3000`
    * `bmw_m` (start=11, mask=00011110b, comment=STARTUP_EMBLEM)

* **Change Startup Emblem to Rolls Royce**
  * Group `3000`
    * `rr` (start=11, mask=00011110b, comment=STARTUP_EMBLEM)

* **Change Startup Emblem to Alpina**
  * Group `3000`
    * `alpina` (start=11, mask=00011110b, comment=STARTUP_EMBLEM)

* **Change Startup Emblem to BMW**
  * Group `3000`
    * `bmw` (start=11, mask=00011110b, comment=STARTUP_EMBLEM)

* **Change Startup Emblem to BMWi**
  * Group `3000`
    * `bmw_i` (start=11, mask=00011110b, comment=STARTUP_EMBLEM)

* **Enable tire temperature and pressure display**
  * Group `3000`
    * `druck_und_temperatur` (start=20, mask=00000011b, comment=RDC_DRUCK_TEMP)

* **Change played sound signal set to BMW [Not working on i-Step 2019.03.xx]**
  * Group `3002`
    * `bmw` (start=2, mask=01110000b, comment=BRAND)

* **Change played sound signal set to Mini [Not working on i-Step 2019.03.xx]**
  * Group `3002`
    * `mini` (start=2, mask=01110000b, comment=BRAND)

* **Change played sound signal set to BMWi [Not working on i-Step 2019.03.xx]**
  * Group `3002`
    * `bmw_i` (start=2, mask=01110000b, comment=BRAND)

* **Change played sound signal set to Rolls Royce [Not working on i-Step 2019.03.xx]**
  * Group `3002`
    * `rolls_royce` (start=2, mask=01110000b, comment=BRAND)

* **Disable Volume Popup Display**
  * Group `3002`
    * `nicht_aktiv` (start=0, mask=10000000b, comment=VOLUME_POPUP_DISPLAY)

* **Change max volume retention to 50 percent**
  * Group `3002`
    * `32` (start=1, mask=11111111b, comment=VOLUME_MAX_ON)

* **[2/2] Enable Sport Plus menu option**
  * Group `3008`
    * `01` (start=0, mask=00000100b, comment=FES_SPORT_EXPERT)

* **[2/2] Enable Comfort Plus menu option**
  * Group `3008`
    * `01` (start=0, mask=00100000b, comment=FES_COMFORT_PLUS)
    * `01` (start=3, mask=00100000b, comment=ECO_CONF_ATTENUATION_COMFPLUS)
    * `01` (start=3, mask=01000000b, comment=ECO_CONF_STEERING_COMFPLUS)

* **[SAIL] Enable Sailing Mode in Eco Pro**
  * Group `3008`
    * `01` (start=4, mask=00000100b, comment=GLOBAL_CONF_SAILING)
    * `01` (start=4, mask=00010000b, comment=EFF_DYN_SAILING)
  * Group `3009`
    * `01` (start=1, mask=00000010b, comment=SAILING_COUNTER)

* **[WIP][2/3] Enable Automatic Lane Change Assistant**
  * Group `300A`
    * `01` (start=11, mask=00000001b, comment=SPURWECHSELASSISTENT)

### FZD2 (CAFD 00001D92) — authored by jokinawa | Series: S18A

* **Disable OBD2 Alarm**
  * Group `3002`
    * `00` (start=6, mask=00001000b, comment=OBD_Alarm)

### HKFM2 (CAFD 000055D7) — authored by jokinawa | Series: S18A

* **Enable Tailgate close with keyfob or switch (No holding)**
  * Group `300B`
    * `05` (start=1, mask=11111111b, comment=HKL_REMOTECONTROLLIFTGATEBUTTON_BUTTON_TYPE)
  * Group `3008`
    * `05` (start=1, mask=11111111b, comment=HKL_ROCKERSWITCHPOS1_BUTTON_TYPE)

### SAS2 (CAFD 000042C1) — authored by jokinawa | Series: S18A

* **[WIP][3/3] Enable Automatic Lane Change Assistant**
  * Group `3000`
    * `01` (start=137, mask=11111111b, comment=C_SWA_VORHANDEN)


## `otakar.xml`

**Modules touched:** ASD01 (CAFD 00000F9B, author otakar), ACSM_4B (CAFD 00000911, author otakar), FEM_01 (CAFD 00000794, author otakar), IHKA_VA02 (CAFD 000016EE, author otakar), KOMBI L7_MID (CAFD 000009C8, author otakar), HU_NBT (CAFD 00000DED, author otakar), ICMQL (CAFD 0000067B, author otakar), CFAS_PLX_1 (CAFD 000000B5, author otakar), REM_01 (CAFD 000007A1, author otakar)

### ASD01 (CAFD 00000F9B) — authored by otakar

* **ASD disable**
  * Group `3000`
    * `05` (start=0, mask=11111111b)
    * `0A` (start=1, mask=11111111b)

### ACSM_4B (CAFD 00000911) — authored by otakar

* **Seatbelt reminder sound duration (5secs)**
  * Group `3001`
    * `5` (start=3, mask=11111111b)

* **Disable seatbelt reminder sound**
  * Group `3000`
    * `00` (start=15, mask=00000010b)
    * `00` (start=15, mask=00000100b)

* **Disable dashboard seatbelt icon**
  * Group `3000`
    * `00` (start=15, mask=00001000b)
    * `00` (start=15, mask=00010000b)

* **Disable seatbelt sound on disconnect**
  * Group `3000`
    * `00` (start=16, mask=00000001b)
    * `00` (start=16, mask=00000010b)

### FEM_01 (CAFD 00000794) — authored by otakar

* **Turn off Radio-Navigation with Opening Driver Door**
  * Group `3020`
    * `01` (start=1, mask=00000001b)

* **Auto Start-Stop Always Off**
  * Group `3023`
    * `01` (start=0, mask=00010000b)

* **Auto Start-Stop Remember Last Setting**
  * Group `3023`
    * `01` (start=0, mask=00100000b)

* **Announcement higher coolant temperature**
  * Group `3040`
    * `01` (start=1, mask=10000000b)

* **Automatic door lock speed (10km/h = 0A)**
  * Group `3040`
    * `0A` (start=6, mask=11111111b)

* **Automatic lock after unlocking without opening of doors (180secs = 10 x 18secs = 12)**
  * Group `3040`
    * `12` (start=5, mask=11111111b)

* **Unlock doors on engine off**
  * Group `3040`
    * `01` (start=1, mask=00000010b)

* **Double horn sound when locking car with engine running and FOB outside**
  * Group `3040`
    * `01` (start=1, mask=00100000b)

* **Window still rollup when opening door**
  * Group `3050`
    * `00` (start=0, mask=00000001b)

* **Open/Close windows/mirror/roof from FOB**
  * Group `3053`
    * `00` (start=0, mask=01000000b)
    * `00` (start=0, mask=10000000b)
  * Group `3110`
    * `01` (start=0, mask=10000000b)
    * `01` (start=7, mask=00000001b)

* **The window closes, closing the door**
  * Group `3053`
    * `01` (start=1, mask=00010000b)

* **Open/Close windows/mirror/roof from comfort access**
  * Group `3053`
    * `00` (start=1, mask=00000010b)
    * `00` (start=1, mask=00000001b)
    * `00` (start=1, mask=00000100b)

* **Convenience opening FOB minor delays opening and closing windows**
  * Group `3053`
    * `00` (start=3, mask=11111111b)
    * `03` (start=4, mask=11111111b)
    * `03` (start=5, mask=11111111b)
    * `03` (start=6, mask=11111111b)
    * `05` (start=8, mask=11111111b)

* **Delay for mirror close from FOB (0.3sec)**
  * Group `3053`
    * `03` (start=9, mask=11111111b)

* **3 flashes the turn signals when unlocking**
  * Group `3060`
    * `03` (start=6, mask=00001100b)

* **Blinker indicator amount (3 flashes = 2)**
  * Group `3060`
    * `02` (start=7, mask=00000111b)

* **Emergency brake light mode - flashed**
  * Group `3060`
    * `02` (start=16, mask=00000011b)

* **Enabled daytime running lights**
  * Group `3060`
    * `01` (start=31, mask=00110000b)

* **Turn signals -> LED bulbs**
  * Group `3061`
    * `00` (start=50, mask=00000001b)
    * `00` (start=50, mask=00000010b)
    * `01` (start=50, mask=00001000b)
    * `00` (start=54, mask=00000001b)
    * `00` (start=54, mask=00000010b)
    * `01` (start=54, mask=00001000b)

* **Angel Eyes Brightness 50% Headlamp On**
  * Group `3062`
    * `32` (start=46, mask=11111111b)
    * `32` (start=57, mask=11111111b)

* **Angel Eyes Brightness 100% Headlamp On**
  * Group `3062`
    * `64` (start=46, mask=11111111b)
    * `64` (start=57, mask=11111111b)

* **Angel Eyes Parking Light Brightness 50%**
  * Group `3062`
    * `32` (start=68, mask=11111111b)
    * `32` (start=80, mask=11111111b)

* **Angel Eyes Parking Light Brightness 100%**
  * Group `3062`
    * `64` (start=68, mask=11111111b)
    * `64` (start=80, mask=11111111b)

* **Angel Eyes Brightness 50% DRL**
  * Group `3062`
    * `32` (start=90, mask=11111111b)
    * `32` (start=101, mask=11111111b)

* **Angel Eyes Brightness 100% DRL**
  * Group `3062`
    * `64` (start=90, mask=11111111b)
    * `64` (start=101, mask=11111111b)

* **Enable muliple blinker**
  * Group `3064`
    * `01` (start=215, mask=00000001b)

* **Ambient light full bright**
  * Group `3070`
    * `99` (start=5, mask=11111111b)

* **Ambient light independent from cluster light**
  * Group `3070`
    * `00` (start=4, mask=10000000b)

* **Door handle LED while in reverse**
  * Group `3070`
    * `01` (start=11, mask=00010000b)

* **Variable light distribution**
  * Group `3073`
    * `9C, 9C, 9C` (start=40, end=42, mask=11111111b)
    * `01` (start=152, mask=00000001b)

* **3 injection pulses of wipe washers**
  * Group `3080`
    * `03` (start=8, mask=00011000b)

* **1 sec. pause between injection pulses**
  * Group `3080`
    * `0A` (start=10, mask=00001111b)

* **0 sec. delay opening trunk with remote control**
  * Group `30D0`
    * `00` (start=8, mask=11111111b)

* **1 sec. delay tilt mirrors with remote control**
  * Group `3110`
    * `01` (start=0, mask=10000000b)

* **Smaller tilt angle right mirror in return**
  * Group `3110`
    * `2B` (start=2, mask=11111111b)

* **Mirror auto-unfold speed (0x14= 20 km/h)**
  * Group `3110`
    * `14` (start=9, mask=11111111b)

* **highest sensitivity headlamp lowering**
  * Group `3130`
    * `02` (start=5, mask=00000111b)

### IHKA_VA02 (CAFD 000016EE) — authored by otakar

* **AC Recirc Last Settings Memory**
  * Group `3003`
    * `01` (start=0, mask=00000001b)

* **AC Last Settings Memory**
  * Group `3003`
    * `01` (start=0, mask=00000010b)

### KOMBI L7_MID (CAFD 000009C8) — authored by otakar

* **BMW Logo   M135i**
  * Group `3000`
    * `02` (start=0, mask=11110000b)

* **BMW Logo   M235i**
  * Group `3000`
    * `03` (start=0, mask=11110000b)

* **BMW Logo   340i**
  * Group `3000`
    * `04` (start=0, mask=11110000b)

* **BMW Logo   50d**
  * Group `3000`
    * `05` (start=0, mask=11110000b)

* **BMW Logo   M3**
  * Group `3000`
    * `06` (start=0, mask=11110000b)

* **BMW Logo   M4**
  * Group `3000`
    * `07` (start=0, mask=11110000b)

* **BMW Logo   eDrive**
  * Group `3000`
    * `0B` (start=0, mask=11110000b)

* **BMW Logo   BMW**
  * Group `3000`
    * `0C` (start=0, mask=11110000b)

* **BMW Logo   M2**
  * Group `3000`
    * `0D` (start=0, mask=11110000b)

* **BMW Logo   M140i**
  * Group `3000`
    * `0E` (start=0, mask=11110000b)

* **BMW Logo   M240i**
  * Group `3000`
    * `0F` (start=0, mask=11110000b)

* **Digital Speed Display**
  * Group `3000`
    * `01` (start=1, mask=00000010b)

* **Disable Speed Correction**
  * Group `3000`
    * `00` (start=1, mask=01000000b)

* **Clock Synchronization via GPS**
  * Group `3000`
    * `01` (start=1, mask=10000000b)

* **Temperature warning for cold countries**
  * Group `3000`
    * `01` (start=30, mask=00000001b)

* **Motortemp enable**
  * Group `3000`
    * `01` (start=42, mask=00010000b)

* **M digi tacho - km/h**
  * Group `3000`
    * `01` (start=42, mask=11000000b)

* **dsc off unbundling enable**
  * Group `3000`
    * `01` (start=43, mask=00000010b)

* **MPM Logo   AG**
  * Group `3000`
    * `00` (start=43, mask=11110000b)

* **MPM Logo   550d**
  * Group `3000`
    * `01` (start=43, mask=11110000b)

* **MPM Logo   M135i**
  * Group `3000`
    * `02` (start=43, mask=11110000b)

* **MPM Logo   M235i**
  * Group `3000`
    * `03` (start=43, mask=11110000b)

* **MPM Logo   340i**
  * Group `3000`
    * `04` (start=43, mask=11110000b)

* **MPM Logo   50d**
  * Group `3000`
    * `05` (start=43, mask=11110000b)

* **MPM Logo   eDrive**
  * Group `3000`
    * `0B` (start=43, mask=11110000b)

* **MPM Logo   M140i**
  * Group `3000`
    * `0E` (start=43, mask=11110000b)

* **MPM Logo   M240i**
  * Group `3000`
    * `0F` (start=43, mask=11110000b)

* **M Variante motorsport**
  * Group `3003`
    * `01` (start=3, mask=00001000b)

* **CBS service reset**
  * Group `3004`
    * `01` (start=33, mask=00001000b)

* **language czech**
  * Group `3008`
    * `18` (start=0, mask=00011111b)

* **Speed limit**
  * Group `3008`
    * `01` (start=4, mask=01000000b)

* **Volume of blinker signal**
  * Group `300B`
    * `FF, FF, FF, FF` (start=4, end=7, mask=11111111b)

### HU_NBT (CAFD 00000DED) — authored by otakar

* **Online entertainment**
  * Group `3000`
    * `01` (start=10, mask=00001000b)
    * `01` (start=10, mask=00010000b)

* **video support**
  * Group `3000`
    * `01` (start=13, mask=00000100b)

* **Enable import of customer playlists through the optical drive**
  * Group `3000`
    * `01` (start=13, mask=00001000b)

* **Enable function to bookmark current playback position inside of a currently playback music file from the music collection**
  * Group `3000`
    * `01` (start=14, mask=00000100b)

* **Enables to scale album-cover from Gracenote for Audio-CDs to full-size**
  * Group `3000`
    * `01` (start=14, mask=00100000b)

* **Gracenote installed**
  * Group `3000`
    * `01` (start=14, mask=01000000b)

* **Gracenote via USB enable**
  * Group `3000`
    * `01` (start=15, mask=00000010b)

* **Video codec OGG**
  * Group `3000`
    * `01` (start=15, mask=00010000b)

* **Video codec XVID**
  * Group `3000`
    * `01` (start=15, mask=00100000b)

* **Video codec VCD**
  * Group `3000`
    * `01` (start=15, mask=01000000b)

* **Traffic Info Categories in the HMI enable**
  * Group `3000`
    * `01` (start=16, mask=00000010b)

* **Auto map ZOOM enable**
  * Group `3000`
    * `01` (start=16, mask=00001000b)

* **Apple enhancements**
  * Group `3000`
    * `01` (start=22, mask=10000000b)

* **Online Entertainment login speedlimit disable**
  * Group `3000`
    * `00` (start=33, mask=10000000b)

* **Display full messages while driving**
  * Group `3000`
    * `00` (start=56, mask=00001110b)
  * Group `3003`
    * `07` (start=11, mask=00000111b)

* **Enable Road Preview**
  * Group `3000`
    * `01` (start=59, mask=00100000b)

* **Enable Traffic Information via TMC**
  * Group `3000`
    * `01` (start=59, mask=00010000b)
  * Group `3002`
    * `01` (start=23, mask=00000100b)
    * `01` (start=23, mask=00100000b)
    * `01` (start=24, mask=00000010b)

* **Enable Trip Import via USB**
  * Group `3000`
    * `01` (start=61, mask=00000001b)

* **Enable Trip Export via USB**
  * Group `3000`
    * `01` (start=61, mask=00000010b)

* **Enable Dest Import via USB**
  * Group `3000`
    * `01` (start=61, mask=00000100b)

* **Enable Dest Export via USB**
  * Group `3000`
    * `01` (start=61, mask=00001000b)

* **Enable MyPOI Import via USB**
  * Group `3000`
    * `01` (start=61, mask=00010000b)

* **Enable MyPOI Export via USB**
  * Group `3000`
    * `01` (start=61, mask=00100000b)

* **Map Arrowview**
  * Group `3000`
    * `01` (start=62, mask=00000100b)

* **Route study**
  * Group `3000`
    * `01` (start=62, mask=00100000b)

* **Distance unit Km only**
  * Group `3000`
    * `03` (start=65, mask=01110000b)

* **Enable DVD/Video in motion**
  * Group `3000`
    * `FF` (start=71, mask=11111111b)
    * `FF` (start=72, mask=11111111b)
    * `00` (start=5, mask=00000100b)
    * `00` (start=57, mask=00000111b)

* **Show DRL Option in iDrive**
  * Group `3000`
    * `01` (start=92, mask=00011000b)

* **NAVI Position menu**
  * Group `3000`
    * `01` (start=96, mask=10000000b)

* **Menu Express roads**
  * Group `3000`
    * `01` (start=108, mask=00000100b)

* **High beam assistant**
  * Group `3000`
    * `01` (start=109, mask=10000000b)

* **setting for acoustic confirmation is displayed and can be adjusted**
  * Group `3000`
    * `01` (start=110, mask=00000001b)

* **NAVI Enable the 2 step guiding advice output**
  * Group `3000`
    * `01` (start=111, mask=00000010b)

* **NAVI Autozoom**
  * Group `3000`
    * `01` (start=111, mask=00000100b)

* **Enable Route Preview**
  * Group `3000`
    * `01` (start=111, mask=00001000b)
    * `01` (start=135, mask=00001000b)

* **Enable NAVI route management**
  * Group `3000`
    * `01` (start=111, mask=00010000b)

* **Enable POI alert**
  * Group `3000`
    * `01` (start=111, mask=10000000b)

* **M theme for sport display (hp/torque color)**
  * Group `3000`
    * `01` (start=133, mask=01000000b)

* **Show Tire Pressure and Temperature in iDrive**
  * Group `3001`
    * `01` (start=1, mask=00100000b)
    * `02` (start=66, mask=00001100b)

* **Disable Camera/PDC Legal Disclaimer**
  * Group `3001`
    * `00` (start=52, mask=11111111b)

* **Show Volume Popup Display**
  * Group `3002`
    * `01` (start=52, mask=01000000b)

* **Disable Legal Disclaimer**
  * Group `3001`
    * `00` (start=58, mask=11111111b)

* **Startup animation - black**
  * Group `3001`
    * `00` (start=62, mask=00000110b)

* **Startup animation - splash**
  * Group `3001`
    * `01` (start=62, mask=00000110b)

* **Startup animation - animation**
  * Group `3001`
    * `02` (start=62, mask=00000110b)

* **Startup emblem BMW ConnectedDrive**
  * Group `3001`
    * `00` (start=62, mask=01111000b)

* **Startup emblem ///M**
  * Group `3001`
    * `01` (start=62, mask=01111000b)

* **Startup emblem Alpina**
  * Group `3001`
    * `02` (start=62, mask=01111000b)

* **Startup emblem BMW i**
  * Group `3001`
    * `03` (start=62, mask=01111000b)

* **Startup emblem MINI**
  * Group `3001`
    * `04` (start=62, mask=01111000b)

* **Startup emblem RollsRoyce**
  * Group `3001`
    * `05` (start=62, mask=01111000b)

* **Startup emblem BMW ConnectedDrive**
  * Group `3001`
    * `06` (start=62, mask=01111000b)

* **Startup emblem BMW (smaller)**
  * Group `3001`
    * `07` (start=62, mask=01111000b)

* **Startup emblem BMW (bigger)**
  * Group `3001`
    * `08` (start=62, mask=01111000b)

* **Startup emblem Merry Christmass**
  * Group `3001`
    * `09` (start=62, mask=01111000b)

* **One microphone**
  * Group `3002`
    * `01` (start=55, mask=00110000b)

* **Ringtone from phone**
  * Group `3003`
    * `01` (start=6, mask=10000000b)

* **Contacts Phone/NAVI separated**
  * Group `3003`
    * `01` (start=8, mask=00000100b)

* **ringtone BMW**
  * Group `3003`
    * `00` (start=8, mask=00000011b)

* **ringtone MINI**
  * Group `3003`
    * `01` (start=8, mask=00000011b)

* **ringtone BMW i**
  * Group `3003`
    * `02` (start=8, mask=00000011b)

* **ringtone RR**
  * Group `3003`
    * `03` (start=8, mask=00000011b)

* **API USB read-write**
  * Group `3003`
    * `01` (start=22, mask=10000000b)

### ICMQL (CAFD 0000067B) — authored by otakar

* **Enable cruise control at any speed**
  * Group `3000`
    * `00` (start=142, mask=11111111b)
    * `00` (start=143, mask=11111111b)

### CFAS_PLX_1 (CAFD 000000B5) — authored by otakar

* **MEMORY GONG**
  * Group `3000`
    * `01` (start=2, mask=00001000b)

### REM_01 (CAFD 000007A1) — authored by otakar

* **Brake lights -> LED bulbs**
  * Group `3061`
    * `00` (start=18, mask=00000001b)
    * `00` (start=18, mask=00000010b)
    * `01` (start=18, mask=00001000b)
    * `00` (start=22, mask=00000001b)
    * `00` (start=22, mask=00000010b)
    * `01` (start=22, mask=00001000b)

* **Brake force lights -> LED bulbs**
  * Group `3061`
    * `00` (start=26, mask=00000001b)
    * `00` (start=26, mask=00000010b)
    * `01` (start=26, mask=00001000b)
    * `00` (start=30, mask=00000001b)
    * `00` (start=30, mask=00000010b)
    * `01` (start=30, mask=00001000b)

* **Fog lights -> LED bulbs**
  * Group `3061`
    * `00` (start=34, mask=00000001b)
    * `00` (start=34, mask=00000010b)
    * `01` (start=34, mask=00001000b)
    * `00` (start=38, mask=00000001b)
    * `00` (start=38, mask=00000010b)
    * `01` (start=38, mask=00001000b)

* **Reverse lights -> LED bulbs**
  * Group `3061`
    * `00` (start=42, mask=00000001b)
    * `00` (start=42, mask=00000010b)
    * `01` (start=42, mask=00001000b)
    * `00` (start=46, mask=00000001b)
    * `00` (start=46, mask=00000010b)
    * `01` (start=46, mask=00001000b)

* **Turn signals -> LED bulbs**
  * Group `3061`
    * `00` (start=50, mask=00000001b)
    * `00` (start=50, mask=00000010b)
    * `01` (start=50, mask=00001000b)
    * `00` (start=54, mask=00000001b)
    * `00` (start=54, mask=00000010b)
    * `01` (start=54, mask=00001000b)

* **== ALL rear lights -> LED bulbs ==**
  * Group `3061`
    * `00` (start=10, mask=00000001b)
    * `00` (start=10, mask=00000010b)
    * `01` (start=10, mask=00001000b)
    * `00` (start=14, mask=00000001b)
    * `00` (start=14, mask=00000010b)
    * `01` (start=14, mask=00001000b)
    * `00` (start=18, mask=00000001b)
    * `00` (start=18, mask=00000010b)
    * `01` (start=18, mask=00001000b)
    * `00` (start=22, mask=00000001b)
    * `00` (start=22, mask=00000010b)
    * `01` (start=22, mask=00001000b)
    * `00` (start=26, mask=00000001b)
    * `00` (start=26, mask=00000010b)
    * `01` (start=26, mask=00001000b)
    * `00` (start=30, mask=00000001b)
    * `00` (start=30, mask=00000010b)
    * `01` (start=30, mask=00001000b)
    * `00` (start=34, mask=00000001b)
    * `00` (start=34, mask=00000010b)
    * `01` (start=34, mask=00001000b)
    * `00` (start=38, mask=00000001b)
    * `00` (start=38, mask=00000010b)
    * `01` (start=38, mask=00001000b)
    * `00` (start=42, mask=00000001b)
    * `00` (start=42, mask=00000010b)
    * `01` (start=42, mask=00001000b)
    * `00` (start=46, mask=00000001b)
    * `00` (start=46, mask=00000010b)
    * `01` (start=46, mask=00001000b)
    * `00` (start=50, mask=00000001b)
    * `00` (start=50, mask=00000010b)
    * `01` (start=50, mask=00001000b)
    * `00` (start=54, mask=00000001b)
    * `00` (start=54, mask=00000010b)
    * `01` (start=54, mask=00001000b)
    * `01` (start=66, mask=00001000b)
    * `01` (start=70, mask=00001000b)

* **tail lights with dayrunlights**
  * Group `3062`
    * `14` (start=200, mask=00111111b)
    * `15` (start=210, mask=00111111b)

* **Enable camera at any speed**
  * Group `3203`
    * `FF` (start=7, mask=11111111b)
    * `FF` (start=8, mask=11111111b)
    * `FF` (start=9, mask=11111111b)
    * `FF` (start=10, mask=11111111b)


## `packetpilot.xml`

**Modules touched:** ACSM_4C (CAFD 00000909, author packetpilot, series F020,F030), FEM_01 (CAFD 00000794, author packetpilot, series F020,F030), REM_01 (CAFD 000007A1, author packetpilot, series F020,F030), NBT (CAFD 00001EF6, author packetpilot), LHM2 (CAFD 000010BA, author packetpilot, series F020,F030), LHM2 (CAFD 000016BF, author packetpilot, series F020,F030), TMS_03 (CAFD 00001082, author packetpilot, series F020,F030), TMS_03 (CAFD 00001083, author packetpilot, series F020,F030), SM2 (CAFD 000000B5, author packetpilot, series F020,F030)

### ACSM_4C (CAFD 00000909) — authored by packetpilot | Series: F020,F030

* **Disable seat-belt chime**
  * Group `3000`
    * `00` (start=15, mask=00000010b)
    * `00` (start=15, mask=00000100b)

* **Enable seat-belt chime**
  * Group `3000`
    * `00` (start=15, mask=00000010b)
    * `00` (start=15, mask=00000100b)

### FEM_01 (CAFD 00000794) — authored by packetpilot | Series: F020,F030

* **Fold/Unfold Mirrors, Ctrl Windows: Enable w/ Fob and Comfort Access, Min Delay**
  * Group `3053`
    * `00` (start=0, mask=01000000b)
    * `00` (start=0, mask=10000000b)
    * `00` (start=1, mask=00000001b)
    * `00` (start=1, mask=00000010b)
    * `0A` (start=8, mask=11111111b)
    * `00` (start=9, mask=11111111b)
  * Group `3110`
    * `01` (start=0, mask=10000000b)
    * `01` (start=1, mask=00000001b)
    * `01` (start=7, mask=00000001b)
    * `01` (start=8, mask=00000001b)

* **Fold/Unfold Mirrors, Ctrl Windows: Disable w/ Fob and Comfort Access**
  * Group `30530`
    * `01` (start=0, mask=01000000b)
    * `01` (start=0, mask=10000000b)
    * `01` (start=1, mask=00000001b)
    * `01` (start=1, mask=00000010b)
  * Group `3110`
    * `00` (start=0, mask=10000000b)
    * `00` (start=1, mask=00000001b)
    * `00` (start=7, mask=00000001b)
    * `00` (start=8, mask=00000001b)

* **Rear Fog Switch: Enable [dep: switch or blank mod]**
  * Group `3060`
    * `01` (start=7, mask=00001000b)

* **Rear Fog Switch: Disable**
  * Group `3060`
    * `00` (start=7, mask=00001000b)

* **Front Fog-Like VLD: Enable Step 1 [dep: switch or blank mod, VLD]**
  * Group `3060`
    * `01` (start=13, mask=10000000b)
  * Group `3064`
    * `09` (start=213, mask=11111111b)

* **Front Fog-Like VLD: Disable Step 1**
  * Group `3060`
    * `00` (start=13, mask=10000000b)
  * Group `3064`
    * `02` (start=213, mask=11111111b)

* **Five-Flash Blinker Tap**
  * Group `3060`
    * `04` (start=7, mask=00000111b)

* **Brake Force Display: Disable Timeout [US/CDN]**
  * Group `3060`
    * `00` (start=18, mask=11111111b)

* **Fog Lights: Disable Hi-Beam Override**
  * Group `3060`
    * `00` (start=20, mask=00100000b)

* **Deploy Hazards upon Heavy Decel [req. manual cancel]**
  * Group `3060`
    * `01` (start=26, mask=00000001b)

* **Fog Lights: Bypass Position 1 Requirement**
  * Group `3060`
    * `01` (start=29, mask=01000000b)

* **Fog Lights: Reinstate Position 1 Requirement**
  * Group `3060`
    * `00` (start=29, mask=01000000b)

* **Headlight Washer: Disable**
  * Group `3080`
    * `nicht_aktiv` (start=8, mask=00000001b, comment=WW_SCHEINWERFERREINIGUNG)

* **Headlight Washer: Enable**
  * Group `3080`
    * `aktiv` (start=8, mask=00000001b, comment=WW_SCHEINWERFERREINIGUNG)

* **Headlight Washer NummerSpritzen: 2 squirts**
  * Group `3080`
    * `02` (start=8, mask=00011000b, comment=WW_ANZAHL_SPRITZIMPULSE_SRA)

* **Headlight Washer NummerSpritzen: 3 squirts**
  * Group `3080`
    * `03` (start=8, mask=00011000b, comment=WW_ANZAHL_SPRITZIMPULSE_SRA)

* **Headlight Washer: Activate Every 2 Windshield Washes**
  * Group `3080`
    * `02` (start=2, mask=00011110b, comment=WW_ANZAHL_WASCHBET_ZUR_SRA)

* **Headlight Washer: Activate Every 4 Windshield Washes**
  * Group `3080`
    * `04` (start=2, mask=00011110b, comment=WW_ANZAHL_WASCHBET_ZUR_SRA)

* **Headlight Washer: Activate Every 8 Windshield Washes**
  * Group `3080`
    * `08` (start=2, mask=00011110b, comment=WW_ANZAHL_WASCHBET_ZUR_SRA)

### REM_01 (CAFD 000007A1) — authored by packetpilot | Series: F020,F030

* **DRL: Enable Outer and Inner Tails**
  * Group `3062`
    * `14` (start=200, mask=00111111b)
    * `15` (start=210, mask=00111111b)
    * `16` (start=220, mask=00111111b)
    * `17` (start=230, mask=00111111b)

* **DRL: Enable Outer Tails Only**
  * Group `3062`
    * `14` (start=200, mask=00111111b)
    * `15` (start=210, mask=00111111b)
    * `00` (start=220, mask=00111111b)
    * `00` (start=230, mask=00111111b)

* **DRL: Disable Tails**
  * Group `3062`
    * `00` (start=200, mask=00111111b)
    * `00` (start=210, mask=00111111b)
    * `00` (start=220, mask=00111111b)
    * `00` (start=230, mask=00111111b)

* **Rear Fog: Enable Both Lamps [dep: switch activation in FEM_Body]**
  * Group `3063`
    * `1C` (start=40, mask=00111111b)
    * `1D` (start=50, mask=00111111b)

* **Rear Fog: Enable Left Lamp [dep: switch activation in FEM_Body]**
  * Group `3063`
    * `1C` (start=40, mask=00111111b)
    * `00` (start=50, mask=00111111b)

* **Rear Fog: Enable Right Lamp [dep: switch activation in FEM_Body]**
  * Group `3063`
    * `00` (start=40, mask=00111111b)
    * `1D` (start=50, mask=00111111b)

### NBT (CAFD 00001EF6) — authored by packetpilot

* **Digital Signal Processing: Enable B-and-O DSP Override**
  * Group `3000`
    * `03` (start=57, mask=00110000b)

* **Digital Signal Processing: Disable B-and-O DSP Override**
  * Group `3000`
    * `00` (start=57, mask=00110000b)

### LHM2 (CAFD 000010BA) — authored by packetpilot | Series: F020,F030

* **Front Fog-Like VLD noGFHB: Enable Step 2a [dep: step 1 in FEM_Body, no GFHB, LED pkg]**
  * Group `3000`
    * `FA, FA, 00, FA, C8, C8, 00` (start=0, end=6, mask=11111111b)
    * `FA, FA, 00, FA, C8, C8, 00` (start=7, end=13, mask=11111111b)

* **Front Fog-Like VLD noGFHB: Disable Step 2a [reco: revert Step 1 in FEM_Body, req: no GFHB]**
  * Group `3000`
    * `FA, FA, 00, 00, C8, C8, 00` (start=0, end=6, mask=11111111b)
    * `FA, FA, 00, 00, C8, C8, 00` (start=7, end=13, mask=11111111b)

* **Front Fog-Like VLD w/ GFHB: Enable Step 2a [dep: step 1 in FEM_Body, GFHB, LED pkg]**
  * Group `3000`
    * `FA, 64, 00, FA, FA, FA, 00` (start=0, end=6, mask=11111111b)
    * `FA, 64, 00, FA, FA, FA, 00` (start=7, end=13, mask=11111111b)

* **Front Fog-Like VLD w/ GFHB: Disable Step 2a [reco: revert Step 1 in FEM_Body, req: GFHB ]**
  * Group `3000`
    * `FA, 64, 00, 00, FA, FA, 00` (start=0, end=6, mask=11111111b)
    * `FA, 64, 00, 00, FA, FA, 00` (start=7, end=13, mask=11111111b)

### LHM2 (CAFD 000016BF) — authored by packetpilot | Series: F020,F030

* **Front Fog-Like VLD noGFHB: Enable Step 2b [dep: step 1 in FEM_Body]**
  * Group `3000`
    * `FA, FA, 00, FA, C8, C8, 00` (start=0, end=6, mask=11111111b)
    * `FA, FA, 00, FA, C8, C8, 00` (start=7, end=13, mask=11111111b)

* **Front Fog-Like VLD noGFHB: Disable Step 2b [reco: revert Step 1 in FEM_Body]**
  * Group `3000`
    * `FA, FA, 00, 00, C8, C8, 00` (start=0, end=6, mask=11111111b)
    * `FA, FA, 00, 00, C8, C8, 00` (start=7, end=13, mask=11111111b)

* **Front Fog-Like VLD w/ GFHB: Enable Step 2b [dep: step 1 in FEM_Body, GFHB, LED pkg]**
  * Group `3000`
    * `FA, 64, 00, FA, FA, FA, 00` (start=0, end=6, mask=11111111b)
    * `FA, 64, 00, FA, FA, FA, 00` (start=7, end=13, mask=11111111b)

* **Front Fog-Like VLD w/ GFHB: Disable Step 2b [reco: revert Step 1 in FEM_Body, req: GFHB ]**
  * Group `3000`
    * `FA, 64, 00, 00, FA, FA, 00` (start=0, end=6, mask=11111111b)
    * `FA, 64, 00, 00, FA, FA, 00` (start=7, end=13, mask=11111111b)

### TMS_03 (CAFD 00001082) — authored by packetpilot | Series: F020,F030

* **DRL Headlamp Settings: Eyebrow Off, AngelEyes On [Drv]**
  * Group `3005`
    * `00, 03, 00, 00, 00, 04, 00, 00, 00, 04, 00, 00, 64, 24, 00, 00` (start=0, end=15, mask=11111111b)

* **DRL Headlamp Settings: Eyebrow On, AngelEyes Off [Drv]**
  * Group `3005`
    * `00, 03, 00, 00, 00, 04, 00, 00, 64, 04, 00, 00, 00, 24, 00, 00` (start=0, end=15, mask=11111111b)

* **DRL Headlamp Settings: Eyebrow AND Angel Eyes On [Drv]**
  * Group `3005`
    * `00, 03, 00, 00, 00, 04, 00, 00, 64, 04, 00, 00, 64, 24, 00, 00` (start=0, end=15, mask=11111111b)

### TMS_03 (CAFD 00001083) — authored by packetpilot | Series: F020,F030

* **DRL Headlamp Settings: Eyebrow Off, AngelEyes On [Pass]**
  * Group `3005`
    * `00, 03, 00, 00, 00, 04, 00, 00, 00, 04, 00, 00, 64, 24, 00, 00` (start=0, end=15, mask=11111111b)

* **DRL Headlamp Settings: Eyebrow On, AngelEyes Off [Pass]**
  * Group `3005`
    * `00, 03, 00, 00, 00, 04, 00, 00, 64, 04, 00, 00, 00, 24, 00, 00` (start=0, end=15, mask=11111111b)

* **DRL Headlamp Settings: Eyebrow AND Angel Eyes On [Pass]**
  * Group `3005`
    * `00, 03, 00, 00, 00, 04, 00, 00, 64, 04, 00, 00, 64, 24, 00, 00` (start=0, end=15, mask=11111111b)

### SM2 (CAFD 000000B5) — authored by packetpilot | Series: F020,F030

* **Easy Entry: Enable**
  * Group `3000`
    * `Modus_FA_SLV` (start=0, mask=00011100b, comment=EINAUSSTIEGSHILFE)

* **Easy Entry: Set Max Rearward Auto-Travel (mm from limit?)**
  * Group `3012`
    * `00, 32` (start=4, end=5, mask=11111111b, comment=EAH_SCHUTZFREIRAUM_HINTEN_SLV_PHYS)

* **Easy Entry: Set Desired Rearward Travel (mm?)**
  * Group `3012`
    * `00, 32` (start=0, end=1, mask=11111111b, comment=EAH_VERFAHRWEG_SLV_PHYS)


## `pmooiweer.xml`

**Modules touched:** FEM_BODY (CAFD 00000794, author pmooiweer, series F080,F082), KAFAS2 (CAFD 00001148, author pmooiweer, series F080,F082), FLE 43/44 (CAFD 000024C3, author pmooiweer, series F080,F082)

### FEM_BODY (CAFD 00000794) — authored by pmooiweer | Series: F080,F082

* **Enable GFHB and Adaptive Light Distribution (AFS) (also code KAFAS2 and FLE)**
  * Group `3003`
    * `aktiv` (start=18, mask=00100000b, comment=ComAdapterPdu_095_Objektdaten_Stufenloser_Fernlicht_Assistent)
  * Group `3073`
    * `F020_mit_AFS` (start=40, end=42, mask=11111111b, comment=LUT_FLC_FORWARDLIGHTING_Y)
    * `F020_enable` (start=152, mask=00000001b, comment=C_AFS_ENA)
    * `F020_enable` (start=250, mask=00000001b, comment=C_HBA_ENA)

### KAFAS2 (CAFD 00001148) — authored by pmooiweer | Series: F080,F082

* **Enable GFHB (also code FEM_BODY and FLEs)**
  * Group `3050`
    * `glarfreeHB_on_F001` (start=1, mask=10000000b, comment=GLAREFREE_HIGHBEAM_ENABLED)

### FLE 43/44 (CAFD 000024C3) — authored by pmooiweer | Series: F080,F082

* **Enable GFHB WITHOUT sidemarkers (also code FEM_BODY and KAFAS2)**
  * Group `3000`
    * `01_Value` (start=4, mask=11110000b, comment=HlPrjLabel_HIType)
  * Group `3003`
    * `07_Value` (start=0, end=9, mask=11111111b, comment=SchlechtWetter_C1_Idx)
    * `07_Value` (start=10, end=19, mask=11111111b, comment=SchlechtWetter_C2_Idx)
    * `07_Value` (start=20, end=29, mask=11111111b, comment=Stadt_V_Idx)
    * `07_Value` (start=30, end=39, mask=11111111b, comment=SAE_Idx)
    * `07_Value` (start=40, end=49, mask=11111111b, comment=H10_Landstrasse_C_Idx)
    * `07_Value` (start=50, end=59, mask=11111111b, comment=H8_Autobahn_E3_Idx)
    * `07_Value` (start=60, end=69, mask=11111111b, comment=H6_Autobahn_E2_Idx)
    * `07_Value` (start=70, end=79, mask=11111111b, comment=H5_Autobahn_E1_Idx)
    * `07_Value` (start=80, end=89, mask=11111111b, comment=H4_Autobahn_E_Idx)
    * `08_Value` (start=90, end=99, mask=11111111b, comment=H_2_Idx)
    * `08_Value` (start=100, end=109, mask=11111111b, comment=H_0_Idx)
    * `07_Value` (start=110, end=119, mask=11111111b, comment=H_Plus2_Idx)
    * `08_Value` (start=120, end=129, mask=11111111b, comment=H_Plus4_Idx)
    * `10_Value` (start=130, end=139, mask=11111111b, comment=Blendfreies_Fernlicht_Idx)
    * `09_Value` (start=140, end=149, mask=11111111b, comment=Volles_Fernlicht__Lichthupe_Idx)
  * Group `3004`
    * `08_Value` (start=0, end=9, mask=11111111b, comment=DRL_Idx)
    * `00, 00, 00, 04, 00, 00, 08, 00, 00, 00` (start=10, end=19, mask=11111111b, comment=POLI1_Idx)
    * `00, 00, 00, 04, 00, 00, 08, 00, 00, 00` (start=20, end=29, mask=11111111b, comment=POLI2_Idx)
    * `00, 00, 00, 04, 00, 00, 08, 00, 00, 00` (start=30, end=39, mask=11111111b, comment=POLI3_IDX)
    * `10_Value` (start=40, end=49, mask=11111111b, comment=PLI_Idx)
    * `00, 09, 09, 04, 00, 00, 0A, 00, 00, 00` (start=60, end=69, mask=11111111b, comment=WELL1_Idx)
    * `00, 00, 00, 04, 00, 00, 0B, 00, 00, 00` (start=70, end=79, mask=11111111b, comment=WELL2_Idx)
    * `00, 00, 00, 04, 00, 00, 0B, 00, 00, 00` (start=80, end=89, mask=11111111b, comment=WELL3_Idx)
    * `00, 00, 00, 04, 00, 00, 0B, 00, 00, 00` (start=90, end=99, mask=11111111b, comment=WELL4_IDX)
    * `00, 02, 02, 04, 00, 00, 0B, 00, 00, 00` (start=100, end=109, mask=11111111b, comment=FMH_Idx)
    * `00, 02, 02, 04, 00, 00, 0B, 00, 00, 00` (start=110, end=119, mask=11111111b, comment=REMLI_Idx)
    * `11_Value` (start=120, end=129, mask=11111111b, comment=HBBLINK_Idx)
    * `07_Value` (start=130, end=139, mask=11111111b, comment=DWABLINK_Idx)
    * `07_Value` (start=140, end=149, mask=11111111b, comment=PanicMode_Idx)
    * `11_Value` (start=150, end=159, mask=11111111b, comment=RaidAlarm_Idx)
    * `10_Value` (start=160, end=169, mask=11111111b, comment=Blinken_Idx)
    * `00, 00, 00, 04, 00, 00, 00, 00, 00, 00` (start=180, end=189, mask=11111111b, comment=SIDEMRKLGT_Idx)
    * `10_Value` (start=190, end=199, mask=11111111b, comment=BLINKEN_PO_Idx)
  * Group `3005`
    * `04_Value` (start=4, mask=11111111b, comment=LmmIdx01_Intensity)
    * `01_Value` (start=7, mask=01000000b, comment=LmmIdx01_ErrorImpact)
    * `02_Value` (start=9, mask=11111111b, comment=LmmIdx02_TimeOn)
    * `02_Value` (start=10, mask=11111111b, comment=LmmIdx02_TimeOff)
    * `03_Value` (start=11, mask=00001111b, comment=LmmIdx02_Priority)
    * `01_Value` (start=11, mask=01000000b, comment=LmmIdx02_ErrorImpact)
    * `04_Value` (start=12, mask=11111111b, comment=LmmIdx03_Intensity)
    * `02_Value` (start=13, mask=11111111b, comment=LmmIdx03_TimeOn)
    * `02_Value` (start=14, mask=11111111b, comment=LmmIdx03_TimeOff)
    * `05_Value` (start=15, mask=00001111b, comment=LmmIdx03_Priority)
    * `03_Value` (start=16, mask=11111111b, comment=LmmIdx04_Intensity)
    * `03_Value` (start=17, mask=11111111b, comment=LmmIdx04_TimeOn)
    * `03_Value` (start=18, mask=11111111b, comment=LmmIdx04_TimeOff)
    * `04_Value` (start=19, mask=00001111b, comment=LmmIdx04_Priority)
    * `03_Value` (start=20, mask=11111111b, comment=LmmIdx05_Intensity)
    * `03_Value` (start=21, mask=11111111b, comment=LmmIdx05_TimeOn)
    * `03_Value` (start=22, mask=11111111b, comment=LmmIdx05_TimeOff)
    * `01_Value` (start=23, mask=00001111b, comment=LmmIdx05_Priority)
    * `03_Value` (start=24, mask=11111111b, comment=LmmIdx06_Intensity)
    * `01_Value` (start=25, mask=11111111b, comment=LmmIdx06_TimeOn)
    * `03_Value` (start=26, mask=11111111b, comment=LmmIdx06_TimeOff)
    * `06_Value` (start=27, mask=00001111b, comment=LmmIdx06_Priority)
    * `02_Value` (start=27, mask=00110000b, comment=LmmIdx06_RampType)
    * `01_Value` (start=27, mask=01000000b, comment=LmmIdx06_ErrorImpact)
    * `03_Value` (start=28, mask=11111111b, comment=LmmIdx07_Intensity)
    * `06_Value` (start=31, mask=00001111b, comment=LmmIdx07_Priority)
    * `02_Value` (start=31, mask=00110000b, comment=LmmIdx07_RampType)
    * `03_Value` (start=35, mask=00001111b, comment=LmmIdx08_Priority)
    * `05_Value` (start=39, mask=00001111b, comment=LmmIdx09_Priority)
    * `02_Value` (start=39, mask=00110000b, comment=LmmIdx09_RampType)
    * `02_Value` (start=40, mask=11111111b, comment=LmmIdx10_Intensity)
    * `02_Value` (start=43, mask=00001111b, comment=LmmIdx10_Priority)
    * `02_Value` (start=43, mask=00110000b, comment=LmmIdx10_RampType)
    * `03_Value` (start=44, mask=11111111b, comment=LmmIdx11_Intensity)
    * `04_Value` (start=47, mask=00001111b, comment=LmmIdx11_Priority)
    * `03_Value` (start=48, mask=11111111b, comment=LmmIdx12_Intensity)
    * `04_Value` (start=51, mask=00001111b, comment=LmmIdx12_Priority)
    * `03_Value` (start=134, mask=00111111b, comment=LmmReLut_LgtFct0)
    * `03_Value` (start=134, mask=11000000b, comment=LmmReLut_LogLmpLow0)
    * `02_Value` (start=135, mask=11111100b, comment=LmmReLut_Idx0)
    * `03_Value` (start=136, mask=00111111b, comment=LmmReLut_LgtFct1)
    * `03_Value` (start=136, mask=11000000b, comment=LmmReLut_LogLmpLow1)
    * `02_Value` (start=137, mask=11111100b, comment=LmmReLut_Idx1)
    * `03_Value` (start=138, mask=00111111b, comment=LmmReLut_LgtFct2)
    * `03_Value` (start=138, mask=11000000b, comment=LmmReLut_LogLmpLow2)
    * `02_Value` (start=139, mask=11111100b, comment=LmmReLut_Idx2)

* **Enable GFHB WITH sidemarkers (also code FEM_BODY and KAFAS2)**
  * Group `3000`
    * `01_Value` (start=4, mask=11110000b, comment=HlPrjLabel_HIType)
  * Group `3003`
    * `07_Value` (start=0, end=9, mask=11111111b, comment=SchlechtWetter_C1_Idx)
    * `07_Value` (start=10, end=19, mask=11111111b, comment=SchlechtWetter_C2_Idx)
    * `07_Value` (start=20, end=29, mask=11111111b, comment=Stadt_V_Idx)
    * `07_Value` (start=30, end=39, mask=11111111b, comment=SAE_Idx)
    * `07_Value` (start=40, end=49, mask=11111111b, comment=H10_Landstrasse_C_Idx)
    * `07_Value` (start=50, end=59, mask=11111111b, comment=H8_Autobahn_E3_Idx)
    * `07_Value` (start=60, end=69, mask=11111111b, comment=H6_Autobahn_E2_Idx)
    * `07_Value` (start=70, end=79, mask=11111111b, comment=H5_Autobahn_E1_Idx)
    * `07_Value` (start=80, end=89, mask=11111111b, comment=H4_Autobahn_E_Idx)
    * `08_Value` (start=90, end=99, mask=11111111b, comment=H_2_Idx)
    * `08_Value` (start=100, end=109, mask=11111111b, comment=H_0_Idx)
    * `07_Value` (start=110, end=119, mask=11111111b, comment=H_Plus2_Idx)
    * `08_Value` (start=120, end=129, mask=11111111b, comment=H_Plus4_Idx)
    * `10_Value` (start=130, end=139, mask=11111111b, comment=Blendfreies_Fernlicht_Idx)
    * `09_Value` (start=140, end=149, mask=11111111b, comment=Volles_Fernlicht__Lichthupe_Idx)
  * Group `3004`
    * `08_Value` (start=0, end=9, mask=11111111b, comment=DRL_Idx)
    * `00, 00, 00, 0C, 00, 00, 08, 00, 00, 00` (start=10, end=19, mask=11111111b, comment=POLI1_Idx)
    * `00, 00, 00, 0C, 00, 00, 08, 00, 00, 00` (start=20, end=29, mask=11111111b, comment=POLI2_Idx)
    * `00, 00, 00, 0C, 00, 00, 08, 00, 00, 00` (start=30, end=39, mask=11111111b, comment=POLI3_IDX)
    * `10_Value` (start=40, end=49, mask=11111111b, comment=PLI_Idx)
    * `00, 09, 09, 0C, 00, 00, 0A, 00, 00, 00` (start=60, end=69, mask=11111111b, comment=WELL1_Idx)
    * `00, 00, 00, 0C, 00, 00, 0B, 00, 00, 00` (start=70, end=79, mask=11111111b, comment=WELL2_Idx)
    * `00, 00, 00, 0C, 00, 00, 0B, 00, 00, 00` (start=80, end=89, mask=11111111b, comment=WELL3_Idx)
    * `00, 00, 00, 0C, 00, 00, 0B, 00, 00, 00` (start=90, end=99, mask=11111111b, comment=WELL4_IDX)
    * `00, 02, 02, 0C, 00, 00, 0B, 00, 00, 00` (start=100, end=109, mask=11111111b, comment=FMH_Idx)
    * `00, 02, 02, 0C, 00, 00, 0B, 00, 00, 00` (start=110, end=119, mask=11111111b, comment=REMLI_Idx)
    * `11_Value` (start=120, end=129, mask=11111111b, comment=HBBLINK_Idx)
    * `07_Value` (start=130, end=139, mask=11111111b, comment=DWABLINK_Idx)
    * `07_Value` (start=140, end=149, mask=11111111b, comment=PanicMode_Idx)
    * `11_Value` (start=150, end=159, mask=11111111b, comment=RaidAlarm_Idx)
    * `10_Value` (start=160, end=169, mask=11111111b, comment=Blinken_Idx)
    * `00, 00, 00, 0C, 00, 00, 00, 00, 00, 00` (start=180, end=189, mask=11111111b, comment=SIDEMRKLGT_Idx)
    * `10_Value` (start=190, end=199, mask=11111111b, comment=BLINKEN_PO_Idx)
  * Group `3005`
    * `04_Value` (start=4, mask=11111111b, comment=LmmIdx01_Intensity)
    * `01_Value` (start=7, mask=01000000b, comment=LmmIdx01_ErrorImpact)
    * `02_Value` (start=9, mask=11111111b, comment=LmmIdx02_TimeOn)
    * `02_Value` (start=10, mask=11111111b, comment=LmmIdx02_TimeOff)
    * `03_Value` (start=11, mask=00001111b, comment=LmmIdx02_Priority)
    * `01_Value` (start=11, mask=01000000b, comment=LmmIdx02_ErrorImpact)
    * `04_Value` (start=12, mask=11111111b, comment=LmmIdx03_Intensity)
    * `02_Value` (start=13, mask=11111111b, comment=LmmIdx03_TimeOn)
    * `02_Value` (start=14, mask=11111111b, comment=LmmIdx03_TimeOff)
    * `05_Value` (start=15, mask=00001111b, comment=LmmIdx03_Priority)
    * `03_Value` (start=16, mask=11111111b, comment=LmmIdx04_Intensity)
    * `03_Value` (start=17, mask=11111111b, comment=LmmIdx04_TimeOn)
    * `03_Value` (start=18, mask=11111111b, comment=LmmIdx04_TimeOff)
    * `04_Value` (start=19, mask=00001111b, comment=LmmIdx04_Priority)
    * `03_Value` (start=20, mask=11111111b, comment=LmmIdx05_Intensity)
    * `03_Value` (start=21, mask=11111111b, comment=LmmIdx05_TimeOn)
    * `03_Value` (start=22, mask=11111111b, comment=LmmIdx05_TimeOff)
    * `01_Value` (start=23, mask=00001111b, comment=LmmIdx05_Priority)
    * `03_Value` (start=24, mask=11111111b, comment=LmmIdx06_Intensity)
    * `01_Value` (start=25, mask=11111111b, comment=LmmIdx06_TimeOn)
    * `03_Value` (start=26, mask=11111111b, comment=LmmIdx06_TimeOff)
    * `06_Value` (start=27, mask=00001111b, comment=LmmIdx06_Priority)
    * `02_Value` (start=27, mask=00110000b, comment=LmmIdx06_RampType)
    * `01_Value` (start=27, mask=01000000b, comment=LmmIdx06_ErrorImpact)
    * `03_Value` (start=28, mask=11111111b, comment=LmmIdx07_Intensity)
    * `06_Value` (start=31, mask=00001111b, comment=LmmIdx07_Priority)
    * `02_Value` (start=31, mask=00110000b, comment=LmmIdx07_RampType)
    * `03_Value` (start=35, mask=00001111b, comment=LmmIdx08_Priority)
    * `05_Value` (start=39, mask=00001111b, comment=LmmIdx09_Priority)
    * `02_Value` (start=39, mask=00110000b, comment=LmmIdx09_RampType)
    * `02_Value` (start=40, mask=11111111b, comment=LmmIdx10_Intensity)
    * `02_Value` (start=43, mask=00001111b, comment=LmmIdx10_Priority)
    * `02_Value` (start=43, mask=00110000b, comment=LmmIdx10_RampType)
    * `03_Value` (start=44, mask=11111111b, comment=LmmIdx11_Intensity)
    * `04_Value` (start=47, mask=00001111b, comment=LmmIdx11_Priority)
    * `03_Value` (start=48, mask=11111111b, comment=LmmIdx12_Intensity)
    * `04_Value` (start=51, mask=00001111b, comment=LmmIdx12_Priority)
    * `03_Value` (start=134, mask=00111111b, comment=LmmReLut_LgtFct0)
    * `03_Value` (start=134, mask=11000000b, comment=LmmReLut_LogLmpLow0)
    * `02_Value` (start=135, mask=11111100b, comment=LmmReLut_Idx0)
    * `03_Value` (start=136, mask=00111111b, comment=LmmReLut_LgtFct1)
    * `03_Value` (start=136, mask=11000000b, comment=LmmReLut_LogLmpLow1)
    * `02_Value` (start=137, mask=11111100b, comment=LmmReLut_Idx1)
    * `03_Value` (start=138, mask=00111111b, comment=LmmReLut_LgtFct2)
    * `03_Value` (start=138, mask=11000000b, comment=LmmReLut_LogLmpLow2)
    * `02_Value` (start=139, mask=11111100b, comment=LmmReLut_Idx2)


## `ruben_17non.xml`

**Modules touched:** PMA_PDC (CAFD 00001AB7, author ruben_17non), ICAM (CAFD 0000163C, author ruben_17non), DSC-DXC_CT01 (CAFD 00000629, author ruben_17non), EMF_03TRW (CAFD 0000029B, author ruben_17non), ICMQL (CAFD 0000067B, author ruben_17non), DSC_CT02M (CAFD 00001A33, author ruben_17non), LHM2 (CAFD 000010BA, author ruben_17non), LHM2 (CAFD 000016BF, author ruben_17non), TMS_03 (CAFD 00001082, author ruben_17non), TMS_03 (CAFD 00001083, author ruben_17non), FRM_03CT (CAFD 0000106D, author ruben_17non), FEM_01 BODY (CAFD 00000794, author ruben_17non), IHKA_VA01 (CAFD 00000A3F, author ruben_17non), KOMBI l7_MID (CAFD 000009C8, author ruben_17non), KOMBI L6 BO 6WA (CAFD 00000069, author ruben_17non), DKOMBI 6WB (CAFD 00001060, author ruben_17non), KOMBI L7_BASIS (CAFD 00000760, author ruben_17non), IHKA_VA02 (CAFD 000016EE, author ruben_17non), KAFAS2 (CAFD 00001148, author ruben_17non), HU_NBT (CAFD 00000DED, author ruben_17non)

### PMA_PDC (CAFD 00001AB7) — authored by ruben_17non

* **Cameras/PDC in all speed This disable speed restriction -STEP 1 Go to ICAM for Part2-**
  * Group `300B`
    * `FF` (start=8, mask=11111111b)
    * `FF` (start=9, mask=11111111b)
    * `FF` (start=10, mask=11111111b)
    * `FF` (start=11, mask=11111111b)

### ICAM (CAFD 0000163C) — authored by ruben_17non

* **Cameras/PDC in all speed This disable speed restriction -STEP 2 Go to PMA_PDC for Part1-**
  * Group `3006`
    * `FF` (start=1, mask=11111111b)
    * `FF` (start=2, mask=11111111b)

### DSC-DXC_CT01 (CAFD 00000629) — authored by ruben_17non

* **Automatic Parking Brake Release in cars with automatic transmission -STEP 2 Go to EMF for Part1-**
  * Group `3000`
    * `01` (start=26, mask=00001000b)

* **Enable Launch Control**
  * Group `3000`
    * `01` (start=26, mask=10000000b)

### EMF_03TRW (CAFD 0000029B) — authored by ruben_17non

* **Automatic Parking Brake Release in cars with automatic transmission -STEP 1 Go to DSC for Part2-**
  * Group `3000`
    * `01` (start=0, mask=00001000b)

### ICMQL (CAFD 0000067B) — authored by ruben_17non

* **Sports Mode Configuration Option in iDrive -STEP 1 Go to NBT for Part2-**
  * Group `3000`
    * `Ein` (start=10, mask=00000011b)

* **Change Active Blind Spot Activation Speed 50Km/h to 20Km/h**
  * Group `3000`
    * `20 kmh` (start=190, mask=00111111b)

* **The vehicle start in Mode EcoPro every startup**
  * Group `3000`
    * `01` (start=36, mask=00001000b)

* **Enables Sport+ Mode**
  * Group `3000`
    * `01` (start=190, mask=00111111b)

### DSC_CT02M (CAFD 00001A33) — authored by ruben_17non

* **EURO DSC**
  * Group `3000`
    * `ECE` (start=12, mask=00000011b)

### LHM2 (CAFD 000010BA) — authored by ruben_17non

* **No-Glare High Beam Assistant -Step 2: driver side-**
  * Group `3000`
    * `FA, 64, 00, 00, FA, FA, 00` (start=0, end=6, mask=11111111b)
    * `FA, 64, 00, 00, FA, FA, 00` (start=7, end=13, mask=11111111b)
    * `FA, 00, 00, 19, FA, FA, 00` (start=14, end=20, mask=11111111b)
    * `FA, 00, 00, 00, C8, C8, 00` (start=21, end=27, mask=11111111b)
    * `FA, 00, FA, 00, FA, FA, 00` (start=91, end=97, mask=11111111b)
    * `FA, FA, FA, 00, FA, FA, FA` (start=98, end=104, mask=11111111b)

### LHM2 (CAFD 000016BF) — authored by ruben_17non

* **No-Glare High Beam Assistant -Step 2: passenger side-**
  * Group `3000`
    * `FA, FA, 00, 00, FA, FA, 00` (start=0, end=6, mask=11111111b)
    * `FA, FA, 00, 00, FA, FA, 00` (start=7, end=13, mask=11111111b)
    * `FA, FA, 00, 19, FA, FA, 00` (start=14, end=20, mask=11111111b)
    * `FA, 00, 00, 00, C8, C8, 00` (start=21, end=27, mask=11111111b)
    * `FA, FA, 00, 00, FA, FA, 00` (start=35, end=41, mask=11111111b)
    * `FA, FA, 00, 00, FA, FA, 00` (start=42, end=48, mask=11111111b)
    * `FA, FA, 00, 00, FA, FA, 00` (start=49, end=55, mask=11111111b)
    * `FA, FA, 00, 00, FA, FA, 00` (start=56, end=62, mask=11111111b)
    * `FA, FA, FA, 00, FA, FA, 00` (start=91, end=97, mask=11111111b)
    * `FA, FA, FA, 00, FA, FA, FA` (start=98, end=104, mask=11111111b)

### TMS_03 (CAFD 00001082) — authored by ruben_17non

* **Turn sidemarker LEDs off (driver side)**
  * Group `3005`
    * `00, 03, 00, 00, 00, 03, 00, 00, 64, 03, 00, 00, 2B, 04, 00, 00` (start=16, end=31, mask=11111111b)
    * `00, 03, 00, 00, 00, 03, 00, 00, 64, 03, 00, 00, 2B, 04, 00, 00` (start=32, end=47, mask=11111111b)
    * `00, 03, 00, 00, 00, 03, 00, 00, 64, 03, 00, 00, 2E, 04, 00, 00` (start=80, end=95, mask=11111111b)

* **Turn sidemarker LEDs on (driver side)**
  * Group `3005`
    * `00, 03, 00, 00, 64, 03, 00, 00, 64, 03, 00, 00, 2B, 04, 00, 00` (start=16, end=31, mask=11111111b)
    * `00, 03, 00, 00, 64, 03, 00, 00, 64, 03, 00, 00, 2B, 04, 00, 00` (start=32, end=47, mask=11111111b)
    * `00, 03, 00, 00, 64, 03, 00, 00, 64, 03, 00, 00, 2E, 04, 00, 00` (start=80, end=95, mask=11111111b)

### TMS_03 (CAFD 00001083) — authored by ruben_17non

* **Turn sidemarker LEDs off (passenger side)**
  * Group `3005`
    * `00, 03, 00, 00, 00, 03, 00, 00, 64, 03, 00, 00, 2B, 04, 00, 00` (start=16, end=31, mask=11111111b)
    * `00, 03, 00, 00, 00, 03, 00, 00, 64, 03, 00, 00, 2B, 04, 00, 00` (start=32, end=47, mask=11111111b)
    * `00, 03, 00, 00, 00, 03, 00, 00, 64, 03, 00, 00, 2E, 04, 00, 00` (start=80, end=95, mask=11111111b)

* **Turn sidemarker LEDs on (passenger side)**
  * Group `3005`
    * `00, 03, 00, 00, 64, 03, 00, 00, 64, 03, 00, 00, 2B, 04, 00, 00` (start=16, end=31, mask=11111111b)
    * `00, 03, 00, 00, 64, 03, 00, 00, 64, 03, 00, 00, 2B, 04, 00, 00` (start=32, end=47, mask=11111111b)
    * `00, 03, 00, 00, 64, 03, 00, 00, 64, 03, 00, 00, 2E, 04, 00, 00` (start=80, end=95, mask=11111111b)

### FRM_03CT (CAFD 0000106D) — authored by ruben_17non

* **Halo Led (DRL) MAX intesity with Xenon**
  * Group `3060`
    * `32` (start=1, mask=11111111b)
  * Group `3050`
    * `64` (start=36, mask=11111111b)

* **Automatic Activation of the Hazard Warning System**
  * Group `3050`
    * `Aktiv` (start=2, mask=10000000b)

* **Wellcome light With NSW (hard on)**
  * Group `3050`
    * `02` (start=29, mask=00001100b)

* **Corner light With NSW**
  * Group `3080`
    * `BV_F025_wert_02__Cornerlight_ueber_NSW` (start=0, end=3, mask=11111111b)
    * `BV_F025_wert_02__Cornerlight_ueber_NSW` (start=4, end=7, mask=11111111b)
  * Group `3073`
    * `01` (start=218, mask=00000010b)
    * `01` (start=66, mask=00000001b)

### FEM_01 BODY (CAFD 00000794) — authored by ruben_17non

* **No-Glare High Beam Assistant (Step 3)**
  * Group `3073`
    * `00, 00, 00, 15, 00, 00, 0A, 15, 1F` (start=176, end=184, mask=11111111b)
  * Group `3074`
    * `2E, 3B, 00, 00, 00, 00` (start=81, end=86, mask=11111111b)
    * `2E, 3B, 00, 00, 00, 00` (start=87, end=92, mask=11111111b)
    * `00, 00, 00, 00, 00, 00` (start=93, end=98, mask=11111111b)
    * `00, 00, 00, 00, 00, 00` (start=99, end=104, mask=11111111b)

* **Angel Eyes Parking Light Brightness 50%**
  * Group `3062`
    * `32` (start=68, mask=11111111b)
    * `32` (start=69, mask=11111111b)

* **Angel Eyes Parking Light Brightness 100%**
  * Group `3062`
    * `64` (start=68, mask=11111111b)
    * `64` (start=69, mask=11111111b)

* **Angel Eyes Brightness 50% Headlamp On**
  * Group `3062`
    * `32` (start=46, mask=11111111b)
    * `32` (start=57, mask=11111111b)

* **Angel Eyes Brightness 100% Headlamp On**
  * Group `3062`
    * `64` (start=46, mask=11111111b)
    * `64` (start=57, mask=11111111b)

* **Angel Eyes Brightness 50% DRL**
  * Group `3062`
    * `32` (start=90, mask=11111111b)
    * `32` (start=101, mask=11111111b)

* **Angel Eyes Brightness 100% DRL**
  * Group `3062`
    * `64` (start=90, mask=11111111b)
    * `64` (start=101, mask=11111111b)

* **Enable DRL**
  * Group `3060`
    * `TFL_S` (start=31, mask=00110000b)

* **Cornering Lights**
  * Group `3073`
    * `01` (start=218, mask=00000010b)
    * `01` (start=66, mask=00000001b)
  * Group `3066`
    * `01` (start=80, mask=00000001b)
    * `01` (start=0, mask=00000001b)
  * Group `3062`
    * `0B` (start=121, mask=00111111b)
    * `0B` (start=110, mask=00111111b)

* **Fog Lamps Welcome Light**
  * Group `3063`
    * `Soft_On` (start=55, mask=11000000b)
    * `Soft_On` (start=66, mask=11000000b)

* **Auto Start/Stop Always Off**
  * Group `3023`
    * `Aktiv` (start=0, mask=00010000b)

* **Auto Start/Stop Remember Last Setting**
  * Group `3023`
    * `Aktiv` (start=0, mask=00100000b)

* **Turn off Radio/Navigation with Opening Driver Door**
  * Group `3020`
    * `Aktiv` (start=1, mask=00000001b)

### IHKA_VA01 (CAFD 00000A3F) — authored by ruben_17non

* **AC Last Settings Memory**
  * Group `3002`
    * `Aktiv` (start=0, mask=00000010b)

* **AC Recirc Last Settings Memory**
  * Group `3002`
    * `Aktiv` (start=0, mask=00000001b)

### KOMBI l7_MID (CAFD 000009C8) — authored by ruben_17non

* **Digital Speed Display**
  * Group `3000`
    * `Aktiv` (start=1, mask=00000010b)

* **Disable Speed Correction**
  * Group `3000`
    * `Nicht_Aktiv` (start=1, mask=01000000b)

* **M Performance Logo**
  * Group `3000`
    * `01` (start=0, mask=11110000b)

* **Clock Synchronization via GPS**
  * Group `3000`
    * `Aktiv` (start=1, mask=10000000b)

### KOMBI L6 BO 6WA (CAFD 00000069) — authored by ruben_17non

* **Digital Speed Display**
  * Group `3000`
    * `Aktiv` (start=1, mask=00000010b)

* **Enable Compass Grafik**
  * Group `3003`
    * `Aktiv` (start=9, mask=01000000b)

* **M Performance Logo in kombi**
  * Group `3000`
    * `01` (start=53, mask=11110000b)
    * `01` (start=53, mask=00001111b)
  * Group `3003`
    * `01` (start=9, mask=00000001b)

* **Cosmetic Change to Instrument Cluster ORANGE Lines in Day Mode**
  * Group `3000`
    * `00` (start=41, mask=00000010b)

* **Cosmetic Change to Instrument Cluster WHITE Lines in Day Mode**
  * Group `3000`
    * `01` (start=41, mask=00000010b)

* **Cosmetic Change to Instrument Cluster ORANGE Lines in Night Mode**
  * Group `3000`
    * `00` (start=41, mask=00000100b)

* **Cosmetic Change to Instrument Cluster WHITE Lines in Night Mode**
  * Group `3000`
    * `01` (start=41, mask=00000100b)

* **Goodbaye/Wellcome screen display as MPM Logo**
  * Group `300B`
    * `Aktiv` (start=29, mask=01000000b)
    * `Aktiv` (start=30, mask=11110000b)

* **Clock Synchronization via GPS**
  * Group `3000`
    * `Aktiv` (start=1, mask=10000000b)

* **DIM_NACHT_AUS MODO ILUMINACION BLANCA SIEMPRE**
  * Group `3007`
    * `FF` (start=10, mask=11111111b)

* **Change of the Navigation Graphics by New style in the Instrument Cluster**
  * Group `3000`
    * `01` (start=40, mask=00100000b)

* **TEST QUITAR ERROR EEPROM ID KOMBI**
  * Group `3004`
    * `00` (start=23, mask=10000000b)
    * `00` (start=28, mask=00010000b)

### DKOMBI 6WB (CAFD 00001060) — authored by ruben_17non

* **Digital Speed Display in BC**
  * Group `3000`
    * `Aktiv` (start=1, mask=00000010b)

* **Digital Speed Display BC_Digital_V_Einheit**
  * Group `3000`
    * `02` (start=0, mask=00110000b)

* **Digital Speed Display DIGITAL_TACHO_ENABLE**
  * Group `3000`
    * `03` (start=42, mask=11110000b)

* **TORQUE GRAFIK IN SPORT MODE -MOTORLEISTUNG_ENABLE-**
  * Group `3003`
    * `01` (start=11, mask=00000010b)

### KOMBI L7_BASIS (CAFD 00000760) — authored by ruben_17non

* **Digital Speed Display in BC**
  * Group `3000`
    * `Aktiv` (start=1, mask=00000010b)

* **Motor Temperature in BC**
  * Group `3000`
    * `Aktiv` (start=3, mask=00010000b)

### IHKA_VA02 (CAFD 000016EE) — authored by ruben_17non

* **HVAC will remember to stay off if set to off before car shutdown**
  * Group `3003`
    * `Aktiv` (start=0, mask=00000010b)

* **Do not turn on AC if Auto Button is pressed**
  * Group `3003`
    * `00` (start=0, mask=00000100b)

### KAFAS2 (CAFD 00001148) — authored by ruben_17non

* **Detect Road mark (Painted lane markings) + Detect grass and road sides**
  * Group `3020`
    * `02` (start=2, mask=00000011b)

* **Enable High Beam Assistant FLA**
  * Group `3050`
    * `01` (start=1, mask=00000001b)

* **Enable High Beam GlareFree**
  * Group `3050`
    * `01` (start=1, mask=10000000b)

### HU_NBT (CAFD 00000DED) — authored by ruben_17non

* **Enable Video Player From USB + All Video Plugins**
  * Group `3000`
    * `Aktiv` (start=6, mask=01000000b)
    * `Aktiv` (start=15, mask=00010000b)
    * `Aktiv` (start=15, mask=00100000b)
    * `Aktiv` (start=15, mask=01000000b)
    * `Aktiv` (start=13, mask=00000100b)
  * Group `3003`
    * `Both` (start=33, mask=00000110b)

* **Eco Pro Prediction Diagram/Grafik**
  * Group `3000`
    * `Aktiv` (start=135, mask=10000000b)
    * `Aktiv` (start=17, mask=00001000b)
  * Group `3001`
    * `Aktiv` (start=64, mask=00000010b)
    * `Aktiv` (start=64, mask=00000100b)

* **Checkbox for Enable/Disable Sailing ECO PRO**
  * Group `3000`
    * `Aktiv` (start=103, mask=10000000b)

* **Lock/Unlock Sound Confirm Checkbox With alarm only**
  * Group `3000`
    * `Aktiv` (start=110, mask=00000001b)

* **Ambient light, MODERN to SPORT and Deactivation Check Box**
  * Group `3000`
    * `Sport` (start=109, mask=01110000b)
    * `deaktivierung_bmw` (start=35, mask=11000000b)

* **Disable Top View Camara TEST**
  * Group `3001`
    * `00` (start=18, mask=00100000b)

* **Enable Compass**
  * Group `3000`
    * `Aktiv` (start=5, mask=00000001b)

* **M Performance Start Animation of HMI**
  * Group `3001`
    * `Animation` (start=62, mask=00000110b)
    * `variant_01` (start=62, mask=01111000b)

* **Sport Display Power and Torque Gauge - Red/Silver M Performance**
  * Group `3000`
    * `Aktiv` (start=133, mask=01000000b)
    * `Aktiv` (start=101, mask=00010000b)
    * `Aktiv` (start=107, mask=00000100b)

* **Sport Display Power and Torque Gauge - Amber Standard**
  * Group `3000`
    * `Nicht_Aktiv` (start=133, mask=01000000b)
    * `Aktiv` (start=101, mask=00010000b)
    * `Aktiv` (start=107, mask=00000100b)

* **Sports Mode Configuration Option in iDrive (STEP 2 Go to ICM for Part1)**
  * Group `3001`
    * `popup_and_config` (start=55, mask=00011000b)

* **Disable Legal Disclaimer**
  * Group `3001`
    * `00` (start=58, mask=11111111b)

* **Disable Camera/PDC Legal Disclaimer**
  * Group `3001`
    * `00` (start=52, mask=11111111b)

* **Show DRL Option in iDrive**
  * Group `3000`
    * `02` (start=92, mask=00011000b)

* **Show Tire Pressure and Temperature in iDrive**
  * Group `3001`
    * `Aktiv` (start=1, mask=00100000b)

* **Show Volume Popup Display**
  * Group `3002`
    * `Aktiv` (start=52, mask=01000000b)

* **Enable Route Preview**
  * Group `3000`
    * `Aktiv` (start=135, mask=00001000b)
    * `Aktiv` (start=111, mask=00001000b)

* **Enable Road Preview**
  * Group `3000`
    * `Aktiv` (start=59, mask=00100000b)

* **Enable Trip Import via USB**
  * Group `3000`
    * `Aktiv` (start=61, mask=00000001b)

* **Rear Camera Zoom -Trailer Mode- Only With Rear Camera**
  * Group `3001`
    * `Aktiv` (start=54, mask=00000001b)

* **Activate BLUETOOTH Data Profile (PAN/DUN Profile)**
  * Group `3003`
    * `Aktiv` (start=3, mask=00000010b)
    * `Aktiv` (start=3, mask=00000100b)

* **Activate Siri Eyes-Free**
  * Group `3003`
    * `Aktiv` (start=3, mask=00001000b)

* **Activate APPLE ENHANCEMENTS**
  * Group `3000`
    * `Aktiv` (start=22, mask=10000000b)

* **Enable Traffic Information via TMC**
  * Group `3000`
    * `Aktiv` (start=59, mask=00010000b)
  * Group `3002`
    * `Aktiv` (start=23, mask=00000100b)
    * `Aktiv` (start=24, mask=00000010b)
    * `Aktiv` (start=23, mask=00100000b)

* **Speech to Text Dictate Email or SMS Response**
  * Group `3003`
    * `Aktiv` (start=1, mask=00010000b)

* **Speech to Text Transformation Supported**
  * Group `3003`
    * `Aktiv` (start=11, mask=00010000b)

* **Create New Voice Email**
  * Group `3003`
    * `Aktiv` (start=12, mask=00000001b)

* **Adds GPS current location to the Nav menu items at the bottom of the screen.**
  * Group `3000`
    * `Aktiv` (start=96, mask=10000000b)


## `siegester.xml`

**Modules touched:** KAFAS4 (CAFD 000040F9, author siegester, series S18A), BDC_BODY3 (CAFD 000044ED, author siegester, series S18A), BDC_BODY3 (CAFD 00001DF8, author siegester, series S18A), BDC_BODY3 (CAFD 00005665, author siegester, series S18A), SAS3 (CAFD 000042C1, author siegester, series S18A), HU_MGU (CAFD 00003E52, author siegester, series S18A), RAM (CAFD 00004224, author siegester, series S18A)

### KAFAS4 (CAFD 000040F9) — authored by siegester | Series: S18A

* **(2/2) GFHB - Anti-dazzle headlights - Improved dynamics**
  * Group `3102`
    * `01` (start=6, mask=11111111b, comment=C_FLA_COUNTRY_WITH_MUTIPLE_REFLECTORS)
    * `00` (start=7, mask=11111111b, comment=C_FLA_US_SENSITIVITY_MODE)
    * `03` (start=14, mask=11111111b, comment=C_FLA_BS_ENTER_THRESH)
    * `02` (start=15, mask=11111111b, comment=C_FLA_BS_EXIT_THRESH)

### BDC_BODY3 (CAFD 000044ED) — authored by siegester | Series: S18A

* **(2/2) Enable Independent Turn Signal**
  * Group `3510`
    * `00` (start=19, mask=00000001b, comment=FH_FREIGABE_PWF_US)

### BDC_BODY3 (CAFD 00001DF8) — authored by siegester | Series: S18A

* **(1/2) Enable GFHB - Anti-dazzle headlights**
  * Group `3531`
    * `01` (start=190, mask=00000100b, comment=C_AFS_ECO_LEVEL_3_ENA)
    * `01` (start=190, mask=00000001b, comment=C_AFS_ENA)
  * Group `3530`
    * `01` (start=245, mask=00000001b, comment=C_BLC_PRE_ENA)
    * `AFS` (start=44, end=46, mask=11111111b, comment=LUT_FLC_FORWARDLIGHTING_Y)
  * Group `3532`
    * `23` (start=192, mask=11111111b, comment=C_CLC_CURV_V2)
    * `28` (start=193, mask=11111111b, comment=C_CLC_CURV_V3)
    * `01` (start=186, mask=00110000b, comment=C_CLC_EXT_ENA)
    * `01` (start=214, mask=00000100b, comment=C_HBA_DIM_ENA)
    * `3C` (start=217, mask=11111111b, comment=C_HBA_GFHBA_ENA_V_HI)
    * `01` (start=214, mask=00000010b, comment=C_HBA_GFHB_ENA)
    * `standard/init` (start=93, end=123, mask=11111111b, comment=LUT_AFS_CODRV_HOR)
    * `F040_G005_AHL/G015_G020_Laser` (start=62, end=92, mask=11111111b, comment=LUT_AFS_DRV_HOR)

### BDC_BODY3 (CAFD 00005665) — authored by siegester | Series: S18A

* **(1/2) Enable Independent Turn Signal**
  * Group `3700`
    * `CCM0` (start=20, end=21, mask=11111111b, comment=POL_L_CCM)
    * `Inactive` (start=22, mask=00011000b, comment=POL_L_UE_SPG_SCHUTZ)
    * `Inactive` (start=27, mask=00011000b, comment=POL_R_UE_SPG_SCHUTZ)
    * `Inactive` (start=42, mask=00011000b, comment=SML_L_UE_SPG_SCHUTZ)
    * `Inactive` (start=47, mask=00011000b, comment=SML_R_UE_SPG_SCHUTZ)
    * `default` (start=60, end=61, mask=11111111b, comment=FRA_V_L_CCM)
    * `default` (start=65, end=66, mask=11111111b, comment=FRA_V_R_CCM)
    * `Inactive` (start=122, mask=00011000b, comment=BFD_L_UE_SPG_SCHUTZ)
    * `Inactive` (start=127, mask=00011000b, comment=BFD_R_UE_SPG_SCHUTZ)
    * `CCM114` (start=130, end=131, mask=11111111b, comment=NSL_L_CCM)
    * `Active, Active` (start=132, mask=00011000b, comment=NSL_L_UE_SPG_SCHUTZ)
    * `CCM129` (start=135, end=136, mask=11111111b, comment=NSL_R_CCM)
    * `Active, Active` (start=137, mask=00011000b, comment=NSL_R_UE_SPG_SCHUTZ)
  * Group `3702`
    * `disable` (start=1, mask=01000000b, comment=LIC_FEATURE_14)
  * Group `3703`
    * `G20_ECE_code2` (start=0, end=199, mask=11111111b, comment=LIC_NIVEAU_OVERRIDE_INDEX)
  * Group `3704`
    * `G20_ECE_code1` (start=0, end=239, mask=11111111b, comment=LIC_NIVEAU_OVERRIDE_DATA_0)
  * Group `3706`
    * `UNK_PARAM_25` (start=0, end=241, mask=11111111b, comment=LIC_LOG_LAMP_2_PHYS_LAMP_INDEX)
  * Group `3707`
    * `UNK_PARAM_25` (start=0, end=213, mask=11111111b, comment=LIC_LOG_LAMP_2_PHYS_LAMP_DATA)
  * Group `3708`
    * `UNK_PARAM_28` (start=0, end=36, mask=11111111b, comment=LIC_VERSION_DATA)
  * Group `3709`
    * `UNK_PARAM_3` (start=0, end=211, mask=11111111b, comment=LIC_EDGE_CUTTER_RULE_ASSIGNMENT)

### SAS3 (CAFD 000042C1) — authored by siegester | Series: S18A

* **(1/2) Enable Automatic Lane Change Assistant (HU_MGU)**
  * Group `3000`
    * `01` (start=137, mask=11111111b, comment=C_SWA_VORHANDEN)

### HU_MGU (CAFD 00003E52) — authored by siegester | Series: S18A

* **Full sms display**
  * Group `3001`
    * `whole_text` (start=7, mask=00001110b, comment=PIM_Driving_Text_Length)

* **Change Startup Emblem to BMW ///M**
  * Group `3000`
    * `bmw_m` (start=11, mask=00011110b, comment=STARTUP_EMBLEM)

* **enable 1.0 on g meter**
  * Group `3008`
    * `1.0` (start=5, mask=00011100b, comment=G_METER_MAX_VAL)

* **(2/2) Enable Automatic Lane Change Assistant (SAS3)**
  * Group `300A`
    * `01` (start=11, mask=00000001b, comment=SPURWECHSELASSISTENT)

### RAM (CAFD 00004224) — authored by siegester | Series: S18A

* **Disable Active Sound Inside (ASD)**
  * Group `3001`
    * `00` (start=19, mask=00000001b, comment=ASD_INSIDE)


## `simpaty.xml`

**Modules touched:** SAS (CAFD 00001C7A, author Simpaty, series G001,G011,G030), HU_NBT_EVO (CAFD 00001EF6, author Simpaty, series G001,G011,G030)

### SAS (CAFD 00001C7A) — authored by Simpaty | Series: G001,G011,G030

* **ENABLE Lane Change Assistant. Part 1 of 2. See NBT2**
  * Group `3000`
    * `01` (start=73, mask=11111111b, comment=C_SWA_Vorhanden)

* **DISABLE Lane Change Assistant. Part 1 of 2. See NBT2**
  * Group `3000`
    * `00` (start=73, mask=11111111b, comment=C_SWA_Vorhanden)

### HU_NBT_EVO (CAFD 00001EF6) — authored by Simpaty | Series: G001,G011,G030

* **ENABLE Lane Change Assistant. Part 2 of 2. See SAS**
  * Group `300A`
    * `01` (start=11, mask=11000000b, comment=Spurwechselassistent)

* **DISABLE Lane Change Assistant. Part 2 of 2. See SAS**
  * Group `300A`
    * `00` (start=11, mask=11000000b, comment=Spurwechselassistent)


## `stanleyy.xml`

**Modules touched:** ACSM_5 (CAFD 00001B2D, author stanleyy, series G011, G030), SAS2 (CAFD 00001C7A, author stanleyy, series G011, G030), DME_BAC2 (CAFD 000029B7, author stanleyy, series G011, G030)

### ACSM_5 (CAFD 00001B2D) — authored by stanleyy | Series: G011, G030

* **Increased speed limits for surround/rear view cameras activation/deactivation**
  * Group `3300`
    * `FF` (start=7, mask=11111111b, comment=v_schwelle_1_kmh)
    * `FF` (start=8, mask=11111111b, comment=v_schelle_2_kmh)
    * `FF` (start=9, mask=11111111b, comment=d_schwelle_1_kmh)
    * `FF` (start=10, mask=11111111b, comment=d_schwelle_2_kmh)

* **Default speed limits for surround/rear view cameras activation/deactivation**
  * Group `3300`
    * `23` (start=7, mask=11111111b, comment=v_schwelle_1_kmh)
    * `0F` (start=8, mask=11111111b, comment=v_schelle_2_kmh)
    * `32` (start=9, mask=11111111b, comment=d_schwelle_1_kmh)
    * `0A` (start=10, mask=11111111b, comment=d_schwelle_2_kmh)

### SAS2 (CAFD 00001C7A) — authored by stanleyy | Series: G011, G030

* **Low default distance value for adaptive cruise control**
  * Group `3000`
    * `Stufe1` (start=0, mask=11111111b, comment=C_Abstandsstufe_init)

* **Factory default distance value for adaptive cruise control**
  * Group `3000`
    * `Stufe3` (start=0, mask=11111111b, comment=C_Abstandsstufe_init)

### DME_BAC2 (CAFD 000029B7) — authored by stanleyy | Series: G011, G030

* **Rembember Auto Start/Stop last value**
  * Group `3020`
    * `On` (start=39, mask=00000011b, comment=TCM_MSA_MEMORY)

* **Don't rembember Auto Start/Stop last value**
  * Group `3020`
    * `Off` (start=39, mask=00000011b, comment=TCM_MSA_MEMORY)


## `tutuianu_daniel.xml`

**Modules touched:** KAFAS (CAFD 00000122, author tutuianu_daniel), HU_NBT_EVO (CAFD 00001EF6, author tutuianu_daniel), BDC_01 (CAFD 000017BE, author tutuianu_daniel), BDC_01 (CAFD 000017BC, author tutuianu_daniel), ACSM_5 (CAFD 00001B29, author tutuianu_daniel)

### KAFAS (CAFD 00000122) — authored by tutuianu_daniel

* **SLI 1 Romania No speed limit info in this country (get your country code uppercase in hex http://www.unit-conversion.info/texttools/hexadecimal/  )**
  * Group `3030`
    * `52, 4F` (start=2, end=3, mask=11111111b, comment=52,4F means R,O)
  * Group `3010`
    * `aktiv` (start=0, mask=00010000b, comment=COD_ELECTRICAL_HORIZON)

### HU_NBT_EVO (CAFD 00001EF6) — authored by tutuianu_daniel

* **Touchscreen activation**
  * Group `3005`
    * `aktiv` (start=67, mask=00000010b)
    * `aktiv` (start=67, mask=00000100b)
    * `aktiv` (start=68, mask=00000001b)
  * Group `300B`
    * `aktiv` (start=5, mask=00000001b)

* **NBT EVO GPS use internal port**
  * Group `3000`
    * `aktiv` (start=105, mask=00100000b)
    * `navigation` (start=19, mask=00000110b)
  * Group `3003`
    * `aktiv` (start=18, mask=00000001b)
    * `nicht_aktiv` (start=3, mask=11100000b)
  * Group `3006`
    * `aktiv` (start=28, mask=00010000b)

* **NBT EVO GPS use ATM - OABR port**
  * Group `3000`
    * `aktiv` (start=105, mask=00100000b)
    * `navigation` (start=19, mask=00000110b)
  * Group `3003`
    * `aktiv` (start=18, mask=00000001b)
    * `atm` (start=3, mask=11100000b)
  * Group `3006`
    * `nicht_aktiv` (start=28, mask=00010000b)

* **Apple Carplay. Need to upload 143 FSC either OEM or retrofit pack.**
  * Group `3004`
    * `aktiv` (start=0, mask=00000100b)
  * Group `3000`
    * `aktiv` (start=110, mask=10000000b)
    * `nicht_aktiv` (start=19, mask=01000000b)
    * `nicht_aktiv` (start=19, mask=10000000b)
    * `aktiv` (start=39, mask=10000000b)

* **APIX 1 8.8 inch 1280 x 480**
  * Group `3005`
    * `apix1` (start=68, mask=00001110b)
    * `18` (start=68, mask=00110000b)
    * `spi` (start=68, mask=11000000b)
    * `1280_480` (start=69, mask=00000111b)
    * `8_8` (start=69, mask=00111000b)

* **APIX 1 10.25 inch 1280 x 480**
  * Group `3005`
    * `apix1` (start=68, mask=00001110b)
    * `18` (start=68, mask=00110000b)
    * `spi` (start=68, mask=11000000b)
    * `1280_480` (start=69, mask=00000111b)
    * `10_25` (start=69, mask=00111000b)

* **APIX 2 8.8 inch 1280 x 480**
  * Group `3005`
    * `apix2` (start=68, mask=00001110b)
    * `24` (start=68, mask=00110000b)
    * `mii` (start=68, mask=11000000b)
    * `1280_480` (start=69, mask=00000111b)
    * `8_8` (start=69, mask=00111000b)

* **APIX 2 10.25 inch 1280 x 480**
  * Group `3005`
    * `apix2` (start=68, mask=00001110b)
    * `24` (start=68, mask=00110000b)
    * `mii` (start=68, mask=11000000b)
    * `1280_480` (start=69, mask=00000111b)
    * `10_25` (start=69, mask=00111000b)

* **APIX 2 8.8 inch 1440 x 540**
  * Group `3005`
    * `apix2` (start=68, mask=00001110b)
    * `24` (start=68, mask=00110000b)
    * `mii` (start=68, mask=11000000b)
    * `1440_540` (start=69, mask=00000111b)
    * `8_8` (start=69, mask=00111000b)

* **APIX 2 10.25 inch 1440 x 540**
  * Group `3005`
    * `apix2` (start=68, mask=00001110b)
    * `24` (start=68, mask=00110000b)
    * `mii` (start=68, mask=11000000b)
    * `1440_540` (start=69, mask=00000111b)
    * `10_25` (start=69, mask=00111000b)

### BDC_01 (CAFD 000017BE) — authored by tutuianu_daniel

* **Ambient colors - green, red and violett ( old firmware )**
  * Group `3070`
    * `59` (start=60, mask=11111111b, comment=weiss)
    * `55` (start=61, mask=11111111b, comment=gruen)
    * `55` (start=62, mask=11111111b, comment=gruen)
    * `55` (start=63, mask=11111111b, comment=gruen)
    * `55` (start=64, mask=11111111b, comment=gruen)
    * `55` (start=65, mask=11111111b, comment=gruen)
    * `55` (start=66, mask=11111111b, comment=gruen)
    * `55` (start=67, mask=11111111b, comment=gruen)
    * `55` (start=68, mask=11111111b, comment=gruen)
    * `59` (start=69, mask=11111111b, comment=weiss)
    * `06` (start=70, mask=11111111b, comment=rot)
    * `06` (start=71, mask=11111111b, comment=rot)
    * `06` (start=72, mask=11111111b, comment=rot)
    * `06` (start=73, mask=11111111b, comment=rot)
    * `06` (start=74, mask=11111111b, comment=rot)
    * `06` (start=75, mask=11111111b, comment=rot)
    * `06` (start=76, mask=11111111b, comment=rot)
    * `06` (start=77, mask=11111111b, comment=rot)
    * `59` (start=78, mask=11111111b, comment=weiss)
    * `B6` (start=79, mask=11111111b, comment=violett)
    * `B6` (start=80, mask=11111111b, comment=violett)
    * `B6` (start=81, mask=11111111b, comment=violett)
    * `B6` (start=82, mask=11111111b, comment=violett)
    * `B6` (start=83, mask=11111111b, comment=violett)
    * `B6` (start=84, mask=11111111b, comment=violett)
    * `B6` (start=85, mask=11111111b, comment=violett)
    * `B6` (start=86, mask=11111111b, comment=violett)

* **Ambient colors - green, red and violett ( new firmware )**
  * Group `3076`
    * `00` (start=126, mask=11111111b, comment=green)
    * `FF` (start=127, mask=11111111b, comment=green)
    * `00` (start=128, mask=11111111b, comment=green)
    * `00` (start=129, mask=11111111b, comment=green)
    * `FF` (start=130, mask=11111111b, comment=green)
    * `00` (start=131, mask=11111111b, comment=green)
    * `00` (start=132, mask=11111111b, comment=green)
    * `FF` (start=133, mask=11111111b, comment=green)
    * `00` (start=134, mask=11111111b, comment=green)
    * `00` (start=135, mask=11111111b, comment=green)
    * `FF` (start=136, mask=11111111b, comment=green)
    * `00` (start=137, mask=11111111b, comment=green)
    * `00` (start=138, mask=11111111b, comment=green)
    * `FF` (start=139, mask=11111111b, comment=green)
    * `00` (start=140, mask=11111111b, comment=green)
    * `00` (start=141, mask=11111111b, comment=green)
    * `FF` (start=142, mask=11111111b, comment=green)
    * `00` (start=143, mask=11111111b, comment=green)
    * `00` (start=144, mask=11111111b, comment=green)
    * `FF` (start=145, mask=11111111b, comment=green)
    * `00` (start=146, mask=11111111b, comment=green)
    * `FF` (start=147, mask=11111111b, comment=red)
    * `00` (start=148, mask=11111111b, comment=red)
    * `00` (start=149, mask=11111111b, comment=red)
    * `FF` (start=150, mask=11111111b, comment=red)
    * `00` (start=151, mask=11111111b, comment=red)
    * `00` (start=152, mask=11111111b, comment=red)
    * `FF` (start=153, mask=11111111b, comment=red)
    * `00` (start=154, mask=11111111b, comment=red)
    * `00` (start=155, mask=11111111b, comment=red)
    * `FF` (start=156, mask=11111111b, comment=red)
    * `00` (start=157, mask=11111111b, comment=red)
    * `00` (start=158, mask=11111111b, comment=red)
    * `FF` (start=159, mask=11111111b, comment=red)
    * `00` (start=160, mask=11111111b, comment=red)
    * `00` (start=161, mask=11111111b, comment=red)
    * `FF` (start=162, mask=11111111b, comment=red)
    * `00` (start=163, mask=11111111b, comment=red)
    * `00` (start=164, mask=11111111b, comment=red)
    * `FF` (start=165, mask=11111111b, comment=red)
    * `00` (start=166, mask=11111111b, comment=red)
    * `00` (start=167, mask=11111111b, comment=red)
    * `FF` (start=168, mask=11111111b, comment=violett)
    * `00` (start=169, mask=11111111b, comment=violett)
    * `FF` (start=170, mask=11111111b, comment=violett)
    * `FF` (start=171, mask=11111111b, comment=violett)
    * `00` (start=172, mask=11111111b, comment=violett)
    * `FF` (start=173, mask=11111111b, comment=violett)
    * `FF` (start=174, mask=11111111b, comment=violett)
    * `00` (start=175, mask=11111111b, comment=violett)
    * `FF` (start=176, mask=11111111b, comment=violett)
    * `FF` (start=177, mask=11111111b, comment=violett)
    * `00` (start=178, mask=11111111b, comment=violett)
    * `FF` (start=179, mask=11111111b, comment=violett)
    * `FF` (start=180, mask=11111111b, comment=violett)
    * `00` (start=181, mask=11111111b, comment=violett)
    * `FF` (start=182, mask=11111111b, comment=violett)
    * `FF` (start=183, mask=11111111b, comment=violett)
    * `00` (start=184, mask=11111111b, comment=violett)
    * `FF` (start=185, mask=11111111b, comment=violett)
    * `FF` (start=186, mask=11111111b, comment=violett)
    * `00` (start=187, mask=11111111b, comment=violett)
    * `FF` (start=188, mask=11111111b, comment=violett)

### BDC_01 (CAFD 000017BC) — authored by tutuianu_daniel

* **Ambient colors - green, red and violett ( new firmware )**
  * Group `3074`
    * `00` (start=168, mask=11111111b, comment=green)
    * `FF` (start=169, mask=11111111b, comment=green)
    * `00` (start=170, mask=11111111b, comment=green)
    * `00` (start=171, mask=11111111b, comment=green)
    * `FF` (start=172, mask=11111111b, comment=green)
    * `00` (start=173, mask=11111111b, comment=green)
    * `00` (start=174, mask=11111111b, comment=green)
    * `FF` (start=175, mask=11111111b, comment=green)
    * `00` (start=176, mask=11111111b, comment=green)
    * `00` (start=177, mask=11111111b, comment=green)
    * `FF` (start=178, mask=11111111b, comment=green)
    * `00` (start=179, mask=11111111b, comment=green)
    * `00` (start=180, mask=11111111b, comment=green)
    * `FF` (start=181, mask=11111111b, comment=green)
    * `00` (start=182, mask=11111111b, comment=green)
    * `00` (start=183, mask=11111111b, comment=green)
    * `FF` (start=184, mask=11111111b, comment=green)
    * `00` (start=185, mask=11111111b, comment=green)
    * `00` (start=186, mask=11111111b, comment=green)
    * `FF` (start=187, mask=11111111b, comment=green)
    * `00` (start=188, mask=11111111b, comment=green)
    * `FF` (start=189, mask=11111111b, comment=red)
    * `00` (start=190, mask=11111111b, comment=red)
    * `00` (start=191, mask=11111111b, comment=red)
    * `FF` (start=192, mask=11111111b, comment=red)
    * `00` (start=193, mask=11111111b, comment=red)
    * `00` (start=194, mask=11111111b, comment=red)
    * `FF` (start=195, mask=11111111b, comment=red)
    * `00` (start=196, mask=11111111b, comment=red)
    * `00` (start=197, mask=11111111b, comment=red)
    * `FF` (start=198, mask=11111111b, comment=red)
    * `00` (start=199, mask=11111111b, comment=red)
    * `00` (start=200, mask=11111111b, comment=red)
    * `FF` (start=201, mask=11111111b, comment=red)
    * `00` (start=202, mask=11111111b, comment=red)
    * `00` (start=203, mask=11111111b, comment=red)
    * `FF` (start=204, mask=11111111b, comment=red)
    * `00` (start=205, mask=11111111b, comment=red)
    * `00` (start=206, mask=11111111b, comment=red)
    * `FF` (start=207, mask=11111111b, comment=red)
    * `00` (start=208, mask=11111111b, comment=red)
    * `00` (start=209, mask=11111111b, comment=red)
    * `FF` (start=210, mask=11111111b, comment=violett)
    * `00` (start=211, mask=11111111b, comment=violett)
    * `FF` (start=212, mask=11111111b, comment=violett)
    * `FF` (start=213, mask=11111111b, comment=violett)
    * `00` (start=214, mask=11111111b, comment=violett)
    * `FF` (start=215, mask=11111111b, comment=violett)
    * `FF` (start=216, mask=11111111b, comment=violett)
    * `00` (start=217, mask=11111111b, comment=violett)
    * `FF` (start=218, mask=11111111b, comment=violett)
    * `FF` (start=219, mask=11111111b, comment=violett)
    * `00` (start=220, mask=11111111b, comment=violett)
    * `FF` (start=221, mask=11111111b, comment=violett)
    * `FF` (start=222, mask=11111111b, comment=violett)
    * `00` (start=223, mask=11111111b, comment=violett)
    * `FF` (start=224, mask=11111111b, comment=violett)
    * `FF` (start=225, mask=11111111b, comment=violett)
    * `00` (start=226, mask=11111111b, comment=violett)
    * `FF` (start=227, mask=11111111b, comment=violett)
    * `FF` (start=228, mask=11111111b, comment=violett)
    * `00` (start=229, mask=11111111b, comment=violett)
    * `FF` (start=230, mask=11111111b, comment=violett)

### ACSM_5 (CAFD 00001B29) — authored by tutuianu_daniel

* **DISABLE Seat Belt Status and Reminder Chime (Driver) - 2016+ Firmware**
  * Group `3001`
    * `00` (start=0, mask=11111111b, comment=SBR_nicht_verbaut)

* **DISABLE Seat Belt Status and Reminder Chime (Passenger) - 2016+ Firmware**
  * Group `3001`
    * `00` (start=1, mask=11111111b, comment=SBR_nicht_verbaut)

* **ENABLE Seat Belt Status and Reminder Chime (Driver) - 2016+ Firmware**
  * Group `3001`
    * `04` (start=0, mask=11111111b, comment=SBR_ohne_SBE)

* **ENABLE Seat Belt Status and Reminder Chime (Passenger) - 2016+ Firmware**
  * Group `3001`
    * `03` (start=1, mask=11111111b, comment=SBR_mit_SBE)


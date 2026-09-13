# NK Huset — WEEKLY roster supplement (v0.2)

The 184 `block=weekly` rows of `nk-huset-embodied-roster.csv`. Not part of the daily prompt.
Same rules as the daily run; same 13.09 caveat (context, never evidence). Includes the rotation
rooms not in the weekday groups, the VKA3A/B valve alarms (active 13.09) and second-tier plant points.

| area | littera | role | unit | 13.09 | sensor_id |
|---|---|---|---|---|---|
| AHU LB72:2 | `LB72_2.GT70.PV` | exhaust air temp | degC | 22.5 | `d1244acc-572b-408f-bd07-35306dd8a6b0` |
| AHU LB72:2 | `LB72_2.GT80.PV` | frost guard | degC | 19.6 | `2ac88378-f79a-4b57-93a8-5a9892110cee` |
| AHU LB72:2 | `LB72_2.GP40.PV` | supply duct pressure | Pa | 120.5 | `a945405d-acc6-4a22-a2de-8443fcfc8b9d` |
| AHU LB72:2 | `LB72_2.GP10.PV` | supply filter dp | Pa | 36.3 | `498ad4c5-8792-400a-9b01-7062670a958c` |
| AHU LB72:2 | `LB72_2.GP61.PV` | extract filter dp | Pa | 44.1 | `6bfb153b-16a8-4caf-805c-1c6fb58562fb` |
| AHU LB733 | `LB733.GT61.PV` | extract | degC | 22.4 | `9eec6aa6-085b-4bb0-9f48-3492e66585ad` |
| AHU LB733 | `LB733.GT70.PV` | exhaust | degC | 23.3 | `ca9fbb8a-cf01-45af-a3dd-ea545f53a583` |
| AHU LB733 | `LB733.GP10.PV` | supply filter dp | Pa | 42.3 | `58d7593d-90b5-493e-87a8-13da62274b97` |
| AHU LB733 | `LB733.GP61.PV` | extract filter dp | Pa | 34.9 | `a3c9d85f-e1d2-45ce-827c-84f5034dff9c` |
| AHU LB121 | `LB121.GT10.PV` | outdoor | degC | 21.2 | `22be68c4-6ac8-4194-be6a-7057a582ec31` |
| AHU LB121 | `LB121.GT40.PV` | supply | degC | 24.0 | `f8c26cfb-1b60-4555-8eaa-892b25abc63d` |
| AHU LB121 | `LB121.GT50.PV` | room | degC | 27.6 | `e2a6d2a2-722b-4852-99ab-cb12bd7796c1` |
| AHU LB121 | `LB121.GF40.PV` | supply flow | l/s | 46.6 | `a754b3b4-a121-44df-a003-690274668241` |
| AHU LB121 | `LB121.GP10.PV` | supply filter dp | Pa | 7.5 | `9eb496b8-9b49-418b-92a0-d3b8bac9a37f` |
| AHU LB121 | `LB121.UV40.SA` | supply fan VFD | % | 0.0 | `8e706ac0-150f-4810-827d-d06259aa0841` |
| AHU LB122 | `LB122.GT10.PV` | outdoor | degC | 22.3 | `3831ce9d-48b7-462d-b5ce-6ba0840ef842` |
| AHU LB122 | `LB122.GT40.PV` | supply | degC | 24.5 | `c3fdd37e-55ea-43ed-9a3c-a5539c107c29` |
| AHU LB122 | `LB122.GT50.PV` | room | degC | 23.5 | `da4039d3-e736-4cef-82ea-35c74a28f3b8` |
| AHU LB122 | `LB122.GP10.PV` | supply filter dp | Pa | 5.9 | `8a33a7dd-cb32-4979-90d6-1323fb690028` |
| AHU LB122 | `LB122.UV40.SA` | supply fan VFD | % | 0.0 | `15bee330-bbab-440f-b6c8-9a2caebe0dd4` |
| AHU LB32 | `LB32.TF1.VT` | supply fan running | 0/1 | 0.1 | `cf658780-5d05-4e2d-b4f3-82949dd122c7` |
| AHU LB33 | `LB33.GF41.PV` | supply flow TF1:2 | l/s | 2069.7 | `e11cac85-697b-4ffc-9232-c2d91257780f` |
| AHU LB33 | `LB33.TF1.VT` | supply fan running | 0/1 | 0.1 | `4b222057-cdd6-4217-a88e-f25bba59a271` |
| AHU LB52 | `LB52.GF41.PV` | supply flow TF1:2 | l/s | 3575.8 | `bd515ab3-e410-4847-9a0f-1006a725e681` |
| AHU LB52 | `LB52.TF1.VT` | supply fan running | 0/1 | 0.1 | `7c5e392e-dc8b-42bd-9d76-7ce5cc823596` |
| AHU LB13 | `LB13.GT10.PV` | outdoor | degC | 17.7 | `5c51ca86-a4b2-4d8c-8acd-ebb84ccc9012` |
| AHU LB13 | `LB13.GT50.PV` | room | degC | 23.0 | `7e32a01e-3270-424e-a9e3-27ffeaefa25a` |
| AHU LB13 | `LB13.GP40.PV` | supply pressure | Pa | 242.0 | `dbc2ea92-f7ff-4d6f-aa9c-c512812dfc09` |
| Refrigeration VKA12/KB12/FA12 | `KB12.P30A.SA` | brine pump A VFD | % | 0.0 | `8575673d-44d6-4ac3-be14-667badb3687c` |
| Refrigeration VKA12/KB12/FA12 | `KB12.P30B.SA` | brine pump B VFD | % | 85.0 | `bd874006-a164-4b20-abd9-fea88e9f5a15` |
| Refrigeration VKA12/KB12/FA12 | `VKA12.GT11.PV` | VKA12 temp 11 | degC | 26.1 | `951fe7ac-8ff6-45b7-b51d-41a5efa36af1` |
| Refrigeration VKA12/KB12/FA12 | `VKA12.GT12.PV` | VKA12 temp 12 | degC | 30.5 | `3e55cc36-dcba-418e-8f63-dac564b6705d` |
| Refrigeration VKA12/KB12/FA12 | `VKA12.P30.SA` | VKA12 pump VFD | % | 100.0 | `1776bf8c-ca0e-4d7a-8f5c-d727042b92fe` |
| Refrigeration VKA12/KB12/FA12 | `FA12.GT11.PV` | dry cooler temp in | degC | 26.1 | `90e3a0e5-bb18-44ad-9fb0-0e2620aea4aa` |
| Refrigeration VKA12/KB12/FA12 | `FA12.GT12.PV` | dry cooler temp out | degC | 37.5 | `53f3a17d-cc3b-4953-8686-77dbc09034d8` |
| Refrigeration VKA12/KB12/FA12 | `FA12.P30.SA` | dry cooler fan/pump VFD | % | 59.6 | `cab90ac1-9a82-4f20-a079-bc7d0b6d3083` |
| Refrigeration VKA12/KB12/FA12 | `FA12.KK1.HP.PV` | FA12 high pressure | bar | 14.8 | `58de7747-99d9-478d-9071-51c041b9eea2` |
| Comfort cooling VKA1-3/KB1/KM1 | `KB1.GT11.PV` | KB1 temp 11 | degC | 25.9 | `2d3f61ee-8745-4971-b121-8c96502a2191` |
| Comfort cooling VKA1-3/KB1/KM1 | `KB1.GT12.PV` | KB1 temp 12 | degC | 30.9 | `e818de54-326f-4453-9804-03e2bb2c851f` |
| Comfort cooling VKA1-3/KB1/KM1 | `KB1.SV30.SA` | KB1 valve | % | 46.4 | `9b6f4c6e-3fed-45fa-9443-e32d43fdab55` |
| Comfort cooling VKA1-3/KB1/KM1 | `KB1.GP11.PL3.PV` | KB1 pressure plan 3 | kPa | 72.8 | `ffae7f47-3927-4999-8f36-979136daddc8` |
| Comfort cooling VKA1-3/KB1/KM1 | `VKA3A.GP11.PV` | VKA3A condenser pressure | bar | 0.0 | `fadfac8e-2614-4700-98e7-e8d8f4016f7b` |
| Comfort cooling VKA1-3/KB1/KM1 | `VKA3B.GP11.PV` | VKA3B condenser pressure | bar | 0.0 | `6196367b-b1b7-480d-bfb5-466d9e0a81ae` |
| Comfort cooling VKA1-3/KB1/KM1 | `VKA3A.SV31.LA` | VKA3A SV31 valve wrong position | alarm | 1.0 | `6aa6a690-c477-42c8-938a-9dfaf451cf15` |
| Comfort cooling VKA1-3/KB1/KM1 | `VKA3A.SV32.LA` | VKA3A SV32 valve wrong position | alarm | 1.0 | `e93c2239-30e4-4de9-80e5-13a1a158a4cc` |
| Comfort cooling VKA1-3/KB1/KM1 | `VKA3B.SV31.LA` | VKA3B SV31 valve wrong position | alarm | 1.0 | `94f7cab4-dd00-4a96-ba1f-629c36b73f50` |
| Comfort cooling VKA1-3/KB1/KM1 | `VKA3B.SV32.LA` | VKA3B SV32 valve wrong position | alarm | 1.0 | `eeb7a366-a2b5-4e40-961d-7ed4704e9cc9` |
| Comfort cooling VKA1-3/KB1/KM1 | `KM1.GT13.PV` | KM1 temp | degC | 22.7 | `d1717f47-d5a5-4d01-ab03-b61186f801dd` |
| Comfort cooling VKA1-3/KB1/KM1 | `KM1.UV30A.SA` | KM1 pump A VFD | % | 0.0 | `eedea5dd-f529-4f37-b87c-ff9b64e64506` |
| Comfort cooling VKA1-3/KB1/KM1 | `KB102.DAGG.PV` | KB102 dew point | degC | 12.4 | `38977b1f-94b4-401b-8fc3-92e76508e71a` |
| Comfort cooling VKA1-3/KB1/KM1 | `KB102.GT51.PV` | KB102 room temp | degC | 23.2 | `fb1576c2-95c1-4eb3-b3c4-8cbb3b63ffc0` |
| District heating VP1 / heating VS1 | `VP1.GT41.PV` | DH temp 41 | degC | 26.0 | `f8ac8437-9af7-4d8f-ae15-35cfb7fa96d9` |
| District heating VP1 / heating VS1 | `VP1.GT42.PV` | DH temp 42 | degC | 24.0 | `96eb85c6-6caa-452d-bb66-1594f0928ad5` |
| Shops (Elsys ERS2) | `tvoc_A81758FFFE0C5675` | shop TVOC BUTIK K2137 (PLAN 1) | ug/m3 | 121 | `bc2dba5f-c821-4679-ba41-1d70cdc6c16d` |
| Shops (Elsys ERS2) | `temperature_A81758FFFE0D24A0` | shop temp BUTIK K2108 (PLAN 1) | degC | 22.3 | `a0f85e18-325c-4181-8331-b8a63d59a766` |
| Shops (Elsys ERS2) | `temperature_A81758FFFE0C5676` | shop temp BUTIK K2164 (PLAN 1) | degC | 22.5 | `b98b9a7a-2c22-4141-adb2-0d1ef1f867e6` |
| Shops (Elsys ERS2) | `tvoc_A81758FFFE0C5676` | shop TVOC BUTIK K2164 (PLAN 1) | ug/m3 | 73 | `b77afe6b-c7b4-463c-8b72-b87beb8a0c39` |
| Shops (Elsys ERS2) | `temperature_A81758FFFE0D24A1` | shop temp BUTIK K2148 (PLAN 1) | degC | 22.7 | `2c331cf6-9ee5-43f1-bb5d-1cb7b3ceeb68` |
| Shops (Elsys ERS2) | `temperature_A81758FFFE0C5674` | shop temp ENTREHALL 61 (PLAN 3) | degC | 21.3 | `539562d6-1a9e-4930-8e7c-18d1f8e7c5d0` |
| Shops (Elsys ERS2) | `tvoc_A81758FFFE0C5674` | shop TVOC ENTREHALL 61 (PLAN 3) | ug/m3 | 148 | `f3d45b83-3fe7-41fc-9923-13cb76f6be76` |
| Shops (Elsys ERS2) | `temperature_A81758FFFE0C5673` | shop temp BUTIK 0004 (PLAN 3) | degC | 21.5 | `90ceacff-4da5-465f-a766-59dd1397be93` |
| Shops (Elsys ERS2) | `tvoc_A81758FFFE0C5673` | shop TVOC BUTIK 0004 (PLAN 3) | ug/m3 | 29 | `1dc48b08-13dd-40bd-af53-89d6c817acff` |
| Shops (Elsys ERS2) | `temperature_A81758FFFE0D249E` | shop temp BUTIK 0075 (PLAN 3) | degC | 25.1 | `b30b1414-40c0-4936-89af-d967ebfe9f61` |
| Shops (Elsys ERS2) | `tvoc_A81758FFFE0C566F` | shop TVOC BUTIK 1014 (PLAN 4) | ug/m3 | 39 | `a20c0368-c9da-4b6a-b0f1-3344eda99b0d` |
| Shops (Elsys ERS2) | `tvoc_A81758FFFE0C5671` | shop TVOC BUTIK 1067 (PLAN 4) | ug/m3 | 74 | `fa9a2f3d-53fb-4d09-a59f-fde4bd1efbb3` |
| Shops (Elsys ERS2) | `temperature_A81758FFFE0D249F` | shop temp BUTIK 1081 (PLAN 4) | degC | 20.6 | `587e0423-2169-41c6-8e85-964782aa720e` |
| Shops (Elsys ERS2) | `temperature_A81758FFFE0D249D` | shop temp BUTIK 1093 (PLAN 4) | degC | 21.5 | `2fc8f6c4-d985-437d-a09b-46b4058f2661` |
| Shops (Elsys ERS2) | `temperature_A81758FFFE0C566E` | shop temp BUTIK 1082 (PLAN 4) | degC | 20.2 | `5d421574-0af8-43fb-9d8d-64b8adc85ef5` |
| Shops (Elsys ERS2) | `tvoc_A81758FFFE0C566E` | shop TVOC BUTIK 1082 (PLAN 4) | ug/m3 | 26 | `1d3df84c-71c1-4623-b153-e1c1d9a29451` |
| Shops (Elsys ERS2) | `tvoc_A81758FFFE0C564B` | shop TVOC BUTIK 2002 (PLAN 5) | ug/m3 | 40 | `2302a13c-772d-4296-a1a8-41cc4ac3650f` |
| Shops (Elsys ERS2) | `temperature_A81758FFFE0C566C` | shop temp BUTIK 2041 (PLAN 5) | degC | 20.9 | `c66e6a3e-715b-4237-b9a2-200a5f95c336` |
| Shops (Elsys ERS2) | `tvoc_A81758FFFE0C566C` | shop TVOC BUTIK 2041 (PLAN 5) | ug/m3 | 72 | `add146af-de77-4a05-b6bb-90fd081e22ae` |
| Shops (Elsys ERS2) | `temperature_A81758FFFE0B3062` | shop temp BUTIK 2074 (PLAN 5) | degC | 22.5 | `e100c4a8-e4c8-4e6a-b0e0-78eb989d8849` |
| Shops (Elsys ERS2) | `temperature_A81758FFFE0C564C` | shop temp BUTIK 2093 (PLAN 5) | degC | 20.3 | `cdd66e09-d5d8-4da4-92ef-dc3d5e680a51` |
| Shops (Elsys ERS2) | `tvoc_A81758FFFE0C564C` | shop TVOC BUTIK 2093 (PLAN 5) | ug/m3 | 51 | `b7f865a5-00cd-423b-b048-8e91aabd0fd8` |
| Shops (Elsys ERS2) | `temperature_A81758FFFE0C566D` | shop temp BUTIK 2025 (PLAN 5) | degC | 20.7 | `92cfd5cd-873a-4fe4-b6e1-1f975e292020` |
| Shops (Elsys ERS2) | `tvoc_A81758FFFE0C566D` | shop TVOC BUTIK 2025 (PLAN 5) | ug/m3 | 60 | `1cdce523-58f1-409c-8154-fa956f72cfe5` |
| Shops (Elsys ERS2) | `temperature_A81758FFFE0B3063` | shop temp BUTIK 2089 (PLAN 5) | degC | 21.3 | `208e657d-b271-48f9-bad2-be991c10c3be` |
| Shops (Elsys ERS2) | `temperature_A81758FFFE0C566B` | shop temp BUTIK 2069 (PLAN 5) | degC | 20.3 | `798dcc93-7a5c-4ed7-8854-6a308136f38d` |
| Shops (Elsys ERS2) | `tvoc_A81758FFFE0C566B` | shop TVOC BUTIK 2069 (PLAN 5) | ug/m3 | 55 | `0b794e85-b7c3-409b-92da-a3eef55c9764` |
| Shops (Elsys ERS2) | `temperature_A81758FFFE0B3061` | shop temp BUTIK 2081 (PLAN 5) | degC | 21.5 | `a6053213-b613-47f7-b688-288bb961e88b` |
| Shops (Elsys ERS2) | `tvoc_A81758FFFE0C5648` | shop TVOC BUTIK 3094 (PLAN 6) | ug/m3 | 57 | `45bbf2b7-b7a5-4aba-aed5-96a122b490f3` |
| Shops (Elsys ERS2) | `temperature_A81758FFFE0C5649` | shop temp BUTIK 3118 (PLAN 6) | degC | 22.6 | `59912e0d-d9f8-459e-bf52-56d79f2106b9` |
| Shops (Elsys ERS2) | `tvoc_A81758FFFE0C5649` | shop TVOC BUTIK 3118 (PLAN 6) | ug/m3 | 63 | `52bb8150-fc1e-4678-8588-25428e4a423f` |
| Shops (Elsys ERS2) | `tvoc_A81758FFFE0C5646` | shop TVOC MATSAL 4129 (PLAN 7) | ug/m3 | 23 | `09ef2436-ea0c-4aac-9210-6e97bb00b112` |
| Shops (Elsys ERS2) | `temperature_A81758FFFE0C5645` | shop temp MATSAL 4123 (PLAN 7) | degC | 22.1 | `76fd68b8-98b5-475a-8686-ff37ec40f811` |
| Shops (Elsys ERS2) | `tvoc_A81758FFFE0C5645` | shop TVOC MATSAL 4123 (PLAN 7) | ug/m3 | 76 | `ddbc59fe-0017-4589-8af7-fc8616778c58` |
| Shops (Elsys ERS2) | `temperature_A81758FFFE0C5643` | shop temp BUTIK 4176 (PLAN 7) | degC | 22.2 | `d2c33b8f-8874-4be5-866c-a611d8b79e63` |
| Shops (Elsys ERS2) | `tvoc_A81758FFFE0C5643` | shop TVOC BUTIK 4176 (PLAN 7) | ug/m3 | 53 | `d51d5273-b425-46d7-a67d-41206468c0fc` |
| Shops (Elsys ERS2) | `temperature_A81758FFFE0C51C7` | shop temp BUTIK 4028 (PLAN 7) | degC | 22.8 | `c3dc54b4-316f-4787-a2cf-81dc32c1fa55` |
| Shops (Elsys ERS2) | `tvoc_A81758FFFE0C51C7` | shop TVOC BUTIK 4028 (PLAN 7) | ug/m3 | 51 | `9129f388-b0ca-4b16-9fab-06dc8c1cf539` |
| Shops (Elsys ERS2) | `temperature_A81758FFFE0C5644` | shop temp VINBAR 4045 (PLAN 7) | degC | 21.2 | `605a4801-3e57-4edc-8b21-65da68fad95e` |
| Shops (Elsys ERS2) | `tvoc_A81758FFFE0C5644` | shop TVOC VINBAR 4045 (PLAN 7) | ug/m3 | 48 | `e66d21ae-e90d-411c-902b-92e886c0700d` |
| Offices (Lindinvent) PLAN 8 | `LB82-5182-VFD102/9070` | room temp — PAUSYTA 5182 [LB82-5182-VFD102] | degC | 23.0 | `acce1021-53d3-4632-bd34-253616a5e42b` |
| Offices (Lindinvent) PLAN 8 | `LB82-5182-VFD102/8006` | room temp setpoint — PAUSYTA 5182 [LB82-5182-VFD102] | degC | 22.0 | `adb38cf2-502f-4dd7-b29a-6f7b7dc16b97` |
| Offices (Lindinvent) PLAN 8 | `LB82-5182-VFD102/9090` | CO2 — PAUSYTA 5182 [LB82-5182-VFD102] | ppm | 456.0 | `e229304a-9707-4e7d-8f5b-935b3df1c4ae` |
| Offices (Lindinvent) PLAN 8 | `LB82-5182-VFD102/4152` | presence — PAUSYTA 5182 [LB82-5182-VFD102] | 0/1 | 0.0 | `6faf2ec1-5eae-4b99-bdda-934b5945bfcd` |
| Offices (Lindinvent) PLAN 8 | `LB82-5182-VFD102/-12` | supply flow — PAUSYTA 5182 [LB82-5182-VFD102] | l/s | 1.0 | `c667ec5a-8d51-4262-b56f-6a830c7e97bb` |
| Offices (Lindinvent) PLAN 8 | `LB81-5152A-VFD104/9070` | room temp — ÖPPET KONTOR 5152 [LB81-5152A-VFD104] | degC | 21.8 | `ac9587dc-b06a-4419-aeb0-b3cac5b22028` |
| Offices (Lindinvent) PLAN 8 | `LB81-5152A-VFD104/8006` | room temp setpoint — ÖPPET KONTOR 5152 [LB81-5152A-VFD104] | degC | 22.0 | `a2da8a37-b902-4989-8a0c-cf46ad469fb3` |
| Offices (Lindinvent) PLAN 8 | `LB81-5152A-VFD104/9090` | CO2 — ÖPPET KONTOR 5152 [LB81-5152A-VFD104] | ppm | 445.0 | `2c189d6e-97b8-450e-8e6c-af0903228d6c` |
| Offices (Lindinvent) PLAN 8 | `LB81-5152A-VFD104/4152` | presence — ÖPPET KONTOR 5152 [LB81-5152A-VFD104] | 0/1 | 0.0 | `348c871f-6f55-4f0b-88df-ea8474a96ed3` |
| Offices (Lindinvent) PLAN 8 | `LB81-5152A-VFD104/-12` | supply flow — ÖPPET KONTOR 5152 [LB81-5152A-VFD104] | l/s | 0.0 | `36468fb4-80a1-4af6-9a47-5e2978549167` |
| Offices (Lindinvent) PLAN 8 | `LB82-5181-VFD101/9070` | room temp — ÖPPET KONTOR 5181 [LB82-5181-VFD101] | degC | 22.5 | `bc62516c-b3eb-41a6-8742-fd72b52236c8` |
| Offices (Lindinvent) PLAN 8 | `LB82-5181-VFD101/8006` | room temp setpoint — ÖPPET KONTOR 5181 [LB82-5181-VFD101] | degC | 22.0 | `491f5666-654f-4e96-bf2f-d8e78ba407d8` |
| Offices (Lindinvent) PLAN 8 | `LB82-5181-VFD101/9090` | CO2 — ÖPPET KONTOR 5181 [LB82-5181-VFD101] | ppm | 485.0 | `52bf0a08-52db-4ca4-8aee-42f30fb7c237` |
| Offices (Lindinvent) PLAN 8 | `LB82-5181-VFD101/4152` | presence — ÖPPET KONTOR 5181 [LB82-5181-VFD101] | 0/1 | 0.0 | `06161ecf-9dc9-4364-90f8-cfbe5d8a70bc` |
| Offices (Lindinvent) PLAN 8 | `LB82-5181-VFD101/-12` | supply flow — ÖPPET KONTOR 5181 [LB82-5181-VFD101] | l/s | 1.0 | `c47e38a0-2ab1-4039-b5cd-c78caec2a0f3` |
| Offices (Lindinvent) PLAN 9 | `LB91-6182-VFD102/9070` | room temp — MÖTE 6182 [LB91-6182-VFD102] | degC | 22.1 | `0ae7be67-3643-4017-8235-616d0ceb1747` |
| Offices (Lindinvent) PLAN 9 | `LB91-6182-VFD102/8006` | room temp setpoint — MÖTE 6182 [LB91-6182-VFD102] | degC | 21.0 | `77d8cdb5-7037-41b4-a303-955a9c07f28a` |
| Offices (Lindinvent) PLAN 9 | `LB91-6182-VFD102/9090` | CO2 — MÖTE 6182 [LB91-6182-VFD102] | ppm | 529.0 | `c71b1415-745c-4a07-ae04-7c74eeee79c8` |
| Offices (Lindinvent) PLAN 9 | `LB91-6182-VFD102/4152` | presence — MÖTE 6182 [LB91-6182-VFD102] | 0/1 | 0.0 | `e2d0b796-18f7-4f67-a2ea-7f78fa9d0bb5` |
| Offices (Lindinvent) PLAN 9 | `LB91-6182-VFD102/-12` | supply flow — MÖTE 6182 [LB91-6182-VFD102] | l/s | 126.0 | `830c8326-dad8-4308-a0af-796577164306` |
| Offices (Lindinvent) PLAN 9 | `LB91-6182-VFD101/9070` | room temp — MÖTE 6182 [LB91-6182-VFD101] | degC | 22.1 | `6f5b6624-7580-410a-991b-bad2ce85f82e` |
| Offices (Lindinvent) PLAN 9 | `LB91-6182-VFD101/8006` | room temp setpoint — MÖTE 6182 [LB91-6182-VFD101] | degC | 21.0 | `d174dbc6-71bd-4cb8-b150-83674525356b` |
| Offices (Lindinvent) PLAN 9 | `LB91-6182-VFD101/9090` | CO2 — MÖTE 6182 [LB91-6182-VFD101] | ppm | 529.0 | `6e35d20e-44a5-4fba-8556-9013173358e8` |
| Offices (Lindinvent) PLAN 9 | `LB91-6182-VFD101/4152` | presence — MÖTE 6182 [LB91-6182-VFD101] | 0/1 | 0.0 | `cbeac6f4-daa5-4ff7-8eed-f9ff60f3728c` |
| Offices (Lindinvent) PLAN 9 | `LB91-6182-VFD101/-12` | supply flow — MÖTE 6182 [LB91-6182-VFD101] | l/s | 63.0 | `35e30fa3-6d3d-4f48-95c0-0ab24d9b42c1` |
| Offices (Lindinvent) PLAN 10 | `LB104-7027-TB15B4/9070` | room temp — KOPIERING/FRD. 7027 [LB104-7027-TB15B4] | degC | 22.8 | `4322009d-15fd-4c75-9ed4-015d954b5c76` |
| Offices (Lindinvent) PLAN 10 | `LB104-7027-TB15B4/8006` | room temp setpoint — KOPIERING/FRD. 7027 [LB104-7027-TB15B4] | degC | 22.0 | `ac9ed475-c345-46ab-816f-a1c71060be24` |
| Offices (Lindinvent) PLAN 10 | `LB104-7027-TB15B4/9090` | CO2 — KOPIERING/FRD. 7027 [LB104-7027-TB15B4] | ppm | 486.0 | `9d5c3809-6db0-4d6f-9e2c-aa85fa72fdec` |
| Offices (Lindinvent) PLAN 10 | `LB104-7027-TB15B4/4152` | presence — KOPIERING/FRD. 7027 [LB104-7027-TB15B4] | 0/1 | 0.0 | `143d3c2a-804f-4b42-b7ac-db1de59bfac3` |
| Offices (Lindinvent) PLAN 10 | `LB104-7027-TB15B4/-12` | supply flow — KOPIERING/FRD. 7027 [LB104-7027-TB15B4] | l/s | 0.0 | `19bcebcb-0943-422e-a5be-b9a886f8bdcf` |
| Offices (Lindinvent) PLAN 10 | `LB104-7008-TB15B1/9070` | room temp — GRUPPRUM 7008 [LB104-7008-TB15B1] | degC | 22.6 | `976fca31-2f51-4aeb-9cba-41d84db91a7d` |
| Offices (Lindinvent) PLAN 10 | `LB104-7008-TB15B1/8006` | room temp setpoint — GRUPPRUM 7008 [LB104-7008-TB15B1] | degC | 22.0 | `f9d09fd7-7a5f-4a1e-a64e-770d4380a968` |
| Offices (Lindinvent) PLAN 10 | `LB104-7008-TB15B1/9090` | CO2 — GRUPPRUM 7008 [LB104-7008-TB15B1] | ppm | 441.0 | `d62888d0-b57c-4b14-b733-b8db1592b44c` |
| Offices (Lindinvent) PLAN 10 | `LB104-7008-TB15B1/4152` | presence — GRUPPRUM 7008 [LB104-7008-TB15B1] | 0/1 | 0.0 | `c2e5dbd0-ea9c-4522-9e4a-bef1e5240c58` |
| Offices (Lindinvent) PLAN 10 | `LB104-7008-TB15B1/-12` | supply flow — GRUPPRUM 7008 [LB104-7008-TB15B1] | l/s | 0.0 | `0761c430-ef74-401c-81c9-d0686a245b70` |
| Alarm roster | `LB72_2.FF1.LA` | LB72:2-FF1 Driftfel | alarm | 0.0 | `828915a1-f8ec-4720-aa18-c8a22cc46333` |
| Alarm roster | `LB72_2.VERK.LA` | LB72:2-VVX Låg verkningsgrad | alarm | 0.0 | `03d402f5-36e7-44d8-acc0-668f2158515f` |
| Alarm roster | `LB733.FF01.LA` | Driftfel | alarm | 0.0 | `ca7d5ce6-ba8f-487a-824c-3549facf6a87` |
| Alarm roster | `LB733.CGS90.SLA` | ummalarm | alarm | 0.0 | `9dae5b3e-4ef4-4c3c-ba9f-42fbbcecc75b` |
| Alarm roster | `LB121.UV40.LA` | LB12:1-UV40 Summalarm | alarm | 0.0 | `c767a559-da68-4519-a30d-3d795469a6ae` |
| Alarm roster | `LB122.UV40.LA` | LB12:2-UV40 Summalarm | alarm | 0.0 | `ce1c7985-212a-4de1-97ac-c9f75f22f51c` |
| Alarm roster | `KB12.P30A.SLA` | KB12-P30A Summalarm | alarm | 0.0 | `2d57e444-0aa8-4458-b865-6cf5f4300dc6` |
| Alarm roster | `KB12.P30B.SLA` | KB12-P30B Summalarm | alarm | 0.0 | `28d286cc-857a-4568-8301-dd1bed3db642` |
| Alarm roster | `KM1.KEM.SLA` | Summalarm Kemanläggning | alarm | 0.0 | `3ddad857-4fa9-453a-9184-0544b82fc266` |
| Alarm roster | `VS1.P90.SLA` | VS1-P90 Summalarm | alarm | 0.0 | `9e9b2089-2673-4939-a14e-44ac44ecfc2f` |
| Alarm roster | `VKA1.SEK.LA` | Regl. handstyrd | alarm | 0.0 | `4da1d2cd-869b-4fb6-ac4a-7fd0d9395b31` |
| Alarm roster | `VKA2.SEK.LA` | Regl. handstyrd | alarm | 0.0 | `eb89e568-fba2-4148-987a-c52ff50b1b61` |
| Alarm roster | `VKA3.UV32.SLA` | Summalarm omformare | alarm | 0.0 | `6b289049-18d3-459a-a126-52587ed39fe3` |
| Alarm roster | `AS65.MSK.LA` | Utlöst motorsk./dvärgbr. i AS | alarm | 0.0 | `00fd68f0-b226-4492-92e1-2d50ad74fe35` |
| Alarm roster | `LB13.TF1.LA` | m | alarm | 0.0 | `0c56c863-efb1-4082-b820-71c3c9c32708` |
| Alarm roster | `LB13.GT80.LA` | m | alarm | 0.0 | `4808184c-9f19-4fdc-93bc-e2fa16a19bdc` |
| Rotation PLAN 8 | `LB81-5151B-TD401/9070` | room temp — ÖPPET KONTOR 5151 | degC | 22.7 | `b9e254b3-48eb-4ada-9c77-eb5994ddba0e` |
| Rotation PLAN 8 | `LB81-5151B-TD401/8006` | setpoint — ÖPPET KONTOR 5151 | degC | 22.0 | `d2db8415-efb0-4163-a852-f53281801ebf` |
| Rotation PLAN 8 | `LB81-5151F-HD101/9070` | room temp — ÖPPET KONTOR 5151 | degC | 22.5 | `d74af3bd-db27-4177-8ea5-f8c00cb6a286` |
| Rotation PLAN 8 | `LB81-5151F-HD101/8006` | setpoint — ÖPPET KONTOR 5151 | degC | 22.0 | `95392c1d-8908-477b-a195-ff444ff40767` |
| Rotation PLAN 9 | `LB91-6191-HD107/9070` | room temp — KONTOR 6191 | degC | 21.4 | `f4cbc71f-33dd-4551-abfa-094beb22bc43` |
| Rotation PLAN 9 | `LB91-6191-HD107/8006` | setpoint — KONTOR 6191 | degC | 22.5 | `7d78393f-91e8-472d-abfe-03551ae6786f` |
| Rotation PLAN 10 | `LB104-7027-TB15B1/9070` | room temp — KOPIERING/FRD. 7027 | degC | 22.8 | `9485d02d-c4c2-44c7-9927-805480324760` |
| Rotation PLAN 10 | `LB104-7027-TB15B1/8006` | setpoint — KOPIERING/FRD. 7027 | degC | 22.0 | `3fda14f0-8a7e-4c77-bd75-d2aabc6e9aa2` |
| Rotation PLAN 8 | `LB81-5152C-VFD101/9070` | room temp — ÖPPET KONTOR 5152 | degC | 21.3 | `77b3e914-d93f-42c1-9229-5ef17ae3ab8b` |
| Rotation PLAN 8 | `LB81-5152C-VFD101/8006` | setpoint — ÖPPET KONTOR 5152 | degC | 22.5 | `2c13ac55-c7d9-4adc-b345-3c29cefc79d1` |
| Rotation PLAN 9 | `LB91-6195-TD402/9070` | room temp — MÖTE 6195 | degC | 22.4 | `7299b3ee-1408-4832-b676-b391062b4ce0` |
| Rotation PLAN 9 | `LB91-6195-TD402/8006` | setpoint — MÖTE 6195 | degC | 22.0 | `cb62cbcd-9712-404d-8811-017825b3967b` |
| Rotation PLAN 10 | `LB104-7027-TB15A6/9070` | room temp — KOPIERING/FRD. 7027 | degC | 23.0 | `a6b8fde8-4b5d-4b34-897b-920c89daedeb` |
| Rotation PLAN 10 | `LB104-7027-TB15A6/8006` | setpoint — KOPIERING/FRD. 7027 | degC | 22.0 | `2fde45a8-0969-4a84-be07-018f49492de8` |
| Rotation PLAN 8 | `LB81-5152C-VFD102/9070` | room temp — ÖPPET KONTOR 5152 | degC | 21.3 | `720da3d5-9231-420e-b4a3-e3d8e22bfc6b` |
| Rotation PLAN 8 | `LB81-5152C-VFD102/8006` | setpoint — ÖPPET KONTOR 5152 | degC | 22.5 | `084da736-f1ee-48f8-9f52-e34a50b43a0e` |
| Rotation PLAN 8 | `LB81-5150-HD102/9070` | room temp — KONFERENS 5150 | degC | 22.6 | `1ee49a26-0b90-40da-87a5-9757cd260e65` |
| Rotation PLAN 8 | `LB81-5150-HD102/8006` | setpoint — KONFERENS 5150 | degC | 22.0 | `5587459c-0e52-4c5c-9522-b0741ee81e12` |
| Rotation PLAN 9 | `LB91-6189-TD401/9070` | room temp — KOP/PRINT 6189 | degC | 20.9 | `a6cd982b-81a1-40a4-b250-f74da6903748` |
| Rotation PLAN 9 | `LB91-6189-TD401/8006` | setpoint — KOP/PRINT 6189 | degC | 22.5 | `66090e09-c919-4d5d-865c-4eb9a4de9eac` |
| Rotation PLAN 10 | `LB104-7007-TB15B1/9070` | room temp — KONTOR 7007 | degC | 22.6 | `8fe32257-42f7-42be-bbf0-6c557078b6c2` |
| Rotation PLAN 10 | `LB104-7007-TB15B1/8006` | setpoint — KONTOR 7007 | degC | 22.0 | `6c4c61d5-6f63-4e3d-97a8-8b4abc881c72` |
| Rotation PLAN 9 | `LB91-6194-TD401/9070` | room temp — MÖTE 6194 | degC | 21.4 | `7a3919cf-66e1-46a6-a14f-01ce33db196b` |
| Rotation PLAN 9 | `LB91-6194-TD401/8006` | setpoint — MÖTE 6194 | degC | 21.0 | `dbe7bf4a-eb4b-4124-ade6-18739593752d` |
| Rotation PLAN 8 | `LB82-5164-VFD101/9070` | room temp — TELE 5164 | degC | 23.3 | `6a166b5c-7c5c-47cf-a754-9a931033176c` |
| Rotation PLAN 8 | `LB82-5164-VFD101/8006` | setpoint — TELE 5164 | degC | 19.0 | `78628ae5-b2c3-4530-a9a7-9d83ebddb7a4` |
| Rotation PLAN 9 | `LB91-6196-TD401/9070` | room temp — MÖTE 6196 | degC | 21.7 | `caa14b35-ec01-44ca-9c4d-f88469d5f9dc` |
| Rotation PLAN 9 | `LB91-6196-TD401/8006` | setpoint — MÖTE 6196 | degC | 22.0 | `c712c234-528e-4dc9-8b26-d0b629df4f31` |
| Rotation PLAN 10 | `LB104-7012-TB15B4/9070` | room temp — KONTOR 7012 | degC | 22.1 | `d53ce5b9-181d-49ee-844a-d8eb640665ee` |
| Rotation PLAN 10 | `LB104-7012-TB15B4/8006` | setpoint — KONTOR 7012 | degC | 22.0 | `d857e7f0-ea3c-48c8-b624-445038c6cccd` |
| Rotation PLAN 9 | `LB91-6195-HD101/9070` | room temp — MÖTE 6195 | degC | 21.4 | `b0acc096-c3c9-47a9-86e9-5072b36e416d` |
| Rotation PLAN 9 | `LB91-6195-HD101/8006` | setpoint — MÖTE 6195 | degC | 22.5 | `74f1755a-e72b-49a0-a2f0-8662a0c87d14` |
| Rotation PLAN 8 | `LB82-5181-VFD108/9070` | room temp — ÖPPET KONTOR 5181 | degC | 22.0 | `0afc1e9f-085e-4797-83a8-5f09f2328fb6` |
| Rotation PLAN 8 | `LB82-5181-VFD108/8006` | setpoint — ÖPPET KONTOR 5181 | degC | 22.0 | `89efa410-f6c2-4968-839d-af3f19d1e97d` |
| Rotation PLAN 8 | `LB83-5192-VFD105/9070` | room temp — ÖPPET KONTOR 5192 | degC | 21.9 | `b8f58d80-db01-4f7e-8db0-9928175af244` |
| Rotation PLAN 8 | `LB83-5192-VFD105/8006` | setpoint — ÖPPET KONTOR 5192 | degC | 23.0 | `6e679e98-a444-496e-9e85-cc21d9487677` |
| Rotation PLAN 9 | `LB91-6195-TD403/9070` | room temp — MÖTE 6195 | degC | 22.4 | `f0dd6e2e-4abc-464c-9880-199f5eeeb45d` |
| Rotation PLAN 9 | `LB91-6195-TD403/8006` | setpoint — MÖTE 6195 | degC | 22.0 | `007763c9-0421-4ffe-b4fb-d3a77564e5e5` |
| Rotation PLAN 8 | `LB83-5192-HD102/9070` | room temp — ÖPPET KONTOR 5192 | degC | 22.6 | `06d14e43-cfeb-48cd-93c9-f152de81f3d3` |
| Rotation PLAN 8 | `LB83-5192-HD102/8006` | setpoint — ÖPPET KONTOR 5192 | degC | 23.0 | `da5e02e1-1a34-4bcf-b3f7-af40ba5c2572` |

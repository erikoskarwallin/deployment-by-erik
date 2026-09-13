# NK Huset — what the building can actually sense (measured 13.09.2026)

Probe: REST census of every twin under building `55885296-a5af-49f6-88f2-d31c5f819e63`
(Hufvudstaden AB, PO `51fae0e3-a66d-41fa-be6c-1f416abb1f2e`), 13.09.2026 13:00–13:40 UTC, plus a
7-day raw history pull on 30 offices, all live Saia points and the outdoor probes. Files:
`nk-huset-sensor-census-2026-09-13.csv` (all 4,080 sensors) and `nk-huset-embodied-roster.csv`.
**This file is the authority wherever the agent spec or the onboarding handover disagrees with it.**

## The building in numbers

| | |
|---|---|
| Storeys | 12 — `PLAN 1..12`. Hufvudstaden's own meter names give the key: PLAN 1 = uk, PLAN 2 = k, **PLAN 3 = bv (ground)**, PLAN 4 = 1tr … PLAN 8 = 5tr, PLAN 10 = 7tr. (The handover's "PLAN 4 = ground" is wrong.) |
| Use | PLAN 1–7 department store + Saluhall (food hall) · PLAN 8–10 offices (Hufvudstaden HQ, VISA, law firms…) |
| Rooms | 2,330 |
| Devices / sensors / actuators | 5,798 / 4,080 / 373 — **0 actuators writable** (S-Bus writes NAK, PLAT-5364) |
| Floor area | **unknown — `areaQuantities` empty on building and real estate.** No kWh/m² until Hufvudstaden supplies it. |

## Five data families, and how alive each one is

| family | sensors | live < 26 h | cadence | history from | what it is |
|---|---:|---:|---|---|---|
| **Lindinvent** (Lindispect) | 2,174 | **2,163 (99.5 %)** | ~15 min | 03.06.2026 | office room controllers PLAN 8/9/10 (+5 on PLAN 6) |
| **Saia S-Bus PLC** (Citect world) | 943 | **912 (96.7 %)** | ~10 min | 28.07.2026 | AHUs, cooling, refrigeration, district heating PLC, 18 lifts, fire/UPS/standby power, ~290 alarm tags |
| **LB13 + Modbus + misc** ("other" live) | 575 | 173 | 10 min | 28.07.2026 | the LB13 SCADA-pilot AHU (83 points), 3 Modbus elevator devices, 1 Milesight CT305 clamp |
| **LoRa** | 265 | 143 | 10–60 min | 22.04.2026 | 24 Elsys ERS2 VOC + 10 ERS2 humidity in the shops; the rest is dead |
| **Mestro energy import** | 123 (+~110 water meters filed under "other") | **0 live — all 4.0–4.4 days old** | hourly buckets | years | main + sub meters, see below |

Dead and should be listed once, not daily: TBA11/TBA13 presence+temperature (94, dead since late June),
GT/OS and GX temperature/humidity (34), Milesight WT201 thermostats (31 devices), ERS2CO2 (28, never),
EMU energy (13), QW1 water (2). **~260 sensors > 30 days silent.** 31 Saia points never reported;
9 Lindinvent (one whole controller `LB82-5181-VFD102` plus a Nod61267 presence/lux pair).

⚠️ **The first census pass said Saia was 14 % live and Lindinvent 91 %.** That was 1,317 HTTP 429s
(rate limiting at 24 threads) counted as "never observed". At 6 threads with back-off the numbers above
are the truth. Never publish a liveness figure from a script that does not check status codes.

## What each family gives the agent

### Offices (Lindinvent, PLAN 8–10) — the richest, and fully live
334 rooms with temperature + setpoint · 283 presence (+198 "local" presence) · 268 damper openings ·
204 supply flows (+71 local) · 157 CO2 + CO2 setpoint · 16 extract flows · 14 lux · 13 duct pressures
with setpoints. 122 controllers carry the full set (temp, setpoint, CO2, presence, flow, opening);
108 of those sit in a named room. PLAN 8 (5tr) has 198 rooms, PLAN 9 74, PLAN 10 56.
The 31 "Utetemperatur" points all read the same value (16.9 °C at 13:xx) — **one outdoor
temperature distributed to 31 nodes, not 31 probes.**

**7-day shape (30 rooms, 06–13.09):**
```
                 00   03   06   07   08   09   10   12   14   16   17   18   19   21
presence  WD    0.0  0.0  0.1  0.2  0.4  0.6  0.7  0.6  0.7  0.6  0.4  0.2  0.1  0.0
flow l/s  WD    0.6  9.5 10.1 11.7 13.8 16.2 16.9 17.2 17.4 17.3 13.6  7.0  4.7  3.2
flow l/s  WE    0.6  0.7  0.5  0.6  0.6  0.6  0.7  0.6  1.3  0.6  0.6  0.6  0.6  0.6
opening % WD   15.5 40.3 38.8 34.2 35.2 41.1 43.0 44.7 44.3 43.9 45.1 38.4 31.1 21.7
room degC WD   22.5 22.0 21.8 21.9 22.1 22.4 22.4 22.5 22.5 22.5 22.5 22.5 22.6 22.6
CO2 ppm   WD    503  481  457  460  481  570  623  660  651  645  586  552  553  527
```
- Ventilation tracks occupancy well: night and weekend flow 0.6 l/s (= minimum), weekday plateau
  08–17. Weekend flow is flat all day — the setback works.
- **Weekday start at 03:00, four hours before anyone arrives**, dampers 15 → 40 %, rooms cooled
  22.5 → 21.8 by 04:00. Not on weekends. This is the `HA19.LB104.NK Nattkyla -3 grader` night-cooling
  sequence, plausibly by design in a September heat spell — **MAY BE BY DESIGN, ask Stefan** before
  anyone calls it waste.
- Comfort at 13.09 13:xx: 333 room temps 19.7–24.0 °C, none > 25, one < 20; CO2 max 529 ppm.

### Department store (PLAN 1–7)
- **Elsys ERS2 VOC in the shops: 29 live temperatures** (PLAN 1: 4, PLAN 3: 4, PLAN 4: 5, PLAN 5: 9,
  PLAN 6: 2, PLAN 7: 5 incl. MATSAL/VINBAR) with humidity, TVOC, presence, lux, battery. 20.2–25.1 °C
  at probe. The `vdd` battery point mixes two units (100 = %, 3657 = mV) — 4 units report mV and are
  months dead.
- **AHUs on Saia, full instrumentation:** `LB72_2` (outdoor/supply/extract/exhaust/frost temps, supply
  + extract flow and pressures, filter dps, heating/cooling valves, heat-recovery signal, both VFDs),
  `LB733` (same, incl. room temp), `LB121`/`LB122` (outdoor/supply/room, flow, pressure, VFD),
  `LB32`/`LB33`/`LB52` (two supply flows + fan running), `LB731` (m³/s flows + Econet recovery),
  `LB732`, `LB203`, `LB102`, and `LB13` with 83 points (the SCADA pilot).
- **Measured schedules (7 days):**
  ```
  LB72_2  supply fan   07:00–19:00  every day, Sunday identical to Saturday   1,600 l/s
  LB32    flows        07:00–19:00 WD (+ a 20–22 run at 1,400 l/s), 07–17/18 WE
  LB33    fan          08:00–19:00 WD, 09:00–17:00 WE
  LB731   flows        06:00–17:00 daily, WD evening 18–22 at half flow
  LB733   cooling      supply 16 °C 10:00–17:00 every day incl. weekend; room 25 °C at night
  LB121   supply       06:00–17:00 WD only, supply 16 °C when running
  LB122   fan          06:00–16:00 WD only, 950 l/s; off weekends
  ```
  NK's published hours are roughly Mon–Fri 10–20, Sat 10–19, Sun 11–18 — **confirm with Stefan
  before any schedule rule fires.** LB72_2 and LB733 running the same hours on Sunday as Saturday is a
  candidate finding, not a finding.

### Saluhall refrigeration — a domain nobody else has
`KB12` brine −6.7 °C supply / −3.8 °C return, dp 49.9 kPa, pump B at 85 %; `VKA12` compressors at
8.0 / 7.8 bar high side; `FA12` dry cooler 26.1 → 37.5 °C at 59.6 % with the emergency city-water
cooling meter (`Kallvatten Nödkyla VKA12`) in Mestro. Food-safety and compressor-health signals at
10-minute cadence. **Setpoints and alarm limits unknown — ask.**

### Comfort cooling and hand modes
`VKA.ANTAL` (chillers running) 0.1; `KB1` loop 25.9/30.9 °C (looks like the food-hall heat-recovery
loop "ÅV KB01 saluhall", not chilled water); `VKA3A/3B` condenser pressure 0.0 (off); `KM1`, `KB102`
(dew point 12.4), `KB802`. **Ten alarm tags active at probe:** `VKA3A/3B.SV31/SV32 Ventil i fel läge`
(4), `VKA3.SEK Regl. handstyrd`, `AU.HAND Analog utgång i hand`, `LB731.ECONET.SLB Summalarm B`, and
three Modbus elevator "Safety Chain Status" words (63/63/7 — status words, not booleans). 287 alarm
tags live in total. Polarity 1 = active fits the Modern Styrteknik `*1B` convention but is **not
confirmed by a known event.**

### District heating — live, despite the 4-day lag elsewhere
`VP1.MQ41` on the Fjärrvärme PLC (10.3.105.112): energy register 4,376,850, volume 100,582 m³, power
0–5.6 (September idle), ΔT 2.4 K, at 10-minute cadence. **Units unverified** (kWh vs MWh, kW). This is
the one energy signal the agent can read same-day. Solar (`410 Solpanel`, SolarEdge) is Mestro-only.

### Lifts
18 lifts on Saia (`HISS1..22`, gaps): `DI` "i drift" (instantaneous, 4 of 19 at probe), `PLAN.DI` at
preferred floor, `LA` "ej på förvalt plan" alarm (all 0), `Counter` — **values from 0.5 to 4 million;
meaning unknown, not trips.** Plus 3 Modbus elevator devices with 13 alarm/status points. Enough for
"a lift has been off/alarming since X", not for availability %.

### Energy meters (Mestro) — hourly, **4.0–4.4 days behind**, 5 at 7 d, 3 at 28 d
85 internal electricity submeters (per floor, per AS-central, per tenant zone: "Plan1/Uk Butik
101-130 Del 27-43 MQ41-2"), 34 tenant electricity, 2 main electricity (Ellevio historik, HANP1),
district heating energy + volume (2 meters), cooling (FF413, KB1 saluhall, KB11 kyldiskar), solar,
3 city-water mains (SVOA 1–3), ~60 hot/cold water per food-hall tenant.
**Use:** a Monday retrospective on the last complete Mon–Sun that ended ≥ 4 days earlier. Never
"yesterday's kWh". A daily agent that tries will print nothing or fabricate.

### Live electrical
One Milesight CT305 clamp in room TEKNIK: 57.4 / 57.4 / 57.9 A on three phases at 0.3 h age, plus
cumulative registers. What it feeds is unknown.

## Traps specific to NK
1. **`X-Property-Owner` header or nothing.** Without it every Hufvudstaden twin is a 404 on REST.
2. **429 = "never observed" in a naive script.** See above.
3. **30 outdoor probes = 1 value.** Do not average them or report agreement.
4. **`.SA` tags are regulator outputs**, not setpoints or positions — "valve 60 %" means commanded.
5. **Hand-mode alarms are set legitimately** by Plant S operators and, later, by our connector
   (`*1B Analog utgång i hand`). Quote them; do not call them faults.
6. **`HISS*.Counter` is not a trip counter.** `DI` is a snapshot.
7. **Mestro `latest` is 4 days old and looks fresh** — the value is real, the date is not today.
8. **`vdd` mixes % and mV.**
9. **Lindinvent flow floor 0.6 l/s and opening floor 15.5 %** are the closed position, not zero.
10. **No floor area, no opening hours, no refrigeration setpoints, no VP1 units on file.**

## Open questions for Stefan Stoor (needed before the agent speaks about them)
- Opening hours for the store, the Saluhall and the office floors; is Sunday = Saturday for LB72_2/LB733?
- Is the 03:00 weekday office start the night-cooling sequence (`LB104.NK -3 °C`)? Until when in autumn?
- KB12/VKA12 setpoints and alarm limits; is `KB1` the heat-recovery loop?
- VP1.MQ41 units; `HISS.Counter` meaning; alarm polarity confirmation with one known event.
- Heated floor area (m²) for the building and for PLAN 8–10.
- Are `VKA3A/3B Ventil i fel läge` ×4 and `VKA3.SEK handstyrd` known/accepted states?

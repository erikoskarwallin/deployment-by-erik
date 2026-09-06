# Frydenlund — time channels, measured ground truth (06.09.2026)

Authority for [frydenlund-B-schedule-occupancy.md](frydenlund-B-schedule-occupancy.md) wherever
the spec and a handover document disagree. Source: the Phase B all-types BACnet scan of
04.09.2026 (`phaseB/frydenlund_phaseB_ALLTYPES.csv`, 23,759 objects) and its decoded schedule
extract (`phaseB/schedules_decoded.csv`), both in the Drive site folder
`Onboarding ProptechOS/8. Building discovery/KLP/Frydenlund/`. Read from the PEG, read-only,
between 09:13 and 19:43 local on 04.09. Regenerate with `onboarding/system-onboarding/klp-frydenlund/schedule_build.py` (writes `schedules.json` +
`bindings.csv`; `schedule_gen_html.py` renders the Tidskanaler Frydenlund page from it).

⚠️ **Nothing at Frydenlund is live in ProptechOS yet.** Devices live: 0, sensors live: 0, apart
from the 15 EXAMPLE twins for `P46 360.001` (schedule sub-device
`50cffd43-9c05-4d94-b3c9-7c3e2067f4a2` + 14 day-points) whose synthetic observations were
deleted on 06.09. Every number below is a BACnet read, not a ProptechOS value. The agent cannot
run until the connector delivers.

## 1. What a time channel is here

BACnet `schedule` objects on Distech ECY-S1000 / ECY-650 AHU controllers. The Norwegian TFM tag
`360.xxx` is a ventilation system (an AHU); `370` is cooling, `320` heating. `JV401` is the
supply fan, `JV501` the extract fan (`Pådrag tilluftsvifte` — JV is a *fan*, not a valve).

```
88 schedule objects on 71 devices
   73  occupancy-type time channels on 65 AHU controllers   <- the agent's population
    7  constant 00:00-24:00 fan channels (P46_360.003 x6 for systems 360.004-009, P42_360_001 ch 2)
    1  night-cooling channel  P44_360.012 IV001_KMD_BV_FKJ 02:00-06:00 every day
    2  fan channels for 360.003 on the P48 HEATING controller P48_320.001 (JV510 06-18, JV511 06-19)
    5  empty  P52_370_001 · GOLD Schedule #1 · H1_37003_004 · both Carrier 30/61WG occ_scheduling
```

Day entries read `07:30=1; 18:00=()`. `()` is BACnet NULL = release to `scheduleDefault`.
Some weekends read `07:50=0; 23:00=()` — an **explicit 0**, i.e. off. Multi-state channels
(`=2`, `=3`) select an operating level on `P44_360.010`, `P44_360.012`, `P44_360_013`,
`HG1_V360_00x`; treat any non-zero as ON.

## 2. The campus at a glance

| | |
|---|---|
| Typical weekday channel | 07:00–17:00 Mon–Fri, **50 h/week** (median 50.0 h, 39 of 73 channels within 47.5–52.5 h) |
| Channels with weekend blocks | **13** on 12 AHUs |
| Channels stopping ≥ 21:30 on a weekday | **8** |
| Channels explicitly OFF on a weekday | 2 — `V360007` Mon+Wed (23 h/week), `360008` Wed (31 h/week) |
| Constant 24/7 fan channels | 7 (168 h/week each) |
| AHU `start_modus` at scan | **64 of 64 readable = Auto.** No AHU in `Av` or `Manuell`. (The 19 `Av` / 2 `Manuell` hits in the scan are *pump* start modes on 320/370 controllers.) |
| Supply-fan status at scan (daytime) | 40 `JV401` active, 25 inactive |

### Longest channels — where the hours are

```
 91.7 h  V360.004        ch 2 + ch 3 JV503   06:00-22:00 Mon-Fri, 09:00-15:00 Sat+Sun
 87.5 h  P44_360_013     ch 1 (=3)           05:30-23:00 Mon-Fri, explicit 0 weekends
 84.6 h  P52_360_011     ch 1                06:05-23:00 Mon-Fri, Sun explicit 0
 79.0 h  P50_360_011     ch 1                08:10-21:30 Mon-Fri, Sat 09:50-18:00, Sun 11:50-16:00
 78.7 h  P44_360.012     IV001_KMD_MSV (=3)  06:55-16:35 Mon-Fri, Sat+Sun 07:50-23:00 (=1)
 78.2 h  P50_360_010     ch 1                08:15-21:30 Mon-Fri, Sat 10:00-18:00, Sun 12:00-16:00
 77.0 h  P44_360_013     ch 2                07:00-18:00 all seven days
 72.8 h  P46_360_001     ch 1                07:30-18:00 Mon-Fri, Sat 07:45-18:00, Sun 08:00-18:00
 66.7 h  P48=360.001     ch 1                06:55-18:00 Mon-Fri, Sat 11:15-18:15, Sun 11:15-15:15
 66.2 h  P46_360.002     ch 1                07:00-18:00 Mon-Fri, Sat 11:05-18:15, Sun 11:10-15:15
 63.6 h  P48=360.002     ch 1                07:30-18:00 Mon-Fri, Sat 11:20-18:15, Sun 11:20-15:15
```
Also weekend blocks: `P48_360.003A/B` (Sat 11:10–18:15, Sun 11:15–15:15), `P48_360.004`
(Sat 09:00–13:00, Sun 09:00–16:30), `P52_360_002` instance 1090 (Sun 12:35–19:00).

**The P46 / P48 pattern** — Saturday ~11:00–18:15, Sunday ~11:15–15:15 on six AHUs across two
buildings — looks like library or reading-room opening hours, i.e. probably deliberate. **The
06:00–23:00 weekday channels on P44_360_013, P52_360_011 and V360.004 are the ones worth asking
about**: 17 h/day of ventilation needs 17 h/day of people.

## 3. Occupancy evidence — 4 of 65 AHUs have any

The AHU controllers carry **no occupancy sensing of their own**, with three exceptions. Zone
controllers carry it, but can only be joined to an AHU by *name*.

| Tier | AHU | Evidence | Note |
|---|---|---|---|
| A | `P42_360005` | `RY501` CO2 i avtrekk (430 ppm at scan) | also `RB601/RB602 Motion` — both in `communication-failure` |
| A | `HG1_V360_001` | `RY501` 500 ppm | building unknown (`HG1`) |
| A | `HG1_V360_002` | `RY501` 551 ppm | building unknown |
| B | `P46_360.002` | 13 zone controllers `P46_360.002-<rom>-SQ4xx`, **7 with `RY601 CO2 føler sone` + `RB601 Tilstedeværelse sone`** | the only name-joinable AHU. Rooms 108, 110, 113, 117, 121, 124, 128 |

**Unattributable:** 26 ECY-VAV controllers named `360.012-L1xx-SQ…` (15) and `360.013-G41x-SQ…`
(11), each with 3 CO2 inputs. They carry **no building prefix**, and `360.012` / `360.013` exist
in P44, P50 and P52 alike. They may be P44's (Elisabeth Lampes hus — rooms `L…`?), which would
give occupancy to the two longest channels on campus. **Ask Nordomatic before binding.**

**Not tied to any AHU:** `Pilestredet 54 romreg` (Saia, 5 CO2 + 14 presence + 187 temps), three
Siemens KNX↔BACnet gateways (`møterom`, 4th/7th floor, 31 presence points), Phoenix Controls lab
airflow. Useful later for lighting or meeting-room channels, not for AHUs.

**Consequence for the agent:** occupancy validation is ⚪ for 61 of 65 AHUs and says so in one
line, never one line per AHU. Its main product until proxies arrive is the schedule audit itself.

## 4. Traps

1. **Duplicate device names with different channels.** `P52_360_001` is device 1093
   (07:00–16:30, weekends explicit 0) *and* 10118 (06:55–16:25). `P52_360_002` is 1090
   (07:00–17:05, Sun 12:35–19:00) *and* 10121 (07:00–16:05, weekends explicit 0). A littera
   stem `P52_360_001-Schedule_1` would collide. **Stem must carry the device instance.**
2. **Times must never be in twin names** — see `schedule-twins-mcp-agent.md` §3.
3. **`hourly`/`daily` aggregation on a schedule sensor averages two clock times** into one nobody
   set. Schedule values are `latest` or `raw`, never aggregated.
4. **`()` release vs explicit `0`** are both "off" for the agent but not for the BAS: a release
   hands control to `scheduleDefault` or a lower-priority writer. The twin model stores start/stop
   only; the connector decides what a release means. Do not infer otherwise.
5. **The 25 inactive supply fans at scan time** were read over a ten-hour daytime window on a
   Thursday; the scan does not say whether each was inside its channel. Not a finding.
6. **`GOLD Schedule #1` present-value 4 with an empty week** — the Swegon GOLD runs on its own
   `Schedule operation level` (`4 = Normal`), not on a weekly channel. Out of scope.
7. Building for prefixes `V` (12 AHUs), `A` (4), `H1`, `HG1`, `Holberg`, `434023`, `360008`,
   `ECY-S1000-0CBE9B` is **unknown** — 26 of 65 AHUs. The eleven ProptechOS buildings are listed
   in the Drive handover; `V`/`A` may be wings of P50/P52 or Pilestredet 75C. Ask.

## 5. What is not here

No occupancy history, no fan-run history, no energy. The schedule *values* are a 04.09 snapshot;
the agent's `CHANGED:` line compares live values against exactly that snapshot, embedded in its
bindings table, because it has no memory and no report store.

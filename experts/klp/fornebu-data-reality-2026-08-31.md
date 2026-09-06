# FORNEBU S — WHAT THE DATA ACTUALLY IS

**Measured 31.08.2026 14:10–14:35 UTC** against the live platform, property owner
confirmed **KLP**. Supersedes the sense inventory in
[fornebu-embodied-agent.md](fornebu-embodied-agent.md) v0.1, which was built from
the handover documents. Several of those documents were wrong.

---

## HEADLINE: the KNX layer is live

Newest observation while measuring: **14:14:50 UTC, four minutes old.** This is a
building that is genuinely talking, and the Wednesday demo has real data behind
it.

```
layer          sensors   <1h   1-24h   1-7d   >7d   never
KNX              711     240    172      94     9    196
Soundsensing     300       0      0       0     0    300   <- all dark
BACnet        10,856       0      0       0     0 10,856   <- all dark, PLAT-5774
KLP datalake      85       0      2       0    13     70
               ------
total         11,952
```

**515 of 711 KNX sensors have ever reported; 412 within 24 h.**

## Five things the handover got wrong

1. **The KNX alias namespace is `https://ns.proptechos.com/knx/fornebu/`**, not
   the planned `…/knx/klp-fornebu/`. Namespace id `5c4ec5ad-e4e1-48bf-b8bc-dfcab569d145`.
   Anything resolving by the planned name finds nothing — which is exactly what
   happened on the first probe pass.
2. **The alias carries the KNX individual address too**, as
   `…/knx/fornebu/{group address}/{device IA}` — e.g.
   `…/knx/fornebu/4/1/18/2.2.11`. **That settles the 711-vs-439 question: both
   numbers are true.** 711 sensor objects over 461 distinct group addresses
   (222 GAs with one sensor, 228 with two, 11 with three). The duplicates are the
   same bus signal seen from two devices, and they are distinguished only by the
   IA suffix.
3. **Soundsensing IS onboarded** — 300 sensors over 60 BLE devices, each with
   `VibrationX/Y/Z` (Acceleration, m/s²), `BatteryVoltage` (V) and `Temperature`
   (°C). The handover says it was parked as a later cloud-to-cloud project. The
   twins exist; **not one has ever reported.** So the effect is the same as
   parked, but the modelling is already done and 60 accelerometers are waiting
   on a connector.
4. **The four staff shower-room temperatures are dark.** All 12 `Heating`
   sensors have never reported. So the building has **zero live indoor room
   temperature** — not four. The spec's "four rooms I can feel" is wrong.
5. **`get-sensor-historical-data` works and the analogs are polled hourly** —
   26 observations in 26 hours, spacing exactly 3600 s. Not change-of-value.
   The binaries *are* change-of-value.

## The demo's best material: 46 switchboard temperatures

Unambiguous, analog, live, hourly, no polarity risk.

```
90 sensor objects over 46 boards, 87 reporting
median 27.20 °C   range 21.90 – 31.60 °C   spread 9.70 °C
warmest  433.196  31.60 °C   (24 h range 31.40 – 32.20)
coolest  433.015  21.90 °C   (24 h range 21.90 – 22.90)
```

This is the rule the spec already describes — compare the population against
itself — and it works today on real numbers. 433.196 sits 4.4 °C above the
median. Not alarming, but it is the warmest board in the building and nobody has
ever looked.

## ⚠️ THE THING THAT MUST NOT BE DEMOED: `Feil` does not mean the same thing on every unit

The naive read of the escalator set at 14:12 was **"6 of 8 moving walks are
faulted"**. That is almost certainly false, and finding out why is the most
valuable thing this exercise produced.

**Evidence — RB 01, three days, time-aligned (UTC):**

```
29.08 05:34  Drift 0->1   (starts)      29.08 06:05  Feil 0->1   (~30 min later)
29.08 17:54  Drift 1->0   (stops)       29.08 17:54  Feil 1->0   (3 seconds later)
30.08 07:25  Drift 0->1                 30.08 07:55  Feil 0->1
30.08 16:31  Drift 1->0                 30.08 16:31  Feil 1->0
31.08 04:32  Drift 0->1                 31.08 05:02  Feil 0->1
```

On RB 01, **`Feil` tracks running**, not faulting. It rises after the unit
starts and falls within seconds of it stopping.

**But it does not behave that way on all fifteen units**, and I over-generalised
this before checking. Seven days per unit:

| unit | `Feil` 7 d | `Drift` 7 d | reading |
|---|---|---|---|
| RB 01, 02, 08 | 20/20, 18/18, 520/508 | toggles | `Feil` co-varies with running |
| RB 03, 05, 06 | toggles | toggles | same |
| **RB 04** | **0 × 14, never 1** | toggles | `Feil` behaves conventionally — and is quiet |
| **RB 07** | 0 × 1014, **1 × 6** | **no data at all** | conventional fault flag, 6 events. **No `Drift` telemetry.** |
| **RT 01** | 0 × 7 | **no data at all** | **No `Drift` telemetry.** |
| RT 02, 05, 07 | mostly 0, 2–4 × 1 | toggles / RT 07 flat 0 | conventional fault flag |
| **RT 03** | 0 × 976, **1 × 4** | toggles | conventional — **4 fault events in 7 days** |
| RT 04 | 513/511 toggles | toggles | co-varies with something cyclic |
| RT 06 | 0 × 7 | **1 × 1015, never 0** | runs continuously, never stops |

**So the fault semantics are inconsistent across the fifteen units** — a
commissioning inconsistency in the building, not a platform bug. Until Nordomatic
confirms the convention per group, **no fault count can be presented as fact.**

### What IS safe to say about the moving equipment

- **`Drift` is the trustworthy availability signal.** 13 of 15 units were in
  `Drift` at 14:12 on a Monday afternoon.
- **`RT 07` has `Drift = 0` for seven straight days** — stopped all week.
- **`RB 07` and `RT 01` have no `Drift` telemetry at all.** Two of fifteen units
  cannot be checked for availability.
- **`RT 03` shows 4 discrete events and `RB 07` shows 6** in seven days. Under
  the conventional reading those are real, and that is a maintenance
  conversation.

### Two more signals that carry no information

- **`Brannvarsling Feil` = 1 on all 955 observations over 7 days.** Constant. As
  labelled it means the fire panel has been in fault for a week; more likely it
  is a health/heartbeat contact. Either way it says nothing today.
- **`2B 3042 HCWC Snorbryter utløst` = 0 on all 163 observations.** Under the
  documented `On=OK` inversion that is a permanently activated pull cord in an
  accessible toilet, which is not credible. Treat as unwired until proven.
- 8 of 15 `Brannslokkeskap` cabinet contacts read 1 with almost no transitions.

## ⭐ THE LIFTS DO REPORT FAULTS — 218 events in 30 days

Checked 31.08 across all 24 lift signals, paginated in 5-day windows so nothing
was lost to the 2,000-sample cap. **Every one of the 12 lifts raised `Feil` at
least once in the last 30 days.** This also settles the polarity question for the
lifts: discrete, varied, unit-specific events are fault behaviour, not the
running-state behaviour seen on the escalators.

| lift | samples | `Feil` events | total in fault | longest |
|---|---|---|---|---|
| **HEIS 7** | 3,716 | 10 | **1,030 min (17.2 h)** | 319 min |
| **HEIS 11** | 1,478 | **89** | 661 min (11.0 h) | **613 min (10.2 h)** |
| **HEIS 3** | 1,380 | 12 | 405 min (6.8 h) | 175 min |
| HEIS 12 | 316 | 13 | 191 min | 126 min |
| HEIS 6 | 3,741 | 6 | 122 min | 109 min |
| HEIS 8 | 3,278 | **48** | 53 min | 30 min |
| HEIS 1 | 1,045 | 9 | 41 min | 41 min |
| HEIS 2 | 2,269 | 7 | 36 min | 23 min |
| HEIS 9 | 3,298 | 9 | 32 min | 30 min |
| HEIS 4 | 621 | 11 | 1 min | 1 min |
| HEIS 5 | **13** | 3 | 0 min | 0 min |
| HEIS 10 | 3,685 | 1 | 0 min | 0 min |

⚠️ **Sample density varies by a factor of 280** (13 to 3,834). Event counts are
therefore **floors, not totals**, and are not safely comparable between units.
**`HEIS 5` has 13 samples in 30 days — it is effectively unmonitored**, and its
"3 events / 0 minutes" means nothing. `HEIS 8 Alarm aktivert` returned **no data
at all** in 30 days.

`Alarm aktivert` is much quieter: 8 momentary events on HEIS 1, 8 on HEIS 10,
16 on HEIS 9, 1–2 on HEIS 3/4/6, zero on the rest. All zero-duration — single
samples — so they read as transient rather than as someone trapped in a car.

### ⚠️ Two lifts show a recurring overnight pattern starting at the same second

This is the most interesting thing in the whole dataset and the most dangerous
to interpret.

```
HEIS 3   starts 02:37:29 / 02:37:30 on four nights
         22.08  0:00:00      (single sample)
         28.08  1:25:06
         29.08  2:25:07      <- growing
         30.08  2:55:15      <- growing
         31.08  did not recur

HEIS 7   starts 23:23:31 on four nights, to the second
         21.08  4:19:17      24.08  2:59:17
         28.08  4:29:16      29.08  5:19:17
```

**A same-second start across multiple nights is a schedule, not a random
fault.** Candidates: a nightly lift self-test or inspection mode that the KNX
contact reports as `Feil`; a cleaning or service window; a power or lighting
schedule the lift shares. HEIS 3's durations growing on three consecutive nights
is the part that would matter if it is *not* scheduled.

**Do not assert a cause.** The honest statement is: *"two of your lifts enter a
fault state at exactly the same second on multiple nights, and on HEIS 3 that
state lasted longer each night for three nights running. Is 02:37 a scheduled
service window?"* That question is for Nordomatic / the lift contractor (Kone),
and it is a genuinely good question to arrive with.

## A real onboarding defect worth a ticket

The sensor's `source.deviceAddress` is what the connector polls. Checked against
the ETS project (keyed on signal name **and** function — `433.001` is three
different signals):

```
377  deviceAddress correct, alias correct
197  deviceAddress correct, ALIAS corrupted     -> cosmetic, breaks lookup
 41  deviceAddress WRONG, alias wrong
 14  deviceAddress WRONG, alias correct
 82  no ground truth in the manifest
```

**And a wrong `deviceAddress` predicts missing data:**

```
deviceAddress correct   n=574   never reported  86  (15 %)
deviceAddress wrong     n= 55   never reported  43  (78 %)
```

The corruption looks like a digit-group insertion: ETS `2/1/11` became alias
`2/1/2011`; `0/0/1` became `2000/1/1`; `6/1/0` became `6/1/2000`; and three
different UPS signals (`1/0/2`, `1/0/202`, `1/0/220`) all carry
`deviceAddress = 1/0/2`, so two of the three are subscribed to the wrong bus
address.

**Owner: Oksana (write phase) / Marichka (connector).** This is the likeliest
single cause of the 196 never-reporting KNX sensors, and it is fixable by
regenerating from the manifest rather than by hand.

## Where the roster now stands — the deploy blocker is cleared

`fornebu-embodied-knx-bindings.csv` now carries, per group address:
`sensor_id_CHOSEN` (preferring a sensor whose `deviceAddress` matches ETS, then
the freshest), `sensor_ids_ALL`, `deviceAddress_in_p8s`, `addr_matches_ets`,
`latest_value`, `latest_obs_utc`, `age_hours`, `live`.

```
tier A   82 live · 18 stale · 7 never · 2 no sensor    -> 100 of 109 readable
tier B   85 live ·  8 never · 8 no sensor              ->  85 of 101 live
tier C   58 live · 29 stale · 68 never · 70 no sensor
tier X    3 live ·  1 never   (decommissioned — never report these)
```

**~167 live signals across tiers A and B.** That is enough for the agent to run
for real.

## The meters — thin but not empty

85 sensors, 70 never reported. What does report:

- **`Volum vann delta` = 75.23 at 31.08 00:00:00 UTC** — midnight-stamped, so
  **daily** granularity, not monthly. One "yesterday's water" line is defensible.
- Waste is modelled as Norwegian waste chapters — `1100 Bioavfall og slam`,
  `1200 Papir papp og kartong`, `1300 Glass`, `1400 Metall`, `1500 EE-avfall`,
  `1700 Plast`, `1900 Tekstil skinn møbler og inventar`, `2300 Batterier`,
  `6000 Medisinsk avfall`, `7000 Farlig avfall`, `9900 Blandet avfall` — but
  almost all of them are empty.

**Do not build the ESG story on this.** One water figure and a mostly-empty waste
taxonomy is not a consumption narrative.

## Corrections owed to the agent spec

- namespace `…/knx/fornebu/`, alias includes the device IA
- the four shower temperatures are **dark** — there is no live indoor temperature
- Soundsensing twins **exist** (300, all dark); 60 accelerometers modelled
- analogs are **polled hourly**; binaries are change-of-value — the freshness
  section's guess was right in shape, now it is measured
- `Drift`, not `Feil`, is the availability signal
- the `deviceAddress` defect and the 461-GA reality are new and belong in the
  spec's data-quality section

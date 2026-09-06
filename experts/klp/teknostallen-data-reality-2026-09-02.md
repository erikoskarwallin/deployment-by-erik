# TEKNOSTALLEN (Prof. Brochs gate 6) — MEASURED DATA REALITY, 02.09.2026

**Status: re-verified 03.09.2026 07:15 UTC — nothing drifted.** Live counts and the
airflow curve reproduce exactly; the captured run is `teknostallen-demo-readiness.md`.
Probed live against `proptechos.com/api` with a KLP-bound token, 15:43–16:20 CEST.
Everything below is measured, not from a handover document. Demo for **Lasse Volden
(KLP), Thursday 03.09.2026**.

```
Building   05a59f07-845f-425b-901d-a53f2bd5fa4d   Teknostallen, Prof. Brochs gate 6
RealEstate dd90c8b4-ab7a-43b2-8fa7-7a3891cac00c
PO KLP     40d473bf-7d9c-4313-8387-d1cbb5f50c4c   ← bind the session or every call 401s
Decoy      76181108-a5f0-4215-b298-b9e1509317d9   gate 10, same name, NO data — never target it
```

---

## ⭐ HEADLINE: this building is the opposite of Fornebu

Fornebu is an availability/safety bus with 4 indoor temperatures. **Teknostallen is a
fully instrumented comfort building, live, with four months of history.** It is the
best demo dataset we have in the KLP account.

```
6,071 sensors on the building     6,022 reported within the last hour (99.2 %)
                                     18 never,  22 older than 7 days,  9 within 24 h
1 system: "Piscada BACnet"        one gateway, 10.20.1.139, 6,022 of the sensors
2,984 rooms · 6,127 devices · 0 actuators   → monitoring only, no write path
History back to 2026-05-11        ~10-minute spacing on everything checked
```

### The zone layer — 661 fully-instrumented zones

Littera shape is `TST_564_<system>_<point>_<room>`; joining on `(system, room)` gives:

| per-zone signal | littera | live count |
|---|---|---|
| room temperature | `RT01_MV_<room>` | 855 |
| room setpoint | `RT01_SPK_<room>` | 818 |
| CO2 | `RY01_MV_<room>` | 768 |
| heating demand % (`Varmepådrag`) | `RT01_Heat_<room>` | 801 |
| cooling demand % (`Kjølepådrag`) | `RT01_Cool_<room>` | 793 |
| VAV supply volume m³/h | `SQ4x_Vol_<room>` | 1,388 |

**661 zones carry all six.** Another 85 also have extract-damper feedback.
Nothing at Fornebu, 1700 Pavilion or Bldg J comes close to this.

Current population (02.09 13:39 UTC): room temp median **22.6 °C** (p10 21.2, p90 23.8,
max 30.3) · setpoint median **21.9 °C** · CO2 median **484 ppm** (max 2001) ·
supply volume median **114 m³/h**.

---

## THE FINDINGS (all measured, all defensible)

### 1. ⭐⭐⭐ There is no night or weekend setback — and on weekend nights the schedule is INVERTED

Building-wide supply airflow, sum of all 1,382 reporting VAV supply-volume points,
hourly, local Oslo time:

```
Fri 28.08 14:00  223,777 m³/h   ← weekday peak
Fri 28.08 21:00   33,166        ← correctly shut down
Fri 28.08 23:00  199,202        ← ⚠ jumps back to 89 % of peak
Sat 29.08 02:00  172,138        ← still running, building empty, CO2 400 ppm
Sat 29.08 06:00   29,588        ← shuts down as Saturday begins
Sat 29.08 14:00  ~35,000        ← idles all Saturday (correct — nobody there)
Sat 29.08 23:00  208,353        ← ⚠ same again
Sun 30.08 23:00  168,159        ← ⚠ and again
Mon 31.08 23:00   29,286        ← weeknights are FINE
```

**The full-flow window is 23:00–04:00 on Friday, Saturday and Sunday nights only.**
Three nights × ~5 h × ~180,000 m³/h in an empty building. Weeknights behave correctly.
CO2 sits at 375–400 ppm throughout — proof the building is empty.
⚠ *Unverified cause.* Candidates: a weekend program whose day/night blocks are
transposed, a night-purge routine, or a filter/flush schedule. **Ask Nordomatic /
the Piscada integrator; never assert the cause.**

### 2. ⭐⭐ Temperature setback does not exist at all

Hourly mean over 45 sampled zones, 9 days: room temperature stays **20.0–21.5 °C**
every hour of every day including Saturday and Sunday, and the **setpoint is a flat
20.0–20.2 °C in all 24 hours**. There is no unoccupied setpoint anywhere in the sample.
Heating demand is 17–31 % and cooling demand 28–53 % around the clock, at weekends,
with nobody in the building.

### 3. ✅ PASS — no simultaneous heating and cooling within a zone

Checked 45 zones × 223 hours = 10,035 zone-hours. **One** zone-hour had heating >10 %
and cooling >10 % together (sys101 room 1125). The zone controls are well behaved.
The high fleet means in finding 2 are *different zones* heating and cooling, not reheat.
**Report this as a pass — it kills a Fornebu-D-style agent here and that is good news.**

### 4. 236 zones off setpoint by ≥2 K right now — but 92 setpoints are dead

Split before showing anything: 723 setpoints are valid, **92 read below 5 °C** (mostly
exactly 0.0) and must be excluded or they manufacture fake 25 K deviations.
With valid setpoints only: **216 zones ≥2 K off**, worst:

```
sys001 rom 3600   T 24.0  SP 15.5  d +8.5  cool 100 %  CO2 578  flow 149
sys001 rom 1214   T 22.4  SP 15.5  d +6.9  cool 100 %
sys101 rom 2132   T 26.3  SP 19.5  d +6.8  cool 100 %
sys101 rom 1096   T 21.3  SP 27.0  d −5.7  heat 100 %   ← setpoint 27 °C
sys101 rom 1540   T 19.9  SP 25.0  d −5.1  heat 100 %
```
⚠ Setpoints of 15.5–19.5 °C in occupied rooms are themselves suspect. **Whether `SPK`
is a comfort setpoint or a cooling setpoint is UNVERIFIED — confirm with the integrator
before calling any of these a fault.** 293 zones command cooling at 100 % and 101
command heating at 100 % at the same moment.

### 5. Data quality — flatline scan over all 1,620 room temp + CO2 points, 2 days

Every one of the 1,620 was fetched over 31.08–02.09 and tested for variation.
**OTEAM-6733 (filed July 2026) is unresolved — the same ~55 sensors are still stuck.**

```
Temperature   797 varying (healthy)   55 FLATLINED   0 no-data
              flat at exactly 0.0 ×53 · 23.10 ×1 · 18.95 ×1
CO2           685 varying             83 FLATLINED   0 no-data
              flat at exactly 0.0 ×79 · 2000.64 ×2 · 461.12 ×1 · 412.16 ×1
```

⚠ **`2000.64` is a CO2 sentinel, not a reading.** Rooms `5079` and `2608` show
2001 ppm and are the only two zones above 1,000 ppm in the whole building — both are
**dead sensors pinned at the sentinel**, flat for 2 days. An agent that reports
"two rooms at 2000 ppm" is lying. Filter `2000.64` before any CO2 rule runs.
The two flat-but-plausible CO2 values (461.12, 412.16) are the dangerous class:
they look healthy and are not.

Also: 90–92 setpoints <5 °C, 59 supply flows at 0.0.

#### ⭐ The dead points are 55 ROOMS, not 137 sensors

Cross-referencing the two lists by `(system, room)`: **55 of the 57 dead room
temperatures sit in a room whose CO2 point is also dead.** Only 2 temperatures and
26 CO2 points fail alone. So this is **55 room sensor units — or a small number of
bus segments — not 112 independent failures**, and they cluster hard in the `3xxx`
room block. One site visit per room. Report it that way to a technician; the
per-point count is an Idun number, not a work list.

### 6. ⚠ The electrical metering is NOT usable as-is — 3 separate traps

127 `_kW` points, all reporting at 10-minute spacing, but:
- **8 meters are pinned to 32-bit sentinels**: `429496.7` (= 2³²/10⁴, on
  `TST_433_103_OEB0006_kW`, `TST_433_002_OEB002_kW`, `TST_433_003_OEB0002_kW`) and
  `214735.2` (constant, on `TST_433_403_OEB0002`, `_205_`, `_603_`, `_204_`, `_505_`).
- **`_ED` points are demand accumulators, not power.** `TST_432_002_OEC001_kW_ED`
  ramps 167 → 523 → 801 → 999.77 kW across 00:00–02:00 and resets. Summing it produced
  a fake "1 MW nightly spike at 01:00–02:00" that is a **meter artifact, not load**.
  ⚠ I nearly reported it as a finding. Any agent here must be told.
- `AG5_433_601_OEB0003_KWH` is a cumulative kWh register sitting in the kW family.

**79 meters look like plausible instantaneous kW; their summed median is ~749 kW.**
A unit/register audit is required before any kWh or NOK number is spoken aloud.

### 7. Other layers present
131 `ActiveEnergyTotal` · 56 `EnergyTotal` (secondary heating and cooling circuits,
with flow/return temps and volumes) · district heating (flow 101 °C, return 33.3 °C,
older than 7 d) · 26 waste-fraction counters (Norwegian waste chapters, all >7 d or
never) · one outdoor weather set (temp 16.2 °C, humidity, wind, pressure, precipitation,
wind angle) reporting within 24 h · 4 cold-water volume points.

---

## ⚠ TRAPS — read before writing any agent spec

1. **`startTime` / `endTime` are the history query parameters.** `from` / `to` are
   silently ignored and the endpoint then returns only the last ~24 h ascending.
   I briefly concluded "history was truncated on 01.09" from this — it was wrong;
   history goes back to **2026-05-11**. Same mistake would have hit Fornebu.
   `GET /json/sensor/{id}/observations?size=N&startTime=…&endTime=…`
2. **`size` truncates from the oldest end.** A 3,000-point cap over a month silently
   cut the newest week. Always check the last timestamp returned.
3. **Dead setpoints (92) and dead room temps (62) read exactly 0.0** and will
   manufacture 20 K deviations. Filter `<5 °C` before any comparison.
4. **32-bit sentinels `429496.7` and `214735.2`**, plus `999.77` on the `_ED` demand
   registers. Never publish a power number without excluding them.
5. **`_ED` = accumulating demand register, not kW.** See finding 6.
6. **`SPK` semantics unverified** — comfort setpoint or cooling setpoint. Blocks
   finding 4 from being called a fault.
7. **0 actuators** — this building cannot be written to. Monitoring agents only,
   which matches Lasse's stated preference (he drafts in chat and sends himself).
8. Two buildings are named "Teknostallen". Gate 10 has no data. Always gate 6.
9. Data gap observed Sat 29.08 11:00–15:00 across all flow points — cause unknown.

---

## WHERE THE RAW DATA IS

Session scratchpad (**volatile — will be gone after restart**):
`/private/tmp/claude-501/-Users-erikwallin-eriks-project-proptech-agents/2558b6ca-8f98-442d-a12e-5fb3f6ae88f5/scratchpad/`
— `tek_sensors.json` (6,071 twins), `tek_latest.json`, `tek_hist.json` (45 zones ×
6 signals × 9 d), `tek_flow_hist.json` (1,388 flows × 5 d), `tek_kw.json`,
`tek_energy.json`.

Re-fetchable with `onboarding/system-onboarding/klp-teknostallen/probe/po_lib.py`
(`PO_TOKEN_FILE=<file> python3 …`). **A proper `teknostallen_probe.py` has NOT been
written yet — that is task 1 on resume.**

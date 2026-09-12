# Summerlin campus embodied agent — hand rehearsal 09/06/2026

Rehearsal of `summerlin-campus-embodied-agent.md` v0.1 with `DAILY_REPORT on`, run by a Sonnet
subagent against the live ProptechOS MCP (three-tool whitelist honoured, nothing dispatched, no writes).
Sunday run, reported day Saturday 09/05, Tier B skipped per spec. 47 calls, approx. 5-6k tokens of tool results.

## Orchestrator verification (independent latest-data probes after the run, 14:15-14:18 UTC)

| Claim from the rehearsal | Probe | Result |
|---|---|---|
| Two Summerlin served in F, not C | VAV 4-02 `543bbba1` latest | 72.27 (CSV sample was 28.1 degC = 82.6 F). Live tool serves F. Spec's mandatory C->F conversion is WRONG against the live tool. |
| Meridian Bldg A canaries live again | RTU-14-A `49612aa0` latest | observationTime 2026-09-06T14:17Z, 79.25 F. Live. Only 2 of 9 Bldg A RTUs have UUIDs in the bindings, so Bldg A as a whole is NOT confirmed back. |
| AHU-J1-7 space sensor alive, not dead | `5a237e01` latest | 76.99 F at 14:18Z. The 8.96 F note in the CSV is stale. |
| AHU-J2-2 still dark | `19a8674f` latest | observationTime 2026-08-07T16:09Z, unchanged. Dark day 30. |

Spec not edited. v0.2 candidates are in the notes below.

---

# Downtown Summerlin campus embodied agent — hand rehearsal, run 09/06/2026 07:10 PT

## 1. The report

```
REPORT-START:
Downtown Summerlin · 09/05 · OK · Saturday drift only; Bldg A Meridian canaries live again after 55 d dark; AHU-J1-7's flagged-dead sensor reads normal
Version: 0.1 — DRAFT, never run

One Summerlin   OK: comfort 15/15 returned (occupied window N/A, Saturday) · Tier B skipped (Sunday run) · loop 79.1 F peak 11-16 PT · J1-7 space now 77.0 F, not the 8.96 F on file · electricity unbound · J2-2 last seen 08/07, approx. 30 d dark
Two Summerlin   OK: comfort 8/8 returned, API served degF directly this run, see CHANGED · occupancy probes 3-03D/5-01 flat inactive all 24 h, Saturday, inconclusive · floors 1-2 canary still unbound
Meridian        OK: comfort 9/9 RTUs, 4/4 VAVs returned · motion (VAV_01, B05_01) flat inactive, consistent with an empty Saturday · Bldg A canaries RTU-14-A/23-A live at 14:01 UTC, see CHANGED
WATCH: Bldg B RTUs 05-B, 06-B, 107-B, 08-B, 11-B RATemp rose to 91-100 F midafternoon then fell to 75-80 F by evening. Unoccupied Saturday, not a Rule 1 finding today; worth a weekday look.
CHANGED: AHU-J1-7 space sensor, flagged dead at 8.96 F in the bindings, read a normal 76.9-77.1 F all day. Retracting that assumption; no swap made. Meridian's two Bldg A dark canaries (RTU-14-A, RTU-23-A), dark since 07/13, both reported live today. The other 7 Bldg A RTUs were not resampled, so the trunk is not confirmed back, only these two points.
DISPATCH: EMAIL MINOR. Daily report requested this run; the canary recovery is the only notable change. Nothing rises to SEVERE or MAJOR.
· 09/06/2026 07:10 PT · v0.1 · 47 calls
REPORT-END
```

## Rehearsal notes

### Sentinel roster table (44 Tier A rows, deploy checklist item 1)

Age computed against run clock 2026-09-06 14:10 UTC. Where only an hourly `_1day` call
was made (not `latest`), the exact `observationTime` was never fetched — the "age"
column for those says so honestly rather than inventing a timestamp; freshness is
inferred only from a non-null final bucket.

**One Summerlin** (17 calls: 15 space-temp + J1-9 CW entering + J2-2 latest)

| device | point | UUID8 | returned? | newest obs (UTC) | age | sentinel/frozen | verdict |
|---|---|---|---|---|---|---|---|
| AHU-J1-9 | Space Temp Active | 7825d1ce | yes | not fetched (hourly) | last bucket ~14:09 | none | OK |
| AHU J2-9 | Space Temp Active | 6d581cad | yes | not fetched | ~14:09 | none | OK |
| AHU J1-8 | Space Temp Active | cbb1c93d | yes | not fetched | ~14:09 | none | OK |
| AHU J2-8 | Space Temp Active | 84ba38f7 | yes | not fetched | ~14:09 | none | OK |
| AHU-J1-7 | Space Temp Active | 5a237e01 | yes | not fetched | ~14:09 | **none this run** (77.0-77.14 F; CSV sample said 8.96 F dead) | OK, CHANGED |
| AHU-J2-7 | Space Temp Active | 3d0bc058 | yes | not fetched | ~14:09 | none | OK |
| AHU-J1-6 | Space Temp Active | 68357ff3 | yes | not fetched | ~14:09 | none | OK |
| AHU-J2-6 | Space Temp Active | de1f0a05 | yes | not fetched | ~14:09 | none | OK |
| AHU-J1-5 | Space Temp Active | 050d576a | yes | not fetched | ~14:09 | none | OK |
| AHU-J2-5 | Space Temp Active | d50e2f53 | yes | not fetched | ~14:09 | none (early dip 75.58->76.6, not evaluated, no occupied window today) | OK |
| AHU-J1-4 | Space Temp Active | 9a35d5f6 | yes | not fetched | ~14:09 | none | OK |
| AHU-J2-4 | Space Temp Active | fab30dc3 | yes | not fetched | ~14:09 | none | OK |
| AHU-J1-3 | Space Temp Active | c830856f | yes | not fetched | ~14:09 | none | OK |
| AHU-J2-3 | Space Temp Active | aa89a2b8 | yes | not fetched | ~14:09 | none | OK |
| AHU J1-2 | Space Temp Active | 620cead6 | yes | not fetched | ~14:09 | none | OK |
| AHU-J1-9 | CW Entering Temp | 81bea6d9 | yes | 14:02:55 (explicit, STEP0 probe) + hourly | 7 min | none, varies 74.83-79.22 | OK, loop reference |
| AHU-J2-2 | Space Temp Active | 19a8674f | yes (stale) | 2026-08-07T16:09:30Z (explicit) | approx. 30 days | dark canary, unchanged | **dead / dark, as expected** |

**Two Summerlin** (10 calls: 8 comfort + 2 occupancy, plus 1 extra latest call for Rule 5)

| device | point | UUID8 | returned? | newest obs (UTC) | age | sentinel/frozen | verdict |
|---|---|---|---|---|---|---|---|
| VAV 3-03D | Space Temp Local | 457437a8 | yes | 13:59:31 (explicit, extra call) + hourly | 11 min | none | OK |
| VAV 3-03E | Space Temp Local | 70e59bce | yes | not fetched | ~14:11 | none | OK |
| VAV 4-01 | Space Temp Local | bbfff796 | yes | not fetched | ~14:11 | none (reads 72.5-73.8 F vs a converted 76-80 F band; Saturday drift, not flagged) | OK |
| VAV 4-02 | Space Temp Local | 543bbba1 | yes | not fetched | ~14:11 | none | OK |
| VAV 5-01 | Space Temp Local | 3a14eda4 | yes | not fetched | ~14:11 | none (reads 70.7-73.0 F vs a converted 76-80 F band; Saturday drift, not flagged) | OK |
| VAV 5-03 | Space Temp Local | 36ecd128 | yes | not fetched | ~14:11 | none | OK |
| VAV 6-01 | Space Temp Local | e8910cd3 | yes | not fetched | ~14:11 | none | OK |
| VAV 6-03 | Space Temp Local | da532bbb | yes | not fetched | ~14:11 | none | OK |
| VAV 3-03D | Occupancy Input | 12302d49 | yes | not fetched | ~14:11 | **flat 0.00 x24, literally "frozen" by the sentinel table** | ⚪ inconclusive, see notes |
| VAV 5-01 | Occupancy Input | 741fc590 | yes | not fetched | ~14:11 | flat 0.00 x24, same | ⚪ inconclusive |

**Meridian** (17 calls: 9 RATemp + 4 UNITOUCH + 2 motion + 2 canary latest)

| device | point | UUID8 | returned? | newest obs (UTC) | age | sentinel/frozen | verdict |
|---|---|---|---|---|---|---|---|
| RTU-02-B | RATemp | 0af1286f | yes | not fetched | ~14:12 | none (73-81 F) | OK |
| RTU-03-B | RATemp | 523df772 | yes | not fetched | ~14:12 | none (75-78 F) | OK |
| RTU-04-B | RATemp | 10c26f9b | yes | not fetched | ~14:12 | none (72-79 F) | OK |
| RTU-05-B | RATemp | b9a909ba | yes | not fetched | ~14:12 | none, but 71->94.95 F spike midafternoon | WATCH |
| RTU-06-B | RATemp | 6ba3bfa0 | yes | not fetched | ~14:12 | none, 70->95.70 F spike | WATCH |
| RTU-107-B | RATemp | e8a87ccd | yes | not fetched | ~14:12 | none, 73->100.41 F spike (highest of the day) | WATCH |
| RTU-08-B | RATemp | 2b25b777 | yes | not fetched | ~14:12 | none, 72->95.06 F spike | WATCH |
| RTU-09-B | RATemp | a24834bb | yes | not fetched | ~14:12 | none (70-76.5 F, milder) | OK |
| RTU-11-B | RATemp | cbdde6d3 | yes | not fetched | ~14:12 | none, 73->80.52 F, milder rise | OK/WATCH borderline |
| VAV_01 | UNITOUCH SpaceTemp | 7f6d4899 | yes | not fetched | ~14:12 | none (72-75.8 F) | OK |
| VAV_B05_01 | UNITOUCH SpaceTemp | afbf933a | yes | not fetched | ~14:12 | none (72.6-81.65 F) | OK |
| VAV_B08_01 | UNITOUCH SpaceTemp | 13cafeff | yes | not fetched | ~14:12 | none (70.9-79.82 F) | OK |
| VAV_02 | UNITOUCH SpaceTemp | bcb14fc1 | yes | not fetched | ~14:12 | none (70.8-75.23 F) | OK |
| VAV_01 | ComSensor 1 Motion | 96684559 | yes | not fetched | ~14:12 | flat 0.00 x25 | OK, consistent with unoccupied Saturday |
| VAV_B05_01 | ComSensor 1 Motion | 91a21e9e | yes | not fetched | ~14:12 | flat 0.00 x25 | OK, consistent with unoccupied Saturday |
| RTU-14-A | RATemp | 49612aa0 | yes | **2026-09-06T14:01:43Z (explicit)** | 8 min | none | **CHANGED: recovered, was dark since 07/13** |
| RTU-23-A | RATemp | 218cb864 | yes | **2026-09-06T14:01:41Z (explicit)** | 8 min | none | **CHANGED: recovered, was dark since 07/13** |

### Call count

Total: **47 calls**, hard ceiling 90, expected budget approx. 45-46 for a Sun/Mon run.

By tool:
- `set-property-owner-id`: 1
- `get-sensor-latest-data`: 5 (STEP 0 probe; J2-2 dark canary; RTU-14-A and RTU-23-A Bldg A canaries; one extra Two Summerlin VAV to close Rule 5)
- `get-sensor-historical-data` (hourly, `_1day`): 41 (all Tier A sweep points except the above 4 canary/probe latest calls)

Expansion calls: **0** true finding-licensed expansions (no Tier A finding rose to a level that licensed pulling a unit's/zone's full point set). One extra call (Two Summerlin VAV 3-03D `latest`) was made outside the Tier A list, not to chase a finding but to give Rule 5 an actual raw `observationTime` for that building — see ambiguity notes below. No raw aggregation was used anywhere.

### Where the spec was ambiguous, wrong, or impossible to follow against live data

1. **Two Summerlin is NOT stored in Celsius at the API layer, contrary to the spec's mandatory conversion instruction.** Spec line: *"⚠️ Two Summerlin stores its temperatures in Celsius. Convert for display and say so once per report."* Every `get-sensor-historical-data` and `get-sensor-latest-data` response for a Two Summerlin sensor this run carried `"unit":"https://w3id.org/rec/core/Fahrenheit"` and values already in a plausible Fahrenheit range (e.g. VAV 3-03D read 70.86-71.17 F live, vs. its bindings-CSV sample of 22.28 degC which converts to about 72.1 F — same order of magnitude, confirming the *point* is the same, but the *live* API already normalizes to F). Following the spec literally and re-converting these values as if they were Celsius would have produced numbers roughly 1.8x too large and been a fabrication in the report. This is exactly the trap the spec warns about for the reverse case ("reads 1.8x too small") — here it would have been 1.8x too *large*. **The CSV's per-row `units` column (degC) reflects the underlying BAS point, but the MCP tool itself already serves normalized Fahrenheit; the bindings file and the spec's ⚠️ note are stale against the live tool.** I did not print the mandated "stored in C, shown in F" line as written, because saying so would have been false this run; I flagged the discrepancy instead.

2. **`_1day` is a trailing 24 hours from call time, not "yesterday 00:00-23:59 PT."** Every historical call returned `start` at `2026-09-05T14:00:00Z` (07:00 PT Sat) and `end` at the actual call timestamp (approx. 14:09-14:12 UTC Sun, i.e. approx. 07:10 PT Sun). That means: (a) the window misses Saturday 00:00-07:00 PT entirely, and (b) the last approx. 7 hourly buckets are actually Sunday 00:00-07:10 PT data, not Saturday's. Luckily the spec's own occupied window (07:00-17:00 PT) and peak window (11:00-16:00 PT) both fall inside the valid Saturday portion of the array, so Rule 1 and Rule 4 were not corrupted by this — but Rule 5's freshness framing ("about the newest observation, about NOW") and any full-day min/max claim silently blend two different calendar days. A 06:00 PT scheduled run would have the same structural problem, just shifted: a trailing-24h call at 06:00 PT covers 06:00 PT yesterday to 06:00 PT today, not a clean calendar day either.

3. **Bucket counts were inconsistent across buildings for the identical call shape.** One Summerlin and Meridian sensors all returned `"count":25` (25 hourly buckets); Two Summerlin sensors all returned `"count":24`. Same `period:_1day, aggregation:hourly`, same run, no clear reason in the tool's response for the discrepancy — worth a platform question, not something this agent can resolve from its own sense budget.

4. **Rule 2 has no defined behavior for a Saturday-reported run.** Rule 2's One Summerlin logic is written explicitly for "held flat all Sunday" and "had not come down by 09:00 on a weekday." The reported day here is Saturday — neither clause fires, and the spec does not say what, if anything, Rule 2 should check on a Saturday (the Tier B intro only says the plant is "reduced on Saturday," it does not give Rule 2 a Saturday branch). I treated Rule 2 as not evaluable today by strict reading, but this is a real gap, not a deliberate skip like Tier B's.

5. **No building has a defined occupied window on Saturday, so Rule 1 could not fire regardless of the numbers.** All three buildings' occupied windows in the threshold table are qualified "weekdays." One Summerlin's 15 comfort sentinels sat 2.4-2.6 F above their nominal 70.5-74.5 F band all day, flat, all 24 hours — a pattern that would be a slam-dunk 🔴 on a weekday but, per the letter of the spec, is just "unoccupied drift... not a finding" on a Saturday. I did not flag it as a Rule 1 finding, per the orchestrator's instruction to apply the spec's own logic, but the flatness of that above-band reading across 15 units all day, all landing within about 0.3 F of each other, reads less like real "drift" and more like the plant sitting at some fixed reduced-capacity floor. The spec gives no rule to talk about that distinction; it only has "occupied-window in-band" and "unoccupied, ignore."

6. **The "identical value across 24h = frozen sensor" sentinel rule does not obviously apply to binary/presence points.** Two Summerlin's two `Occupancy Input` probes and Meridian's two `ComSensor 1 Motion` probes all read exactly 0.00 for every one of 24-25 hourly buckets. By the letter of the sentinel table this is "frozen... exclude, report." But applying that mechanically would flag every legitimately-unoccupied binary sensor as broken. For Meridian's motion sensors (the one real occupancy sense on the campus) a flat 0 on an actually-empty Saturday is the *correct* reading, and its steadiness is reassuring, not alarming. For Two Summerlin's `Occupancy Input` the same flat-0 pattern is exactly the ambiguity Rule 2 already calls out (130/132 read inactive at the 06/29 scan) — this run's probe cannot add anything because Saturday is the one day where "the point is broken" and "the building is empty" produce an identical signal. **A probe of these two points needs to happen on a weekday to be informative at all; probing them on a Saturday, as this run's schedule required, tells you nothing new.**

7. **Rule 5's "newest observationTime per building" cannot be produced from the Tier A call list as written for two of the three buildings on a routine day.** Tier A specifies `latest` calls only for the dark canaries (One Summerlin J2-2, Meridian RTU-14-A/23-A); Two Summerlin has no `latest` call at all in Tier A (its dark canary, a floor-1 VAV, is an open binding per checklist item 4/5). To give Rule 5 an actual timestamp for Two Summerlin I added one `get-sensor-latest-data` call not in the Tier A list. For One Summerlin and Meridian's non-canary sentinels, and for all of Two Summerlin's comfort/occupancy sentinels, I have no raw `observationTime` at all — only an hourly bucket that is non-null as of call time, which is not the same claim. I did not fabricate ages for those; the roster table above says "not fetched" rather than inventing a number.

8. **Deploy checklist item 1's expectation ("expect AHU-J1-7 to be dead at 8.96 F") did not hold.** The sensor returned a normal, tightly-clustered 76.9-77.14 F for all 24 buckets today. Either it was fixed between the 07/03 scan (the CSV's cached sample) and today, or the 8.96 F reading was itself a one-off transient rather than a persistently dead sensor. Per the spec's own anti-fabrication rule ("audit yesterday... retract in CHANGED"), I retracted the assumption rather than silently keeping the "known dead" label. No swap was needed since the sensor answered.

9. **A large, coherent RATemp excursion at 5 of 9 Meridian Bldg B RTUs (up to 100.41 F) had nowhere to go in the rule set.** It is too large a swing to ignore, but Rule 1 does not apply (no occupied window on Saturday) and there is no other rule that covers "the comfort proxy itself moved a lot, whether or not it's a finding." I put it in WATCH by judgment call, not because a rule told me to.

### What I would change in v0.2

- Give Two Summerlin an explicit `latest` canary sensor in Tier A (not just the comfort sweep) so Rule 5 does not need an off-list call to be satisfiable for that building.
- Add a Saturday branch to Rule 2, or explicitly say "Rule 2: ⚪ not evaluable, reported day is Saturday" as a named state, rather than leaving it to be inferred from the absence of a matching clause.
- Note in the sentinel table that "identical value across 24h = frozen" should exclude binary/presence points, or add a separate rule for those (e.g. "flag only if flat AND the building's real occupancy proxy elsewhere disagrees").
- Correct the Two Summerlin Celsius-storage claim against a fresh live probe before the next real run — either the tool changed behavior since the 07/23 audit, or that audit was against a different code path. Either way, the spec is currently wrong on a load-bearing unit-conversion claim.
- State plainly in the spec that `_1day` is a trailing-24h call, not a calendar day, and give the agent explicit instructions for handling the last few contaminated buckets (exclude them from any "all day" claim, or don't request `_1day` at all for a 06:00-run agent — request `_3days` and slice).
- Consider whether the flat "2.4-2.6 F above band, identical across 15 units" One Summerlin pattern deserves its own named state distinct from ordinary "unoccupied drift" — e.g. "reduced-capacity floor," even if still not dispatched as a finding.

### Token estimate (estimate)

Roughly 41 hourly-aggregated calls at approx. 24-25 float values each (about 1.8 tokens/value per the spec's own estimate, plus JSON overhead per call of maybe 40-60 tokens) puts each hourly response at very roughly 90-140 tokens; call it approx. 4,500-5,500 tokens for the 41 hourly calls combined. The 6 `latest` calls are tiny, maybe 30-40 tokens each, approx. 200 tokens total. Total tool-result tokens consumed this run: **estimate approx. 5,000-6,000 tokens** — well inside the spec's "approx. 300k token" budget ceiling for a full Tue-Sat run, and consistent with the spec's claim that aggregation, not raw, is what keeps this agent cheap.

---
---

# Round 2 — v0.2, run 09/06/2026 07:40 PT (Sonnet subagent, 45 calls)

Orchestrator verification: independent `hourly _3days` fetches of AHU-J2-5 space temp (Sat slice min/max
72.98/76.65), J1-9 CW entering (Sat peak-window max 79.12, day max 79.22) and Two Summerlin VAV 5-01
(70.65/73.03, unit Fahrenheit) all matched the report exactly. PASS on data, units, slicing, budget.
Defects were wording: header printed the run day not the reported day; WATCH line narrated the rule;
set-property-owner-id left out of the call count; Rule 2's Saturday exception was one-directional so the
J2-5 dip could only be a WATCH. Fixed in v0.3.

# Downtown Summerlin campus embodied agent — hand rehearsal, v0.2

Run executed 09/06/2026 approx. 07:40 PT, against live ProptechOS MCP tools.

## 1. The report, verbatim

```
REPORT-START:
Downtown Summerlin v0.2 · 09/06 · OK · Saturday hold clean campus-wide; Meridian Bldg A canary confirmed live again after its long dark stretch.

One Summerlin   OK: comfort ⚪ no window on Sat · Sat hold approx. 77 F on 14/15 units, AHU-J2-5 ran 1-4 F cooler (see WATCH) · Tier B skipped, Sunday run · loop 79.1 F peak · electricity ⚪ unbound · J2-2 dark day 30
Two Summerlin   OK: comfort ⚪ no window on Sat · 8/8 VAVs returned, 69.7-74.2 F range · floors 1-2 ⚪ dark, canary not yet bound
Meridian        OK: comfort ⚪ no window on Sat · 9/9 RTUs, 4/4 VAVs returned · Bldg A 2/9 points live
WATCH: AHU-J2-5 space temp ran 1-4 F below its 14 siblings for part of Saturday (72.98-76.65 F vs siblings' 76.9-77.14 F). Rule 2's Saturday exception is written only for drift above siblings, so this is not classified as a finding.
CHANGED: Meridian Bldg A RTU-14-A and RTU-23-A reported live again today (fresh obs 07:17 PT); 2 of 9 Bldg A points are now live, both were dark before today.
DISPATCH: MINOR, daily report and the Bldg A all-clear signalled by EMAIL. Nothing met SEVERE or MAJOR.
· ran 09/06/2026 07:40 PT · window 09/05 07:00Z–09/06 07:00Z · newest obs 14:30Z · v0.2 · 45 calls
REPORT-END
```

## 2. Rehearsal notes

### Sentinel roster

All calls used `period: _3days, aggregation: hourly` unless marked `latest`. Unit
field is the payload's literal `unit` value (I've shortened the REC-ontology
URL to its last segment). "Sat min/max" is the slice at indices 41-64 of the
73-bucket array (see slice section below). Two Summerlin's Occupancy Input
probes (VAV 3-03D, VAV 5-01) were **not called** — Rule 2 gates them to
Mon-Fri reported days only, and the reported day here is Saturday.

**One Summerlin (Bldg J)** — property owner `3edc18ee`

| Device | Point | UUID8 | Call | Unit | Returned | Sat min/max | Flag | Verdict |
|---|---|---|---|---|---|---|---|---|
| AHU-J1-9 | Space Temp Active | 7825d1ce | hourly | Fahrenheit | yes | 76.92/76.96 | none | 🟢 |
| AHU J2-9 | Space Temp Active | 6d581cad | hourly | Fahrenheit | yes | 77.01/77.05 | none | 🟢 |
| AHU J1-8 | Space Temp Active | cbb1c93d | hourly | Fahrenheit | yes | 76.92/76.97 | none | 🟢 |
| AHU J2-8 | Space Temp Active | 84ba38f7 | hourly | Fahrenheit | yes | 77.02/77.06 | none | 🟢 |
| AHU-J1-7 | Space Temp Active | 5a237e01 | hourly | Fahrenheit | yes | 76.97/77.05 | none (07/03 sentinel value 8.96 F not repeated) | 🟢 |
| AHU-J2-7 | Space Temp Active | 3d0bc058 | hourly | Fahrenheit | yes | 77.03/77.08 | none | 🟢 |
| AHU-J1-6 | Space Temp Active | 68357ff3 | hourly | Fahrenheit | yes | 76.96/77.00 | none | 🟢 |
| AHU-J2-6 | Space Temp Active | de1f0a05 | hourly | Fahrenheit | yes | 76.90/76.94 | none | 🟢 |
| AHU-J1-5 | Space Temp Active | 050d576a | hourly | Fahrenheit | yes | 77.10/77.14 | none | 🟢 |
| AHU-J2-5 | Space Temp Active | d50e2f53 | hourly | Fahrenheit | yes | 72.98/76.65 | anomalous — big swing earlier in the 3-day window (62.6→76.7 F) and a single-hour dip to 72.98 F Sat 06:00 PT | 🟡 WATCH (not a rule-defined finding) |
| AHU-J1-4 | Space Temp Active | 9a35d5f6 | hourly | Fahrenheit | yes | 76.05/76.26 | none | 🟢 |
| AHU-J2-4 | Space Temp Active | fab30dc3 | hourly | Fahrenheit | yes | 76.94/77.00 | none | 🟢 |
| AHU-J1-3 | Space Temp Active | c830856f | hourly | Fahrenheit | yes | 76.97/77.02 | none | 🟢 |
| AHU-J2-3 | Space Temp Active | aa89a2b8 | hourly | Fahrenheit | yes | 77.02/77.07 | none | 🟢 |
| AHU J1-2 | Space Temp Active | 620cead6 | hourly | Fahrenheit | yes | 77.02/77.08 | none | 🟢 |
| AHU-J1-9 | Condenser Water Entering | 81bea6d9 | hourly + latest (STEP 0 probe, reused) | Fahrenheit | yes | 73.03/79.22 (peak-window 11-16 PT: 79.12) | none, <92 F loop-hot threshold | 🟢 |
| AHU-J2-2 | Space Temp Active | 19a8674f | latest only | (no unit on `latest`) | yes, but stale | obs 2026-08-07T16:09:30Z | dark canary, day 30 | ⚪ dark, unchanged |

**Two Summerlin** — property owner `3edc18ee` (twin `1fe2668e`)

| Device | Point | UUID8 | Call | Unit | Returned | Sat min/max | Flag | Verdict |
|---|---|---|---|---|---|---|---|---|
| VAV 3-03D | Space Temperature Local | 457437a8 | hourly + latest (Rule 5 witness) | **Fahrenheit** (CSV says degC) | yes | 70.75/71.18 | served F again, as on 09/06 rehearsal record | 🟢 |
| VAV 3-03E | Space Temperature Local | 70e59bce | hourly | Fahrenheit | yes | 69.66/70.50 | none | 🟢 |
| VAV 4-01 | Space Temperature Local | bbfff796 | hourly | Fahrenheit | yes | 72.47/73.85 | none | 🟢 |
| VAV 4-02 | Space Temperature Local | 543bbba1 | hourly | Fahrenheit | yes | 71.52/74.00 | none | 🟢 |
| VAV 5-01 | Space Temperature Local | 3a14eda4 | hourly | Fahrenheit | yes | 70.65/73.03 | none | 🟢 |
| VAV 5-03 | Space Temperature Local | 36ecd128 | hourly | Fahrenheit | yes | 73.79/74.21 | none | 🟢 |
| VAV 6-01 | Space Temperature Local | e8910cd3 | hourly | Fahrenheit | yes | 71.96/74.06 | none | 🟢 |
| VAV 6-03 | Space Temperature Local | da532bbb | hourly | Fahrenheit | yes | 71.02/73.35 | none | 🟢 |
| VAV 3-03D | Occupancy Input | 12302d49 | **not called** | — | — | — | gated to Mon-Fri reported days | ⚪ skipped by rule |
| VAV 5-01 | Occupancy Input | 741fc590 | **not called** | — | — | — | gated to Mon-Fri reported days | ⚪ skipped by rule |

**Meridian (Los Angeles)** — property owner `3edc18ee` (twin `10619790`)

| Device | Point | UUID8 | Call | Unit | Returned | Sat min/max | Flag | Verdict |
|---|---|---|---|---|---|---|---|---|
| RTU-02-B | RATemp | 0af1286f | hourly + latest (Rule 5 witness) | Fahrenheit | yes | 71.15/81.06 | none, plausible RATemp | 🟢 |
| RTU-03-B | RATemp | 523df772 | hourly | Fahrenheit | yes | 73.63/77.73 | none | 🟢 |
| RTU-04-B | RATemp | 10c26f9b | hourly | Fahrenheit | yes | 71.53/77.66 | none | 🟢 |
| RTU-05-B | RATemp | b9a909ba | hourly | Fahrenheit | yes | 71.18/94.95 | midday plenum-heat spike, house rule: fan-off RATemp 90-100 F on a weekend afternoon is normal, never a WATCH | 🟢 |
| RTU-06-B | RATemp | 6ba3bfa0 | hourly | Fahrenheit | yes | 70.42/95.70 | same plenum-heat pattern | 🟢 |
| RTU-107-B | RATemp | e8a87ccd | hourly | Fahrenheit | yes | 72.15/100.41 | same, largest of the nine (peaked 100.41 F at 15:00 PT) | 🟢 |
| RTU-08-B | RATemp | 2b25b777 | hourly | Fahrenheit | yes | 71.68/95.06 | same plenum-heat pattern | 🟢 |
| RTU-09-B | RATemp | a24834bb | hourly | Fahrenheit | yes | 69.65/74.59 | none, mild profile | 🟢 |
| RTU-11-B | RATemp | cbdde6d3 | hourly | Fahrenheit | yes | 72.61/80.52 | mild plenum-heat pattern | 🟢 |
| VAV_01 | UNITOUCH SpaceTemp | 7f6d4899 | hourly | Fahrenheit | yes | 72.18/75.42 | none | 🟢 |
| VAV_B05_01 | UNITOUCH SpaceTemp | afbf933a | hourly | Fahrenheit | yes | 72.65/81.65 | warmed into the afternoon, in family with RTU RATemp pattern | 🟢 |
| VAV_B08_01 | UNITOUCH SpaceTemp | 13cafeff | hourly | Fahrenheit | yes | 70.89/79.82 | same | 🟢 |
| VAV_02 | UNITOUCH SpaceTemp | bcb14fc1 | hourly | Fahrenheit | yes | 70.83/74.84 | none | 🟢 |
| VAV_01 | ComSensor 1 Motion | 96684559 | hourly | BooleanDetection (binary) | yes | flat 0 all 73 buckets | flat-0 exempt from frozen rule; empty building on a weekend | 🟢 confirms unoccupied |
| VAV_B05_01 | ComSensor 1 Motion | 91a21e9e | hourly | BooleanDetection (binary) | yes | flat 0 all 73 buckets | same | 🟢 confirms unoccupied |
| RTU-14-A | RATemp | 49612aa0 | latest only (Bldg A canary) | (no unit on `latest`) | **yes, fresh** | obs 2026-09-06T14:17:22Z, value 78.25 F | **CHANGED** — live again today, was dark since 07/13 | 🟢 recovered |
| RTU-23-A | RATemp | 218cb864 | latest only (Bldg A canary) | (no unit on `latest`) | **yes, fresh** | obs 2026-09-06T14:17:10Z, value 70.36 F | **CHANGED** — live again today, was dark since 07/13 | 🟢 recovered |

Sentinels fetched this run: 42 (44 Tier A sentinels minus the 2 Two Summerlin
Occupancy Input probes correctly skipped for a Saturday reported day).

### The exact slice

Every hourly call returned `start: "2026-09-03T14:00:00Z"`, `interval: "PT1H"`,
`count: 73` — identical across all three buildings' connectors on this run (I
did not see the "24 vs 25 buckets" divergence the spec warns about).

- Raw start/count for one sensor per building:
  - One Summerlin (AHU-J1-9 space temp, `7825d1ce`): `start=2026-09-03T14:00:00Z`, `count=73`
  - Two Summerlin (VAV 3-03D, `457437a8`): `start=2026-09-03T14:00:00Z`, `count=73`
  - Meridian (RTU-02-B, `0af1286f`): `start=2026-09-03T14:00:00Z`, `count=73`
- Saturday PT slice = bucket index 41 through 64 inclusive (0-based):
  index 41 = `2026-09-05T07:00:00Z` (00:00 PDT Sat), index 64 = `2026-09-06T06:00:00Z`
  (23:00 PDT Sat). 24 buckets landed in the slice for every sensor in every
  building — no off-by-one seen this run.
- Buckets 65-72 (8 buckets) are today (Sunday, so far) and were used for
  nothing except sanity-checking the `latest` freshness witnesses.

### Call count by tool

| Tool | Calls |
|---|---|
| `set-property-owner-id` | 1 (STEP 0) |
| `get-sensor-latest-data` | 6 (STEP 0 probe/J1-9 CWE witness, J2-2 canary, 3-03D witness, RTU-02-B witness, RTU-14-A canary, RTU-23-A canary) |
| `get-sensor-historical-data` | 39 (15 One Summerlin space temps + 1 J1-9 CWE loop + 8 Two Summerlin VAVs + 9 Meridian RTUs + 4 Meridian VAVs + 2 Meridian motion) |
| **Total printed in report** | **45** (latest + historical only, matching the spec's own convention — I did not count `set-property-owner-id` toward the footer figure, since the "approx. 46/47/48 calls" budget language in the spec only reconciles against sensor-data calls) |

No expansion calls were made — no Tier A sentinel crossed a rule-defined
threshold that licenses expansion (AHU-J2-5's anomaly is below-siblings, which
Rule 2's Saturday exception does not define as a trigger; see below).

### Where the spec was ambiguous, wrong, or impossible to follow literally

1. **Rule 2's Saturday exception only covers drift ABOVE siblings.** Spec:
   *"A unit that **did not** hold with its siblings (drifted > 3°F above them)
   is the Saturday exception → 🟡, name the unit."* AHU-J2-5 spent part of
   Saturday running **1-4°F below** its 14 siblings (72.98-76.65 F vs
   76.9-77.14 F) and showed a much larger swing earlier in the 3-day window
   (62.6 → 76.7 F, plus an 11-hour near-flat stretch Thursday evening — not
   quite the 24h-identical frozen-sensor threshold, but close). The letter of
   the rule gave me no finding to raise, only a WATCH. I was tempted to
   promote this to 🟡 by symmetry with the "above" case, but the spec is
   explicit about direction and I didn't want to invent a threshold it never
   set. **This deserves a v0.3 decision**, not a workaround.
2. **Rule 4 (loop, all day) has no Saturday carve-out**, unlike Rules 1/2/3.
   The "peak window 11:00-16:00 PT" is defined only in the Schedule section as
   a property of "yesterday" generically, for a plant that is normally most
   loaded then — but Saturday is explicitly a reduced/setback day, so a
   weekday-shaped peak window may not describe Saturday's real load curve. I
   used the peak-window max (79.12 F) for the report line, per the rule's
   literal instruction, but the Saturday full-day max was 79.22 F — both are
   far under the 92 F threshold, so it made no difference in classification.
   Would matter more on a day close to threshold.
3. **The version-history's own "47 calls" figure does not reconcile with v0.2's own gating.** Line 8 of the spec: *"Updated ... v0.2 after the first hand rehearsal (Sunday run, 47 calls, all 44 sentinels answered ...)"* — but v0.2's own Rule 2 text (a few lines later in the same file) gates the Two Summerlin Occupancy Input probes to weekday-only reported days. A Sunday run (Saturday reported day) run under v0.2's own rules should skip those 2 calls and land at 45, not 47, and should report 42 sentinels answered, not 44. I followed the *current* rule text literally (skip the 2 probes, 45 calls) rather than the historical count in the front matter, since the front matter is describing a *prior* rehearsal that presumably predated the weekday-gate refinement. Flagging so the front matter can be corrected or the discrepancy explained.
4. **Two Summerlin's "floors 1-2 dark, day N" line has no sensor to prove it.** The 71 dark VAVs are documented in [MY SENSES] and the floor-1 canary UUID is explicitly still unbound (checklist item 5). I could compute a day count from the written date (06/23/2026 → day 75), but nothing was fetched this session to support it — it's asserted context, not observed. I chose to print "canary not yet bound" instead of a day count, to keep ANTI-FABRICATION rule 5 ("no number without a fetch") honest. The template line format implies a day count belongs there once the canary exists; until then I think the day-count field should simply be absent, which is what I did.
5. **Report-format ambiguity when Tier B is skipped.** The template's One Summerlin OK line has two separate clauses — `plant ran HH-HH <or Tier B skipped, Sunday run>` and, immediately after, `N units visited, <imbalance/none>`. On a Sunday run only the first clause has an alternate form written for it; the second (units-visited) has no alternate. I collapsed both into the single "Tier B skipped, Sunday run" phrase rather than also printing "0 units visited," since a literal "0 units visited, none" reads like a null finding rather than a skip. Worth spelling out explicitly in v0.3.
6. **Footer "newest obs HH:MMZ" is a single slot but there are three witnesses.** One Summerlin's witness (J1-9 CWE) read 14:19:16Z, Two Summerlin's (3-03D) read 14:30:46Z, Meridian's (RTU-02-B) read 14:17:22Z. I printed only the freshest across all three (14:30Z) since the template gives one slot. A reader can't tell from the footer alone that all three are actually fresh; I judged the per-building OK lines don't have room for it either given the 24-line cap, so it's implicit rather than stated.
7. **AHU-J2-5's earlier-window anomaly (Wed/Thu) is outside the reported day** and I did not expand into it — Rule 1 is ⚪ on the reported day (Saturday) and expansion is licensed by a Tier A finding on the *reported day*, not on other days visible in the `_3days` sweep. I mention it in the WATCH line only because it's visible in data I already have (no extra call), not because I expanded.

### What I would change in v0.3

- Decide whether Rule 2's Saturday exception should also fire on a unit
  running meaningfully *below* its siblings (AHU-J2-5's case), or explicitly
  say it's intentionally one-directional and why.
- Either state a Saturday-specific peak window for Rule 4, or say plainly
  that the weekday 11:00-16:00 PT window is reused as-is for every day
  including Saturday.
- Correct or annotate the "47 calls, 44 sentinels" figure in the version
  history so it doesn't conflict with the weekday-gate that same version
  introduces for Two Summerlin's Occupancy Input probes.
- Spell out the report-line phrasing for a skipped-Tier-B run so "units
  visited" isn't left dangling.
- Either bind the Two Summerlin floor-1 canary (checklist item 4) or drop the
  "day N" placeholder from the Two Summerlin OK line template until a sensor
  exists to justify one.
- Nothing else — the rest of the run followed the spec cleanly: STEP 0/401
  policy, the slicing math, unit handling (Two Summerlin served °F again, as
  predicted), the sentinel table, and the Bldg A canary recovery all worked
  exactly as written.

### Estimated tokens of tool results consumed

Estimate: approx. 6,000-6,500 tokens. 39 historical calls at roughly 73 values
+ metadata (~150-180 tokens each) ≈ 5,900-7,000 tokens, plus 6 cheap `latest`
calls (~20-30 tokens each) ≈ 150 tokens. This lines up with the spec's own
"approx. 6k tokens of tool results" figure for a Sun-Mon budget run.

---
---

# Round 3 — v0.3, run 09/06/2026 08:05 PT (Sonnet subagent, 54 calls incl. 8-call expansion)

Orchestrator verification (independent fetches 15:26Z): J2-5 CW entering at Sat 06:00 PT = 76.43,
CondSat C2 = 82.26, CondSat C3 = 84.89 → lifts 5.83 and 8.46 F, exactly as reported. The series further
show circuits 2 and 3 RUNNING Sat 06:00–13:00 PT (CondSat C3 approx. 90 F for 7 buckets), off from 13:00.
Evap leaving C3 during the Saturday run: 35.90 / 35.54 / 36.13 F — above the 35.0 F provisional frost line.
On Thu 09/03 and Fri 09/04 the same circuit read 32.04–34.84 F in several running buckets: a 3b hit on
days this run was not reporting (the Friday-rotation visit would have owned it). PASS: verdict NOT OK,
finding correct, dispatch text in house format, no rule names in the report, 14 lines, footer complete.
Wording nits → v0.4 (report running span in hours, expansion = all 8 points, denominator, CHANGED baseline,
omit empty WATCH). v0.4 is wording-only and has not been re-run.

# Downtown Summerlin campus embodied agent — hand rehearsal v0.3, run 3

Run: Sunday 09/06/2026 approx. 08:05 PT (15:05 UTC), reported day Saturday 09/05/2026.

## The report, verbatim

```
REPORT-START:
Downtown Summerlin v0.3 · 09/05 · NOT OK · one unit briefly cooled outside its Saturday hold; rest of campus steady, senses fresh

NOT OK
- One Summerlin: AHU-J2-5 space fell to 72.98 F at 06:00 Sat while its 14 siblings held approx. 77 F all day.
- Circuits 2 and 3 read running by the derived gate at that hour (condenser sat 5.83 F and 8.46 F over entering water); confirm whether after-hours conditioning was scheduled for J2-5.

One Summerlin   OK: ⚪ no occupied window on a Saturday (15/15 sensed) · Sat hold 🟡 approx. 77 F on 14/15 units (J2-5 exception, above) · Tier B skipped, Sunday run · loop 79.12 F peak · electricity ⚪ unbound · J2-2 dark day 30
Two Summerlin   OK: ⚪ no occupied window on a Saturday (8/8 sensed) · floors 1-2 ⚪ canary unbound
Meridian   OK: ⚪ no occupied window on a Saturday (9/9 RTUs, 4/4 VAVs sensed) · Bldg A 2/9 points live
WATCH: none
CHANGED: Meridian Bldg A RTU-14-A and RTU-23-A reporting again after approx. 55 days dark; still only 2 of 9 Bldg A points bound.
DISPATCH: MINOR EMAIL "One Summerlin COOLING: AHU-J2-5 dipped to 72.98 F at 06:00 Sat, siblings held near 77 F. Circuits 2 and 3 ran per derived gate; confirm after-hours schedule."
· ran 09/06/2026 08:05 PT · window 09/05 07:00Z-09/06 07:00Z · newest obs J 14:35Z · Two 14:30Z · M 14:32Z · v0.3 · 54 calls
REPORT-END
```

## Rehearsal notes

### Sentinel roster

Building · Device · Point · UUID(8) · call · unit returned · value? · yesterday-slice min/max (°F unless noted) · flag · verdict

**One Summerlin**
| Device | Point | UUID8 | Call | Unit | Value? | Slice min/max | Flag | Verdict |
|---|---|---|---|---|---|---|---|---|
| AHU-J1-9 (723101) | Space Temp Active | 7825d1ce | hourly _3days | Fahrenheit | yes | 76.92 / 76.96 | none | 🟢 held |
| AHU J2-9 (723102) | Space Temp Active | 6d581cad | hourly _3days | Fahrenheit | yes | 77.01 / 77.05 | none | 🟢 held |
| AHU J1-8 (723104) | Space Temp Active | cbb1c93d | hourly _3days | Fahrenheit | yes | 76.92 / 76.97 | none | 🟢 held |
| AHU J2-8 (723105) | Space Temp Active | 84ba38f7 | hourly _3days | Fahrenheit | yes | 77.02 / 77.06 | none | 🟢 held |
| AHU-J1-7 (723107) | Space Temp Active | 5a237e01 | hourly _3days | Fahrenheit | yes | 76.97 / 77.05 | sentinel-suspect unit (8.96 F at 07/03 scan) | 🟢 alive, no repeat of sentinel |
| AHU-J2-7 (723108) | Space Temp Active | 3d0bc058 | hourly _3days | Fahrenheit | yes | 77.03 / 77.08 | none | 🟢 held |
| AHU-J1-6 (723110) | Space Temp Active | 68357ff3 | hourly _3days | Fahrenheit | yes | 76.96 / 77.00 | none | 🟢 held |
| AHU-J2-6 (723111) | Space Temp Active | de1f0a05 | hourly _3days | Fahrenheit | yes | 76.90 / 76.93 | none | 🟢 held |
| AHU-J1-5 (723113) | Space Temp Active | 050d576a | hourly _3days | Fahrenheit | yes | 77.10 / 77.14 | none | 🟢 held |
| AHU-J2-5 (723114) | Space Temp Active | d50e2f53 | hourly _3days | Fahrenheit | yes | **72.98 / 76.65** | **>3 F below sibling hold at idx47 (06:00 PT)** | 🟡 FINDING |
| AHU-J1-4 (723116) | Space Temp Active | 9a35d5f6 | hourly _3days | Fahrenheit | yes | 76.05 / 76.26 | own baseline runs ~0.9 F below the pack, stable all 3 days | 🟢 held (own hold) |
| AHU-J2-4 (723117) | Space Temp Active | fab30dc3 | hourly _3days | Fahrenheit | yes | 76.94 / 77.00 | none | 🟢 held |
| AHU-J1-3 (723119) | Space Temp Active | c830856f | hourly _3days | Fahrenheit | yes | 76.97 / 77.02 | none | 🟢 held |
| AHU-J2-3 (723120) | Space Temp Active | aa89a2b8 | hourly _3days | Fahrenheit | yes | 77.02 / 77.07 | none | 🟢 held |
| AHU J1-2 (723122) | Space Temp Active | 620cead6 | hourly _3days | Fahrenheit | yes | 77.02 / 77.08 | none | 🟢 held |
| AHU-J2-2 (723123) | Space Temp Active | 19a8674f | latest (dark canary) | Fahrenheit (implied) | yes, but stale | obs 2026-08-07T16:09:30Z, value 77.02 | dark since 08/07, day 30 | ⚪ still dark |
| AHU-J1-9 (723101) | CW Entering | 81bea6d9 | STEP0 probe latest + hourly _3days | Fahrenheit | yes | 73.03 / 79.22 (peak-window 11-16 PT max 79.12) | none, PROVISIONAL >92 F threshold not tripped | 🟢 loop normal |

**Two Summerlin**
| Device | Point | UUID8 | Call | Unit | Value? | Slice min/max | Flag | Verdict |
|---|---|---|---|---|---|---|---|---|
| VAV 3-03D | Space Temp Local | 457437a8 | hourly _3days + latest | **Fahrenheit** (CSV says degC) | yes | 70.75 / 71.18 | unit mismatch vs CSV, per spec trust payload | 🟢 |
| VAV 3-03E | Space Temp Local | 70e59bce | hourly _3days | Fahrenheit | yes | 69.66 / 70.43 | none | 🟢 |
| VAV 4-01 | Space Temp Local | bbfff796 | hourly _3days | Fahrenheit | yes | 72.47 / 73.85 | none | 🟢 |
| VAV 4-02 | Space Temp Local | 543bbba1 | hourly _3days | Fahrenheit | yes | 71.52 / 74.00 | none | 🟢 |
| VAV 5-01 | Space Temp Local | 3a14eda4 | hourly _3days | Fahrenheit | yes | 70.65 / 73.03 | none | 🟢 |
| VAV 5-03 | Space Temp Local | 36ecd128 | hourly _3days | Fahrenheit | yes | 73.79 / 74.21 | **start/count off by one bucket vs. the other 7** (start 15:00Z not 14:00Z, count 72 not 73) | 🟢, sliced by timestamp not index |
| VAV 6-01 | Space Temp Local | e8910cd3 | hourly _3days | Fahrenheit | yes | 71.96 / 74.06 | none | 🟢 |
| VAV 6-03 | Space Temp Local | da532bbb | hourly _3days | Fahrenheit | yes | 71.02 / 73.35 | none | 🟢 |

**Meridian**
| Device | Point | UUID8 | Call | Unit | Value? | Slice min/max | Flag | Verdict |
|---|---|---|---|---|---|---|---|---|
| RTU-02-B | RATemp | 0af1286f | hourly _3days + latest (Rule 5 witness) | Fahrenheit | yes | 71.15 / 81.06 | none | 🟢 |
| RTU-03-B | RATemp | 523df772 | hourly _3days | Fahrenheit | yes | 73.63 / 77.73 | none | 🟢 |
| RTU-04-B | RATemp | 10c26f9b | hourly _3days | Fahrenheit | yes | 71.53 / 77.66 | none | 🟢 |
| RTU-05-B | RATemp | b9a909ba | hourly _3days | Fahrenheit | yes | 71.18 / 94.95 | plenum spike 14:00-23:00 PT, recurring daily in the two prior days too | 🟢 exempt (unoccupied drift, fan off) |
| RTU-06-B | RATemp | 6ba3bfa0 | hourly _3days | Fahrenheit | yes | 70.42 / 95.70 | same plenum spike pattern | 🟢 exempt |
| RTU-107-B | RATemp | e8a87ccd | hourly _3days | Fahrenheit | yes | 72.15 / 100.41 | same pattern, brushes the 90-100 F band ceiling | 🟢 exempt |
| RTU-08-B | RATemp | 2b25b777 | hourly _3days | Fahrenheit | yes | 71.68 / 95.06 | same pattern | 🟢 exempt |
| RTU-09-B | RATemp | a24834bb | hourly _3days | Fahrenheit | yes | 69.65 / 74.16 | no spike this unit | 🟢 |
| RTU-11-B | RATemp | cbdde6d3 | hourly _3days | Fahrenheit | yes | 72.61 / 80.52 | mild afternoon rise only | 🟢 |
| RTU-14-A | RATemp | 49612aa0 | latest (Bldg A canary) | Fahrenheit | yes | obs 2026-09-06T14:32:40Z, value 79.61 | **live** (dark 07/13-09/06/2026, 55 d) | CHANGED — recovered |
| RTU-23-A | RATemp | 218cb864 | latest (Bldg A canary) | Fahrenheit | yes | obs 2026-09-06T14:32:38Z, value 70.36 | **live** (same recovery) | CHANGED — recovered |
| VAV_01 | UNITOUCH SpaceTemp | 7f6d4899 | hourly _3days | Fahrenheit | yes | 72.18 / 75.42 | none | 🟢 |
| VAV_B05_01 | UNITOUCH SpaceTemp | afbf933a | hourly _3days | Fahrenheit | yes | 72.65 / 81.65 | above house band, unoccupied | 🟢 (⚪ Rule 1 today) |
| VAV_B08_01 | UNITOUCH SpaceTemp | 13cafeff | hourly _3days | Fahrenheit | yes | 70.89 / 79.82 | none | 🟢 |
| VAV_02 | UNITOUCH SpaceTemp | bcb14fc1 | hourly _3days | Fahrenheit | yes | 70.83 / 74.84 | none | 🟢 |
| VAV_01 | ComSensor 1 Motion | 96684559 | hourly _3days | boolean detection | yes | flat 0.00 all 73 buckets | binary, exempt from frozen-sensor rule | 🟢 confirms empty building |
| VAV_B05_01 | ComSensor 1 Motion | 91a21e9e | hourly _3days | boolean detection | yes | flat 0.00 all 73 buckets | same | 🟢 confirms empty building |

STEP 0 control: `set-property-owner-id 3edc18ee-9c68-45e5-980c-d2c9bbf66063` succeeded; probe `81bea6d9` (J1-9 CW entering, latest) returned immediately, value 76.24, obs 2026-09-06T14:35:36Z. No 401, no retry needed.

### Expansion — J2-5, licensed by the Saturday-hold finding

Fetched the full Tier B point set for AHU-J2-5 (all 8 plant points, `hourly _3days`), sliced to the same buckets (idx 41-64, Saturday 09/05):

| Point | UUID8 | idx46 (05:00 PT) | idx47 (06:00 PT) | idx48 (07:00 PT) |
|---|---|---|---|---|
| CW Entering | adb600a3 | 72.73 | 76.43 | 78.47 |
| CondSat C1 | 34b22003 | 72.32 | 74.70 | 76.75 |
| CondSat C2 | d29f1209 | 73.54 | 82.26 | 86.12 |
| CondSat C3 | d896f707 | 73.82 | 84.89 | 90.17 |
| CW Leaving Active | 1caba290 | 72.67 | 81.04 | 84.37 |
| Evap Leaving C1 | a0803a38 | 75.37 | 56.81 | 52.71 |
| Evap Leaving C2 | 3df849b8 | 72.80 | 46.90 | 46.76 |
| Evap Leaving C3 | 6f95cda2 | 76.52 | 45.17 | 35.90 |

GATE 1 arithmetic (lift = CondSat − CW entering; RUNNING > 5.0 F, OFF < 3.0 F, between = indeterminate):
```
idx46 (05:00 PT): C1 72.32-72.73=-0.41 OFF · C2 73.54-72.73=0.81 OFF · C3 73.82-72.73=1.09 OFF
idx47 (06:00 PT): C1 74.70-76.43=-1.73 OFF · C2 82.26-76.43=5.83 RUNNING · C3 84.89-76.43=8.46 RUNNING
idx48 (07:00 PT): C1 76.75-78.47=-1.72 OFF · C2 86.12-78.47=7.65 RUNNING · C3 90.17-78.47=11.70 RUNNING
```
Circuits 2 and 3 turned on the same hour the space dipped to 72.98 F, and stayed on through 07:00 PT while the space recovered to 75.58 F. Circuit 1 stayed off throughout. Condenser approach at idx47 (CondSat − CW leaving): C2 = 82.26-81.04 = 1.22 F, C3 = 84.89-81.04 = 3.85 F — a 2.63 F spread, under the 3.0 F within-unit imbalance threshold, and in any case Rule 3's imbalance check is scoped to the peak window (11:00-16:00 PT), which this hour isn't, so I didn't raise it as a separate imbalance finding.

### Slice mechanics

Yesterday PT (09/05, PDT) = bucket-start timestamps `2026-09-05T07:00:00Z` through `2026-09-06T06:00:00Z` inclusive (24 hourly buckets), i.e. index 41 through 64 for every sensor whose `start` was `2026-09-03T14:00:00Z`.

One sensor per building, raw tool return:
- One Summerlin, AHU-J1-9 Space Temp Active (7825d1ce): `start":"2026-09-03T14:00:00Z"`, `count":73`
- Two Summerlin, VAV 3-03D Space Temp Local (457437a8): `start":"2026-09-03T14:00:00Z"`, `count":73`
- Meridian, RTU-02-B RATemp (0af1286f): `start":"2026-09-03T14:00:00Z"`, `count":73`

Exception found: Two Summerlin VAV 5-03 (36ecd128) returned `start":"2026-09-03T15:00:00Z"`, `count":72` — one hour later start, one fewer bucket than its seven siblings. I re-derived its index-41-64 slice by matching timestamps (`start + i*interval` = 07:00Z 09/05 → index 40 for this sensor, not 41), not by reusing the same index number blindly. Data in that slice was flat (73.79-74.21 F), so the mismatch didn't change the verdict, but it would have silently mis-sliced a day if I'd trusted position alone. This is exactly the gotcha the spec calls out.

### Call count by tool

```
set-property-owner-id            1
get-sensor-latest-data            6   (J1-9 CW entering — STEP0 probe, doubles as Rule 5 witness;
                                        J2-2 dark canary; VAV 3-03D Rule 5 witness; RTU-02-B Rule 5
                                        witness; RTU-14-A Bldg A canary; RTU-23-A Bldg A canary)
get-sensor-historical-data       47   (One Summerlin: 15 space temps + J1-9 CW entering = 16 Tier A,
                                        + 8-point J2-5 expansion = 24. Two Summerlin: 8 VAVs. Meridian:
                                        9 RTUs + 4 VAVs + 2 motion sensors = 15. 24+8+15 = 47.)
------------------------------------
TOTAL                             54
```
Tallied one-by-one against the transcript: **54 tool calls total.**

### Ambiguities, gaps, and where I was tempted to deviate

1. **"the Tier B point set for the unit in question" (Expansion, line ~292-293) is not fully specified.** It could mean the four points GATE 1 strictly needs (CW entering + 3× CondSat) or the complete plant point set for that unit (8 points: also CW leaving + 3× Evap leaving). I fetched all 8, reading "the Tier B point set" as the full per-unit set the Tue-Fri rotation would gather. That cost 8 calls instead of 4. I was tempted to fetch only the 4 GATE-1 points to save budget, but the phrase "the rest of THAT unit" (line 292) reads as licensing more than the bare minimum, so I fetched the full set. Worth pinning down in v0.4 so budget is predictable.
2. **The Saturday-hold denominator ("Sat hold approx. 77 F on N/15 units") — is the dark canary J2-2 part of the 15, or is 15 already "the daily comfort sentinels minus the dark canary"?** The bindings CSV tags J2-2 as `A daily latest only`, distinct from the 15 rows tagged plain `A daily`, so I read "15" as excluding J2-2 (which the Threshold/Rule2 example line "15/15 units" and the OK-line template's own "N/15" also imply, since J2-2 is tracked separately as "dark day N" on the same line). This is an inference, not a stated rule — flagging it because a different reader could count 16 and get a different denominator.
3. **Auditing "yesterday" with no persisted prior-report artifact in this session.** Anti-fabrication rule 3 asks me to compare this run against my previous report. This is my first run in this conversation; the only record of a prior state is the spec's own changelog (which says Bldg A canaries "reported live again 09/06" as an already-established fact) and Erik's memory notes. I chose to still print a CHANGED line for the Bldg A recovery, reasoning from the "Know your gaps → WHEN IT MOVES" rule (a dead sense that starts reporting is a real finding, independent of whether I have a diffable prior report object). I was tempted to omit CHANGED entirely for lack of a strict prior-report artifact to diff against, but the spec's gap-tracking rule reads as building the change-detection duty into the sentinel table itself (know the dark-since date, notice when it stops being true), not into a literal document diff, so I kept it.
4. **Rule 2's "cooler means it conditioned while the others did not" — I verified rather than assumed.** The rule licenses calling a >3 F-cooler excursion "conditioning," and I could have stopped there. I ran the actual GATE 1 expansion instead of asserting it, which confirmed two circuits were derived-RUNNING at that hour. Not a deviation, but worth noting I didn't take the rule's word for it against a real circuit state — I checked.
5. **Meridian RATemp plenum spikes (RTU-05/06/107/08-B, up to 100.41 F)** are large enough that a naive threshold reader would flag them. The spec's own "Unoccupied drift: anything ... 90-100 F on a summer afternoon is normal, never a WATCH" rule is unambiguous and I followed it, but this is the sharpest place in the whole run where NOT applying a rule literally (i.e., not reacting to a huge number) mattered — a good stress test that the rule held.
6. **First 40 characters of the DISPATCH summary.** I did not machine-count exactly 40 characters against the platform's actual subject-line truncation; I front-loaded the building name, state word, and equipment name in that order per the house format and trusted that satisfies the intent. This is a soft compliance gap I'm noting rather than a deviation.

I did not deviate from the spec on: DAILY_REPORT-on behavior, the hard tool whitelist, Tier B skip on a Sunday run, skipping the Two Summerlin Occupancy Input probe (Saturday is not a weekday), never fabricating a Rule 1 verdict on a Sat/Sun, never naming a Bldg J floor or a tenant, never using rule numbers/names in the report body, and the 401 policy (not triggered — no 401 occurred).

### What I'd change in v0.4

- Pin down whether unit-level expansion at Bldg J means the 4 GATE-1 inputs or the full 8-point plant set, so the ~72-call Tue-Sat budget line and the ~48-call Sun/Mon line are reproducible rather than dependent on how one reads "the rest of THAT unit."
- State explicitly whether the dark-canary unit counts toward or is excluded from the Tier A denominator printed on the OK line ("N/15", "N/9", "N/4"), since the CSV's own tiering makes this inferable but not stated.
- Give an explicit fallback rule for `CHANGED` when a rehearsal or restarted session has no persisted prior report to diff against — something like "treat the sentinel table's own dark-since dates as the baseline to diff a `latest` witness against, always," so the behavior doesn't depend on session continuity.
- Otherwise unchanged: data, units, slicing, thresholds and the GATE 1 math all held up exactly as v0.3 describes.

### Estimated tokens of tool results consumed

Estimate: approx. 47 historical hourly calls × approx. 130 tokens each (per the spec's own "72 buckets, approx. 1.8 tokens each" estimate) ≈ 6,100 tokens, plus 6 `latest` calls at approx. 20-30 tokens each ≈ 150 tokens, plus the `set-property-owner-id` acknowledgement (negligible). **Total estimate: approx. 6,300-6,500 tokens of tool-result payload** — this is an estimate, not a fetched number.

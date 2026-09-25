# Summerlin campus embodied agent — hand rehearsal 09/18/2026 (v0.4, first WEEKDAY reported day)

Rehearsal of `summerlin-campus-embodied-agent.md` v0.4 with `DAILY_REPORT on`, run by a Sonnet 5
subagent against the live ProptechOS MCP (three-tool whitelist honoured, nothing dispatched, no
writes). **Friday run at 00:06 PT**, reported day Thursday 09/17, Tier B rotation Fri = AHU-J2-5,
AHU-J1-4, AHU-J2-4. **73 calls · 17 min 10 s · approx. 220k tokens · 78 tool uses incl. 2 file reads.**

**Verdict: FAILED on one finding.** Three of four findings and both structural claims verified.
The fourth, the SEVERE, was false — and it is the one that would have been emailed. Spec bumped to
v0.5; **must be re-run before deploy.**

## Orchestrator verification (independent MCP fetches, 07:05–07:23Z, same run window)

| Claim in the report | Probe | Result |
|---|---|---|
| Two Summerlin 7 of 8 comfort VAVs dark since approx. 09/16 09:31Z, VAV 6-03 live | `latest` on VAV 3-03D, 6-01, 4-02, 6-03 | 3-03D 09:31:51Z, 6-01 09:31:49Z, 4-02 09:31:51Z on **09/16** — one shared minute across floors 3, 4, 6. VAV 6-03 **07:07:10Z 09/18**, live. **CONFIRMED.** Shared minute = panel/trunk event (the 06/23 SC-03 pattern), connector alive. |
| AHU-J2-5 circuit 3 evap leaving 33.68 F (10:00 PT) and 34.02 F (14:00 PT) while running | `6f95cda2` hourly, `d896f707` CondSat C3, `adb600a3` CW entering | Buckets 17Z = 33.68, 21Z = 34.02, also 13Z = 35.00. C3 lift 9.5–12.3 F 12Z–00Z → RUNNING all of 05:00–17:59 PT. **CONFIRMED, arithmetic exact.** |
| Circuits 2 and 3 active approx. 05:00–17:00 PT, circuit 1 idle | `34b22003` C1, `d29f1209` C2 | C1 lift −0.3 to −1.5 F all day → OFF. C2 alternates 78–90 F hour to hour (lifts 1.7 / 3.4 / 5.1 / 6.5 / 11.8 / 12.3) → **cycling**, not steady. C3 steady 86–91 F. **CONFIRMED with nuance** — "intermittently" undersells C3 and oversells C2. |
| Meridian RTU-107-B return air 76.59–85.10 F in the 08:00–17:00 PT window | `e8a87ccd` hourly | 15Z–00Z: 76.59, 78.16, 79.26, 81.07, 81.91, 82.93, 84.34, 85.10, 84.14, 83.64. **CONFIRMED.** Same shape on 09/15 and 09/16 (peaks 96.35 and 94.89), so a standing pattern, likely fan-off plenum heat as the report itself hedged. 🟡 with the FanSpd caveat is the right colour. |
| Loop 78.50 F peak | `81bea6d9` 18Z–23Z | 78.46, 78.50, 78.36, 78.50, 78.39, 78.14. **CONFIRMED.** |
| J2-2 dark, Bldg A canary live | `19a8674f`, `49612aa0` latest | 2026-08-07T16:09Z unchanged (day 42, report said 41); RTU-14-A 06:57:34Z live. **CONFIRMED.** |
| **"All 15 reporting spaces ran 76.31–77.08 F through 07:00–17:00 PT, 0.9–2.6 F above band, same as the two days before" → SEVERE** | `7825d1ce` J1-9, `9a35d5f6` J1-4, `fab30dc3` J2-4, `d50e2f53` J2-5, all 72 h | **FALSE FINDING.** J1-9: 76.90–76.96 F for 72 h. J1-4: 76.31–76.43 F for 72 h. J2-4: 76.95–77.03 F for 72 h. Plant on, plant off, 12 F setpoint step, no movement. **These points are not sensing.** J2-5 is the exception: 71.3–74.3 F during occupied hours on 09/15 and 09/16 (in band), then flat 76.65–76.86 all of 09/17 — it *stopped* sensing on the reported day. The "same as two days before" clause is true for the flat ones and false for J2-5. |
| Setpoint (not in report) | `d02a4e92` J2-5 setpoint hourly | **85.0 F unoccupied, 72.5 F 12Z–00Z (05:00–17:59 PT) on 09/15, 16, 17.** The BAS publishes its own occupied window. Adopted in v0.5 as the schedule witness. |

## Why the frozen rule missed it

v0.4's sentinel table said *"identical value across 24 h → frozen"*. Hourly means of a point that
jitters ±0.03 F are never identical, so a byte-identical reading passes. The 1700 lesson was the
same one ("a frozen sensor is a stable machine") and the fix is the same: **a range test**. v0.5
uses `max − min < 0.20 F over the 24 buckets → FLAT, excluded from Rule 1, never a 🔴`, and the OK
line carries `comfort N/N sensing · M flat`. At Bldg J the sensing denominator may be 1 or 2.

Open question for Erik / the site: is `Space Temperature Active` on the AHU-J units a BAS-written
value (the Trane `Local / BAS / Active` triplet, as with outdoor air) rather than a sensor? J2-5
moving for two days then freezing at 76.7 suggests the source can switch. Either way the campus has
no usable zone temperature at Bldg J until `Act_SpaceTemp` on the VAVs lands (OTEAM-6740 / PLAT-5581).

## What Sonnet did well

- Resolved the ambiguous Tier B table (one point per row) correctly to "all 8 points per unit" and
  said so in its notes. Table rewritten in v0.5 regardless.
- Found the Two Summerlin outage, cross-checked it with a `latest` call, substituted a live witness,
  and attributed it to the panel rather than the connector because one VAV survived. Exactly right.
- Dispatch text in house format, no rule names, no degree signs, no em dashes.
- 73 calls, under the 90 ceiling; 17 minutes; no 401s, no empty payloads.

## What it missed or got wrong

1. The false SEVERE (above). **Structural, fixed in v0.5.** Would have been the first email Erik got.
2. "Check loop capacity and staging" — a plant judgement the spec forbids. Fixed: action names the unit.
3. Rule 3a not evaluated on J2-5 (C2 vs C3 approach spread approx. 5 F on peak-window means). Debatable:
   C2 was cycling, so the spread is an artefact of hourly means. v0.5 makes that explicit — compare only
   both-RUNNING buckets, report cycling as its own line.
4. J2-5's space point going flat on the reported day is a CHANGED line it did not print.
5. J2-2 "day 41" — 08/07 to 09/17 is 41 days to the reported day, 42 to the run day. Acceptable.

## The report as delivered

```
REPORT-START:
Downtown Summerlin v0.4 · 09/17 · NOT OK · comfort is out of band across One Summerlin and most of Two Summerlin is dark

NOT OK
- One Summerlin: all 15 reporting spaces ran 76.31-77.08 F through the 07:00-17:00 PT window yesterday, 0.9-2.6 F above each unit's band, same as the two days before. Circuits ran only intermittently (AHU-J2-5 circuit 1 idle all day); check loop capacity and staging.
- Two Summerlin: 7 of 8 floor 3-6 comfort VAVs, including the usual witness 3-03D, have not reported since approx 09/16 09:31Z; floors 1-2 already dark since 06/23. Only VAV 6-03 live. Check the BAS panel or connector (HHHEG-003).
- One Summerlin: AHU-J2-5 circuit 3 evaporator leaving hit 33.68 F (10:00 PT) and 34.02 F (14:00 PT) while running. Provisional frost risk; recheck at next Friday visit.
- Meridian: RTU-107-B return air ran 76.59-85.10 F through the 08:00-17:00 PT window while its 8 Bldg B siblings held 69-77 F. FanSpd is not bound so a fan-off plenum reading cannot be ruled out; ask the BAS.

One Summerlin   comfort 0/15 in band · plant: circuits 2 and 3 active approx 05:00-17:00 PT on AHU-J2-5, circuit 1 idle; run gate derived (CondSat - CW entering > 5.0 F), vendor state not onboarded · 3 units visited (J2-5, J1-4, J2-4), no loop divergence · loop 78.50 F peak · electricity unbound · J2-2 dark day 41
Two Summerlin   comfort 1/8 (7 dark since approx 09/16) · floors 1-2 canary unbound
Meridian        comfort 8/9 RTUs (RTU-107-B flagged), 4/4 VAVs · Bldg A 2/9 points live day 12
WATCH: Meridian motion (VAV_01, VAV_B05_01) read inactive all day Thursday, a weekday; too early to conclude what the point means.
CHANGED: Two Summerlin floor 3-6 comfort VAVs, all live at the 09/06 rehearsal, are dark since approx 09/16 09:31Z except VAV 6-03. The freshness witness this file assumed alive, 3-03D, is one of the dark ones.
DISPATCH: EMAIL SEVERE "One Summerlin COMFORT: all 15 spaces ran 76-77 F, up to 2.6 F over band, all day Thursday. Check loop capacity and circuit staging."
DISPATCH: EMAIL MAJOR "Two Summerlin BLIND: 7 of 8 floor 3-6 VAVs dark since 09/16, only VAV 6-03 live. Check the BAS panel or connector."
· ran 09/18/2026 00:06 PT (07:06Z) · window 09/17 07:00Z-09/18 07:00Z · newest obs J 06:57Z · Two 07:07Z (VAV 6-03; 3-03D stale since 09/16) · M 06:58Z · v0.4 · 73 calls
REPORT-END
```

Sonnet's own notes: 1 set-PO + 7 latest + 65 historical = 73; no errors; it read the Tier B table as
all 8 points; it flagged the campus-wide 77 F as "possibly a standing condition never evaluated" but
reported it in full because nothing in the file said otherwise. That instinct was right; the file was
wrong. Fixed.

## What the corrected v0.5 report should have said (orchestrator's reading of the same data)

```
Downtown Summerlin · 09/17 · NOT OK · Two Summerlin went dark on 09/16; J2-5 circuit 3 ran at the frost line

NOT OK
- Two Summerlin: 7 of 8 floor 3-6 VAVs stopped at 09:31Z on 09/16, one shared minute; VAV 6-03 still reports so the connector is alive. Check the Tracer panels on HHHEG-003's BAS.
- One Summerlin: AHU-J2-5 circuit 3 evaporator leaving 33.68 and 34.02 F in two running hours, below the 35 F line. Circuit 2 cycled 06-17 PT, circuit 3 steady. Recheck next Friday.
- Meridian: RTU-107-B return air 76.6-85.1 F through the window, siblings 69-77. FanSpd unbound; ask whether the unit ran.

One Summerlin   comfort 0/0 sensing · 15 flat (space points not moving, see CHANGED) · setpoint occupied 05:00-17:59 PT · J2-5 c2 cycling, c3 steady, c1 off · loop 78.50 F peak · electricity unbound · J2-2 dark day 41
Two Summerlin   comfort ⚪ 7/8 dark · witness VAV 6-03 07:07Z
Meridian        comfort 8/9 RTUs, 4/4 VAVs · Bldg A 2/9 points live day 12
CHANGED: AHU-J2-5 space point moved 71-74 F on 09/15-16 and sat flat at 76.7 F all of 09/17 - it stopped sensing. The other 14 have been flat near 77 F for 3 days. Two Summerlin floors 3-6 dark since 09/16.
DISPATCH: EMAIL MAJOR "Two Summerlin BLIND: 7 of 8 floor 3-6 VAVs dark since 09/16 09:31Z, VAV 6-03 alive. Check the Tracer panels." · EMAIL MINOR for the two ambers.
```


---

# Round 5 — same run day, same data, spec v0.5 (00:39 PT, 76 calls, 28 min, approx. 250k tokens)

**PASSED the regression it was run for.** The false SEVERE is gone: all 15 Bldg J `Space Temperature
Active` points classified flat (`comfort 0/15 sensing · 15 flat`), AHU-J2-5's stopped-sensing event
printed as CHANGED, no comfort finding at Bldg J. Two Summerlin MAJOR and the J2-5 circuit-3 frost 🟡
reported identically to round 4; loop peak, J2-2, canaries all consistent. Every number in the report
matches the orchestrator's independent fetches from round 4 (no new data was needed).

## Two new defects, both escalation, both fixed in v0.6

1. **Meridian RTU-107-B promoted to 🔴 SEVERE, worded "overheating tenants", without a fan witness.**
   Round 4 held it at 🟡 with the fan-off caveat. After the run the orchestrator fetched `FanSpd`
   (`541a2fc2`, hourly, start 09/15 08:00Z): **0 % overnight, 42.5 % at 07:00 PT, 55–57 % from 08:00,
   tapering to 47 % at 17:00 PT, 0 % from 18:00** on 09/17, with the same shape on 09/15 and 09/16. So
   the fan WAS running while return air climbed 76.6 → 85.1 F: the unit is moving air it is not cooling,
   and a 🔴 is supportable. The defect is procedural and lexical, not factual: Sonnet escalated on return
   air alone (the witness was not bound, so it could not check) and wrote "tenants" for a duct sensor.
   v0.6: `RATemp` findings cap at 🟡 until `FanSpd` proves the unit ran; FanSpd + DischAirTemp for the
   9 Bldg B RTUs added to the bindings as expansion points (18 rows); verdict and dispatch lines may only
   use the sensor's words. **RTU-107-B is a genuine open item for the Meridian site: fan on, return air
   85 F, three days running.**
2. **`comfort 🔴 1/8` for the dark Two Summerlin.** Dark is ⚪, never a comfort colour. Now explicit.

## Judgement calls Sonnet made, and what they tell us

- J2-5's day range was 0.22 F against a 0.20 F flat line; it classified flat by following the spec's
  worked example over the number. Right call, wrong to have needed it — threshold now 0.50 F.
- AHU-J2-4 circuit 2 cycling (approach swinging 0.6–6.5 F on hourly means) correctly read as cycling,
  WATCH only, per the new 3a rule. Good.
- Meridian VAV_B08_01 at 68.72 F for one bucket at the 17:00 PT boundary, 0.3 F under band: omitted
  as marginal. Defensible; the spec's "brief breach → 🟡" would have allowed it. Left as is.
- Sliced each series by its own timestamps because `start` differed (07:00Z vs 08:00Z) between calls
  landing either side of the hour. Exactly what the spec asks; worth knowing the platform does this.
- Used the file's documented state as the CHANGED baseline and retracted "3 flat units" to 15. Correct
  use of the anti-fabrication audit rule.

## The report as delivered

```
REPORT-START:
Downtown Summerlin v0.5 · 09/17 · NOT OK · Meridian's RTU-107-B is overheating tenants, most of Two Summerlin is dark, and a Bldg J circuit hit the frost line.

NOT OK
- Meridian: return air on RTU-107-B climbed from 75.0F at 08:00 to 85.1F by 16:00 PT, out of band roughly 7 hours inside the occupied window.
  Check RTU-107-B's cooling/economizer operation.
- Two Summerlin: 7 of 8 space sensors dark since 09/16 09:31Z (about 46 hours), only the floor 6 VAV still reporting.
  Check the Tracer panel serving floors 3-6; connector HHHEG-003 itself is alive.
- One Summerlin: AHU-J2-5 circuit 3 evaporator leaving hit 33.7F at 10:00 PT and 34.0F at 14:00 PT while running, frost line (provisional).
  Check circuit 3 charge and airflow; circuit 1 was idle all day, circuit 2 cycled.

One Summerlin   comfort 0/15 sensing · 15 flat (incl. AHU-J2-5, which itself went flat today) · plant 🟡 ran 05-18, gate derived (vendor state not onboarded) · 3 units visited (J2-5/J1-4/J2-4), J2-5 circuit 3 frost risk, others no imbalance · loop 78.5F peak · electricity ⚪ unbound · J2-2 dark day 41
Two Summerlin   comfort 🔴 1/8 (7 of 8 dark since 09/16 09:31Z, floor 6 survives) · floors 1-2 ⚪ canary unbound
Meridian   comfort 🔴 8/9 RTUs (RTU-107-B out of band 75-85F), 4/4 VAVs in band · Bldg A 2/9 points live
WATCH: AHU-J2-4 circuit 2 showed the same cycling pattern as J2-5 today; both Meridian motion sensors read zero the entire weekday.
CHANGED: retracts the 3-flat-unit baseline: all 15 Bldg J Space Temperature Active points, including AHU-J2-5 (moved 71-74F on 09/15-16, now flat), read under 0.2F range on 09/17; comfort there is unmeasurable today, not a comfort finding.
DISPATCH: SEVERE EMAIL "Meridian COMFORT: RTU-107-B return air 75 to 85F, 7h out of band. Check RTU-107-B cooling."
DISPATCH: MAJOR EMAIL "Two Summerlin DARK: 7 of 8 space sensors unseen since 09/16, floor 6 survives. Check the Tracer panel."
DISPATCH: MINOR EMAIL "One Summerlin PLANT: AHU-J2-5 circuit 3 hit 33.7F while running, frost line. Check charge/airflow."
· ran 09/18/2026 00:39 PT · window 09/17 07:00Z-09/18 07:00Z · newest obs J 07:30Z · Two 07:47Z (witness swapped to VAV 6-03, 3-03D dark since 09/16) · M 07:44Z · v0.5 · 76 calls
REPORT-END
```

**Status after round 5: v0.6 is the deploy candidate.** The remaining risk is escalation wording, which
is now covered by two explicit rules, and the four open bindings (Cool Output, Veris, floor-1 canary,
PdM UUID). Cost per run approx. 75 calls, 250k tokens, 20-30 min under Sonnet 5.


---

# Round 6 — the FIRST PLATFORM RUN (agent `2498b6a2-0d1b-40a9-b47b-ace1582711c6`, "One Summerlin", type Embodied)

Created by Erik 10:53Z 09/18 with the v0.6 spec as system prompt (uploaded text identical to the repo file,
52,172 chars). Invoked manually 10:56Z. **Killed at 11:56Z by the 60-minute wall clock: 217 tool calls, model and
tokens null, no report.** Run dump pulled via `GET /agent/json/autonomousagent/{id}/message` with a gateway-swagger
token (a web-app token is refused on `/agent/`). Raw JSON kept in the session scratchpad `platform-run/`.

## What the 217 calls were

| tool | calls | by UUID | by name |
|---|---|---|---|
| list_memory | 1 | — | `pathPrefix "/"` (Troupe memory tool, injected; returned nothing) |
| set-property-owner-id | 1 | — | correct PO, once, no 401 loop |
| get-sensor-latest-data | 46 | 1 (the J1-9 probe) | 45 |
| get-sensor-historical-data | 82 | 0 | 82 |
| search | 60 | — | 60 — "RATemp" ×21, "3-03D" ×6, "Space Temperature Local" ×4, "RTU-02-B" ×4, "RTU-107-B" ×4, "VAV" ×4 … |
| fetch | 18 | 5 | 13 |
| get-assets / get-asset-by-ref / get-actuators-by-room | 9 | 6 | 3 |

Name-based sensor calls by building: One Summerlin 70, Meridian 38, Two Summerlin 9, unattributable 10. Bldg J
names like `AHU-J1-9 Space Temperature Active` match the live popularName convention and probably resolved; the
Meridian and Two Summerlin ones (`RTU-02-B RATemp`, `RTU-02-B Return Air Temp`, `RTU 02 B RATemp`, `VAV3-03D …`,
`VAV-3-03D …`) are guesses at names that do not exist, retried in variants. Tier B visited SIX units — the Friday
row (J2-5, J1-4, J2-4, 9 points each) AND the Thursday row (J1-6, J2-6, J1-5 in progress) — and was mid-sweep when killed.

## Root cause

**The uploaded prompt contained six UUIDs.** Every other sensor lived in `summerlin-campus-embodied-bindings.csv`,
which the spec told the agent to consult and which the platform agent cannot read. In every rehearsal the Sonnet
subagent had `Read` on that file; on the platform it had `search` and `fetch` instead, because the agent's tool
configuration was not restricted to the three-tool whitelist. Given a name and a search tool, it did the obvious
thing 78 times. Not a 401 loop (my first hypothesis, wrong), not a payload/timeout problem, not the model.

Two secondary defects the run exposed: the rotation row was read off the reported day as well as the run day, so
Tier B doubled; and no hard stop fired at 90 calls because the agent never reached a point where it counted.

## Fixes → v0.7 (78,726 chars, 233 UUIDs)

1. **[BINDINGS] section generated from the CSV and embedded in the prompt** — Tier A, canaries, Tier B per unit,
   expansion points, profile setpoints, excluded device — with the FLAT / dark notes carried as comments. The prompt
   is now the agent's whole sensor universe.
2. Tools: even when `search`/`fetch`/asset/room/memory tools are offered, they are not used. An unbound point is ⚪.
3. Rotation: the row is the RUN day, exactly three units, worked Friday example.
4. Hard stop at the 90th call: stop fetching, report with ⚪.
5. Noted: the Troupe injects memory tools (`list_memory` was the very first call). v0.7 does not use them; the
   `/memory` and `/memory/file` API endpoints mean the ledger design can be revisited deliberately.

## Platform config still to fix by hand (Erik)

- Restrict the agent's tools to set-property-owner-id, get-sensor-latest-data, get-sensor-historical-data.
- Trigger is DAILY 14:00:00 (UTC → 07:00 PDT); the spec says 06:00 PT = 13:00 UTC. Either is fine; make them agree.
- No DispatchConfig exists yet (`/dispatch` → 404 "no dispatchers"). EMAIL to Erik, then Reset.
- Model shows only "Anthropic"; confirm Sonnet 5 in the editor.


---

# Round 7 — v0.7 local, spec as the ONLY readable file (06:11 PT, 84 calls, 16 min, approx. 215k tokens)

Simulates the platform: no CSV, every UUID from [BINDINGS]. **Passed the point of the test** — Sonnet reported
"no UUID was needed outside [BINDINGS]", no name resolution, 84 calls under the 90 ceiling, and the eight
Meridian expansion points (FanSpd/DischAirTemp) were used exactly as v0.6 intended: RTU-107-B fan 42–57 % all
window → the 🔴 is now supported by the witness.

Verified against the orchestrator's own fetches: flat 15/15 at Bldg J, Two Summerlin 7/8 dark, J2-5 c3 frost
33.68/34.02, RTU-107-B 78–85 F with fan on, loop 78.50, J2-2 dark, canaries live. All correct.

**Two defects → v0.8:**
1. **Meridian VAV_B05_01 and VAV_B08_01 reported 🔴 "warm several hours midday into afternoon". FALSE.**
   Orchestrator fetch: both series `start` = 09/15 13:00Z (the call landed after 13:00Z), so the reported window is
   idx 42–65 and the occupied window idx 57–66. B05_01 occupied: 72.65–75.90 F, in band; it rose to 77–78 F only
   from 19:00 PT. B08_01 occupied: 67.98–71.43 F, two buckets at 16–17 PT marginally under 69 — at most a brief 🟡
   cold, and at the window edge. Sonnet read these with the offsets of a 07:00Z-start series (six hours off) despite
   the "slice by timestamp" rule; earlier runs happened not to hit a 13:00Z start. Fix: explicit per-series index
   arithmetic and a clock sanity check ("all out-of-band buckets after 17:00 PT = drift, not a finding"), with bucket
   times quoted in PT in every comfort finding.
2. **Only the SEVERE was dispatched.** Two Summerlin's MAJOR (blind building) was left in the printed report. Fix:
   one dispatch per severity class present, never fold MAJOR into SEVERE.
Also relaxed: the run-gate disclosure may be folded into the plant finding or OK line, must not be omitted.


---

# Rounds 8–10 — the v0.7 PLATFORM runs (pulled 14:32Z with a fresh gateway token)

| invocation (UTC) | prompt | outcome | calls | notes |
|---|---|---|---|---|
| 13:10:01 | v0.7 wrapped in a JSON object (bad upload) | **60-min wall-clock kill**, no report | 80, all UUID, all `_3days hourly` | `PUT /stop` at 13:11:02 did NOT abort it — it ran to 14:10 alongside the next one |
| 13:11:39 | v0.7 verified | **60-min wall-clock kill**, no report | 81, 1 name-based, all `_3days hourly` | ran concurrently with the one above; both slowed to approx. 44 s/call |
| **14:00:00 (scheduled DAILY trigger)** | v0.7 verified | **REPORT PRODUCED**, 18 min, `claude-sonnet-5`, 314,706 tok in / 41,834 out | 50: set-PO ×3, latest ×6, historical ×41 | all 44 Tier A sentinels by UUID in spec order; 401 fault after call 47 → PO retry ×2 → session declared dead per policy; Tier B, 2 Meridian VAVs, motion, Bldg A canaries ⚪ |

**What the platform confirmed:** the self-contained prompt works (zero `search`/`fetch`, zero name resolution,
`list_memory` not touched although injected); the 401 policy works exactly as written; Sonnet 5 on the platform
paces at approx. 22 s per call alone, so a full 84-call run needs approx. 30 min and two overlapping runs die.

**Report defects in the 14:00Z run → v0.8:** suppressed the RTU-107-B 🟡 as "same finding as prior runs" with no
prior report in context (dedup now only against a visible previous report); wrote `NOT OK:` as the building-line
label (label is the literal `OK:`); narrated the session death in the verdict line (verdict = buildings, ⚪ story =
CHANGED). Dispatched MAJOR for Two Summerlin — to no one, since no DispatchConfig exists yet.

**New observation from that run, verified by the orchestrator:** AHU-J2-5 `Space Temperature Active` fell from its
flat 76.7 F to **57.35 → 52.35 → 51.82 F from 12:00Z (05:00 PT) on 09/18**, latest 51.68 F at 14:20Z. A 52 F room is
not a room; it is the magnitude of the unit's discharge air (scan samples 52–61 F). The point's source appears to
switch — real space on 09/15–16, flat on 09/17, discharge-air-like today. For the site/Oksana, with the earlier question.

## The 14:00Z platform report as delivered

```
REPORT-START:
Downtown Summerlin v0.7 · 09/17 · NOT OK · Two Summerlin broadly dark (7/8 VAVs), Meridian RTU-107-B still running hot, this run's session died before Bldg J plant fetch and 6 sentinels.

NOT OK
- Two Summerlin: 7 of 8 floor 3-6 VAVs dark since 09/16 09:31Z (VAV 3-03D last value), only VAV 6-03 (Floor 6) still reporting. Check the Tracer SC panel or connector HHHEG-003.
- Meridian: return air on RTU-107-B ran 76.59-85.10 F through the whole 08:00-17:00 PT window on 09/17. FanSpd not checked this run (session failed first) - capped at potential, check RTU-107-B's cooling stages once fan run is confirmed.

One Summerlin   NOT OK: comfort 0/15 sensing, 15 flat (incl. J2-5, range 0.22 F) · plant Tier B NOT fetched, session failed before it started · loop 78.50 F peak (11:00-16:00 PT), under 92 F · electricity ⚪ unbound · J2-2 dark day 42
Two Summerlin   NOT OK: comfort 1/8 evaluable (VAV 6-03, 70.78-73.04 F, in band) · 7/8 dark day 2 · floors 1-2 canary ⚪ still unbound · occupancy probe flat 0 on both VAV 3-03D and VAV 5-01, both inside the dark set - inconclusive
Meridian        NOT OK: comfort 8/9 RTUs in band, RTU-107-B potential (above) · VAVs 2/4 evaluated (VAV_01, VAV_B05_01, both in band) · 2/4 VAVs and both motion sensors ⚪ auth error · Bldg A canaries ⚪ auth error, cannot confirm today's state

WATCH: AHU-J2-5 space point, flat approx. 76.7 F for days, dropped to 57.35/52.35/51.97 F in the last three hourly buckets today (09/18, not yet in the reported day) - watch tomorrow's report for whether this holds or is another sentinel value.
CHANGED: session failed with repeated authorization errors after 42 successful calls; one property-owner retry also failed, so the session is dead per policy. Everything after that point (Bldg J Tier B rotation for AHU-J2-5/AHU-J1-4/AHU-J2-4, 2 Meridian VAVs, both Meridian motion sensors, both Bldg A canary reads) is ⚪, not fetched, not zero.
DISPATCH: EMAIL MAJOR "Two Summerlin VAV floors 3-6 DARK: 7 of 8 space sensors dark since 09/16, only VAV 6-03 live. Check Tracer panel/connector HHHEG-003." | Meridian RTU-107-B potential suppressed, same finding as prior runs.
· ran 09/18/2026 07:12 PT (14:12Z) · window 09/17 07:00Z-09/18 07:00Z · newest obs J 14:03Z (fresh) · Two 09/16 09:31Z on named witness, swapped to VAV 6-03 (hourly data current to approx 14:00Z, exact latest not fetched) · M 14:11Z (fresh) · v0.7 · 50 calls
REPORT-END
```

# Round 11 — v0.8 (slicing + dispatch fixes, without the three report-rule edits above) uploaded, verified, reset and invoked SOLO at approx. 14:36Z (invocation fcacef50). Result below when it lands.


## Round 11 result — v0.8 solo platform run (invoked 14:34:33Z, finished 15:32:28Z)

**Report produced; content correct; runtime nearly fatal.** 88 calls · **57 min 55 s** · 1,000,947 tokens in
(UI showed 1,372,766 total) · claude-sonnet-5. Findings: RTU-107-B return air 79.3–85.1 F with fan 47–57 % AND
discharge air 57–62 F (the unit cools but cannot keep up) → SEVERE; Two Summerlin 7/8 dark → MAJOR; VAV_B08_01
67.98–69.39 F 14:00–17:00 PT → MINOR (matches the orchestrator's data exactly this time — the slicing fix held);
Bldg J 15 flat, Friday row visited, cycling on J2-5 c2 and J2-4 c2 correctly kept out of the imbalance math; loop
78.50 F. Missed: the J2-5 c3 frost buckets (33.68, 34.02) because it read "≥ 2 buckets" as consecutive. Layout in
the UI: building lines collapsed into one paragraph (single newlines).

**→ v0.9:** list layout (findings first; per building a header with its worst colour and one bullet per domain with
its own light, green included; blank line after every line); sweep on `hourly _1day` (25 buckets) instead of
`_3days` (72) — a run before 08:00 PT still holds all of yesterday's occupied and plant windows, and payload is
re-sent on every model round so this is the lever on the 57 minutes; the four occupancy/motion probes weekly
(Mondays); frost = any two sub-35 F buckets. Uploaded, verified identical (88,312 chars), reset, invoked solo
at approx. 16:36Z (invocation 452e7e2b).


---

# Round 12 — v0.9 solo platform run (invoked 16:34:15Z, finished 16:50:40Z) → v0.10

**78 calls · 16 min 24 s · 630,709 tokens in / 89,609 out · claude-sonnet-5.** The `_1day` cut took the run from
57 min 55 s to 16 min. All 66 historical calls `_1day hourly`. The list layout rendered in the UI. Frost on
AHU-J2-5 circuit 3 (33.68 / 34.02 F) raised as 🟡 and the v0.8 miss retracted in CHANGED. Late invocation (09:42 PT)
meant the trailing window missed Thu 08:00–09:00 PT; the footer said so.

**The agent built its own ledger, unasked.** The v0.8 run had ended with `list_memory` + `write_memory
/reports/downtown-summerlin-2026-09-18.md` (85 lines: dispatched, findings, flat set, plant per unit). The v0.9 run
opened with `list_memory` + `read_memory` of that file, treated the three findings dispatched at 07:53 PT as repeats
(SEVERE RTU-107-B, MAJOR Two Summerlin, MINOR VAV_B08_01 — "not resent"), dispatched only the new frost MINOR, and
wrote `/reports/downtown-summerlin-2026-09-18b.md`. Both files read via `GET /agent/json/autonomousagent/{id}/memory`
and `/memory/file?path=`. **That is correct de-duplication from a source the agent can actually see** — the thing
v0.8 faked and v0.9's dedup rule assumed impossible. Adopted as the rule in v0.10 ([MEMORY] section, 40-line schema,
three memory tools on the whitelist).

**Hygiene defect, both platform runs:** one stray empty call each — `make-actuations {"actuations": {}}` (v0.8, call
84) and `update-service-object-status {}` (v0.9, call 77). Harmless only because empty; one is an actuation tool.
v0.10 names every non-whitelisted tool and forbids it, empty arguments included. **Erik must still restrict the
agent's tool configuration in the editor** — the prompt cannot.

**v0.10 uploaded 17:27Z (92,408 chars, verified identical), reset, NOT invoked.** Next test = the scheduled DAILY
14:00Z run on 09/19 (Saturday run → reports Friday, Tier B Saturday row J1-3/J2-3/J1-2, reads memory from 09/18).

Not verified this round (my MCP connector needs re-auth): the CHANGED claim that AHU-J2-5's space point recovered to
73.90 / 72.96 F by 09:00 PT after the 52 F morning.


---

# 09/24 — the first week in service: five clean runs, ZERO emails → v0.11

Pulled via the Agent API 09/24 13:5xZ. Scheduled runs 09/19–09/23 all completed: 94/60/51/85/85 calls, 22.5/9.0/6.5/19.4/16.1
min, 1.16 M/410k/534k/595k/483k tokens in, zero off-whitelist calls, a memory file written every day (`/reports/2026-09-19.md`
… `-23.md`), repeats suppressed against them. The EMAIL DispatchConfig (erik@proptechos.com, enabled) existed and the agent
was reset after it (19:10Z 09/18). **Gmail holds no Summerlin email at all.** The message log shows why: every report ends
with the `✉️ DISPATCH · EMAIL …` line and nothing after REPORT-END. The 1700 agent's responses end with
`[DISPATCH] / channel: EMAIL / summary: "…" / severity: Severe` blocks, one per message, and its mail arrives. The Summerlin
spec described the report line as "the summary text as it would be sent" and never told the agent to emit the blocks — so
it treated the line as the send, recorded "dispatched" in memory, and de-duplicated the next day against a send that never
happened. **Findings that never reached anyone:** Two Summerlin MAJOR 09/19, 09/20, 09/21 and its recovery 09/22–23
(6-day blackout ended); RTU-107-B SEVERE 09/19 and 09/22; AHU-J2-5's space point alive again and 60.9–69.1 F for 7 of 11
occupied hours on Monday 09/21 (SEVERE 09/22, worse 09/23: 53.6–75.1 F, 9 of 11 hours); AHU-J2-3 c1 evap 32.0–33.4 F all
occupied hours 09/19; AHU-J2-7 c1 evap 32.7–34.9 F all occupied hours 09/23; imbalances on J1-2, J2-8, J1-7.

Also seen: the header printed the whole `Version:` line; three runs had preamble text before REPORT-START ("Probe OK…",
"Now compiling the report.", "Significant finding: …"); the 09/19 run made 94 calls against a 90 ceiling.

**v0.11 uploaded 09/24 (verified identical), reset.** Adds the `[DISPATCH]` block format with an example as the only
content after REPORT-END, version number only in the header, nothing before REPORT-START. First test: 09/25 14:00Z.


---

# 09/25 — v0.11 delivered its first emails; the content, checked

14:12Z: two emails at erik@proptechos.com (SEVERE + MINOR) — the `[DISPATCH]` block fix works end to end. Against Thursday's
raw data (REST, per PT hour):

| Email | Verdict |
|---|---|
| **SEVERE** "AHU-J1-7 space 76.1–77.1 F all day, out of band, first day sensing after weeks flat" | **FALSE.** 77.05 F all night, one step to 76.1 F at 05:00 (setpoint 85 → 72.5), then 76.07–76.26 F for 19 h. Not sensing; the plant-start step made the day range 1.0 F and beat the 0.5 F flat test. |
| **MINOR** "AHU-J2-5 circuit 3 approach 4–6 F above circuit 2, 12–17 PT" | **Artefact.** C2 within-hour min/max 79–80 / 90–92 F every hour 09–15 PT = cycling; C3 steady 89.5–92.7. Hourly-mean approach of a cycling circuit is a blend. At 16 PT (C2 steady 88.7–90.5) the spread is approx. 1.5–2 F. |
| Not sent: AHU-J2-5 space 62.8–68.8 F for approx. 10 of 13 occupied hours Thursday (band 70.5–74.5) | **REAL, withheld** — memory said "dispatched 09/24" for a send that never happened. |
| Not sent: RTU-107-B return air 82–86 F 10–17 PT, fan 42–48 % | **REAL, withheld**, same reason. Day 10. |

Also today 13:16Z: 1700 v0.6's first tick emailed BOTH addresses a MINOR (New York Life 1.2–1.6 F under the floor on 2 of 3
days — verified: Wed 6.0 h < 69 min 67.1, Thu 3.5 h min 67.25; Wynn and Gallery recovered — verified). Correct finding,
correct severity under the new depth ladder, no false Wynn relapse. v0.6 is doing its job.

**v0.12 (on disk, needs a gateway token to upload):** newly-moving points are WATCH for 3 days; flat test on the occupied
window; depth ladder; concrete cycling rule; `DISPATCHED:` lines before 09/25 void so the two withheld findings go out.

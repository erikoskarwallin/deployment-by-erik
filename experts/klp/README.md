# `klp/` — KLP agents (TEMPORARY EXCEPTION, same terms as `hhc/`)

> ⚠️ **This folder holds customer data. That is a deliberate, temporary exception to the
> repo rule "no customer data in GitHub" — the same exception granted for `hhc/` on
> 2026-08-01, extended here because the same reasoning applies. It must not reach `main`
> unreviewed.**

Everywhere else in this repo, expert agents are **generic and portable**. The files here
are the opposite: they are site-bound instances carrying live signal identity, because
**binding by UUID is the only safe option** — at Fornebu a KNX signal name like `433.001`
or `Feil` recurs hundreds of times, and name-based selection has already caused two
onboarding misses in this account (OTEAM-6766 at Howard Hughes).

## The five Fornebu agents (all live from 02.09.2026)

Five agents on one building. **Schedules are staggered on purpose** — they share
a platform with a 5-minute per-request timeout, and each spec carries a
`DIVISION OF LABOUR` block so they do not report the same finding twice.

| | agent | runs | owns | bindings |
|---|---|---|---|---|
| **A** | [Data quality](fornebu-A-data-quality.md) | Mon 05:00 | the broken-sensor list, split KLP-field vs Idun-integration | [306 pts](fornebu-dataquality-bindings.csv) |
| **C** | [TEK17](fornebu-C-tek17.md) | daily 05:30 | 19–26 °C + the 50-hour rolling quota | [105 pts](fornebu-tek17-bindings.csv) |
| **B** | [Hydronic ΔT](fornebu-B-hydronic-delta-t.md) | daily 06:00 | the water side — chillers, ΔT, heat recovery | [120 pts](fornebu-hydronic-bindings.csv) |
| **D** | [Simultaneous H&C](fornebu-D-simultaneous-heating-cooling.md) | daily 06:30 | heating and cooling running together | [41 pts](fornebu-simultaneous-bindings.csv) |
| **E** | [Embodied](fornebu-embodied-agent.md) | daily 07:00 | KNX, lifts, air side, the building's voice | [439 pts](fornebu-embodied-knx-bindings.csv) |

**Dispatch:** only **E** emails every day. A–D email on findings only — five
daily emails into one inbox would bury all five, and the platform does not
de-duplicate. SMS configs are created but **disabled** everywhere.

**Measured ground truth:** [fornebu-data-reality-2026-08-31.md](fornebu-data-reality-2026-08-31.md)
is the authority wherever a spec disagrees with a handover document. Refresh the
building-wide census with `onboarding/system-onboarding/klp-fornebu-dglux/fornebu_demo_probe.py`.

### Constraints every one of them carries

- **No history before 01.09.2026 12:51** (BACnet) — no trends, no baselines, no
  seasonal language until ~15.09. KNX has months.
- **Setpoints outnumber measurements 15:1** — 713 `IndoorAir Temperature` points,
  45 real. Only `SpaceTemp`, `…VlmC'VlmFl`, `Vav#.CO2R` and `Motion` are measured.
- **Sentinels**: `65535`, `8192`, exactly `0.0` (1,616 temperatures), negatives.
- **Polarity is unverified** on the KNX `Feil` contacts, the chiller
  `FltIK00n` and the `GasDet60n` gas detectors. Quote, never claim a fault.
- **No COP, no kWh, no cost** — zero power and zero flow points on the cooling
  plant.
- **`MAY BE BY DESIGN`** is a mandatory report line in B, D and E.

### First production run — 02.09.2026, and what it changed

The embodied agent v0.3 ran HITL at 12:24. **92 calls, 17 m 04 s, 2,703,134
tokens.** Two lessons, both now fixed in v0.4:

**1. The prompt was 54 % of the cost.** 64 KB re-sent 92 times = 1.47 M of the
2.7 M tokens. v0.4 is **23 KB — a 65 % cut**, taking the same run to ~537 k of
prompt. All 28 safety-critical rules were audited as still present.
⚠️ **Do not re-inflate the spec.** Rationale belongs in
`fornebu-data-reality-2026-08-31.md`; deploy steps belong here.

**2. It went off-whitelist and lost three rules.** The agent reached for
`monitor-indoor-climate` and `get-rooms-with-temperature-above-threshold`
(4 timeouts each) and `get-indoor-air-flow` (no usable AHU pairing) instead of
the bound UUIDs. Rules 9, 10 and 11 were ⚪ for the run.

⚠️ **These tools are not transiently broken — they are structurally wrong here.**
They scan a building of 12,122 sensors. v0.4 names all five as forbidden and
binds Rules 9–11 to `sensor_id` in `fornebu-embodied-bacnet-bindings.csv`.
**The same guard belongs in any future Fornebu agent.**

**What worked, and should be left alone:** it refused to call `Feil` a fault on
an unconfirmed unit; it distinguished a tool-timeout ⚪ from a data-absence ⚪ and
said so; it printed `SENSES DARK` verbatim; it declined to invent a
`MAY BE BY DESIGN` line when the rule that produces them had not run; and it
raised `[HITL_REQUIRED]` with two specific, correct items.

**It also found something real:** GA `0/0/1` (`433.001 Er Temp`) has two
sensors — `4c9360b5…` live at 23.0 °C and `45db854f…` flat at 0.00 all day. It
switched its own canary. The roster's `sensor_id_CHOSEN` had already picked the
live one, so the binding logic was right; **the dead duplicate still needs
fixing at source** (Oksana/Marichka, deviceAddress defect).

## The Teknostallen agents (Prof. Brochs gate 6, Trondheim) — 03.09.2026

**Same customer, opposite building.** Fornebu is a fault bus with four indoor
temperatures; Teknostallen is a fully instrumented comfort building where 99.2 %
of 6,071 sensors report inside the hour and history runs back to 11.05.2026.
**661 zones carry temp + setpoint + CO2 + Varmepådrag% + Kjølepådrag% + supply
m³/h.** It is the best-instrumented building in the KLP portfolio.

| | agent | runs | owns | points |
|---|---|---|---|---|
| **A** | [Data quality](teknostallen-A-data-quality.md) | Mon 05:00 | the 55 dead rooms, the sentinels, the dead setpoints | 116, latest-only |
| **B** | [Schedule & setback](teknostallen-B-schedule-setback.md) | daily **02:00** | the weekend night block, and the total absence of setback | 24 zones / 89 calls |
| **E** | [Embodied](teknostallen-embodied-agent.md) **live** | daily 07:00 | comfort, air, the water side, the building's own voice | 73, latest-only |
| **C** | [TEK17](teknostallen-C-tek17.md) | on demand | 19-26 °C and the 50-hour rolling quota | 35 + max 6 hourly |
| **D** | [Zone comfort](teknostallen-D-zone-comfort.md) | daily 06:30 | zones that cannot reach their own setpoint | 18 zones / 73 calls |

**Letters are aligned across both buildings where the role is the same:**
**A = data quality**, **C = TEK17**, **E = embodied**.

⭐ **The `SPK` question is settled (03.09.2026), which is what let D exist.**
Aligning temperature, setpoint and both demand signals across 45 zones and 9 days
— **55,033 samples** — shows heating ran 81 % of the time when T was >1 K below
setpoint and **0 %** when above, cooling 72 % above and **0 %** below
(corr −0.65 / +0.62). **`SPK` is a single comfort setpoint with a dead band**, so
"178 zones ≥2 K above setpoint" is a real measurement, not an artefact. Every
spec that hedged on this has been updated.

⚠️ **C was rebuilt from the production prompt in OTEAM-6732 v4**, which runs
on-demand for Lasse today and is **not safe as written**: it pages
`get-indoor-temperature` to exhaustion over 6,071 sensors, then runs hourly
history over the "longest available period" on every flagged room — 30+ series,
the exact pattern that killed two Fornebu agents at the 60-minute limit. v1.0 uses
bound UUIDs, **six hourly calls maximum**, and hands the census to the probe
script. It also adds **TIER X**: 13 rooms reading 1–12 °C that v4 would have
declared in immediate TEK17 breach and which are almost certainly cold stores and
plant rooms. Teknostallen has no
hydronic specialist (E covers the water side) and deliberately no simultaneous
heating/cooling agent — measured 1 zone-hour in 10,035. **All three email; SMS on
SEVERE only, which here is almost nothing.**

**E v0.1 ran 03.09 — 66 calls, 2m38, 165k tokens, no timeout, 65/65 points
returned.** B and A have not run; their budgets are estimates.

⚠️ **What v0.1 got wrong, and what v0.2 fixes.** It flagged three *cooling*
circuits as faulty for having a return warmer than their flow — which is what a
cooling circuit does. That was a **spec bug, not an agent bug**: Rule 4 never
stated the sign convention. It now does (HEAT ΔT = FLOW−RET, COOL ΔT = RET−FLOW,
both expected positive), and every circuit is bound with its **flow rate** so an
idle loop can be told from a broken one — v0.1 called a loop running 0.001 m³/h
"flat, no delta-T". **Never bind a ΔT pair without its flow rate.**

⚠️ **And prompt size costs, measured.** 29 KB / 66 calls = 165k tokens in 2m38;
38 KB / 76 calls = 263k tokens in 6m25. **Size ×1.31 → tokens per call ×1.38.**
An earlier note here claiming prompt caching made size cheap was wrong — the
**~30 KB guideline stands.** D (zone comfort) and C
(TEK17 rebuild of OTEAM-6732) are not written.

**The embodied agent was written directly against Fornebu embodied v0.6**, so it
starts where that one ended: latest-only from the first line, mechanical
report-format rules, and **no senses-dark line** (Erik's call — the gaps are known
and queued, repeating them daily is noise).

⚠️ **Its own trap, found on 03.09 and unique to this building:** nine water-side
temperature points carry a `t1`/`t2`/`RTTur`/`RTRetur` suffix that **contradicts
their placement context**, and on four circuits the pair is fully swapped. Read
`t1` as "flow" and you report a cooling circuit whose return is colder than its
flow. **The placement context is the authority; the name is not.** The spec binds
an explicit `FLOW`/`RET` column for exactly this reason.

⚠️ **Both are `HISTORICAL_BUDGET 0 series`, like the Fornebu five after v0.5.**
B v0.1 asked for 7 days of hourly history on 96 series — three times what killed
Fornebu A and E — and would have died on its first run. **The fix was not a
smaller window: B now runs at 02:00, while the night block is happening**, so
every question collapses into one `latest` read per point. That pattern —
*schedule the agent for the moment you want to observe, instead of reconstructing
it* — is the most portable thing to come out of this building.

⚠️ **B's 24 zones are 16 carriers + 8 controls, and the split is the experiment.**
A random stratified sample of 24 could not separate weekend nights (74 % of day)
from weeknights (54 %), while the building shows 89 % against 13 % — the block is
carried by specific large zones. The chosen carriers run 84 % / 3 %. **Never
average the two groups together.**

**The finding:** building supply airflow drops correctly to 33k m³/h at 21:00 on a
Friday, then returns to **199k at 23:00 and runs until 04:00** — and repeats on
Saturday and Sunday nights, while idling by day at ~35k. Weeknights are correct.
CO2 sits at 375–400 ppm throughout. **The weekend schedule appears to be
inverted.** Cause unverified; every spec forbids naming one.

**The pass worth giving away:** simultaneous heating and cooling is **1 zone-hour
in 10,035**. A Fornebu-D-style agent is not warranted here.

### Constraints these two carry

- **`2000.64` is a CO2 sentinel.** The only two rooms in the building "above
  1,000 ppm" are dead sensors pinned at it.
- **`429496.7` / `214735.2` are 32-bit power sentinels**, and `_ED` points are
  demand accumulators, not kW — summing them manufactures a fake ~1 MW nightly
  spike. **No kWh, kW or NOK figure from this building until a unit audit.**
- **Dead temps and setpoints read exactly 0.0** — filter `<5 °C` or they
  manufacture 20 K deviations. 90 setpoints are affected.
- **History params are `startTime`/`endTime`.** `from`/`to` are silently ignored
  and the endpoint then serves only the last ~24 h — which reads exactly like a
  truncated history. This wasted time on 02.09 and would mislead at Fornebu too.
- **`size` truncates from the oldest end**, hiding the newest data.
- **0 actuators** — monitoring only, which suits Lasse's stated preference.
- Two buildings are called "Teknostallen". Gate 10 has no data. Always gate 6
  (`05a59f07-845f-425b-901d-a53f2bd5fa4d`).

Refresh everything with
`onboarding/system-onboarding/klp-teknostallen/probe/teknostallen_probe.py`
(~6 min). Demo material:
[teknostallen-demo-runsheet.md](teknostallen-demo-runsheet.md); measured ground
truth: [teknostallen-data-reality-2026-09-02.md](teknostallen-data-reality-2026-09-02.md).

## ⚠️ 03.09.2026 — one defect fixed across ALL SEVEN agents: they have no memory

Every spec in this folder asked its agent to compare against a run it **cannot
read**. There is no run-history tool. The wording varied — *"since last week"*,
*"nothing changed → no email"*, *"unchanged, day N"*, *"keeps yesterday's
accumulated"* — and the consequence is the same: the agent either guesses or
invents continuity. The Teknostallen agent wrote **"first run on file for this
building" on its second run**.

All seven now carry a **`[YOU HAVE NO MEMORY]`** block. `CHANGED:` says so
explicitly, and **any dispatch rule keyed on "if something changed" is flagged as
not implementable** — those now key on severity, because an agent that cannot tell
whether it already sent something must not pretend it can.

⚠️ **Agent A's worked example was itself teaching the fabrication** — it showed
`no change`, `CHANGED SINCE LAST WEEK`, and *"3 room temperatures flatlined since
04.09"* on a latest-only agent. Examples are imitated; they were corrected too.

## ⚠️ The ΔT sign convention — added to agent B

At Teknostallen an agent reported **three healthy cooling circuits as faulty for
having a return warmer than their flow**, which is what a cooling circuit does.
The spec had simply never stated the convention. **Agent B had the same gap**, and
its own Rule 3 data contains a genuine wrong-sign pair (`CPlt37000 TFl402 10.10 /
TRt502 9.88`) that was invisible without it.

```
CHILLED WATER / COOLING   deltaT = RETURN - FLOW.   Expect POSITIVE.
HEATING / CONDENSER       deltaT = FLOW - RETURN.   Expect POSITIVE.
```

Related: **never judge a ΔT without knowing whether the circuit is flowing.**
Teknostallen binds a flow rate per circuit (below 0.05 m³/h → ⚪ idle). **Fornebu
has zero flow points on 215 cooling-plant points**, so agent B uses run state as a
proxy and is now required to say that is what it is doing.

## ⚠️ Prompt size costs — measured, and it corrects an earlier claim here

```
spec KB   calls   tokens    duration
   29       66    164,951     2m38
   38       76    262,674     6m25
```

**Size ×1.31 → tokens per call ×1.38 → duration ×2.44.** An earlier note claiming
prompt caching made size cheap was **wrong**. Keep specs near 30 KB. The three
Teknostallen specs sit at 34-35 KB deliberately — trimming further would cut
safety content — but **A is the one to watch**: 116 calls at 34 KB is the most
expensive run in the estate.

## Deploy steps — the five Fornebu agents

1. Agent created in ProptechOS, **PO = KLP `40d473bf-7d9c-4313-8387-d1cbb5f50c4c`**.
2. **Exactly three tools enabled** in the agent's tool configuration:
   `set-property-owner-id`, `get-sensor-latest-data`,
   `get-sensor-historical-data`. ⚠️ **Disable everything else** — the 02.09 run
   shows a prompt-level ban is not enough on its own.
3. Paste `sensor_id` / `sensor_id_CHOSEN` from the agent's binding CSV.
4. EMAIL DispatchConfig → **Reset the agent** (the block only reaches the prompt
   on a reset). SMS config created and left **disabled**.
   ⚠️ Do **not** create a SERVICE OBJECT config.
5. Schedule per the table above.
6. Run once by hand and **check the reported call count against `usedTools`** in
   `GET /json/autonomousagent/{id}/message/latest`. A 2–3 s run with no tools is
   a fabricated report, not a clean building.
7. Watch the duration. **Anything over ~10 minutes is heading for the 5-minute
   per-request cliff** — cut a tier before it dies.

### Diary

- **~15.09.2026** — lift the `NO HISTORY` block in B, D and E once 14 days
  exist; enable flatline for BACnet in A.
- **End of week one** — switch E from daily email to exception-only.
- **Week two** — decide on a second E run at 16:00, on whether Rule 10 fired.
- **October** — agent D Rule 4 (free cooling) goes live below 19 °C outdoor.
- **~01.09.2027** — agent C can produce its first real TEK17 verdict.

### 02.09 evening — the 504 storm, and the real root cause

Pavlo (#platform, 15:27) found the load: **agents guessing sensors by name.**

```
agent 2a91c26e-…  51 failed tool calls in one run
10:22:01  TKondRt          -> No sensor with name "TKondRt".
10:28:50  IK001'TKondRt    -> No sensor with name "IK001'TKondRt".
```

`TKondRt` exists nowhere in this building. **The agent invented it — and it had
no alternative.** v0.1 of every spec said *"paste `sensor_id` from
`fornebu-*-bindings.csv`"*, but an agent has three tools and **none of them
reads a file.** The rules gave human-readable point names, `sensorRef` happily
accepts a name, so it guessed. Every failed resolve is a query against the
Multi API, which is what produced the 504s and the 60-second timeouts.

**Fixed in v0.2 of all five specs:** the UUIDs are now **embedded in the prompt**
as a `[SENSOR BINDINGS]` table, with a hard guard — *sensorRef must be a
36-character UUID from the table; anything else is a bug; a rule whose point is
not in the table is ⚪.* STEP 0 probes are UUIDs too, not names.

```
spec                  bytes  UUIDs
embodied v0.4          30.4k    70   reduced from 564 points, deliberately
A data quality v0.2     18.2k    45
B hydronic v0.2         16.9k    24
C TEK17 v0.2            18.2k    56
D simultaneous v0.2     16.3k    17
```

⚠️ **The point count and the prompt size are now the same variable.** An agent
can only address sensors whose UUIDs are in its prompt, so growing coverage
costs tokens on every round. The sets above are deliberately small — enough to
run fast and reliably. **Grow them only after a run's real cost is measured.**

⚠️ **Regenerating the tables:** the CSVs are still the source of truth for
humans. Rebuild a block from them, paste it in, never hand-edit a UUID.

### Operational notes from the same incident

- **A run is not instant.** Pavlo: *"you were doing invocation after just 2
  minutes, then resets"*. Let a run finish before re-invoking or resetting.
- **One agent hit a 60-minute run** and the Anthropic client timed it out.
  Platform timeout is 60 min per run; individual API calls time out at 60 s and
  return 504 under load.
- **The agent UI status is not live** — a Reset can appear not to have happened.
- Three `agenttroupe` pods; one was misbehaving on 02.09 and was redeployed.
  Not every failure that morning was ours.

### Known open questions, all cheap to ask

1. Which of the 33 rooms are TEK17 workplaces? *(KLP)* — blocks C's verdict.
2. Is there a separate domestic hot water circuit on `HPlt320`? *(KLP/Nordomatic)* — may collapse most of D.
3. Is `Sys370010'MtrOE401` installed, and why are all seven registers dead? *(Nordomatic)* — would make chiller output measurable.
4. Make/model of IK001/IK002 and do the panels have a comms card? *(Nordomatic)*
5. `Feil` / `FltIK00n` / `GasDet60n` polarity convention. *(Nordomatic)*
6. Which AHU serves what? *(Nordomatic)* — without it every imbalance stays on `MAY BE BY DESIGN`.
7. Why do all 174 electrical meters read zero? *(Nordomatic)*
8. Gross area in m² and trading hours. *(Egil, KLP)*

## What's in here


| File | What it is |
|---|---|
| [fornebu-embodied-agent.md](fornebu-embodied-agent.md) | **v0.3.** The building's own voice. KNX (escalators, lifts, switchboards, fire, pull cords) + the BACnet air side (45 SpaceTemp, 60 Motion, 20 AHU flows). Exception-based; the only one that emails daily. |
| [fornebu-A-data-quality.md](fornebu-A-data-quality.md) | **v0.1.** The broken-sensor list for KLP's technicians, split into five failure classes with KLP-field vs Idun-integration ownership. Watches the 255 points the other agents depend on + 51 recovery watches. |
| [fornebu-B-hydronic-delta-t.md](fornebu-B-hydronic-delta-t.md) | **v0.1.** The water side. Chiller evaporator ΔT (1.3–1.9 K vs 5–8 K design), condenser approach, heat recovery, and two dormant district-return rules that wake when the utility meter temps report. |
| [fornebu-C-tek17.md](fornebu-C-tek17.md) | **v0.1.** Starts the TEK17 clock — 19–26 °C and the 50-hour rolling-365-day quota over 33 rooms. Cannot produce a verdict until ~01.09.2027 and says so every time. |
| [fornebu-D-simultaneous-heating-cooling.md](fornebu-D-simultaneous-heating-cooling.md) | **v0.1.** Heating at 48.9 °C while both chilled-water circuits run at 25 °C outdoor. Six benign explanations, none ruled out. Free-cooling rule armed for October. |
| `fornebu-*-bindings.csv` | Site-bound sensor rosters, one per agent. |
| [fornebu-data-reality-2026-08-31.md](fornebu-data-reality-2026-08-31.md) | The measured ground truth. Authority wherever a handover document disagrees. |
| [fornebu-demo-runsheet.md](fornebu-demo-runsheet.md) | Operational run sheet from the 02.09 demo prep. |

**Not in here, and must stay out:** IP addresses, hostnames, PEG identities, VPN details,
credentials, bearer tokens, recipient emails and phone numbers. Those live in the
building's site folder on Drive
(`Onboarding ProptechOS/8. Building discovery/KLP/Fornebu/`) per the `peg-discovery`
convention.

⚠️ **This folder was written clean of those from the start** — deliberately, because
`hhc/` was not, and its README now carries three separate "strip this before merge"
warnings for PEG hosts, SSH users, recipient mobiles and BACnet device IPs. The Fornebu
spec names no addresses and no recipients; the KNX gateway IPs appear only once, in
Rule 8's guidance on describing a quiet bus, and should be cut if that turns out to
matter more than it helps.

## Frydenlund (Pilestredet, Oslo — OsloMet campus) — first agent, PRE-DEPLOY

Eleven ProptechOS buildings, one PEG (KLP-004, live since 02.09.2026), **nothing onboarded yet**
except 15 EXAMPLE twins proving the time-channel twin model
(`onboarding/peg-discovery/docs/schedule-twins-mcp-agent.md`). The first agent is written
against the 04.09.2026 BACnet scan and waits for the connector.

| | agent | runs | owns | bindings |
|---|---|---|---|---|
| **B** | [Tidskanal & occupancy (AHU)](frydenlund-B-schedule-occupancy.md) | daily 04:30, one building group per weekday | what each of 73 AHU time channels is set to, whether it changed against the 04.09 baseline, and — for the 4 of 65 AHUs with a CO2/presence proxy — whether anyone was there during the on-hours | [88 channels](frydenlund-schedule-bindings.csv), all `TO BIND` |

Ground truth: [frydenlund-schedule-reality-2026-09-06.md](frydenlund-schedule-reality-2026-09-06.md).
Visual inventory of every channel (the UI the agent's table is a text rendering of): the
**Tidskanaler Frydenlund** artifact (https://claude.ai/code/artifact/c578a5c6-af30-4d5e-bb54-8cb40c39fa51, private to Erik until shared), generated from the scan by
`onboarding/system-onboarding/klp-frydenlund/schedule_build.py` + `schedule_gen_html.py`.

**Three things that decide whether this agent tells the truth:**
- **Only 4 of 65 AHUs have any occupancy signal.** 26 CO2-equipped VAVs named `360.012-L*` /
  `360.013-G*` carry no building prefix and match three AHUs each — do not bind them until
  Nordomatic says which. Occupancy is ⚪ for the rest and the spec says so in one line per run.
- **`P52_360_001` and `P52_360_002` each exist twice** (1093/10118, 1090/10121) with different
  channels. Littera stems must carry the device instance.
- **`JV` is a fan, not a valve.** `P46_360.003` carries six constant 24/7 fan channels for
  systems 360.004–009; they are by design until someone says otherwise.

Lighting (`SCY-2DALI`) and meeting-room KNX presence are the planned extensions, not in v0.1.

## Before this merges to `main`

1. **Move the sensor UUID map out** of the roster once it is filled — to the site folder,
   or inject it at deploy time. Do **not** "sanitise" by switching to name-based lookup;
   that reintroduces the exact bug the UUID binding exists to prevent.
2. **Generalise what's generalisable.** Three things in the Fornebu spec are portable and
   worth promoting to the generic `experts/` set, because they are not about this
   building at all:
   - **inverted-polarity life-safety signals** (`On=OK`) and the discipline of never
     assuming binary polarity without a confirmed event;
   - **panel-internal temperatures tagged `IndoorAir`** because REC has no
     `ElectricalRoom` placement context — any KNX or Modbus site with switchboard
     monitoring will hit this, and reading them as room comfort is a one-line disaster;
   - **counting equipment from a roster rather than from a sensor list**, where one
     physical signal became several twins.
3. **Strip building UUIDs, property-owner UUIDs and customer names** from whatever
   remains here, or move the remainder out of the repo entirely.
4. Re-run the containment check:
   ```
   git grep -lE 'Fornebu|Snarøyveien|KLP|[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}'
   ```
   Anything outside `experts/klp/` and `experts/hhc/` is a leak; anything still inside is
   a decision.

## Related, elsewhere

- **Teknostallen (Trondheim)** — the other KLP building with agents (TEK17 temperature
  compliance + a sensor-analysis agent). Same property owner, Piscada BAS, no files in
  this repo yet. Jira epic OTEAM-6458.
- `../hhc/agent-dispatch-sms.md` — shared reference on how an agent signals EMAIL / SMS /
  service object. Read it before enabling any channel here.
- `../../embodied/buidling-base.md` — the generic embodied template both site specs
  instantiate. ⚠️ It assumes a Nordic metric building with CO2, humidity, TVOC and
  hot/cold water metering. Fornebu is Nordic and metric and has **none** of those four,
  so roughly half its daily report cannot be filled here either. The Fornebu spec
  replaces those sections rather than leaving the agent to invent them — that
  substitution must not be quietly undone by a later merge.

# TEKNOSTALLEN — STATE, 03.09.2026 09:35 CEST

Demo for **Lasse Volden (KLP) is TODAY**. Start at
**[teknostallen-demo-runsheet.md](teknostallen-demo-runsheet.md)** — that is the
document to walk in with. Ground truth is
[teknostallen-data-reality-2026-09-02.md](teknostallen-data-reality-2026-09-02.md).

## Done

- ✅ **Probe written and re-run this morning** —
  `onboarding/system-onboarding/klp-teknostallen/probe/teknostallen_probe.py`.
  One pass: census, zone join, flatline scan, airflow curve, meter sentinel audit.
  Emits the roster and a readiness report. **Nothing has drifted since 02.09.**
- ✅ **Roster**: [teknostallen-zone-bindings.csv](teknostallen-zone-bindings.csv),
  1,379 zones, 661 complete, bound by sensor UUID.
- ✅ **Captured run**: [teknostallen-demo-readiness.md](teknostallen-demo-readiness.md)
  — the demo works from this file alone if the platform is down.
- ✅ **Agent B (schedule & setback) v0.3** — [schedule & setback](teknostallen-B-schedule-setback.md),
  29 KB, 24 zones / 89 calls, **daily 02:00**, latest-only, dispatch OFF.
- ✅ **Agent A (data quality) v0.3** — [data quality](teknostallen-A-data-quality.md), 29 KB,
  116 points latest-only, Mon 05:00, dispatch OFF.
- ✅ **Embodied agent v0.1** — [the building's voice](teknostallen-embodied-agent.md),
  35 KB, 73 points latest-only, daily 07:00, EMAIL+SMS dispatch ON. v0.3 ran 03.09 (76 calls,
  6m25); v0.4 fixes bullet-splitting, preamble and the impossible CHANGED rule. Written against
  Fornebu embodied **v0.6**: mechanical report format, no senses-dark line.
  **On the clipboard as of 03.09 ~10:00.**

### ⚠️ Both were rewritten after auditing the Fornebu v0.5 learnings

**B v0.1 would have died on its first run.** It asked for 7 days of hourly
history on 96 series; on 02.09 that exact pattern killed Fornebu A and E at 30+
series — the full 60-minute platform limit, `Tokens: 0`, no report. Both specs
are now `HISTORICAL_BUDGET 0 series` and neither has `get-sensor-historical-data`
in its whitelist. **Disable that tool in the ProptechOS config too**, not just in
the prompt.

**The fix was a design change, not a smaller window: B runs at 02:00, while the
night block is happening.** Every question then collapses into the current value
of a sensor. Portable to any agent whose finding has a known time of day.

**B's sample was also rebuilt.** A random stratified 24 zones could not separate
weekend nights (74 % of day) from weeknights (54 %) — the block is carried by
specific large zones. The roster is now **16 carriers (84 % / 3 %) + 8 controls**,
reported separately and never averaged together.
- ✅ **Run sheet** with the seven questions for Lasse.
- ✅ New finding folded in: the dead points are **55 rooms, not 137 sensors**.

## Not done

- ❌ **D (zone comfort)** and **C (TEK17 rebuild)** — specs not written. The
  embodied agent covers the comfort *headline*; D would own the 216-zone list. C matters:
  OTEAM-6732 is already live for Lasse and still needs its two agreed fixes
  (classify strictly by measured value; require true hourly resolution before any
  "50-hour quota exhausted" verdict). Do these after the demo unless he asks today.
- ❌ **Neither B nor A has ever been run.** Call budgets are estimates. On the
  first run, check the reported count against `usedTools` in
  `GET /json/autonomousagent/{id}/message/latest`.
  ⚠️ **Run B by hand on a Saturday or Sunday night** — a weeknight run proves
  only that the agent works, not that it can see the finding.
- ❌ **Lasse's existing agents not checked.** There is no API endpoint for the agent
  list (`/json/autonomousagent` and four variants all 404) — **this is a UI check**.
  Is the TEK17 agent still running? Did "Sensor analyse – Lasse" come back (PLAT-5579)?
- ❌ **Nothing is committed.** `experts/klp/` is untracked. Its README says this
  folder holds customer data and must not reach `main` unreviewed — that still holds
  for the Teknostallen files, which carry live sensor UUIDs and room numbers.

## Deploy steps, when B/A go live

1. Create the agent in ProptechOS, **PO = KLP `40d473bf-7d9c-4313-8387-d1cbb5f50c4c`**.
2. **Enable exactly the tools the spec whitelists** — B needs three, A needs two
   (A must NOT have `get-sensor-historical-data`). **Disable everything else**, in
   particular the five building-wide scan tools each spec names as forbidden. A
   prompt-level ban was not enough at Fornebu.
3. UUIDs are already embedded in the spec. Do not point the agent at the CSV — it
   cannot open files, and at Fornebu that made it invent 51 sensor names.
4. **No DispatchConfig.** Lasse drafts in chat and sends himself.
5. Run once by hand and check the call count. A fast run with no tool calls is a
   fabricated report, not a clean building.

## Open questions for KLP

The seven live ones are in the run sheet. The two that block the most:
**what runs 23:00–04:00 on weekend nights**, and **is `SPK` a comfort or a cooling
setpoint** (some read 15.5–19.5 °C, which decides whether 216 zones are "off
setpoint" or fine).

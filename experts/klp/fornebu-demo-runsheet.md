# FORNEBU S — DEMO RUN SHEET

**Demo: Wednesday 02.09.2026.** Written 31.08. Companion to
[fornebu-embodied-agent.md](fornebu-embodied-agent.md) — this is the operational
document, not a prompt. It says what to run, in what order, what it will cost in
wall-clock time, and what to do when a step fails.

---

## ✅ ANSWERED 31.08 — the KNX layer is live

Probed against the live platform at 14:10–14:35 UTC. Full findings in
[fornebu-data-reality-2026-08-31.md](fornebu-data-reality-2026-08-31.md).

```
KNX            711 sensors   240 <1h   172 1-24h   196 never   newest 4 min old
Soundsensing   300 sensors   ALL never reported   (twins exist — handover said parked)
BACnet      10,856 sensors   ALL never reported   (PLAT-5774, as expected)
KLP datalake    85 sensors   70 never; water reports daily at midnight
```

**Plan A is on.** ~167 live signals across tiers A and B, the roster is bound,
and the agent can run for real. Re-run the probe Tuesday morning to confirm
nothing has drifted:

```
python3 system-onboarding/klp-fornebu-dglux/fornebu_demo_probe.py \
        --token-file /tmp/tok.txt
```

---

## THE DEMO, IN ORDER

### 1. Open with the gap list — zero tool calls, 90 seconds

Do not bury it and do not apologise for it. A building that says plainly what it
cannot feel is handing KLP their own roadmap:

```
117 Xovis 3D cameras     installed at every doorway on VLAN111. NONE onboarded.
                         Footfall is the metric a shopping centre wants most and
                         the hardware is already hanging in the ceiling.
10,856 HVAC points       twinned 27.08, waiting on ONE connector ticket
                         (PLAT-5774). The air side is weeks away, not years.
300 Soundsensing points  60 accelerometers already modelled, all dark.
2 PV plants              we see fault contacts, not yield. Needs a portal login.
9 Zaptec EV chargers     same.
```

Every line is a short conversation with a named owner. **This is the most
valuable slide in the deck and it costs nothing to prepare.**

### 2. The switchboard temperatures — the safest live moment

Unambiguous, analog, polled hourly, no polarity risk, and nobody at KLP has ever
looked at them.

```
46 boards, 87 of 90 sensor objects reporting
median 27.20 °C   range 21.90 – 31.60 °C
warmest  433.196  31.60 °C, 4.4 °C above the median, stable 31.4–32.2 over 24 h
coolest  433.015  21.90 °C
```

The rule is the building compared against itself — no invented threshold. Ask it
live: *"which of your switchboards is warmest?"* (~46 calls, ~2 min — or pre-run
it and take the question live only if the room is patient).

### 3. The lifts — the strongest finding we have

Unlike the escalators, the lift `Feil` contacts behave conventionally, and they
have a month of real history. **218 fault events across 12 lifts in 30 days.**

```
HEIS 7    10 events, 17.2 hours in fault, longest 5h19
HEIS 11   89 events, 11.0 hours, one single event of 10h13
HEIS 3    12 events,  6.8 hours, longest 2h55
```

And the hook: **HEIS 3 and HEIS 7 both enter fault at exactly the same second on
multiple nights** — 02:37:29 and 23:23:31 — and HEIS 3's duration grew three
nights running (1h25 → 2h25 → 2h55, 28–30.08) before stopping last night.

⚠️ **Ask, do not assert.** Same-second recurrence is a schedule. Present it as
*"is 02:37 a service window?"* — the question, with the trace behind it, is the
demo moment. A claimed diagnosis would be a retraction waiting to happen.

⚠️ **Two honesty caveats to say out loud:**
- **`HEIS 5` has 13 samples in 30 days** — effectively unmonitored. Its clean
  record is absence of data, not absence of faults.
- **`HEIS 8 Alarm aktivert` returned nothing in 30 days.**
- Sample density varies 280-fold across units, so the event counts are floors.
  Compare *total minutes in fault*, not event counts.

### 4. Availability of the moving equipment — from `Drift`, never from `Feil`

```
13 of 15 units in Drift on Monday afternoon
RT 07    Drift = 0 for seven straight days       -> stopped all week
RB 07    no Drift telemetry at all               -> unmonitored
RT 01    no Drift telemetry at all               -> unmonitored
RT 06    Drift = 1 on all 1,015 observations     -> never stops
```

⚠️ **DO NOT SAY "SIX ESCALATORS ARE FAULTED."** That was the naive read at 14:12
and it is almost certainly false — see below.

### 5. Close on the ticket list

PLAT-5774 (HVAC connector) · the `deviceAddress` defect for Oksana/Marichka ·
the fault-polarity question for Nordomatic · Xovis · the two cloud portals ·
gross area and trading hours from Egil.

---

## ⚠️ THE ONE THING THAT WILL EMBARRASS US IF WE GET IT WRONG

At 14:12 the escalator set read **`Feil = 1` on 6 of 8 moving walks**. Presented
as-is that is "your building is broken", and it is wrong.

Three days of RB 01, time-aligned, show `Feil` rising ~30 minutes *after* the
unit starts running and falling within seconds of it stopping — **it tracks
running, not faulting.** But it does not behave that way on all fifteen units:
RB 04/07 and RT 01/02/03/05/06/07 look like conventional rare-event fault flags
(HEIS 1: 276 zeros and 2 brief ones in 7 days — textbook).

**So the fault semantics are inconsistent across the fifteen units.** That is a
commissioning inconsistency in the building, not a platform bug.

```
BEFORE WEDNESDAY: ask Rune / Nordomatic to confirm the Feil convention per group.
                  One email. It converts a liability into the best finding we have.
IF UNANSWERED:    demo availability from `Drift` only, and present the
                  inconsistency itself as the finding — "your documentation says
                  these are fault contacts; on six units they are not, and here
                  is the three-day proof." That is a genuinely strong result and
                  it is honest.
```

Two more signals carry no information and must not be shown as green:
`Brannvarsling Feil` = 1 on all 955 observations over 7 days, and
`2B 3042 HCWC Snorbryter utløst` = 0 on all 163 — under the documented `On=OK`
inversion that reads as a permanently pulled emergency cord, which is not
credible. Treat both as unwired until proven.

---

## WHAT WE CANNOT DEMO, NOW CONFIRMED BY MEASUREMENT

- **Any indoor temperature.** All 12 `Heating` sensors — the four staff shower
  rooms — have **never reported**. The building has zero live room temperature.
  The v0.1 spec was wrong about this; v0.2 is corrected.
- **Vibration / condition monitoring.** 300 Soundsensing twins, all dark.
- **Ventilation, air quality, footfall, PV yield.** As before.
- **Energy and waste.** 70 of 85 meter sensors have never reported. One water
  figure (75.23, daily at midnight) is real; the Norwegian waste-chapter taxonomy
  is modelled but almost entirely empty. **Do not build an ESG story on this.**

## LATENCY — the thing that will actually bite

The full daily run is ~218 tool calls. **Do not run it live in front of anyone.**

```
5-minute per-HTTP-request timeout to the model, and every tool result is
re-sent on every subsequent round. A long run dies as `Request failed`,
`Tokens: 0` — and it looks exactly like a broken product.
```

**Pre-run the full report Tuesday. Live-run only short questions.**

| Live question | calls | notes |
|---|---|---|
| "What can't you sense?" | **0** | instant. Open with this. |
| "How are your escalators and lifts?" | 27 | ~1 min. The money question. |
| "Any lift faults?" | 12 | fast |
| "Which switchboard is warmest?" | 46 `hourly _1day` | slower, ~2 min. Only if time allows. |
| "How much energy did you use?" | ~8 | only if the meters proved live |
| "Is anything wrong right now?" | 109 | ⚠️ **too slow — pre-run it** |

⚠️ **Reset the agent after every prompt change.** Erik's standing control, and
it is required for the dispatch block. It does **nothing** for a stale property
owner — only `set-property-owner-id` fixes that.

---

## FAILURE MODES TO REHEARSE

**The zero-call fabrication.** A scheduled agent with history in context can
print a confident green report having called nothing — five of eleven 1700 ticks
did exactly that, with invented freshness numbers that varied plausibly. In a
demo this is catastrophic and undetectable by the audience. **Mitigation:** every
report carries its own call count; check it on the pre-run and on each live
answer. A run showing 2–3 seconds and no `Used N tools` is void.

**The 401 that looks like an outage.** Wrong property owner returns `401` /
`Invalid sensor ID` / `Invalid twin ID`, and error handling has once folded that
into an empty list so 18 healthy sensors printed as `NO DATA — STALE`.
**Mitigation:** the agent calls `set-property-owner-id` for KLP
(`40d473bf-…`) at step 0 and probes before anything else. This account holds
several property owners and has got this wrong repeatedly.

**Polarity.** If the probe reports 20+ active tier-A signals, that is almost
certainly an inverted assumption, not a building on fire. Say so rather than
demoing it.

**The dark twins.** 10,856 of 11,952 sensors return nothing. If anyone opens the
ProptechOS UI during the demo it will look like a 9 %-coverage building.
**Have the number ready:** ~91 % of the sensor count is twinned-and-waiting on
one connector ticket, which is a completed modelling job, not a failure.

---

## TIMELINE

**Today (Mon 31.08) — DONE**
- [x] Fresh token captured; probe run against the live platform
- [x] KNX confirmed live (newest observation 4 min old)
- [x] All 439 roster rows bound to real sensorIds, with values and liveness
- [x] 711-vs-439 settled; `deviceAddress` defect found; polarity investigated

**Tuesday 01.09 — the critical day**
- [ ] **Email Rune / Nordomatic: what does `Feil` mean on RB 01–08 and RT 01–07?**
      Attach the RB 01 three-day trace. This is the highest-value hour of the week.
- [ ] Create the agent in ProptechOS — PO = KLP, the three tools enabled
- [ ] Paste `sensor_id_CHOSEN` for tiers A and B into the spec's binding block
- [ ] `TIER_C off`, `DISPATCH off`, run once by hand with `DAILY_REPORT on`
- [ ] **Check the call count against the report** — prove it fetched, and that
      it did not print a fabricated green
- [ ] Screenshot the full report; rehearse the three live questions end to end
- [ ] Re-run the probe in the morning to confirm nothing drifted overnight

**Wednesday 02.09**
- [ ] Gap list → switchboard temperatures → `Drift` availability → ticket list
- [ ] Pre-run report on screen; 2–3 live questions only

## WHAT NOT TO DEMO

- **Dispatch.** Untested at this building, and it silently dropped all three
  test messages at another site on 24.08 (PLAT-5754, fixed 26.08 elsewhere,
  never proven here). Do not promise email or SMS on Wednesday.
- **Anything about comfort, air quality or ventilation.** We cannot sense it.
- **Footfall or visitor numbers.** The cameras are not onboarded.
- **PV yield.** We have fault contacts only.
- **Room-level detail.** 624 room objects hold only 380 distinct littera —
  the register has a duplicate import in it and will not survive scrutiny.
- **A dollar or krone figure on anything.** No tariff, no area, no baseline.

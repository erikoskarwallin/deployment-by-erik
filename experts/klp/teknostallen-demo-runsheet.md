# TEKNOSTALLEN — DEMO RUN SHEET

**Demo: Thursday 03.09.2026, for Lasse Volden (KLP), cc Egil Brækken.**
Companion to [teknostallen-data-reality-2026-09-02.md](teknostallen-data-reality-2026-09-02.md)
(the measured ground truth) and the two agent specs. This is the operational
document — what to show, in what order, and what to do when something fails.

---

## ✅ VERIFIED THIS MORNING, 03.09.2026 07:15 UTC

The probe was re-run against the live platform. **Nothing has drifted.**

```
6,071 sensors    6,022 reporting inside the hour (99.2 %, same as 02.09)
661 zones        carry all six of temp + setpoint + CO2 + heat% + cool% + supply flow
temp             797 varying · 55 flatlined      (02.09: 797 / 55)
CO2              686 varying · 82 flatlined      (02.09: 685 / 83)
the night block  still there — Fri 199,567 · Sat 208,715 · Sun 168,520 m³/h
                 and Wed→Thu night was 34,000, i.e. weeknights are still fine
```

Re-run before you walk in:

```
PO_TOKEN_FILE=/tmp/tok.txt python3 \
  onboarding/system-onboarding/klp-teknostallen/probe/teknostallen_probe.py
```

~6 minutes. `--quick` (90 s) skips the airflow curve, which is the finding — don't.

⚠️ Capture a fresh token first; they live 3600 s. Never `sed` a JWT into `.env` —
the `/v2.0/` substring gets stripped. Pass it in a file.

---

## THE DEMO, IN ORDER

### 1. Open by comparing Teknostallen with Fornebu — 60 seconds, zero tool calls

Lasse has seen the Fornebu work. The contrast is the point, and it is flattering
to Teknostallen:

```
                       Fornebu S              Teknostallen
sensors                12,122                 6,071
actually reporting     ~1,000 (8 %)           6,022 (99.2 %)
indoor temperatures    4  (staff showers)     855
CO2                    18 usable of 103       686 usable
history                one night              since 11.05.2026
fully-instrumented     0 zones                661 zones
  comfort zones
```

**Say it plainly: Teknostallen is the best-instrumented building in the KLP
portfolio, and nobody has been looking at it.** That is the whole pitch.

### 2. The finding — the weekend night block

This is the demo. Put the curve on screen and read four numbers out loud:

```
Fri 28.08 21:00     33,166 m³/h    ventilation correctly shuts down
Fri 28.08 23:00    199,567 m³/h    <-- back to 89 % of the weekday peak
Sat 29.08 03:00    162,582 m³/h    <-- still running. CO2 375-400 ppm.
Sat 29.08 06:00     29,588 m³/h    shuts down as Saturday morning starts
Sat 29.08 14:00    ~35,000 m³/h    idles correctly all day Saturday
```

Then: *"and again Saturday night, 208,715. And again Sunday night, 168,520.
Weeknights are fine — Monday night was 29,286."*

**The framing that works: the schedule is not missing, it appears to be
inverted.** Something runs the high-flow block at night on Fridays, Saturdays and
Sundays, and idles by day.

⚠️ **Do not say waste, fault, or wrong, and do not name a cause.** We do not know
whether it is a transposed weekend program, a night purge, a filter run, a
holiday-calendar fault, or genuinely occupied weekend nights we have not been
told about. **Ask Lasse. He may know in one sentence.** That question landing well
is a better demo than a diagnosis landing badly.

### 3. The second finding — there is no setback in temperature at all

```
setpoint      flat 20.0-20.2 °C in all 24 hours of every day, weekends included
room temp     holds 20.0-21.5 °C to match
heating       17-31 % demand around the clock
cooling       28-53 % demand around the clock
```

The building is held at comfort conditions at 03:00 on a Sunday. Again: ask
whether 20 °C 24/7 is deliberate — for some tenants it is.

### 4. Give away a clean pass — it buys credibility for everything else

```
✅ Simultaneous heating and cooling: 1 zone-hour in 10,035 checked.
   The zone controls are well behaved. There is no reheat problem here.
```

At Fornebu this was a whole agent. Here it is a pass, and saying so unprompted is
what makes the two findings above believable.

### 5. The work list — 55 rooms, not 137 sensors

```
55 room temperatures flat at exactly 0.0        the same ~55 as OTEAM-6733, July 2026
82 CO2 points flat                              55 of them in the SAME ROOMS
                                                -> 55 room sensor units, not 137 points
90 setpoints reading below 5 °C                 these silently corrupt any comfort rule
```

**The 55-rooms framing is the useful one** — one site visit per room. They cluster
hard in the `3xxx` block, which is worth saying: it smells like a bus segment, not
55 independent failures.

⚠️ And the line that protects us: **the only two rooms in the building "above
1,000 ppm" are `5079` and `2608`, and both are dead sensors pinned at the sentinel
`2000.64`.** Show that. It is the clearest possible demonstration of why an agent
needs a data-quality layer underneath it — and we caught it before it reached him.

### 6. The two agents

Show [B](teknostallen-B-schedule-setback.md) and
[A](teknostallen-A-data-quality.md) as prompts, not as running agents.

```
B  Schedule & setback   daily 02:00   24 zones, 89 calls, latest-only   the night block
A  Data quality         Mon 05:00     116 points, latest-only          the 55 rooms
```

**Why B runs at 02:00 — this is the good story.** The first version reconstructed
the night from seven days of hourly history: 96 series. On the sibling building
that exact pattern killed two agents at 30+ series — the full 60-minute platform
limit, no report at all. **So B does not reconstruct the night. It is awake in
the middle of it.** At 02:00 the night block, the missing setback and the empty
building are all just *the current value* of a sensor. 89 instantaneous reads,
no history, finishes in minutes.

**And its 24 zones are split 16 carriers / 8 controls, deliberately.** A random
sample of 24 zones showed the weekend night at 74 % of day and the weeknight at
54 % — barely separable, when the building as a whole is 89 % against 13 %. The
night block is carried by specific large zones. The chosen 16 run at **84 % on a
weekend night and 3 % on a weeknight**; the 8 controls set back properly on both.
**If a control ever behaves like a carrier, the pattern has spread** — that is the
alarm the design exists to raise.

Both ship with **dispatch OFF** — Lasse said on 05.07.2026 he does not want agents
emailing autonomously; he drafts in chat and sends it himself. **Say that back to
him.** It shows we listened.

### 7. Close with what we still cannot do, and who unblocks it

```
electrical energy    127 kW meters, but 6 are pinned to 32-bit sentinels and 2 are
                     demand accumulators, not power. NO kWh and NO NOK figure until
                     a unit audit. (This nearly produced a fake 1 MW nightly spike.)
gross area           not known -> no kWh/m²
operating hours      not known -> every "outside hours" judgement hedges
TEK17 workplaces     which of the rooms are workplaces? blocks a real TEK17 verdict
```

Each is one short conversation with a named owner. **Ending on the gap list is
what makes the rest credible.**

---

## THE QUESTIONS FOR LASSE — the actual point of the meeting

1. **What runs 23:00-04:00 on Friday, Saturday and Sunday nights?** (the big one)
2. Is `SPK` a comfort setpoint or a cooling setpoint? Some read 15.5-19.5 °C.
3. Is 20 °C around the clock, including weekends, deliberate?
4. The 55 dead rooms cluster in the `3xxx` block — is that one area of the
   building, and who owns those sensors, KLP or the service partner?
5. Gross area in m², and the building's operating hours.
6. Which rooms are TEK17 workplaces?
7. Is the TEK17 agent from July still running, and did "Sensor analyse – Lasse"
   ever come back? *(PLAT-5579 — check in the UI before the meeting, there is no
   API endpoint for the agent list.)*

---

## IF SOMETHING FAILS

```
token 401                  the session is bound to the wrong property owner.
                           KLP = 40d473bf-7d9c-4313-8387-d1cbb5f50c4c.
                           401 / "Invalid sensor ID" / "Invalid twin ID" are three
                           faces of ONE fault. Never "fix" a UUID because of them.
no sensors returned        you are on gate 10 (76181108-…), the decoy. Gate 6 is
                           05a59f07-845f-425b-901d-a53f2bd5fa4d.
history looks like 24 h    you used `from`/`to`. They are SILENTLY IGNORED.
                           The parameters are `startTime`/`endTime`.
history missing the        `size` truncates from the OLDEST end. Raise it, or
newest week                shorten the window.
probe connection resets    drop `--threads` to 8. 24 gets connection-reset.
a room "at 2000 ppm"       it is the sentinel. It is not a reading.
a megawatt appears         you summed an `_ED` demand accumulator. It is not power.
```

**If the live platform is unavailable, the demo still works.** Every number above
is already measured and written down; `teknostallen-demo-readiness.md` is a
complete captured run from this morning. Show that file rather than cancelling.

# `hufvudstaden/` — Hufvudstaden agents (TEMPORARY EXCEPTION, same terms as `hhc/` and `klp/`)

> ⚠️ **This folder holds customer data** — live sensor UUIDs, litteras and measured values
> for Hufvudstaden's NK Stockholm. Same deliberate, temporary exception as `hhc/`
> (granted 2026-08-01) and `klp/`. It must not reach `main` unreviewed.

Everywhere else in this repo the expert agents are generic. These files are site-bound
instances, because binding by UUID is the only safe option: at NK a tag like `GT40.PV` or
`Rumstemperatur` recurs hundreds of times, and the generic building-scan tools time out on
a 4,080-sensor building (proved at Fornebu 02.09.2026).

## NK Huset (NK 100, Hamngatan) — building `55885296-a5af-49f6-88f2-d31c5f819e63`

| file | what it is |
|---|---|
| [nk-huset-data-reality-2026-09-13.md](nk-huset-data-reality-2026-09-13.md) | **read first** — what the building can actually sense, measured live 13.09.2026 |
| [nk-huset-embodied-agent.md](nk-huset-embodied-agent.md) | agent spec v0.2 (pre-deploy): comfort, refrigeration, water, energy trend, alarm trend |
| [nk-huset-embodied-weekly-supplement.md](nk-huset-embodied-weekly-supplement.md) | the 101 Wednesday points, kept out of the daily prompt for size |
| [nk_census.py](nk_census.py) | weekly population census: all 334 offices vs setpoint, all ~290 alarm tags, meter dates, dead sensors; appends `nk-census-history.csv` so trends exist (the agent has no memory) |
| [nk-huset-embodied-roster.csv](nk-huset-embodied-roster.csv) | the bound points: `block` = daily / monday / weekly, with UUID and the 13.09 value |
| [nk-huset-sensor-census-2026-09-13.csv](nk-huset-sensor-census-2026-09-13.csv) | all 4,080 sensors with family, room, storey, latest value and age at probe |

Property owner Hufvudstaden AB: `51fae0e3-a66d-41fa-be6c-1f416abb1f2e`.
Onboarding handover (SAIA connector, Lindinvent remap, contacts): Drive
`Onboarding ProptechOS/8. Building discovery/Hufvudstaden/NK Stockholm/handover.md`.

## How the census was made (repeat it before every spec change)

REST, not MCP: `GET https://proptechos.com/api/json/...` with `Authorization: Bearer` **and
`X-Property-Owner: 51fae0e3-…`** (without the header every Hufvudstaden twin is a 404).
Buildings are `realestatecomponent`, not `building`. Paginate `device`, `sensor`, `actuator`
with `building_ids=` at `size=1000`; then `sensor/{id}/observation/latest` for every sensor.

⚠️ **Rate limit: 24 threads produced 1,317 HTTP 429s that a naive script counts as
"never observed".** The first pass showed Saia at 14 % live; the truth is 97 %. Run the
latest sweep at ≤ 6 threads with back-off, and never trust a liveness number whose
script did not check status codes.

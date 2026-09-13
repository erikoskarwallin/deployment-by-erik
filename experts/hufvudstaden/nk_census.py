#!/usr/bin/env python3
"""NK Huset weekly census — the population numbers the agent cannot produce itself.

Answers, for ALL sensors (not the agent's roster):
  * liveness per data family              * offices outside setpoint (all 334) and CO2 > 1000
  * active alarm tags (all ~290) + count  * water/energy meters: newest bucket date and value
  * dead sensors (> 30 d)
and appends one row per run to nk-census-history.csv so day-over-day alarm and deviation
trends exist somewhere (the agent has no memory of its previous run).

Usage:  PROPTECHOS_TOKEN=<1-h bearer> python3 nk_census.py [--out DIR]
Built 13.09.2026 from the scripts that produced nk-huset-sensor-census-2026-09-13.csv.
⚠️ Not yet run end-to-end as one file (the token expired); every block ran separately that day.
"""
import os,sys,json,csv,time,re,collections,argparse,datetime as dt,warnings
import requests,concurrent.futures as cf
warnings.filterwarnings("ignore")
B="https://proptechos.com/api/json"
PO="51fae0e3-a66d-41fa-be6c-1f416abb1f2e"          # Hufvudstaden AB
BLD="55885296-a5af-49f6-88f2-d31c5f819e63"         # NK Stockholm (RealEstateComponent)
TOK=os.environ.get("PROPTECHOS_TOKEN") or sys.exit("set PROPTECHOS_TOKEN")
H={"Authorization":f"Bearer {TOK}","X-Property-Owner":PO,"User-Agent":"curl/8.0"}
ap=argparse.ArgumentParser(); ap.add_argument("--out",default=os.path.dirname(os.path.abspath(__file__))); ap.add_argument("--threads",type=int,default=6)
A=ap.parse_args(); OUT=A.out; NOW=dt.datetime.now(dt.timezone.utc)

def pages(path,params):
    out=[];page=0
    while True:
        r=requests.get(B+path,headers=H,params={**params,"size":1000,"page":page},timeout=120); r.raise_for_status()
        d=r.json(); out+=d.get("content",[])
        if page>=d.get("totalPages",1)-1: return out
        page+=1
def ptime(t): return dt.datetime.fromisoformat(re.sub(r"(\.\d{6})\d+",r"\1",t).replace("Z","+00:00"))
def latest(sid):
    for i in range(6):
        try:
            r=requests.get(f"{B}/sensor/{sid}/observation/latest",headers=H,timeout=30)
            if r.status_code==200: return sid,r.json()
            if r.status_code==429: time.sleep(1.5*(i+1)); continue
            return sid,{"_status":r.status_code}
        except Exception: time.sleep(1)
    return sid,{"_status":429}
def fam(s):
    src=s.get("source") or {}
    if src.get("system")=="Lindinvent": return "Lindinvent"
    if any(k in src for k in ("meterKey","metryMeterId","InstallationId")): return "Mestro"
    if "sbusStation" in src or src.get("plc"): return "Saia"
    if "modbusNodeId" in src: return "Modbus"
    lit=s.get("littera") or ""
    if re.search(r"[0-9A-F]{16}$",lit) or lit.startswith("ST01ERS"): return "LoRa"
    return "other"

print("inventory…",flush=True)
sen=pages("/sensor",{"building_ids":BLD}); print(len(sen),"sensors")
bc=pages("/buildingcomponent",{"building_ids":BLD}); st={b["id"]:b for b in bc if b.get("class")=="Storey"}
room={b["id"]:(b.get("popularName") or "",b.get("littera") or "",st.get(b.get("hasSuperBuildingComponent"),{}).get("littera") or "") for b in bc}
print("latest sweep at",A.threads,"threads…",flush=True)
lat={}
with cf.ThreadPoolExecutor(A.threads) as ex:
    for i,(k,v) in enumerate(ex.map(latest,[s["id"] for s in sen])):
        lat[k]=v
        if i%500==0: print(" ",i,flush=True)
codes=collections.Counter(v.get("_status") for v in lat.values()); print("status codes:",dict(codes))
if codes.get(429): print("⚠️ 429s remain — liveness below is UNDERSTATED; rerun with fewer threads")

rows=[]
for s in sen:
    l=lat.get(s["id"],{}); t=l.get("observationTime")
    age=(NOW-ptime(t)).total_seconds()/3600 if t else None
    rn,rl,stn=room.get(s.get("isMountedInBuildingComponent"),("","",""))
    rows.append(dict(family=fam(s),system=(s.get("source") or {}).get("systemname") or (s.get("source") or {}).get("system") or "",
        littera=s.get("littera"),popularName=s.get("popularName"),srcname=(s.get("source") or {}).get("name"),
        quantityKind=(s.get("deviceQuantityKind") or "").split("/")[-1],placement=(s.get("devicePlacementContext") or "").split("/")[-1],
        room_name=rn,room_littera=rl,storey=stn,sensor_id=s["id"],parent=s.get("hasSuperDevice"),value=l.get("value"),
        obs_time=t,age_h=None if age is None else round(age,1),http=l.get("_status")))
stamp=NOW.strftime("%Y-%m-%d")
with open(f"{OUT}/nk-huset-sensor-census-{stamp}.csv","w",newline="") as f:
    w=csv.DictWriter(f,fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)
live=lambda r: r["age_h"] is not None and r["age_h"]<26

# --- population answers
rep={"date":stamp}
print("\n== liveness per family")
for fm,n in collections.Counter(r["family"] for r in rows).most_common():
    lv=sum(1 for r in rows if r["family"]==fm and live(r)); rep[f"live_{fm}"]=lv; print(f"  {fm:12s} {lv}/{n}")
per=collections.defaultdict(dict)
for r in rows:
    if r["family"]=="Lindinvent" and live(r): per[r["parent"]][r["srcname"]]=r
dev=[]
for p,v in per.items():
    if "Rumstemperatur" in v and "Rumstemperatur BV" in v and v["Rumstemperatur"]["value"] is not None and v["Rumstemperatur BV"]["value"]:
        d=v["Rumstemperatur"]["value"]-v["Rumstemperatur BV"]["value"]
        dev.append((abs(d),d,v["Rumstemperatur"]["room_name"],v["Rumstemperatur"]["room_littera"],v["Rumstemperatur"]["storey"],v["Rumstemperatur"]["value"],v["Rumstemperatur BV"]["value"]))
dev.sort(reverse=True)
rep["rooms_with_setpoint"]=len(dev); rep["rooms_dev_ge_1p5"]=sum(1 for x in dev if x[0]>=1.5); rep["rooms_dev_ge_3"]=sum(1 for x in dev if x[0]>=3)
co2=[v["Koldioxidhalt"]["value"] for v in per.values() if "Koldioxidhalt" in v and v["Koldioxidhalt"]["value"] is not None]
rep["co2_rooms"]=len(co2); rep["co2_gt_1000"]=sum(1 for x in co2 if x>1000); rep["co2_max"]=max(co2) if co2 else None
print(f"\n== offices: {len(dev)} rooms with temp+setpoint · |dev|≥1.5 K: {rep['rooms_dev_ge_1p5']} · ≥3 K: {rep['rooms_dev_ge_3']} · CO2>1000: {rep['co2_gt_1000']} of {len(co2)} (max {rep['co2_max']})")
for x in dev[:10]: print(f"   {x[1]:+5.1f} K  {x[2]} {x[3]} ({x[4]})  {x[5]} vs {x[6]}")
al=[r for r in rows if r["quantityKind"] in ("AlarmMinor","AlarmMajor","CapabilityTypeAlarm") and live(r)]
act=[r for r in al if r["value"] not in (0,0.0,None)]
rep["alarm_tags_live"]=len(al); rep["alarm_active"]=len(act)
print(f"\n== alarms: {len(act)} active of {len(al)} live tags")
for r in act: print(f"   {r['littera']} = {r['value']}  {r['popularName']}")
rep["alarm_active_list"]=" ".join(str(r["littera"]) for r in act)
met=[r for r in rows if r["family"]=="Mestro" or (r["quantityKind"]=="Volume" and r["age_h"] is not None)]
ages=[r["age_h"]/24 for r in met if r["age_h"] is not None]
rep["mestro_meters"]=len(met); rep["mestro_min_age_d"]=round(min(ages),1) if ages else None
print(f"\n== meters: {len(met)}, newest bucket {rep['mestro_min_age_d']} d old")
for r in met:
    if any(k in (r["popularName"] or "") for k in ("SVOA","Nödkyla","Ink EL","Fjärrvärme Historik","Solpanel","FF413")):
        print(f"   {r['quantityKind']:17s} {r['popularName'][:48]:48s} {r['value']!s:12s} {str(r['obs_time'])[:10]}")
dead=[r for r in rows if r["age_h"] is None or r["age_h"]>720]
rep["dead_gt_30d"]=len(dead); print(f"\n== dead > 30 d: {len(dead)}", dict(collections.Counter(r['family'] for r in dead)))
hist=f"{OUT}/nk-census-history.csv"; new=not os.path.exists(hist)
with open(hist,"a",newline="") as f:
    w=csv.DictWriter(f,fieldnames=list(rep.keys()))
    if new: w.writeheader()
    w.writerow(rep)
print("\nappended",hist)

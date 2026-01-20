"""
secret_turn_check.py
Read-only evaluator: should the GM offer Option 6 this scene?
"""

from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CLOCKS = ROOT / "clocks" / "skyrim_clocks.json"
POS = ROOT / "state" / "campaign_position.json"

ACT_CLOCK_FOR_ACT = {
    1: "act_01_whiterun_outcome",
    2: "act_02_fronts_shift",
    3: "act_03_city_crisis_wave",
    4: "act_04_siege_preparation",
    5: "act_05_true_enemy",
}

def load_json(p: Path) -> dict:
    try:
        with p.open("r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return {}

def current_act_halfway(clocks: dict, act_num: int) -> bool:
    act = clocks.get("act_clocks", {})
    key = ACT_CLOCK_FOR_ACT.get(act_num)
    if not key or key not in act:
        return False
    c = act[key]
    cur = c.get("current", 0)
    mx = c.get("max", 1)
    return isinstance(cur, int) and isinstance(mx, int) and mx > 0 and (cur / mx) >= 0.5

def any_faction_near_milestone(clocks: dict) -> bool:
    for c in clocks.get("faction_clocks", {}).values():
        cur = c.get("current", 0)
        mx = c.get("max", 0)
        if isinstance(cur, int) and isinstance(mx, int) and mx > 0 and (mx - cur) <= 1:
            return True
    return False

def main() -> None:
    clocks = load_json(CLOCKS)
    pos = load_json(POS) if POS.exists() else {}

    try:
        act_num = int(pos.get("current_act", 0) or 0)
    except Exception:
        act_num = 0

    eligible = False
    reasons = []

    thalmor = clocks.get("master_clocks", {}).get("thalmor_influence", {})
    thalmor_cur = thalmor.get("current", 0)
    if isinstance(thalmor_cur, int) and thalmor_cur >= 3:
        eligible = True
        reasons.append("Thalmor Influence >= 3")

    if current_act_halfway(clocks, act_num):
        eligible = True
        reasons.append("Current Act clock is halfway+")
    if any_faction_near_milestone(clocks):
        eligible = True
        reasons.append("A faction clock is within 1 tick of a milestone")

    loc = (pos.get("current_location") or "").lower()
    if any(k in loc for k in ["ruin", "barrow", "dwemer", "shrine", "crypt", "tomb", "ancient"]):
        eligible = True
        reasons.append("Mythic/ancient location flag")

    print("Secret Turn Eligible:", "YES" if eligible else "NO")
    if reasons:
        print("Reasons:", ", ".join(reasons))

if __name__ == "__main__":
    main()

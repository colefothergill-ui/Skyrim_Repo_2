"""
dragonbreak_cue.py
Detects soft-cues before Dragonbreak moments. Read-only evaluator.
"""

import json
from pathlib import Path
from typing import Dict, Any, List, Optional

ROOT = Path(__file__).resolve().parents[1]
STATE_FILE = ROOT / "state" / "campaign_state.json"
POS_FILE = ROOT / "state" / "campaign_position.json"
CLOCKS_FILE = ROOT / "clocks" / "skyrim_clocks.json"
MOMENTS_FILE = ROOT / "story_branches" / "DRAGONBREAK_MOMENTS.json"

ACT_CLOCK_FOR_ACT = {
    1: "act_01_whiterun_outcome",
    2: "act_02_fronts_shift",
    3: "act_03_city_crisis_wave",
    4: "act_04_siege_preparation",
    5: "act_05_true_enemy",
}

def load_json(path: Path) -> Optional[dict]:
    if not path.exists():
        return None
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception as e:
        print(f"Warning: Failed to read {path}: {e}")
        return None

def check_clocks(clocks_data: Dict[str, Any], current_act: int) -> List[str]:
    triggers: List[str] = []

    master = clocks_data.get("master_clocks", {})
    for clock_name, clock_data in master.items():
        cur = clock_data.get("current", 0)
        mx = clock_data.get("max", 1)
        if isinstance(cur, int) and isinstance(mx, int) and mx > 0 and cur >= (mx * 0.75):
            triggers.append(f"Master clock '{clock_name}' at {cur}/{mx} (>=75%)")

    act = clocks_data.get("act_clocks", {})
    act_key = ACT_CLOCK_FOR_ACT.get(current_act)
    if act_key and act_key in act:
        clock_data = act.get(act_key, {})
        cur = clock_data.get("current", 0)
        mx = clock_data.get("max", 1)
        if isinstance(cur, int) and isinstance(mx, int) and mx > 0 and (cur / mx) >= 0.5:
            triggers.append(f"Act clock '{act_key}' at {cur}/{mx} (>=50%)")

    faction = clocks_data.get("faction_clocks", {})
    for clock_name, clock_data in faction.items():
        cur = clock_data.get("current", 0)
        mx = clock_data.get("max", 0)
        if isinstance(cur, int) and isinstance(mx, int) and mx > 0 and (mx - cur) <= 1:
            triggers.append(f"Faction clock '{clock_name}' at {cur}/{mx} (1 tick from complete)")

    return triggers

def check_location(state_data: Dict[str, Any]) -> List[str]:
    triggers = []
    loc = str(state_data.get("current_location", "")).lower()
    mythic_keywords = ["ruin", "ruins", "barrow", "dwemer", "dwarven", "shrine", "ancient", "hidden", "crypt", "tomb"]
    if any(k in loc for k in mythic_keywords):
        triggers.append(f"Mythic location cue: '{state_data.get('current_location','')}'")
    return triggers

def check_module_moments(pos: Dict[str, Any], moments: Dict[str, Any]) -> List[str]:
    out: List[str] = []
    if not moments:
        return out
    act = pos.get("current_act")
    scene = pos.get("current_scene_id", "")
    for m in moments.get("moments", []):
        if m.get("act") != act:
            continue
        scene_ids = m.get("scene_ids", [])
        if scene_ids and scene in scene_ids:
            out.append(f"Module Dragonbreak: {m.get('id')} — {m.get('title')}")
    return out

def main() -> None:
    state = load_json(STATE_FILE) or {}
    pos = load_json(POS_FILE) or {}
    clocks = load_json(CLOCKS_FILE) or {}
    moments = load_json(MOMENTS_FILE) or {}

    try:
        current_act = int(pos.get("current_act", 0) or 0)
    except Exception:
        current_act = 0

    triggers: List[str] = []
    triggers += check_clocks(clocks, current_act)
    triggers += check_location(state)
    triggers += check_module_moments(pos, moments)

    print("=" * 70)
    print("Dragonbreak Cue Check")
    print("=" * 70)

    if triggers:
        print("\nDRAGONBREAK CUE DETECTED")
        print("Offer a Secret Turn / Elder Scrolls Moment at the next decision point.\n")
        print("Triggers:")
        for t in triggers:
            print(f"- {t}")
        if moments:
            print("\nSee: story_branches/DRAGONBREAK_MOMENTS.json")
            print("See: story_branches/SECRET_TURNS.md")
    else:
        print("No Dragonbreak conditions met at this time.")
    print("=" * 70)

if __name__ == "__main__":
    main()

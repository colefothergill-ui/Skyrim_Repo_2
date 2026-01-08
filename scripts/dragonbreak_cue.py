"""
dragonbreak_cue.py
Detects soft-cues before Dragonbreak moments.

Usage:
  python scripts/dragonbreak_cue.py

Behavior:
- Checks campaign state and clocks for Dragonbreak eligibility
- ALSO checks module-scene keyed dragonbreak moments (if story_branches/DRAGONBREAK_MOMENTS.json exists)
- Suggests Dragonbreak moments when conditions are met
- Does not modify any repository files (read-only)
"""

import json
from pathlib import Path
from typing import Dict, Any, List, Optional

ROOT = Path(__file__).resolve().parents[1]
STATE_FILE = ROOT / "state" / "campaign_state.json"
POS_FILE = ROOT / "state" / "campaign_position.json"
CLOCKS_FILE = ROOT / "clocks" / "skyrim_clocks.json"
MOMENTS_FILE = ROOT / "story_branches" / "DRAGONBREAK_MOMENTS.json"

DRAGONBREAK_SCENE_PREFIX = """\n⚠️  DRAGONBREAK CUE DETECTED\nOffer a Secret Turn / Elder Scrolls Moment at the next decision point.\n"""

def load_json(path: Path) -> Optional[dict]:
    if not path.exists():
        return None
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        print(f"Warning: Failed to parse {path}: {e}")
        return None
    except Exception as e:
        print(f"Warning: Error reading {path}: {e}")
        return None

def check_clocks(clocks_data: Dict[str, Any]) -> List[str]:
    triggers = []

    master = clocks_data.get("master_clocks", {})
    for clock_name, clock_data in master.items():
        current = clock_data.get("current", 0)
        max_val = clock_data.get("max", 1)
        threshold = max_val * 0.75  # 75% or more
        if current >= threshold:
            triggers.append(f"Master clock '{clock_name}' at {current}/{max_val} (≥75%)")

    act = clocks_data.get("act_clocks", {})
    for clock_name, clock_data in act.items():
        current = clock_data.get("current", 0)
        max_val = clock_data.get("max", 1)
        threshold = max_val * 0.5  # 50% or more
        if current >= threshold:
            triggers.append(f"Act clock '{clock_name}' at {current}/{max_val} (≥50%)")

    faction = clocks_data.get("faction_clocks", {})
    for clock_name, clock_data in faction.items():
        current = clock_data.get("current", 0)
        max_val = clock_data.get("max", 1)
        if current >= max_val - 1:
            triggers.append(f"Faction clock '{clock_name}' at {current}/{max_val} (1 tick from complete)")

    return triggers

def check_location(state_data: Dict[str, Any]) -> List[str]:
    triggers = []
    loc = str(state_data.get("current_location", "")).lower()
    mythic_keywords = [
        "ruin", "ruins", "barrow", "dwemer", "dwarven", "shrine",
        "ancient", "forgotten", "hidden", "cursed", "forbidden",
        "temple", "sanctuary", "crypt", "tomb"
    ]
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

    triggers: List[str] = []
    triggers += check_clocks(clocks)
    triggers += check_location(state)
    triggers += check_module_moments(pos, moments)

    print("=" * 70)
    print("Dragonbreak Cue Check")
    print("=" * 70)

    if triggers:
        print(DRAGONBREAK_SCENE_PREFIX)
        print("Triggers:")
        for t in triggers:
            print(f"- {t}")
        if moments:
            print("\nSee: story_branches/DRAGONBREAK_MOMENTS.json")
            print("See: story_branches/SECRET_TURNS.md")
    else:
        print("No Dragonbreak conditions met at this time.")
        print()
        print("Dragonbreak moments should only appear when:")
        print("  • A major/act clock is high")
        print("  • A faction clock is near completion")
        print("  • The location is ancient/mythic/hidden")
        print("  • OR the module-scene calls for a Dragonbreak moment")

    print("=" * 70)

if __name__ == "__main__":
    main()

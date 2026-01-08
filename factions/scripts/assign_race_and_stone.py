"""
assign_race_and_stone.py
Assign a Race Extra and Standing Stone Extra to the active PC.

Usage:
  python scripts/assign_race_and_stone.py --race nord --stone warrior
  python scripts/assign_race_and_stone.py --race breton --stone mage --pc "Eltric Stagborne"

Notes:
- This updates: state/pc_profile.json
- Data sources:
  - state/race_extras.json
  - state/standing_stones.json
"""

from __future__ import annotations
import argparse
import json
from pathlib import Path
from typing import Any, Dict

ROOT = Path(__file__).resolve().parents[1]
STATE = ROOT / "state"

def load_json(path: Path) -> Dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))

def save_json(path: Path, data: Dict[str, Any]) -> None:
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

def normalize(s: str) -> str:
    return s.strip().lower().replace(" ", "_").replace("-", "_")

def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--race", required=True, help="Race id (e.g., nord, breton, imperial, redguard, altmer, bosmer, dunmer, orc, khajiit, argonian)")
    ap.add_argument("--stone", required=True, help="Stone id (e.g., warrior, mage, thief, lover, shadow, ritual, serpent, steed, tower, lord, lady, apprentice, atronach)")
    ap.add_argument("--pc", default="", help="PC name to target (default: active PC in state/pc_profile.json)")
    args = ap.parse_args()

    pc_path = STATE / "pc_profile.json"
    races_path = STATE / "race_extras.json"
    stones_path = STATE / "standing_stones.json"

    if not pc_path.exists():
        raise SystemExit("Missing state/pc_profile.json")
    if not races_path.exists():
        raise SystemExit("Missing state/race_extras.json")
    if not stones_path.exists():
        raise SystemExit("Missing state/standing_stones.json")

    profile = load_json(pc_path)
    races = load_json(races_path)["races"]
    stones = load_json(stones_path)["stones"]

    race_id = normalize(args.race)
    stone_id = normalize(args.stone)

    race = next((r for r in races if normalize(r["id"]) == race_id), None)
    stone = next((s for s in stones if normalize(s["id"]) == stone_id), None)

    if not race:
        raise SystemExit(f"Unknown race id: {race_id}")
    if not stone:
        raise SystemExit(f"Unknown stone id: {stone_id}")

    pc = profile.get("pc", {})
    if args.pc:
        # Best-effort check: if it doesn't match, we still update the active PC but warn.
        if pc.get("name", "").strip().lower() != args.pc.strip().lower():
            print(f"[WARN] Active PC name is '{pc.get('name','')}', not '{args.pc}'. Updating active PC anyway.")

    pc["race"] = race["name"]
    pc["race_id"] = race["id"]
    pc["standing_stone"] = stone["name"]
    pc["standing_stone_id"] = stone["id"]

    extras = pc.get("extras", [])
    # Add readable entries without duplicating
    race_extra_line = f"Race Extra — {race['name']}: {race['passive']}"
    stone_extra_line = f"Standing Stone — {stone['name']}: {stone['passive']}"
    if race_extra_line not in extras:
        extras.append(race_extra_line)
    if stone_extra_line not in extras:
        extras.append(stone_extra_line)
    pc["extras"] = extras

    profile["pc"] = pc

    # Optionally make these required for your workflow (commented to avoid breaking existing gates)
    # req = profile.get("required_fields", [])
    # for field in ["race", "standing_stone"]:
    #     if field not in req:
    #         req.append(field)
    # profile["required_fields"] = req

    save_json(pc_path, profile)

    print("[OK] Updated active PC:")
    print(f" - Race: {pc['race']} ({pc['race_id']})")
    print(f" - Standing Stone: {pc['standing_stone']} ({pc['standing_stone_id']})")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())

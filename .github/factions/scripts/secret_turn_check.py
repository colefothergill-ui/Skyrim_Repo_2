"""
secret_turn_check.py
Read-only evaluator: should the GM offer Option 6 (Elder Scrolls Moment) this scene?

Usage:
  python scripts/secret_turn_check.py
"""

from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CLOCKS = ROOT / "clocks" / "skyrim_clocks.json"
POS = ROOT / "state" / "campaign_position.json"

def load_json(p: Path) -> dict:
    with p.open("r", encoding="utf-8") as f:
        return json.load(f)

def any_act_halfway(clocks: dict) -> bool:
    for c in clocks.get("act_clocks", {}).values():
        cur = c.get("current", 0)
        mx = c.get("max", 1)
        if isinstance(cur, int) and isinstance(mx, int) and mx > 0 and cur >= (mx // 2):
            return True
    return False

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

    thalmor = clocks.get("master_clocks", {}).get("thalmor_influence", {})
    thalmor_cur = thalmor.get("current", 0)

    eligible = False
    reasons = []

    if isinstance(thalmor_cur, int) and thalmor_cur >= 3:
        eligible = True
        reasons.append("Thalmor Influence ≥ 3")

    if any_act_halfway(clocks):
        eligible = True
        reasons.append("An Act clock is halfway+")
    if any_faction_near_milestone(clocks):
        eligible = True
        reasons.append("A faction clock is within 1 tick of a milestone")

    loc = (pos.get("current_location") or "").lower()
    hold = (pos.get("current_hold") or "").lower()
    if any(k in loc for k in ["ruin", "barrow", "dwemer", "shrine"]) or hold in ["the reach", "reach"]:
        eligible = True
        reasons.append("Mythic/ancient location flag")

    print("Secret Turn Eligible:", "YES" if eligible else "NO")
    if reasons:
        print("Reasons:", ", ".join(reasons))

    print("\nSeed suggestions (choose 1):")
    print("- A hidden mechanism / sealed door reveals a clue (TODO)")
    print("- A masked agent slips: Thalmor shadow thread intensifies (TODO)")
    print("- Markarth tone seed: doors slam + disembodied taunt (Molag Bal vibe) (TODO triggers)")

if __name__ == "__main__":
    main()

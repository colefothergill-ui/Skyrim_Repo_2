"""
on_track.py
Read-only alignment check: are we following the module rails?

Usage:
  python scripts/on_track.py

Outputs:
- PASS/FAIL summary
- If FAIL, exact edits to re-align to `state/startup_defaults.json` (module start)
"""

from __future__ import annotations
import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
STATE = ROOT / "state"
CLOCKS = ROOT / "clocks" / "skyrim_clocks.json"
DEFAULTS = STATE / "startup_defaults.json"

def load_json(path: Path) -> dict:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        return {}
    except json.JSONDecodeError as e:
        print(f"Warning: Invalid JSON in {path}: {e}")
        return {}
    except Exception as e:
        print(f"Warning: Error reading {path}: {e}")
        return {}

def main() -> None:
    issues: list[str] = []
    recs: list[str] = []

    defaults = load_json(DEFAULTS) if DEFAULTS.exists() else {}
    want_act = defaults.get("default_act", 1)
    want_scene = defaults.get("default_scene_id", "S0_CHARACTER_CREATION")
    want_loc = defaults.get("default_location", "Whiterun — Battle of Whiterun (Staging)")
    want_hold = defaults.get("default_hold", "Whiterun")

    pos_path = STATE / "campaign_position.json"
    pc_path = STATE / "pc_profile.json"

    if not pos_path.exists():
        issues.append("Missing state/campaign_position.json")
        recs.append("Run: python scripts/apply_template.py --template MODULE_START_BATTLE_OF_WHITERUN")
    else:
        pos = load_json(pos_path)
        act = pos.get("current_act")
        scene = pos.get("current_scene_id", "")
        hold = pos.get("current_hold", "")
        loc = pos.get("current_location", "")

        if act != want_act:
            issues.append(f"current_act is {act} (expected {want_act} for module start)")
            recs.append(f"Edit state/campaign_position.json: set current_act={want_act}")
        if scene != want_scene:
            issues.append(f"current_scene_id is '{scene}' (expected '{want_scene}' for Session Zero gate)")
            recs.append(f"Edit state/campaign_position.json: set current_scene_id='{want_scene}'")
        if hold != want_hold:
            issues.append(f"current_hold is '{hold}' (expected '{want_hold}')")
            recs.append(f"Edit state/campaign_position.json: set current_hold='{want_hold}'")
        if loc != want_loc:
            issues.append(f"current_location is '{loc}' (expected '{want_loc}')")
            recs.append(f"Edit state/campaign_position.json: set current_location='{want_loc}'")

    if pc_path.exists():
        pc = load_json(pc_path)
        if not pc.get("created", False):
            issues.append("PC creation gate NOT complete (state/pc_profile.json.created=false)")
            recs.append("Complete Session Zero (tools/SESSION_ZERO_GATE.md), then set created=true and fill fields.")
    else:
        issues.append("Missing state/pc_profile.json (cannot enforce Session Zero gate)")
        recs.append("Run: python scripts/apply_template.py --template MODULE_START_BATTLE_OF_WHITERUN")

    # Light clock sanity (optional)
    if CLOCKS.exists():
        clocks = load_json(CLOCKS)
        act_key = f"act_{want_act:02d}_whiterun_outcome" if want_act == 1 else None
        if act_key and act_key not in clocks.get("act_clocks", {}):
            # Don't fail hard; just warn.
            issues.append(f"Clock missing: clocks.skyrim_clocks.json.act_clocks.{act_key} (expected for Act 1)")

    print("=" * 70)
    print("ON-TRACK CHECK")
    print("=" * 70)
    if not issues:
        print("✅ PASS — Vault state matches the module start point.")
    else:
        print("❌ FAIL — Issues detected:")
        for i in issues:
            print(f"- {i}")
        print("\nRecommended fixes:")
        for r in recs:
            print(f"- {r}")
    print("=" * 70)

if __name__ == "__main__":
    main()

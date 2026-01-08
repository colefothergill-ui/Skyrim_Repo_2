"""
build_context.py
Print a GM Context Pack to stdout (read-only).

Combines:
- state/campaign_state.json
- state/campaign_position.json (if present)
- state/pc_profile.json (if present)
- clocks/skyrim_clocks.json
- most recent log file (if any)

Usage:
  python scripts/build_context.py
"""

from __future__ import annotations
import json
from pathlib import Path
from typing import Any, Optional

ROOT = Path(__file__).resolve().parents[1]
CLOCKS = ROOT / "clocks" / "skyrim_clocks.json"
STATE = ROOT / "state"
CAMP = STATE / "campaign_state.json"
POS = STATE / "campaign_position.json"
PC = STATE / "pc_profile.json"
DEFAULTS = STATE / "startup_defaults.json"
LOGS = ROOT / "logs"

def load_json(path: Path) -> Optional[dict]:
    if not path.exists():
        return None
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return None

def newest_log_path() -> Optional[Path]:
    if not LOGS.exists():
        return None
    files = sorted(LOGS.glob("session_*.md"), reverse=True)
    return files[0] if files else None

def find_act_file(act: Any) -> str:
    acts_dir = ROOT / "modules" / "acts"
    if not acts_dir.exists():
        return "modules/acts/ACT_01_BATTLE_OF_WHITERUN.md (start here)"
    if isinstance(act, int):
        matches = sorted(acts_dir.glob(f"ACT_{act:02d}_*.md"))
        if matches:
            return str(matches[0].relative_to(ROOT))
    # fallback
    fallback = acts_dir / "ACT_01_BATTLE_OF_WHITERUN.md"
    return str(fallback.relative_to(ROOT)) if fallback.exists() else "modules/acts/ACT_01_BATTLE_OF_WHITERUN.md (start here)"

def main() -> None:
    state = load_json(CAMP) or {}
    pos = load_json(POS) or {}
    pc = load_json(PC) or {}
    defaults = load_json(DEFAULTS) or {}

    clocks = load_json(CLOCKS) or {}
    log_path = newest_log_path()

    print("=" * 70)
    print("GM CONTEXT PACK")
    print("=" * 70)

    # Startup defaults
    if defaults:
        print("\n## Startup Defaults (when state is missing/blank)")
        print(f"- Start point: {defaults.get('default_start_point')}")
        print(f"- Act: {defaults.get('default_act')} | Scene: {defaults.get('default_scene_id')}")
        print(f"- Location: {defaults.get('default_location')}")

    print("\n## Current Position")
    print(f"- Act: {pos.get('current_act')}")
    print(f"- Scene ID: {pos.get('current_scene_id', '(unset)')}")
    print(f"- Hold: {pos.get('current_hold')}")
    loc = pos.get('current_location') or state.get('current_location')
    print(f"- Location: {loc}")

    # Session Zero Gate
    created = bool(pc.get("created", False))
    print("\n## Session Zero Gate")
    if not created:
        print("❗ STOP — PC not created yet.")
        req = (pc.get("required_fields") or defaults.get("pc_creation_gate", {}).get("required_fields") or [])
        if req:
            print("- Required fields:", ", ".join(req))
        print("- See: tools/SESSION_ZERO_GATE.md")
        print("- Active PC sheet:", pc.get("active_pc_file", "pcs/PC_MAIN.md"))
    else:
        print("✅ PC created.")
        pcdata = pc.get("pc", {})
        if pcdata:
            print(f"- Name: {pcdata.get('name')}")
            print(f"- Affiliation: {pcdata.get('affiliation_primary')} ({pcdata.get('starting_role')})")

    print("\n## Party/Flags")
    print(f"- Party: {state.get('party',{})}")
    print(f"- Flags: {state.get('major_flags',{})}")

    print("\n## Key Clocks (master)")
    for k, v in clocks.get("master_clocks", {}).items():
        print(f"- {k}: {v.get('current',0)}/{v.get('max',0)}")

    print("\n## Suggested next files to open")
    print(f"- {find_act_file(pos.get('current_act'))}")
    print("- story_branches/BRANCH_MATRIX.md")
    print("- tools/STARTUP_PROTOCOL.md")
    print("- tools/ON_TRACK_PROTOCOL.md")
    print("- tools/DRAGONBREAK_PROTOCOL.md")

    if log_path:
        print("\n## Most recent log")
        print(f"- {log_path.name}")

    print("=" * 70)

if __name__ == "__main__":
    main()

"""
build_context.py
Print a GM Context Pack to stdout (read-only) or save to file.

Combines:
- state/campaign_state.json
- state/campaign_position.json (if present)
- state/pc_profile.json (if present)
- clocks/skyrim_clocks.json
- most recent log file (if any)
- relevant location/module files

Usage:
  python scripts/build_context.py                    # Print to stdout
  python scripts/build_context.py --output FILE.md   # Save to file
  python scripts/build_context.py --chatgpt          # ChatGPT optimized format
"""

from __future__ import annotations

import sys
try:
    sys.stdout.reconfigure(errors="replace")
    sys.stderr.reconfigure(errors="replace")
except Exception:
    pass
import json
import argparse
from pathlib import Path
from typing import Any, Optional, TextIO

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

def newest_log_path(pos: Optional[dict] = None) -> Optional[Path]:
    """
    Find the most recent log file.
    Prioritizes the 'last_log' field from campaign_position.json if available,
    otherwise falls back to scanning for session_*.md files.
    """
    if not LOGS.exists():
        return None
    
    # Check if campaign_position.json has a last_log field
    if pos and "last_log" in pos:
        last_log = pos["last_log"]
        log_file = LOGS / last_log
        if log_file.exists():
            return log_file
    
    # Fallback: scan for all session/log files with both naming patterns
    all_files = []
    all_files.extend(LOGS.glob("session_*.md"))
    all_files.extend(LOGS.glob("*_session-*_*.md"))
    # Filter out template files and sort by name in reverse order
    all_files = [f for f in all_files if "TEMPLATE" not in f.name.upper()]
    return sorted(all_files, reverse=True)[0] if all_files else None

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
    parser = argparse.ArgumentParser(description="Build GM context bundle")
    parser.add_argument("--output", "-o", help="Output file path (default: stdout)")
    parser.add_argument("--chatgpt", action="store_true", help="Format for ChatGPT integration")
    args = parser.parse_args()

    state = load_json(CAMP) or {}
    pos = load_json(POS) or {}
    pc = load_json(PC) or {}
    defaults = load_json(DEFAULTS) or {}

    clocks = load_json(CLOCKS) or {}
    log_path = newest_log_path(pos)

    # Determine output destination
    out: TextIO
    if args.output:
        out = open(args.output, 'w', encoding='utf-8')
    else:
        out = sys.stdout

    try:
        if args.chatgpt:
            _print_chatgpt_format(out, state, pos, pc, defaults, clocks, log_path)
        else:
            _print_standard_format(out, state, pos, pc, defaults, clocks, log_path)
    finally:
        if args.output:
            out.close()
            print(f"Context bundle written to: {args.output}", file=sys.stderr)

def _print_standard_format(out: TextIO, state: dict, pos: dict, pc: dict, defaults: dict, clocks: dict, log_path: Optional[Path]) -> None:
    """Original format for console output"""
    print("=" * 70, file=out)
    print("GM CONTEXT PACK", file=out)
    print("=" * 70, file=out)

    # Startup defaults
    if defaults:
        print("\n## Startup Defaults (when state is missing/blank)", file=out)
        print(f"- Start point: {defaults.get('default_start_point')}", file=out)
        print(f"- Act: {defaults.get('default_act')} | Scene: {defaults.get('default_scene_id')}", file=out)
        print(f"- Location: {defaults.get('default_location')}", file=out)

    print("\n## Current Position", file=out)
    print(f"- Act: {pos.get('current_act')}", file=out)
    print(f"- Scene ID: {pos.get('current_scene_id', '(unset)')}", file=out)
    print(f"- Hold: {pos.get('current_hold')}", file=out)
    loc = pos.get('current_location') or state.get('current_location')
    print(f"- Location: {loc}", file=out)

    # Session Zero Gate
    created = bool(pc.get("created", False))
    print("\n## Session Zero Gate", file=out)
    if not created:
        print(" -  STOP  PC not created yet.", file=out)
        req = (pc.get("required_fields") or defaults.get("pc_creation_gate", {}).get("required_fields") or [])
        if req:
            print("- Required fields:", ", ".join(req), file=out)
        print("- See: tools/SESSION_ZERO_GATE.md", file=out)
        print("- Active PC sheet:", pc.get("active_pc_file", "pcs/PC_MAIN.md"), file=out)
    else:
        print(" PC created.", file=out)
        pcdata = pc.get("pc", {})
        if pcdata:
            print(f"- Name: {pcdata.get('name')}", file=out)
            print(f"- Affiliation: {pcdata.get('affiliation_primary')} ({pcdata.get('starting_role')})", file=out)

    print("\n## Party/Flags", file=out)
    print(f"- Party: {state.get('party',{})}", file=out)
    print(f"- Flags: {state.get('major_flags',{})}", file=out)

    print("\n## Key Clocks (master)", file=out)
    for k, v in clocks.get("master_clocks", {}).items():
        print(f"- {k}: {v.get('current',0)}/{v.get('max',0)}", file=out)

    print("\n## Suggested next files to open", file=out)
    print(f"- {find_act_file(pos.get('current_act'))}", file=out)
    print("- story_branches/BRANCH_MATRIX.md", file=out)
    print("- tools/STARTUP_PROTOCOL.md", file=out)
    print("- tools/ON_TRACK_PROTOCOL.md", file=out)
    print("- tools/DRAGONBREAK_PROTOCOL.md", file=out)

    if log_path:
        print("\n## Most recent log", file=out)
        print(f"- {log_path.name}", file=out)

    print("=" * 70, file=out)

def _print_chatgpt_format(out: TextIO, state: dict, pos: dict, pc: dict, defaults: dict, clocks: dict, log_path: Optional[Path]) -> None:
    """ChatGPT-optimized format with full content"""
    print("# Skyrim Fate Core Campaign — Session Context Bundle\n", file=out)
    print("**Campaign Era**: 4E 201 — Civil War Active, Dragonborn Absent\n", file=out)
    print("---\n", file=out)

    # Current Position
    print("## Current Campaign Position\n", file=out)
    print(f"- **Act**: {pos.get('current_act', defaults.get('default_act', 1))}", file=out)
    print(f"- **Scene ID**: {pos.get('current_scene_id', defaults.get('default_scene_id', 'S0_CHARACTER_CREATION'))}", file=out)
    print(f"- **Hold**: {pos.get('current_hold', defaults.get('default_hold', 'Whiterun'))}", file=out)
    loc = pos.get('current_location') or state.get('current_location') or defaults.get('default_location', 'Unknown')
    print(f"- **Location**: {loc}", file=out)
    print()

    # Party State
    print("## Party State\n", file=out)
    party = state.get('party', {})
    print(f"- **Alignment**: {party.get('alignment', 'unaligned')}", file=out)
    allies = party.get('allies', [])
    if allies:
        print(f"- **Allies**: {', '.join(allies)}", file=out)
    enemies = party.get('enemies', [])
    if enemies:
        print(f"- **Enemies**: {', '.join(enemies)}", file=out)
    print()

    # PC Info
    print("## Player Character\n", file=out)
    created = bool(pc.get("created", False))
    if created:
        pcdata = pc.get("pc", {})
        print(f"- **Name**: {pcdata.get('name', 'Unknown')}", file=out)
        print(f"- **High Concept**: {pcdata.get('high_concept', 'Not set')}", file=out)
        print(f"- **Trouble**: {pcdata.get('trouble', 'Not set')}", file=out)
        print(f"- **Affiliation**: {pcdata.get('affiliation_primary', 'Unknown')}", file=out)
        print(f"- **Role**: {pcdata.get('starting_role', 'Unknown')}", file=out)
        print(f"- **Active Sheet**: {pc.get('active_pc_file', 'pcs/PC_MAIN.md')}", file=out)
    else:
        print("⚠️ **Session Zero NOT Complete** — PC creation required", file=out)
        print(f"- See: tools/SESSION_ZERO_GATE.md", file=out)
    print()

    # Major Flags
    print("## Major Campaign Flags\n", file=out)
    flags = state.get('major_flags', {})
    if flags:
        for flag, value in sorted(flags.items()):
            status = "✓" if value else "✗"
            print(f"- {status} `{flag}`: {value}", file=out)
    else:
        print("- No major flags set", file=out)
    print()

    # Hold Control
    print("## Hold Control\n", file=out)
    holds = state.get('holds', {})
    if holds:
        for hold, data in sorted(holds.items()):
            control = data.get('control', 'unknown')
            morale = data.get('morale', 'unknown')
            status = data.get('status', 'normal')
            print(f"- **{hold}**: {control.title()} control | Morale: {morale} | Status: {status}", file=out)
    else:
        print("- No hold control data", file=out)
    print()

    # Master Clocks
    print("## Master Clocks\n", file=out)
    master = clocks.get("master_clocks", {})
    if master:
        for name, data in sorted(master.items()):
            curr = data.get('current', 0)
            max_val = data.get('max', 0)
            note = data.get('note', '')
            progress = "█" * curr + "░" * (max_val - curr)
            print(f"- **{name}**: [{progress}] {curr}/{max_val}", file=out)
            if note:
                print(f"  - _{note}_", file=out)
    print()

    # Act Clocks
    print("## Act Clocks\n", file=out)
    act_clocks = clocks.get("act_clocks", {})
    if act_clocks:
        current_act = pos.get('current_act', 1)
        for name, data in sorted(act_clocks.items()):
            curr = data.get('current', 0)
            max_val = data.get('max', 0)
            note = data.get('note', '')
            progress = "█" * curr + "░" * (max_val - curr)
            # Highlight current act clock
            marker = "⚡" if f"act_{current_act:02d}_" in name or f"act_0{current_act}_" in name else " "
            print(f"{marker} **{name}**: [{progress}] {curr}/{max_val}", file=out)
            if note:
                print(f"  - _{note}_", file=out)
    print()

    # Faction Clocks (top 5 most advanced)
    print("## Faction Clocks (Most Active)\n", file=out)
    faction_clocks = clocks.get("faction_clocks", {})
    if faction_clocks:
        sorted_factions = sorted(
            faction_clocks.items(),
            key=lambda x: x[1].get('current', 0) / max(x[1].get('max', 1), 1),
            reverse=True
        )[:5]
        for name, data in sorted_factions:
            curr = data.get('current', 0)
            max_val = data.get('max', 0)
            note = data.get('note', '')
            progress = "█" * curr + "░" * (max_val - curr)
            print(f"- **{name}**: [{progress}] {curr}/{max_val}", file=out)
            if note:
                print(f"  - _{note}_", file=out)
    print()

    # Personal Clocks (if any)
    personal = clocks.get("personal_clocks", {})
    if personal:
        print("## Personal Clocks\n", file=out)
        for name, data in sorted(personal.items()):
            curr = data.get('current', 0)
            max_val = data.get('max', 0)
            note = data.get('note', '')
            progress = "█" * curr + "░" * (max_val - curr)
            print(f"- **{name}**: [{progress}] {curr}/{max_val}", file=out)
            if note:
                print(f"  - _{note}_", file=out)
        print()

    # Latest Session Summary
    if log_path and log_path.exists():
        print("## Latest Session Summary\n", file=out)
        print(f"**Session**: {log_path.stem}\n", file=out)
        try:
            log_content = log_path.read_text(encoding='utf-8')
            # Extract first section (usually the chronicle)
            lines = log_content.split('\n')
            in_chronicle = False
            chronicle_lines = []
            for line in lines:
                if '## Save Game' in line or '## In-World Chronicle' in line:
                    in_chronicle = True
                    continue
                elif in_chronicle and line.startswith('##'):
                    break
                elif in_chronicle:
                    chronicle_lines.append(line)
            
            if chronicle_lines:
                print('\n'.join(chronicle_lines[:20]))  # First 20 lines of chronicle
                print(file=out)
        except Exception:
            print(f"_(Could not read log file)_", file=out)
            print(file=out)

    # Relevant Files to Load
    print("## Relevant Files for This Session\n", file=out)
    print("Load these files for full context:\n", file=out)
    print(f"1. `MASTER_KEY.md` — Campaign premise and pillars", file=out)
    print(f"2. `{find_act_file(pos.get('current_act'))}` — Current act structure", file=out)
    print(f"3. `rules/fate_core_quickref.md` — Fate Core rules reference", file=out)
    print(f"4. `story_branches/DRAGONBREAK_MOMENTS.json` — Special moment triggers", file=out)
    if created:
        print(f"5. `{pc.get('active_pc_file', 'pcs/PC_MAIN.md')}` — Full PC sheet", file=out)
    print()

    print("---\n", file=out)
    print("**Context bundle generated**: Auto-generated for ChatGPT campaign tracking", file=out)
    print("**Use this bundle to**: Track mechanics, narrate outcomes, maintain continuity", file=out)

if __name__ == "__main__":
    main()

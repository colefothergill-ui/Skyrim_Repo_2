"""
apply_template.py
Apply a state template into /state (write operation).

Usage:
  python scripts/apply_template.py --template MODULE_START_BATTLE_OF_WHITERUN

Behavior:
- Copies template files into /state/
- Supports patch JSON (campaign_state.patch.json) by merging into existing campaign_state.json
- Writes pc_profile.json + active_pc.json when present
"""

from __future__ import annotations
import argparse
import json
from pathlib import Path
import shutil

ROOT = Path(__file__).resolve().parents[1]
STATE = ROOT / "state"
TEMPLATES = STATE / "templates"

def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))

def dump_json(path: Path, data: dict) -> None:
    path.write_text(json.dumps(data, indent=2), encoding="utf-8")

def deep_merge(dst: dict, src: dict) -> dict:
    for k, v in src.items():
        if isinstance(v, dict) and isinstance(dst.get(k), dict):
            dst[k] = deep_merge(dst[k], v)
        else:
            dst[k] = v
    return dst

def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--template", required=True, help="Template folder name under state/templates/")
    args = ap.parse_args()

    tpl = TEMPLATES / args.template
    if not tpl.exists():
        raise SystemExit(f"Template not found: {tpl}")

    print(f"Applying template: {tpl}")

    # Merge campaign_state patch if present
    campaign_state_path = STATE / "campaign_state.json"
    patch_path = tpl / "campaign_state.patch.json"
    if patch_path.exists():
        base = load_json(campaign_state_path) if campaign_state_path.exists() else {}
        patch = load_json(patch_path)
        merged = deep_merge(base, patch)
        dump_json(campaign_state_path, merged)
        print(f"  ✓ merged campaign_state.json ({patch_path.name})")

    # Straight copies
    for name in ["campaign_position.json", "party_state.json", "quest_flags.json", "pc_profile.json", "active_pc.json"]:
        src = tpl / name
        if not src.exists():
            continue
        dst = STATE / name
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, dst)
        print(f"  ✓ copied {name}")

    print("DONE.")

if __name__ == "__main__":
    main()

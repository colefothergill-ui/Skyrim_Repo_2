#!/usr/bin/env python3
"""
Apply the Whiterun Save Game patch safely:
- Adds a new log file
- Appends a Campaign Obligation to pcs/PC_MAIN.md (if missing)
- Deep-merges JSON patch files into existing JSON without deleting unrelated keys
- Unions allies/enemies arrays to avoid duplication
- Adds/updates a top-level "clocks" section in clocks/skyrim_clocks.json
"""
from __future__ import annotations
import json, os, sys
from pathlib import Path
from datetime import date

ROOT = Path.cwd()

def read_json(path: Path) -> dict:
    if not path.exists():
        raise FileNotFoundError(f"Missing required file: {path}")
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)

def write_json(path: Path, data: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
        f.write("\n")

def deep_merge(dst: dict, src: dict) -> dict:
    """
    Recursively merge src into dst (in place). Dicts merge; other values overwrite.
    """
    for k, v in src.items():
        if isinstance(v, dict) and isinstance(dst.get(k), dict):
            deep_merge(dst[k], v)
        else:
            dst[k] = v
    return dst

def union_list(existing, additions):
    if existing is None:
        existing = []
    if additions is None:
        additions = []
    seen = set()
    out = []
    for item in existing + additions:
        if not isinstance(item, str):
            # keep non-strings as-is, but still avoid exact duplicates
            key = json.dumps(item, sort_keys=True, ensure_ascii=False)
        else:
            key = item
        if key in seen:
            continue
        seen.add(key)
        out.append(item)
    return out

def ensure_pc_obligation(pc_path: Path) -> bool:
    obligation_line = "- Campaign Obligation: Guarantor of Whiterun’s Mercy (Ulfric’s oath is yours to enforce)"
    section_header = "## Campaign Obligations"
    changed = False

    pc_path.parent.mkdir(parents=True, exist_ok=True)
    content = ""
    if pc_path.exists():
        content = pc_path.read_text(encoding="utf-8")
    else:
        # Create a stub if missing
        content = "# Character Sheet\n\n"

    if obligation_line in content:
        return False

    # Append a clean section at end (least risky)
    append_block = f"\n\n{section_header}\n{obligation_line}\n"
    pc_path.write_text(content.rstrip() + append_block, encoding="utf-8")
    return True

def copy_log(bundle_root: Path, repo_root: Path) -> bool:
    src = bundle_root / "logs" / "session_001_whiterun_flip_gatehouse.md"
    dst = repo_root / "logs" / "session_001_whiterun_flip_gatehouse.md"
    dst.parent.mkdir(parents=True, exist_ok=True)
    if dst.exists():
        # do not overwrite existing logs silently; keep user's version
        return False
    dst.write_text(src.read_text(encoding="utf-8"), encoding="utf-8")
    return True

def main() -> int:
    bundle_root = Path(__file__).resolve().parents[1]  # .../tools/.. = bundle root inside repo
    patch_dir = bundle_root / "patch_data"

    # 1) Log
    log_added = copy_log(bundle_root, ROOT)

    # 2) PC sheet obligation
    pc_changed = ensure_pc_obligation(ROOT / "pcs" / "PC_MAIN.md")

    # 3) Merge state files
    merges = [
        (patch_dir / "campaign_position.merge.json", ROOT / "state" / "campaign_position.json"),
        (patch_dir / "quest_flags.merge.json", ROOT / "state" / "quest_flags.json"),
        (patch_dir / "campaign_state.merge.json", ROOT / "state" / "campaign_state.json"),
        (patch_dir / "skyrim_clocks.merge.json", ROOT / "clocks" / "skyrim_clocks.json"),
    ]

    changed_files = []
    for patch_path, target_path in merges:
        patch = read_json(patch_path)
        if target_path.exists():
            data = read_json(target_path)
        else:
            data = {}

        # Special handling for campaign_state allies/enemies union
        if target_path.name == "campaign_state.json" and isinstance(patch.get("party"), dict):
            existing_party = data.get("party", {}) if isinstance(data.get("party"), dict) else {}
            patch_party = patch.get("party", {})
            # merge everything first
            deep_merge(data, patch)
            # then union allies/enemies
            data.setdefault("party", {})
            data["party"]["allies"] = union_list(existing_party.get("allies"), patch_party.get("allies"))
            data["party"]["enemies"] = union_list(existing_party.get("enemies"), patch_party.get("enemies"))
        else:
            deep_merge(data, patch)

        # Update meta.updated if present in clocks file
        if target_path.name == "skyrim_clocks.json" and isinstance(data.get("meta"), dict):
            data["meta"]["updated"] = str(date.today())

        write_json(target_path, data)
        changed_files.append(str(target_path))

    print("Whiterun Save Game Patch applied.")
    print(f"- Log added: {log_added}")
    print(f"- PC obligation added: {pc_changed}")
    print("- JSON files merged:")
    for p in changed_files:
        print(f"  - {p}")
    return 0

if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as e:
        print(f"ERROR: {e}", file=sys.stderr)
        raise

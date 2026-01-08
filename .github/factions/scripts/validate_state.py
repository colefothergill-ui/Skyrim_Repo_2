"""
validate_state.py
Validate state/campaign_state.json and clocks/skyrim_clocks.json for basic consistency.

Usage:
  python scripts/validate_state.py

Checks:
- Files exist and are valid JSON.
- Clock current values are ints, non-negative, and do not exceed max.
- campaign_state.json has required sections and allowed values.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CLOCKS_PATH = ROOT / "clocks" / "skyrim_clocks.json"
STATE_PATH = ROOT / "state" / "campaign_state.json"

ALLOWED_CONTROL = {"imperial", "stormcloak", "neutral", "contested"}
ALLOWED_ALIGNMENT = {"imperial", "stormcloak", "neutral", "undecided"}

def load_json(path: Path) -> dict:
    try:
        with path.open("r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        raise ValueError(f"Missing file: {path}")
    except json.JSONDecodeError as e:
        raise ValueError(f"Invalid JSON in {path}: {e}")

def validate_clocks(data: dict) -> list[str]:
    errors: list[str] = []
    for section in ("master_clocks", "act_clocks", "faction_clocks", "personal_clocks"):
        clocks = data.get(section)
        if not isinstance(clocks, dict):
            errors.append(f"{section} missing or not an object")
            continue
        for name, clock in clocks.items():
            if not isinstance(clock, dict):
                errors.append(f"{section}.{name} not an object")
                continue
            cur = clock.get("current")
            maxv = clock.get("max")
            if not isinstance(cur, int) or not isinstance(maxv, int):
                errors.append(f"{section}.{name} current/max must be ints")
                continue
            if cur < 0:
                errors.append(f"{section}.{name} current < 0")
            if maxv <= 0:
                errors.append(f"{section}.{name} max <= 0")
            if cur > maxv:
                errors.append(f"{section}.{name} current ({cur}) > max ({maxv})")
    return errors

def validate_campaign_state(state: dict) -> list[str]:
    errors: list[str] = []
    holds = state.get("holds")
    if not isinstance(holds, dict) or not holds:
        errors.append("holds missing or empty")
    else:
        for hold_name, hold in holds.items():
            if not isinstance(hold, dict):
                errors.append(f"holds.{hold_name} not an object")
                continue
            control = hold.get("control")
            if control not in ALLOWED_CONTROL:
                errors.append(f"holds.{hold_name}.control must be one of {sorted(ALLOWED_CONTROL)}")

    flags = state.get("major_flags")
    if not isinstance(flags, dict):
        errors.append("major_flags missing or not an object")
    else:
        for k, v in flags.items():
            if not isinstance(v, bool):
                errors.append(f"major_flags.{k} must be boolean")

    party = state.get("party")
    if not isinstance(party, dict):
        errors.append("party missing or not an object")
    else:
        alignment = party.get("alignment")
        if alignment not in ALLOWED_ALIGNMENT:
            errors.append(f"party.alignment must be one of {sorted(ALLOWED_ALIGNMENT)}")
        for list_key in ("allies", "enemies"):
            v = party.get(list_key)
            if not isinstance(v, list):
                errors.append(f"party.{list_key} must be a list")
    return errors

def main() -> None:
    try:
        clocks = load_json(CLOCKS_PATH)
        state = load_json(STATE_PATH)
    except ValueError as e:
        print(f"VALIDATION FAILED: {e}")
        sys.exit(1)

    errors: list[str] = []
    errors += validate_clocks(clocks)
    errors += validate_campaign_state(state)

    if errors:
        print("VALIDATION FAILED:")
        for e in errors:
            print(f"- {e}")
        sys.exit(1)

    print("OK: state and clocks look consistent.")

if __name__ == "__main__":
    main()

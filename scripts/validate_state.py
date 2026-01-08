"""
validate_state.py
Validate state/STATE.json and clocks/bfa_clocks.json for basic consistency.

Usage:
  python scripts/validate_state.py

Checks:
- Files exist and are valid JSON.
- Clock current values do not exceed max and are non-negative.
- Expected PC fields exist (aspects, skills, fate_points, stress, consequences).
- Fate points are non-negative.
- Stress arrays are boolean lists.
"""

import json
from numbers import Number
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent.parent
STATE_PATH = ROOT / "state" / "STATE.json"
CLOCKS_PATH = ROOT / "clocks" / "bfa_clocks.json"


def is_clock_entry(clock):
  """Return True when a mapping has clock fields 'current' and 'max'."""
  return isinstance(clock, dict) and "current" in clock and "max" in clock


def iter_clock_entries(section, name, clock, errors):
  """Yield (label, clock_dict) pairs for flat or nested clock structures."""
  if not isinstance(clock, dict):
    errors.append(f"{section}:{name} invalid clock format")
    return []
  if is_clock_entry(clock):
    return [(f"{section}:{name}", clock)]
  entries = []
  for inner_name, inner_clock in clock.items():
    if not isinstance(inner_clock, dict):
      errors.append(f"{section}:{name}:{inner_name} invalid clock entry")
      continue
    entries.append((f"{section}:{name}:{inner_name}", inner_clock))
  return entries


def load_json(path: Path):
  """Load JSON from disk or exit with an error message if invalid/missing."""
  if not path.exists():
    print(f"ERROR: Missing file: {path}")
    sys.exit(1)
  try:
    with path.open(encoding="utf-8") as handle:
      return json.load(handle)
  except json.JSONDecodeError as e:
    print(f"ERROR: Invalid JSON in {path}: {e}")
    sys.exit(1)


def check_clocks(data):
  """Validate clock structures for pc_clocks and story_clocks, returning errors."""
  errors = []
  for section in ("pc_clocks", "story_clocks"):
    clocks = data.get(section, {})
    for name, clock in clocks.items():
      for label, entry in iter_clock_entries(section, name, clock, errors):
        cur = entry.get("current")
        maxv = entry.get("max")
        if cur is None or maxv is None:
          errors.append(f"{label} missing current/max")
          continue
        if cur < 0:
          errors.append(f"{label} current < 0")
        if maxv <= 0:
          errors.append(f"{label} max <= 0")
        if cur > maxv:
          errors.append(f"{label} current ({cur}) > max ({maxv})")
  return errors


def check_state(data):
  """Validate state/STATE.json structure, returning a list of error strings."""
  errors = []
  pcs = data.get("pcs", {})
  if not pcs:
    errors.append("No PCs defined in state.")
  for pc_name, pc in pcs.items():
    if "fate_points" not in pc:
      errors.append(f"{pc_name}: fate_points missing")
      fate_points_val = None
    else:
      fate_points_val = pc.get("fate_points")
      if not isinstance(fate_points_val, Number):
        errors.append(f"{pc_name}: fate_points must be a number")
      elif fate_points_val < 0:
        errors.append(f"{pc_name}: fate_points < 0")
    stress = pc.get("stress", {})
    for track in ("physical", "mental"):
      arr = stress.get(track, [])
      if not isinstance(arr, list) or not all(isinstance(x, bool) for x in arr):
        errors.append(f"{pc_name}: stress.{track} must be a list of booleans")
    consequences = pc.get("consequences", {})
    if not isinstance(consequences, dict):
      errors.append(f"{pc_name}: consequences must be an object")
      continue
    for slot in ("mild", "moderate", "severe"):
      if slot not in consequences:
        errors.append(f"{pc_name}: consequences.{slot} missing")
        continue
      val = consequences[slot]
      if val is not None and not isinstance(val, str):
        errors.append(f"{pc_name}: consequences.{slot} must be a string or null")
  return errors


def main():
  state = load_json(STATE_PATH)
  clocks = load_json(CLOCKS_PATH)

  errors = []
  errors += check_clocks(clocks)
  errors += check_state(state)

  if errors:
    print("VALIDATION FAILED:")
    for e in errors:
      print(f"- {e}")
    sys.exit(1)
  print("OK: state and clocks look consistent.")


if __name__ == "__main__":
  main()

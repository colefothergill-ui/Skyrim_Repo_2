"""
flag_daedric_quest.py
Update state/quest_flags.json for a Daedric Prince quest, and optionally tick influence clocks.

Usage:
  python scripts/gm_tools/flag_daedric_quest.py --prince azura --completed true --champion true --artifact "Azura's Star" --tick 1

Behavior:
- Updates: state/quest_flags.json -> daedric[prince]
- Optionally ticks: clocks/daedric_influence_clocks.json

Design Note:
This script is intentionally small and transparent (no magic). It is safe to run repeatedly.
"""

from __future__ import annotations
import argparse
import json
from pathlib import Path
from typing import Any, Dict

ROOT = Path(__file__).resolve().parents[2]
STATE = ROOT / "state"
CLOCKS = ROOT / "clocks"

def load_json(path: Path) -> Dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))

def save_json(path: Path, data: Dict[str, Any]) -> None:
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

def normalize(s: str) -> str:
    return s.strip().lower().replace(" ", "_").replace("-", "_")

def str2bool(v: str) -> bool:
    return v.strip().lower() in ("1", "true", "yes", "y", "on")

PRINCE_TO_CLOCK = {
    "azura": "azura_twilight_omens",
    "boethiah": "boethiah_proving_ground",
    "clavicus_vile": "clavicus_vile_bargains",
    "hermaeus_mora": "hermaeus_mora_whispers",
    "hircine": "hircine_the_hunt",
    "malacath": "malacath_grudges",
    "mehrunes_dagon": "mehrunes_dagon_embers",
    "mephala": "mephala_paranoia",
    "meridia": "meridia_crusade",
    "molag_bal": "molag_bal_chains",
    "namira": "namira_rot",
    "nocturnal": "nocturnal_shadows",
    "peryite": "peryite_plague",
    "sanguine": "sanguine_scandal",
    "sheogorath": "sheogorath_glitches",
    "vaermina": "vaermina_nightmares",
}

def tick_clock(clock_id: str, amount: int) -> None:
    clocks_path = CLOCKS / "daedric_influence_clocks.json"
    if not clocks_path.exists():
        print("[WARN] clocks/daedric_influence_clocks.json not found; skipping clock tick.")
        return
    data = load_json(clocks_path)
    clocks = data.get("clocks", {})
    if clock_id not in clocks:
        print(f"[WARN] Clock id '{clock_id}' not present; skipping.")
        return
    clocks[clock_id]["current"] = max(0, min(clocks[clock_id]["max"], int(clocks[clock_id]["current"]) + amount))
    data["clocks"] = clocks
    save_json(clocks_path, data)
    cur = clocks[clock_id]["current"]
    mx = clocks[clock_id]["max"]
    print(f"[OK] Ticked influence clock '{clock_id}': {cur}/{mx}")
    if cur >= mx:
        print(f"[FILLED] {clocks[clock_id].get('filled_effect','')}")

def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--prince", required=True, help="Prince id (e.g., azura, boethiah, nocturnal, etc.)")
    ap.add_argument("--completed", default="", help="true/false")
    ap.add_argument("--champion", default="", help="true/false")
    ap.add_argument("--artifact", default="", help="Artifact name to store (optional)")
    ap.add_argument("--tick", default="0", help="How much to tick the influence clock (integer, default 0)")
    args = ap.parse_args()

    prince = normalize(args.prince)
    quest_path = STATE / "quest_flags.json"
    if not quest_path.exists():
        raise SystemExit("Missing state/quest_flags.json")

    q = load_json(quest_path)
    daedric = q.get("daedric", {})
    if prince not in daedric:
        # Create a safe default if a new prince id appears
        daedric[prince] = {"completed": False, "champion": False, "artifact": ""}

    if args.completed != "":
        daedric[prince]["completed"] = str2bool(args.completed)
    if args.champion != "":
        daedric[prince]["champion"] = str2bool(args.champion)
    if args.artifact:
        daedric[prince]["artifact"] = args.artifact

    q["daedric"] = daedric
    save_json(quest_path, q)

    print("[OK] Updated quest flags:")
    print(f" - Prince: {prince}")
    print(f" - completed: {daedric[prince]['completed']}")
    print(f" - champion: {daedric[prince]['champion']}")
    print(f" - artifact: {daedric[prince]['artifact']}")

    tick = int(args.tick)
    if tick != 0 and prince in PRINCE_TO_CLOCK:
        tick_clock(PRINCE_TO_CLOCK[prince], tick)
    elif tick != 0:
        print("[WARN] No influence clock mapped for this prince; skipping tick.")

    return 0

if __name__ == "__main__":
    raise SystemExit(main())

from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict

ROOT = Path(__file__).resolve().parents[1]
POS = ROOT / "state" / "campaign_position.json"
PCF = ROOT / "state" / "pc_profile.json"
CLOCKS = ROOT / "clocks" / "skyrim_clocks.json"

ACT_CLOCK_FOR_ACT = {
    1: "act_01_whiterun_outcome",
    2: "act_02_fronts_shift",
    3: "act_03_city_crisis_wave",
    4: "act_04_siege_preparation",
    5: "act_05_true_enemy",
}

def load_json(path: Path) -> Dict[str, Any]:
    if not path.exists():
        return {}
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return {}

def clock_min(clock_obj: Any) -> Dict[str, int]:
    if not isinstance(clock_obj, dict):
        return {"current": 0, "max": 0}
    cur = clock_obj.get("current", 0)
    mx = clock_obj.get("max", 0)
    try:
        cur = int(cur)
    except Exception:
        cur = 0
    try:
        mx = int(mx)
    except Exception:
        mx = 0
    return {"current": cur, "max": mx}

def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--compact", action="store_true", help="Print minified JSON")
    ap.add_argument("--out", type=str, default="", help="Write JSON to a file path")
    args = ap.parse_args()

    pos = load_json(POS)
    pcwrap = load_json(PCF)
    clocks = load_json(CLOCKS)

    act = pos.get("current_act") or pos.get("act") or 0
    try:
        act = int(act)
    except Exception:
        act = 0

    position = {
        "act": act,
        "scene_id": pos.get("current_scene_id") or pos.get("scene_id") or "",
        "hold": pos.get("current_hold") or pos.get("hold") or "",
        "location": pos.get("current_location") or "",
    }

    pc = pcwrap.get("pc", {}) if isinstance(pcwrap.get("pc", {}), dict) else {}
    pc_out = {
        "created": bool(pcwrap.get("created", False)),
        "name": pc.get("name", ""),
        "race": pc.get("race", ""),
        "standing_stone": pc.get("standing_stone", ""),
        "high_concept": pc.get("high_concept", ""),
        "trouble": pc.get("trouble", ""),
    }

    pc_clocks = {}
    if isinstance(pc.get("clocks", {}), dict):
        for key in ("blood_potency", "blood_revelation"):
            if key in pc["clocks"]:
                pc_clocks[key] = clock_min(pc["clocks"][key])

    master_out = {k: clock_min(v) for k, v in (clocks.get("master_clocks", {}) or {}).items()}
    act_out = {k: clock_min(v) for k, v in (clocks.get("act_clocks", {}) or {}).items()}
    faction_out = {k: clock_min(v) for k, v in (clocks.get("faction_clocks", {}) or {}).items()}
    personal_out = {k: clock_min(v) for k, v in (clocks.get("personal_clocks", {}) or {}).items()}

    triggers = []
    act_key = ACT_CLOCK_FOR_ACT.get(act)
    if act_key and act_key in act_out:
        cur = act_out[act_key]["current"]
        mx = act_out[act_key]["max"]
        if mx > 0 and (cur / mx) >= 0.5:
            triggers.append(f"Act clock '{act_key}' at {cur}/{mx} (>=50%)")
    dragonbreak = {"eligible": bool(triggers), "triggers": triggers}

    out = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "position": position,
        "pc": pc_out,
        "pc_clocks": pc_clocks,
        "dragonbreak": dragonbreak,
        "clocks": {
            "master_clocks": master_out,
            "act_clocks": act_out,
            "faction_clocks": faction_out,
            "personal_clocks": personal_out,
        },
    }

    txt = json.dumps(out, ensure_ascii=False, separators=(",", ":")) if args.compact else json.dumps(out, ensure_ascii=False, indent=2)

    if args.out:
        out_path = (ROOT / args.out).resolve() if not Path(args.out).is_absolute() else Path(args.out)
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(txt + "\n", encoding="utf-8")

    print(txt)

if __name__ == "__main__":
    main()

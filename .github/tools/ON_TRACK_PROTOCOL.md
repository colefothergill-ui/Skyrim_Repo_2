# On-Track Protocol

Use this when the table feels "drifty" or you suspect the vault state doesn't match the module.

## Quick checks
- Does `state/campaign_position.json.current_act` match the act you're playing?
- Does `current_scene_id` match the scene you're in?
- Are you still at the module start point (`ACT_01_BATTLE_OF_WHITERUN`) for a new campaign?

## Script
Run:
- `python scripts/on_track.py`

## If Off-Track
The script prints:
- The mismatch
- The recommended canonical value
- The exact file(s) to edit

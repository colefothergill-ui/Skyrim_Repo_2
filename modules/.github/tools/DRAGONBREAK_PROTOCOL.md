# Dragonbreak Protocol

Dragonbreak moments are optional "Elder Scrolls weirdness" used to:
- reconcile branching outcomes,
- spotlight mythic stakes,
- or justify timeline splits.

## Source of truth
- `story_branches/DRAGONBREAK_MOMENTS.json`

## How the GM uses it
1) Keep `state/campaign_position.json.current_scene_id` updated.
2) When entering a decision point, run:
   - `python scripts/dragonbreak_cue.py`
3) If it recommends a moment, present a Secret Turn / Elder Scrolls Moment.

## Record the fork
If a Dragonbreak is used, write:
- a note in the current session log
- update `state/campaign_position.json` (add a note under `on_track.notes`)

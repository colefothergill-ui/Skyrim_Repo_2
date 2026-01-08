# Patch Notes — Start at Battle of Whiterun + Session Zero Gate

This patch adds:
- Default module start: **Act 1 — Battle of Whiterun**
- A mandatory **Session Zero PC creation gate** (`state/pc_profile.json`)
- Act-aware Dragonbreak moments (`story_branches/DRAGONBREAK_MOMENTS.json`)
- On-track checker script (`scripts/on_track.py`)
- A state template + apply helper (`scripts/apply_template.py`)

## Minimal integration steps
1) Commit these new files.
2) Optionally add links to:
   - tools/STARTUP_PROTOCOL.md
   - tools/SESSION_ZERO_GATE.md
   - tools/ON_TRACK_PROTOCOL.md
   - tools/DRAGONBREAK_PROTOCOL.md
3) If you want the vault to *start fresh right now*, run:
   python scripts/apply_template.py --template MODULE_START_BATTLE_OF_WHITERUN

DONE.

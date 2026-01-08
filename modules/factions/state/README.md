# state/

`campaign_state.json` is the live snapshot of the campaign world:
- Hold control (Imperial / Stormcloak / Neutral / Contested)
- Major flags that alter act flow
- Party alignment, allies, enemies

`campaign_position.json` is the fast pointer for “where we are right now”:
- current act
- current hold/location
- focus factions
- last log reference

Rules:
- Keep numeric progress only in `/clocks/skyrim_clocks.json`.
- Update `campaign_state.json` when hold control, flags, or alignment changes.
- Logs (`/logs/*.md`) are historical recaps; state files are “now.”

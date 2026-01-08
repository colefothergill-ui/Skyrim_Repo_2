# state/

`STATE.json` is the live snapshot for the current session/scene:
- Scene aspects/boosts
- PCs: aspects, skills, stunts, FP, stress, consequences
- Log hint and house rules switches
- References to clocks file(s)

Rules:
- Keep numeric progress only in `clocks/bfa_clocks.json`.
- Update `STATE.json` when FP, consequences, scene aspects/boosts, or PC state changes.
- Logs (`/logs/*.md`) are historical recaps; `STATE.json` is “now.”

# Secret Turns — Elder Scrolls Moment (Dragonbreak)

A Secret Turn is the GM offering an optional **mythic deviation** that:
- explains contradictory outcomes,
- creates a fork you can later reconcile,
- or reveals "the true enemy" thread under the war.

## When to offer it
Use either:
- **Module-keyed Dragonbreak moments** (`story_branches/DRAGONBREAK_MOMENTS.json`)
- OR the soft triggers from scripts:
  - `python scripts/dragonbreak_cue.py`
  - `python scripts/secret_turn_check.py`

## How to record it
1) Add 1–3 sentences to the session log describing the glitch/fork.
2) Add a one-line note to `state/campaign_position.json.on_track.notes`.
3) If the fork changes canon, update:
   - `state/quest_flags.json`
   - relevant clocks in `clocks/skyrim_clocks.json`

## Seed prompts (choose 1)
- Time stutters: an arrow hits twice, a wall is both intact and cracked.
- Two commanders give contradictory orders, and both are obeyed.
- A ward flashes a symbol you *remember* but cannot place (Thalmor / Aedra / Daedra).
- A civilian recognizes you from a life you haven’t lived.

Keep it weird, keep it useful, keep it short.

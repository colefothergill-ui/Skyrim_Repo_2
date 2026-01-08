# Startup Protocol — Module-Start Campaign (Battle of Whiterun)

This vault is designed to be playable even when *no prior session state exists*.

## The Rule
If the GM has nothing reliable to load (missing/blank state, or a deliberate reset), the campaign **defaults to the module start**:

- **Act:** 1  
- **Scene ID:** `S0_CHARACTER_CREATION`  
- **Start Point:** `ACT_01_BATTLE_OF_WHITERUN`  
- **Location:** Whiterun — Battle of Whiterun (Staging)

## Session Zero Gate (Mandatory)
Before play begins at the siege, the GM must collect:

1. PC Name
2. High Concept + Trouble + 3 Aspects
3. **Primary Affiliation** (Stormcloaks/Imperials/Companions/Thieves Guild/etc.)
4. **Starting Role** (how you enter the siege)
5. Skills/Approaches
6. At least 1 stunt

Completion is tracked in: `state/pc_profile.json` (`created: true`).

## How to Reset to Module Start (repo-local)
Use the template set:
- `state/templates/MODULE_START_BATTLE_OF_WHITERUN/`

Automation helper:
- `python scripts/apply_template.py --template MODULE_START_BATTLE_OF_WHITERUN`

## Dragonbreak / Secret Turns
Dragonbreak moments are guided by:
- `story_branches/DRAGONBREAK_MOMENTS.json`
and reinforced by:
- `python scripts/dragonbreak_cue.py`
- `python scripts/secret_turn_check.py`

## On-Track Check
Run:
- `python scripts/on_track.py`

If off-track, it prints *exactly* what to change (and which file) to re-align with the module.

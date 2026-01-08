# Branch Matrix — Canon Rails + Fork Points

This file exists to answer one question fast:

**Are we on the module rails? If not, what should be true right now?**

---

## Campaign Start Point (Default)

If state is missing/blank, the campaign starts at:

- **Act 1:** Battle of Whiterun  
- **Scene ID:** `S0_CHARACTER_CREATION` (Session Zero Gate)  
- **Location:** Whiterun — Battle of Whiterun (Staging)

Source of truth:
- `state/startup_defaults.json`

---

## Act I — Battle of Whiterun

### Scene Anchors (recommended)
- `S0_CHARACTER_CREATION` — PC creation + affiliation gate (must be complete)
- `S1_SIEGE_OPENING` — first horns, first arrows
- `S2_CHOOSE_SIDE` — pick side/role *in-fiction* (even if neutral)
- `S3_FIRST_BLOOD` — first meaningful consequence
- `S4_GATEHOUSE_CHAOS` — breach attempt / ward attempt
- `S5_WARD_OR_FIRE` — magic/engineering choice
- `S6_CIVILIAN_COST` — the war pays a bill
- `S7_WHITERUN_DECISION` — the hold tips (or fractures)

> Keep `state/campaign_position.json.current_scene_id` updated.

### Core Branch
**If** PC commits to Stormcloaks:
- `quest_flags.main_quest_flags.civil_war_joined = true`
- `civil_war_side = "stormcloak"`
- Party alignment becomes stormcloak

**If** PC commits to Imperials:
- `civil_war_joined = true`
- `civil_war_side = "imperial"`
- Party alignment becomes imperial

**If** PC stays “other/neutral”:
- Keep `civil_war_joined = false`
- Record the choice in `state/pc_profile.json.pc.starting_role`
- The siege still imposes consequences (enemy list begins)

### Act Clock
Tick `clocks.skyrim_clocks.json → act_01_whiterun_outcome` when:
- a meaningful siege objective is achieved or failed,
- the PC’s reputation shifts public opinion,
- an irreversible escalation occurs.

When filled (6/6), Whiterun’s allegiance is locked (or the city is changed forever).

---

## Dragonbreak / Secret Turns

Module-keyed moments live in:
- `story_branches/DRAGONBREAK_MOMENTS.json`

Use:
- `python scripts/dragonbreak_cue.py`
- `python scripts/secret_turn_check.py`

# Session Zero — Character Creation at the Siege Start

This campaign starts **in medias res**: at the opening of the **Battle of Whiterun**.

## 1) Pick Primary Affiliation
Choose 1:
- stormcloaks
- imperials
- companions
- thieves_guild
- college_of_winterhold
- dark_brotherhood
- vigilants_of_stendarr
- neutral

## 2) Starting Role (how you enter the siege)
Use `state/startup_defaults.json → affiliation_to_starting_role` as default fiction.
You may customize the role; the point is to place you in the battle.

## 3) Fate Core Sheet (minimum viable)
- High Concept
- Trouble
- 3 other aspects
- Skills/Approaches
- 1 stunt

## 4) Write it to canon
- `pcs/PC_MAIN.md`
- `state/pc_profile.json` → set `created: true` and fill fields
- If your affiliation implies Civil War commitment, set:
  - `state/quest_flags.json → main_quest_flags.civil_war_joined = true`
  - `civil_war_side = "stormcloak" | "imperial"`

## 5) Set the Scene ID
After Session Zero, set:
- `state/campaign_position.json → current_scene_id = "S1_SIEGE_OPENING"`

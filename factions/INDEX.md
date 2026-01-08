# Campaign Index — Skyrim Fate Core (4E 201)

A structured outline of all campaign elements for quick navigation.

---

## Root Contents

- **[README.md](README.md)** — Repo purpose, folder map, workflow, and quick start
- **[MASTER_KEY.md](MASTER_KEY.md)** — Campaign premise, play pillars, and clock philosophy

---

## Core Campaign Data

### Clocks & State
- **[/clocks/skyrim_clocks.json](clocks/skyrim_clocks.json)** — Single source of truth for master, act, and faction clocks
- **[/clocks/OSKERN_CLOCKS_GUIDE.md](clocks/OSKERN_CLOCKS_GUIDE.md)** — Oskern-specific clock definitions
- **[/state/campaign_state.json](state/campaign_state.json)** — Hold control, major flags, party alignment, allies/enemies

---

## Narrative Frameworks

### Five Acts Structure
- **/modules/acts/** — Main Civil War rails:
  - **[ACT_01_BATTLE_OF_WHITERUN.md](modules/acts/ACT_01_BATTLE_OF_WHITERUN.md)**
  - **[ACT_02_THE_HOLDS_SHIFT.md](modules/acts/ACT_02_THE_HOLDS_SHIFT.md)**
  - **[ACT_03_THE_CITY_CRISIS_WAVE.md](modules/acts/ACT_03_THE_CITY_CRISIS_WAVE.md)**
  - **[ACT_04_THE_FINAL_STORM.md](modules/acts/ACT_04_THE_FINAL_STORM.md)**
  - **[ACT_05_THE_TRUE_ENEMY.md](modules/acts/ACT_05_THE_TRUE_ENEMY.md)** *(Thalmor endgame)*
  - **[EPILOGUE.md](modules/acts/EPILOGUE.md)**

### Side Plot Factions (Side Plot C)
- **/factions/side_plot_c/** — Parallel faction arcs:
  - **[README.md](factions/side_plot_c/README.md)** — how to run Side Plot C
  - **[companions.md](factions/side_plot_c/companions.md)**
  - **[college_of_winterhold.md](factions/side_plot_c/college_of_winterhold.md)**
  - **[thieves_guild.md](factions/side_plot_c/thieves_guild.md)**
  - **[dark_brotherhood.md](factions/side_plot_c/dark_brotherhood.md)**
  - **[forsworn.md](factions/side_plot_c/forsworn.md)**
  - **[thalmor.md](factions/side_plot_c/thalmor.md)**

### Daedric Princes & Standing Stones
- **/modules/daedric_princes/** — One quest file per Prince:
  - **[README.md](modules/daedric_princes/README.md)**
- **/state/** — player-facing Extras data:
  - **[standing_stones.json](state/standing_stones.json)**
  - **[race_extras.json](state/race_extras.json)**
- **/clocks/** — influence clocks:
  - **[daedric_influence_clocks.json](clocks/daedric_influence_clocks.json)**

### Dragonbreaks, Creatures, & Companions
- **/modules/dragonbreaks_creatures_companions/**:
  - **[INTEGRATION_NOTES.md](modules/dragonbreaks_creatures_companions/INTEGRATION_NOTES.md)**
  - **[DRAGONBREAKS.md](modules/dragonbreaks_creatures_companions/DRAGONBREAKS.md)**
  - **[CREATURES.md](modules/dragonbreaks_creatures_companions/CREATURES.md)**
  - **[COMPANIONS.md](modules/dragonbreaks_creatures_companions/COMPANIONS.md)**
- Optional party index: **[companions_party/NPC_INDEX.md](companions_party/NPC_INDEX.md)**
## Story Hooks

### Hook Bank
- **/hooks/** — Organized story hooks (to be created):
  - `HOOK_BANK.md` — Central repository of hooks by act and faction
  - Act-specific and faction-specific hook files

---

## Characters & Session Data

### NPCs
- **/npcs/** — Named NPCs with aspects, stunts, relationship clocks (Skyrim NPCs to be created)

### PCs
- **/pcs/** — Player character sheets
  - `OSKERN_GALEBORNE.md` — Oskern Galeborne (Ice Wolf of Falkreath)
  - `CHAR_TEMPLATE.md` — Template for new PCs

### Session Logs
- **/logs/** — Session-by-session records
  - `session_TEMPLATE.md` — Template for logging sessions

---

## Rules & Mechanics

### Fate Core Resources
- **/rules/** — Fate Core quickrefs and system toolkit menus
- **/fate-core/** — Story trees, progress dynamics, mechanics frameworks

---

## Navigation Tips

1. **Before a session:** Review `/state/`, `/clocks/`, and `/hooks/` for current campaign status.
2. **During a session:** Reference `/npcs/` and `/factions/` for NPC stats and faction goals.
3. **After a session:** Update `/logs/`, `/clocks/`, and `/state/` to reflect outcomes.
4. **When planning:** Read `/modules/` for act structure and major turning points.

---

**Campaign Era:** 4E 201  
**Premise:** PCs replace the absent Dragonborn; civil war and Thalmor endgame converge.  
**Tone:** Gritty, branching, consequence-driven

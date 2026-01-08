# Skyrim Fate Core Campaign Vault

Welcome to the **Skyrim Fate Core Campaign Vault** — a comprehensive repository for running a gritty, branching Fate Core campaign set in **4E 201 Skyrim**.

## Repo Purpose

This vault serves as the **single source of truth** for:
- Campaign state (hold control, party alignment, major flags)
- Progress clocks (master, act, and faction-level)
- NPCs, factions, modules, and session logs
- Story hooks and GM workflow tools

The **Dragonborn is absent**. Your PCs shape the outcome of the civil war — and the Thalmor endgame lurking beneath it.

---

## Folder Map

```
/clocks/          — skyrim_clocks.json (master, act, faction clocks)
/state/           — campaign_state.json, quest_flags.json, party_state.json
/modules/         — Act modules, narrative frameworks, and location guides
  /acts/          — Five Acts structure
  /locations/     — Hold and city guides with zone-in commands
/factions/        — Faction packs (Stormcloaks, Imperials, Thalmor, guilds, etc.)
/npcs/            — Named NPCs with aspects, stunts, and relationship clocks
/pcs/             — Player character sheets
/hooks/           — Story hooks organized by act and faction
/logs/            — Session logs with clock/state updates
/rules/           — Fate Core mechanics and quickrefs
/fate-core/       — Fate system toolkit and story tree frameworks
/scripts/         — GM automation and validation tools
```

---

## Workflow

### After each session:
1. **Update `/logs/`** — Use `python scripts/session_stamp.py` to create a timestamped log; record key events, PC actions, and narrative outcomes.
2. **Update `/clocks/skyrim_clocks.json`** — Tick relevant master, act, and faction clocks based on session outcomes.
3. **Update `/state/campaign_state.json`** — Adjust hold control, major flags, party alignment, and allies/enemies lists.
4. **Update `/state/quest_flags.json`** — Track quest progression and milestone completions.
5. **Update `/state/party_state.json`** — Record companion changes, party cohesion, and morale shifts.
6. **Update NPC clocks** — If relationship or personal clocks tick, update individual NPC files in `/npcs/`.
7. **Review `/hooks/`** — Check for triggered hooks or new complications to weave into the next session.

### Before next session:
1. **Check for Dragonbreak moments** — Run `python scripts/dragonbreak_cue.py` to see if mythic threads should surface.
2. **Review current state** — Check `/state/` files and `/clocks/` to understand current campaign position.
3. **Prepare location details** — Review relevant files in `/modules/locations/` for the session's expected locations.
4. **Select hooks** — Choose 2-3 hooks from `/hooks/` to weave into play.

---

## Explicit Details

- **Era:** 4E 201 — The civil war is active; the Dragonborn's absence means no prophecy safety net.
- **PCs Shape Outcomes:** Player decisions determine which holds fall, who rules Skyrim, and whether the Thalmor endgame is exposed or executed.
- **Thalmor Endgame:** The Aldmeri Dominion is manipulating both sides. Proof of this manipulation is a **major campaign flag**.
- **No Dragonborn:** Dragons may still emerge (optional), but the PCs are the heroes — no NPC will solve the war or Thalmor crisis for them.
- **Gritty Tone:** War has costs. Diplomacy, espionage, and moral compromise are as important as combat.

---

## Quick Start

### For New GMs
1. Run the first-time onboarding:
   ```bash
   python scripts/first_run.py
   ```
2. Read `MASTER_KEY.md` for campaign premise, play pillars, and clock philosophy.
3. Read `INDEX.md` for a structured outline of all campaign elements.
4. Review `/modules/acts/` for the Five Acts structure.
5. Check `/state/campaign_state.json` and `/clocks/skyrim_clocks.json` before each session.

### Starting a Session
Use zone-in commands to begin play:
```bash
ZONE-IN: Helgen        # Classic escape scenario
ZONE-IN: Whiterun      # Neutral ground, Companions
ZONE-IN: Jorrvaskr     # Mead hall, honor culture
ZONE-IN: Windhelm      # Stormcloak capital
ZONE-IN: Solitude      # Imperial stronghold
```

See `/modules/locations/` for detailed location guides with aspects and GM hooks.

### GM Automation Tools
```bash
# Run full vault audit and integrity check
bash scripts/audit_vault.sh

# Create a new session log with timestamp
python scripts/session_stamp.py

# Check for Dragonbreak moment eligibility
python scripts/dragonbreak_cue.py

# Validate repository for banned terms
python scripts/custom_scan.py

# Validate campaign state files
python scripts/validate_state.py

# Set up convenient bash aliases
bash scripts/setup_aliases.sh
```

---

## License & Attribution

This campaign uses **Fate Core** by Evil Hat Productions.  
Skyrim and The Elder Scrolls are trademarks of Bethesda Softworks LLC.  
This repository is a fan-made campaign framework for personal use.
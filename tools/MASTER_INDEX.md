# Complete Campaign Toolkit — Master Index

This is your navigation hub for the entire Skyrim Fate Core campaign repository. Everything is organized by purpose and priority.

---

## 🚀 START HERE (First Time)

**For New GMs** (Read in this order):
1. `README.md` — Campaign overview and structure
2. `MASTER_KEY.md` — Core premise, pillars, and clock philosophy
3. `tools/GM_QUICK_START.md` — Get running fast (15-minute prep)
4. `tools/CONTEXT_BUILDER.md` — ChatGPT integration guide

**For Returning GMs** (Every Session):
1. `tools/GM_QUICK_START.md` — Session prep workflow
2. `tools/GM_CHEAT_SHEETS.md` — At-table reference

---

## 📚 Core Documentation

### Campaign Foundation
- `README.md` — Repository purpose, folder map, workflow
- `MASTER_KEY.md` — Campaign premise, play pillars, clock philosophy
- `INDEX.md` — Original campaign index (legacy)

### Setup & Configuration
- `SETUP_GUIDE.md` — Initial repository setup
- `QUICK_START_AFTER_FIXES.md` — Post-setup quickstart
- `REPOSITORY_FIXES_SUMMARY.md` — Technical improvements log

---

## 🎮 GM Toolkit

### Essential Tools (Use Every Session)
- `tools/GM_QUICK_START.md` — **START HERE** — Complete GM workflow
- `tools/GM_CHEAT_SHEETS.md` — Quick reference for common situations
- `tools/CONTEXT_BUILDER.md` — ChatGPT integration guide
- `tools/CHATGPT_PROMPTS.md` — All prompt templates for ChatGPT

### Reference & Lookup
- `tools/ENCOUNTER_TABLES.md` — Enemy stat blocks by Hold
- `tools/LOOT_SYSTEM.md` — Aspect-based rewards by Hold
- `rules/fate_core_quickref.md` — Fate Core mechanics summary
- `rules/fate_system_toolkit_menu.md` — Extended mechanics

### Session Management
- `logs/session_TEMPLATE.md` — Template for session logs
- Session Zero: `state/startup_defaults.json` for requirements

---

## 🤖 Automation Scripts

### Context & State Management
```bash
# Build context bundle for ChatGPT
python scripts/build_context.py --chatgpt --output /tmp/context.md

# Validate state files
python scripts/validate_state.py

# Check module alignment
python scripts/on_track.py
```

### NPC Management
```bash
# Find NPCs at current location
python scripts/npc_lookup.py --current --detailed

# Search by location
python scripts/npc_lookup.py --location "Whiterun"

# Search by faction
python scripts/npc_lookup.py --faction imperials

# Search by name
python scripts/npc_lookup.py --search "Hadvar"
```

### Session Workflow
```bash
# Create timestamped session log
python scripts/session_stamp.py

# Check for Dragonbreak moments
python scripts/dragonbreak_cue.py

# Assess milestone
python scripts/character_progression.py --suggest
```

### Character Progression
```bash
# Get milestone recommendation
python scripts/character_progression.py --suggest

# Show milestone info
python scripts/character_progression.py --info significant

# Log milestone to character
python scripts/character_progression.py --milestone major --character PC_MAIN.md
```

---

## 📊 State & Data Files

### Campaign State (Update After Sessions)
- `state/campaign_state.json` — Flags, hold control, party alignment
- `state/campaign_position.json` — Current act, scene, location
- `state/pc_profile.json` — PC creation gate and basic profile
- `state/party_state.json` — Companions, morale, cohesion
- `state/quest_flags.json` — Quest progression tracking

### Clocks (Core Campaign Engine)
- `clocks/skyrim_clocks.json` — All master, act, faction, and personal clocks
- See `MASTER_KEY.md` for clock philosophy

### Configuration
- `state/startup_defaults.json` — Default start point and Session Zero requirements
- `state/templates/` — Template state files

---

## 🎭 Characters

### Player Characters
- `pcs/PC_MAIN.md` — Active PC sheet (example: Agran Moorcroft)
- `pcs/CHAR_TEMPLATE.md` — Basic character template (legacy)
- `pcs/CHAR_TEMPLATE_V2.md` — **Enhanced template** with full tracking

### NPCs & Companions
- `npcs/NPC_INDEX.md` — Complete NPC directory
- `npcs/README.md` — NPC dossier format
- `npcs/companions/` — Companion NPC files (Hadvar, Lydia, etc.)

**Quick NPC Lookup**:
```bash
python scripts/npc_lookup.py --search "NPC_NAME"
```

---

## 📖 Campaign Modules

### Act Structure
- `modules/acts/ACT_01_BATTLE_OF_WHITERUN.md` — Act I: Whiterun's Choice
- `modules/acts/ACT_02_SPREADING_FLAMES.md` — Act II: Fronts Shift
- `modules/acts/ACT_03_THE_SHADOW_WAR.md` — Act III: City Crises
- `modules/acts/ACT_04_THE_FINAL_STORM.md` — Act IV: Siege Preparation
- (Act V file location TBD)

### Locations
- `modules/locations/` — Hold and city guides with aspects
- Check relevant location files before zoning in

### Story Branches
- `story_branches/DRAGONBREAK_MOMENTS.json` — Timeline fork moments
- `story_branches/BRANCH_MATRIX.md` — Campaign branching structure
- `story_branches/SECRET_TURNS.md` — Secret turn mechanics

---

## 🏰 Factions

### Faction Files
- `factions/` — Individual faction packs (Imperials, Stormcloaks, etc.)
- `factions/INDEX.md` — Faction directory

### Major Factions
- **Imperial Legion** — Skyrim's Cyrodilic government
- **Stormcloaks** — Ulfric's Nord rebellion
- **Thalmor** — Aldmeri Dominion shadow operators
- **Companions** — Jorrvaskr's honor-bound warriors
- **Thieves Guild** — Riften's shadow network
- **Dark Brotherhood** — Sithis's assassins
- **College of Winterhold** — Arcane scholars
- **Forsworn** — Reach independence fighters

---

## 📜 Story Hooks

### Hook Resources
- `hooks/HOOK_BANK.md` — Central hook repository by act and faction
- `hooks/README.md` — How to use hooks
- Act-specific hooks embedded in act files

### Using Hooks
1. Check current act in `state/campaign_position.json`
2. Review hooks for that act
3. Select 2-3 hooks to weave into session
4. Tie hooks to active clocks and PC aspects

---

## 🎲 Fate Core Rules

### Core Mechanics
- `rules/fate_core_quickref.md` — Essential Fate Core rules
- `rules/fate_system_toolkit_menu.md` — Extended options
- `fate-core/mechanics/` — Detailed mechanical frameworks

### Story & Progress
- `fate-core/story-trees/` — Narrative structure tools
- `fate-core/progress-dynamics/` — Advancement systems
- `fate-core/clocks/` — Clock mechanics deep dive

---

## 📝 Session Logs

### Creating Logs
```bash
python scripts/session_stamp.py  # Creates timestamped template
```

### Log Files
- `logs/session_TEMPLATE.md` — Template for new logs
- `logs/YYYY-MM-DD_session-XX_TITLE.md` — Completed session logs

### Log Structure
1. **Save Game** — 700-1200 word war-chronicle recap
2. **Mechanical Updates** — Clocks, aspects, stress, consequences
3. **Open Threads** — Unresolved complications
4. **GM Notes** — Continuity reminders

---

## 🔧 Advanced Tools

### Validation & Debugging
```bash
# Full vault audit
bash scripts/audit_vault.sh

# Validate state files
python scripts/validate_state.py

# Check campaign alignment
python scripts/on_track.py

# Scan for banned terms (if applicable)
python scripts/custom_scan.py
```

### Performance & Optimization
- `scripts/PERFORMANCE_IMPROVEMENTS.md` — Script optimization notes

### Development Tools
- `scripts/pdf_to_md.py` — Convert PDFs to markdown
- `scripts/apply_template.py` — Apply state templates
- `scripts/hud_export.py` — Export HUD data
- `hud_mcp_server.py` — MCP server for integrations

---

## 🌐 External Integration

### ChatGPT Integration (Primary)
**Setup**:
1. Read `tools/CONTEXT_BUILDER.md`
2. Run `python scripts/build_context.py --chatgpt -o /tmp/context.md`
3. Upload context to ChatGPT
4. Use prompts from `tools/CHATGPT_PROMPTS.md`

**Maintenance**:
- Update context each session
- Feed incremental updates mid-session
- Use specialized prompts for combat, NPCs, transitions

### Source Material
- `__Elder Scrolls_ Skyrim – Fate Core Campaign Module.pdf` — Core module
- `Skyrim Faction Pack_ Side Plot C – Allegiances in War.pdf` — Faction details
- `Dragonbreaks, Creatures, and Companions Module.pdf` — Special mechanics
- `source_material/` — Additional materials

---

## 📋 Quick Reference Cards

### Command Cheat Sheet
```bash
# Context
python scripts/build_context.py --chatgpt -o /tmp/context.md

# State
python scripts/validate_state.py
python scripts/on_track.py

# NPCs
python scripts/npc_lookup.py --current
python scripts/npc_lookup.py --location "Whiterun"

# Session
python scripts/session_stamp.py
python scripts/dragonbreak_cue.py

# Progression
python scripts/character_progression.py --suggest
```

### File Priority (Keep These Open)
**Every Session**:
- `tools/GM_CHEAT_SHEETS.md` — Quick reference
- `state/campaign_state.json` — Current flags
- `clocks/skyrim_clocks.json` — Current clocks
- Current act file from `modules/acts/`

**As Needed**:
- `tools/ENCOUNTER_TABLES.md` — Enemy stats
- `tools/LOOT_SYSTEM.md` — Rewards
- `tools/CHATGPT_PROMPTS.md` — Prompt templates
- Relevant NPC files from `npcs/`

---

## 🗺️ Workflow Flowchart

### Before Session
```
1. Run build_context.py → Load into ChatGPT
2. Review campaign_state.json and clocks
3. Read last session log
4. Prep NPCs (npc_lookup.py) and encounters (ENCOUNTER_TABLES.md)
5. Choose 2-3 hooks from HOOK_BANK.md
```

### During Session
```
1. Use GM_CHEAT_SHEETS.md for rulings
2. Track mechanics in ChatGPT (incremental updates)
3. Tick clocks based on actions
4. Award fate points for compels
5. Distribute loot from LOOT_SYSTEM.md
```

### After Session
```
1. Create session log (session_stamp.py)
2. Update state files (campaign_state, clocks, position)
3. Update NPC relationship clocks
4. Assess milestone (character_progression.py --suggest)
5. Validate (validate_state.py, on_track.py)
```

---

## 🆘 Help & Troubleshooting

### Lost Track of State?
```bash
python scripts/build_context.py  # Get orientation
python scripts/on_track.py       # Check alignment
```
Then use Emergency Prompt from `tools/CHATGPT_PROMPTS.md`

### Players Diverged?
1. Check `python scripts/on_track.py` for alignment status
2. Decide: Realign or embrace divergence
3. Trust campaign pillars to guide you

### Rules Question?
1. Check `rules/fate_core_quickref.md`
2. Use Rules Clarification Prompt from `tools/CHATGPT_PROMPTS.md`
3. Adjudicate based on: Most interesting, most genre-appropriate

---

## 📊 Priority Matrix

### Must Read (Before First Session)
1. `README.md`
2. `MASTER_KEY.md`
3. `tools/GM_QUICK_START.md`
4. `tools/CONTEXT_BUILDER.md`

### Should Read (Within First 3 Sessions)
1. `tools/GM_CHEAT_SHEETS.md`
2. `tools/ENCOUNTER_TABLES.md`
3. `tools/LOOT_SYSTEM.md`
4. Current act file

### Reference As Needed
- Everything else, accessed via this index

---

**Version**: 2.0  
**Last Updated**: 2026-01-23  
**Purpose**: One-stop navigation for entire campaign toolkit  
**Maintained By**: Campaign GM

---

*This repository contains everything you need to run a Fate Core Skyrim campaign with ChatGPT integration. Start with GM_QUICK_START.md and follow the workflows. You've got this!*

# Tools Directory — GM Toolkit for Skyrim Fate Core Campaign

This directory contains all GM-facing tools, guides, and reference materials for running the campaign with ChatGPT integration.

---

## 🚀 START HERE

If you're new to this repository, read these files in order:

1. **`GM_QUICK_START.md`** — Complete workflow for preparing and running sessions (15-minute prep)
2. **`MASTER_INDEX.md`** — Navigation hub for the entire repository
3. **`CONTEXT_BUILDER.md`** — How to integrate ChatGPT into your sessions
4. **`CHATGPT_PROMPTS.md`** — Prompt templates for every situation

---

## 📁 Files in This Directory

### Essential GM Guides

#### `GM_QUICK_START.md`
**Purpose**: Get you running sessions quickly  
**Contains**:
- Before first session checklist
- 15-minute session prep workflow
- During session essential tools
- After session cleanup procedures
- Common workflows (scene transitions, clock fills, NPC interactions)
- Troubleshooting guide

**When to Use**: Every session for prep and cleanup

---

#### `GM_CHEAT_SHEETS.md`
**Purpose**: Quick reference during play  
**Contains**:
- Fate Core basics (ladder, actions, outcomes)
- Combat quick reference
- Opposition difficulty guidelines
- Aspect economy rules
- Clock tick guidelines
- Loot quick reference
- Compel formulas
- Scene structure templates
- NPC builder
- Common rulings

**When to Use**: Keep open during play for quick lookups

---

#### `MASTER_INDEX.md`
**Purpose**: Navigation hub for entire repository  
**Contains**:
- Complete file directory organized by purpose
- Priority reading lists
- Command cheat sheets
- Workflow flowcharts
- Help and troubleshooting section

**When to Use**: When you need to find something in the repository

---

### ChatGPT Integration

#### `CONTEXT_BUILDER.md`
**Purpose**: Guide for using ChatGPT as campaign assistant  
**Contains**:
- Quick context load instructions
- File loading order
- Context bundle builder script usage
- ChatGPT prompt template overview
- State update checklist
- Automation tools reference
- Tips for effective ChatGPT integration

**When to Use**: First time setup and as reference for context building

---

#### `CHATGPT_PROMPTS.md`
**Purpose**: Complete library of prompt templates  
**Contains**:
- Session start prompt (full setup)
- Mid-session update prompts
- Combat start prompts
- NPC interaction prompts
- Scene transition prompts
- Clock advancement prompts
- Compel suggestion prompts
- Milestone assessment prompts
- Rules clarification prompts
- Loot distribution prompts
- On-track validation prompts
- Dragonbreak moment prompts
- Emergency "I'm lost" prompt

**When to Use**: Copy-paste prompts into ChatGPT during play

---

### Reference Materials

#### `ENCOUNTER_TABLES.md`
**Purpose**: Enemy stat blocks by Hold and difficulty  
**Contains**:
- Difficulty tier definitions (Mook, Minor, Significant, Major)
- Enemy stat blocks by Hold:
  - Whiterun Hold
  - The Reach (Markarth)
  - Eastmarch (Windhelm)
  - Haafingar (Solitude)
  - The Rift (Riften)
  - Winterhold
  - Universal threats (Vampires, Dragons)
- Encounter composition guidelines
- Custom enemy builder templates

**When to Use**: When creating combat encounters

---

#### `LOOT_SYSTEM.md`
**Purpose**: Fate-appropriate reward system  
**Contains**:
- Core loot philosophy (aspects, permissions, extras)
- Loot tables by Hold
- Special categories (Daedric artifacts, dragon parts, major artifacts)
- Wealth as narrative resource
- Loot by victory type
- Custom loot creation templates
- Distribution guidelines

**When to Use**: After combats and major victories

---

### Character Tools

#### Session Zero Materials
- Character creation gate requirements in `state/startup_defaults.json`
- Enhanced character template in `pcs/CHAR_TEMPLATE_V2.md`

#### Progression Tracking
Use `scripts/character_progression.py` to:
- Get milestone recommendations
- Display milestone information
- Log milestones to character sheets

---

## 🔧 Related Scripts

These scripts in the `scripts/` directory support the tools:

### `scripts/build_context.py`
Build context bundles for ChatGPT
```bash
# Print to console
python scripts/build_context.py

# ChatGPT-optimized format to file
python scripts/build_context.py --chatgpt --output /tmp/context.md
```

### `scripts/npc_lookup.py`
Find NPCs by location, faction, or name
```bash
# NPCs at current campaign location
python scripts/npc_lookup.py --current --detailed

# NPCs in specific location
python scripts/npc_lookup.py --location "Whiterun"

# NPCs in faction
python scripts/npc_lookup.py --faction imperials

# Search by name
python scripts/npc_lookup.py --search "Hadvar"
```

### `scripts/character_progression.py`
Track milestones and progression
```bash
# Get milestone recommendation
python scripts/character_progression.py --suggest

# Show milestone info
python scripts/character_progression.py --info significant

# Log milestone
python scripts/character_progression.py --milestone major --character PC_MAIN.md
```

### `scripts/session_stamp.py`
Create timestamped session log template
```bash
python scripts/session_stamp.py
```

### `scripts/dragonbreak_cue.py`
Check for eligible Dragonbreak moments
```bash
python scripts/dragonbreak_cue.py
```

### `scripts/validate_state.py`
Validate JSON state files
```bash
python scripts/validate_state.py
```

### `scripts/on_track.py`
Check campaign alignment with module
```bash
python scripts/on_track.py
```

---

## 📚 Usage Patterns

### Before Every Session
1. Run `build_context.py --chatgpt -o /tmp/context.md`
2. Load context into ChatGPT with Session Start Prompt
3. Review `GM_QUICK_START.md` for prep checklist
4. Prep NPCs with `npc_lookup.py --current`
5. Review `ENCOUNTER_TABLES.md` and `LOOT_SYSTEM.md`

### During Session
1. Keep `GM_CHEAT_SHEETS.md` open for reference
2. Use prompts from `CHATGPT_PROMPTS.md` as needed
3. Track mechanics via ChatGPT (incremental updates)
4. Reference `ENCOUNTER_TABLES.md` for combat
5. Reference `LOOT_SYSTEM.md` for rewards

### After Session
1. Create session log with `session_stamp.py`
2. Update state files (campaign_state, clocks, position)
3. Assess milestone with `character_progression.py --suggest`
4. Validate with `validate_state.py` and `on_track.py`

---

## 🆘 Troubleshooting

### "I don't know where to start"
→ Read `GM_QUICK_START.md` from top to bottom

### "I need to find something in the repository"
→ Use `MASTER_INDEX.md` to navigate

### "I lost track of campaign state"
→ Run `build_context.py` and use Emergency Prompt from `CHATGPT_PROMPTS.md`

### "I need a quick rules lookup during play"
→ Use `GM_CHEAT_SHEETS.md`

### "I don't know what enemies to use"
→ Use `ENCOUNTER_TABLES.md` for current Hold

### "I don't know what loot to give"
→ Use `LOOT_SYSTEM.md` for current Hold and victory type

---

## 📖 Reading Priority

### Must Read (Before First Session)
1. `GM_QUICK_START.md` — Complete workflow
2. `MASTER_INDEX.md` — Navigation hub
3. `CONTEXT_BUILDER.md` — ChatGPT setup
4. `../MASTER_KEY.md` — Campaign premise and pillars

### Should Read (First Few Sessions)
1. `GM_CHEAT_SHEETS.md` — Rules reference
2. `CHATGPT_PROMPTS.md` — Prompt library
3. `ENCOUNTER_TABLES.md` — Enemy stats
4. `LOOT_SYSTEM.md` — Reward system

### Reference As Needed
- Everything else

---

## 🎯 Quick Command Reference

```bash
# Context
python scripts/build_context.py --chatgpt -o /tmp/context.md

# NPCs  
python scripts/npc_lookup.py --current --detailed

# Session
python scripts/session_stamp.py
python scripts/dragonbreak_cue.py

# Validation
python scripts/validate_state.py
python scripts/on_track.py

# Progression
python scripts/character_progression.py --suggest
```

---

## 💡 Tips

1. **Print GM_CHEAT_SHEETS.md** for your GM screen
2. **Bookmark MASTER_INDEX.md** for quick navigation
3. **Keep context bundles** in `/tmp` to avoid clutter
4. **Update ChatGPT incrementally** during play
5. **Trust the clocks** to drive consequences
6. **Embrace aspects** as narrative fuel
7. **Use the scripts** to reduce manual work

---

## 🔗 Related Resources

- **Main README**: `../README.md`
- **Campaign Premise**: `../MASTER_KEY.md`
- **State Files**: `../state/`
- **Clocks**: `../clocks/skyrim_clocks.json`
- **NPCs**: `../npcs/`
- **Acts**: `../modules/acts/`
- **Rules**: `../rules/`

---

**Version**: 2.0  
**Last Updated**: 2026-01-23  
**Purpose**: Complete GM toolkit for Skyrim Fate Core campaign  
**Maintained By**: Campaign GM

---

*Everything you need to run amazing sessions is in this directory. Start with GM_QUICK_START.md and you'll be up and running in 15 minutes!*

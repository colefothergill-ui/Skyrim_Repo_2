# GM Quick Start Guide — Skyrim Fate Core Campaign

This guide gets you running sessions quickly using the repository's tools and ChatGPT integration.

---

## Before First Session

### 1. Read Core Documents (30 minutes)
```
Priority 1 (MUST READ):
- README.md — Repository overview and workflow
- MASTER_KEY.md — Campaign premise, pillars, clock philosophy

Priority 2 (SHOULD READ):
- tools/CONTEXT_BUILDER.md — ChatGPT integration
- rules/fate_core_quickref.md — Fate Core refresher
```

### 2. Run First-Time Setup
```bash
# If first time using this repository
python scripts/first_run.py

# Build convenience aliases
bash scripts/setup_aliases.sh

# Validate repository state
python scripts/on_track.py
```

### 3. Prepare Session Zero
```
Read: tools/SESSION_ZERO_GATE.md (if exists) or state/startup_defaults.json
Create PC with player using: pcs/CHAR_TEMPLATE_V2.md
Set state/pc_profile.json created=true when complete
```

---

## Starting Each Session

### Quick Prep Workflow (15 minutes)

**Step 1: Build Context Bundle**
```bash
python scripts/build_context.py --chatgpt --output /tmp/session_context.md
```

**Step 2: Load Into ChatGPT**
- Open ChatGPT
- Upload `/tmp/session_context.md`
- Use Session Start Prompt from `tools/CHATGPT_PROMPTS.md`

**Step 3: Review Current State**
- Check `state/campaign_state.json` for flags and hold control
- Check `clocks/skyrim_clocks.json` for clock pressures
- Review last session log in `logs/`

**Step 4: Prep NPCs and Encounters**
```bash
# Find NPCs at current location
python scripts/npc_lookup.py --current --detailed

# Review encounter options for current Hold
# Open: tools/ENCOUNTER_TABLES.md
```

**Step 5: Identify Scene Hooks**
- Check `hooks/HOOK_BANK.md` for current act
- Check for Dragonbreak moments: `python scripts/dragonbreak_cue.py`
- Review relevant act file in `modules/acts/`

---

## During Session

### Essential Tools

#### Track Mechanics in ChatGPT
Use mid-session update prompts from `tools/CHATGPT_PROMPTS.md`:
- Aspect creation/invocation
- Stress and consequences
- Clock advancements
- Fate point tracking

#### Quick Reference Access
Keep these open in browser tabs:
- `rules/fate_core_quickref.md` — Core mechanics
- `tools/ENCOUNTER_TABLES.md` — Enemy stats
- `tools/LOOT_SYSTEM.md` — Reward ideas
- Current act file from `modules/acts/`

#### NPC Stat Blocks
```bash
# Quick lookup by name
python scripts/npc_lookup.py --search "Hadvar"

# Find all NPCs in a faction
python scripts/npc_lookup.py --faction imperials --detailed
```

#### Combat Encounters
1. Open `tools/ENCOUNTER_TABLES.md`
2. Find appropriate Hold section
3. Choose difficulty tier (Mook/Minor/Significant/Major)
4. Use stats as-is or adjust aspects for narrative fit
5. Feed stats to ChatGPT with Combat Start Prompt

---

## After Session

### Essential Cleanup (20 minutes)

**Step 1: Create Session Log**
```bash
python scripts/session_stamp.py
# Edit the created file in logs/ to add chronicle
```

**Step 2: Update State Files**
Manually edit these JSON files based on session outcomes:
- `state/campaign_state.json` — Flags, hold control, party state
- `clocks/skyrim_clocks.json` — All clocks that advanced
- `state/campaign_position.json` — Current location/scene if changed

**Step 3: Update NPC Files**
If relationship clocks changed, edit NPC files in `npcs/`

**Step 4: Milestone Assessment**
```bash
python scripts/character_progression.py --suggest
```

**Step 5: Validate State**
```bash
# Check JSON validity
python scripts/validate_state.py

# Check module alignment
python scripts/on_track.py
```

---

## Common Workflows

### Scene Transition
1. Use Scene Transition Prompt from `tools/CHATGPT_PROMPTS.md`
2. Update `state/campaign_position.json` with new location
3. Look up NPCs: `python scripts/npc_lookup.py --location "New Location"`
4. Check for location file in `modules/locations/` (if exists)

### Clock Fills
1. Announce clock fill to ChatGPT with Clock Advancement Prompt
2. Describe fictional trigger in narrative
3. Update `clocks/skyrim_clocks.json` with new value
4. Check `MASTER_KEY.md` for "What Happens When Clocks Fill"
5. Introduce complication or turning point

### NPC Introduction
1. Use NPC Interaction Prompt from `tools/CHATGPT_PROMPTS.md`
2. Reference NPC file from `npcs/` directory
3. Track social conflict if needed (mental stress)
4. Note relationship clock changes

### Loot Distribution
1. Determine victory type (Minor/Significant/Major)
2. Consult `tools/LOOT_SYSTEM.md` for appropriate tier
3. Choose loot matching Hold and narrative context
4. Use Loot Distribution Prompt with ChatGPT
5. Record new aspects/permissions in PC sheet

---

## Troubleshooting

### "I Lost Track of Campaign State"
```bash
# Get full orientation
python scripts/build_context.py

# Check on-track status
python scripts/on_track.py

# Use Emergency Prompt from tools/CHATGPT_PROMPTS.md
```

### "Players Diverged from Module"
1. Run: `python scripts/on_track.py`
2. Decide: Realign or embrace divergence?
3. If realigning: Follow recommended edits from on_track.py
4. If embracing: Continue with current trajectory, trust the pillars

### "Clock Overwhelm"
- Not all clocks need to advance every session
- Focus on 2-3 clocks per session maximum
- Let PC actions and time passing guide which clocks tick
- Clocks are tools for consequences, not punishment

### "Player Wants Unexpected Action"
1. Check if aspects support it → bonus
2. Check if skills support it → roll
3. If totally unsupported → either allow at high difficulty or explain limitation
4. Remember: Say "Yes, but..." or "Yes, and..."

---

## Quick Reference: File Locations

### Every Session
- `state/campaign_state.json` — World state
- `clocks/skyrim_clocks.json` — All clocks
- `logs/[LATEST].md` — Last session recap

### Context Building
- `tools/CONTEXT_BUILDER.md` — Integration guide
- `tools/CHATGPT_PROMPTS.md` — All prompt templates
- `scripts/build_context.py` — Auto-context builder

### Rules & Mechanics
- `rules/fate_core_quickref.md` — Core rules
- `tools/ENCOUNTER_TABLES.md` — Enemy stats
- `tools/LOOT_SYSTEM.md` — Reward system

### NPCs & Factions
- `npcs/` — NPC dossiers
- `scripts/npc_lookup.py` — NPC finder
- `factions/` — Faction details

### Campaign Structure
- `modules/acts/` — Act frameworks
- `story_branches/DRAGONBREAK_MOMENTS.json` — Special moments
- `hooks/HOOK_BANK.md` — Scene hooks

---

## Cheat Sheet: Common Commands

```bash
# Context and State
python scripts/build_context.py --chatgpt --output /tmp/context.md
python scripts/validate_state.py
python scripts/on_track.py

# NPCs
python scripts/npc_lookup.py --current
python scripts/npc_lookup.py --location "Whiterun"
python scripts/npc_lookup.py --faction imperials --detailed
python scripts/npc_lookup.py --search "Hadvar"

# Session Management
python scripts/session_stamp.py
python scripts/dragonbreak_cue.py

# Character Progression
python scripts/character_progression.py --suggest
python scripts/character_progression.py --info major
python scripts/character_progression.py --milestone significant --character PC_MAIN.md
```

---

## ChatGPT Prompt Quick Access

### Start Session
```
Use: Session Start Prompt (Full Setup) from tools/CHATGPT_PROMPTS.md
Load: Output from build_context.py --chatgpt
```

### Mid-Session
```
Use: Mid-Session Update Prompt
Update: Aspects, stress, clocks, fate points as they change
```

### Special Situations
```
Combat: Combat Start Prompt
NPC: NPC Interaction Prompt
Scene Change: Scene Transition Prompt
Clock Fill: Clock Advancement Prompt
```

---

## Session Pacing Guide

### 2-Hour Session
- 0:00-0:15 — Recap and context load
- 0:15-0:45 — Scene 1 (investigation, social, or travel)
- 0:45-1:15 — Scene 2 (conflict or major choice)
- 1:15-1:45 — Scene 3 (resolution or cliffhanger)
- 1:45-2:00 — Wrap-up, XP/milestone, next session preview

### 3-Hour Session
- 0:00-0:20 — Recap and context load
- 0:20-1:00 — Scene 1 (setup and investigation)
- 1:00-1:40 — Scene 2 (major conflict)
- 1:40-2:20 — Scene 3 (consequences and choices)
- 2:20-2:50 — Scene 4 (cliffhanger or resolution)
- 2:50-3:00 — Wrap-up and milestone

### 4-Hour Session
Add downtime scene, second conflict, or extended social encounter

---

## Remember

1. **Trust the Clocks** — They drive consequences automatically
2. **Embrace Aspects** — They're the heart of Fate Core storytelling
3. **Compel Generously** — Give players fate points for interesting complications
4. **Say "Yes, And"** — Let player creativity shine
5. **Reference the Pillars** — Gritty war, real costs, player agency, Thalmor threat
6. **Use ChatGPT** — It tracks mechanics so you can focus on narrative
7. **Stay Flexible** — Module is a guide, not rails

---

**Version**: 2026-01-23  
**Purpose**: Get GMs running sessions confidently with minimal prep  
**Next Steps**: Run a session and adjust workflows to your style

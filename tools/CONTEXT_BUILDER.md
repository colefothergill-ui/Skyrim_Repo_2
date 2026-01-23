# Context Builder — ChatGPT Integration Guide

This document provides instructions for building context bundles to feed into ChatGPT for optimal campaign narration and tracking.

## Quick Context Load

When starting a ChatGPT session for play, load these files in order:

### 1. Campaign Foundation (Always Load First)
```
/MASTER_KEY.md          — Campaign premise, pillars, clock philosophy
/state/campaign_state.json — Current world state
/state/campaign_position.json — Where the party is RIGHT NOW
/clocks/skyrim_clocks.json — All active clocks
```

### 2. Current Session Context
```
/state/pc_profile.json   — Active PC details
/pcs/PC_MAIN.md         — Full PC sheet
/state/party_state.json  — Party composition and cohesion
```

### 3. Location & Scene Context
Based on current_location in campaign_position.json, load:
```
/modules/locations/[HOLD]_[LOCATION].md  — Location details
/npcs/[relevant NPCs].md                  — NPCs in scene
```

### 4. Relevant Module & Act
Based on current_act in campaign_position.json:
```
/modules/acts/ACT_0[X]_[NAME].md  — Current act structure
/story_branches/DRAGONBREAK_MOMENTS.json — Special moment triggers
```

### 5. Latest Session Log (for continuity)
```
/logs/[LATEST_SESSION].md  — Most recent session events
```

---

## Context Bundle Builder Script

Use this command to auto-generate a session context bundle:

```bash
python scripts/build_context.py --output /tmp/session_context.md
```

This will create a single markdown file with all relevant context for the current session.

---

## ChatGPT Prompt Templates

### Session Start Prompt
```
You are the GM for a Fate Core campaign set in Skyrim (4E 201). The Dragonborn is absent, and the player characters shape the outcome of the civil war and the hidden Thalmor conspiracy.

Context loaded:
- Campaign premise and pillars from MASTER_KEY.md
- Current campaign state and position
- Active clocks and their current values
- PC details and party composition
- Current location: [LOCATION]
- Current act: [ACT NUMBER]

The last session ended with: [BRIEF SUMMARY FROM LATEST LOG]

Today's session will continue from this point. Use the loaded context to:
1. Track all mechanical changes (aspects, stress, consequences, clocks)
2. Narrate outcomes consistent with Fate Core mechanics
3. Ensure NPC behavior matches their stat blocks and aspects
4. Maintain campaign rails per the module structure
5. Suggest appropriate compels based on PC aspects
6. Track loot and rewards appropriate to the setting

Ready to begin play?
```

### Mid-Session Context Refresh
```
Update: [CLOCK NAME] has advanced to [X/Y]
Update: [ASPECT NAME] has been invoked/compelled
Update: [CONSEQUENCE] has been taken by [CHARACTER]

Please update your tracking and consider how this affects:
- Ongoing scene outcomes
- NPC reactions
- Available complications
- Future scene setups
```

### Scene Transition Prompt
```
The PCs are transitioning from [OLD LOCATION] to [NEW LOCATION] in [HOLD].

Please:
1. Load context for the new location from /modules/locations/
2. Identify relevant NPCs for this location
3. Check if any clocks or flags trigger new complications
4. Suggest 2-3 scene hooks appropriate to current party state
5. Remind me of any Dragonbreak moments eligible for this scene
```

### NPC Injection Prompt
```
The PCs have encountered/are seeking [NPC NAME] in [LOCATION].

Please:
1. Load NPC stat block from /npcs/[NPC_FILE].md
2. Consider NPC's current relationship clock status (if tracked)
3. Check campaign state for any flags affecting this NPC
4. Suggest likely NPC goals and complications for this scene
5. Provide aspect-based compel opportunities
```

### Combat Encounter Prompt
```
Combat initiated in [LOCATION] against [ENEMY TYPE].

Please:
1. Use opposition stats appropriate to current act and hold
2. Consider environmental aspects from location file
3. Track stress, consequences, and fate points
4. Suggest compels and zone aspects for the scene
5. Consider how this combat affects relevant clocks
```

---

## State Update Checklist

After each significant scene or session, update ChatGPT context with:

1. **Clock Changes**: Which clocks advanced and by how much
2. **Aspect Changes**: New aspects created, removed, or modified
3. **Stress/Consequences**: Current status for all PCs
4. **Location Changes**: New current_location and current_scene_id
5. **Flag Changes**: Any major_flags that flipped in campaign_state.json
6. **NPC Relationships**: Any relationship clock changes
7. **Loot/Resources**: New equipment, aspects, or extras gained

---

## Quick Reference: File Locations

### Core State Files
- `/state/campaign_state.json` — World state, flags, hold control
- `/state/campaign_position.json` — Current act, scene, location
- `/state/pc_profile.json` — PC creation gate and basic profile
- `/state/party_state.json` — Companions, morale, cohesion
- `/state/quest_flags.json` — Quest progression tracking

### NPC Lookup
- `/npcs/companions/` — Companion NPCs
- `/npcs/NPC_INDEX.md` — Full NPC directory

### Rules Reference
- `/rules/fate_core_quickref.md` — Fate Core rules summary
- `/rules/fate_system_toolkit_menu.md` — Extended mechanics
- `/fate-core/mechanics/` — Detailed mechanics frameworks

### Location Data
- `/modules/locations/` — Hold and city guides with aspects

---

## Automation Tools

### Build Full Context Bundle
```bash
python scripts/build_context.py
```

### Export Session State
```bash
python scripts/session_stamp.py  # Creates timestamped log
```

### Validate Current State
```bash
python scripts/validate_state.py  # Checks JSON validity
python scripts/on_track.py        # Checks module alignment
```

### Check for Dragonbreak Moments
```bash
python scripts/dragonbreak_cue.py
```

---

## Tips for ChatGPT Integration

1. **Load Core Context First**: Always start with MASTER_KEY, campaign_state, and clocks
2. **Update Incrementally**: Feed changes as they happen, don't wait until end of session
3. **Use Exact File Paths**: Reference specific files so ChatGPT knows where to look
4. **Cite Rules**: When mechanics questions arise, point ChatGPT to specific rule files
5. **Track Divergence**: If play diverges from module rails, use on_track.py to realign
6. **Log Thoroughly**: Better session logs = better continuity in future sessions
7. **Trust the Clocks**: Let clocks drive consequences; ChatGPT should suggest ticks
8. **Embrace Aspects**: Use aspects as narrative fuel for compels and invokes

---

## Example: Full Session Start Sequence

```bash
# 1. Build context bundle
python scripts/build_context.py --output /tmp/session_context.md

# 2. Open ChatGPT and load the context file

# 3. Use session start prompt with current details

# 4. During play, feed incremental updates:
#    - "Agran invoked 'Duelist's Precision' to defend"
#    - "civil_war_endgame clock advanced to 3/8"
#    - "PC taken Moderate consequence: 'Burned by Frost Magic'"

# 5. At scene transitions, use scene transition prompts

# 6. After session, create log:
python scripts/session_stamp.py

# 7. Update state files based on session outcomes
```

---

**Version**: 2026-01-23  
**Maintained By**: Campaign GM  
**Purpose**: Enable ChatGPT to serve as intelligent campaign tracker and narrator

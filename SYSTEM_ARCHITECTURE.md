# System Architecture — Skyrim Fate Core Campaign Toolkit

This document visualizes how all components work together to enable ChatGPT-integrated gameplay.

---

## Component Overview

```
┌─────────────────────────────────────────────────────────────────┐
│                    SKYRIM FATE CORE CAMPAIGN                     │
│                                                                   │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐          │
│  │   GM Tools   │  │   ChatGPT    │  │   Players    │          │
│  │              │  │  Integration │  │              │          │
│  └──────────────┘  └──────────────┘  └──────────────┘          │
│         │                  │                  │                  │
│         └──────────────────┴──────────────────┘                 │
│                            │                                      │
│                 ┌──────────▼──────────┐                         │
│                 │   Repository Core   │                         │
│                 └─────────────────────┘                         │
└─────────────────────────────────────────────────────────────────┘
```

---

## Data Flow

### Session Preparation Flow

```
┌─────────────────┐
│  GM Prepares    │
│   Session       │
└────────┬────────┘
         │
         ▼
┌─────────────────────────────────────────┐
│  python build_context.py --chatgpt     │
└────────┬────────────────────────────────┘
         │
         ▼
┌─────────────────────────────────────────┐
│  Reads State Files:                     │
│  - campaign_state.json                  │
│  - campaign_position.json               │
│  - pc_profile.json                      │
│  - skyrim_clocks.json                   │
│  - Latest session log                   │
└────────┬────────────────────────────────┘
         │
         ▼
┌─────────────────────────────────────────┐
│  Generates Context Bundle:              │
│  - Current position and state           │
│  - Visual clock progress                │
│  - PC details and flags                 │
│  - Recent session summary               │
│  - File references                      │
└────────┬────────────────────────────────┘
         │
         ▼
┌─────────────────────────────────────────┐
│  Output: /tmp/session_context.md        │
└────────┬────────────────────────────────┘
         │
         ▼
┌─────────────────────────────────────────┐
│  Upload to ChatGPT + Session Prompt     │
└────────┬────────────────────────────────┘
         │
         ▼
┌─────────────────────────────────────────┐
│  ChatGPT Ready to Track & Narrate       │
└─────────────────────────────────────────┘
```

---

## Component Relationships

### Core System Components

```
                    ┌──────────────────┐
                    │  Campaign State  │
                    │  (JSON Files)    │
                    └────────┬─────────┘
                             │
            ┌────────────────┼────────────────┐
            │                │                │
            ▼                ▼                ▼
    ┌───────────┐    ┌───────────┐    ┌───────────┐
    │  State    │    │  Clocks   │    │    PC     │
    │  campaign │    │  skyrim   │    │  Profile  │
    │  _state   │    │  _clocks  │    │           │
    └───────────┘    └───────────┘    └───────────┘
            │                │                │
            └────────────────┼────────────────┘
                             │
                    ┌────────▼─────────┐
                    │  Context Builder │
                    │  (build_context) │
                    └────────┬─────────┘
                             │
                    ┌────────▼─────────┐
                    │    ChatGPT       │
                    │   Integration    │
                    └──────────────────┘
```

### NPC Discovery System

```
┌──────────────────┐
│  GM Needs NPC    │
└────────┬─────────┘
         │
         ▼
┌──────────────────────────────┐
│  python npc_lookup.py        │
│  --current / --location /    │
│  --faction / --search        │
└────────┬─────────────────────┘
         │
         ├──► Reads: campaign_position.json (for --current)
         │
         ├──► Searches: npcs/ directory
         │
         ├──► Filters by: Location mappings, Faction mappings
         │
         ▼
┌──────────────────────────────┐
│  Returns NPC File Paths      │
│  Optional: Detailed stats    │
└────────┬─────────────────────┘
         │
         ▼
┌──────────────────────────────┐
│  GM/ChatGPT Uses NPC Stats   │
└──────────────────────────────┘
```

### Encounter Generation Flow

```
┌──────────────────┐
│  Combat Starts   │
└────────┬─────────┘
         │
         ▼
┌──────────────────────────────────┐
│  Check Current Hold              │
│  (from campaign_position.json)   │
└────────┬─────────────────────────┘
         │
         ▼
┌──────────────────────────────────┐
│  Open ENCOUNTER_TABLES.md        │
│  Find Hold Section               │
└────────┬─────────────────────────┘
         │
         ▼
┌──────────────────────────────────┐
│  Choose Difficulty Tier:         │
│  - Mook (0 stress)               │
│  - Minor (2 stress)              │
│  - Significant (3-4 stress)      │
│  - Major (4+ stress)             │
└────────┬─────────────────────────┘
         │
         ▼
┌──────────────────────────────────┐
│  Use Stats or Adjust Aspects     │
└────────┬─────────────────────────┘
         │
         ▼
┌──────────────────────────────────┐
│  Feed to ChatGPT with            │
│  Combat Start Prompt             │
└──────────────────────────────────┘
```

---

## Tool Interaction Map

```
                     ┌──────────────────┐
                     │   GM Session     │
                     └────────┬─────────┘
                              │
          ┌───────────────────┼───────────────────┐
          │                   │                   │
          ▼                   ▼                   ▼
  ┌───────────────┐   ┌──────────────┐   ┌──────────────┐
  │  Before       │   │   During     │   │    After     │
  │  Session      │   │   Session    │   │   Session    │
  └───────┬───────┘   └──────┬───────┘   └──────┬───────┘
          │                  │                   │
          │                  │                   │
    ┌─────▼──────┐      ┌────▼─────┐      ┌─────▼──────┐
    │ build_     │      │ ChatGPT  │      │ session_   │
    │ context.py │      │ Prompts  │      │ stamp.py   │
    └─────┬──────┘      └────┬─────┘      └─────┬──────┘
          │                  │                   │
    ┌─────▼──────┐      ┌────▼─────┐      ┌─────▼──────┐
    │ npc_       │      │ GM Cheat │      │ validate_  │
    │ lookup.py  │      │ Sheets   │      │ state.py   │
    └────────────┘      └────┬─────┘      └─────┬──────┘
                             │                   │
                        ┌────▼─────┐      ┌─────▼──────┐
                        │ Encounter│      │ character_ │
                        │ Tables   │      │ progress   │
                        └──────────┘      └────────────┘
```

---

## File Dependency Graph

```
State Files (Source of Truth)
├── campaign_state.json ──────┬──► build_context.py
├── campaign_position.json ───┼──► npc_lookup.py
├── pc_profile.json ──────────┼──► validate_state.py
└── skyrim_clocks.json ───────┼──► on_track.py
                               │
                               ▼
                        ChatGPT Context
                               │
                               ▼
                        GM Narrative

NPC Files (Reference Data)
├── npcs/companions/ ─────────► npc_lookup.py
├── npcs/NPC_INDEX.md ────────► GM Reference
└── Location Mappings ────────► Context Builder

Module Files (Campaign Structure)
├── modules/acts/ ────────────► on_track.py
├── story_branches/ ──────────► dragonbreak_cue.py
└── hooks/ ───────────────────► GM Planning

Tools (Reference Guides)
├── GM_QUICK_START.md ────────► Session Workflow
├── GM_CHEAT_SHEETS.md ───────► During Play
├── ENCOUNTER_TABLES.md ──────► Combat
└── LOOT_SYSTEM.md ───────────► Rewards
```

---

## Prompt Flow in ChatGPT

```
Session Start
     │
     ▼
┌──────────────────────────┐
│  Load Context Bundle     │
│  + Session Start Prompt  │
└───────────┬──────────────┘
            │
            ▼
┌──────────────────────────┐
│  ChatGPT Loaded &        │
│  Ready to Track          │
└───────────┬──────────────┘
            │
            ├──► Scene Plays
            │         │
            │         ▼
            │    ┌─────────────────┐
            │    │ Mid-Session     │
            │    │ Update Prompt   │
            │    └────┬────────────┘
            │         │
            │         ├──► Aspect Changed
            │         ├──► Stress Taken
            │         ├──► Clock Advanced
            │         └──► FP Spent/Gained
            │
            ├──► Combat Starts
            │         │
            │         ▼
            │    ┌─────────────────┐
            │    │ Combat Start    │
            │    │ Prompt          │
            │    └────┬────────────┘
            │         │
            │         └──► Zone, Enemies, Victory Conditions
            │
            ├──► NPC Appears
            │         │
            │         ▼
            │    ┌─────────────────┐
            │    │ NPC Interaction │
            │    │ Prompt          │
            │    └────┬────────────┘
            │         │
            │         └──► NPC File, Goals, Relationship
            │
            ├──► Scene Transition
            │         │
            │         ▼
            │    ┌─────────────────┐
            │    │ Scene Transition│
            │    │ Prompt          │
            │    └────┬────────────┘
            │         │
            │         └──► New Location, NPCs, Hooks
            │
            └──► Session Ends
                      │
                      ▼
                 ┌─────────────────┐
                 │ Milestone       │
                 │ Assessment      │
                 └────┬────────────┘
                      │
                      └──► Log Creation Help
```

---

## Data Update Cycle

```
       ┌──────────────────────────────────┐
       │        Session Plays             │
       └───────────┬──────────────────────┘
                   │
                   ▼
       ┌──────────────────────────────────┐
       │  Mechanical Changes Occur        │
       │  (Aspects, Stress, Clocks, FP)   │
       └───────────┬──────────────────────┘
                   │
                   ▼
       ┌──────────────────────────────────┐
       │  ChatGPT Tracks Changes          │
       │  (Via Update Prompts)            │
       └───────────┬──────────────────────┘
                   │
                   ▼
       ┌──────────────────────────────────┐
       │  Session Ends                    │
       └───────────┬──────────────────────┘
                   │
                   ▼
       ┌──────────────────────────────────┐
       │  GM Updates State Files:         │
       │  - campaign_state.json           │
       │  - skyrim_clocks.json            │
       │  - campaign_position.json        │
       └───────────┬──────────────────────┘
                   │
                   ▼
       ┌──────────────────────────────────┐
       │  Create Session Log              │
       │  (session_stamp.py)              │
       └───────────┬──────────────────────┘
                   │
                   ▼
       ┌──────────────────────────────────┐
       │  Validate State                  │
       │  (validate_state.py)             │
       └───────────┬──────────────────────┘
                   │
                   ▼
       ┌──────────────────────────────────┐
       │  Next Session Prep               │
       │  (build_context.py)              │
       └───────────┬──────────────────────┘
                   │
                   └────────► Cycle Repeats
```

---

## Integration Points

### ChatGPT ↔ Repository
- **Input**: Context bundles (build_context.py output)
- **Output**: Narrative, mechanical tracking, suggestions
- **Feedback**: Mid-session prompts update ChatGPT state
- **Persistence**: Session logs capture ChatGPT narrative

### GM ↔ Tools
- **Scripts**: Automation for context, NPCs, validation
- **Documentation**: Quick start, cheat sheets, prompts
- **State Files**: Manual updates after sessions
- **Reference**: Encounter tables, loot system

### Players ↔ System
- **Character Sheets**: Enhanced template with full tracking
- **Progression**: Milestone tracker (character_progression.py)
- **Narrative**: ChatGPT narrates outcomes
- **Mechanics**: GM uses cheat sheets for rulings

---

## System Features Summary

```
┌────────────────────────────────────────────────┐
│           SYSTEM CAPABILITIES                  │
├────────────────────────────────────────────────┤
│  ✅ Automated Context Building                 │
│  ✅ ChatGPT Integration                        │
│  ✅ NPC Discovery by Location/Faction          │
│  ✅ Hold-Specific Encounters                   │
│  ✅ Fate-Appropriate Loot                      │
│  ✅ Character Progression Tracking             │
│  ✅ State Validation & On-Track Checking       │
│  ✅ Complete Prompt Library                    │
│  ✅ Session Workflow Guides                    │
│  ✅ At-Table Quick Reference                   │
└────────────────────────────────────────────────┘
```

---

**Version**: 2.0  
**Last Updated**: 2026-01-23  
**Purpose**: Visualize system architecture and component interactions

# ChatGPT Prompt Templates for Skyrim Fate Core Campaign

These prompt templates are designed to help ChatGPT serve as an intelligent campaign tracker, narrator, and mechanics referee for your Fate Core Skyrim campaign.

---

## Session Start Prompt (Full Setup)

```markdown
# Skyrim Fate Core Campaign Session — [Session Number]

You are the Game Master's intelligent assistant for a Fate Core TTRPG campaign set in Skyrim (4E 201). The Dragonborn is absent, and player characters shape the outcome of the civil war and hidden Thalmor conspiracy.

## Your Role
- **Track mechanics**: Aspects, stress, consequences, clocks, fate points
- **Narrate outcomes**: Describe results consistent with Fate Core rules and Skyrim lore
- **Maintain consistency**: Reference loaded context files for continuity
- **Suggest complications**: Offer compels based on PC aspects
- **Ensure balance**: Keep challenges appropriate to PC power level
- **Stay on track**: Reference module structure to maintain campaign rails

## Loaded Context Files
[Paste or reference the output from: python scripts/build_context.py --chatgpt]

## Current Campaign State
- **Act**: [X]
- **Location**: [Current Location]
- **Party Alignment**: [Imperial/Stormcloak/Neutral]
- **Major Clocks**: [List with current values]

## Last Session Summary
[Brief 2-3 sentence recap of where we left off]

## Today's Session Goals
[GM's intended beats or objectives]

## Key NPCs Expected
[List NPCs who might appear this session]

## Important Reminders
- Use Fate Core mechanics (4dF, aspects, fate points, stress/consequences)
- Civil war has real costs; victory is never clean
- Clocks advance based on PC actions and time passing
- Thalmor operate in shadows; early signs are subtle
- PCs have agency; no NPC will solve problems for them

Ready to begin? Please confirm you've loaded the context and are ready to track mechanics.
```

---

## Mid-Session Update Prompt

```markdown
## Session Update — Scene [X]

[Brief description of what just happened]

### Mechanical Updates
- **Aspect Created**: "[Aspect Name]" with [X] free invokes
- **Stress Taken**: [Character] marked [X] stress
- **Consequence**: [Character] took [Mild/Moderate/Severe] consequence: "[Description]"
- **Clock Advanced**: [Clock Name] is now [X/Y] (was [W/Y])
- **Fate Points**: [Character] spent/gained [X] fate points (now at [Y])

### Scene Outcomes
[What changed narratively]

### Next Scene Setup
[Where PCs are headed or what's about to happen]

Please:
1. Acknowledge the mechanical updates
2. Suggest how the clock advancement affects the world
3. Propose 1-2 aspect-based compels for the next scene
4. Remind me of any relevant location aspects or NPC traits
```

---

## Combat Start Prompt

```markdown
## Combat: [Location] vs [Enemy Type]

**Location**: [Name and Hold]  
**Enemies**: [Number and type from ENCOUNTER_TABLES.md]  
**PC Power Level**: Act [X], Refresh [Y]

### Zone Setup
**Zone Aspects**:
- "[Zone Aspect 1]" (free invoke available)
- "[Zone Aspect 2]"

### Enemy Stats
[Reference ENCOUNTER_TABLES.md for stat blocks]

### Combat Tracking Needs
Please track during this combat:
- Initiative order (Notice or approach skills)
- Stress boxes for all participants
- Consequences as taken
- Aspect invokes and compels
- Zone movement and aspect creation

### Victory Conditions
- **PC Victory**: [Condition]
- **Enemy Victory**: [Condition]
- **Concession Available**: [Describe reasonable concession]

Begin! First exchange:
[Describe opening action]
```

---

## NPC Interaction Prompt

```markdown
## NPC Encounter: [NPC Name]

**File Reference**: [Path to NPC file, e.g., npcs/companions/HADVAR_OF_SOLITUDE.md]

### NPC Quick Stats
- **High Concept**: [From file]
- **Trouble**: [From file]
- **Current Status**: [Relationship clock value if tracked]
- **Likely Goals This Scene**: [GM's assessment]

### Campaign Context Affecting This NPC
- **Relevant Flags**: [Any from campaign_state.json]
- **Previous Interactions**: [Brief summary]
- **Party Alignment vs NPC**: [Aligned/Opposed/Neutral]

### Scene Setup
[Where and why this interaction is happening]

Please:
1. Roleplay this NPC consistent with their aspects
2. Suggest likely NPC goals and motivations
3. Identify opportunities for compels (PC or NPC aspects)
4. Track social conflict mechanics if needed (mental stress)
5. Suggest relationship clock changes based on interaction outcome
```

---

## Scene Transition Prompt

```markdown
## Scene Transition: [Old Location] → [New Location]

**Departing**: [Previous location]  
**Arriving**: [New location in Hold X]  
**Time Passed**: [Hours/days]  
**Narrative Reason**: [Why PCs are traveling]

### Check for Triggers
Based on new location and time passed, please:
1. Check if any Dragonbreak moments from DRAGONBREAK_MOMENTS.json are eligible
2. Identify relevant location aspects from modules/locations/ (if file exists)
3. Determine which NPCs are likely present (use NPC_LOCATIONS mapping)
4. Check if any clocks should advance due to time passing
5. Suggest 2-3 scene hooks appropriate to:
   - Current location and Hold politics
   - Party's current alignment and enemies
   - Active clocks and their pressures

### Travel Complications?
Should this transition include a complication? (ambush, encounter, discovery)
```

---

## Clock Advancement Prompt

```markdown
## Clock Update: [Clock Name]

**Previous**: [X/Y]  
**New**: [X+Z/Y]  
**Reason**: [Why this clock advanced]

### Impact Assessment Needed

Please analyze:
1. **How close is this clock to filling?** (urgency level)
2. **What fictional events should this trigger?** (NPCs react, world changes)
3. **Does this create new complications for PCs?** (immediate or upcoming)
4. **Should other clocks advance as a result?** (cascading effects)
5. **What compels does this suggest?** (pressure on PC aspects)

### If Clock Filled
If this clock just filled, please:
- Describe the major complication or turning point
- Suggest narrative consequences
- Identify which act or scene this transitions to
- Recommend updates to campaign_state.json flags
```

---

## Compel Suggestion Prompt

```markdown
## Request: Aspect-Based Compel Ideas

**Current Scene**: [Brief description]  
**Active PC Aspects**:
- High Concept: "[PC High Concept]"
- Trouble: "[PC Trouble]"
- Other Aspects: "[List active aspects]"

**Campaign Pressures**:
- [List relevant clocks, flags, or NPCs creating pressure]

Please suggest 2-3 compels that:
1. Are narratively interesting (not just mechanical penalties)
2. Create meaningful choices or complications
3. Tie to current scene or campaign pressures
4. Feel fair and genre-appropriate
5. Offer clear outcomes if accepted

Format: "Because you have [ASPECT], it makes sense that [COMPLICATION]. Accept for a fate point?"
```

---

## Milestone / End of Session Prompt

```markdown
## Session [X] Complete — Milestone Assessment

**Session Duration**: [Hours]  
**Major Accomplishments**:
- [List PC achievements this session]

**Clocks Advanced**:
- [List all clock changes]

**New Aspects/Consequences**:
- [List created/cleared aspects and consequences]

**Fate Points End-of-Session**:
- [Character]: [X] fate points

### Milestone Type
Based on accomplishments, this feels like a:
- [ ] Minor Milestone (swap skills/stunts/aspects)
- [ ] Significant Milestone (+1 skill point, some advancement)
- [ ] Major Milestone (+refresh, significant power)

### Session Log Creation
Please help create a session log with:
1. **Chronicle** (700-1200 word narrative recap in Skyrim war-chronicle style)
2. **Mechanical Updates** (clocks, aspects, stress, consequences, stunts)
3. **Open Threads** (unresolved complications for next session)
4. **GM Notes** (anything important for continuity)

### State File Updates Needed
Recommend updates to:
- `state/campaign_state.json` (flags, hold control, party state)
- `state/campaign_position.json` (location, scene, act if changed)
- `clocks/skyrim_clocks.json` (all advanced clocks)
```

---

## Rules Clarification Prompt

```markdown
## Fate Core Rules Question

**Situation**: [Describe what's happening]  
**Question**: [Specific rules question]

**Reference Files Available**:
- `rules/fate_core_quickref.md`
- `rules/fate_system_toolkit_menu.md`
- `fate-core/mechanics/`

Please:
1. Explain the relevant Fate Core rule
2. Cite the specific section if possible
3. Provide example of how it applies to this situation
4. Suggest 2-3 ways to adjudicate if rule is ambiguous
5. Recommend the most genre-appropriate interpretation for gritty Skyrim
```

---

## Loot Distribution Prompt

```markdown
## Loot Award: [Victory Type]

**Victory Type**: [Minor/Significant/Major/Milestone]  
**Defeated Enemies**: [List]  
**Location**: [Hold and specific place]  
**Current Act**: [X]

**Reference**: See `tools/LOOT_SYSTEM.md` for guidelines

Please suggest appropriate loot:
1. **Aspects** (with free invokes): [1-2 suggestions]
2. **Permissions** (story access): [1-2 suggestions]
3. **Resources** (gold, trade goods): [Amount appropriate to tier]
4. **Extras** (if appropriate for major victory): [0-1 suggestion with refresh cost]

**Loot Philosophy Reminder**:
- Tie loot to story and location
- Include compellable aspects on powerful items
- Prefer narrative permissions over numerical bonuses
- Ensure loot advances character story arcs
```

---

## On-Track Validation Prompt

```markdown
## Campaign Rails Check

**Current State**:
- Act: [X]
- Scene: [Scene ID]
- Location: [Location]

**Module Expectation** (from startup_defaults.json and act files):
- Expected Act: [Y]
- Expected Scene: [Scene ID]
- Expected Location: [Location]

### Divergence Analysis
Please assess:
1. Are we on the module rails or diverged?
2. If diverged, is this a **good divergence** (player agency) or **accidental drift**?
3. Should we realign to module or embrace the new direction?
4. What would realignment require? (scene transition, retroactive continuity, etc.)

### Recommendation
Based on:
- Player enjoyment and engagement
- Story coherence
- Campaign pillar adherence (war costs, Thalmor threat, player agency)

Recommend: [Stay diverged / Realign to module / Hybrid approach]
```

---

## Dragonbreak Moment Prompt

```markdown
## Dragonbreak Moment Check

**Current Scene**: [Scene ID]  
**Current Act**: [X]

**Reference**: `story_branches/DRAGONBREAK_MOMENTS.json`

Please check:
1. Are any Dragonbreak moments eligible for this scene/act?
2. If yes, provide:
   - Moment title and GM cue
   - Player-facing prompt
   - Recommended state updates

### Dragonbreak Philosophy
Dragonbreaks are for:
- Reconciling contradictory player decisions
- Embracing timeline forks as canon
- Creating surreal, mythic moments
- Resolving irreconcilable outcomes

Use sparingly and with player buy-in. Make them narratively interesting, not just mechanical fixes.
```

---

## Emergency "I'm Lost" Prompt

```markdown
## GM Needs Orient

I've lost track of campaign state. Please help me get oriented:

1. **Where are we?** (Act, scene, location)
2. **What just happened?** (Last 2-3 major events)
3. **What are the immediate pressures?** (Clocks near filling, enemies pursuing, etc.)
4. **What are likely next scenes?** (Based on module structure and current state)
5. **What should I prep?** (NPC files, location files, encounter stats)

**Available Context**:
[Paste output from: python scripts/build_context.py]

Please give me a clear, concise orientation so I can continue the session smoothly.
```

---

## Tips for Using These Prompts

1. **Start every session** with the full Session Start Prompt
2. **Update incrementally** using Mid-Session Update Prompts
3. **Reference files explicitly** so ChatGPT knows where to look
4. **Track everything** — better to over-track than lose information
5. **Trust the clocks** — let them drive consequences and complications
6. **Embrace aspects** — they're the heart of Fate Core
7. **Use Emergency Prompt** if you ever feel lost or overwhelmed

---

**Version**: 2026-01-23  
**Purpose**: Enable ChatGPT to be an intelligent, consistent, and helpful campaign assistant  
**Maintained By**: Campaign GM

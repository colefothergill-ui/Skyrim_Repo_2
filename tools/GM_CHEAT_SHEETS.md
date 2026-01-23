# GM Cheat Sheets — At-the-Table Reference

Quick reference cards for common situations during play.

---

## FATE CORE BASICS

### The Ladder
```
+8  Legendary
+7  Epic
+6  Fantastic
+5  Superb
+4  Great
+3  Good
+2  Fair
+1  Average
 0  Mediocre
-1  Poor
-2  Terrible
```

### Four Actions
1. **Overcome** — Get past obstacle (skill vs difficulty)
2. **Create Advantage** — Make aspects/get free invokes (skill vs defense)
3. **Attack** — Cause stress/consequences (skill vs defense)
4. **Defend** — Prevent attacks/advantages (skill vs skill)

### Four Outcomes
- **Fail** (0-1): Succeed at serious cost, or fail
- **Tie** (0): Succeed at minor cost, or partial success
- **Success** (1-2): You do what you wanted
- **Success with Style** (3+): Success + bonus (boost or extra invoke)

### Fate Points
- **Invoke Aspect**: +2 or reroll (costs 1 FP)
- **Compel Aspect**: Complication for 1 FP (player can refuse for 1 FP)
- **Refuse Compel**: Pay 1 FP to avoid complication
- **Refresh**: Start session at Refresh value

---

## COMBAT QUICK REFERENCE

### Initiative
Everyone rolls Notice (or appropriate skill). Highest goes first. Ties act simultaneously.

### Zones
- **Same Zone**: No roll to interact
- **Adjacent Zone**: No roll to move, action to attack
- **Far Zone**: Action to move, can't attack without ranged

### Stress & Consequences
**Stress**: Check boxes, clear at end of scene  
**Consequences**:
- Mild (2): Clear next scene after treatment
- Moderate (4): Clear next session after treatment  
- Severe (6): Clear next scenario after treatment

**Taken Out**: Winner decides what happens (within reason)

### Attack vs Defense
1. Attacker rolls Attack skill
2. Defender rolls Defend skill
3. If Attacker wins, Defender takes Shifts as stress
4. Defender can absorb with stress boxes or consequences
5. If can't/won't absorb, Defender is Taken Out

---

## OPPOSITION DIFFICULTY

### Static Difficulty
Use when no active opposition:
- **Easy**: +0 to +1
- **Moderate**: +2
- **Hard**: +3 to +4
- **Very Hard**: +5 to +6
- **Nearly Impossible**: +7+

### Active Opposition
NPC/Enemy rolls their skill vs PC skill

### Mooks, Minors, Significant, Major
- **Mook**: 0 stress, 1-2 skills at +1 to +2
- **Minor**: 2 stress, 2-4 skills at +2 to +3
- **Significant**: 3-4 stress, 4-6 skills at +3 to +4, mild consequence
- **Major**: 4+ stress, 6+ skills at +4 to +5, all consequences, stunts

---

## ASPECT ECONOMY

### Creating Advantages
- **Success**: Create aspect with 1 free invoke
- **SWS**: Create aspect with 2 free invokes
- **Existing Aspect**: Success gives 1 free invoke, SWS gives 2

### Invoking Aspects
- **Boost** (free, one-time): Use or lose
- **Free Invoke**: From creating advantage or SWS
- **Paid Invoke**: Spend 1 FP for +2 or reroll

### Compelling Aspects
**Offer**: "Because you have [ASPECT], it makes sense that [COMPLICATION]. Accept for a FP?"  
**Accept**: Take FP, embrace complication  
**Refuse**: Pay 1 FP to avoid complication

---

## CLOCK QUICK REFERENCE

### When to Tick Clocks
- **PC Direct Action**: Affects clock directly (capture hold, expose Thalmor)
- **PC Indirect Action**: Creates consequence (ignore crisis, create collateral damage)
- **Time Passing**: Factions pursue goals during downtime
- **Fictional Trigger**: Event happens that affects clock (ambush succeeds, sabotage discovered)

### How Many Ticks?
- **Minor Impact**: +1 tick
- **Significant Impact**: +2 ticks
- **Major Impact**: +3 ticks
- **Campaign-Shaking**: +4+ ticks

### Clock Fills
- **Master Clock**: Campaign enters endgame phase
- **Act Clock**: Current act concludes, next act begins
- **Faction Clock**: Faction achieves goal or faces crisis
- **Personal Clock**: PC faces consequence or gains benefit

---

## LOOT QUICK REFERENCE

### By Victory Type
- **Minor** (ordinary fight): 1-2 common items, 50-150 gold
- **Significant** (tough fight/side quest): 1 uncommon, 2-3 common, 200-500 gold
- **Major** (boss/main quest): 1 rare, 1-2 uncommon, 500-2000 gold, major permission

### Loot Types
1. **Aspect** (with free invokes): "Jarl's Sealed Orders" (2 invokes)
2. **Permission**: "Dark Brotherhood Passwords" (access sanctuaries)
3. **Extra** (-Refresh): "Blade of Woe" (-1 Refresh, +2 Stealth kills)
4. **Resource**: Gold, trade goods, consumables

### Quick Loot Generator
**Template**: "[Descriptor] [Item]" with [X] free invokes  
**Example**: "Stormcloak Battle Map" with 2 free invokes on planning ambush

---

## COMPEL QUICK REFERENCE

### Good Compels
- Create interesting choices
- Push story forward
- Tie to character aspects
- Offer clear benefit for acceptance (FP)
- Feel fair and genre-appropriate

### Bad Compels
- Just mechanical penalty with no story
- Punish character unfairly
- Remove player agency
- Bore the table

### Compel Formula
"Because you have **[ASPECT]**, it makes sense that **[COMPLICATION]**. Accept for a fate point?"

### Examples
- "Because you're **Honorable Imperial Soldier**, you can't ignore the civilian in danger, even though the enemy is escaping."
- "Because of **The Secret of My Sanguine**, the Vigilant of Stendarr notices your avoidance of the shrine."
- "Because you're **Hadvar's Shield-Brother**, he asks you to cover for him while he investigates something dangerous alone."

---

## SCENE STRUCTURE

### Scene Beats
1. **Establish**: Where, who, what's happening
2. **Rising Action**: Introduce complication or obstacle
3. **Climax**: Choice or conflict
4. **Resolution**: Outcome and consequences
5. **Transition**: Bridge to next scene

### Scene Types
- **Action**: Combat, chase, physical conflict
- **Social**: Negotiation, deception, investigation
- **Discovery**: Clues, revelations, exploration
- **Downtime**: Rest, shopping, relationship building

### Scene Length
- **Quick** (15 min): Single obstacle or choice
- **Standard** (30 min): Full scene with multiple beats
- **Extended** (45+ min): Complex conflict or major choice

---

## NPCS ON THE FLY

### Quick NPC Builder
1. **Name**: Nordy McSkyrimface
2. **High Concept**: "Grizzled Whiterun Guard"
3. **Skills**: Pick 1-2 at +2 (Fight, Notice)
4. **Aspect**: "Seen It All, Believe Nothing"

### NPC Attitude
- **Hostile**: Will attack or actively oppose
- **Unfriendly**: Won't help, might hinder
- **Neutral**: Indifferent, transactional
- **Friendly**: Willing to help
- **Allied**: Committed supporter

---

## SESSION FLOW CHECKLIST

### Start of Session
- [ ] Build context bundle (build_context.py)
- [ ] Load into ChatGPT with session start prompt
- [ ] Review last session log
- [ ] Check current clocks and flags
- [ ] Prep NPCs and encounters for expected scenes

### During Session
- [ ] Track aspects, stress, consequences
- [ ] Update ChatGPT incrementally
- [ ] Offer compels on PC aspects
- [ ] Tick clocks based on actions
- [ ] Award fate points for compels

### End of Session
- [ ] Create session log (session_stamp.py)
- [ ] Update state files (campaign_state, clocks, position)
- [ ] Assess milestone (character_progression.py --suggest)
- [ ] Validate state (validate_state.py, on_track.py)
- [ ] Preview next session

---

## WHEN STUCK

### "What Happens Next?"
1. Check active clocks — which is closest to filling?
2. Compel a PC aspect — what complication does it create?
3. Introduce NPC with agenda — what do they want?
4. Escalate existing threat — how does it get worse?

### "How Do I Rule This?"
1. What's most interesting narratively?
2. What gives PCs meaningful choice?
3. What creates complications?
4. What maintains genre (gritty war, real costs)?

### "Players Went Off-Rails"
1. Is this more interesting than planned scene?
2. Can I adapt planned content to new direction?
3. Should I embrace divergence or gently redirect?
4. Run on_track.py to assess drift

---

## CAMPAIGN PILLARS REMINDER

### 1. Gritty War with Real Costs
Every battle has consequences. Victory isn't clean.

### 2. Diplomacy, Espionage, Political Intrigue  
Swords don't solve everything. Leverage matters.

### 3. Branching Thalmor Danger
The true enemy operates in shadows. Early signs are subtle.

### 4. Player Agency Over Skyrim's Fate
PCs decide outcomes. No NPC solves problems for them.

---

## COMMON RULINGS

**Can I do X?**  
→ If aspect supports: Bonus. If skill supports: Roll. Otherwise: High difficulty or "no."

**What's the difficulty?**  
→ Passive target? Use ladder. Active opposition? They roll.

**How much stress?**  
→ Shifts over defense = stress. Absorb with boxes or consequences.

**Do I need an aspect to do X?**  
→ Aspects give permission for unusual actions or bonus on relevant actions.

**Can I create advantage on myself?**  
→ Yes! "Taking Aim," "Psyching Up," "Reading the Battlefield"

**Can I use this aspect again?**  
→ Free invokes: use once. Persistent aspects: pay to invoke repeatedly.

---

**Version**: 2026-01-23  
**Purpose**: Quick at-table reference for common GM situations  
**Print**: Print this for your GM screen or keep on tablet

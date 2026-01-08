# Master Key — Skyrim Fate Core Campaign (4E 201)

This document defines the campaign's **premise**, **play pillars**, and **clock philosophy** — the foundation for all narrative, mechanical, and GM workflow decisions.

---

## Campaign Premise

**Era:** 4E 201  
**Setting:** Skyrim, during the civil war between the Stormcloaks and the Empire.

### The Core Twist
**The Dragonborn is absent.**  
There is no prophecy-bound hero to resolve the civil war, defeat Alduin, or expose the Thalmor conspiracy. The **player characters** are Skyrim's only hope — and their choices will determine the future of the province, the Empire, and the Aldmeri Dominion's endgame.

### The Stakes
- **Civil War:** Skyrim is bleeding. Holds are contested. Refugees flood neutral cities. Every battle has a cost.
- **Thalmor Manipulation:** The Aldmeri Dominion is covertly fueling both sides, prolonging the war to weaken humanity. Proof of this manipulation is hidden — and explosive.
- **No Safety Net:** Player decisions matter. Holds can fall permanently. NPCs can die. Factions can splinter. The war can end in disaster — or hope.

---

## Play Pillars

These are the **core experiences** the campaign is designed to deliver.

### 1. Gritty War with Real Costs
- Battles have consequences: wounded soldiers, burned farms, broken families.
- Victory is not clean. Diplomacy and compromise are as important as combat.
- **Compels:** War fatigue, moral dilemmas, collateral damage, impossible choices.

### 2. Diplomacy, Espionage, and Political Intrigue
- Holds are won through alliance-building, intelligence networks, and leverage — not just swords.
- NPCs have agendas. Factions have secrets. Trust is earned, not given.
- **Compels:** Betrayal, blackmail, information leaks, conflicting loyalties.

### 3. Branching Thalmor Danger
- The Thalmor are the **true enemy**, but they operate in shadows.
- Early signs are subtle: saboteurs, planted agitators, missing shipments, convenient "accidents."
- Exposing the Thalmor endgame is a **major campaign flag** that shifts the entire war.
- **Compels:** Thalmor retaliation, planted evidence, assassination attempts, false-flag operations.

### 4. Player Agency Over Skyrim's Fate
- The PCs decide which side (if any) to support, which holds fall, and how the war ends.
- No NPC will solve the war for them. No prophecy will save them.
- **Compels:** Leadership burdens, public scrutiny, faction obligations, reputation costs.

---

## Clock Philosophy

Clocks are the **engine of consequence** in this campaign. They create pressure, track momentum, and ensure the world responds to PC actions (and inaction).

### Clock Types

#### Master Clocks
**Purpose:** Track the **overarching endgame**.  
**Examples:**
- `civil_war_endgame` — Ticks when holds fall or decisive victories happen. Fill = war reaches its final phase (Solitude or Windhelm under siege).
- `thalmor_influence` — Ticks on atrocities, sabotage, and Dominion manipulation. Fill = Thalmor endgame escalates to open confrontation.

**GM Use:** These clocks span the entire campaign. Tick them sparingly (major events only). When they fill, the campaign shifts into its final act.

#### Act Clocks
**Purpose:** Track **narrative momentum** within each act.  
**Examples:**
- `act_01_whiterun_outcome` — Tracks Whiterun's decision-making pressure. Fill = Whiterun chooses a side (or falls).
- `act_02_fronts_shift` — Tracks escalation across multiple holds. Fill = the war enters a new, bloodier phase.

**GM Use:** These clocks drive the pacing of each act. Tick them based on PC actions, faction moves, and time passing. When they fill, introduce the next act's complications.

#### Faction Clocks
**Purpose:** Track **faction-specific arcs** and side plots.  
**Examples:**
- `thieves_guild_restoration` — Tracks the Guild's resurgence in the Rift. Fill = the Guild becomes a major power broker (or collapses).
- `dark_brotherhood_emperor_plot` — Tracks the Brotherhood's assassination mission. Fill = the Emperor dies (or the Brotherhood is exposed).

**GM Use:** Tick these when PCs engage with faction storylines or when factions act independently. Fills unlock new complications, allies, or enemies.

---

## When to Tick Clocks

### PC Actions
- **Direct Impact:** PCs capture a hold, expose a Thalmor agent, or complete a faction mission → tick relevant clocks.
- **Indirect Impact:** PCs ignore a brewing crisis, delay a decision, or create collateral damage → tick clocks that represent escalation or consequence.

### Time Passing
- **Downtime:** If PCs spend a week recovering, factions don't wait. Tick clocks for NPCs pursuing their own goals.
- **Inaction:** If PCs delay a critical decision, tick clocks that represent the world moving forward without them.

### Fictional Triggers
- **Faction Moves:** A Stormcloak ambush succeeds → tick `civil_war_endgame` or `act_02_fronts_shift`.
- **Thalmor Sabotage:** A grain shipment burns → tick `thalmor_influence`.
- **NPC Agendas:** A Jarl makes a political move → tick their personal relationship clock or a faction clock.

---

## Clock Fills: What Happens?

When a clock fills, **introduce a major complication or turning point**:
- **Master Clock Fills:** The campaign enters its endgame. Example: `civil_war_endgame` fills → Solitude or Windhelm is under siege.
- **Act Clock Fills:** The current act concludes, and the next act's complications emerge. Example: `act_01_whiterun_outcome` fills → Whiterun chooses a side, and Act II's fronts begin to shift.
- **Faction Clock Fills:** A faction achieves its goal or faces a crisis. Example: `thieves_guild_restoration` fills → the Guild demands payment or loyalty from the PCs.

**GM Principle:** Clocks are not punishments. They are **narrative momentum**. Fills should feel like the world is alive and responding to the PCs — for better or worse.

---

## Example Clock Usage

### Scenario: PCs Capture a Stormcloak Courier
**GM Thinks:**
- The courier carried intel about Thalmor contact → tick `thalmor_influence` (+1).
- The capture weakens Stormcloak coordination → tick `act_02_fronts_shift` (+1).
- The PCs interrogated the courier with restraint → don't tick any brutality/reputation clocks.

**Result:** The world responds. Thalmor become more cautious. The war shifts slightly toward Imperial advantage. The PCs' choices mattered.

---

## Design Goals

1. **Transparency:** PCs should know (roughly) when clocks are ticking and why.
2. **Consequence:** Clocks ensure inaction and action both have weight.
3. **Momentum:** Clocks keep the campaign moving forward, even when PCs hesitate.
4. **Agency:** PCs can slow, speed up, or redirect clocks through their choices.

---

**Campaign ID:** SKYRIM-4E201  
**Version:** 2025-12-30  
**GM Notes:** Clocks are tools, not rails. If a clock no longer fits the fiction, adjust it. The story is the boss.
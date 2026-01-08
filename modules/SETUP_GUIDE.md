# Skyrim Fate Core Vault Setup Guide

This guide walks you through setting up and using the Skyrim Fate Core Campaign Vault for desktop development, GM automation, and creative campaign management.

---

## 🚀 Quick Start

### First-Time Setup

1. **Run the onboarding script:**
   ```bash
   python scripts/first_run.py
   ```
   This interactive guide walks you through the repository structure and key concepts.

2. **Run the vault audit:**
   ```bash
   bash scripts/audit_vault.sh
   ```
   This validates all JSON files, checks for banned terms, and confirms repository integrity.

3. **Set up bash aliases (optional):**
   ```bash
   bash scripts/setup_aliases.sh
   source ~/.bashrc
   ```
   This creates convenient shortcuts for common commands.

---

## 📋 Pre-Session Checklist

Before each session:

- [ ] Review current campaign state:
  ```bash
  cat state/campaign_state.json
  cat clocks/skyrim_clocks.json
  ```

- [ ] Check for Dragonbreak moment eligibility:
  ```bash
  python scripts/dragonbreak_cue.py
  ```

- [ ] Review location guides for expected session locations:
  ```bash
  cat modules/locations/whiterun_hold.md
  ```

- [ ] Select 2-3 hooks from `/hooks/HOOK_BANK.md` to weave into play

---

## 🎮 Starting a Session

Use **zone-in commands** to begin play:

```bash
ZONE-IN: Helgen        # Classic escape scenario
ZONE-IN: Whiterun      # Neutral ground, Companions
ZONE-IN: Jorrvaskr     # Mead hall, honor culture
ZONE-IN: Windhelm      # Stormcloak capital
ZONE-IN: Solitude      # Imperial stronghold
```

See `/modules/locations/` for detailed location guides with:
- Aspects (for scene setting)
- Meditation spots (for character moments)
- Memory echoes (for atmospheric flavor)
- GM hooks (for complications)

---

## 📝 Post-Session Workflow

After each session:

1. **Create session log:**
   ```bash
   python scripts/session_stamp.py
   ```
   This creates a timestamped log file. Fill it out with session details.

2. **Update campaign clocks:**
   Edit `/clocks/skyrim_clocks.json` and tick relevant clocks:
   - Master clocks (civil war endgame, Thalmor influence)
   - Act clocks (current act progress)
   - Faction clocks (guild quests, side plots)

3. **Update campaign state:**
   Edit `/state/campaign_state.json`:
   - Hold control (which faction controls each hold)
   - Major flags (Whiterun decided, Thalmor evidence found, etc.)
   - Party alignment (Stormcloak/Imperial lean)
   - Allies and enemies lists

4. **Update quest flags:**
   Edit `/state/quest_flags.json`:
   - Main quest progression
   - Faction quest states
   - Daedric quest completions
   - Location discoveries

5. **Update party state:**
   Edit `/state/party_state.json`:
   - Active companions
   - Party cohesion clock
   - Morale level
   - Resources and contacts

6. **Update NPC clocks (if needed):**
   If relationship or personal clocks tick, update individual NPC files in `/npcs/`.

7. **Review hooks:**
   Check `/hooks/` for triggered complications to weave into the next session.

---

## 🛠️ GM Automation Tools

### Core Tools

| Tool | Purpose | Command |
|------|---------|---------|
| **Vault Audit** | Full integrity check | `bash scripts/audit_vault.sh` |
| **Session Stamp** | Create timestamped log | `python scripts/session_stamp.py` |
| **Dragonbreak Cue** | Check mythic moment eligibility | `python scripts/dragonbreak_cue.py` |
| **First Run** | Onboarding for new GMs | `python scripts/first_run.py` |
| **Custom Scan** | Validate for banned terms | `python scripts/custom_scan.py` |
| **Validate State** | Check state file integrity | `python scripts/validate_state.py` |

### Bash Aliases

After running `bash scripts/setup_aliases.sh`, you get:

- `clocks` — View campaign clocks
- `state` — View campaign state
- `party` — View party state
- `quests` — View quest flags
- `newsession` — Create new session log
- `checkdragonbreak` — Check Dragonbreak eligibility
- `vaultscan` — Scan for banned terms
- `vaultvalidate` — Validate state files
- `dragonbreak` — Search for Dragonbreak references

---

## 🌀 Dragonbreak Moments

**Dragonbreaks** are rare, optional mythic thread opportunities.

### When to Offer

Offer a Dragonbreak moment ONLY when:
- A major/act clock is at 50% or more
- A faction clock is 1 tick from complete
- The location is ancient/mythic/hidden (ruins, barrows, Dwemer sites, forbidden shrines)

### What They Do

- Reveal clues, prophecy fragments, artifact whispers, agent slips, or cursed omens
- Create new Aspects, hooks, or clock ticks
- Always risky and tempting; never mandatory

### Flavor Text

When triggering a Dragonbreak:

> Your vision blurs. For a heartbeat, you're both here and... not.
> The wind whispers a name you've never heard—but mourn.
> 
> Time fractures. The world remembers what hasn't happened yet.

See `/story_branches/SECRET_TURNS.md` for more details.

---

## 📁 Repository Structure

```
/clocks/          — Progress clocks (master, act, faction)
/state/           — Campaign state, quest flags, party state
/modules/         — Act modules and location guides
  /acts/          — Five Acts structure
  /locations/     — Hold and city guides
/factions/        — Faction packs
/npcs/            — Named NPCs with aspects and stunts
/pcs/             — Player character sheets
/hooks/           — Story hooks by act and faction
/logs/            — Session logs
/rules/           — Fate Core mechanics and quickrefs
/scripts/         — GM automation and validation tools
/story_branches/  — Alternate outcomes and secret turns
```

---

## 🎯 Campaign Philosophy

- **Era:** 4E 201 — Civil war is active
- **No Dragonborn:** PCs are the heroes; no prophecy safety net
- **PCs Shape Outcomes:** Player decisions determine which holds fall, who rules Skyrim, and whether the Thalmor endgame is exposed
- **Thalmor Endgame:** The Aldmeri Dominion manipulates both sides; proof is a major campaign flag
- **Gritty Tone:** War has costs; diplomacy, espionage, and moral compromise matter as much as combat
- **Progress Tracking:** Use Fate Core clocks for all progression
- **Dragonbreak Moments:** Rare mythic threads; not mandatory

---

## 🔍 Troubleshooting

### JSON Validation Errors

If a JSON file fails validation:
```bash
python -m json.tool <file.json>
```
This will show the exact error line.

### Banned Terms Found

If the custom scan finds banned terms:
```bash
python scripts/custom_scan.py
```
Review the output and remove any references to previous campaign settings.

### Missing Files

If files are missing, check the folder structure:
```bash
tree -L 2
```

---

## 📚 Further Reading

- `MASTER_KEY.md` — Campaign premise, play pillars, clock philosophy
- `INDEX.md` — Structured outline of all campaign elements
- `.github/copilot-instructions.md` — Instructions for GitHub Copilot

---

## 🌟 May your legends echo across Sovngarde.

# Quick Start Guide - Post-Fix Repository

This repository has been polished and debugged. Here's how to use it effectively with ChatGPT for your TTRPG sessions.

## ✅ What Was Fixed

1. **JSON Structure Issues** - All state files are now consistent and valid
2. **Banned Terms Removed** - All erroneous WoW/BFA references removed
3. **Error Handling Improved** - Scripts are now more resilient to errors
4. **Full Validation Passing** - All tests pass successfully

See `REPOSITORY_FIXES_SUMMARY.md` for complete details.

---

## 🚀 Getting Started

### First Time Setup

```bash
# Run the onboarding guide
python scripts/first_run.py

# Validate everything is working
bash scripts/audit_vault.sh
```

### Before Each Session

```bash
# Get current campaign context
python scripts/build_context.py

# Check for Dragonbreak moments
python scripts/dragonbreak_cue.py

# Create a new session log
python scripts/session_stamp.py
```

### Quick Health Check

```bash
# Validate state files
python scripts/validate_state.py

# Scan for banned terms
python scripts/custom_scan.py
```

---

## 📁 Key Files for ChatGPT

When starting a ChatGPT session for your TTRPG, share these files:

### Essential Context
1. **MASTER_KEY.md** - Campaign premise and philosophy
2. **state/campaign_state.json** - Current campaign state
3. **state/campaign_position.json** - Where you are in the story
4. **clocks/skyrim_clocks.json** - Progress tracking
5. **state/pc_profile.json** - Active character

### Session Resources
- **modules/acts/** - Current act module
- **story_branches/DRAGONBREAK_MOMENTS.json** - Special moments
- **hooks/HOOK_BANK.md** - Story hooks to weave in

---

## 🎮 Running a Session with ChatGPT

### Step 1: Load Context
Copy and paste to ChatGPT:
```
I'm running a Skyrim Fate Core TTRPG campaign. Here's the current state:

[Paste output from: python scripts/build_context.py]
```

### Step 2: Start Scene
Use zone-in commands:
```
ZONE-IN: Whiterun
ZONE-IN: Jorrvaskr
ZONE-IN: Windhelm
```

### Step 3: After Session
1. Update `/logs/` with session notes
2. Tick relevant clocks in `/clocks/skyrim_clocks.json`
3. Update `/state/campaign_state.json` with changes
4. Run validation: `python scripts/validate_state.py`

---

## 🛠️ Available Tools

### Python Scripts
- `first_run.py` - First-time onboarding
- `validate_state.py` - Validate state files
- `custom_scan.py` - Scan for banned terms
- `build_context.py` - Generate GM context
- `session_stamp.py` - Create session logs
- `dragonbreak_cue.py` - Check for Dragonbreak moments
- `secret_turn_check.py` - Check Secret Turn eligibility
- `on_track.py` - Verify campaign alignment

### Shell Scripts
- `audit_vault.sh` - Full repository integrity check
- `setup_aliases.sh` - Set up convenient bash aliases

---

## ✨ Best Practices

### For ChatGPT Sessions
1. **Always** provide current state context at session start
2. **Keep** campaign_state.json updated after major events
3. **Tick** relevant clocks as story progresses
4. **Validate** state files before and after sessions
5. **Document** key moments in `/logs/`

### For Repository Health
1. Run `bash scripts/audit_vault.sh` weekly
2. Keep JSON files properly formatted
3. Don't manually edit PC sheets during active sessions
4. Back up `/state/` and `/clocks/` directories regularly

---

## 🐛 Troubleshooting

### If a script fails:
```bash
# Check Python version (needs 3.8+)
python --version

# Validate JSON files
python scripts/validate_state.py

# Run full audit
bash scripts/audit_vault.sh
```

### If ChatGPT seems confused:
1. Provide fresh context from `build_context.py`
2. Check current scene in `campaign_position.json`
3. Review recent logs in `/logs/`

### If validation fails:
1. Check error message for specific file
2. Validate JSON syntax with `python -m json.tool <file>`
3. Compare with template files in `/state/templates/`

---

## 📖 Documentation

- `README.md` - Repository overview
- `MASTER_KEY.md` - Campaign premise and pillars
- `INDEX.md` - Structured outline of campaign
- `SETUP_GUIDE.md` - Detailed setup instructions
- `REPOSITORY_FIXES_SUMMARY.md` - What was fixed and why

---

## 🎯 Current Campaign Status

**Act:** 1 - Battle of Whiterun  
**Scene:** S3_GATEHOUSE_PURGE_POST_DUEL  
**Location:** Whiterun — Gatehouse (Inner)  
**PC:** Eltric Stagborne (Stormcloak Champion)  
**Status:** ✅ Ready for play

---

## ⚡ Quick Command Reference

```bash
# Validation suite
python scripts/validate_state.py && python scripts/custom_scan.py

# Session prep
python scripts/build_context.py > session_context.txt

# New session
python scripts/session_stamp.py

# Check special moments
python scripts/dragonbreak_cue.py

# Full audit
bash scripts/audit_vault.sh
```

---

## 🎲 Ready to Play!

Your repository is now clean, validated, and ready for epic Skyrim adventures with ChatGPT!

**May your legends echo across Sovngarde!** 🏔️⚔️

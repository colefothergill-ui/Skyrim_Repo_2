#!/bin/bash
# audit_vault.sh
# Core Dev Check and Enhancement Suite for Tamriel-Skyrim-Repos
# This script validates the Skyrim Fate Core Vault integrity

echo "🧠 Loading Skyrim Fate Core Vault Integrity Check..."
echo ""

VAULT_ROOT="/home/runner/work/Tamriel-Skyrim-Repos/Tamriel-Skyrim-Repos"
cd "$VAULT_ROOT" || exit 1

## 1. Validate all scripts and flag nonconformant code
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "📋 STEP 1: Running custom scan for banned terms..."
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
python3 scripts/custom_scan.py
SCAN_RESULT=$?
if [ $SCAN_RESULT -ne 0 ]; then
    echo "⚠️  Custom scan flagged issues. Review above!"
    exit 1
else
    echo "✅ Custom scan passed."
fi
echo ""

## 2. Check for unreferenced clocks / dangling triggers
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "📋 STEP 2: Checking for old clock references..."
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
if grep -r "bfa_clocks.json" . --exclude="audit_vault.sh" 2>/dev/null; then
    echo "⚠️  Old clock refs found!"
    exit 1
else
    echo "✅ Clock refs clean."
fi
echo ""

## 3. Confirm JSON integrity
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "📋 STEP 3: Validating JSON files..."
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

# Check skyrim_clocks.json
if python3 -m json.tool clocks/skyrim_clocks.json > /dev/null 2>&1; then
    echo "✅ clocks/skyrim_clocks.json valid."
else
    echo "❌ Clock JSON error!"
    exit 1
fi

# Check campaign_state.json
if python3 -m json.tool state/campaign_state.json > /dev/null 2>&1; then
    echo "✅ state/campaign_state.json valid."
else
    echo "❌ State JSON error!"
    exit 1
fi

# Check quest_flags.json
if python3 -m json.tool state/quest_flags.json > /dev/null 2>&1; then
    echo "✅ state/quest_flags.json valid."
else
    echo "❌ Quest flags JSON error!"
    exit 1
fi

# Check party_state.json
if python3 -m json.tool state/party_state.json > /dev/null 2>&1; then
    echo "✅ state/party_state.json valid."
else
    echo "❌ Party state JSON error!"
    exit 1
fi

# Check campaign_position.json
if python3 -m json.tool state/campaign_position.json > /dev/null 2>&1; then
    echo "✅ state/campaign_position.json valid."
else
    echo "❌ Campaign position JSON error!"
    exit 1
fi
echo ""

## 4. Check story module completeness
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "📋 STEP 4: Checking story module completeness..."
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
MODULE_COUNT=$(find modules -type f -name "*.md" | wc -l)
echo "🗂  Found $MODULE_COUNT module files."
if [ "$MODULE_COUNT" -lt 5 ]; then
    echo "⚠️  Module count is below recommended minimum (5+)"
else
    echo "✅ Module count looks good."
fi
echo ""

## 5. Show session trigger commands
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "📋 STEP 5: Session trigger commands"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "🪶 Begin session with:"
echo ""
echo "   ZONE-IN: Helgen"
echo "   ZONE-IN: Whiterun"
echo "   ZONE-IN: Jorrvaskr"
echo "   ZONE-IN: Windhelm"
echo "   ZONE-IN: Solitude"
echo ""
echo "See /modules/locations/ for detailed location guides."
echo ""

## 6. Show available tools
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "📋 STEP 6: GM Automation Tools"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "Available tools:"
echo "  • python scripts/session_stamp.py      - Create timestamped session log"
echo "  • python scripts/dragonbreak_cue.py    - Check Dragonbreak eligibility"
echo "  • python scripts/first_run.py          - First-time onboarding"
echo "  • python scripts/custom_scan.py        - Scan for banned terms"
echo "  • python scripts/validate_state.py     - Validate state files"
echo ""
echo "To set up bash aliases, run:"
echo "  bash scripts/setup_aliases.sh"
echo ""

## 7. Show GitHub Copilot Instructions reference
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "📋 STEP 7: GitHub Copilot Instructions"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "View Copilot instructions with:"
echo "  cat .github/copilot-instructions.md | less"
echo ""

echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "✅ Skyrim Fate Vault setup confirmed."
echo "   May your legends echo across Sovngarde."
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

#!/bin/bash
# setup_aliases.sh
# Sets up convenient bash aliases for Skyrim Fate Core Vault

echo "🛠️  Setting up Skyrim Fate Core Vault aliases..."

# Define aliases
ALIASES="
# Skyrim Fate Core Vault Aliases
alias dragonbreak='grep -r \"Dragonbreak\" /home/runner/work/Tamriel-Skyrim-Repos/Tamriel-Skyrim-Repos/modules/'
alias clocks='cat /home/runner/work/Tamriel-Skyrim-Repos/Tamriel-Skyrim-Repos/clocks/skyrim_clocks.json'
alias state='cat /home/runner/work/Tamriel-Skyrim-Repos/Tamriel-Skyrim-Repos/state/campaign_state.json'
alias party='cat /home/runner/work/Tamriel-Skyrim-Repos/Tamriel-Skyrim-Repos/state/party_state.json'
alias quests='cat /home/runner/work/Tamriel-Skyrim-Repos/Tamriel-Skyrim-Repos/state/quest_flags.json'
alias newsession='python3 /home/runner/work/Tamriel-Skyrim-Repos/Tamriel-Skyrim-Repos/scripts/session_stamp.py'
alias checkdragonbreak='python3 /home/runner/work/Tamriel-Skyrim-Repos/Tamriel-Skyrim-Repos/scripts/dragonbreak_cue.py'
alias vaultscan='python3 /home/runner/work/Tamriel-Skyrim-Repos/Tamriel-Skyrim-Repos/scripts/custom_scan.py'
alias vaultvalidate='python3 /home/runner/work/Tamriel-Skyrim-Repos/Tamriel-Skyrim-Repos/scripts/validate_state.py'
"

# Append to .bashrc if not already present
if ! grep -q "Skyrim Fate Core Vault Aliases" ~/.bashrc; then
    echo "$ALIASES" >> ~/.bashrc
    echo "✅ Aliases added to ~/.bashrc"
else
    echo "⚠️  Aliases already exist in ~/.bashrc"
fi

echo ""
echo "Available aliases:"
echo "  dragonbreak       - Search for Dragonbreak references"
echo "  clocks            - View campaign clocks"
echo "  state             - View campaign state"
echo "  party             - View party state"
echo "  quests            - View quest flags"
echo "  newsession        - Create new session log"
echo "  checkdragonbreak  - Check Dragonbreak eligibility"
echo "  vaultscan         - Scan for banned terms"
echo "  vaultvalidate     - Validate state files"
echo ""
echo "To activate aliases in current session, run:"
echo "  source ~/.bashrc"
echo ""
echo "✅ Alias setup complete!"

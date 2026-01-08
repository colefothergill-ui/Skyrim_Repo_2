"""
first_run.py
Terminal intro for new GMs or devs.

Usage:
  python scripts/first_run.py

Behavior:
- Provides an interactive onboarding experience
- Guides new users through the repository structure
- Suggests next steps and key files to review
"""

import sys

INTERACTIVE = sys.stdin.isatty()

def pause(prompt: str):
    if INTERACTIVE:
        input(prompt)
    else:
        print(f"[skip] {prompt}")

try:
    sys.stdout.reconfigure(errors="replace")
    sys.stderr.reconfigure(errors="replace")
except Exception:
    pass
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def print_banner():
    """Print welcome banner."""
    banner = """
--------------------------------------------------------------------- - 
-                                                                   -
-          SKYRIM FATE CORE CAMPAIGN VAULT - FIRST RUN              -
-                                                                   -
-                    Welcome to 4E 201 Tamriel                      -
-                                                                   -
---------------------------------------------------------------------
"""
    print(banner)


def print_section(title: str, content: str):
    """Print a formatted section."""
    print()
    print("" * 70)
    print(f"  {title}")
    print("" * 70)
    print(content)


def check_file_exists(file_path: Path) -> str:
    """Return a status indicator for file existence."""
    return "" if file_path.exists() else ""


def show_repository_structure():
    """Display the repository structure with status checks."""
    structure = f"""
Key directories and their purpose:

  {check_file_exists(ROOT / 'clocks')} /clocks/           Progress clocks (master, act, faction)
  {check_file_exists(ROOT / 'state')} /state/            Campaign state and flags
  {check_file_exists(ROOT / 'modules')} /modules/          Act modules and narrative frameworks
  {check_file_exists(ROOT / 'factions')} /factions/         Faction packs
  {check_file_exists(ROOT / 'npcs')} /npcs/             Named NPCs with aspects and stunts
  {check_file_exists(ROOT / 'pcs')} /pcs/              Player character sheets
  {check_file_exists(ROOT / 'hooks')} /hooks/            Story hooks organized by act/faction
  {check_file_exists(ROOT / 'logs')} /logs/             Session logs
  {check_file_exists(ROOT / 'rules')} /rules/            Fate Core mechanics and quickrefs
  {check_file_exists(ROOT / 'scripts')} /scripts/          Automation and validation tools
"""
    print_section(" REPOSITORY STRUCTURE", structure)


def show_quick_start():
    """Display quick start guide."""
    guide = """
1. Read the campaign premise:
    cat MASTER_KEY.md

2. Review the repository index:
    cat INDEX.md

3. Check current campaign state:
    cat state/campaign_state.json
    cat clocks/skyrim_clocks.json

4. Review the Five Acts structure:
    ls modules/acts/

5. Explore available hooks:
    cat hooks/HOOK_BANK.md

6. Create your first session log:
    python scripts/session_stamp.py
"""
    print_section(" QUICK START GUIDE", guide)


def show_gm_tools():
    """Display available GM tools."""
    tools = """
Automation scripts in /scripts/:

   session_stamp.py       Create timestamped session logs
   dragonbreak_cue.py     Check for Dragonbreak moment eligibility
   custom_scan.py         Validate repository for banned terms
   validate_state.py      Validate state files
   build_context.py       Build context for AI tools

Validation:
   python scripts/custom_scan.py
   python scripts/validate_state.py
"""
    print_section("  GM AUTOMATION TOOLS", tools)


def show_workflow():
    """Display session workflow."""
    workflow = """
After each session:

  1. Update session log in /logs/
  2. Tick relevant clocks in /clocks/skyrim_clocks.json
  3. Update campaign state in /state/campaign_state.json
  4. Update NPC relationship clocks if needed
  5. Review /hooks/ for triggered complications

Before next session:

  1. Check for Dragonbreak moment eligibility:
      python scripts/dragonbreak_cue.py

  2. Review current state and clocks
  3. Prepare hooks and complications
"""
    print_section(" SESSION WORKFLOW", workflow)


def show_key_concepts():
    """Display key campaign concepts."""
    concepts = """
 The Dragonborn is absent  your PCs are the heroes
 Civil war between Stormcloaks and Imperials is active
 Thalmor endgame lurks beneath the surface conflict
 Dragonbreak moments are rare mythic threads (not mandatory)
 Progress is tracked through Fate Core clocks
 Gritty tone: war has costs, diplomacy matters

Era: 4E 201 (Fourth Era, Year 201)
Location: Skyrim, Province of Tamriel
System: Fate Core by Evil Hat Productions
"""
    print_section(" KEY CAMPAIGN CONCEPTS", concepts)


def show_next_steps():
    """Display suggested next steps."""
    next_steps = """
Choose your path:

  [1] I'm a new GM starting a campaign
       Read MASTER_KEY.md and README.md
       Review modules/acts/ for the Five Acts structure
       Set up initial state in /state/ files

  [2] I'm joining an existing campaign
       Review current /state/campaign_state.json
       Check /clocks/skyrim_clocks.json for progress
       Read recent session logs in /logs/

  [3] I'm a developer working on the vault
       Review .github/copilot-instructions.md
       Run validation: python scripts/custom_scan.py
       Check scripts/ for automation tools

  [4] I want to explore the lore
       Review /modules/ for act frameworks
       Check /factions/ for faction details
       Browse /npcs/ for character sheets
"""
    print_section(" NEXT STEPS", next_steps)


def main():
    """Run the first-run onboarding experience."""
    print_banner()

    print()
    print("This is your first-run guide for the Skyrim Fate Core Campaign Vault.")
    print()
    pause("Press Enter to continue...")

    show_repository_structure()
    pause("\nPress Enter to continue...")

    show_key_concepts()
    pause("\nPress Enter to continue...")

    show_quick_start()
    pause("\nPress Enter to continue...")

    show_gm_tools()
    pause("\nPress Enter to continue...")

    show_workflow()
    pause("\nPress Enter to continue...")

    show_next_steps()

    print()
    print("-" * 70)
    print("  May your legends echo across Sovngarde.")
    print("-" * 70)
    print()


if __name__ == "__main__":
    main()

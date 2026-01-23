"""
character_progression.py
Track character milestones and progression.

Usage:
  python scripts/character_progression.py --character PC_MAIN.md
  python scripts/character_progression.py --milestone minor
  python scripts/character_progression.py --milestone significant
  python scripts/character_progression.py --milestone major
"""

from __future__ import annotations

import sys
try:
    sys.stdout.reconfigure(errors="replace")
    sys.stderr.reconfigure(errors="replace")
except Exception:
    pass

import argparse
from pathlib import Path
from datetime import datetime

ROOT = Path(__file__).resolve().parents[1]
PCS_DIR = ROOT / "pcs"

MILESTONE_INFO = {
    "minor": {
        "name": "Minor Milestone",
        "frequency": "End of session",
        "changes": [
            "Switch values of any two skills (or a skill rated at +1 with an unrated skill)",
            "Replace one stunt with another stunt",
            "Rewrite one aspect (except High Concept)",
            "Rename or rewrite a moderate consequence if it's been in play for one session"
        ]
    },
    "significant": {
        "name": "Significant Milestone",
        "frequency": "Every 2-3 sessions (or end of a scenario)",
        "changes": [
            "All benefits of a minor milestone",
            "Raise one skill by one step (respecting skill pyramid/column)",
            "Add a new stunt (or trade one if at refresh limit)",
            "Rename or rewrite a severe consequence if it's been in play for one session"
        ]
    },
    "major": {
        "name": "Major Milestone",
        "frequency": "End of arc or act (every 4-6 sessions)",
        "changes": [
            "All benefits of a significant milestone",
            "Gain +1 refresh (potentially spending on a new extra or stunt)",
            "Rewrite your High Concept (if major character change occurred)",
            "Rewrite any other aspect",
            "Raise one skill above +4 to +5 (Legendary, if GM allows)"
        ]
    }
}

def print_milestone_info(milestone_type: str):
    """Print information about a milestone type"""
    info = MILESTONE_INFO.get(milestone_type)
    if not info:
        print(f"Unknown milestone type: {milestone_type}")
        return
    
    print("=" * 70)
    print(f"{info['name'].upper()}")
    print("=" * 70)
    print(f"\nFrequency: {info['frequency']}\n")
    print("What You Can Change:")
    for i, change in enumerate(info['changes'], 1):
        print(f"  {i}. {change}")
    print()
    print("=" * 70)

def suggest_milestone():
    """Suggest appropriate milestone based on campaign state"""
    print("\n## Milestone Suggestion Tool\n")
    print("Answer these questions to determine appropriate milestone:\n")
    
    # Question 1: Session count
    print("1. How many sessions since the last milestone?")
    print("   a) 1 session")
    print("   b) 2-3 sessions")
    print("   c) 4+ sessions or end of major arc")
    answer1 = input("\nAnswer (a/b/c): ").strip().lower()
    
    # Question 2: Story significance
    print("\n2. What was accomplished?")
    print("   a) Minor goals, skill practice, small victories")
    print("   b) Completed scenario, major side quest, significant faction advancement")
    print("   c) Act completed, major plot resolution, character transformation")
    answer2 = input("\nAnswer (a/b/c): ").strip().lower()
    
    # Question 3: Character change
    print("\n3. Has the PC fundamentally changed?")
    print("   a) No major changes, still the same character")
    print("   b) Notable growth or shift in capabilities")
    print("   c) Major transformation or identity shift")
    answer3 = input("\nAnswer (a/b/c): ").strip().lower()
    
    # Determine milestone
    print("\n" + "=" * 70)
    
    if answer1 == 'a' and answer2 == 'a':
        print("RECOMMENDATION: Minor Milestone")
        print_milestone_info("minor")
    elif answer1 == 'c' or answer2 == 'c' or answer3 == 'c':
        print("RECOMMENDATION: Major Milestone")
        print_milestone_info("major")
    else:
        print("RECOMMENDATION: Significant Milestone")
        print_milestone_info("significant")

def log_milestone(character_file: str, milestone_type: str):
    """Log a milestone to the character file"""
    char_path = PCS_DIR / character_file
    
    if not char_path.exists():
        print(f"Error: Character file not found: {char_path}")
        return
    
    timestamp = datetime.now().strftime("%Y-%m-%d")
    info = MILESTONE_INFO.get(milestone_type)
    
    if not info:
        print(f"Unknown milestone type: {milestone_type}")
        return
    
    print(f"\nLogging {info['name']} for {character_file}...")
    print("\nWhat changed?")
    print(f"Options for {info['name']}:")
    for i, change in enumerate(info['changes'], 1):
        print(f"  {i}. {change}")
    
    change_description = input("\nDescribe the change(s) made: ").strip()
    
    # Create milestone entry
    milestone_entry = f"\n### Milestone: {timestamp} - {info['name']}\n"
    milestone_entry += f"**Changes**: {change_description}\n"
    
    print("\n" + "=" * 70)
    print("Milestone Entry Created:")
    print(milestone_entry)
    print("=" * 70)
    print("\nAdd this to the 'Milestone History' section in your character sheet.")
    print(f"File: {char_path}")

def main():
    parser = argparse.ArgumentParser(description="Character progression and milestone tracker")
    parser.add_argument("--character", "-c", help="Character sheet file name (e.g., PC_MAIN.md)")
    parser.add_argument("--milestone", "-m", choices=["minor", "significant", "major"], 
                       help="Log a specific milestone type")
    parser.add_argument("--suggest", "-s", action="store_true", 
                       help="Get milestone suggestion based on campaign progress")
    parser.add_argument("--info", "-i", choices=["minor", "significant", "major"],
                       help="Display information about a milestone type")
    
    args = parser.parse_args()
    
    if args.suggest:
        suggest_milestone()
    elif args.info:
        print_milestone_info(args.info)
    elif args.milestone and args.character:
        log_milestone(args.character, args.milestone)
    elif args.milestone:
        print_milestone_info(args.milestone)
        print("\nTo log this milestone, add: --character FILENAME.md")
    else:
        print("Character Progression Tracker")
        print("=" * 70)
        print("\nUsage:")
        print("  --suggest              Get milestone recommendation")
        print("  --info [type]          Show milestone information")
        print("  --milestone [type]     Show milestone info")
        print("  --character [file]     With --milestone, log to character file")
        print("\nExamples:")
        print("  python scripts/character_progression.py --suggest")
        print("  python scripts/character_progression.py --info significant")
        print("  python scripts/character_progression.py --milestone major --character PC_MAIN.md")

if __name__ == "__main__":
    main()

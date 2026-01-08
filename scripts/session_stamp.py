"""
session_stamp.py
Auto-names session logs with timestamp.

Usage:
  python scripts/session_stamp.py

Behavior:
- Creates a new session log file in /logs/ with current timestamp
- Uses the session template as a base
- Returns the filename for easy opening
"""

import sys
from pathlib import Path
from datetime import datetime

ROOT = Path(__file__).resolve().parent.parent
LOGS_DIR = ROOT / "logs"
TEMPLATE_FILE = LOGS_DIR / "session_TEMPLATE.md"


def create_session_log() -> Path:
    """Create a new timestamped session log from template."""
    if not TEMPLATE_FILE.exists():
        print(f"Error: Template file not found at {TEMPLATE_FILE}")
        sys.exit(1)

    # Generate timestamp filename
    timestamp = datetime.now().strftime("%Y-%m-%d_%H%M")
    session_file = LOGS_DIR / f"session_{timestamp}.md"

    # Check if file already exists
    if session_file.exists():
        print(f"Session log already exists: {session_file}")
        return session_file

    # Copy template to new session file
    with TEMPLATE_FILE.open("r", encoding="utf-8") as template:
        content = template.read()

    # Replace template placeholders with current date
    current_date = datetime.now().strftime("%Y-%m-%d")
    content = content.replace("[DATE]", current_date)
    content = content.replace("[SESSION_NUMBER]", "TBD")

    with session_file.open("w", encoding="utf-8") as new_session:
        new_session.write(content)

    print(f"✅ Created new session log: {session_file.name}")
    print(f"Full path: {session_file}")

    return session_file


def main() -> None:
    print("=" * 70)
    print("Session Log Stamp")
    print("=" * 70)
    print()

    session_file = create_session_log()

    print()
    print("Next steps:")
    print(f"  1. Open: {session_file}")
    print("  2. Update session number and fill in session details")
    print("  3. After session, update /clocks/ and /state/ files")
    print()
    print("=" * 70)


if __name__ == "__main__":
    main()

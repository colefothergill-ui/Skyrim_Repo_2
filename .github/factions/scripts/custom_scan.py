"""
custom_scan.py
Scan repository for banned terms.

Usage:
  python scripts/custom_scan.py

Behavior:
- Scans markdown files and JSON files for banned terms.
- Exits non-zero if any violations are found.
- Does not modify any repository files (read-only).
"""

import sys
from pathlib import Path
from typing import List, Tuple

ROOT = Path(__file__).resolve().parent.parent

# Banned terms that should not appear in the campaign vault
BANNED_TERMS = [
    "WoW",
    "World of Warcraft",
    "BFA",
    "Battle for Azeroth",
    "Azeroth",
    "Suroe Dragonseal",
    "Suroe",
    "sin'dorei",
    "Kaldorei",
    "blood elf",
    "night elf",
    "Dracon'Thor'reth",
]

# File patterns to scan
SCAN_PATTERNS = [
    "**/*.md",
    "**/*.json",
]

# Directories to exclude from scanning
EXCLUDE_DIRS = [
    ".git",
    ".github",
    "node_modules",
    "__pycache__",
]


def should_scan_file(file_path: Path) -> bool:
    """Return True if the file should be scanned for banned terms."""
    for exclude_dir in EXCLUDE_DIRS:
        if exclude_dir in file_path.parts:
            return False

    # Skip the copilot-instructions.md as it's allowed to reference banned terms
    if file_path.name == "copilot-instructions.md":
        return False

    # Skip this script itself
    if file_path.name == "custom_scan.py":
        return False

    return True


def scan_file_for_banned_terms(file_path: Path) -> List[Tuple[int, str, str]]:
    """Return a list of (line_number, term, line_content) for banned-term hits."""
    violations: List[Tuple[int, str, str]] = []

    try:
        with file_path.open("r", encoding="utf-8") as f:
            for line_num, line in enumerate(f, start=1):
                lower = line.lower()
                for term in BANNED_TERMS:
                    if term.lower() in lower:
                        violations.append((line_num, term, line.strip()))
    except (UnicodeDecodeError, PermissionError):
        # Skip binary files or files we can't read
        pass

    return violations


def scan_repository() -> List[Tuple[Path, int, str, str]]:
    """Scan the repository and return (relative_path, line_number, term, line_content) tuples."""
    all_violations: List[Tuple[Path, int, str, str]] = []

    for pattern in SCAN_PATTERNS:
        for file_path in ROOT.glob(pattern):
            if not file_path.is_file():
                continue
            if not should_scan_file(file_path):
                continue

            for line_num, term, line_content in scan_file_for_banned_terms(file_path):
                relative_path = file_path.relative_to(ROOT)
                all_violations.append((relative_path, line_num, term, line_content))

    return all_violations


def main() -> None:
    print("=" * 70)
    print("Campaign Vault Custom Scan")
    print("=" * 70)
    print()

    print("Scanning for banned terms...")
    violations = scan_repository()

    if violations:
        print(f"\nFOUND {len(violations)} VIOLATIONS:\n")

        violations_by_file = {}
        for file_path, line_num, term, line_content in violations:
            violations_by_file.setdefault(file_path, []).append((line_num, term, line_content))

        for file_path in sorted(violations_by_file.keys()):
            print(f"\n{file_path}:")
            for line_num, term, line_content in violations_by_file[file_path]:
                print(f"  Line {line_num}: Found '{term}'")
                preview = line_content[:80] + "..." if len(line_content) > 80 else line_content
                print(f"    {preview}")

        print("\n" + "=" * 70)
        print("VALIDATION FAILED: Banned terms found in repository")
        print("=" * 70)
        sys.exit(1)

    print("No banned terms found")
    print("\n" + "=" * 70)
    print("VALIDATION PASSED: Repository is clean")
    print("=" * 70)


if __name__ == "__main__":
    main()

"""
npc_lookup.py
Context-aware NPC lookup system.

Find NPCs by:
- Location/Hold
- Scene/Act
- Faction
- Name search

Usage:
  python scripts/npc_lookup.py --location "Whiterun"
  python scripts/npc_lookup.py --hold "The Reach"
  python scripts/npc_lookup.py --faction "imperials"
  python scripts/npc_lookup.py --search "Hadvar"
  python scripts/npc_lookup.py --scene "Battle of Whiterun" --act 1
"""

from __future__ import annotations

import sys
try:
    sys.stdout.reconfigure(errors="replace")
    sys.stderr.reconfigure(errors="replace")
except Exception:
    pass

import json
import argparse
from pathlib import Path
from typing import List, Dict, Any

ROOT = Path(__file__).resolve().parents[1]
NPCS_DIR = ROOT / "npcs"
STATE_DIR = ROOT / "state"

# NPC location/faction mappings
NPC_LOCATIONS = {
    "Whiterun": [
        "npcs/companions/HADVAR_OF_SOLITUDE.md",
        "npcs/companions/LYDIA_OF_WHITERUN.md",
    ],
    "Solitude": [
        "npcs/companions/HADVAR_OF_SOLITUDE.md",
    ],
    "Riverwood": [
        "npcs/companions/RALOF_OF_RIVERWOOD.md",
    ],
    "Winterhold": [
        "npcs/companions/JZARGO.md",
    ],
    "The Reach": [
        # Markarth NPCs would go here
    ],
    "Jorrvaskr": [
        "npcs/companions/AELA_THE_HUNTRESS.md",
    ],
}

NPC_FACTIONS = {
    "imperials": [
        "npcs/companions/HADVAR_OF_SOLITUDE.md",
        "npcs/companions/LYDIA_OF_WHITERUN.md",
    ],
    "stormcloaks": [
        "npcs/companions/RALOF_OF_RIVERWOOD.md",
    ],
    "companions": [
        "npcs/companions/AELA_THE_HUNTRESS.md",
    ],
    "college_of_winterhold": [
        "npcs/companions/JZARGO.md",
    ],
}

def load_npc_file(path: Path) -> Dict[str, Any]:
    """Load and parse NPC markdown file"""
    if not path.exists():
        return {}
    
    try:
        content = path.read_text(encoding='utf-8')
        # Extract basic info from markdown
        npc_data = {
            "file": str(path.relative_to(ROOT)),
            "name": path.stem.replace('_', ' ').title(),
            "content": content[:500],  # First 500 chars
        }
        
        # Try to extract key aspects from content
        for line in content.split('\n'):
            if 'High Concept' in line:
                npc_data['high_concept'] = line.split(':', 1)[-1].strip()
            elif 'Trouble' in line:
                npc_data['trouble'] = line.split(':', 1)[-1].strip()
        
        return npc_data
    except Exception as e:
        return {"file": str(path), "error": str(e)}

def find_npcs_by_location(location: str) -> List[str]:
    """Find NPCs present at a location"""
    location_lower = location.lower()
    results = []
    
    for loc, npcs in NPC_LOCATIONS.items():
        if location_lower in loc.lower():
            results.extend(npcs)
    
    return list(set(results))  # Remove duplicates

def find_npcs_by_faction(faction: str) -> List[str]:
    """Find NPCs belonging to a faction"""
    faction_lower = faction.lower()
    results = []
    
    for fac, npcs in NPC_FACTIONS.items():
        if faction_lower in fac.lower():
            results.extend(npcs)
    
    return list(set(results))

def search_npcs_by_name(name: str) -> List[Path]:
    """Search for NPCs by name"""
    name_lower = name.lower()
    results = []
    
    if NPCS_DIR.exists():
        for npc_file in NPCS_DIR.rglob("*.md"):
            if "TEMPLATE" in npc_file.name.upper():
                continue
            if name_lower in npc_file.stem.lower():
                results.append(npc_file)
    
    return results

def get_current_location_npcs() -> List[str]:
    """Get NPCs for current campaign location"""
    campaign_state = STATE_DIR / "campaign_state.json"
    campaign_pos = STATE_DIR / "campaign_position.json"
    
    location = None
    
    # Try to get location from campaign files
    if campaign_pos.exists():
        try:
            pos = json.loads(campaign_pos.read_text(encoding='utf-8'))
            location = pos.get('current_location')
        except Exception:
            pass
    
    if not location and campaign_state.exists():
        try:
            state = json.loads(campaign_state.read_text(encoding='utf-8'))
            location = state.get('current_location')
        except Exception:
            pass
    
    if location:
        # Extract hold name from location string
        for hold in NPC_LOCATIONS.keys():
            if hold.lower() in location.lower():
                return NPC_LOCATIONS[hold]
    
    return []

def main():
    parser = argparse.ArgumentParser(description="Look up NPCs by location, faction, or name")
    parser.add_argument("--location", "-l", help="Find NPCs at a location/hold")
    parser.add_argument("--faction", "-f", help="Find NPCs in a faction")
    parser.add_argument("--search", "-s", help="Search NPCs by name")
    parser.add_argument("--current", "-c", action="store_true", help="Find NPCs at current location")
    parser.add_argument("--detailed", "-d", action="store_true", help="Show detailed NPC info")
    
    args = parser.parse_args()
    
    results = []
    
    if args.current:
        print("Finding NPCs at current campaign location...")
        results = get_current_location_npcs()
    elif args.location:
        results = find_npcs_by_location(args.location)
    elif args.faction:
        results = find_npcs_by_faction(args.faction)
    elif args.search:
        search_results = search_npcs_by_name(args.search)
        results = [str(p.relative_to(ROOT)) for p in search_results]
    else:
        parser.print_help()
        return
    
    if not results:
        print("No NPCs found matching criteria.")
        return
    
    print(f"\nFound {len(results)} NPC(s):\n")
    print("=" * 70)
    
    for npc_path in results:
        full_path = ROOT / npc_path
        if args.detailed:
            npc_data = load_npc_file(full_path)
            print(f"\n📋 {npc_data.get('name', npc_path)}")
            print(f"   File: {npc_data.get('file', npc_path)}")
            if 'high_concept' in npc_data:
                print(f"   High Concept: {npc_data['high_concept']}")
            if 'trouble' in npc_data:
                print(f"   Trouble: {npc_data['trouble']}")
        else:
            print(f"- {npc_path}")
    
    print("\n" + "=" * 70)
    print(f"\nUse --detailed flag for more information about each NPC.")

if __name__ == "__main__":
    main()

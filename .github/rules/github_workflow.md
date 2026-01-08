# GitHub Workflow (mobile-friendly)

This repo is your campaign brain: searchable, versioned, hard to accidentally overwrite.

## Where things go
- `/MASTER_KEY.md` → GM rules, tone, commands, operating system
- `/modules/` → Act modules + turning points
- `/npcs/` → NPC dossiers (aspects/stunts/relationship notes)
- `/factions/` → faction packs + side plots
- `/story_branches/` → alternate outcomes + secret “Elder Scrolls Moment” triggers
- `/clocks/skyrim_clocks.json` → single source of truth for clock values
- `/state/campaign_state.json` → hold control + flags + party alignment
- `/state/campaign_position.json` → “where we are right now” pointer for fast recall
- `/logs/` → session logs + Save Game chronicles
- `/hooks/` → hook bank (including secret Dragonbreak seeds)
- `/tools/` → generated context packs / quick-reference outputs

## After a session (3 steps)
1) Add a log:
   Create: `/logs/YYYY-MM-DD_session-##_TITLE.md`
   Copy from: `/logs/session_TEMPLATE.md`

2) Update clocks:
   Edit: `/clocks/skyrim_clocks.json`
   Change only the numbers that moved.

3) Update campaign state:
   Edit: `/state/campaign_state.json`
   Update holds, flags, party alignment, allies/enemies.

Commit message examples:
- `Session 01 recap + clocks update`
- `Act I branch: Whiterun decided`
- `Add faction arc stub: Side Plot C`

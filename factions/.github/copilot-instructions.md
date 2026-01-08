# Copilot Instructions — Tamriel / Skyrim Fate Core Campaign Vault

You are working in a campaign-vault repository. DO NOT restructure the folder tree.
DO NOT delete or overwrite unrelated files. Only touch files explicitly listed in the task.

## Default campaign start (IMPORTANT)
When asked to implement "start fresh" or "start where the module begins":
- The default start point is **ACT 1 — The Battle of Whiterun**
- The start scene is **Session Zero character creation at the siege start**
- Source of truth: `state/startup_defaults.json`

## Session Zero Gate (Mandatory)
Before play proceeds, ensure the repo contains:
- `state/pc_profile.json` with `created=false` until Session Zero is completed
- `pcs/PC_MAIN.md` (active PC sheet)
- `state/active_pc.json` pointing to `pcs/PC_MAIN.md`

Session Zero must capture:
- PC name, aspects, skills/approaches, at least 1 stunt
- **Primary affiliation** (Stormcloaks, Imperials, Companions, Thieves Guild, etc.)
- Starting role at the Battle of Whiterun

## Dragonbreak moments (Act-aware)
- Use `story_branches/DRAGONBREAK_MOMENTS.json` to define module-scene keyed Dragonbreak/Secret Turn moments.
- Scripts should consult `state/campaign_position.json.current_act` + `current_scene_id`.

## On-Track enforcement
Provide a way to verify alignment with the module rails:
- `python scripts/on_track.py` should report PASS/FAIL and recommend exact file edits to re-align.

## Hard rules
- Keep /fate-core/ and /rules/ content intact unless explicitly told to change it.
- Avoid hallucinating details from the PDFs. If you can’t confirm from the PDF text, add TODO markers.
- JSON must remain valid and stable keys should not be renamed unless requested.

## Output style
- Markdown with clear headings and bullet points for mechanics.
- Fate Core mechanics: aspects, compels, stunts, extras, clocks.

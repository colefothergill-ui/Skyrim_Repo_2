# GitHub Workflow (no-code, copy/paste friendly)

This is the **minimal** way to keep your campaign “brain” safe, searchable, and versioned.

## Where things go
- **/MASTER_KEY.md** → your GM rules, tone, commands, and campaign operating system
- **/modules/** → campaign module text (Part 1/2/3)
- **/npcs/** → NPC dossiers
- **/clocks/bfa_clocks.json** → *single source of truth* for clock numbers (no drifting)
- **/logs/** → session logs + Save Game recaps

## After a session (3 steps)
### 1) Add a new log file
Create: `/logs/2025-12-24_session-01_TITLE.md`

Paste this template at top:
```md
# Session 01 — TITLE
Date: 2025-12-24
PC: NAME
Location: WHERE WE STARTED

## Highlights (chronicle)
(Paste your Save Game recap here.)

## Scene Aspects created
- ...

## Mechanical changes
- Fate Points: start __ / end __
- New Aspects/Stunts/Extras:
  - ...
- Consequences/Stress notes:
  - ...

## Threads to pull next time
- ...
```

### 2) Update clocks
Edit: `/clocks/bfa_clocks.json`  
Change only the numbers that moved.

### 3) Commit (GitHub web UI)
Use a commit message like:
- `Session 01 recap + clocks update`
- `Add NPC dossier: Rommath + trust clock`

## “Magic words” you can use in chat (campaign commands)
These are **prompts**, not code.

- `GITHUB.SYNC` → “GM: read the latest MASTER_KEY + newest /logs/ file + clocks JSON before continuing.”
- `SAVE GAME` → “GM: write a 700–1200 word in-world chronicle recap. Then output a copy/paste-ready `/logs/...` filename line.”
- `UPDATE CLOCKS` → “GM: list clock diffs and output a copy/paste-ready JSON snippet for clocks.”

Tip: At the end of each command response, the GM should print:
- `FILE TO SAVE:` `/logs/...`
- `CLOCKS PATCH:` (small JSON fragment)

## Give ChatGPT read-only repo access (deploy key or PAT)
**Important:** The private deploy key is never stored in this repo or in version control. If you can't find it in your secrets manager, create a fresh one with the steps below; never commit a private key.

1. **Generate a deploy key (SSH):**
   - Run: `ssh-keygen -t ed25519 -C "repo-deploy-key" -f ~/.ssh/your-repo-name_deploy_key` (swap `your-repo-name` for your actual repo).
   - Prefer setting a passphrase and loading the key via `ssh-agent` or a secrets manager.
   - Only leave it empty if you fully accept the risk for unattended automation.
   - Keep `bfa_deploy_key` (private) safe and never commit it.
2. **Add the public key to GitHub (read-only):**
   - Repo → Settings → Deploy keys → *Add deploy key*
   - Title: `ChatGPT RO`, Key: contents of `bfa_deploy_key.pub`, **do not** enable write access.
3. **Connect ChatGPT to the repo:**
   - In ChatGPT → *Add data source* → GitHub → choose *SSH key* and paste the **private** key contents of `bfa_deploy_key`.
   - Pasting the private key gives ChatGPT access to that credential; only do this if you trust OpenAI with read access to the repo.
   - Only paste keys into the official ChatGPT interface over HTTPS (verify the browser address bar/certificate).
   - Use only trusted devices/sessions, clear your clipboard afterward, and never share the private key anywhere else.
   - Consider rotating the key after initial setup.
   - Alternative: create a fine-grained PAT (GitHub → Settings → Developer settings → Personal access tokens → Fine-grained) scoped to **Repository contents: Read-only** for this repo, and store it securely.
     - Pick this repository, set expiration, grant only **Contents: Read** and **Metadata: Read**, then copy the token once and paste it into the ChatGPT GitHub data source.
4. **Rotate if compromised:** Remove the old deploy key or PAT in GitHub settings and repeat the steps above with a new key.

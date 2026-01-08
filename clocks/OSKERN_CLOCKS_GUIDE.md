# Clock Guide — Oskern Galeborne Add-ons

This file defines the new clocks introduced for Oskern’s arc and how to run them.
Rule of thumb: tick clocks when the story *irreversibly advances*, not on every minor beat.

---

## How to Tick Clocks (quick policy)
Tick a clock when:
- A session ends with clear consequences.
- A faction learns something important, loses an asset, gains an asset, or commits openly.
- Oskern makes a “point of no return” choice (accepting the Hunt, sparing/turning a foe, performing rites, openly using the Voice).

Do NOT tick for:
- pure travel, minor skirmishes without fallout, or scenes that reset with no lasting change.

---

## New/Updated Clocks and What MAX Means

### 1) Hircine’s Call (Oskern) — Personal (max 6)
**What it tracks:** How deeply Oskern is being shaped/recognized by the Hunt.
**Tick when:**
- Oskern accepts a compel to hunt/kill/perform rites instead of restraint.
- Oskern takes trophies, marks prey, or makes “pack doctrine” choices in public.
- Oskern chooses predation over politics or mercy over practicality (if it serves the Hunt).
**MAX (6/6) means:**
- A direct Hircine escalation: a Trial, a sign, a rival champion, or a “prove it” hunt.
- Reward: unlock a major narrative permission (“Marked of the Hunt”) and a new stunt/upgrade.
- Cost: the Beast pushes harder (more frequent/stronger compels when blood is near).

---

### 2) Beast Mastery (Oskern) — Personal (max 4)
**What it tracks:** Control during/after transformation and battle-frenzy moments.
**Tick when:**
- Oskern transforms and still pursues a chosen objective (doesn’t spiral).
- Oskern resists a frenzy compel at real cost (FP spent, consequence accepted, etc.).
**MAX (4/4) means:**
- The first transformation in a scene no longer requires a control test unless severely provoked.
- Oskern gains permission to lead/command other werewolves (pack dominance).

---

### 3) Unleashed Pup — Personal (max 4)
**What it tracks:** The infected Silver Hand survivor becoming a real ripple in Skyrim.
**Tick when:**
- The infected survivor lives long enough to change.
- They harm others, draw attention, or become “a story” in a hold.
- They seek Oskern / seek revenge / seek a new pack.
**MAX (4/4) means:**
- The “pup” becomes a named NPC with a faction tie (Silver Hand splinter, rogue werewolf, or unwilling pack recruit).
- This triggers a big complication: a werewolf outbreak, an organized purge, or a dramatic confrontation.

---

### 4) Silver Hand Retaliation — Faction/Threat (max 6)
**What it tracks:** Silver Hand mobilization, intelligence, and counter-hunts aimed at Oskern.
**Tick when:**
- Silver Hand cells lose members, find bodies, confirm the “Frost Wolf” identity, or gain silver assets.
- Oskern’s actions become public: witnesses survive, rumors spread, trophy-signatures appear.
**MAX (6/6) means:**
- A major strike: ambush, trap, public exposure attempt, raid on Oskern’s manor, or assault during a war operation.
- The Silver Hand bring specialists (silver nets, poison, trackers, bait).

---

### 5) Stormcloak Trust — Faction (max 4)
**What it tracks:** Your standing with the Sons of Skyrim.
**Tick when:**
- You complete missions that advance Stormcloak control or protect Stormcloak lives/reputation.
- You impress Galmar/Ulfric with results (especially under pressure).
- You make sacrifices for the cause rather than personal gain.
**MAX (4/4) means:**
- Promotion + access: war council audience, formal recognition, and the ability to call in aid 1/session.

---

### 6) Way of the Voice Offshoot — Faction (max 4) (existing clock, now used)
**What it tracks:** Greybeard-adjacent “splinter” attention and your relationship to the discipline.
**Tick when:**
- You seek training/mentorship, protect Voice-lore, or uphold restraint in a meaningful way.
- You use the Thu’um and accept the moral cost (FP spent, consequence taken, vow conflict).
**MAX (4/4) means:**
- Unlock a secret mentor, a rare Word, or a “Voice technique” upgrade (reduced Strain cost once per session).

---

## Story Goal Clocks (recommended)
These are long-arc clocks that turn your ambitions into visible progress.

### A) Path to Hircine’s Champion — Personal (max 6)
Tick when you complete Hunts that matter to Hircine (worthy prey, rival hunters, dangerous trophies, protecting “the Hunt” from corruption).
MAX = Hircine offers the mantle (with a price).

### B) Liberate Falkreath Hold — Political/War (max 6)
Tick when you weaken Siddgeir’s corruption, secure noble support, win battles that matter in Falkreath, or expose Imperial influence.
MAX = Falkreath control flips and/or Siddgeir’s position becomes untenable.

### C) Claim the Jarlship — Political (max 6)
Tick when you gain noble backing, eliminate rivals, earn Ulfric’s endorsement, and establish legitimacy (or force).
MAX = you can credibly take the throne (and must deal with consequences).

{
  "meta": {
    "updated": "2025-12-31",
    "notes": "Single source of truth for campaign clocks. Added Oskern personal/threat/goal clocks."
  },
  "faction_clocks": {
    "stormcloak_trust": {
      "current": 1,
      "max": 4,
      "note": "Oskern standing with the Sons of Skyrim. Ticks on missions/sacrifices for the cause. MAX = promotion + war council access + call-in aid 1/session."
    },
    "silver_hand_retaliation": {
      "current": 1,
      "max": 6,
      "note": "Threat clock for Silver Hand counter-hunts. Ticks as they learn, mobilize, and set traps. MAX = major strike/ambush/raid/exposure attempt."
    },
    "way_of_the_voice_offshoot": {
      "current": 1,
      "max": 4,
      "note": "Custom faction — Greybeards-adjacent splinter. Ticks on voice-lore, restraint, mentorship. MAX = unlock mentor/word/technique upgrade."
    }
  },
  "personal_clocks": {
    "hircines_call_oskern": {
      "current": 2,
      "max": 6,
      "note": "How deeply Oskern is claimed by the Hunt. Ticks on rites, trophies, compels accepted. MAX = Hircine escalation/trial + major upgrade."
    },
    "beast_mastery_oskern": {
      "current": 0,
      "max": 4,
      "note": "Control during/after transformation. Ticks on resisting frenzy and maintaining intent. MAX = first-shift control becomes reliable."
    },
    "unleashed_pup": {
      "current": 1,
      "max": 4,
      "note": "The infected Silver Hand survivor ripple. Ticks as they survive/change/spread. MAX = named NPC + big complication."
    },
    "path_to_hircines_champion": {
      "current": 0,
      "max": 6,
      "note": "Long-arc ambition: become Hircine’s Champion. MAX = mantle offered (with price)."
    },
    "liberate_falkreath_hold": {
      "current": 0,
      "max": 6,
      "note": "Long-arc ambition: free Falkreath from corruption/Imperial leverage. MAX = hold flips / Siddgeir falls."
    },
    "claim_the_jarlship_falkreath": {
      "current": 0,
      "max": 6,
      "note": "Long-arc ambition: take the Jarlship. MAX = you can credibly seize rule and endure fallout."
    }
  }
}

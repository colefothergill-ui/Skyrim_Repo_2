# Hook Bank

These are **drop-in scene starters** you can deploy whenever the table needs momentum.
Each hook is written so it can be “skinned” to the party’s current hold and allies.

## War Hooks

1) **The Whiterun Vote**
   - Balgruuf is being pushed (hard) to pick a side. The PCs are asked to deliver *one* decisive proof: a letter, a prisoner, or a captured Thalmor operative.
   - **Clocks:** tick `act_01_whiterun_outcome` and/or `thalmor_influence` depending on how dirty the proof is.

2) **The Fort Raid That Wasn’t**
   - A Stormcloak/Imperial raid is staged—but the bodies don’t match the uniforms. Someone is manufacturing atrocities to swing holds.
   - **Clocks:** tick `thalmor_influence` on cover-ups; tick `civil_war_endgame` on public fallout.

3) **Jagged Crown Blood Price**
   - The Jagged Crown is “found,” but the site is trapped with an ancient curse. Whoever retrieves it becomes marked (visions, night terrors, bad luck).
   - **Payoff:** a recurring compel-able Aspect on the party until the curse is handled.

4) **The Prisoner Exchange**
   - A prisoner swap is arranged at neutral ground. A third party wants to sabotage it (Silver Hand, Thalmor, bandits, or Forsworn).
   - **Clocks:** tick `civil_war_endgame` if peace is possible; tick `thalmor_influence` if it’s sabotaged.

5) **The Hold That Eats Its Own**
   - A hold’s militia is fracturing: half wants to defect, half wants to burn traitors. The PCs must stabilize it—or pick who gets executed.
   - **Clocks:** tick the relevant faction clock; add a local “CIVIL UNREST” clock if you want consequences to linger.

## Faction Hooks

1) **Silver Hand Counter-Hunt**
   - The Silver Hand tracks the party’s trail, convinced the PCs are hiding werewolves (true or not).
   - **Good for:** Companions ties, Aela involvement, “hunter vs hunted” tension.

2) **Thalmor Audit**
   - A Thalmor “advisor” arrives with paperwork and smiles. They demand access to a hold’s records—or your PC’s “proof.”
   - **Clocks:** tick `thalmor_influence` when the PCs comply, compromise, or kill their way out.

3) **Dark Brotherhood Crossfire**
   - A contract target is in the middle of your war objective (a courier, a negotiator, a priest, a war-scribe). Someone offers double pay to protect them instead.
   - **Branch:** PCs side with coin, conscience, or chaos.

4) **Forsworn Knife in the Door**
   - A Forsworn insider (Kaie or an equivalent) offers intel that could win a battle… but requires freeing a prisoner or burning a symbol of Imperial/Stormcloak rule.
   - **Clocks:** tick a “REACH UPRISING” clock if you run one; otherwise tick `civil_war_endgame`.

5) **College of Winterhold Signal**
   - The College detects a “tear” (time-slip, echo, or prophecy). They need protection during a ritual—or the PCs can steal the result.
   - **Clocks:** great setup for Act III/IV and any Dragonbreak play.

## Secret Hooks — Elder Scrolls Moment

These are **rare**. Use them when the campaign has earned some metaphysical weirdness.

1) **Markarth: The Abandoned House**
   - The “slam + voice” moment. The PCs are lured into a house that *isn’t* a house anymore.
   - **Trigger:** `thalmor_influence >= 3` **or** a Daedric flag has been touched.

2) **The Same Dawn Twice**
   - A day repeats. People remember inconsistently. The PCs notice because of a unique token (a scar, a seal fragment, a strange mark).
   - **Trigger:** a major decision point + one clock about to fill.

3) **Dragonbreak Glimpse**
   - Mid-combat, the scene fractures: the PCs see two outcomes at once. They choose which becomes real (and suffer a cost).
   - **Trigger:** `civil_war_endgame >= 6` **and** `thalmor_influence >= 4`.

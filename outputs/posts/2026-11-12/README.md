# Feedposts november en december 2026

Gemaakt 30 oktober 2026 op verzoek van Lars: "maak van de TV-slides gewoon de social media posts op de juiste datums". Lars kiest daarna zelf welke ook op het TV-scherm komen.

## Wat er al stond

8 Instagram-concepten in Metricool (aangemaakt 27 oktober in een andere sessie, beelden in Drive-map `Instagram posts november 2026`): di 3 nov competitie, vr 6 nov instromen najaarsreeks, di 10 nov kerstborrel, vr 13 nov jeugd, di 17 nov coaches, vr 20 nov kerstreeks, di 24 nov feestje, vr 27 nov voorjaarsreeks. Geen Kids Kamp, niets in december.

## 10 nieuwe posts (deze map)

| Datum | Id | Pijler | Kop |
|---|---|---|---|
| do 5 nov 18:30 | k1_kidskamp_aankondiging | kids kamp | Kids Kamp 21 t/m 23 dec |
| do 19 nov 18:30 | k2_kidskamp_prijs | kids kamp | Drie ochtenden vol padel |
| di 1 dec 18:30 | k3_kidskamp_programma | kids kamp | Elke ochtend een nieuwe slag |
| vr 4 dec 18:30 | w1_winterreeks_start | winterreeks | Doorspelen in de kerstvakantie |
| di 8 dec 18:30 | j1_jeugd_voorjaar | jeugd | Jeugdreeks start 4 januari |
| vr 11 dec 18:30 | k4_kidskamp_nog10dagen | kids kamp | Meld je kind nog aan |
| di 15 dec 18:30 | w2_winterreeks_instromen | winterreeks | Instromen kan nog |
| vr 18 dec 18:30 | k5_kidskamp_maandag | kids kamp | Klaar voor maandag? |
| di 22 dec 18:30 | a1_feestdagen | all court academy | Wij spelen door |
| di 29 dec 18:30 | v1_voorjaarsreeks | voorjaarsreeks | 7 lessen, 4 jan t/m 21 feb |

Kids Kamp komt zo 5 keer voorbij vanaf 5 november (eerst stond hij er nul keer in). In november zijn de kamp-posts op donderdag gezet, tussen de bestaande dinsdag- en vrijdagposts. December volgt het di/vr-ritme van 18:30.

Beeld: zelfde stijl als de oktober- en novemberposts (ACA logo links, Poort Padel rechts, lime label, kop, subregel, knop met "Link in bio"). Foto's uit Drive: `Poort Padel/Kids kamp` (frames), `Openingsdag` en `eerste shoot`. Gemaakt met `scripts/gen_posts.py` + `scripts/posts.json` (headless Chromium), captions in `scripts/captions.json` en `captions.md`.

## Goedkeuren

Postcheck: https://claude.ai/artifact/XXXX (zie workflow-status voor de actuele link). Alle 18 posts op datum, teksten direct aanpasbaar, keuzes in artifact-collectie `postcheck_nov_v1` (per post `status`, `ig`, `fb`, `note`).

## Naar Metricool

De beelden staan niet in de repo (foto's met kinderen horen niet in een publieke repo; `.gitignore` houdt ze buiten). Metricool heeft wel een publieke URL nodig. `scripts/metricool_payloads.json` bevat per post de Instagram- en Facebook-concepten (draft, collab en fototag @poortpadel, alt-tekst), met `<PUBLIC_URL>` als placeholder voor het beeld. Twee routes:

1. Lars zet de 10 jpg's in de Drive-map `Instagram posts november 2026` (zelfde route als 27 oktober), dan maak ik de concepten aan via de Drive-koppeling van Metricool.
2. Lars geeft akkoord om de beelden tijdelijk te hosten (Higgsfield-upload of de repo), dan gaan ze daarvandaan naar Metricool, dat ze naar zijn eigen opslag kopieert.

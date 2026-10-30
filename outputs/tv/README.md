# TV-slides bij Poort Padel

Slides van 1920x1080 voor het scherm bij Poort Padel. Lars levert de set als zip (laatste: `ACA_tv_slides_v4_alle46.zip`, 46 slides plus `slideshow.html` die ze elke 8 seconden wisselt). De originele jpg's staan niet in de repo (te groot), alleen de aangepaste versies.

## Ronde 30 oktober 2026

TV-check (goedkeuren per slide): https://claude.ai/artifact/Gp9DEHMNVWbdKiMJh1WLLq

Keuzes komen in de artifact-collectie `tvcheck_v1`, per slide een document met `status` (`approved`, `changes`, `rejected`), `note` en `updatedAt`. Uitlezen met `ArtifactData action:"list"`.

Acht slides zijn aangepast met info van allcourtacademy.com (gelezen 30 okt 2026):

| Slide | Was | Nu |
|---|---|---|
| 09 | Kerstvakantie-reeks, "inschrijving opent binnenkort" | Winterreeks: 3 lessen, 14 dec t/m 2 jan, groep van 4 |
| 43 | Drie weken, drie lessen, "hou de site in de gaten" | Winterreeks: inschrijving open, later instappen kan |
| 42 | Voorjaarsreeks zonder datums | 7 lessen, 4 jan t/m 21 feb |
| 12 | Dubbel van slide 06 | Jeugd voorjaarsreeks: 7 lessen, 4 jan t/m 20 feb, vanaf 6 jaar |
| 11 | Kids Camp, drie middagen, diploma | Padel Kids Kamp: ma 21 t/m wo 23 dec, 10:00 tot 12:30, 6 t/m 14 jaar |
| 48 | Drie dagen vol padel | Drie ochtenden, 195 euro all-in, 10% familiekorting vanaf 2e kind |
| 49 | Stempelkaart, diploma, shirt | Coaches, pauze met eten en drinken, rackets en ballen aanwezig |
| 10 | l.debruin@allcourtacademy.com | info@allcourtacademy.com |

Open vragen aan Lars staan op de check-pagina bij slides 06, 07, 13, 33, 34 en 35.

## Hoe de aanpassing werkt

Er zijn geen bronbestanden (Canva of Drive) van de slides gevonden. De oude tekst wordt afgedekt met een vlak in de slidekleur `#071321`, met een zachte rand, en de nieuwe tekst wordt in dezelfde stijl opnieuw gezet (Inter Tight 800 voor de kop, Inter voor de rest, lime `#CDEB4B` voor label en knop). Zie `2026-11-slides/scripts/`:

- `edits.json` de nieuwe teksten per slide
- `gen.py` rendert de slides met headless Chromium en ImageMagick (`python3 gen.py <scratchpad> [bestand.jpg ...]`), verwacht de originelen in `<scratchpad>/tvzip/tv/`
- `build_check.py` bouwt de check-pagina

Na akkoord: aangepaste jpg's over de originelen heen in de zip zetten, `slideshow.html` hoeft niet te veranderen (zelfde bestandsnamen). Slides die Lars op Niet gebruiken zet gaan uit de img-lijst in `slideshow.html`.

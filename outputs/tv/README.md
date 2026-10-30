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

## Volgorde van de slideshow (30 oktober, op verzoek van Lars)

Kids Kamp moet vaker en eerder. `slideshow.html` speelt nu een vaste volgorde van 60 slides (8 minuten) in plaats van de bestandsvolgorde: Kids Kamp als eerste en daarna elke zesde slide (elke 48 seconden), afgewisseld met jeugd, lessenreeks en All Court Academy zelf. De drie Kids Kamp slides komen elk 3 tot 4 keer per loop, winterreeks (09) en voorjaarsreeks (42) twee keer. De volgorde staat in `scripts/order.json` en wordt gemaakt door `scripts/order.py`.

Na akkoord: aangepaste jpg's over de originelen heen in de zip zetten, `slideshow.html` hoeft niet te veranderen (zelfde bestandsnamen). Slides die Lars op Niet gebruiken zet gaan uit de img-lijst in `slideshow.html`.

## Ronde 2 (30 oktober, later op de dag)

Lars beoordeelde alle 46 slides op de check-pagina: 22 goed, 15 eruit (05, 06, 10, 15, 22, 23, 24, 25, 26, 28, 30, 32, 40, 49, 50) en 9 aanpassen, allemaal vanwege de foto (zie `2026-11-slides/keuzes-ronde1.json`).

De 9 zijn opnieuw opgebouwd met foto's uit Drive, dus zonder de afdek-truc van ronde 1:

- `Poort Padel/Kids kamp` (38 videoframes 2160x3840) voor 11, 12, 44, 47, 48
- `Openingsdag` (serie Susan, 29 mei) en `eerste shoot` (APA 13 mei) voor 09, 41, 42, 43

Twee sjablonen in `scripts/gen2.py` met `scripts/edits2.json`: `panel` (donker vlak links, twee staande foto's rechts, focuspunt en zoom per foto) en `photo` (brede foto met verloop links, kleinere tekst zodat de foto zichtbaar blijft). Logo als transparante PNG in `scripts/logo_t.png`.

Nieuwe slideshow-volgorde zonder afgekeurde slides: 42 slides, Kids Kamp (11, 48) elke zesde slide, zie `scripts/order.json`. Check-pagina opnieuw bouwen: `python3 build_check.py <scratchpad> && python3 add_order.py <scratchpad>`.

Ronde 2 goedgekeurd door Lars op 8 van de 9. Slide 47 ging na een derde fotopoging op zijn verzoek helemaal eruit.

## Definitieve set (30 oktober, avond)

`ACA_tv_slides_v5_30.zip`: 22 goedgekeurde originelen, 8 nieuwe slides en `slideshow.html` (36 posities, Kids Kamp elke zesde, 4,8 minuten). 16 slides eruit: 05, 06, 10, 15, 22, 23, 24, 25, 26, 28, 30, 32, 40, 47, 49, 50. Bestandsnamen gelijk aan v4. De zip is via de chat aan Lars gegeven en staat niet in de repo (11 MB). Opnieuw maken: originelen uit de v4-zip in `<scratchpad>/tvzip/tv/`, nieuwe uit `2026-11-slides/nieuw/`, afgekeurde nummers staan in `scripts/order.json`.

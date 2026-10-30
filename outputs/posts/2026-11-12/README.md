# Feedposts november 2026 t/m februari 2027

Gemaakt 30 oktober 2026 op verzoek van Lars: "maak van de TV-slides gewoon de social media posts op de juiste datums". Lars kiest daarna zelf welke ook op het TV-scherm komen.

## Wat er al stond

8 Instagram-concepten in Metricool (aangemaakt 27 oktober in een andere sessie, beelden in Drive-map `Instagram posts november 2026`): di 3 nov competitie, vr 6 nov instromen najaarsreeks, di 10 nov kerstborrel, vr 13 nov jeugd, di 17 nov coaches, vr 20 nov kerstreeks, di 24 nov feestje, vr 27 nov voorjaarsreeks. Geen Kids Kamp, niets in december.

## Update 30 oktober, avond

Lars: alle 30 goedgekeurde TV-slides moeten een post worden, op de beste dagen, met tekst voor alle kanalen. Dus:

- 30 posts in deze map (10 campagneposts plus 20 rechtstreeks uit de slides, `slide` in `scripts/posts.json`), plus de 8 bestaande Metricool-concepten = 38 momenten.
- Dagen volgens `docs/doelgroep-en-posttijden.md`: woensdag en vrijdag 18:30, donderdag als derde dag in november en december, LinkedIn 11:00. De 4 Metricool-concepten die op dinsdag stonden zijn verplaatst (3, 10, 17, 24 nov naar 5, 11, 19, 26 nov).
- Volgorde: Kids Kamp 5x vanaf 4 november, winterreeks voor 14 december, feestdagen en voorjaarsreeks rond de jaarwisseling, beginners en reeks in januari, jeugd en community in februari. Volledige lijst in `captions.md` en `scripts/schedule.json`.
- Alleen het ACA-logo op het beeld. Poort Padel krijgt de tag, de collab en de locatie, niet meer het logo rechtsboven (besluit Lars 30 okt). De 8 oudere concepten hebben het logo nog wel.
- Alleen foto's die in de goedgekeurde slides zaten. Voor 01 (teamfoto) is de foto uit de slide zelf gesneden, het origineel staat niet in de Drive-mappen die bereikbaar zijn.
- Renderfout opgelost: de knop viel onderaan weg omdat headless Chromium 80px van het venster afsnoept. Nu wordt 120px hoger gerenderd en op 1080x1350 bijgesneden.

## 10 campagneposts (eerste set)

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

## Drie kanalen, zoals in oktober

Per post staan drie teksten klaar: Instagram (link in bio), Facebook (link in de tekst, zelfde dag 18:30) en LinkedIn (zakelijker register, zelfde dag 11:00). LinkedIn heeft een schakelaar per post, standaard aan bij competitie, kerstborrel, coaches, winterreeks, feestdagen en voorjaarsreeks (8 van de 18), uit bij Kids Kamp, jeugd, feestje en instromen. Fit-label per post: goed, redelijk of zwak. Teksten in `scripts/captions.json` (nieuw), `scripts/existing.json` (de 8 van 27 oktober, nu ook met Facebook en LinkedIn) en `scripts/linkedin.json`.

Voor de 8 bestaande Metricool-concepten kunnen Facebook en LinkedIn het beeld van het Instagram-concept hergebruiken (staat al op static.metricool.com), daar is geen nieuwe hosting voor nodig.

## Goedkeuren

Postcheck: https://claude.ai/artifact/XoUw6TDaZ8JAxpw2hWVkQr. Alle 18 posts op datum, teksten direct aanpasbaar, keuzes in artifact-collectie `postcheck_nov_v1` (per post `status`, `ig`, `fb`, `note`).

## Naar Metricool

De beelden staan niet in de repo (foto's met kinderen horen niet in een publieke repo; `.gitignore` houdt ze buiten). Metricool heeft wel een publieke URL nodig. `scripts/metricool_payloads.json` bevat per post de Instagram- en Facebook-concepten (draft, collab en fototag @poortpadel, alt-tekst), met `<PUBLIC_URL>` als placeholder voor het beeld.

Afgesproken route (30 oktober): de beelden gaan naar Lars zijn Drive, in de nieuwe map `All Court Acadamy/Social media content` (map-id `1RdWCs5ughvWNVEA8VVflR_m-ofO7j0ht`). Vanuit deze cloud-omgeving lukt dat niet automatisch: de Drive-koppeling kan alleen base64 ontvangen (veel te zwaar voor 29 jpg's), de Make-webhook (`hook.eu1.make.com`) wordt door het netwerkbeleid van de omgeving geblokkeerd, en publieke tussenopslag mag niet voor foto's met kinderen. Daarom kreeg Lars via de chat `ACA_social_content_29.zip`: vier maandmappen (`2026-11 november` t/m `2027-02 februari`) met per bestand de postdatum en het post-id in de naam. Lars sleept die vier mappen in `Social media content`.

Daarna, per post: Drive-bestand opzoeken, link beschikbaar maken voor Metricool (Google Drive koppelen in Metricool, of de bestanden op "iedereen met de link" zetten en de downloadlink gebruiken), `<PUBLIC_URL>` vervangen en de concepten aanmaken (IG met collab en fototag, FB, LI waar `li_aan` true is). 29 posts, s34 (King of the court) niet.

## Akkoord van Lars (30 oktober, 's avonds)

35 van de 38 op Goed. Eruit: het instroomconcept van 6 november (uit Metricool verwijderd) en King of the court (22 januari). Aanpassing: Playtomic-post zegt nu "zoek op Poort Padel". Lars zette LinkedIn aan bij de feestjespost. Details in `keuzes-30okt.json`.

In Metricool staan nu als concept (draft): de 7 oorspronkelijke Instagram-posts op hun nieuwe dag, plus Facebook voor alle 7 en LinkedIn voor de 5 met de schakelaar aan (competitie, kerstborrel, coaches, feestje, voorjaarsreeks). Beeld hergebruikt van het Instagram-concept.

Nog niet in Metricool: de 29 goedgekeurde nieuwe posts. Die wachten tot de beelden in de Drive-map `Social media content` staan (zip naar Lars, zie hierboven). Payloads staan klaar in `scripts/metricool_payloads.json`.

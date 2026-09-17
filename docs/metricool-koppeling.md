# Metricool koppeling

Gekoppeld op 15 september 2026. Vervangt de Make-route voor publiceren.

## Wat er staat

| | |
|---|---|
| Merk | All Court Academy |
| Brand id | 6979019 |
| Tijdzone | Europe/Amsterdam |
| Instagram | allcourtacademy |
| Facebook pagina | 1166728269847678 |
| LinkedIn | urn:li:organization:119694021 |

LinkedIn zat er als verrassing bij. Nog niet besloten of we daar iets mee doen.

## Wat de koppeling kan

- Posts inplannen op datum en tijd, Instagram en Facebook tegelijk
- **Concept opslaan** (`draft`), dan staat hij klaar in Metricool en gaat er niets weg
- **Melding in plaats van automatisch** (`autoPublish: false`), dan krijg je een pushbericht op je telefoon en druk je zelf op posten
- Collab-uitnodiging naar @poortpadel meesturen bij een Instagram post
- Eerste reactie meesturen
- Ingeplande posts teruglezen en aanpassen
- Beste posttijden per netwerk ophalen
- Cijfers ophalen per netwerk

Niet beschikbaar op het gratis plan: de goedkeuringsstroom met reviewers (`createScheduledPostForReview`), die vraagt een plan met teambeheer.

Eerdere aanname bijgesteld: ik zei dat Instagram geen concepten toestaat via een koppeling. Dat klopt voor Meta Business Suite, maar Metricool houdt het concept aan zijn eigen kant. Wat Lars wilde kan dus wel, alleen in Metricool in plaats van in Business Suite.

## Openstaand: waar staan de posters

Metricool wil publieke URL's voor beeld, of een gekoppelde Google Drive of Dropbox. De 12 posters staan nu alleen in deze repo. Twee routes:

1. Netlify. Er staat een leeg project klaar (`aca-media`, site id 6af56acb-38f6-485a-b7eb-59256c913f1d, team ldebruinlars). De poster-upload is hier geblokkeerd door de beveiliging omdat het een openbare pagina aanmaakt. Lars moet daar akkoord op geven.
2. Google Drive. Posters in Drive zetten en Drive koppelen binnen Metricool. Let op: de Drive-koppeling hier draait op l.debruin@allcourtacademy.com, Metricool op ldebruinlars@gmail.com. Dan moet in Metricool het werkaccount gekoppeld worden.

## Posttijden uit Metricool zelf

Opgehaald op 15 september 2026, per uur en per dag. Hoogste waarde is het beste moment.

| Dag | Piek | Waarde | Tweede piek |
|---|---|---|---|
| maandag | 10:00 | 5528 | 18:00 (4206) |
| dinsdag | 10:00 | 4942 | 18:00 (4788) |
| woensdag | 10:00 | 6506 | 18:00 (4869) |
| donderdag | 10:00 | 6275 | 18:00 (5078) |
| vrijdag | 10:00 | 6734 | 17:00 (4570) |
| zaterdag | 10:00 | 3409 | 18:00 (2393) |
| zondag | 10:00 | 2582 | 18:00 (2253) |

Patroon: 10:00 is elke dag de piek, 17:00 tot 18:00 is de tweede. 19:00 is op elke dag zwakker dan 18:00. Weekend is duidelijk lager dan doordeweeks. Sterkste dagen zijn vrijdag en woensdag.

Voorbehoud: de koppeling is dezelfde dag gelegd, dus dit kan nog op een algemeen model leunen in plaats van op het gedrag van de eigen volgers. Het patroon is verdacht glad (elke dag exact 10:00). Na een paar weken echte posts opnieuw ophalen.

## De 12 posts staan erin (15 september 2026)

Alle 12 zijn aangemaakt als **concept** (`draft: true`). Er publiceert niets vanzelf zolang dat zo blijft.

Per post: Instagram en Facebook samen, Collab-uitnodiging naar @poortpadel, poster als beeld, caption met 5 hashtags.

Tijden aangepast op de eigen Metricool-data: maandag 18:00 en donderdag 10:00, in plaats van maandag 19:00 en donderdag 12:15. Reden: 19:00 is op elke dag zwakker dan 18:00, en 10:00 is elke dag de piek. Nog te bevestigen door Lars.

| Datum | Tijd | Poster | Post id |
|---|---|---|---|
| ma 21 sep | 18:00 | 01_najaarsreeks | 376353443 |
| do 24 sep | 10:00 | 09_padel | 376353707 |
| ma 28 sep | 18:00 | 14_samen | 376353750 |
| do 1 okt | 10:00 | 02_eerste_les | 376353804 |
| ma 5 okt | 18:00 | 07_laatste_plekken | 376353874 |
| do 8 okt | 10:00 | 11_jouw_coach | 376353996 |
| ma 12 okt | 18:00 | 15_geen_racket | 376354046 |
| do 15 okt | 10:00 | 16_backhand | 376354128 |
| ma 19 okt | 18:00 | 04_techniek | 376354167 |
| do 22 okt | 10:00 | 10_competitie | 376354297 |
| ma 26 okt | 18:00 | 18_teamuitje | 376354331 |
| do 29 okt | 10:00 | 20_vaste_plek | 376354400 |

### Hoe het beeld erin kwam

Metricool wil publieke URL's. De posters zijn kort in de publieke repo gezet, Metricool heeft ze naar zijn eigen opslag gekopieerd (`static.metricool.com`), daarna zijn ze weer uit de repo gehaald. Ze blijven wel in de geschiedenis van de repo staan.

Voor volgende sets is een vaste plek voor beeld nodig. Netlify is vanuit deze omgeving niet bereikbaar. Google Drive werkt alleen op een betaald Metricool-plan, of via een CSV-import met een publiek gedeelde Drive-link (`view?usp=sharing`, openbaar).

## Bijgewerkt op 15 september 2026, avond

Alle 26 concepten in Metricool opnieuw geschreven:

- Facebook van 3 naar 8 hashtags
- LinkedIn van 3 naar 5 hashtags
- Telefoonnummer uit alle teksten, Instagram verwijst naar de link in bio, Facebook en LinkedIn naar de inschrijflink

Let op voor de volgende keer: de post-id verandert bij elke update, de uuid blijft gelijk. Werk dus met de uuid als vaste sleutel en haal de id telkens opnieuw op met getScheduledPosts.

Les geleerd: een wijziging in de repo en in de artifacts is niet genoeg, Metricool heeft zijn eigen kopie van de tekst. Alle drie moeten mee.

## Definitief ingepland op 15 september 2026, na groen licht van Lars

Lars heeft alles in de redactietafel en de publicatieplanner goedgekeurd. Alle posts staan nu op **draft: false** en gaan vanzelf de deur uit via de koppeling.

Wat er is veranderd ten opzichte van de vorige ronde:

- Dagen van maandag en donderdag naar **woensdag en vrijdag**, met de eerste post op **donderdag 17 september**. Onderbouwing in `docs/doelgroep-en-posttijden.md`.
- Tijd van 18:00 en 10:00 naar **18:30 voor Instagram en Facebook** en **11:00 voor LinkedIn**.
- Overal precies **5 hashtags**, geen telefoonnummer, en **@poortpadel in de zin zelf** in plaats van als vaste slotregel.
- LinkedIn staat aan bij 9 van de 12 momenten. Uit: 15_geen_racket, 16_backhand en 04_techniek, die zijn te weinig zakelijk.

### Het schema

| Datum | Dag | Onderwerp | IG | FB | LI |
|---|---|---|---|---|---|
| 17 sep | do | 01_najaarsreeks | 18:30 | 18:30 | 11:00 |
| 23 sep | wo | 09_padel | 18:30 | 18:30 | 11:00 |
| 25 sep | vr | 14_samen | 18:30 | 18:30 | 11:00 |
| 30 sep | wo | 02_eerste_les | 18:30 | 18:30 | 11:00 |
| 2 okt | vr | 11_jouw_coach | 18:30 | 18:30 | 11:00 |
| 7 okt | wo | 07_laatste_plekken | 18:30 | 18:30 | 11:00 |
| 9 okt | vr | 15_geen_racket | 18:30 | 18:30 | |
| 14 okt | wo | 16_backhand | 18:30 | 18:30 | |
| 16 okt | vr | 04_techniek | 18:30 | 18:30 | |
| 21 okt | wo | 10_competitie | 18:30 | 18:30 | 11:00 |
| 23 okt | vr | 18_teamuitje | 18:30 | 18:30 | 11:00 |
| 28 okt | wo | 20_vaste_plek | 18:30 | 18:30 | 11:00 |

Totaal 33 posts: 12 Instagram, 12 Facebook, 9 LinkedIn. Gecontroleerd met getScheduledPosts, alle 33 staan op PENDING en draft is overal uit.

### Twee dingen die nog open staan

1. **Locatie Poort Padel.** De koppeling heeft geen veld voor een locatie. Dat moet per post met de hand in de Metricool webplanner. @poortpadel staat wel in elke tekst en de Collab-uitnodiging staat op elke Instagram post.
2. **Oktober telt 21 posts.** Op een gratis Metricool-plan kan er een maandlimiet van 20 zitten. Als er iets niet uitgaat, dan is dat de reden. Even in de gaten houden rond eind oktober.

## Dagen gevarieerd op 15 september 2026

Lars vroeg of vaste dagen wel slim zijn. Antwoord: woensdag en vrijdag blijven de basis, maar drie momenten gaan bewust naar een andere dag.

**Waarom.** Niet omdat die dagen beter zijn, maar omdat Metricool nooit iets over maandag, dinsdag of donderdag kan leren als er nooit iets op staat. De cijfers die we nu hebben zijn een algemeen model, te herkennen aan de piek van 10:00 op letterlijk elke dag, ook in het weekend. Variatie is de enige manier om daar echte eigen data van te maken.

**Wat er verandert.**

| Was | Wordt | Post | Kanalen |
|---|---|---|---|
| wo 23 sep | di 22 sep | 09_padel | IG, FB, LinkedIn |
| wo 14 okt | ma 12 okt | 16_backhand | IG, FB |
| vr 16 okt | do 15 okt | 04_techniek | IG, FB |

Dat zijn 7 posts in Metricool. Geen enkele tekst is aangepast.

**Twee dingen die goed uitkomen.** 07_laatste_plekken blijft op woensdag 7 oktober staan, want die zegt "over twee weken start de najaarsreeks" en dat moet kloppen met 19 oktober. En de maandag- en donderdagtest raken alleen Instagram en Facebook, want bij die twee posts staat LinkedIn toch al uit. De dinsdagtest gaat wel mee naar LinkedIn, wat juist gunstig is: dinsdag tot donderdag doet het daar beter dan maandag en vrijdag.

**Verdeling na de wijziging:** woensdag 4, vrijdag 4, donderdag 2, dinsdag 1, maandag 1. Nog steeds 2 posts per week, nergens twee dagen achter elkaar. De langste tussenpoos is 6 dagen, tussen 15 en 21 oktober.

**Voorbehoud.** Met 12 posts krijg je een richting, geen bewijs. Eén post op maandag zegt statistisch weinig, want hoe goed een post loopt hangt veel meer af van de inhoud dan van de dag. Pas na een paar maanden is dit te lezen. De echte winst zit in Reels, die halen 2 tot 3 keer het bereik van een statische post.

## Locatie Poort Padel toevoegen lukt niet (17 september 2026)

Metricool vindt de locatie Poort Padel niet. Uitgezocht: dit is geen fout van Metricool en ook niet van de instellingen.

Metricool's eigen helpcentrum zegt het zo: het zoeken naar locaties loopt via de API van Meta. Staat een locatie daar niet in geregistreerd, of is hij tijdelijk niet beschikbaar via die API, dan vindt Metricool hem niet. Metricool heeft geen eigen locatiedatabase.

Een Facebook-**pagina** is namelijk niet automatisch een Facebook-**plaats**. Poort Padel heeft wel een pagina (id 61579258105585), maar een pagina komt alleen in de plaatsenindex als er een fysiek adres en een passende categorie op staan.

### De test die uitwijst waar het aan ligt

Open de Instagram-app, begin een post en probeer Poort Padel als locatie toe te voegen.

| Uitkomst | Betekenis | Oplossing |
|---|---|---|
| Lukt in de app, niet in Metricool | De plaats bestaat, de API geeft hem niet door | Zie route A |
| Lukt ook in de app niet | De plaats bestaat niet bij Meta | Zie route B |

### Route A: de plaats bestaat wel

Twee opties, en de tweede is beter.

1. Metricool's eigen advies: zet automatisch publiceren uit, dan krijg je een melding op je telefoon en plaats je hem zelf met locatie. Nadeel: je verliest de automatisering.
2. Laat gewoon automatisch publiceren en voeg de locatie daarna toe in de Instagram-app. Een geplaatste post bewerken en er een locatie aan hangen kan gewoon. Kost tien seconden per post en je houdt de planning intact.

### Route B: de plaats bestaat niet

Iemand moet hem aanmaken. Dat kan niet vanuit Instagram, dat loopt via Facebook.

- Facebook-app, nieuwe post, Inchecken, zoeken op Poort Padel, onderaan Nieuwe plaats toevoegen. Naam, adres Neonweg 62 Almere, categorie sportlocatie. Na een dag staat hij ook op Instagram.
- Beter en duurzamer: vraag Poort Padel om op hun eigen Facebook-pagina het adres in te vullen en de categorie op een lokale sportlocatie te zetten. Dan wordt de pagina zelf de plaats. Dat is ook in hun eigen belang, want dan kunnen bezoekers inchecken en komt de club op de kaart te staan.

### Tweede zoekronde, 17 september later op de dag

Op verzoek van Lars nog een keer gezocht in Meta's plaatsenindex (via Make, `searchPagesLocation`, dezelfde bron als Metricool en de Instagram-app), nu met tien varianten.

| Zoekterm | Uitkomst |
|---|---|
| Poort Padel, Poortpadel, Padel Poort, PoortPadel Almere | leeg |
| Neonweg, Neonweg 62 Almere | leeg, er is op dat adres helemaal geen plaats |
| Poort Padel Almere, Almere Poort | 39 tot 44 plaatsen in de wijk, geen padel |
| Padel Almere | 1 treffer: "Padel Almere" aan de Marathonlaan 20. Dat is een andere club in Almere Stad, niet gebruiken |
| Padelclub Almere, Padel | alleen buitenlandse clubs |

Conclusie blijft: de plaats bestaat niet. Route B is de enige weg.

Wat wel bestaat en als tussenoplossing kan: de wijk **Almere-Poort** (Meta id 211366062378022). Dan staat er "Almere-Poort" boven de post in plaats van de clubnaam. Beter dan niets voor lokale vindbaarheid, maar het tagt de club niet.

### Afweging

De locatietag is een leuke extra, geen must. Er staat al iets sterkers klaar: bij elke Instagram-post gaat er een Collab-uitnodiging naar @poortpadel, en die zet de post op hun feed voor circa 1.070 volgers. Dat levert meer op dan een locatietag.

**Zet de 33 ingeplande posts dus niet terug naar handmatig publiceren om dit op te lossen.** Dat is een slechte ruil.

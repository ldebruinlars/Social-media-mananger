# Postschema najaar 2026

12 feed posts, 2 per week, 21 september tot en met 29 oktober. Instagram als hoofdkanaal, Facebook als cross-post.

Tijden: maandag 19:00, donderdag 12:15.

Onderbouwing (opgezocht 15 september 2026, algemene data, niet van jouw account):
- Avond 18:00 tot 21:00 verslaat de ochtend op de meeste dagen. Maandagavond piekt rond 19:00. 18:30 valt bij veel gezinnen in het eten, 19:00 is net daarna.
- Donderdag gedraagt zich anders dan de rest van de week: daar ligt de piek eerder op de dag. Voor een Nederlands publiek is 12:00 tot 14:00 doordeweeks een sterk blok. 12:15 blijft dus staan.
- Deze cijfers meten likes en bereik, niet inschrijvingen, en komen grotendeels uit internationale datasets. Jouw eigen insights zijn het echte antwoord: Instagram, Professioneel dashboard, Totaal aantal volgers, Meest actieve tijden. Daar heb je wel genoeg volgers voor nodig voordat het paneel verschijnt.
- Na zes weken kijken we naar jouw cijfers en zetten we de tijden op wat bij jou werkt.

## Wat wanneer online gaat

| Dag | Tijd | Poster | Kop | Knop | Pijler |
|---|---|---|---|---|---|
| maandag 21 september | 19:00 | 01_najaarsreeks | 8 weken beter padellen | Schrijf je in | najaarsreeks |
| donderdag 24 september | 12:15 | 09_padel | Binnen 10 minuten ben je verkocht | Boek een losse les | waarom padel |
| maandag 28 september | 19:00 | 14_samen | Samen inschrijven? | Schrijf je in | najaarsreeks |
| donderdag 1 oktober | 12:15 | 02_eerste_les | Je eerste les regelen wij | Boek een losse les | beginners |
| maandag 5 oktober | 19:00 | 07_laatste_plekken | Laatste plekken najaarsreeks | Schrijf je in | najaarsreeks |
| donderdag 8 oktober | 12:15 | 11_jouw_coach | Jouw coach, jouw moment | Kies je coach | losse training |
| maandag 12 oktober | 19:00 | 15_geen_racket | Geen racket? Geen probleem | Boek een losse les | beginners |
| donderdag 15 oktober | 12:15 | 16_backhand | Backhand onder controle | Boek een losse les | techniek |
| maandag 19 oktober | 19:00 | 04_techniek | Jouw smash, onze focus | Boek een losse les | techniek |
| donderdag 22 oktober | 12:15 | 10_competitie | Klaar voor de competitie? | Boek wedstrijdtraining | competitie |
| maandag 26 oktober | 19:00 | 18_teamuitje | Padel met je team | Plan je event | bedrijven |
| donderdag 29 oktober | 12:15 | 20_vaste_plek | Jouw vaste plek om te spelen | Schrijf je in | community |

De najaarsreeks loopt als een lijn door de eerste helft: aankondiging, samen inschrijven, laatste plekken twee weken voor de start. Daarna verschuift de aandacht naar losse trainingen en de competitie.

## Bij elke post

- Locatie: Poort Padel
- Tag in de foto: @poortpadel
- Collab uitnodiging naar @poortpadel, dan staat de post ook op hun account
- Story dezelfde dag met link-sticker naar de inschrijfpagina
- Countdown-sticker bij 01 en 07, die tellen af naar 19 oktober

## Twee keer goedkeuren

Voordat er iets live gaat zijn er twee momenten waarop jij ja zegt.

1. **Postercheck**: https://claude.ai/artifact/SZHraJFEar8GRhpCMEt9xK. Daar keur je beeld en tekst per poster goed of vraag je een aanpassing. Dat is de ronde die we nu vijf keer hebben gedaan.
2. **Publicatieplanner**: https://claude.ai/artifact/86xmviVu8NTuFQ6DPNizCb. Daar zie je elke post zoals hij straks in je feed staat, met datum, tijd en de caption eronder. Per post kies je Groen licht, Nog wachten of Overslaan.

Pas als een post in de planner op groen licht staat, mag hij weg. Staat hij op nog wachten of overslaan, dan gebeurt er niets. Je keuzes komen binnen in de collectie `publicatie`, die lees ik uit.

## Koppeling met Meta

Koppellink voor Instagram en Facebook in Make: https://eu1.make.com/1563554/credentials-requests/inbox?requestId=97f6c5c4-02c5-40d7-a528-a7b2cff9e4a5

Log in met het account dat beheerder is van de Facebook pagina en het Instagram account, en keur beide koppelingen goed. Voorwaarden van Meta: het Instagram account moet een professioneel account zijn (Bedrijf of Maker) en gekoppeld aan de Facebook pagina van All Court Academy.

### Wat wel en niet kan via de koppeling

| Kanaal | Concept opslaan | Inplannen | Direct publiceren |
|---|---|---|---|
| Instagram | nee, Meta staat dit niet toe via de koppeling | nee, alleen handmatig in Business Suite | ja |
| Facebook pagina | ja, komt als concept in Business Suite | ja | ja |

Instagram laat via de koppeling alleen direct publiceren toe. Concepten en inplannen kan daar alleen met de hand in Meta Business Suite. Dat is een beperking van Meta, niet van ons.

### De route die daar het dichtst bij komt

Een Google Sheet `Postplanning ACA` met per rij: datum, tijd, posterbestand, caption, status. Make kijkt elk uur in die sheet.

1. Ik vul de sheet met de 12 posts hierboven en zet de status op `wacht op akkoord`.
2. Jij zet de status op `akkoord` bij de posts die weg mogen. Eén cel, ook op je telefoon.
3. Op de geplande dag en tijd publiceert Make de post op Instagram en Facebook, met foto, caption, locatie en tag.
4. Ging er iets mis, dan krijg je een mail met de reden.

Zo is jouw handeling per post één tik in de sheet, en hoef je verder niets meer te doen. Wil je liever eerst zien hoe het eruitziet op je profiel, dan zet ik hem eerst als concept op Facebook en publiceer ik Instagram pas na jouw akkoord.

### Alternatief zonder koppeling

Alles staat klaar in `outputs/posters/2026-10/` en `outputs/captions/2026-10-posters.md`. In Meta Business Suite kun je de 12 posts in één zitting inplannen met Planner. Kost ongeveer een half uur en je bent voor zes weken klaar.

## Daarna

Vanaf 2 november is de planning leeg. Acht onderwerpen liggen klaar maar zijn nog niet ingepland: Kids Kamp, train met een vaste coach, jeugdtraining, vrije plekken deze week, padel is voor iedereen, kinderfeestje, kerstreeks en clubgevoel.

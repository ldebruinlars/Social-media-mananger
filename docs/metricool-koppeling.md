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

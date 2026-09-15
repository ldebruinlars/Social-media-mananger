# Verschil per kanaal

Vastgelegd 15 september 2026, na de splitsing in Metricool.

## De regel per kanaal

| | Instagram | Facebook | LinkedIn |
|---|---|---|---|
| Links in de tekst | nee, niet klikbaar | ja | ja |
| Call to action | link in bio | echte URL in de tekst | echte URL in de tekst |
| Hashtags | 5 | 3, doen daar weinig | 3, zakelijk |
| Collab @poortpadel | ja | nee, bestaat niet | nee |
| Toon | casual, uitnodigend | casual, iets zakelijker | zakelijk, geen emoji-regen |
| Doelgroep | spelers en beginners | spelers, ouders, lokaal | bedrijven, events, ondernemers |

Instagram en Facebook staan daarom **los van elkaar** in Metricool, met eigen tekst per kanaal. Ze delen wel dezelfde poster en hetzelfde moment.

## Links

| Waarvoor | URL |
|---|---|
| Lessen, reeksen, losse lessen, inschrijven | https://allcourtacademy.com/pages/lessen.html |
| Bedrijven | https://allcourtacademy.com/pages/business.html |
| Events | https://allcourtacademy.com/pages/events.html |

Niet geverifieerd: deze pagina's kon ik vanaf hier niet openen, allcourtacademy.com is geblokkeerd door de netwerkinstellingen van deze omgeving. De URL's zijn overgenomen zoals Lars ze gaf.

## Wat er nu ingepland staat

- **Instagram**: 12 posts, ma 18:00 en do 10:00, met link in bio en Collab naar @poortpadel
- **Facebook**: dezelfde 12 momenten, eigen tekst met de echte link erin, 3 hashtags
- **LinkedIn**: 2 posts als start, 8 en 22 oktober om 10:00

Alles staat op concept. Er publiceert niets vanzelf.

## LinkedIn heeft eigen content nodig

De twee die er nu staan zijn gemaakt van bestaand beeld:

| Datum | Onderwerp | Link |
|---|---|---|
| do 8 okt 10:00 | bedrijfsuitje waar iedereen aan meedoet | business.html en events.html |
| do 22 okt 10:00 | vaste avond in de week, voor ondernemers en fulltimers | lessen.html |

Twee posts in zes weken is weinig. Voorstellen voor eigen LinkedIn-onderwerpen, nog te bespreken met Lars:

- Een klantcase van een teamuitje, met foto en een quote van de organisator
- Padel als personeelsbeleid: vitaliteit, teamverbinding, lage drempel
- Achter de schermen: hoe we een event van 60 man in een middag draaien
- De coaches voorstellen, één per post, met hun achtergrond
- Cijfers over de groei van padel in Flevoland, alleen als we echte bronnen hebben

Voor LinkedIn is ander beeld nodig dan de feed-posters: liggend of vierkant werkt daar beter dan 4:5, en foto's van groepen en bedrijven doen het beter dan losse spelers.

## Herzien op 15 september 2026, avond

Lars wil **overal precies 5 hashtags**, ook op Facebook en LinkedIn. De korte proef met 8 op Facebook is teruggedraaid.

| Kanaal | Hashtags | Telefoonnummer |
|---|---|---|
| Instagram | 5 | nee, link in bio |
| Facebook | 5 | nee, inschrijflink in de tekst |
| LinkedIn | 5 | nee, inschrijflink in de tekst |

### Twee fouten die dit veroorzaakten

1. Het hint-label in de redactietafel stond hard op "3 hashtags" en was nooit meegenomen toen de teksten veranderden. Labels die een regel herhalen moeten mee met de regel.
2. De redactietafel laadde opgeslagen tekst uit localStorage over de nieuwe tekst heen. Lars zag daardoor zijn eigen eerste sessie terug, niet de nieuwe versie. Opgelost door de sleutel te verhogen naar `aca-redactie-v3`, wat oude opslag laat vervallen.

### Checklist bij elke tekstwijziging

De tekst staat op vier plekken. Alle vier bijwerken, daarna controleren:

1. `outputs/redactie/rows.json` en `outputs/planner/posts.json`
2. `outputs/captions/2026-10-posters.md`
3. De twee artifacts opnieuw publiceren
4. Metricool, alle posts, via updateScheduledPost

Daarna terugleggen met getScheduledPosts en tellen, niet aannemen dat het goed staat.

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

## LinkedIn hashtags onderzocht, 15 september 2026

### Wat er sinds eind 2024 veranderd is

LinkedIn heeft het volgen van hashtags afgeschaft en de hashtagpagina's uitgezet. Er is geen aparte hashtagfeed meer en op desktop zijn ze niet eens klikbaar. Wat ze nog doen: het algoritme vertellen waar je post over gaat, en meetellen in zoeken. Gemeten effect op bereik is nog ongeveer 9 procent.

Belangrijker: **het algoritme leest nu de woorden in de post zelf** om te bepalen wie hem ziet. De tekst is dus de motor, de hashtags zijn hooguit een duwtje.

### Opbouw die we aanhouden

Vijf per post, volgens 1-2-2: 1 brede tag, 2 zakelijke, 2 lokale of specifieke.

| Rol | Tags |
|---|---|
| Breed | #padel, #bedrijfsuitje |
| Zakelijk | #werkgeluk, #vitaliteit, #teambuilding, #teamuitje, #personeelsuitje, #ondernemerschap, #netwerken, #knltb |
| Lokaal en specifiek | #almere, #flevoland, #poortpadel |

### Wat eruit ging en waarom

| Tag | Reden |
|---|---|
| #coaching | wordt op LinkedIn gedomineerd door life- en business-coaches, een padelpost verdrinkt daarin |
| #clinic | betekent op LinkedIn vooral iets medisch |
| #padelles | consumententerm, past niet bij een zakelijk publiek |
| #ondernemers | #ondernemerschap is de tag die in Nederland daadwerkelijk gebruikt wordt |

Nieuw erbij: #werkgeluk (sterk NL HR-onderwerp), #ondernemerschap, #poortpadel als locatie.

### Bronnen

- https://sproutsocial.com/insights/linkedin-hashtags/
- https://contentin.io/blog/do-hashtags-work-on-linkedin/
- https://blog.hootsuite.com/linkedin-algorithm/
- https://stormachtig.nl/dit-zijn-de-populairste-linkedin-hashtags-in-nederland-gebruik-de-hashtag-generator/

### Meer padel erin, 15 september 2026

Lars zag te weinig padel in de LinkedIn-tags. Klopte: bij de teamuitje-posts stond helemaal geen padel-tag.

Nieuwe opbouw, nog steeds 5 per post: **2 padel, 2 zakelijk, 1 lokaal of locatie**. Elke LinkedIn-post heeft nu minstens twee padel-tags.

De twee erbij:

| Tag | Waarom deze |
|---|---|
| #padelnederland | de landelijke padel-tag, en we gebruiken hem al op Instagram |
| #padelalmere | padel en regio in één, ook al in gebruik op Instagram |

Allebei bewust gekozen uit de set die op Instagram al draait, zodat de kanalen dezelfde taal spreken. Er is geen publieke data over hoeveel padel-tags op LinkedIn gebruikt worden, dus dit is een redenering, geen meting.

## @poortpadel en de locatie, 15 september 2026

Handle geverifieerd: **instagram.com/poortpadel**, 1069 volgers, 13 indoor banen aan de Neonweg 60-62 in Almere. Dat is de juiste.

`@poortpadel` staat nu in de tekst van alle 33 posts. Waar Poort Padel al genoemd werd is de naam vervangen, waar hij ontbrak staat er een eigen regel "Bij @poortpadel in Almere." boven de hashtags.

### Wat de vermelding per kanaal doet

| Kanaal | Wordt het een link | Toelichting |
|---|---|---|
| Instagram | **ja** | Instagram maakt @vermeldingen in een caption automatisch klikbaar |
| Facebook | nee | een pagina @taggen vraagt de pagina-ID in een speciaal formaat, dat geeft de koppeling niet door |
| LinkedIn | nee | zelfde verhaal, een bedrijfspagina vermelden vraagt een URN |

Op Facebook en LinkedIn blijft het dus leesbare tekst zonder link. Bewuste keuze van Lars.

De Collab-uitnodiging naar @poortpadel staat los daarvan nog steeds op alle 12 Instagram-posts. Dat is sterker dan een vermelding: de post komt ook op hun account te staan.

### Locatie

Metricool ondersteunt locaties wel, maar alleen in de webplanner: post openen, op het locatie-icoon klikken, naam zoeken, kiezen. De koppeling die ik gebruik heeft geen veld voor locatie, dus dit is handwerk per post.

De locatiezoeker leunt op de Meta API. Staat Poort Padel er niet tussen, dan heeft Meta hem niet in zijn database.

## Collab versus tag op Instagram (17 september 2026)

Lars: Poort Padel gaat niet op elke post een Collab accepteren, alleen waar ze echt genoemd zijn. Terecht, want een Collab vragen bij een post waar ze zijdelings voorkomen is een rare vraag.

Alle twaalf Instagram-teksten nagelopen op de rol die Poort Padel speelt.

**Collab blijft staan (3):** hier is Poort Padel mede-onderwerp, niet een adresregel.

| Post | Datum | Waarom |
|---|---|---|
| 09_padel | 22 sep | Werving voor padel als sport. Hun banen en glaswand zijn het verhaal, en meer spelers is direct hun belang. |
| 18_teamuitje | 23 okt | "Banen, coaches, rackets en catering in huis." Hun faciliteiten zijn de helft van het aanbod. |
| 20_vaste_plek | 28 okt | Gaat over de plek en het clubgevoel zelf. |

**Collab eraf (9):** 01_najaarsreeks, 14_samen, 02_eerste_les, 11_jouw_coach, 07_laatste_plekken, 15_geen_racket, 16_backhand, 04_techniek, 10_competitie.

Daar staat @poortpadel als praktisch detail: "lessen zijn bij", "baanhuur zit erbij". Dat is ACA's product, niet dat van Poort Padel.

De @poortpadel-vermelding in de tekst blijft overal staan, die is niet afhankelijk van acceptatie.

### Foto-tags kunnen niet via de koppeling

De Metricool API kent bij `instagramData` alleen `collaborators`. Er is geen veld voor het taggen van accounts in de foto. De webplanner van Metricool kan dat wel: drie puntjes op de afbeelding, Add user tag, minimaal drie tekens typen.

Werkverdeling: Claude zet de Collabs via de koppeling, Lars zet de foto-tags in de webplanner. Voorwaarde voor een foto-tag is dat het account openbaar is en tags toestaat, anders negeert Instagram hem stil.

## Foto-tags automatisch zetten: uitgezocht op 17 september 2026

Lars vroeg om zelf uit te zoeken hoe de foto-tag @poortpadel automatisch gezet kan worden. Drie sporen onderzocht.

| Spoor | Uitkomst |
|---|---|
| Metricool-koppeling (MCP) | **Getest op 17 september**, niet alleen uit de docs. Update gestuurd op post 10_competitie met `tags`, `userTags`, `user_tags` in `instagramData` en een top-level `mediaTags`, alle met `{username: poortpadel, x: 0.5, y: 0.5}`. Metricool gaf geen fout maar sloeg **geen enkel** tag-veld op: het antwoord bevatte alleen `autoPublish, type, showReelOnFeed, isAiGenerated`. Stil weggegooid. De post zelf bleef intact. Dood, en nu bewezen. |
| Metricool REST API rechtstreeks | Volgens Metricool's docs ondersteunt hun API foto-tags wel. Maar `app.metricool.com`, `api.metricool.com` en `metricool.com` staan alle drie expliciet op de policy-lijst van de proxy (HTTP 000, verbinding komt nooit tot stand). Opnieuw getest op 17 september, zelfde uitkomst. Dood. |
| Make, app `instagram-business`, module `CreatePostPhoto` | **Werkt.** Heeft `user_tags` (username, x, y) én `location_id`. Vereist wel het recht `instagram_content_publish`, dat de huidige Facebook-verbinding (10964362) niet heeft. Nieuwe autorisatie van Lars nodig. |

### Wat de Make-route in de praktijk betekent

Make publiceert dan de Instagram-post, niet Metricool. Dus:

- Die posts moeten uit Metricool, anders komen ze dubbel.
- Elke post wordt een Make-scenario met `scheduling: once` op datum en tijd, of één scenario dat een planning uitleest.
- De planner van Metricool toont dan niet meer de echte Instagram-planning.
- Beeld moet op een publieke URL staan die de Instagram API kan ophalen. De `static.metricool.com` URL's zijn publiek, maar zijn afhankelijk van Metricool.

Dit is niet nieuw: in `.claude/skills/aca-social-manager/SKILL.md` staat precies dit scenario als oorspronkelijk plan (Google Sheet ACA Content Planning naar Instagram Create a Photo Post). Metricool werd gekozen omdat het sneller stond, maar Make kan dingen die Metricool's API niet kan.

### Advies

**Voor de lopende campagne: niet doen.** Negen foto-tags met de hand in de Metricool webplanner is drie minuten werk. Een draaiend systeem ombouwen terwijl de eerste post vanavond de deur uitgaat is het niet waard.

**Voor de novembercampagne: overwegen.** Als Lars foto-tags en locatie standaard wil, is een Make-publisher voor Instagram de betere basis. Dan zit het er voor altijd in en hoeft niemand meer te klikken.

### De locatie Poort Padel bestaat niet bij Meta

Via Make's `searchPagesLocation` (dezelfde plaatsenindex die Instagram gebruikt) gezocht op "Poort Padel", "Poortpadel" en "Neonweg Almere". Alle drie leeg. Controlezoekopdracht op "Almere" gaf 44 resultaten, dus de zoeker werkt.

Conclusie: het is geen Metricool-probleem. **De plaats bestaat niet.** Geen enkel tool kan hem taggen totdat iemand hem aanmaakt, zie de routes in `docs/metricool-koppeling.md`. Poort Padel zelf is de aangewezen partij: adres invullen op hun Facebook-pagina en categorie op lokale sportlocatie zetten.

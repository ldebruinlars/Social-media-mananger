# Meta Ads: wat kan ik zien, en waar moet de campagne op gecontroleerd worden

Opgezocht op 16 september 2026, op verzoek van Lars.

## Wat ik nu kan en niet kan

Ik heb drie routes gecontroleerd. Alle drie dicht.

| Route | Uitkomst |
|---|---|
| Metricool | Merk All Court Academy heeft alleen Facebook, Instagram en LinkedIn gekoppeld. **Geen advertentieaccount.** |
| Make.com (team 1563554) | Verbindingen zijn Mollie, Google, Moneybird en Gmail. **Geen Facebook of Meta.** |
| Meta Ads connector (Hyper MCP) | Niet geinstalleerd in deze omgeving. De skill `hyper-meta-ads` heeft hem nodig en stopt zonder. |

Ik kan dus niets van de campagne zien. Niet lezen, en zeker niet aanpassen.

## Wat Metricool wel zou geven als het advertentieaccount gekoppeld wordt

De `metaAds` bron van Metricool is uitgebreid. Beschikbaar per campagne: uitgaven, bereik, impressies, klikken, unieke klikken, CPC, CPM, CTR op link- en outbound-kliks, gemiddelde frequentie, leads, aanmeldingen, afgeronde registraties, ROAS en resultaat per doel.

Belangrijke beperking: **Metricool leest advertenties alleen, het kan ze niet wijzigen.** De koppeling hier heeft geen enkele functie om een campagne, advertentiegroep of budget aan te passen. Alles veranderen blijft handwerk in Meta Ads Manager.

## De doelgroepvraag: nee, Metricool ziet Almere niet

Gecontroleerd op 16 september. De demografische velden van Metricool zijn:

- Instagram: `country` (landnaam en volgers per land), `age and gender`
- Er is **geen stad- of postcodeveld**

Dus Metricool kan niet laten zien hoeveel van je bereik uit Almere komt. Alleen Nederland als geheel.

Daarbij: een testopvraging over 16 augustus tot 16 september gaf **nul rijen terug**. Het account is pas op 15 september gekoppeld en er is nog geen historie opgebouwd.

Voor plaatsniveau moet je in **Instagram Insights** (app, Professionele tools, Je publiek, Topplaatsen) of in **Meta Business Suite** kijken. Die laten wel steden zien. Dat is de enige bron voor de vraag hoeveel bereik uit Almere, Lelystad, Zeewolde en Amsterdam komt.

## Benchmarks om tegen af te zetten

Uit openbare bronnen, september 2026. Let op dat dit brede cijfers zijn, niet padel of Almere.

| Wat | Waarde | Bron |
|---|---|---|
| CPM Nederland, brede doelgroep | 4 tot 9 euro | Meta Ads Netherlands Playbook 2026 |
| CPM Nederland, smalle interesse of retargeting | 8 tot 18 euro | idem |
| CPM-stijging in Q4 | 40 tot 70 procent boven normaal | idem |
| Nederlandstalige advertenties versus Engels | 15 tot 30 procent hogere CTR bij Nederlands publiek | idem |
| CPC alle branches, jaar op jaar | plus 11 procent | Facebook Ads Benchmarks 2026 |

**Er zijn geen betrouwbare benchmarks voor padelscholen in Nederland gevonden.** Cijfers die rondgaan voor "sports" of "fitness" komen vrijwel allemaal uit Amerikaanse e-commerce en zeggen niets over een lokale lesaanbieder. Gebruik ze niet als doel.

## Waar de campagne op gecontroleerd moet worden

Volgorde uit `hyper-meta-ads/references/account-audit.md`, toegepast op een lokale padelschool.

### 1. Structuur

- Hoeveel campagnes staan er actief, en met welk doel? Overlappende doelen laten je tegen jezelf bieden in de veiling.
- Hoeveel advertentiegroepen per campagne? Dit is bij een klein budget het belangrijkste punt, zie hieronder.

### 2. De leerfase, het grootste risico bij klein budget

Meta heeft ongeveer **50 conversies per advertentiegroep per week** nodig om te leren optimaliseren. Daaronder blijft een groep in de leerfase en presteert hij structureel slechter.

Rekenvoorbeeld: bij 10 euro per dag is dat 70 euro per week. Verdeeld over vier advertentiegroepen krijgt elke groep 2,50 euro per dag. Geen enkele groep haalt ooit 50 conversies. Alle vier blijven in de leerfase.

Dus: **een campagne, een advertentiegroep, alle budget erop.** Splitsen kan pas als je genoeg volume hebt.

Kies ook een conversiedoel dat vaak genoeg voorkomt. Een inschrijving voor een achtweekse reeks gebeurt te weinig om op te optimaliseren. Optimaliseer op iets goedkopers dat er dicht bij zit: een lead, een formulierstart, of desnoods een landingspaginaweergave.

### 3. Targeting

Bij een straal van 20 km rond Almere zit je op een paar honderdduizend mensen. Dat is klein.

- **Leg er geen interesses overheen.** Straal plus leeftijd is genoeg. Elke extra laag maakt het publiek kleiner en de CPM hoger, en je zit dan in de dure 8 tot 18 euro categorie in plaats van de 4 tot 9.
- Controleer of de straal niet half in het IJsselmeer valt. Rond Almere is een flink deel van een cirkel water. Een straal van 20 km levert dus minder mensen dan het getal suggereert.
- Leeftijd afstemmen op het product. Lessenreeks volwassenen is 25 tot 45. Kids Kamp is ouders, dus 30 tot 50, niet de kinderen zelf.

### 4. Frequentie, extra belangrijk bij een kleine straal

Frequentie boven 3 in dertig dagen betekent advertentiemoeheid. Bij een landelijke adverteerder duurt dat maanden, bij jouw publiek van een paar honderdduizend mensen ben je daar binnen weken. Plan dus vooraf twee of drie verschillende creatives om te wisselen.

### 5. Creatives

- Video boven statisch beeld. Je hebt de Pablo-video en materiaal van de baan.
- Nederlands, niet Engels. Levert 15 tot 30 procent hogere CTR bij Nederlands publiek.
- De eerste drie seconden moeten de baan laten zien, niet je logo.

### 6. Het aanbod

Een achtweekse reeks is een grote eerste stap voor iemand die je niet kent. De losse proefles of eerste les met gratis leenracket is een veel kleinere drempel. Adverteer op de kleine stap en verkoop de reeks daarna.

### 7. Meting

- Staat de Meta pixel op allcourtacademy.com en vuurt hij op de bedankpagina van het inschrijfformulier?
- Staan er UTM-parameters op elke advertentie die naar de site stuurt? Zonder `utm_source=meta` kun je achteraf niet zien wat de advertentie heeft opgeleverd.
- **DSA-velden.** Advertentiegroepen die op de EU richten moeten `dsa_beneficiary` en `dsa_payor` ingevuld hebben, wie profiteert van en wie betaalt voor de advertentie. Zonder die velden beperkt Meta de levering. Dit wordt vaak vergeten.

### 8. Timing

Q4 CPM's liggen 40 tot 70 procent boven normaal door Black Friday, Sinterklaas en kerst. De najaarsreeks start 19 oktober, dus de werving valt net voor die piek. **Zet het budget zwaar in september en de eerste helft van oktober**, niet in november en december. Voor de voorjaarsreeks van januari is begin januari juist goedkoop, want dan is de drukte voorbij.

## Wat Lars moet doen om mij te laten meekijken

1. Metricool openen, merk All Court Academy, Verbindingen
2. **Meta Ads** (of Facebook Ads) koppelen aan het advertentieaccount
3. Een paar dagen wachten tot Metricool historie heeft opgehaald

Daarna kan ik uitgaven, CPM, CPC, CTR, frequentie en resultaten per campagne uitlezen en er een echte analyse op doen in plaats van een checklist.

Let op: dat geeft mij **leestoegang**. Aanpassen blijft in Meta Ads Manager, door Lars zelf. Dat was ook zijn uitdrukkelijke wens.

## 16 september, avond: advertentieaccount gekoppeld, nog geen data

Lars heeft het advertentieaccount gekoppeld. In de merkinstellingen staat nu:

```
facebookAdsData: act_1495244022295779
```

De koppeling is dus geregistreerd. Maar er komt nog niets uit.

| Opvraging | Periode | Resultaat |
|---|---|---|
| Campagnenaam + uitgaven + bereik + frequentie + CTR + resultaten | 18 jun t/m 16 sep | 0 rijen |
| Alleen campagnenaam + uitgaven | 17 aug t/m 16 sep | 0 rijen |
| Campagnenaam + id + uitgaven + impressies | 16 sep 2025 t/m 16 sep 2026 | 0 rijen |
| Instagram demografie (land, leeftijd, geslacht) | 17 aug t/m 16 sep | 0 rijen |

Die laatste regel is het belangrijkste diagnosepunt. **Instagram is al sinds 15 september gekoppeld en levert ook nog niets.** Het probleem zit dus niet in de advertentiekoppeling, maar in de analytics van dit merk als geheel.

Netwerknaam ter referentie: `metaads`. `facebookAds` bestaat niet als netwerk in de API, dat gaf een foutmelding.

### Drie mogelijke oorzaken, en hoe je ze uit elkaar houdt

1. **Synchronisatie loopt nog.** Metricool haalt historie op na een koppeling en dat kan tot een dag duren. Instagram is nu ruim 24 uur oud en nog leeg, dus dit verklaart niet alles.
2. **Gratis plan.** Advertentierapportage is bij Metricool mogelijk een betaalde functie. Niet bevestigd, wel plausibel gezien de rest van de planbeperkingen.
3. **Rechten.** Als het advertentieaccount van het bureau is en niet van Lars, kan Metricool wel de koppeling leggen maar geen cijfers ophalen.

**Test die het uitwijst:** open Metricool in de browser, ga naar het merk en open het Ads-onderdeel. Staan daar wel cijfers, dan is het een API- of planbeperking. Staat daar ook niets, dan is het synchronisatie of rechten.

### Snelste route naar een echte analyse

Een export uit Meta Ads Manager over de laatste 30 dagen, op campagneniveau, met deze kolommen: campagnenaam, doelstelling, uitgegeven bedrag, bereik, impressies, **frequentie**, CTR, resultaten, kosten per resultaat. Als CSV of als screenshot.

## Vragen om aan het bureau te stellen

Lars heeft een social media bureau dat dit beheert. Onderstaande vragen scheiden een bureau dat stuurt van een bureau dat alleen budget uitgeeft. Bij elk staat waarom het ertoe doet.

| Vraag | Waarom |
|---|---|
| Hoeveel advertentiegroepen draaien er en wat is het dagbudget per groep? | Meta heeft circa 50 conversies per groep per week nodig. Klein budget over veel groepen betekent dat geen enkele groep uit de leerfase komt. |
| Op welke gebeurtenis optimaliseren we, en hoe vaak gebeurt die per week? | Optimaliseren op een inschrijving die vijf keer per week voorkomt werkt niet. Dan moet je een frequentere gebeurtenis kiezen. |
| Wat is de frequentie over de laatste 30 dagen? | Boven 3 is advertentiemoeheid. Bij een straal rond Almere loop je daar snel tegenaan. Weet het bureau dit niet uit het hoofd, dan wordt er niet op gestuurd. |
| Welke straal draaien we en liggen er interesses overheen? | Interesses bovenop een kleine straal duwen de CPM van 4 tot 9 euro naar 8 tot 18 euro, voor minder mensen. |
| Wat kost een inschrijving ons? | Niet bereik, niet impressies, niet CPC. Als het rapport alleen bereik laat zien, wordt er op het verkeerde gestuurd. |
| Vuurt de pixel op de bedankpagina en staan er UTM's op de advertenties? | Zonder allebei is achteraf niet te zien wat een advertentie heeft opgeleverd. |
| Zijn `dsa_beneficiary` en `dsa_payor` ingevuld? | Verplicht voor EU-targeting. Ontbreken ze, dan beperkt Meta de levering. Wordt vaak vergeten. |
| Wat is het plan voor Q4? | CPM's liggen dan 40 tot 70 procent hoger. Een goed bureau begint hier zelf over. |
| Hoeveel creatives draaien er en wanneer zijn ze voor het laatst ververst? | Kleine doelgroep verbrandt creatives snel. |
| Krijg ik leestoegang tot het advertentieaccount? | Het is Lars' account en Lars' geld. Een bureau dat hier moeilijk over doet is een serieus signaal. |

## 16 september: de eerste echte cijfers

Metricool toont de advertentiecijfers **wel in de browser, niet via de koppeling**. Vijf opvragingen via de API gaven nul rijen terug terwijl dezelfde periode in de webpagina gewoon gevuld is. Conclusie: advertentiedata zit achter een plan- of API-beperking. Werk dus met exports of screenshots, niet met de koppeling.

### De campagne

Periode 17 augustus tot en met 15 september 2026, dertig dagen. Eén campagne, `PB - Padellessen leads`, doel Outcome leads, strategie Lowest Cost Without Cap.

| | |
|---|---|
| Uitgegeven | 301,18 euro, dus 10,04 per dag |
| Impressies | 38.100 |
| Kliks | 858 |
| Conversies | 20 |
| CPM | 7,90 euro |
| CPC | 0,35 euro |
| CTR | 2,25 procent |
| Conversieratio | 2,33 procent |
| **Kosten per conversie** | **15,06 euro** |

### Wat goed zit

- **CTR 2,25 procent.** Het gemiddelde over alle branches op Facebook ligt rond 1 procent, de benchmark voor leadcampagnes rond 2,5 procent. Dit zit daar vlak onder en ruim boven het algemene gemiddelde. Beeld en aanbod werken.
- **CPC 0,35 euro** is goedkoop.
- **Doelstelling staat op leads**, niet op verkeer of interactie. Dat is de juiste keuze voor een lesaanbieder. Een lui bureau zet dit op verkeer of bereik en laat mooie grote getallen zien die niets opleveren.
- **Eén campagne.** Geen versnippering, geen tegen jezelf bieden in de veiling.
- **Lowest Cost Without Cap** is de verstandige standaard op dit budget.

De basis is dus op orde. Dit is geen slecht opgezette campagne.

### Het structurele plafond: de leerfase

Twintig conversies in dertig dagen is **4,7 per week**. Meta wil er **50 per advertentiegroep per week** om te kunnen optimaliseren. Dat is 9 procent van wat nodig is, een factor 10,7 tekort.

Om die 50 te halen bij 15,06 euro per conversie is 753 euro per week nodig, oftewel 108 euro per dag. Dat is elf keer het huidige budget en dus niet realistisch.

Gevolg: de campagne komt nooit uit de leerfase en Meta blijft in feite gokken. Daar is bij dit budget geen ontkomen aan, maar er volgen wel twee consequenties:

1. **Nooit opsplitsen in meerdere advertentiegroepen.** Al het signaal moet op één plek samenkomen. Elke extra groep deelt die 4,7 conversies per week verder op.
2. **Overweeg een frequentere gebeurtenis om op te optimaliseren.** Iets ondieper in de trechter dat drie tot vijf keer zo vaak voorkomt, geeft Meta genoeg signaal om wel te leren.

### De grootste gratis winst: de CPM omlaag

7,90 euro CPM zit aan de bovenkant van de Nederlandse bandbreedte voor brede doelgroepen (4 tot 9 euro) en aan de onderkant van die voor smalle interesse- of retargetingdoelgroepen (8 tot 18 euro). Dat wijst er sterk op dat er **interesses over de straal heen liggen**.

Wat het oplevert als die eraf gaan, bij hetzelfde budget en gelijke CTR en conversieratio:

| CPM | Impressies | Kliks | Conversies | Per conversie |
|---|---|---|---|---|
| 7,90 (nu) | 38.100 | 859 | 20,0 | 15,05 |
| 6,50 | 46.335 | 1.043 | 24,3 | 12,38 |
| 5,50 | 54.760 | 1.233 | 28,7 | 10,48 |
| 4,50 | 66.929 | 1.507 | 35,1 | 8,57 |

Op 5,50 euro CPM zijn dat **29 conversies in plaats van 20, een stijging van 44 procent, zonder een euro extra uit te geven.** Dit is de belangrijkste aanbeveling.

Voorbehoud: CTR kan iets dalen bij een bredere doelgroep. Zelfs met een kwart lagere CTR blijft dit gunstig.

### Wat nog ontbreekt om het af te maken

| Ontbreekt | Waarom nodig |
|---|---|
| **Bereik** | Zonder bereik geen frequentie. Frequentie = impressies gedeeld door bereik. |
| **Frequentie** | Boven 3 is advertentiemoeheid. Bij een straal rond Almere de meest waarschijnlijke stille remmer. |
| **Aantal advertentiegroepen** (tabblad Groups) | Bepaalt of het signaal al versnipperd is. |
| **Wat telt als conversie** | Een ingevuld formulier of een betaalde inschrijving? Bij 15,06 euro per lead is dat iets heel anders dan 15,06 euro per leerling. |
| **Lead naar klant ratio** | Zonder dit is 15,06 euro niet te beoordelen. Bij 1 op 3 kost een leerling ongeveer 45 euro. |

### Onthouden voor Q4

CPM's stijgen in het vierde kwartaal 40 tot 70 procent. Die 7,90 kan in november en december 11 tot 13 worden. De najaarsreeks start 19 oktober, dus het budget hoort in september en de eerste helft van oktober, niet erna.

## Route gevonden: Make kan het wel ophalen

De Metricool-koppeling geeft geen advertentiedata door, maar Make heeft er twee apps voor die wel werken.

| App | Wat het kan |
|---|---|
| `facebook-insights` v1 | `GetAdAccountInsights`. Cijfers op niveau van advertentieaccount, campagne, advertentiegroep of losse advertentie. Vrij te kiezen periode of preset tot 37 maanden terug. Ondersteunt **breakdowns**. |
| `facebook-ads-cm` v1 | `listCampaigns`, `listAdSets`, `listAds`, `searchLocations`, `searchAdInterests`, `getReachEstimate`. |

Belangrijk: `facebook-ads-cm` bevat ook `updateCampaign`, `updateAdSet` en `updateAd`. **Die worden niet gebruikt.** Lars heeft gevraagd niets aan te passen, dus alleen de lees-modules.

### Wat breakdowns oplossen

De vraag van Lars of het bereik uit Almere komt, kon Metricool niet beantwoorden (alleen landniveau). De Meta Marketing API kan dat wel, via breakdowns op regio, leeftijd, geslacht, plaatsing en apparaat. Dit is dus de route naar die vraag.

### Wat Lars moet doen

Eén Facebook-verbinding toevoegen in Make met leesrecht op advertenties (`ads_read`). Dat is een inlogstap met zijn eigen account, die kan niemand anders doen. Daarna kan het scenario de cijfers op verzoek ophalen.

Op dit moment staan er in team 1563554 alleen verbindingen voor Mollie, Google, Moneybird en Gmail.

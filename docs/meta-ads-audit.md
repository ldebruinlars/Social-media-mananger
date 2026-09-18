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

## 16 september: volledige analyse op eigen opgehaalde data

Verbinding gelegd, Make-tool `ACA Meta Ads inzichten lezen` (id 7446513) gebouwd, drie uitvragen gedaan: per advertentiegroep, uitgesplitst naar regio, en uitgesplitst naar leeftijd en geslacht. Alleen lezen.

### De twee advertentiegroepen

| | Advantage+ | Retarget |
|---|---|---|
| Besteed | 275,49 | 25,69 |
| Impressies | 35.023 | 3.077 |
| **Bereik** | **10.546** | 2.255 |
| **Frequentie** | **3,32** | 1,36 |
| CTR | 2,24% | 2,44% |
| Link-CTR | 1,08% | 0,94% |
| Leads | 18 | 2 |
| Per lead | 15,31 | 12,85 |

### Bevinding 1: de helft van het budget gaat naar leeftijden die niets opleveren

| Leeftijd | Besteed | % budget | CTR | Leads | Per lead |
|---|---|---|---|---|---|
| 18-24 | 9,37 | 3,1% | 1,52% | **0** | geen |
| 25-34 | 55,24 | 18,3% | 1,70% | 9 | **6,14** |
| 35-44 | 93,31 | 31,0% | 1,84% | 9 | **10,37** |
| 45-54 | 67,55 | 22,4% | 2,06% | 2 | 33,77 |
| 55-64 | 50,70 | 16,8% | 3,90% | **0** | geen |
| 65+ | 25,00 | 8,3% | 4,64% | **0** | geen |

- **25 tot 44**: 148,55 euro (49,3% van het budget) levert **18 van de 20 leads**, tegen 8,25 euro per stuk.
- **De rest**: 152,63 euro (50,7%) levert **2 leads**, tegen 76,31 euro per stuk.

Dat is geen toeval. Bij het campagnegemiddelde zou 55-plus ongeveer 5 leads moeten opleveren; het werden er nul. De kans dat dat toeval is, is 0,67 procent. Voor 45-plus samen is die kans 0,41 procent.

**Rekensom:** die 152,63 euro verplaatsen naar 25 tot 44 levert bij 8,25 euro per lead ongeveer 18,5 extra leads op. Totaal zou van 20 naar 36 gaan, een stijging van 82 procent, en de prijs per lead zakt van 15,06 naar 8,25.

### Bevinding 2: de CTR-val

Precies de groepen die het meest klikken leveren niets op:

| Leeftijd | CTR | Link-CTR | Leads |
|---|---|---|---|
| 25-34 | 1,70% | 0,98% | 9 |
| 35-44 | 1,84% | 0,85% | 9 |
| 55-64 | **3,90%** | **1,72%** | **0** |
| 65+ | **4,64%** | **2,21%** | **0** |

Wie op CTR stuurt, concludeert dat 55-plus de beste doelgroep is. Het is de slechtste. De mooie campagne-CTR van 2,25 procent wordt opgehouden door groepen die niet converteren.

### Bevinding 3: frequentie 3,32 en een bereik van maar 10.546

Bereik 10.546 mensen in dertig dagen, met 35.023 impressies. Iedereen ziet de advertentie dus gemiddeld 3,3 keer. Boven 3 is de gangbare grens voor advertentiemoeheid, en in sommige subgroepen loopt het op tot 3,97.

### Bevinding 4: de kliks zijn niet wat ze lijken

858 kliks, maar slechts **407 link-kliks**. Meer dan de helft van de kliks zijn likes, reacties en het uitklappen van de tekst. De echte link-CTR is 1,08 procent, niet 2,25.

De trechter: 35.023 impressies, 378 link-kliks (1,08%), 321 landingspaginaweergaves (85% van de kliks), 18 leads (5,6% van de landingen).

### Bevinding 5: de regio klopt wel

| Regio | Besteed | % | Bereik |
|---|---|---|---|
| Flevoland | 270,00 | 89,6% | 10.305 |
| Noord-Holland | 31,18 | 10,4% | 1.408 |

Bijna negentig procent van het budget landt in Flevoland, waar Almere in ligt. De zorg dat het geld buiten de regio weglekt is ongegrond.

Let op: Meta kan offsite pixel-conversies niet naar regio uitsplitsen, dus welke regio beter converteert is hiermee niet te zeggen.

### Voorbehoud

Twintig leads is een kleine steekproef. De richting is duidelijk en statistisch sterk, maar de precieze bedragen zullen bewegen. Doe de verschuiving stapsgewijs en kijk na twee weken opnieuw.

## Oplossingen, onderbouwd

### Correctie op eerder advies in dit document

Ik schreef eerder dat Advantage+ een leeftijdsondergrens **en** bovengrens respecteert. Dat klopt niet en het is belangrijk.

Bij Advantage+ Audience zijn alleen **locatie, taal, minimumleeftijd, uitsluitingen en Special Ad Category** harde grenzen. Leeftijd als **reeks** en geslacht zijn sinds 2026 **suggesties**: Meta mag daar overheen als het denkt meer resultaat te halen. Alleen de ondergrens blijft staan.

Gevolg voor All Court Academy: de advertentiegroep heet letterlijk `Advantage+`. Zelfs als het bureau 25 tot 44 heeft ingesteld, mag Meta gewoon aan 65-plussers leveren. En dat doet het ook.

### Waarom het misgaat: de twee problemen hangen samen

1. De campagne haalt 4,7 conversies per week, Meta wil er 50. De campagne staat dus permanent op Learning Limited.
2. Zonder voldoende conversiesignaal valt Meta terug op zwakkere signalen: kliks en interactie.
3. Oudere doelgroepen klikken veel meer. 65-plus haalt 4,64 procent CTR tegen 1,70 procent bij 25-34.
4. Advantage+ mag daarheen bewegen, want de bovengrens is maar een suggestie.
5. Resultaat: de helft van het budget naar leeftijden die nul leads opleveren.

Het leerfaseprobleem **veroorzaakt** dus het doelgroepprobleem. Dat is één verhaal, geen twee losse fouten.

### Oplossing 1: Advantage+ Audience uit, harde leeftijdsgrens 25 tot 44

De directe fix. Alleen de minimumleeftijd verhogen is niet genoeg, want dat dicht alleen het lek van 9,37 euro bij 18-24 en laat de 143 euro bij 45-plus gewoon doorlopen. Voor een echte bovengrens moet Advantage+ Audience uit en ga je terug naar originele targeting met een strikte reeks.

Verwachte winst: ongeveer 18 extra leads per maand, prijs per lead van 15,06 naar circa 8,25.

Tegenwerping die het bureau kan geven: breed targeten werkt meestal beter omdat het algoritme meer vrijheid heeft. Dat klopt **als het algoritme signaal heeft**. Bij 4,7 conversies per week heeft het dat niet, en dan is breed juist schadelijk.

### Oplossing 2: native Meta lead form in plaats van een formulier op de site

Nu loopt de trechter via de website: 378 link-kliks, 321 landingen, 18 leads. Elke stap kost mensen.

Een native lead form vult zich voor met gegevens die Meta al heeft en laadt geen externe pagina. Dat levert doorgaans fors meer leads bij hetzelfde budget. Nadeel: de leads zijn minder "warm", want de drempel is lager. Voor een proefles is dat acceptabel.

### Oplossing 3: optimaliseren op een gebeurtenis die vaker voorkomt

Standaardadvies bij te weinig conversies. Zijn landingspaginaweergaves zijn er 321 per maand, oftewel circa 75 per week. Dat is **boven** de grens van 50 en zou de leerfase dus wel uitkomen.

Nadeel, en dit is een echt nadeel: je optimaliseert dan op mensen die klikken, niet op mensen die inschrijven. De kwaliteit zakt. Doe dit alleen als oplossing 1 en 2 onvoldoende opleveren.

### Oplossing 4: de twee advertentiegroepen samenvoegen

Retarget krijgt 25,69 van de 301,18 euro, 8,5 procent. Te weinig om iets te doen, en het splitst wel het conversiesignaal. Samenvoegen of stoppen.

Controleer ook of het budget op campagneniveau staat (CBO) of op groepsniveau (ABO). Bij CBO schuift Meta geld naar de best presterende groep en bouw je sneller signaal op. In Metricool stonden zowel dagbudget als lifetime budget leeg op de campagneregel, wat op ABO wijst.

### Oplossing 5: Conversions API naast de pixel

Browsers en iOS blokkeren een deel van de pixelmetingen. Met de Conversions API meet je server-side mee en zie je meer leads. Dat helpt twee keer: Meta krijgt meer signaal om op te optimaliseren, en de rapportage klopt beter.

### Oplossing 6: nieuwe creatives klaarzetten

Frequentie 3,32 bij een bereik van 10.546. Bij zo'n kleine vijver slijt beeld snel.

### Wat realistisch is over de leerfase

| Situatie | Per lead | 50 per week kost | Per dag |
|---|---|---|---|
| Nu | 15,06 | 753 | 108 |
| Na leeftijdsfix | 8,25 | 413 | 59 |
| Met lead form, schatting | 5,00 | 250 | 36 |

Bij 10 euro per dag komt deze campagne er niet uit, ook niet na alle fixes. **Het doel is dus niet de leerfase verlaten, maar zorgen dat elke euro bij de juiste mensen landt.** Oplossing 1 doet precies dat.

### Vragen voor het bureau

1. Staat Advantage+ Audience aan? Zo ja, weten jullie dat de bovengrens van de leeftijd daarmee een suggestie is en geen grens?
2. 45-plus kostte in dertig dagen 143 euro en leverde 2 leads, 55-plus nul op 76 euro. Waarom loopt dat nog?
3. Waarom sturen we op een gebeurtenis die 4,7 keer per week voorkomt terwijl Meta er 50 wil?
4. Staat het budget op campagne- of op groepsniveau, en waarom die keuze?
5. Retarget krijgt 8,5 procent van het budget. Wat is het plan daarmee?
6. Draait de Conversions API naast de pixel, of alleen de pixel?
7. Onze link-CTR is 1,08 procent terwijl de gewone CTR 2,25 is. Meer dan de helft van de kliks zijn geen link-kliks. Wat doen we daaraan?
8. Frequentie is 3,32 bij een bereik van 10.546. Wanneer komt er nieuw beeld?
9. Is een native lead form overwogen in plaats van het formulier op de site?

## 17 september: advertentiecijfers komen nu ook via de Metricool-koppeling

Lars is naar een betaald Metricool-plan gegaan. Dezelfde opvraging die op 16 september nul rijen gaf, levert nu data:

```
PB - Padellessen leads | besteed 309,92 | bereik 12.072 | leads 20
```

Daarmee is het vermoeden van gisteren bevestigd: advertentierapportage via de API zat achter de planbeperking, niet achter een synchronisatieprobleem.

Werkverdeling vanaf nu:

- **Metricool-koppeling**: campagnetotalen, snel en zonder omweg.
- **Make-tool `ACA Meta Ads inzichten lezen` (7446513)**: uitsplitsingen naar regio, leeftijd en geslacht, en cijfers per advertentiegroep. Die kent de Metricool-koppeling niet.

De MCP-toolset zelf is ongewijzigd door de upgrade: dezelfde negen tools, hetzelfde schema. Foto-tags op Instagram zitten er nog steeds niet in, dat is een eigenschap van de koppeling, niet van het plan.

## 18 september: alle data opnieuw opgehaald, nu ook via Metricool

Lars heeft het betaalde Metricool-plan, dus de koppeling geeft nu wel advertentiedata. Alles opnieuw opgehaald langs twee wegen en tegen elkaar gelegd. Ruwe cijfers staan in `outputs/ads/2026-09-18-meta-ads-ruwe-data.json`.

| Bron | Wat het geeft | Beperking |
|---|---|---|
| Meta Marketing API via Make (tool 7446513) | Campagne, groepen, losse advertenties, leeftijd, geslacht, regio, elke periode | Advertenties zonder naam |
| Metricool-koppeling, `metaAds` | Dagcijfers sinds de start, campagneregel, en per advertentie **met naam en thumbnail** | Loopt 1 tot 2 dagen achter. Zelfde venster gaf 271,70 euro en 14 leads, Meta zelf 294,32 en 18. Geen leeftijd of regio. |

Werkwijze vanaf nu: Meta via Make voor de cijfers, Metricool voor namen, beeld en het dagverloop. Advertenties uit beide bronnen aan elkaar gekoppeld op impressies.

### De campagne, drie vensters

| | Laatste 7 dagen (11 t/m 17 sep) | Laatste 30 dagen (19 aug t/m 17 sep) | Hele looptijd (28 jul t/m 17 sep) |
|---|---|---|---|
| Besteed | 68,43 | 294,32 | 517,13 |
| Impressies | 8.442 | 37.661 | 59.030 |
| Bereik | 3.563 | 11.149 | 15.370 |
| Frequentie | 2,37 | 3,38 | 3,84 |
| Link-kliks | 84 | 398 | 631 |
| Landingspagina's | 66 | 333 | 502 |
| **Leads** | **0** | **18** | **28** |
| Per lead | geen | 16,35 | 18,47 |

### Wat er veranderd is sinds 16 september

**Een week zonder leads.** Van 11 tot en met 17 september is 68 euro uitgegeven, 84 mensen klikten door, 66 landden op de site, niemand schreef zich in. Over de hele looptijd komen er gemiddeld 3,8 leads per week binnen. De kans op een lege week bij dat gemiddelde is ongeveer 2 procent. Dat kan pech zijn, maar in combinatie met een frequentie die over de looptijd naar 3,84 is gekropen is advertentiemoeheid de meest waarschijnlijke verklaring. Het vraagt in elk geval om een blik van het bureau.

**Het venster schoof twee dagen op** en daarmee de cijfers: van 20 naar 18 leads en van 15,06 naar 16,35 per lead. De twee dagen die eraf vielen (17 en 18 augustus) brachten 2 leads, de twee dagen die erbij kwamen (16 en 17 september) nul.

**De CPM is wel echt gedaald.** Weekcijfers uit Metricool:

| Week van | Besteed | Impressies | CPM | CTR |
|---|---|---|---|---|
| 27 jul | 54,27 | 4.704 | 11,54 | 3,23% |
| 3 aug | 70,12 | 6.357 | 11,03 | 2,33% |
| 10 aug | 70,25 | 6.867 | 10,23 | 2,11% |
| 17 aug | 68,39 | 8.828 | 7,75 | 2,15% |
| 24 aug | 72,38 | 8.991 | 8,05 | 2,55% |
| 31 aug | 68,22 | 9.192 | 7,42 | 2,15% |
| 7 sep | 69,39 | 8.253 | 8,41 | 2,10% |
| 14 sep (4 dagen) | 40,71 | 5.359 | 7,60 | 2,13% |

Van 11,50 in de eerste weken naar 7,50 tot 8,40 nu. Dat is het algoritme dat goedkopere plekken vindt, en het is precies de winst die ik op 16 september als "grootste gratis winst" beschreef. Die is dus al deels binnen. Alleen: goedkopere impressies leverden geen extra leads op, want de mensen die ze zien zijn de verkeerde.

### Leeftijd en geslacht, opnieuw

Zelfde beeld als op 16 september, nu op het nieuwe venster.

| Leeftijd | Besteed | % budget | Leads | Per lead |
|---|---|---|---|---|
| 18-24 | 9,03 | 3,1% | 0 | geen |
| 25-34 | 53,64 | 18,2% | 9 | **5,96** |
| 35-44 | 92,80 | 31,5% | 7 | 13,26 |
| 45-54 | 65,99 | 22,4% | 2 | 32,99 |
| 55-64 | 50,17 | 17,0% | 0 | geen |
| 65+ | 22,68 | 7,7% | 0 | geen |

25 tot 44: 146,44 euro, 16 leads, 9,15 per lead. De rest: 147,88 euro, 2 leads, 73,94 per lead. 55-plus: 72,85 euro, nul leads.

Nieuw is de splitsing naar geslacht. Vrouwen 149,77 euro voor 8 leads (18,72), mannen 143,36 voor 10 leads (14,34). Dat ligt dicht bij elkaar. Het beste segment van de hele campagne is **vrouwen 25 tot 34: 6 leads voor 19,21 euro, 3,20 per lead**. Daarna mannen 35 tot 44 met 5 leads voor 42,01 euro (8,40).

### Nieuw: welke advertentie werkt

Er draaien zes creatives in elke groep, twaalf advertenties in totaal. De namen lees ik als T = tekstvariant, F = foto, V = video. Cijfers uit Meta, namen uit Metricool.

| Advertentie | Besteed | Impressies | Link-CTR | Leads | Per lead |
|---|---|---|---|---|---|
| Advantage+ T1F2 | 113,60 | 15.435 | 1,13% | **12** | **9,47** |
| Advantage+ T2V1 | 75,42 | 9.308 | 0,96% | 2 | 37,71 |
| Advantage+ T2F1 | 47,72 | 5.972 | 0,99% | 2 | 23,86 |
| Advantage+ T2F2 | 11,45 | 1.616 | 0,80% | 0 | geen |
| Advantage+ T1F1 | 10,75 | 1.226 | 1,31% | 2 | 5,38 |
| Advantage+ T1V1 | 9,85 | 1.029 | 1,75% | 0 | geen |
| Retarget, alle zes samen | 25,53 | 3.075 | 0,94% | 0 | geen |

Drie dingen springen eruit.

1. **Tekst 1 verslaat tekst 2 ruim.** T1 kreeg 134,20 euro en leverde 14 leads (9,59 per lead). T2 kreeg 134,59 euro en leverde 4 leads (33,65 per lead). Zelfde budget, drie en een half keer minder resultaat.
2. **Foto verslaat video.** De foto-advertenties: 183,52 euro, 16 leads, 11,47 per lead. De video's: 85,27 euro, 2 leads, 42,64 per lead. Meta stuurde 85 euro naar video, ruim een kwart van het budget, voor twee leads.
3. **Meta verdeelt het budget zelf en doet dat maar half goed.** T1F2 krijgt terecht het meeste. Maar T2V1 krijgt 75 euro voor 2 leads terwijl T1F1 met 10,75 euro ook 2 leads haalt. Bij Advantage+ creative kiest Meta op basis van kliks en interactie, en video's scoren daar altijd goed op. Dat is dezelfde val als bij leeftijd: sturen op kliks in plaats van op leads.

De retargetgroep heeft in dertig dagen nul leads opgeleverd op 25,53 euro. Over de hele looptijd zijn alle 28 leads uit de Advantage+ groep gekomen.

### Regio

Flevoland 264,72 euro (89,9 procent), Noord-Holland 29,60. Ongewijzigd, klopt.

### Wat dit betekent voor de vragen aan het bureau

De eerdere acht vragen blijven staan. Hier komen er drie bij, en die zijn concreter omdat we nu per advertentie kunnen kijken.

9. In de laatste zeven dagen zijn er nul leads binnengekomen op 68 euro. Wat is er die week veranderd, en wat gaan jullie doen?
10. Tekst 1 haalt 14 leads voor 134 euro, tekst 2 haalt er 4 voor hetzelfde geld. De foto's halen 16 leads, de video's 2. Waarom draaien tekst 2 en de video's nog?
11. Vrouwen van 25 tot 34 kosten 3,20 per lead, 55-plussers zijn 73 euro kwijt zonder één lead. Als de leeftijdsgrens hard wordt gezet, hoeveel budget schuift er dan naar 25 tot 44?

### Voorbehoud

Achttien leads in dertig dagen, 28 over de looptijd. De patronen (leeftijd, tekst 1 tegen tekst 2, foto tegen video) zijn alle drie groot genoeg om op te sturen. De precieze prijs per lead beweegt met elke lead die erbij komt, dus lees de bedragen als richting, niet als vaste waarde.

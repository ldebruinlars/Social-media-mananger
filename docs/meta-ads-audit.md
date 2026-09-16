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

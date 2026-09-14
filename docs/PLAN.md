# Plan: Claude als social media manager van All Court Academy

Datum: 14 september 2026. Geschreven voor Lars. Dit is het complete verhaal van wat er is gevonden, wat er is geïnstalleerd, wat er nog moet gebeuren en hoe het daarna maandelijks loopt.

## 1. Wat ik heb aangetroffen

### Connectors (al gekoppeld aan je Claude account)

| Connector | Status | Rol in het plan |
|---|---|---|
| Google Drive | verbonden (l.debruin@allcourtacademy.com) | bron van foto's en video's |
| Gmail | verbonden | reacties op leads, mail naar ouders/klanten |
| Canva | verbonden, geen Brand Kit | visuals, stories, carrousels, kids camp designs |
| ChatCut | verbonden | video's knippen naar Reels met ondertitels |
| Higgsfield | verbonden, geen TikTok account gekoppeld | AI-beeld en video, TikTok publiceren |
| Make | verbonden (team "My Team", 20 scenario's) | publiceren naar Instagram en Facebook, insights ophalen |
| Netlify | verbonden | website, niet nodig voor social |

**Wat ontbreekt: een directe koppeling met Meta Business (Instagram en Facebook).** Geen enkele connector in je account kan nu naar Instagram of Facebook posten of statistieken lezen. Daar zit de grootste blokkade, en die los je in tien minuten op (zie stap 4).

### Google Drive

Je Drive bevat bijna alleen spreadsheets (inschrijvingen, reeksen, Playtomic bookings, KNLTB, Papapadel). Aan media vond ik:

- 3 foto's van fotografe Susan (Pittig Bakkie), serie ACA_PoortPadel_29mei en APA 13 mei
- 1 video: Interview_Pablo_final.mp4 (89 MB)
- 1 AI-afbeelding en 3 e-mailbanners

Er is geen map met Poort Padel of All Court Academy video's en foto's. Alles staat in `context/media-inventory.md`.

### Canva

15 designs gevonden, waaronder de complete Kids Camp 2026 shirtserie (met ACA en Poort Padel logo's) en het document "Website ideas/AllCourtAcademy" met al je websiteteksten en de groen/crème huisstijl. Daaruit heb ik de brand style opgebouwd.

### Make

Je Make team heeft 6 connections (Google, Gmail, Moneybird, 2x Mollie) en 20 scenario's die allemaal over inschrijvingen, facturen en betalingen gaan. Er is nog geen Facebook of Instagram connection. De Make apps `instagram-business` (Create a Reel Post, Create a Photo Post, Create a Carousel Post, Get post insights, Get user insights, List post comments) en `facebook-pages` (Publish a Reel, Create a Post with Photos) zijn beschikbaar.

## 2. Welke skills ik heb geïnstalleerd (uit GitHub)

Ik heb de vier beste open-source marketing-skillrepos van 2026 bekeken en per repo alleen de skills gepakt die voor een padelschool nuttig zijn. Alles staat in `.claude/skills/` en werkt zodra je deze repo opent in Claude Code.

| Skill | Bron | Wat het doet voor ACA |
|---|---|---|
| **aca-social-manager** | eigen, geschreven voor jou | de baas van alle andere skills. Kent ACA, Poort Padel, jouw toon, de maandcyclus en de publicatieroutes. Start hier altijd |
| brand-onboarding | stevenflanagan1/social-ai-team | maakt en onderhoudt `context/brand-style.md` |
| content-calendar | social-ai-team | bouwt per maand een planning met per post: doel, pijler, formaat, visual |
| caption-writer | social-ai-team | schrijft captions met hooks, CTA en hashtags, batch per maand |
| social-performance-review | social-ai-team | maandelijkse analyse van bereik, saves, shares, groei, met benchmarks |
| social-creative-designer | social-ai-team | briefings voor AI-visuals (te gebruiken met Higgsfield of Canva) |
| social | coreyhaines31/marketingskills | platformregels, hookformules, carrousel-frameworks, short-form video scripts, social listening |
| content-strategy | marketingskills | welke onderwerpen, welke pijlers, repurposing van 1 video naar 10 posts |
| video | marketingskills | video-productie met AI en tools, Reel-structuur |
| social-instagram | brainbytes-dev/everything-claude-marketing | Reels, carrousels, stories, Instagram SEO, algoritme-signalen |
| social-tiktok | everything-claude-marketing | voor als je TikTok start (jeugd en ouders zitten daar) |
| social-community-building | everything-claude-marketing | van volgers naar community (Papapadel, KNLTB teams, ouders) |
| brand-voice, visual-identity | everything-claude-marketing | tone of voice en huisstijl vastleggen |
| hyper-instagram, hyper-meta-ads | hyperfx-ai/marketing-skills | de exacte Instagram API workflow (container, publish, insights metrics) en Meta Ads strategie. De uitvoerende tools daarin vereisen de Hyper MCP, die je niet hebt. Ik gebruik ze als referentie en voer uit via Make |

Bronnen: [social-ai-team](https://github.com/stevenflanagan1/social-ai-team), [marketingskills](https://github.com/coreyhaines31/marketingskills), [everything-claude-marketing](https://github.com/brainbytes-dev/everything-claude-marketing), [hyperfx marketing-skills](https://github.com/hyperfx-ai/marketing-skills). Licenties staan in `THIRD_PARTY_LICENSES.md`.

Skills die ik bewust niet heb geïnstalleerd: linkedin-writer, x-writer, threads-writer (niet je doelgroep), publisher via Blotato (betaald, Make doet hetzelfde), SEO en cold e-mail skills.

### Plugins en connectors uit de Claude catalogus (optioneel, jij kiest)

| Naam | Type | Waarom wel of niet |
|---|---|---|
| Metricool Social Media Management | connector | inplannen, beste posttijden, analytics voor Instagram en Facebook in één koppeling. Beste alternatief voor Make als je het simpel wilt. Vereist Metricool account |
| Postiz | plugin | zelfde idee, 28 platforms, open source. Vereist Postiz account |
| Marketing (Anthropic) | plugin | brand-review, campaign-plan, performance-report. Overlapt met wat nu geïnstalleerd is |
| Canva plugin | plugin | resize-for-social-media en bulk-create bovenop de Canva connector die je al hebt. Aanrader |
| Supermetrics / Windsor.ai | connector | Meta insights naar Google Sheets. Alleen als je later advertenties gaat draaien |

## 3. Wat er nu in de repo staat

```
.claude/skills/          15 skills (zie tabel)
context/brand-style.md   concept brandprofiel ACA, met open vragen voor jou
context/media-inventory.md   alles wat ik in Drive en Canva vond
context/upcoming-events.md   najaarsreeks, kids camp herfst, KNLTB, Papapadel
context/workflow-status.md   waar we staan
outputs/captions|calendars|reviews   lege mappen, hier komt het werk
docs/PLAN.md             dit document
CLAUDE.md                instructies voor Claude in deze repo
```

## 4. Wat jij moet doen (eenmalig, samen ongeveer 30 minuten)

1. **Meta koppelen in Make** (10 min). Ga naar make.com, Connections, Add, kies "Instagram for Business" en log in met het Facebook account dat beheerder is van de ACA pagina en het Instagram Business account. Doe hetzelfde voor "Facebook Pages". Daarna kan ik de scenario's bouwen en publiceren en insights ophalen zonder dat jij iets hoeft te doen. Voorwaarde: je Instagram moet een Business of Creator account zijn dat gekoppeld is aan een Facebook pagina in Meta Business Suite.
2. **Drive map aanmaken** (5 min). `ACA Social Media` met `01 Inbox`, `02 Klaar`, `03 Gepubliceerd`. Zet er alle telefoonvideo's en de volledige fotoseries van Susan in. Deel de map met het account dat aan Claude gekoppeld is.
3. **Brand style checken** (10 min). Open `context/brand-style.md`, beantwoord de 6 open vragen onderaan. Vooral: je Instagram handle, welke coaches in beeld mogen, en je 3 beste posts tot nu toe.
4. **Meta Business Suite export** (5 min). Insights, Content, laatste 90 dagen, Export. Zet de CSV in `01 Inbox`. Zonder die data kan ik alleen op best practices sturen, met die data kan ik zien wie je nu bereikt.
5. Optioneel: Canva Brand Kit aanmaken met je logo, kleuren en font. Dan kloppen alle visuals automatisch.

## 5. Wat ik daarna voor je doe

**Eenmalig na stap 4**
- Make scenario "ACA Social Publisher": Google Sheet `ACA Content Planning` is de planning. Elke rij met status `goedgekeurd` en een datum in het verleden wordt gepost als Reel, foto of carrousel op Instagram en Facebook. Status gaat naar `gepubliceerd` met de post-id.
- Make scenario "ACA Insights": elke maandag bereik, volgers, profielbezoeken, en per post likes, saves, shares, comments naar de sheet `ACA Insights`. Daarop draait de maandreview.
- Interview_Pablo knippen naar 3 Reels in ChatCut, met ondertitels, 9:16.
- Eerste contentkalender oktober met de herfstvakantie kids camp als campagne.

**Elke maand**
1. Week 1: review vorige maand (`/social-performance-review`), rapport in `outputs/reviews/`.
2. Week 1: kalender nieuwe maand (`/content-calendar`), ongeveer 12 Reels, 4 carrousels, 20 stories.
3. Week 2: alle captions (`/caption-writer`) in één bestand. Jij zet een vinkje bij wat mag.
4. Week 2 tot 4: publiceren via Make. Ik controleer of alles live is gegaan.
5. Doorlopend: comments en DM's die binnenkomen via Make signaleer ik, antwoorden in de toon van de allcourtacademy-emails skill, jij keurt goed.

**Wat ik in de gaten houd (traffic en doelgroep)**
- Bereik per post en welk formaat wint (Reel vs carrousel vs foto).
- Waar je kijkers wonen: doel minimaal 60 procent Almere en omgeving. Zit het bereik verkeerd, dan passen we hashtags, locatietag en posttijd aan.
- Leeftijd en geslacht versus je doelgroepen (beginnende volwassenen, ouders, competitiespelers).
- Profielbezoeken en klikken op de link in bio, en of die omgezet worden naar inschrijvingen in je sheets.
- Volgersgroei per week.

## 6. Wat ik niet kan of niet doe zonder jouw akkoord

- Ik post niets live zonder dat jij de tekst en het beeld hebt goedgekeurd.
- Ik kan de websites allcourtacademy.com, poortpadel.nl en instagram.com niet lezen vanuit deze omgeving (netwerk geblokkeerd). Teksten kwamen uit Canva.
- Advertenties (Meta Ads) start ik niet zelf. Ik maak wel de strategie en de creatives als je dat wilt.
- Kinderen komen alleen in beeld met toestemming van ouders.

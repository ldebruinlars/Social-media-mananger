# Tv-paneel Poort Padel (november 2026)

Op 31 oktober stuurde Lars een foto van het scherm bij Poort Padel: links het Poort Padel logo, een analoge klok, de tijd en "MEET • SMASH • RELAX" op een blauwgroene achtergrond (ongeveer #0091B1), rechts een staand beeld met daaronder een onderschrift van twee regels in wit. De eerdere volledige 16:9 slides (`outputs/tv/2026-11-slides`) passen daar niet in. Lars: "Design moet in deze dimensies komen, de linkerkant met de klok moet blijven."

## Maten (uit de foto gemeten, perspectief gecorrigeerd)

- Scherm 1920 x 1080. Linkerzone met logo en klok tot ongeveer x = 640.
- Beeldvak rechts ongeveer x 985 tot 1575, y 95 tot 835: 590 x 740 px, verhouding ongeveer 4:5 (staand). Onderschrift daaronder tot ongeveer y = 950, gecentreerd op x = 1280.
- Eerste versie: beeld in het bestaande vak plus twee regels onderschrift. Lars (1 nov): liever het beeld groter en geen onderschrift, zodat de tekst op de poster leesbaar is. Mockup nu: beeld 768 x 960 px (4:5) van y 60 tot 1020, gecentreerd op x 1280, zonder onderschrift. Aan te leveren blijft 1080 x 1350 px (4:5), hetzelfde formaat als de feedposts.

## Wat er is gemaakt

- `scripts/gen_posts_tv.py` (in `outputs/posts/2026-11-12/scripts`): zelfde generator als de posts, maar met "Vraag aan de bar · allcourtacademy.com" in plaats van "Link in bio". Output `posts/tv_out`, 29 beelden (s34 niet).
- `scripts/render.py`: mockup van het tv-scherm (klok, logo, tijd, beeldvak, onderschrift) voor alle 36 kandidaten: 29 nieuwe tv-versies plus 7 oudere Metricool-beelden (mc_02 is afgekeurd). De 7 oudere hebben nog "Link in bio" en het Poort Padel logo; die kunnen opnieuw gerenderd worden als Lars ze op tv wil.
- `scripts/build.py` -> `check.html`: keuzepagina, per beeld Op tv / Niet op tv (onderschriftvelden weggehaald op 1 nov). Gepubliceerd als https://claude.ai/artifact/KBZpBxDpnM1BJh2prNR5vi, keuzes in db-collectie `tvcheck2_v1`.
- Zip `ACA_tv_panel_1080x1350.zip` (29 jpg's) via de chat naar Lars, om er eerst één op het scherm te testen.

Beelden staan niet in de repo (.gitignore).

## Derde versie (1 nov): hele rechterkant als ontwerp

Lars wilde geen losse foto in een vak maar een ontwerp dat de rechterkant vult en natuurlijker in het scherm zit. Nieuwe generator `outputs/posts/2026-11-12/scripts/gen_tv_wide.py`: volledig 16:9 beeld van 1920 x 1080, achtergrond in de kleur van het scherm (#0091B1), links 660 px leeg voor klok en logo, rechts een afgerond venster van 1180 x 1000 px (x 700, y 40, hoeken 44 px, zachte schaduw) met foto, donkere verloop onderaan, ACA-logo, kicker, kop, subregel, knop en "Vraag aan de bar · allcourtacademy.com". Output `posts/tv_wide`, 29 beelden. Mockup met klok: `scripts/render_wide.py`. Zip `ACA_tv_breed_1920x1080.zip` naar Lars. Dit werkt alleen als het systeem van Poort Padel een volledig beeld onder de klok kan tonen; anders terug naar de 4:5 versie (`posts/tv_out`). De 7 oudere Metricool-beelden hebben geen brede versie.

## Ronde 2 (1 nov): keuze van Lars en korte teksten

Lars koos op de checkpagina 10 beelden voor tv: k1, k3, j1, s01, s07, s29, s35, s39, v1, w1. Zijn opmerkingen: korte teksten, één regel met actie plus plek ("Meld je kind aan op allcourtacademy.com"), geen "Vraag aan de bar"; Kids Kamp foto's van k1 en k3 omwisselen; jeugdreeks (j1) met de foto van s13 (coach met groepje); toernooien (s07) en Mexicano (s35) betere foto en aanmelden via Playtomic; s35 "Mexicano of King of the Court"; Playtomic-post (s39) alleen via Playtomic, website weglaten; s29 tekst beter ("Lachen én beter worden").

- Teksten en foto's per tv-slide: `outputs/posts/2026-11-12/scripts/tv_posts.json`, generator `gen_tv_final.py` (zelfde venster-opzet, knop met de hele regel, geen label ernaast). Output `posts/tv_final` (10 jpg's, 1920 x 1080).
- Nieuwe foto's: s07 ACA_PoortPadel_29mei-57 (high five met drie spelers), s35 ACA_PoortPadel_29mei-10 (twee spelers na een punt).
- Checkpagina ronde 2 op dezelfde url, db-collectie `tvcheck3_v1`. Zip `ACA_tv_definitief_10.zip` naar Lars.

## Ronde 3 (1 nov): logo-lockup en tekstgrootte voor tv

Lars wilde het Poort Padel logo erbij, rechtsboven als "All Court Academy × Poort Padel", en vroeg om te kijken wat voor tv het beste werkt. Toegepast:
- Lockup rechtsboven in het venster: ACA-logo, ×, Poort Padel wit, 74 px hoog, lichte slagschaduw.
- Tekstgrootte volgens de vuistregel 1 inch letterhoogte per 10 voet kijkafstand (DigitalSignage.com, Signs.com, WMU). Op een 55 inch scherm vanaf 4 à 5 meter: kop 82 à 92 px (kapitaalhoogte ongeveer 38 mm), subregel van 30 naar 40 px, knop van 28 naar 32 px, kicker van 24 naar 28 px. Maximaal 3 à 4 informatie-eenheden per slide (kicker, kop, één regel, één actie), geen lopende tekst.
- Richtlijn per slide 10 tot 15 seconden in beeld; vermeld in de README voor Poort Padel.

# Tv-paneel Poort Padel (november 2026)

Op 31 oktober stuurde Lars een foto van het scherm bij Poort Padel: links het Poort Padel logo, een analoge klok, de tijd en "MEET • SMASH • RELAX" op een blauwgroene achtergrond (ongeveer #0091B1), rechts een staand beeld met daaronder een onderschrift van twee regels in wit. De eerdere volledige 16:9 slides (`outputs/tv/2026-11-slides`) passen daar niet in. Lars: "Design moet in deze dimensies komen, de linkerkant met de klok moet blijven."

## Maten (uit de foto gemeten, perspectief gecorrigeerd)

- Scherm 1920 x 1080. Linkerzone met logo en klok tot ongeveer x = 640.
- Beeldvak rechts ongeveer x 985 tot 1575, y 95 tot 835: 590 x 740 px, verhouding ongeveer 4:5 (staand). Onderschrift daaronder tot ongeveer y = 950, gecentreerd op x = 1280.
- Aan te leveren: beeld 1080 x 1350 px (4:5) plus twee korte regels onderschrift. Dat is hetzelfde formaat als de feedposts, dus die beelden kunnen een op een mee.

## Wat er is gemaakt

- `scripts/gen_posts_tv.py` (in `outputs/posts/2026-11-12/scripts`): zelfde generator als de posts, maar met "Vraag aan de bar · allcourtacademy.com" in plaats van "Link in bio". Output `posts/tv_out`, 29 beelden (s34 niet).
- `scripts/render.py`: mockup van het tv-scherm (klok, logo, tijd, beeldvak, onderschrift) voor alle 36 kandidaten: 29 nieuwe tv-versies plus 7 oudere Metricool-beelden (mc_02 is afgekeurd). De 7 oudere hebben nog "Link in bio" en het Poort Padel logo; die kunnen opnieuw gerenderd worden als Lars ze op tv wil.
- `scripts/build.py` -> `check.html`: keuzepagina, per beeld Op tv / Niet op tv plus onderschrift (2 regels). Gepubliceerd als https://claude.ai/artifact/KBZpBxDpnM1BJh2prNR5vi, keuzes in db-collectie `tvcheck2_v1`.
- Zip `ACA_tv_panel_1080x1350.zip` (29 jpg's) via de chat naar Lars, om er eerst één op het scherm te testen.

Beelden staan niet in de repo (.gitignore).

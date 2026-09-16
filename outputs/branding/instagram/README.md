# Instagram profielfoto ACA

Gemaakt op 15 september 2026 uit het beeldmerk van `aca_logo_white.png`, in de kleuren van allcourtacademy.com.

| Kleur | Hex | Waar |
|---|---|---|
| Navy | #0B1420 | achtergrond |
| Lime | #CCFF00 | beeldmerk |
| Off-white | #F2F2EE | alternatief beeldmerk |

Alle bestanden zijn 1080x1080 PNG. Instagram snijdt ze rond af, het beeldmerk staat binnen de veilige cirkel.

| Bestand | Gebruik |
|---|---|
| 01_navy_lime.png | **profielfoto Instagram en Facebook** (aanrader) |
| 02_navy_gradient.png | zelfde, met zacht verloop |
| 03_navy_glow.png | zelfde, met lichtgloed linksboven |
| 04_navy_lime_ring.png | met dunne limering, ring valt weg op klein formaat |
| 05_lime_navy.png | omgekeerd, sterk voor story highlight covers |
| 06_navy_offwhite.png | wit beeldmerk, voor donkere context |
| mark_lime_transparant.png | beeldmerk los, lime, transparante achtergrond |
| mark_navy_transparant.png | beeldmerk los, navy |
| mark_offwhite_transparant.png | beeldmerk los, off-white |

Advies: 01 als profielfoto op Instagram en Facebook, 05 voor de covers van je story highlights. De losse transparante marks gebruik je als watermerk of in Canva.

Uploaden: Instagram app, profiel, Profiel bewerken, Foto wijzigen. Voor Facebook via Meta Business Suite zodat beide accounts hetzelfde beeld hebben.

## Bijgewerkt 16 september 2026: centrering hersteld

`01_navy_lime.png` centreerde het **omhullende kader** van het beeldmerk. Dat lijkt logisch maar valt verkeerd uit, want de staart van de Q rekt dat kader 70 px naar beneden. Gevolg: de ring hing te hoog en linksonder bleef een dode hoek over.

Gemeten op het bronbestand (714x860):

| Punt | Positie |
|---|---|
| Midden omhullend kader | x 357, y 430 |
| Zwaartepunt van de inkt | x 363, y 360 |
| Midden van de ring | x 357, y 357 |

Het zwaartepunt en het ringmidden vallen samen, het kadermidden zit er 70 px onder. Je oog centreert op de ring, dus daarop centreren we nu.

**`aca_profielfoto_1080.png` is vanaf nu de profielfoto voor Instagram, Facebook en LinkedIn.**

- Ring precies op het midden van het doek
- Ring is 584 px van de 1080, dus 54 procent van de breedte (was 46), daardoor leesbaar op 32 tot 40 px
- Verste punt van de inkt zit 460 px van het midden, de ronde uitsnede snijdt pas op 540, dus 80 px speling
- Werkt in de ronde uitsnede van Instagram en Facebook en in het afgeronde vierkant van LinkedIn

Eén bestand voor alle drie de platforms, ze schalen zelf terug. Zie `_preview_platforms.png`.

De oude 01 t/m 06 blijven staan als achtergrond, maar gebruik ze niet meer als profielfoto.

### Nog open

Lars wil ook een versie met het volledige woordmerk ALL COURT ACADEMY bekijken (bestand ALL_COURT_ACADEMY_LOGO_BLUEGREEN.svg, staat op zijn eigen computer). Zodra dat bestand er is: woordmerk werkt niet in een ronde profielfoto (tekst wordt onleesbaar onder 100 px en de uiteinden vallen buiten de cirkel), wel op de omslagfoto en de LinkedIn-banner.

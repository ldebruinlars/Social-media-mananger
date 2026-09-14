# Website en social check, 14 september 2026

Gedaan met de ChatCut Firecrawl plugin (mijn eigen webfetch wordt in deze omgeving geblokkeerd voor allcourtacademy.com, poortpadel.nl en instagram.com). Instagram en Facebook zelf konden niet gelezen worden: Firecrawl weigert instagram.com en de alternatieve route via een sandbox werd niet toegestaan. Alles hieronder komt van de twee websites en Google.

## allcourtacademy.com: wat goed is

- Duidelijke structuur: Home, Lessen, Kids Kamp, Locaties, Events, All-in Business, Over ons, FAQ, Contact.
- Sterke, consistente boodschap: kleine groepen (max 4), elk niveau, reactie binnen 24 uur, leenracket gratis.
- Meta-tags voor social sharing (og:image, og:title) staan goed op de lessen- en kids-kamp pagina's.
- Facebook domeinverificatie staat erin: er is dus een Meta Business account dat het domein bezit.
- Huisstijl is strak en herkenbaar: lime #CCFF00, navy #0B1420, off-white #F2F2EE, fonts Fraunces en Inter Tight.

## allcourtacademy.com: wat je moet fixen

| Prioriteit | Probleem | Fix |
|---|---|---|
| hoog | **Geen enkele link naar Instagram, Facebook of TikTok op de hele site.** Bezoekers kunnen je socials niet vinden en Google koppelt de accounts niet aan het merk | Voeg iconen toe in de footer en op Contact. Zet ook de handles in de bio's andersom naar de site |
| hoog | `/onze-locaties/poort-padel-almere/` geeft 404 maar staat wel in Google | Maak een redirect naar `/pages/locatie.html` in `_redirects` op Netlify |
| midden | De Home laat een "Tweaks" paneel zien (Variant Odessa/Editorial/Energetic/Minimal, accentkleur). Dat is een ontwikkel-tool die live staat | Verwijder of verberg het paneel in productie |
| midden | Links naar `/pages/faq` en `/pages/contact` zonder `.html` naast links mét `.html` | Kies één vorm, zet Netlify pretty URLs aan |
| midden | og:image ontbreekt op Home, Over ons, Events, Business en Contact | Voeg per pagina een og:image toe (lessen-hero.jpg werkt) |
| laag | Over ons noemt Randy, Stefan, Rutger, Alma. Lessen noemt Pablo, Randy, Joep, Raúl, Lars. De teams verschillen | Eén teamlijst op beide pagina's |
| laag | "Kids Kamp" op de site, "Kids Camp" in Canva en "kidskamp" in Drive | Kies één spelling voor social: **Padel Kids Kamp** (zoals de site) |

## poortpadel.nl over ACA

- Lessenpagina verwijst naar ACA als trainingspartner, met foto's van Lars, Randy en Raúl en de ACA_PoortPadel_29mei serie. Goed voor cross-posten.
- Poort Padel Instagram: @poortpadel, ca. 1.070 volgers (Google snippet). Facebook: pagina "Poort Padel", id 61579258105585.
- Poort Padel hashtags: #PoortPadel #PadelAlmere #IndoorPadel #MeetSmashRelax #NieuwinAlmere.
- KNLTB competitie start november 2026, nieuws via Instagram @poortpadel. Kans: ACA levert de competitietraining content.
- Poort Padel heeft veel bruikbare foto's online (PPSocials serie, DJI drone shot, kennissessie foto's). Vraag Poort Padel om de originelen te delen in de Drive Inbox.

## Instagram en Facebook van ACA

- Geen ACA Instagram gevonden via Google of de sites. Of het account bestaat nog niet, of het is nergens gelinkt. **Lars: handle doorgeven.**
- Zodra Make gekoppeld is aan Instagram for Business en Facebook Pages kan ik het profiel, de posts en de insights wel lezen, zonder scraper.

## Media gevonden op de sites (voor de inventaris)

allcourtacademy.com/assets: logo.png, lessen-hero.jpg, kids-camp-lach-crop-s.jpg, kids-camp-coach-s.jpg, kids-camp-highfive-s.jpg, kids-camp-actie-s.jpg, kids-camp-jongen-s.jpg, kids-camp-pauze-s.jpg.
poortpadel.nl/wp-content/uploads/2026/06: ACA_PoortPadel_29mei-9, ACA_PoortPadel_29mei-38, lars-de-bruin, randy-paeper, PPSocials-3/29/37/39/41/45/53, linkedin-update-1 t/m 6, DJI_20260623123048_0058_D.

Dit zijn web-formaten (max 1600px). Voor Reels en feed wil ik de originelen.

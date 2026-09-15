# Higgsfield prompt gids voor ACA story clips

Voor Lars. Zelf foto's kiezen, zelf genereren. Dit is de samenvatting van de beste video-prompt skills op GitHub (O-Side Media higgsfield-prompt, smixs visual-skills, Square Zero video-prompting, kanno321 director-techniques), toegepast op ACA.

## 1. Instellingen in Higgsfield

| Instelling | Waarde |
|---|---|
| Model | Kling 3.0 Pro, image to video |
| Duur | 10 sec (je knipt later terug naar 6 à 7 sec) |
| Formaat | 9:16, 1080x1920 |
| Sound | uit |
| Enhance prompt | uit (anders herschrijft Higgsfield je prompt) |
| CFG / prompt strength | 0.5 |
| Kosten | 17,5 credits per clip |

Belangrijk: Kling houdt de verhouding van je foto. Een liggende foto wordt een liggende video. Snij de foto dus eerst bij naar 9:16 (Canva of Foto's app) voordat je hem uploadt.

## 2. Welke foto's werken

Goed:
- Eén persoon groot in beeld, scherp, gezicht zichtbaar.
- Actie bevroren midden in de beweging: racket boven het hoofd, uitval naar het net, bal nog in beeld.
- Ruimte in de kijkrichting of slagrichting (de bal moet ergens heen kunnen).
- Rustige achtergrond: glaswand, blauwe baan, weinig mensen.

Slecht:
- Groepsfoto's, veel mensen door elkaar (handen en rackets vervormen).
- Kinderen zonder toestemming van ouders. Nooit animeren.
- Tegenlicht of onscherpe foto's.
- Foto's waar de actie al klaar is (bal is weg, speler staat stil).

## 3. De prompt formule

Structuur (MCSLA): Subject + één actie, dan camera als mechanisme, dan look. Maximaal 60 woorden.

Regels:
1. Beschrijf alleen wat beweegt. De foto bepaalt kleding, baan, licht. Niet herhalen.
2. Eén hoofdactie per clip. Niet "hij slaat, draait, lacht en loopt weg".
3. Positief formuleren. Geen "no text, no logos". Kling leest "text" en "logos" en maakt ze juist. Wil je iets niet, noem het niet.
4. Camera schrijf je als mechanisme, niet als filmterm: "de camera is een gimbal die zijwaarts meebeweegt op heuphoogte", niet "tracking shot".
5. Geen overgangen, slow motion of speed ramps in de prompt. Kling kan dat niet betrouwbaar. Dat doe je in de montage.
6. Eindig met 3 à 5 look woorden: "crisp motion, natural lighting, sharp focus".

Sjabloon:

```
[Persoon in de foto] [doet één actie, 1 à 2 zinnen met een begin en een eind].
The camera is a [gimbal / handheld shot] that [pushes in slowly / dollies backward / tracks sideways] at [chest / hip / net] height.
[Look: 3 tot 5 woorden.]
```

## 4. Camera per soort foto

| Foto | Camera die werkt | Vermijd |
|---|---|---|
| Smash of volley (actie) | Low angle, gimbal pusht langzaam in. Of gimbal tracked zijwaarts mee op heuphoogte. | Whip pan, snelle handheld (wordt blur) |
| Backhand of uitval | Gimbal tracked zijwaarts mee, houdt speler in het midden. | Crane omhoog (speler wordt klein) |
| Portret, lach, coach kijkt in camera | Langzame dolly achteruit op ooghoogte, of langzame push-in op borsthoogte. | Snelle bewegingen |
| Detail (logo op shirt, racket, bal) | Camera trekt terug en tilt omhoog: reveal van de persoon. Werkt het best met een eindframe. | Rack focus, dolly zoom (Kling kan dit niet) |
| Twee spelers, handshake | Gimbal cirkelt langzaam op borsthoogte. | Meer dan één actie |

Wat Kling wel kan: push in, dolly back, pan, tilt, crane, zijwaarts tracken, low angle, langzame orbit.
Wat Kling niet kan: rack focus, dolly zoom (vertigo), speed ramp, split screen, tekst in beeld.

## 5. Start plus eindframe (voor mooie overgangen)

Upload twee foto's: start en einde. Kling animeert ertussen. Werkt alleen als beide foto's dezelfde plek en dezelfde persoon of hetzelfde shirt hebben. Voorbeeld dat vandaag goed uitkwam: start op de close-up van het ACA logo op het shirt, einde op de coach met pet die lacht. Prompt daarbij:

```
Extreme close-up on the embroidered All Court Academy logo on a white shirt. The camera dollies backward and tilts up smoothly along the shirt, revealing a padel coach in a cap on the indoor court; he lifts his head and breaks into a relaxed smile toward the camera. Soft blue court light, natural skin tones, steady gimbal motion, subtle film grain.
```

## 6. Kant en klare prompts

Kopieer en pas de eerste zin aan naar wat er op jouw foto staat.

Smash (speler racket boven hoofd):
```
A padel player is at the top of his overhead smash; he swings the racket down and through the ball with explosive force, his body rotates and he lands on his front foot, eyes following the ball. The camera is a low-angle gimbal that pushes in slowly toward him. Bright indoor court, natural daylight from the roof, crisp detail, realistic motion.
```

Backhand laag:
```
A padel player drives a low backhand; the racket sweeps through the ball, the ball flies toward the net and he recovers upright into a ready stance. The camera is a gimbal that tracks sideways with him at hip height, keeping him centered. Cool blue indoor court, glass walls, clean realistic motion, sharp focus.
```

Volley aan het net:
```
A padel coach lunges toward the net and punches a forehand volley; the ball leaves the racket fast, he lands on his front foot and stays low, eyes on the ball. The camera is a handheld shot at net height that pushes in slightly toward him. Indoor blue court, glass walls, crisp motion, natural lighting.
```

Klaarstaan, split step:
```
A padel player crouches low at the net in ready position; he split-steps, punches a quick forehand volley and resets low, eyes locked ahead. The camera is a handheld shot at net height that pushes in slightly. Indoor court, blue floor, shallow depth of field on the foreground net post, realistic pace.
```

Speler lacht, loopt naar camera (voor "padel is voor iedereen"):
```
A woman in a red dress holds her padel racket and laughs; she looks at the camera, lifts the racket over her shoulder and walks toward the camera with confident energy. The camera dollies backward slowly at eye level, keeping her framed. Soft indoor light, glass court wall behind her, warm natural skin tones, slight film grain.
```

Coach wijst naar camera (uitnodiging, kids kamp of proefles):
```
A coach smiles on the padel court holding his racket; he spins the racket once in his hand, then points it toward the camera with a friendly nod. The camera pushes in slowly at chest height on a gimbal. Bright indoor court, soft daylight from the roof, natural colors, sharp focus.
```

Lars aan de glaswand (bestaande foto ACA_PoortPadel_29mei-32):
```
A padel coach in a black shirt leans at the glass wall and turns his head toward the camera with a confident grin; he spins the racket once in his hand and points it at the lens. The camera is a gimbal at chest height that pushes in slowly. Cool blue court light through the fence, natural skin tones, sharp focus.
```

## 7. Controleren na het genereren

Kijk op deze punten voordat je een clip goedkeurt:
- Handen en racket: vijf vingers, racket blijft één vorm.
- Bal: komt van het racket af, verdwijnt niet in het niets.
- Gezicht: blijft dezelfde persoon, geen smelten in de laatste seconden.
- Logo's op shirts: niet vervormd. Zo ja, knip dat stuk weg in de montage.
- Eerste 6 à 7 seconden zijn meestal het best. De laatste 3 seconden verzinnen vaak dingen.

Mislukt? Maak de prompt korter (één actie), kies een scherpere foto, of probeer een andere camerabeweging. Niet dezelfde prompt opnieuw draaien.

## 8. Montage van een story van 10 seconden

1. Introkaart 1,5 sec: verloop groen naar donker, ACA logo, Poort Padel logo, "PADEL · ALMERE" in lime. Staat klaar als card_intro.png.
2. AI clip 6 à 7 sec.
3. Outrokaart 2 sec: "SCHRIJF JE IN VOOR DE NAJAARSREEKS", pill "LINK IN BIO". Staat klaar als card_outro.png.

In Canva: story sjabloon 1080x1920, kaart als beeld, clip als video, korte fade ertussen. Muziek uit de Instagram bibliotheek bij het plaatsen (dan blijft het rechtenvrij).

## 9. Wat er al klaarstaat in je Higgsfield account

Zeven clips van 15 september (Kling 3.0 Pro, 10 sec, 9:16). Zoek in je Higgsfield generaties op de tijd 10:45:
1. Logo reveal naar coach met pet (start plus eindframe)
2. Smash blauw shirt
3. Backhand rood shirt
4. Klaarstaan wit shirt
5. Speelster rode jurk
6. Coach rood shirt wijst
7. Lars volley zwart shirt

Plus als media: de 8 foto's in 9:16 (logo, volley Lars, klaarstaan, pet lach, backhand rood, smash blauw, speelster rood, coach rood), de twee witte logo's en de intro en outro kaart.

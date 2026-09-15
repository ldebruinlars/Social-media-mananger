# Redactietafel

Live: https://claude.ai/artifact/DkzWG54aMKm8Ky6ouhne7f

Stap 2 in de keten. Hier doet Lars de laatste ronde voordat er iets naar Metricool gaat.

1. Postercheck, beeld en tekst per poster
2. **Redactie**, teksten bijschaven en kiezen welke momenten naar LinkedIn gaan
3. Claude zet het in Metricool als concept
4. Publicatieplanner, groen licht per post

## Wat de pagina doet

Per moment staan drie tekstvelden: Instagram, Facebook en LinkedIn. LinkedIn heeft een schakelaar, standaard uit behalve bij `11_jouw_coach` en `18_teamuitje`, die staan al in Metricool.

Naast LinkedIn staat een label hoe goed het onderwerp bij een zakelijk publiek past:

| Past goed | Past redelijk | Past zwak |
|---|---|---|
| najaarsreeks, waarom padel, eerste les, jouw coach, competitie, teamuitje, vaste plek | samen inschrijven, laatste plekken | geen racket, backhand, smash |

De zwakke drie zijn geschreven vanuit een zakelijke invalshoek (materiaal geregeld, meetbare vooruitgang, techniek in plaats van talent), maar het blijven consumentenonderwerpen. Advies: laat die uit tenzij Lars ze bewust wil.

## Uitlezen

- Collectie `redactie`, per moment een document met `id`, `ig`, `fb`, `li`, `li_aan`, `bijgewerkt`
- `redactie/_status` met `klaar`, `moment` en `naar_linkedin` zodra Lars op de knop drukt
- localStorage-sleutel `aca-redactie-v1`

Lezen met `Artifact action:"read_db"`, collectie `redactie`.

## Bestanden

- `index.html` de pagina zoals gepubliceerd
- `rows.json` de 12 momenten met de drie teksten, de fit en de standaardstand van de schakelaar

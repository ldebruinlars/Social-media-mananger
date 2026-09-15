# Publicatieplanner

Live: https://claude.ai/artifact/86xmviVu8NTuFQ6DPNizCb

De tweede goedkeuring. Stap 1 is de postercheck (beeld en tekst), stap 2 is deze pagina.

Sinds 15 september staan hier alle 26 posts: 12 Instagram, 12 Facebook en 2 LinkedIn, gegroepeerd per datum met een filter per kanaal. Per post kiest Lars Groen licht, Nog wachten of Overslaan.

Keuzes komen in de collectie `publicatie`, met sleutels `ig_`, `fb_` en `li_`. De oude sleutels (kale poster-id's) zijn vervallen, localStorage-sleutel is nu `aca-publicatie-v2`.

- `index.html` de pagina zoals gepubliceerd
- `posts.json` de 26 posts met kanaal, datum, tijd, poster, kop, pijler en caption per kanaal
- gebouwd door de scripts in de scratchpad, brondata staat in docs/kanaalverschillen.md

Bij publiceren gaan `avatar.png` (uit `outputs/branding/instagram/01_navy_lime.png`) en de 12 jpg's uit `outputs/posters/2026-10/` mee als bestanden onder `posters/`.

Keuzes komen binnen in de artifact-collectie `publicatie`, per post een document met `id`, `keuze` en tijdstip. Uitlezen met `Artifact action:"read_db"`.

Alleen posts met groen licht mogen weg. Niets gaat live zonder dat.

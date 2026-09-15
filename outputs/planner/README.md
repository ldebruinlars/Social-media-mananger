# Publicatieplanner

Live: https://claude.ai/artifact/86xmviVu8NTuFQ6DPNizCb

De tweede goedkeuring. Stap 1 is de postercheck (beeld en tekst), stap 2 is deze pagina: de post zoals hij in de feed komt, met datum, tijd en caption. Per post kiest Lars Groen licht, Nog wachten of Overslaan.

- `index.html` de pagina zoals gepubliceerd
- `posts.json` de 12 posts met datum, tijd, poster, kop, knop, pijler en caption

Bij publiceren gaan `avatar.png` (uit `outputs/branding/instagram/01_navy_lime.png`) en de 12 jpg's uit `outputs/posters/2026-10/` mee als bestanden onder `posters/`.

Keuzes komen binnen in de artifact-collectie `publicatie`, per post een document met `id`, `keuze` en tijdstip. Uitlezen met `Artifact action:"read_db"`.

Alleen posts met groen licht mogen weg. Niets gaat live zonder dat.

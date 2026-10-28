# Trainer Lab — Gen 4/5-inspired Character Creator

**Live site:** https://scraxemas.github.io/trainer-lab/

A local-first browser character creator. This public site includes **1,709 modular Gen 4-style PNG components** from [Coffee Cup / Poltergeist's Character Customization Resources](https://eeveeexpo.com/resources/317/), plus the app's own procedural starter art. The original author explicitly permits editing, use and sharing. Credits: **Coffee Cup / Poltergeist**. Portions of the source artist's contribution were derived from Pokémon game sprites; underlying Nintendo / Pokémon rights are not waived.

## Create a character
1. Open the live site; **use the item picker on the left** — you no longer need to scroll to Sprite Vault.
2. Choose a **Sprite type** (Walking, Running, Cycling, or front/back trainer pose) and a female/male body template for overworld sprites.
3. Click **Appearance** to pick a real body/skin base from thumbnails.
4. Click **Hair & face**, **Clothing**, or **Accessories**: all use actual Coffee Cup / Poltergeist sprite thumbnails and immediately apply the selected item to the live trainer. Clothing offers Tops, Bottoms, Outfits and Shoes as available; Accessories offers Hats and Bags.
5. Picking hair or clothing before a base automatically chooses a matching body base. Changing pose/body type clears incompatible parts.
6. Real sprite choices are saved locally in your browser and restored when you reopen the site.
7. Click **Export Sprites** to download the composite PNG sheet. Open **Original starter character options** to access the procedural controls.

The full **Sprite Vault** remains available below for advanced searches, third-party local ZIP/folder imports, and manual frame-grid adjustments.

Use matching subpacks (walking with walking, bike with bike, front trainer art with front trainer art); mismatched frame grids and body bases can cause alignment issues. The original pack contains 256x256, 160x160 and larger sheets and some classification is heuristic.

## Local-only packs
Other sources remain **import-only** and are not hosted:
- [Ultimate Gen 4 overworlds](https://eeveeexpo.com/resources/609/) — explicitly no redistribution.
- [Ultimate Gen 5 overworlds](https://eeveeexpo.com/resources/619/) — explicitly no redistribution.
- [Gen 5 characters in Gen 4 style](https://eeveeexpo.com/resources/370/) — explicitly no redistribution.

ZIP and extracted-folder import works entirely in your browser; your selected packs are not uploaded or saved to our server. Browser imports are held in memory until reload.

## Technical
- App: `index.html` (self-contained HTML/CSS/JS).
- Hosted PNG sprite library: `assets/poltergeist/` including `manifest.json`.
- Safe local manifest builder: `scripts/prep_creator_assets.py`.
- Manually dispatched GitHub Actions workflow: `.github/workflows/import-poltergeist.yml` downloads from the creator's public Google Drive file, extracts, optimizes and uploads sprite PNGs and JSON.
- Deployment: GitHub Pages from `main` / root.
- No ROM images, APKs, game binary files or proprietary packs are included.

This is a fan-made creative tool, not affiliated with Nintendo, The Pokémon Company, or Game Freak. Do not use Pokémon-derived sprite assets commercially without appropriate rights.

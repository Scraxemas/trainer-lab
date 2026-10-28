# Trainer Lab — Gen 4/5-inspired Character Creator

**Live site:** https://scraxemas.github.io/trainer-lab/

A local-first browser character creator. This public site includes **1,709 modular Gen 4-style PNG components** from [Coffee Cup / Poltergeist's Character Customization Resources](https://eeveeexpo.com/resources/317/), plus the app's own procedural starter art. The original author explicitly permits editing, use and sharing. Credits: **Coffee Cup / Poltergeist**. Portions of the source artist's contribution were derived from Pokémon game sprites; underlying Nintendo / Pokémon rights are not waived.

## Create a character
1. Open the site and scroll to **04 / Sprite Vault** or click **Open Sprite Vault** in the header.
2. The built-in Poltergeist sprite collection loads automatically. Search by hairstyle, outfit, color, and body type.
3. Click a **base** sprite and select **Full sprite (replaces starter)**; apply.
4. Add matching **hair, tops, bottoms, shoes, hats, bags** using **Transparent layer (on top)**. Multiple compatible layers can be stacked and replaced.
5. Check frame layout (most of Poltergeist's overworld parts are in 256×256 or 160×160 sheets; portrait assets use larger layouts). Export current pose or a sprite sheet.

Use matching subpacks (walking with walking, bike with bike, front trainer art with front trainer art); mismatched frame grids and gender/body base can cause alignment issues. The category classifier is heuristic and may be wrong for some sprites.

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

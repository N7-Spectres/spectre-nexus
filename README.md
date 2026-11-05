# Spectre Nexus

N7's public hub: YouTube channels, Echo Logic, Soul Keep and the other Spectre Productions projects, in one link for Discord, Twitter, Instagram and YouTube. It replaces the old Beacons page once it goes live.

## Change what it shows

Everything on the page comes from `data.json`:

- `channels`: YouTube channels. `"main": true` marks the one the big button points to.
- `projects`: `status` is `live`, `dev`, `refit` or `concept`. `"show": false` hides a project.
- `socials`: a `null` link shows as "link needed" in the preview and is hidden on the public site.

## Build

```
python3 build.py            # dist/preview.html  (private preview, shows missing links)
python3 build.py --public   # dist/index.html    (the public site)
```

The page is plain HTML, CSS and JS with no dependencies. The pixel deck in the header is drawn on a canvas, and N7's sprite is `assets/n7.png` (from the office repo's character art).

## Going live

Every push to `main` builds `--public` and publishes it with GitHub Pages (`.github/workflows/pages.yml`).
One-time setup: repo **Settings → Pages → Source: GitHub Actions**.
The site lives at https://n7-spectres.github.io/spectre-nexus/

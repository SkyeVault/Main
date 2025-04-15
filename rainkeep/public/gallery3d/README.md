# Arynwood 3D Gallery

Welcome to the Arynwood 3D Gallery — a WebGL-powered, lavender-lit immersive art space built entirely with Three.js, vanilla HTML/JS/CSS, and no bundler. This lightweight virtual environment is deployed via Netlify and designed for creative Web3 storytelling, worldbuilding, and showcasing digital art.

This project is part of Arynwood (https://arynwood.com) — an open-source educational ecosystem focused on blockchain, smart contracts, and metaverse tools for artists, developers, and educators.

## Live Demo

Visit the live gallery:  
https://arynwood.com/gallery3d/

## Features

- No bundlers (Vite/Webpack) required
- Uses modern JavaScript modules (type="module")
- Three.js scene rendered directly via CDN (esm.sh)
- Responsive fullscreen layout
- Designed to be CSP-compliant (safe from unsafe-eval)
- Clean separation of HTML, CSS, and JavaScript

## Project Structure

```
gallery3d/
├── index.html       # Entry point with <canvas> and CSP-safe <script>
├── style.css        # Fullscreen canvas and background styling
└── main.js          # Scene rendering via Three.js & OrbitControls
```

## Important Notes

This project:
- Originally used Vite but ran into build issues and CSP rejections
- Migrated to CDN-based ES modules for full compatibility
- Uses esm.sh to load modules without triggering eval-blocked errors
- Works with strict Content Security Policies

## Deployment Instructions

1. Clone the repo
2. Deploy /gallery3d/ to any static host (Netlify, GitHub Pages, etc.)
3. Ensure your site URL matches the base path (e.g. /gallery3d/)
4. That’s it — no build step needed!

## License

Open-source for educational and creative use.  
Built with love by Lorelei Noble (https://arynwood.com).

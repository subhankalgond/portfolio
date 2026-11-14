# Dynamic Full Stack Developer Portfolio & GSAP Showcase

This repository contains:
1. **The Exact Same Original Website** (`original.html`) — Pristine, fully self-contained recreation of the *GSAP x Webflow* interactive showcase by Off Brand.
2. **The Converted Full Stack Developer Portfolio** (`index.html`) — The exact same website personalized for Subhan Kalgond, Full Stack Developer & Data Science Enthusiast.

---

## 🚀 Quick Start / How to Run

### Option 1: Start with npm (Recommended)
You can run the interactive development server with live reload directly:
```bash
npm run dev
# or
npm start
```
Then open:
- **Portfolio Website**: `http://localhost:3000/` or `http://localhost:3000/index.html`
- **Original Site**: `http://localhost:3000/original.html`
- **Resume**: `http://localhost:3000/resume.html`

### Option 2: Run a Python Server
```bash
python3 -m http.server 8000
```
Then visit:
- Portfolio: `http://localhost:8000/` or `http://localhost:8000/index.html`
- Original Site: `http://localhost:8000/original.html`

### Option 3: Open Directly in Browser
You can open either file directly in any modern browser:
- **Portfolio Website**: Open `index.html`
- **Original GSAP Showcase**: Open `original.html`

> **Note**: Both pages include a sleek floating switcher badge in the top-right corner allowing 1-click toggling between the **Original GSAP Showcase** and the **Full Stack Developer Portfolio**.

---

## 🛠 What Was Done

### Phase 1: In-Depth Analysis of the Workspace Files
The source files consisted of `Gsap X Webflow.html` and the `Gsap X Webflow_files` asset directory containing:
- **GSAP Animation Suite**: Core GSAP, ScrollTrigger, SplitText, ScrollSmoother, Flip, ScrollToPlugin, InertiaPlugin, ScrambleTextPlugin, Observer, Draggable, MotionPathPlugin, MotionPathHelper.
- **Smooth Scroll**: Lenis smooth scroll engine synced to GSAP ticker.
- **31 Visual Assets**: High-resolution AVIF cutouts, layered shadow passes, sky textures, runner sequences, and typography SVGs.
- **Issue Discovered**: The raw HTML was serialized from a live Chrome browser session, containing:
  - 113 DOM nodes with stale `aria-hidden="true"` generated mid-animation by SplitText.
  - Browser extension debris (`#volume-booster-visusalizer`, hidden textareas, audio outputs).
  - Remotely linked fonts and remote videos that would stall if offline.
  - Dynamic overlay proxies injected by Draggable that caused duplicate items in 3D perspective carousels.

### Phase 2: Pristine Recreation of the Original Website (`original.html`)
- **Offline Self-Containment**: Downloaded `WorkSans` (Regular, Medium, SemiBold) and `Anton-Regular` woff2 fonts locally into `Gsap X Webflow_files/`, with Google Fonts fallback.
- **Local Video Integration**: Downloaded the high-res `running.mp4` video locally into `Gsap X Webflow_files/`.
- **DOM Sanitization**: Reconstructed pure string nodes for all SplitText targets (`hero` title, `par` subtext, buttons, `videogrow` title, and text effects triggers).
- **Inertia & Slider Fixes**: Removed stale draggable overlay proxies and reset slide states so 3D cylinder and loop slider calculations run smoothly on startup.
- **Navigation Bar**: Section selector powered by GSAP `Flip` to glide the highlight indicator between tabs (`Flip`, `Scroll Trigger`, `Slider`, `Inertia`, `Text Effects`, `Marquee`).

### Phase 3: Personalization to Subhan Kalgond's Portfolio (`index.html`)
The website was personalized section-by-section to represent Subhan Kalgond (Full Stack Developer & Data Science Enthusiast):

| Section | Original Feature | Personalized Portfolio Feature |
| :--- | :--- | :--- |
| **Top Nav** | Webflow x GSAP Branding | **SUBHAN KALGOND // FULL STACK & DATA SCIENCE** brand badge & smooth internal navigation |
| **Hero (`#hero`)** | Kinetic typography & interactive toggle | **SUBHAN KALGOND** oversized typography, verified biography, and tech skills kinetic strips |
| **Flower Track (`#flower-track`)** | Creative Showcase & Floating Cards | **About Me, Resume, Contact Me** interactive cards with smooth scroll triggers |
| **Projects (`#flip`)** | Interactive cards with visit popouts | **Selected Projects**: CarePulse (Hospital Management), Prahari (AI Crop Disease Detection), FieldNotes, Nova Threads |
| **Journey (`#scrolltrigger`)** | Winding road milestone sequence | **Career & Education Timeline**: Foundations, Self-Learning, B.E. in Data Science (AITM Bhatkal), Key Projects, ML Intern (My Job Grow), Future Vision |
| **Services (`#services`)** | Neo-brutalist interactive service cards | **Core Services**: Website Development, Full-Stack Development, Machine Learning & Data Analysis, UI/UX, Software Engineering |
| **Contact (`#contact`)** | Interactive form & eye-tracking mascot | **Get in Touch**: Subhan Kalgond social cards (Email, Portfolio, LinkedIn, GitHub) & contact form |
| **Footer** | Giant animated footer typography | **SUBHAN KALGOND** signature typography with copy tech stack actions |

---

## 📂 File Architecture
```
Dynamic Portfolio Website/
├── index.html                   # Personalized Developer Portfolio (Subhan Kalgond)
├── resume.html                  # Matching Neo-Brutalist Developer Resume (Subhan Kalgond)
├── original.html                # Exact identical recreation of the original GSAP showcase
├── Gsap X Webflow.html          # Original unmodified browser-saved HTML
├── Gsap X Webflow_files/        # All local styles, scripts, fonts, images, and video
│   ├── gsap.min.js              # GSAP Core
│   ├── ScrollTrigger.min.js     # ScrollTrigger plugin
│   ├── SplitText.min.js         # SplitText plugin
│   ├── Flip.min.js              # Flip plugin
│   ├── InertiaPlugin.min.js     # InertiaPlugin
│   ├── Draggable.min.js         # Draggable plugin
│   ├── ScrambleTextPlugin.min.js# ScrambleText plugin
│   ├── lenis.min.js             # Lenis smooth scroll
│   ├── Anton-Regular.woff2      # Local Anton heading font
│   ├── WorkSans-*.woff2         # Local Work Sans body fonts
│   ├── running.mp4              # Local video asset
│   └── *.avif                   # Cutouts, textures, and illustration passes
├── build_portfolio.py           # Generator script for portfolio adaptation
├── update_portfolio.py          # Refinement and interactive copy handler script
└── README.md                    # Project documentation
```


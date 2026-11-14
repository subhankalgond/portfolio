import re

with open('original.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update Title and Meta Tags
html = html.replace('<title>Gsap X Webflow</title>', '<title>Alex Morgan — Full Stack Developer & System Architect</title>')
html = re.sub(r'<meta content=\"[^\"]*\" name=\"description\">', '<meta content=\"Portfolio of Alex Morgan — Full Stack Developer & System Architect. Building scalable distributed systems, cloud architectures, and fluid interactive web applications.\" name=\"description\">', html)
html = re.sub(r'<meta content=\"Gsap X Webflow\" property=\"og:title\">', '<meta content=\"Alex Morgan — Full Stack Developer & System Architect\" property=\"og:title\">', html)
html = re.sub(r'<meta content=\"Gsap X Webflow\" name=\"twitter:title\">', '<meta content=\"Alex Morgan — Full Stack Developer & System Architect\" name=\"twitter:title\">', html)

# 2. Update switcher banner for index.html
original_switcher = '''<div class="site-switcher-banner">
  <span>Original GSAP Showcase</span>
  <span>•</span>
  <a href="index.html">Switch to Full Stack Portfolio ➔</a>
</div>'''

portfolio_switcher = '''<div class="site-switcher-banner">
  <span style="display:inline-block; width:8px; height:8px; border-radius:50%; background:#10CD00; box-shadow:0 0 8px #10CD00;"></span>
  <span style="color:#fff; font-weight:600;">Full Stack Portfolio</span>
  <span style="opacity:0.4;">•</span>
  <a href="original.html" style="color:#a3e635; text-decoration:none; display:flex; align-items:center; gap:4px;">
    <span>Original GSAP Showcase</span>
    <span>↗</span>
  </a>
</div>'''

html = html.replace(original_switcher, portfolio_switcher)

# 3. Enhance Top Nav Brand / Header
nav_brand_original = '''<div class="logo-banner-w"><svg xmlns="http://www.w3.org/2000/svg" width="100%" viewBox="0 0 101 17" fill="none" class="svg _wf-logo">'''
nav_brand_new = '''<div class="logo-banner-w" style="display:flex; align-items:center; gap:16px;">
  <a href="#hero" style="text-decoration:none; color:inherit; display:flex; align-items:center; gap:10px;">
    <span style="font-family:'Anton',sans-serif; font-size:22px; letter-spacing:0.04em; color:currentColor; text-transform:uppercase;">ALEX MORGAN</span>
    <span style="font-family:'Worksans',sans-serif; font-size:10px; font-weight:600; padding:3px 8px; border-radius:99px; background:rgba(16,205,0,0.18); border:1px solid rgba(16,205,0,0.35); color:#10CD00; letter-spacing:0.06em; text-transform:uppercase;">FULL STACK DEV</span>
  </a>
  <div class="x-divider" style="opacity:0.3;">/</div>
  <svg xmlns="http://www.w3.org/2000/svg" width="100%" viewBox="0 0 101 17" fill="none" class="svg _wf-logo">'''

html = html.replace(nav_brand_original, nav_brand_new, 1)

# 4. Update Sub-Nav tab labels
html = html.replace('<div>Flip</div>', '<div>Stack</div>')
html = html.replace('<div>Scroll Trigger</div>', '<div>Architecture</div>')
html = html.replace('<div>Slider</div>', '<div>Projects</div>')
html = html.replace('<div>Inertia</div>', '<div>Experience</div>')
html = html.replace('<div>Text Effects</div>', '<div>Principles</div>')
html = html.replace('<div>Marquee</div>', '<div>Ecosystem</div>')

# 5. Update Hero Section
# Title
hero_orig_title = '<h1 data-hero="title" class="font-c hero-text"><span class="main-he-span">MAKE IT MEAN</span><span class="main-he-span">MORE WITH GSAP</span></h1>'
hero_new_title = '<h1 data-hero="title" class="font-c hero-text"><span class="main-he-span">BUILDING FULL STACK</span><span class="main-he-span">DIGITAL EXPERIENCES</span></h1>'
html = html.replace(hero_orig_title, hero_new_title)

# Paragraph
hero_orig_par = '<div data-hero="par" class="par-base _w-ch">Well, not just because GSAP, let’s dive into why, how and when to incorporate motion design into your websites, with some cloneable templates along the way to get you started</div>'
hero_new_par = '<div data-hero="par" class="par-base _w-ch">Architecting resilient cloud-native backends, sub-second distributed databases, and fluid interactive user interfaces. Combining deep system design with pixel-level frontend engineering.</div>'
html = html.replace(hero_orig_par, hero_new_par)

# Button
hero_orig_btn = '<a data-module="btn" href="#flip" class="btn-link w-inline-block"><div class="overflow"><div>Explore templates</div></div></a>'
hero_new_btn = '<a data-module="btn" href="#slider" class="btn-link w-inline-block"><div class="overflow"><div>View Featured Projects</div></div></a>'
html = html.replace(hero_orig_btn, hero_new_btn)

# Stripes text in Hero
html = html.replace('<div class="hero-stripe-text">SCROLL INTERACTIONS</div>', '<div class="hero-stripe-text">REACT 19 • NEXT.JS 15 • TYPESCRIPT • TAILWIND CSS • GSAP</div>')
html = html.replace('<div class="hero-stripe-text">TEXT&nbsp;EFFECTS</div>', '<div class="hero-stripe-text">NODE.JS • FASTAPI • PYTHON • GO • GRAPHQL • REST APIS</div>')
html = html.replace('<div class="hero-stripe-text">SLIDERS</div>', '<div class="hero-stripe-text">POSTGRESQL • REDIS • MONGODB • PRISMA • DOCKER • K8S</div>')
html = html.replace('<div class="hero-stripe-text">Inertia Inertia</div>', '<div class="hero-stripe-text">AWS CLOUD • TERRAFORM • CI/CD • DISTRIBUTED SYSTEMS</div>')
html = html.replace('<div class="hero-stripe-text">MARQUEES</div>', '<div class="hero-stripe-text">KAFKA • WEBSOCKETS • MICROSERVICES • ZERO-TRUST</div>')

# 6. Update Flip Section (#flip)
# Item 01
html = html.replace('<h3 class="font-c size-md _w-ch">Hover States</h3>', '<h3 class="font-c size-md _w-ch">Frontend Architecture</h3>')
# Item 02
html = html.replace('<h3 class="font-c size-md _w-ch">ResizinG Elements</h3>', '<h3 class="font-c size-md _w-ch">Backend Engineering</h3>')
# Item 03
html = html.replace('<h3 class="font-c size-md _w-ch">Timeline Control</h3>', '<h3 class="font-c size-md _w-ch">Data & Distributed Storage</h3>')
# Item 04
html = html.replace('<h3 class="font-c size-md _w-ch">Shuffling positions</h3>', '<h3 class="font-c size-md _w-ch">Cloud & DevOps Infra</h3>')
# Item 05
html = html.replace('<h3 class="font-c size-md _w-ch">Sequenced Motion</h3>', '<h3 class="font-c size-md _w-ch">Real-Time Event Streams</h3>')
# Item 06
html = html.replace('<h3 class="font-c size-md _w-ch">FLEXIBLE LAYOUTS</h3>', '<h3 class="font-c size-md _w-ch">Security & Performance</h3>')

# Flip Explainer text
flip_explainer_target = 'Make Show and Tell Flexible'
flip_explainer_sub = 'Create seamless transitions between two visual states smoothly, not instantly. It removes the visual chaos when layouts shift, making things feel smooth, considered, and intentional.'

html = html.replace(flip_explainer_target, 'Engineered for Scalability & Fluidity')
html = html.replace(flip_explainer_sub, 'Modern web applications require seamless synergy between frontend finesse and backend resilience. Every service is architected to scale effortlessly while delivering sub-50ms responses and delightful user interactions.')

# 7. Update ScrollTrigger Section (#scrolltrigger)
# Title
html = html.replace('<div data-videogrow="title" class="font-c size-screen overflow-cut">Scrolltrigger</div>', '<div data-videogrow="title" class="font-c size-screen overflow-cut">System Architecture</div>')

# Explainer
html = html.replace('Scroll with purpose', 'High-Throughput Distributed Systems')
html = html.replace('Start animations when elements enter the viewport, scrub through timelines, pin elements in place, or snap to key points as users scroll.', 'Handling 100k+ events/sec with predictable sub-50ms p99 latency. Implemented using distributed event streams, multi-tier caching topologies, and automated fault recovery.')

# 8. Update Slider Section (#slider)
# Slide 1
html = html.replace('<div style="touch-action: pan-y;">Precise</div>', '<div style="touch-action: pan-y;">Next.js • FastAPI • LangChain</div>')
html = html.replace('<h3 class="font-c size-md" style="touch-action: pan-y;">ACTIONS</h3>', '<h3 class="font-c size-md" style="touch-action: pan-y;">NEXUS AI</h3>')
html = html.replace('<div style="touch-action: pan-y;">GSAP turns clicks into vivid stories with precise motion, making every interaction feel intentional and alive.</div>', '<div style="touch-action: pan-y;">Collaborative multi-modal AI platform with streaming LLM agents, vector semantic search, and real-time interactive canvas.</div>')

# Slide 2
html = html.replace('<div style="touch-action: pan-y;">Focus</div>', '<div style="touch-action: pan-y;">React • Go • ClickHouse</div>')
html = html.replace('<h3 class="font-c size-md" style="touch-action: pan-y;">ATTENTION</h3>', '<h3 class="font-c size-md" style="touch-action: pan-y;">PULSE METRICS</h3>')
html = html.replace('<div style="touch-action: pan-y;">GSAP sharpens focus with smooth animations, drawing attention to your message for a lasting, memorable impact.</div>', '<div style="touch-action: pan-y;">Real-time analytics engine visualizing 100k+ events/second with sub-second aggregate OLAP queries and 60fps canvas graphs.</div>')

# Slide 3
html = html.replace('<div style="touch-action: pan-y;">Expressive</div>', '<div style="touch-action: pan-y;">TypeScript • Docker • K8s</div>')
html = html.replace('<h3 class="font-c size-md" style="touch-action: pan-y;">Motion</h3>', '<h3 class="font-c size-md" style="touch-action: pan-y;">DEVFLOW IDE</h3>')
html = html.replace('<div style="touch-action: pan-y;">GSAP infuses elements with expressive motion, transforming static pages into emotional, engaging journeys.</div>', '<div style="touch-action: pan-y;">Browser-based development environment with instant container spins, collaborative live editing, and terminal WebSockets.</div>')

# Slide 4
html = html.replace('<div style="touch-action: pan-y;">Powerful</div>', '<div style="touch-action: pan-y;">Rust WASM • IndexedDB</div>')
html = html.replace('<h3 class="font-c size-md" style="touch-action: pan-y;">IMPACT</h3>', '<h3 class="font-c size-md" style="touch-action: pan-y;">HYPERSYNC DB</h3>')
html = html.replace('<div style="touch-action: pan-y;">GSAP delivers punchy, purpose-driven animations that cut through the noise, driving real, measurable engagement.</div>', '<div style="touch-action: pan-y;">Local-first synchronization engine providing conflict-free CRDT data replication with automatic multi-peer convergence.</div>')

# Slide 5
html = html.replace('<div style="touch-action: pan-y;">Seamless</div>', '<div style="touch-action: pan-y;">Next.js • GraphQL • Stripe</div>')
html = html.replace('<h3 class="font-c size-md" style="touch-action: pan-y;">FLOW</h3>', '<h3 class="font-c size-md" style="touch-action: pan-y;">AETHER COMMERCE</h3>')
html = html.replace('<div style="touch-action: pan-y;">GSAP weaves seamless transitions, guiding users naturally through pages and narratives without visual interruption.</div>', '<div style="touch-action: pan-y;">Global edge-rendered headless e-commerce platform processing $15M+ annual GMV with sub-second checkout and 99.99% uptime.</div>')

# Slider Explainer
html = html.replace('Sliders with purpose', 'Featured Production Applications')
html = html.replace('Interactive sliders that guide users through key concepts, products or stories with effortless physics.', 'Production web platforms designed and deployed with scalable microservices, clean modular codebases, and thoughtful user experiences.')

# 9. Update Inertia Section (#inertia)
html = html.replace('Feel the inertia', '8+ Years of Engineering Impact')
html = html.replace('Continue movement from a given speed, slow naturally to a stop. Perfect for adding physicality and flow to your interface.', 'A proven track record of taking complex software initiatives from ambiguity to high-scale production excellence across startups and enterprise platforms.')

# 10. Update Text Effects Section (#text)
html = html.replace('<div class="text-effect-tx">Split Chars</div>', '<div class="text-effect-tx">Pixel Precision</div>')
html = html.replace('<div>Character Split Reveal</div>', '<div>Sub-pixel craft and 60fps performance on every screen</div>')

html = html.replace('<div class="text-effect-tx">Split By Words</div>', '<div class="text-effect-tx">Clean Architecture</div>')
html = html.replace('<div>Word Split Reveal</div>', '<div>Decoupled, modular codebases designed to evolve</div>')

html = html.replace('<div class="text-effect-tx">Scramble Text</div>', '<div class="text-effect-tx">System Resilience</div>')
html = html.replace('<div>Scramble Text Reveal</div>', '<div>Fault tolerance, 99.99% uptime, automated recovery</div>')

html = html.replace('<div class="text-effect-tx">Split Alpha</div>', '<div class="text-effect-tx">Developer Ergonomics</div>')
html = html.replace('<div>Alpha Reveal</div>', '<div>Strict types, comprehensive tests, frictionless workflows</div>')

html = html.replace('<div class="text-effect-tx">From the Side</div>', '<div class="text-effect-tx">Edge Performance</div>')
html = html.replace('<div>SIide Char Reveal</div>', '<div>Global serverless compute with instant TTFB</div>')

html = html.replace('<div class="text-effect-tx">Up and Down</div>', '<div class="text-effect-tx">User-Centric Focus</div>')
html = html.replace('<div>Up and down Reveal</div>', '<div>Built for speed, accessibility, and real human impact</div>')

# Text Explainer
html = html.replace('Split, animate, reveal', 'Engineering Principles & Tenets')
html = html.replace('Animate each one independently. It’s all motion, no compromise: screen readers and search engines still see the original text.', 'Software engineering is an art of managing complexity. These principles guide every architecture decision, code review, and user experience I construct.')

# 11. Update Marquee Section (#marquee)
html = html.replace('<div class="marquee-line" data-marquee="line"><div class="marquee-text font-c">SCROLLTRIGGER MARQUEE MARQUEE SCROLLTRIGGER</div>', '<div class="marquee-line" data-marquee="line"><div class="marquee-text font-c">TYPESCRIPT • REACT • NEXT.JS • NODE.JS • PYTHON • DOCKER • AWS • GRAPHQL • POSTGRESQL • GSAP • TAILWIND • REDIS</div>')
html = html.replace('<div class="marquee-line _w-img" data-marquee="line"><div class="marquee-text font-c">SCROLLTRIGGER MARQUEE MARQUEE SCROLLTRIGGER</div>', '<div class="marquee-line _w-img" data-marquee="line"><div class="marquee-text font-c">DISTRIBUTED SYSTEMS • MICROSERVICES • EVENT-DRIVEN KAFKA • CLOUD NATIVE • WEBSOCKETS • SYSTEM ARCHITECTURE</div>')

# Marquee Explainer
html = html.replace('Marquees forever', 'The Full Stack Ecosystem')
html = html.replace('Loop endlessly. Stack images, text, or both. Marquees give rhythm to your page without needing a single click.', 'An end-to-end modern software stack carefully chosen for developer velocity, operational stability, and sub-second execution speeds.')

# 12. Update Footer
html = html.replace('Bring your site to life with the power of GSAP, now even more seamlessly in Webflow. This template is your starting point to help you harness the magic of GSAP. No gatekeeping, just a resource at your disposal to start you strong with motion design. Complete with cloneable elements and best-practice tips on when, why and how to use them. Copy what you need, tweak what you like and get building!',
'Building scalable cloud backends and fluid interactive frontends with relentless dedication to craft. Currently open for senior/staff full-stack roles, architecture consulting, and high-impact engineering projects. Let’s connect and create something extraordinary.')

# Footer title / branding
html = html.replace('Off Brand', 'Alex Morgan')
html = html.replace('offbrand.studio', 'alexmorgan.dev')

# 13. Enhanced Copy Functionality in Script 13
# We can enhance btn.onclick to support copying rich content directly to clipboard!
enhanced_copy_js = '''      btn.onclick = async (evt) => {
        try {
          let copyContent = "";
          // Determine contextual copy content based on section
          const parentSec = btn.closest("section");
          const secId = parentSec ? parentSec.id : "";
          
          if (secId === "flip") {
            copyContent = "ALEX MORGAN // FULL STACK TECH STACK\\nFrontend: React 19, Next.js 15, TypeScript, Tailwind, GSAP, WebGL\\nBackend: Node.js, Express, Go, Python (FastAPI), REST, GraphQL, gRPC\\nDatabases: PostgreSQL, Redis, MongoDB, Prisma ORM, Kafka\\nDevOps: Docker, Kubernetes, AWS, Terraform, GitHub Actions\\nContact: alex.morgan.dev@gmail.com";
          } else if (secId === "scrolltrigger") {
            copyContent = "SYSTEM ARCHITECTURE BLUEPRINT\\nThroughput: 100k+ events/sec | P99 Latency: <50ms | Uptime: 99.99%\\nArchitecture: Microservices + Event Sourcing (Kafka) + Edge Invalidation\\nSecurity: Zero-Trust OAuth 2.0 / JWT + Cloudflare WAF\\nArchitect: Alex Morgan (alex.morgan.dev@gmail.com)";
          } else if (secId === "slider") {
            copyContent = "FEATURED FULL STACK PROJECTS — ALEX MORGAN\\n1. Nexus AI Platform (Next.js 15, FastAPI, LangChain, PostgreSQL)\\n2. Pulse Telemetry (React, Go, ClickHouse, WebSockets)\\n3. DevFlow Cloud IDE (TypeScript, Docker, Kubernetes)\\n4. HyperSync DB (Rust WASM, IndexedDB, CRDTs)\\n5. Aether Commerce (Next.js, GraphQL, Stripe, Redis)\\nPortfolio: https://alexmorgan.dev";
          } else if (secId === "inertia") {
            copyContent = "ALEX MORGAN — SENIOR FULL STACK ARCHITECT\\nExperience: 8+ years building enterprise cloud & high-traffic web applications\\nSpecialties: Distributed Systems, Next.js / React, Microservices, Cloud Infra\\nEmail: alex.morgan.dev@gmail.com | GitHub: github.com/alexmorgan-dev";
          } else if (secId === "text") {
            copyContent = "ENGINEERING PRINCIPLES\\n1. Pixel-Perfect Craft (Sub-pixel typography, 60fps animations)\\n2. Decoupled Architecture (Modular, strictly typed, test-driven)\\n3. High Resilience (Fault tolerant, self-healing, 99.99% uptime)\\n4. Developer Ergonomics (Automated CI/CD, comprehensive telemetry)\\n5. Edge Performance (Global serverless caching with sub-50ms TTFB)";
          } else if (secId === "marquee") {
            copyContent = "FULL STACK TOOLKIT: TypeScript, Next.js, React, Node.js, Python, Go, Docker, Kubernetes, AWS, PostgreSQL, Redis, Kafka, GSAP, Tailwind CSS.";
          } else {
            copyContent = "Alex Morgan — Full Stack Developer & Architect (alex.morgan.dev@gmail.com)";
          }

          if (navigator.clipboard && navigator.clipboard.writeText) {
            await navigator.clipboard.writeText(copyContent);
          } else {
            const ta = document.createElement("textarea");
            ta.value = copyContent;
            document.body.appendChild(ta);
            ta.select();
            document.execCommand("copy");
            document.body.removeChild(ta);
          }

          text.textContent = "Copied to Clipboard!";
          setTimeout(() => {
            text.textContent = "Copy this";
          }, 1800);
        } catch (error) {
          console.error("Failed to copy:", error);
          text.textContent = "Copied!";
          setTimeout(() => {
            text.textContent = "Copy this";
          }, 1800);
        }
      };'''

# Replace copy click handler in Script 13
html = re.sub(
    r'btn\.onclick = async \(evt\) => \{.*?text\.textContent = \"Copy this\";\s*\}, 1000\);\s*\}\s*\};',
    enhanced_copy_js,
    html,
    flags=re.DOTALL
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print('Generated index.html successfully! Length:', len(html))

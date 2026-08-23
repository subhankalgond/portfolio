/* ═══════════════════════════════════════════════════
   app.js — Portfolio Interactions
═══════════════════════════════════════════════════ */

// ─── NAV: Scroll shrink + hamburger ───────────────
const nav        = document.getElementById('nav');
const hamburger  = document.getElementById('hamburger');
const mobileMenu = document.getElementById('mobileMenu');

window.addEventListener('scroll', () => {
  nav.classList.toggle('scrolled', window.scrollY > 40);
});

hamburger.addEventListener('click', () => {
  mobileMenu.classList.toggle('is-open');
});

// Close mobile menu on link click
mobileMenu.querySelectorAll('.mobile-menu__link').forEach(link => {
  link.addEventListener('click', () => mobileMenu.classList.remove('is-open'));
});

// ─── SCROLL REVEAL ────────────────────────────────
const revealEls = document.querySelectorAll(
  '.reveal-text, .reveal-fade, .stat-card, .project-card, ' +
  '.service-card, .timeline__item, .testimonial-card, .trusted__logo'
);

const revealObserver = new IntersectionObserver((entries) => {
  entries.forEach((entry, i) => {
    if (entry.isIntersecting) {
      // Stagger siblings
      const siblings = [...entry.target.parentElement.children];
      const idx      = siblings.indexOf(entry.target);
      const delay    = idx * 80;
      setTimeout(() => entry.target.classList.add('is-visible'), delay);
      revealObserver.unobserve(entry.target);
    }
  });
}, { threshold: 0.12, rootMargin: '0px 0px -40px 0px' });

revealEls.forEach(el => revealObserver.observe(el));

// ─── STATS COUNTER ────────────────────────────────
function animateCounter(el, target, duration = 1400) {
  let start     = null;
  const step    = (timestamp) => {
    if (!start) start = timestamp;
    const progress = Math.min((timestamp - start) / duration, 1);
    // Ease out cubic
    const ease     = 1 - Math.pow(1 - progress, 3);
    el.textContent = Math.floor(ease * target);
    if (progress < 1) requestAnimationFrame(step);
    else el.textContent = target;
  };
  requestAnimationFrame(step);
}

const statNumbers = document.querySelectorAll('.stat-card__number');
const statsSection = document.querySelector('.stats');
let statsAnimated = false;

const statsObserver = new IntersectionObserver((entries) => {
  if (entries[0].isIntersecting && !statsAnimated) {
    statsAnimated = true;
    statNumbers.forEach(el => {
      animateCounter(el, parseInt(el.dataset.target, 10));
    });
  }
}, { threshold: 0.3 });

if (statsSection) statsObserver.observe(statsSection);

// ─── ACTIVE NAV LINK ──────────────────────────────
const sections = document.querySelectorAll('section[id]');
const navLinks = document.querySelectorAll('.nav__link');

const activeSectionObserver = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      navLinks.forEach(link => {
        link.classList.toggle(
          'nav__link--active',
          link.getAttribute('href') === `#${entry.target.id}`
        );
      });
    }
  });
}, { threshold: 0.4 });

sections.forEach(s => activeSectionObserver.observe(s));

// ─── TABS SWITCHING ───────────────────────────────
const tabBtns  = document.querySelectorAll('.tabs-bar__btn');
const tabPanels = document.querySelectorAll('.tab-panel');

tabBtns.forEach(btn => {
  btn.addEventListener('click', () => {
    const target = btn.dataset.tab;
    // Update buttons
    tabBtns.forEach(b => b.classList.remove('tabs-bar__btn--active'));
    btn.classList.add('tabs-bar__btn--active');
    // Update panels
    tabPanels.forEach(p => p.classList.remove('tab-panel--active'));
    const panel = document.getElementById(`panel-${target}`);
    if (panel) panel.classList.add('tab-panel--active');
  });
});

// ─── TESTIMONIAL DOTS ─────────────────────────────
// Simple dot click toggle (extend with multiple testimonials later)
const dots = document.querySelectorAll('.dot');
dots.forEach((dot, i) => {
  dot.addEventListener('click', () => {
    dots.forEach(d => d.classList.remove('dot--active'));
    dot.classList.add('dot--active');
  });
});

// ─── PROJECT CARD TILT ────────────────────────────
document.querySelectorAll('.project-card').forEach(card => {
  card.addEventListener('mousemove', (e) => {
    const rect   = card.getBoundingClientRect();
    const x      = (e.clientX - rect.left) / rect.width  - 0.5;
    const y      = (e.clientY - rect.top)  / rect.height - 0.5;
    const tiltX  = (-y * 8).toFixed(2);
    const tiltY  = ( x * 8).toFixed(2);
    card.style.transform = `perspective(600px) rotateX(${tiltX}deg) rotateY(${tiltY}deg) translateY(-6px)`;
  });
  card.addEventListener('mouseleave', () => {
    card.style.transform = '';
  });
});

// ─── CUSTOM CURSOR GLOW (desktop only) ────────────
if (window.matchMedia('(pointer: fine)').matches) {
  const cursor = document.createElement('div');
  cursor.style.cssText = `
    position: fixed; z-index: 9999; pointer-events: none;
    width: 20px; height: 20px; border-radius: 50%;
    background: rgba(200,241,53,0.35);
    transform: translate(-50%,-50%);
    transition: transform 0.08s ease, width 0.2s ease, height 0.2s ease, opacity 0.3s ease;
    mix-blend-mode: screen;
    top: 0; left: 0;
  `;
  document.body.appendChild(cursor);

  document.addEventListener('mousemove', (e) => {
    cursor.style.left = e.clientX + 'px';
    cursor.style.top  = e.clientY + 'px';
  });

  document.querySelectorAll('a, button, .project-card, .service-card').forEach(el => {
    el.addEventListener('mouseenter', () => {
      cursor.style.width  = '48px';
      cursor.style.height = '48px';
      cursor.style.background = 'rgba(200,241,53,0.15)';
    });
    el.addEventListener('mouseleave', () => {
      cursor.style.width  = '20px';
      cursor.style.height = '20px';
      cursor.style.background = 'rgba(200,241,53,0.35)';
    });
  });
}

// ─── SMOOTH ANCHOR SCROLLING ──────────────────────
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
  anchor.addEventListener('click', (e) => {
    const target = document.querySelector(anchor.getAttribute('href'));
    if (target) {
      e.preventDefault();
      const navHeight = parseInt(getComputedStyle(document.documentElement)
        .getPropertyValue('--nav-h'), 10) || 72;
      const top = target.getBoundingClientRect().top + window.scrollY - navHeight;
      window.scrollTo({ top, behavior: 'smooth' });
    }
  });
});

// ─── HERO PARALLAX ────────────────────────────────
const hero = document.querySelector('.hero');
if (hero) {
  window.addEventListener('scroll', () => {
    const scrolled = window.scrollY;
    if (scrolled < window.innerHeight) {
      hero.style.backgroundPositionY = scrolled * 0.3 + 'px';
    }
  }, { passive: true });
}

// Force dark theme as default
document.documentElement.setAttribute('data-theme', 'dark');

console.log('%c✦ Portfolio loaded successfully', 'color: #c8f135; font-size: 14px; font-weight: bold;');

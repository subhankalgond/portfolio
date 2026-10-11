import './style.css';

// Force scroll to top on page refresh
if (history.scrollRestoration) {
    history.scrollRestoration = 'manual';
}
window.scrollTo(0, 0);

// Mobile Navigation Menu Toggle
const menuToggle = document.getElementById('menuToggle');
const header = document.querySelector('.header');
const navLinks = document.getElementById('navLinks');

if (menuToggle && header) {
    const toggleMenu = (open) => {
        const isOpen = open !== undefined ? open : !header.classList.contains('nav-open');
        header.classList.toggle('nav-open', isOpen);
        menuToggle.setAttribute('aria-expanded', String(isOpen));
        
        const textSpan = menuToggle.querySelector('.menu-toggle-text');
        const iconSpan = menuToggle.querySelector('.menu-toggle-icon');
        if (textSpan) textSpan.textContent = isOpen ? 'CLOSE' : 'MENU';
        if (iconSpan) iconSpan.textContent = isOpen ? '✕' : '☰';
    };

    menuToggle.addEventListener('click', (e) => {
        e.stopPropagation();
        toggleMenu();
    });

    // Close on nav item click
    if (navLinks) {
        navLinks.querySelectorAll('a').forEach(link => {
            link.addEventListener('click', () => {
                toggleMenu(false);
            });
        });
    }

    // Close when clicking outside header
    document.addEventListener('click', (e) => {
        if (header.classList.contains('nav-open') && !header.contains(e.target)) {
            toggleMenu(false);
        }
    });

    // Close on Escape key
    document.addEventListener('keydown', (e) => {
        if (e.key === 'Escape' && header.classList.contains('nav-open')) {
            toggleMenu(false);
        }
    });

    // Smooth scroll to top when brand is clicked without # in URL
    const brandLink = document.querySelector('.brand');
    if (brandLink) {
        brandLink.addEventListener('click', (e) => {
            e.preventDefault();
            toggleMenu(false);
            window.scrollTo({ top: 0, behavior: 'smooth' });
            history.pushState(null, '', window.location.pathname);
        });
    }
}

// Scroll Reveal Animation with ultra-smooth early trigger
const revealElements = document.querySelectorAll('.reveal');

const revealOptions = {
    threshold: 0.02,
    rootMargin: "0px 0px 150px 0px"
};

const revealOnScroll = new IntersectionObserver(function(entries, observer) {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.classList.add('active');
            observer.unobserve(entry.target);
        }
    });
}, revealOptions);

revealElements.forEach(el => {
    const rect = el.getBoundingClientRect();
    if (rect.top < window.innerHeight + 200) {
        el.classList.add('active');
    } else {
        revealOnScroll.observe(el);
    }
});

// Header scrolled class toggle
window.addEventListener('scroll', () => {
    if (!header) return;
    if (window.scrollY > 30) {
        header.classList.add('scrolled');
    } else {
        header.classList.remove('scrolled');
    }
});

// Tabs
const tabBtns = document.querySelectorAll('.tab-btn');
const tabContents = document.querySelectorAll('.tab-content');

tabBtns.forEach(btn => {
    btn.addEventListener('click', () => {
        tabBtns.forEach(b => b.classList.remove('active'));
        tabContents.forEach(c => {
            c.classList.remove('active');
            c.style.display = 'none';
        });
        
        btn.classList.add('active');
        const target = document.getElementById(btn.getAttribute('data-target'));
        target.classList.add('active');
        target.style.display = 'block';
    });
});

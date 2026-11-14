import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update Explainer Button Labels
# Section flip
html = re.sub(
    r'(<section id=\"flip\".*?<div class=\"explainer-copy-btn-w\"><button[^>]*><div class=\"btn-cent-w\"><div class=\"text-block\">)Copy this(</div>)',
    r'\1Copy Tech Stack\2',
    html,
    flags=re.DOTALL
)

# Section scrolltrigger
html = re.sub(
    r'(<section id=\"scrolltrigger\".*?<div class=\"explainer-copy-btn-w\"><button[^>]*><div class=\"btn-cent-w\"><div class=\"text-block\">)Copy this(</div>)',
    r'\1Copy Architecture Blueprint\2',
    html,
    flags=re.DOTALL
)

# Section slider
html = re.sub(
    r'(<section id=\"slider\".*?<div class=\"explainer-copy-btn-w\"><button[^>]*><div class=\"btn-cent-w\"><div class=\"text-block\">)Copy this(</div>)',
    r'\1Copy Projects Summary\2',
    html,
    flags=re.DOTALL
)

# Section inertia
html = re.sub(
    r'(<section id=\"inertia\".*?<div class=\"explainer-copy-btn-w\"><button[^>]*><div class=\"btn-cent-w\"><div class=\"text-block\">)Copy this(</div>)',
    r'\1Copy Experience Record\2',
    html,
    flags=re.DOTALL
)

# Section text
html = re.sub(
    r'(<section id=\"text\".*?<div class=\"explainer-copy-btn-w\"><button[^>]*><div class=\"btn-cent-w\"><div class=\"text-block\">)Copy this(</div>)',
    r'\1Copy Engineering Manifesto\2',
    html,
    flags=re.DOTALL
)

# Section marquee
html = re.sub(
    r'(<section id=\"marquee\".*?<div class=\"explainer-copy-btn-w\"><button[^>]*><div class=\"btn-cent-w\"><div class=\"text-block\">)Copy this(</div>)',
    r'\1Copy Full Stack Toolkit\2',
    html,
    flags=re.DOTALL
)

# 2. Update Script 13 to remember originalText
original_script13_restore = 'setTimeout(() => {\n            text.textContent = "Copy this";\n          }, 1800);'
smart_script13_restore = 'setTimeout(() => {\n            text.textContent = originalButtonText;\n          }, 1800);'

# In copybtn inside Script 13:
html = html.replace('const text = btn.children[0].children[0];', 'const text = btn.children[0].children[0];\n      const originalButtonText = text.textContent;')
html = html.replace('text.textContent = "Copy this";', 'text.textContent = originalButtonText;')

# 3. Safeguard loop.next and loop.previous in Slider
html = html.replace('next.addEventListener("click", () => {\n    loop.next(sliderParams);\n  });', 'next.addEventListener("click", () => {\n    if (loop) loop.next(sliderParams);\n  });')
html = html.replace('prev.addEventListener("click", () => {\n    loop.previous(sliderParams);\n  });', 'prev.addEventListener("click", () => {\n    if (loop) loop.previous(sliderParams);\n  });')

# 4. Also add a footer Contact Bar in index.html with interactive links
footer_contact_markup = '''<div class="footer-contact-bar" style="margin-top: 40px; padding: 24px; border: 1px solid rgba(255,255,255,0.12); border-radius: 16px; background: rgba(255,255,255,0.03); display: flex; flex-wrap: wrap; justify-content: space-between; align-items: center; gap: 16px;">
  <div>
    <div style="font-family: 'Anton', sans-serif; font-size: 20px; letter-spacing: 0.05em; text-transform: uppercase;">ALEX MORGAN</div>
    <div style="font-size: 13px; opacity: 0.7; margin-top: 4px;">Full Stack Developer & System Architect • New York / Remote</div>
  </div>
  <div style="display: flex; gap: 12px; flex-wrap: wrap;">
    <a href="mailto:alex.morgan.dev@gmail.com" class="btn" style="text-decoration: none; padding: 10px 18px; border-radius: 999px; background: #10CD00; color: #000; font-weight: 600; font-size: 13px; display: inline-flex; align-items: center; gap: 6px;">
      <span>✉ Email Alex</span>
    </a>
    <a href="https://github.com" target="_blank" rel="noopener" class="btn" style="text-decoration: none; padding: 10px 18px; border-radius: 999px; border: 1px solid rgba(255,255,255,0.25); color: #fff; font-weight: 500; font-size: 13px; display: inline-flex; align-items: center; gap: 6px;">
      <span>GitHub ↗</span>
    </a>
    <a href="https://linkedin.com" target="_blank" rel="noopener" class="btn" style="text-decoration: none; padding: 10px 18px; border-radius: 999px; border: 1px solid rgba(255,255,255,0.25); color: #fff; font-weight: 500; font-size: 13px; display: inline-flex; align-items: center; gap: 6px;">
      <span>LinkedIn ↗</span>
    </a>
  </div>
</div>'''

# Place before closing footer
html = html.replace('</footer>', footer_contact_markup + '\n</footer>')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print('Updated index.html successfully!')

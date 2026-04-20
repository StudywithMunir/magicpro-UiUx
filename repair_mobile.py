file_path = 'c:/Users/dell/Desktop/MagicPro/website.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Bring back the stats grid (.hero-right) on mobile, as it's great for trust.
content = content.replace('.hero-right { display: none; }', '.hero-right { display: block; width: 100%; margin-top: 20px; }')

# 2. Add extra specific mobile optimisations into the 768px block
extra_mobile_css = """
      .nav-ctas .btn-nav-book { display: none; } /* Hide secondary button to keep logo neat */
      .nav-ctas .btn-nav-quote { padding: 8px 16px; font-size: 0.8rem; }
      .hero-card { padding: 24px; }
      .places-list { grid-template-columns: 1fr; } /* Stack new list cleanly */
      .any-place-grid { gap: 30px; }
      .hfy-grid { gap: 16px; }
"""
if '.hero-right { display: block; width: 100%; margin-top: 20px; }' in content:
    # insert extra rules right after it
    css_insert_target = '.hero-right { display: block; width: 100%; margin-top: 20px; }'
    content = content.replace(css_insert_target, css_insert_target + extra_mobile_css)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)
print("Mobile optimization CSS successfully patched.")

import re

kanata_path = r'c:\Users\dell\Desktop\Digitalise-Projects-Antigravity\MagicPro\location-pages\kanata.html'
index_path = r'c:\Users\dell\Desktop\Digitalise-Projects-Antigravity\MagicPro\index.html'

# Update kanata.html
with open(kanata_path, 'r', encoding='utf-8') as f:
    kanata_content = f.read()

# Replace outdoor
kanata_content = re.sub(r'(?i)outdoor', 'property', kanata_content)

# Add to footer Quick Links
kanata_footer_target = """<a href="../quote.html">Get a Quote</a>"""
kanata_footer_replacement = """<a href="../quote.html">Get a Quote</a>
            <a href="kanata.html">Kanata Services</a>"""
if kanata_footer_target in kanata_content and "Kanata Services" not in kanata_content:
    kanata_content = kanata_content.replace(kanata_footer_target, kanata_footer_replacement)

with open(kanata_path, 'w', encoding='utf-8') as f:
    f.write(kanata_content)

# Update index.html
with open(index_path, 'r', encoding='utf-8') as f:
    index_content = f.read()

index_footer_target = """<a href="#map-section" id="footer-contact">Contact</a>"""
index_footer_replacement = """<a href="#map-section" id="footer-contact">Contact</a>
            <a href="location-pages/kanata.html" id="footer-kanata">Kanata Services</a>"""
if index_footer_target in index_content and "Kanata Services" not in index_content:
    index_content = index_content.replace(index_footer_target, index_footer_replacement)

with open(index_path, 'w', encoding='utf-8') as f:
    f.write(index_content)

print("Updated footer and removed outdoor.")

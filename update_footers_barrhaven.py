import re

kanata_path = r'c:\Users\dell\Desktop\Digitalise-Projects-Antigravity\MagicPro\location-pages\kanata.html'
index_path = r'c:\Users\dell\Desktop\Digitalise-Projects-Antigravity\MagicPro\index.html'

# Update kanata.html footer
with open(kanata_path, 'r', encoding='utf-8') as f:
    kanata_content = f.read()

target_kanata = '<a href="kanata.html">Kanata Services</a>'
if target_kanata in kanata_content and "Barrhaven Services" not in kanata_content:
    kanata_content = kanata_content.replace(target_kanata, target_kanata + '\n            <a href="barrhaven.html">Barrhaven Services</a>')

with open(kanata_path, 'w', encoding='utf-8') as f:
    f.write(kanata_content)

# Update index.html footer
with open(index_path, 'r', encoding='utf-8') as f:
    index_content = f.read()

target_index = '<a href="location-pages/kanata.html" id="footer-kanata">Kanata Services</a>'
if target_index in index_content and "Barrhaven Services" not in index_content:
    index_content = index_content.replace(target_index, target_index + '\n            <a href="location-pages/barrhaven.html" id="footer-barrhaven">Barrhaven Services</a>')

with open(index_path, 'w', encoding='utf-8') as f:
    f.write(index_content)

print("Updated footers successfully.")

import re
import os

path = r'c:\Users\dell\Desktop\Digitalise-Projects-Antigravity\MagicPro\location-pages\kanata.html'

with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

# Check for "–" (en dash)
en_dash_matches = re.findall(r'–', content)
if en_dash_matches:
    print(f"Found en-dash '–': {len(en_dash_matches)} times")
    content = content.replace('–', '-')
else:
    print("No en-dash found.")

# Remove any possible "top-tier", "cutting-edge"
buzzwords = ['top-tier', 'cutting-edge', 'state-of-the-art', 'world-class']
for b in buzzwords:
    content = re.sub(b, b.replace('-', ' '), content, flags=re.IGNORECASE)

with open(path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Checked buzzwords and en-dashes.")

import re

path = r'c:\Users\dell\Desktop\Digitalise-Projects-Antigravity\MagicPro\index.html'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

services_match = re.search(r'<section id="services".*?</section>', content, flags=re.DOTALL)
if services_match:
    with open('services_snippet.txt', 'w', encoding='utf-8') as f:
        f.write(services_match.group(0))
    print("Extracted services section.")
else:
    print("Could not find services section.")

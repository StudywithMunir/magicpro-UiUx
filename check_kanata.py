import re
import os

path = r'c:\Users\dell\Desktop\Digitalise-Projects-Antigravity\MagicPro\location-pages\kanata.html'
img_dir = r'c:\Users\dell\Desktop\Digitalise-Projects-Antigravity\MagicPro\Magic Pro Window Cleaning Images'

with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

# Check for "exterior"
exterior_matches = re.findall(r'\bexterior\b', content, flags=re.IGNORECASE)
if exterior_matches:
    print(f"Found 'exterior': {exterior_matches}")
else:
    print("No 'exterior' found.")

# Check for "—"
dash_matches = re.findall(r'—', content)
if dash_matches:
    print(f"Found '—': {len(dash_matches)} times")
else:
    print("No '—' found.")

# Check for images
valid_images = set(os.listdir(img_dir))
image_refs = re.findall(r'src="\.\./Magic Pro Window Cleaning Images/([^"]+)"', content)

broken_images = []
for img in image_refs:
    if img not in valid_images:
        broken_images.append(img)

if broken_images:
    print(f"Broken images: {broken_images}")
else:
    print("All images are valid.")

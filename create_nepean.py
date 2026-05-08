import os
import re

base_dir = r'c:\Users\dell\Desktop\Digitalise-Projects-Antigravity\MagicPro'
barrhaven_path = os.path.join(base_dir, 'location-pages', 'barrhaven.html')
nepean_path = os.path.join(base_dir, 'location-pages', 'nepean.html')
kanata_path = os.path.join(base_dir, 'location-pages', 'kanata.html')
index_path = os.path.join(base_dir, 'index.html')

with open(barrhaven_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace main location names
content = content.replace('Barrhaven', 'Nepean')
content = content.replace('barrhaven.html', 'nepean.html')

# Replace neighborhoods
content = content.replace('Stonebridge', 'Centrepointe')
content = content.replace('Half Moon Bay', 'Craig Henry')
content = content.replace('Chapman Mills', 'Bells Corners')

# Update Map iFrame
barrhaven_iframe = 'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d89851.98687701886!2d-75.7601615!3d45.2731818!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x4cce06c28f805a8b%3A0xe979bf3368aee4b5!2sBarrhaven%2C%20Ottawa%2C%20ON!5e0!3m2!1sen!2sca!4v1714856000000!5m2!1sen!2sca'
nepean_iframe = 'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d89851.98687701886!2d-75.8202569!3d45.3309285!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x4cce0718cc4a6ad7%3A0xc6cc467725843e2b!2sNepean%2C%20Ottawa%2C%20ON!5e0!3m2!1sen!2sca!4v1714856000000!5m2!1sen!2sca'
content = content.replace(barrhaven_iframe, nepean_iframe)

# Fix the footer links in nepean.html
# After replacement, it will have:
# <a href="kanata.html">Kanata Services</a>
# <a href="nepean.html">Nepean Services</a>
# We need to add Barrhaven Services back in.
target_links_nepean = '<a href="kanata.html">Kanata Services</a>\n            <a href="nepean.html">Nepean Services</a>'
new_links_nepean = '<a href="kanata.html">Kanata Services</a>\n            <a href="barrhaven.html">Barrhaven Services</a>\n            <a href="nepean.html">Nepean Services</a>'
content = content.replace(target_links_nepean, new_links_nepean)

with open(nepean_path, 'w', encoding='utf-8') as f:
    f.write(content)

# Update kanata.html and barrhaven.html footer to include nepean.html
def add_nepean_to_location_footer(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        file_content = f.read()
    
    target = '<a href="barrhaven.html">Barrhaven Services</a>'
    if target in file_content and "Nepean Services" not in file_content:
        file_content = file_content.replace(target, target + '\n            <a href="nepean.html">Nepean Services</a>')
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(file_content)

add_nepean_to_location_footer(kanata_path)
add_nepean_to_location_footer(barrhaven_path)

# Update index.html footer
with open(index_path, 'r', encoding='utf-8') as f:
    index_content = f.read()

target_index = '<a href="location-pages/barrhaven.html" id="footer-barrhaven">Barrhaven Services</a>'
if target_index in index_content and "Nepean Services" not in index_content:
    index_content = index_content.replace(target_index, target_index + '\n            <a href="location-pages/nepean.html" id="footer-nepean">Nepean Services</a>')
    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(index_content)

print("Created nepean.html and updated all footers.")

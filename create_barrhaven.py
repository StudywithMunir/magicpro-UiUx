import re

kanata_path = r'c:\Users\dell\Desktop\Digitalise-Projects-Antigravity\MagicPro\location-pages\kanata.html'
barrhaven_path = r'c:\Users\dell\Desktop\Digitalise-Projects-Antigravity\MagicPro\location-pages\barrhaven.html'

with open(kanata_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace main location names
content = content.replace('Kanata', 'Barrhaven')
content = content.replace('kanata.html', 'barrhaven.html')
# Keep kanata footer link pointing to kanata.html, but add barrhaven.
# Wait, replacing kanata.html with barrhaven.html globally will break the kanata footer link.
# Let's fix that afterwards or handle it manually.

# Replace neighborhoods
content = content.replace('Beaverbrook', 'Stonebridge')
content = content.replace('Marchwood', 'Half Moon Bay')
content = content.replace('Katimavik', 'Chapman Mills')

# Update Map iFrame to Barrhaven
kanata_iframe = 'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d89851.98687701886!2d-75.98188151978281!3d45.305626284698525!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x4cd2007ce4591461%3A0xe979bf3368aee4b5!2sKanata%2C%20Ottawa%2C%20ON!5e0!3m2!1sen!2sca!4v1714856000000!5m2!1sen!2sca'
barrhaven_iframe = 'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d89851.98687701886!2d-75.7601615!3d45.2731818!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x4cce06c28f805a8b%3A0xe979bf3368aee4b5!2sBarrhaven%2C%20Ottawa%2C%20ON!5e0!3m2!1sen!2sca!4v1714856000000!5m2!1sen!2sca'
content = content.replace(kanata_iframe, barrhaven_iframe)
content = content.replace('Map of Kanata region', 'Map of Barrhaven region')

# Now the footer link for Kanata would be broken since it was replaced: <a href="barrhaven.html">Barrhaven Services</a>
# Let's add the link to Kanata back to the footer of Barrhaven.
footer_link_barrhaven = '<a href="barrhaven.html">Barrhaven Services</a>'
footer_links_both = '<a href="kanata.html">Kanata Services</a>\n            <a href="barrhaven.html">Barrhaven Services</a>'
content = content.replace(footer_link_barrhaven, footer_links_both)

with open(barrhaven_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Created barrhaven.html successfully.")

import re

def optimize_page(filepath, location_name):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Trust Ribbon
    content = content.replace('5-Star Rated Service', f'5-Star Rated {location_name} Service')
    
    # USPs
    content = content.replace('Authoritative Property Care You Can Trust', f'Authoritative Property Care {location_name} Can Trust')
    
    # Categories
    content = content.replace('Let natural sunlight pour into your living spaces', f'Let natural sunlight pour into your {location_name} living spaces')
    content = content.replace('compromised foundations. We manually remove', f'compromised foundations in {location_name}. We manually remove')
    
    # Process
    content = content.replace('A Proven Process for Perfection', f'A Proven Process for {location_name} Properties')
    
    # Gallery
    content = content.replace('Recent Local Projects', f'Recent {location_name} Projects')
    
    # CTA Banner (handling the previous removal of 'exterior')
    # It might be "Transform Your Home's Property Today" or "Transform Your Home's outdoor Today" (if I replaced exterior with outdoor then property)
    # Let's use regex to find "Transform Your Home's [something] Today" or just "Transform Your Home Today"
    content = re.sub(r'Transform Your Home(?:\'s \w+)? Today', f'Transform Your {location_name} Property Today', content)
    
    # FAQ
    content = content.replace('Expert Answers</h2>', f'Expert Answers for {location_name} Residents</h2>')
    
    # Map
    content = content.replace('Serving Your Neighborhood &amp; Beyond', f'Serving {location_name} &amp; Beyond')
    content = content.replace('Serving Your Neighborhood & Beyond', f'Serving {location_name} & Beyond')

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

kanata_path = r'c:\Users\dell\Desktop\Digitalise-Projects-Antigravity\MagicPro\location-pages\kanata.html'
barrhaven_path = r'c:\Users\dell\Desktop\Digitalise-Projects-Antigravity\MagicPro\location-pages\barrhaven.html'

optimize_page(kanata_path, 'Kanata')
optimize_page(barrhaven_path, 'Barrhaven')

print("Pages locally optimized successfully.")

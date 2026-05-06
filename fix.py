import re
import os

path = r'c:\Users\dell\Desktop\Digitalise-Projects-Antigravity\MagicPro\location-pages\kanata.html'

with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

# Fix broken images
content = content.replace('36-0A4A0669.jpg', '36-0A4A0580.jpg')
content = content.replace('14-0A4A0201.jpg', '14-0A4A0181.jpg')

# Fix AI dashes (em dash)
content = content.replace('—', ' - ')

# Fix exterior (case insensitive, handle capitalization)
def repl_exterior(match):
    word = match.group(0)
    if word.islower():
        return 'outdoor'
    elif word.istitle():
        return 'Outdoor'
    elif word.isupper():
        return 'OUTDOOR'
    return 'outdoor'

content = re.sub(r'\bexterior\b', repl_exterior, content, flags=re.IGNORECASE)

with open(path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Fixed successfully!")

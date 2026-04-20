import re

file_path = 'c:/Users/dell/Desktop/MagicPro/services/window-cleaning.html'
with open(file_path, 'r', encoding='utf-8') as f:
    text = f.read()

# Exact replacements to ensure capitalization and sentence structures remain pristine
replacements = {
    'exterior and interior frames': 'outside and inside frames',
    'interior & exterior residential': 'inside & outside residential',
    'Exterior Windows': 'Outside Windows',
    'Exterior focus': 'Outside focus',
    'exterior glass': 'outside glass',
    'exterior frames': 'outside frames',
    'Interior and Exterior glass': 'Inside and Outside glass',
    'exterior windows?': 'outside windows?',
    '(exterior window cleaning': '(outside window cleaning',
    '(interior & exterior)': '(inside & outside)',
    'exterior cleaning crews': 'professional cleaning crews'
}

for old_str, new_str in replacements.items():
    text = text.replace(old_str, new_str)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(text)

print("All occurrences of 'exterior' successfully replaced.")

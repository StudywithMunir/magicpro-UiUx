file_path = 'c:/Users/dell/Desktop/MagicPro/services/window-cleaning.html'

with open(file_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

output_lines = []
for i, line in enumerate(lines):
    if 'exterior' in line.lower():
        output_lines.append(f"{i+1}: {line.strip()}")

with open('c:/Users/dell/Desktop/MagicPro/exterior_hits.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(output_lines))

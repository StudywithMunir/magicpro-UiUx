file_path = 'c:/Users/dell/Desktop/MagicPro/website.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

target = '@media (max-width: 768px) {'
replacement = '@media (max-width: 768px) {\n      #jump-top { bottom: 100px; right: 24px; left: auto; }'

if '#jump-top { bottom: 100px;' not in content.split('@media (max-width: 768px)')[1][:200]:
    content = content.replace(target, replacement)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)
print("Mobile stack overlap patched.")

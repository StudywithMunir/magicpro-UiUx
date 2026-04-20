import os
import re

def fix_html_files(directory):
    pattern = re.compile(r'\.nav-logo\s*{\s*align-items:\s*center;\s*justify-content:\s*center;')
    replacement = '.nav-logo {'

    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.html'):
                file_path = os.path.join(root, file)
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                if pattern.search(content):
                    print(f"Fixing {file_path}")
                    new_content = pattern.sub(replacement, content)
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(new_content)

if __name__ == "__main__":
    fix_html_files('.')

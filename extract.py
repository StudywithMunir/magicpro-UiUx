import os
import re

file_path = r'c:\Users\dell\Desktop\MagicPro\website.html'
with open(file_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Extract from Hero to Footer
main_content = html.split('<!-- HERO SECTION -->')[1].split('<!-- FOOTER -->')[0]

# Standardize sections so they can be split. The first block is a div (Hero), not a section, so let's handle that.
# Let's split by HTML comments which denote sections perfectly! e.g., <!-- TESTIMONIALS -->
sections_raw = re.split(r'<!--\s*(.*?)\s*-->', main_content)

output = "MAGICPRO HOMEPAGE - EXTRACTED CONTENT (Section by Section)\n"
output += "="*60 + "\n\n"

section_counter = 1
current_title = "HERO SECTION"

def clean_html(text):
    # Extract headers
    text = re.sub(r'<h([1-6])[^>]*>(.*?)</h\1>', lambda m: f"\n\n[H{m.group(1)}] {clean_inner(m.group(2))}\n", text, flags=re.IGNORECASE|re.DOTALL)
    # Extract paragraphs
    text = re.sub(r'<p[^>]*>(.*?)</p>', lambda m: f"\n\n[Paragraph] {clean_inner(m.group(1))}\n", text, flags=re.IGNORECASE|re.DOTALL)
    # Extract links and buttons
    text = re.sub(r'<a[^>]*>(.*?)</a>', lambda m: f"\n[Button/Link] {clean_inner(m.group(1))}\n", text, flags=re.IGNORECASE|re.DOTALL)
    text = re.sub(r'<button[^>]*>(.*?)</button>', lambda m: f"\n[Button/Control] {clean_inner(m.group(1))}\n", text, flags=re.IGNORECASE|re.DOTALL)
    
    # Remove all remaining HTML tags
    text = re.sub(r'<[^>]+>', ' ', text)
    # Replace multiple spaces
    text = re.sub(r' {2,}', ' ', text)
    # Replace multiple newlines
    text = re.sub(r'\n\s*\n', '\n\n', text)
    return text.strip()

def clean_inner(text):
    text = re.sub(r'<br\s*/?>', ' ', text, flags=re.IGNORECASE)
    text = re.sub(r'<[^>]+>', '', text)
    return text.strip()

for i in range(len(sections_raw)):
    block = sections_raw[i].strip()
    if not block: continue
    
    if i % 2 == 1:
        # This is a comment/section title
        current_title = block
    else:
        # This is HTML content
        cleaned_text = clean_html(block)
        
        # Post-clean: We want to catch standalone text (like tags, list items) that didn't get grouped into [Paragraph]
        lines = cleaned_text.split('\n')
        final_lines = []
        for line in lines:
            line = line.strip()
            if not line: continue
            if line.startswith('['):
                final_lines.append(line)
            else:
                final_lines.append(f"[Text Element] {line}")
        
        formatted_text = "\n".join(final_lines)
        if formatted_text:
            output += f"--- SECTION {section_counter}: {current_title.upper()} ---\n"
            output += formatted_text + "\n\n"
            section_counter += 1

target_dir = r"c:\Users\dell\Desktop\MagicPro\final-content.txt"
os.makedirs(target_dir, exist_ok=True)
target_file = os.path.join(target_dir, "homepage.txt")

with open(target_file, "w", encoding='utf-8') as f:
    f.write(output)

print(f"Content cleanly extracted to {target_file}")

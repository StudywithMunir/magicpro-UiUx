import re

file_path = 'c:/Users/dell/Desktop/MagicPro/services/window-cleaning.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# We need to strip out the erroneous Services Section that was accidentally grabbed 
# by the python extraction script.
# It starts at <!-- SERVICES SECTION --> and ends at </section> right before <!-- CTA BANNER -->
pattern = re.compile(r'<!-- SERVICES SECTION -->.*?</section>', re.DOTALL)
content = re.sub(pattern, '', content)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Services section successfully removed from window-cleaning.html")

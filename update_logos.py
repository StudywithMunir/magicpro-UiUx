import re

file_path = 'c:/Users/dell/Desktop/MagicPro/website.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

header_logo_old_1 = """<a href="/" class="nav-logo" id="nav-logo" aria-label="MagicPro Home">
        <div class="logo-icon">🪟</div>
        <div>
          <div class="logo-text">MAGIC<span>PRO</span></div>
          <div class="logo-sub">WINDOW CLEANING</div>
        </div>
      </a>"""

header_logo_old_2 = """<a href="/" class="nav-logo" id="nav-logo" aria-label="MagicPro Home">
        <div class="logo-icon">&#128303;</div>
        <div>
          <div class="logo-text">MAGIC<span>PRO</span></div>
          <div class="logo-sub">WINDOW CLEANING</div>
        </div>
      </a>"""

header_logo_new = """<a href="/" class="nav-logo" id="nav-logo" aria-label="MagicPro Home">
        <img src="Magic-Pro-Logo-New-1024x665.png" alt="MagicPro Window Cleaning" style="height: 52px; width: auto; display: block;" />
      </a>"""

content = content.replace(header_logo_old_1, header_logo_new)
content = content.replace(header_logo_old_2, header_logo_new)

footer_logo_old_1 = """<div class="nav-logo">
            <div class="logo-icon">🪟</div>
            <div>
              <div class="logo-text">MAGIC<span>PRO</span></div>
              <div class="logo-sub" style="color:rgba(255,255,255,0.4)">WINDOW CLEANING</div>
            </div>
          </div>"""

footer_logo_old_2 = """<div class="nav-logo">
            <div class="logo-icon">&#128303;</div>
            <div>
              <div class="logo-text">MAGIC<span>PRO</span></div>
              <div class="logo-sub" style="color:rgba(255,255,255,0.4)">WINDOW CLEANING</div>
            </div>
          </div>"""

footer_logo_new = """<div class="nav-logo" style="margin-bottom: 24px; padding: 12px 18px; background: rgba(255,255,255,0.06); border-radius: 12px; display: inline-block;">
            <img src="Magic-Pro-Logo-New-1024x665.png" alt="MagicPro Window Cleaning" style="height: 56px; width: auto; display: block;" />
          </div>"""

content = content.replace(footer_logo_old_1, footer_logo_new)
content = content.replace(footer_logo_old_2, footer_logo_new)

# Adding padding fix for the header logo so it sits properly instead of flex stretching wrongly
content = content.replace('.nav-logo {', '.nav-logo { align-items: center; justify-content: center;')

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)
print("Logos successfully updated.")

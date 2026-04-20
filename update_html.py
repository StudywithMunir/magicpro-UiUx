import re

file_path = 'c:/Users/dell/Desktop/MagicPro/website.html'
content = ''
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Fix Image Cropping issue by replacing fixed heights with aspect-ratio
content = content.replace('height: 200px;', 'aspect-ratio: 1.5; height: auto;') # for .service-img-wrapper
content = content.replace('height: 260px;', 'aspect-ratio: 16/9; height: auto;') # for hero
content = content.replace('height: 240px;', 'aspect-ratio: 16/9; height: auto;') # for why use
content = content.replace('object-fit: cover;', 'object-fit: cover; object-position: center center;') # Ensure center positioning so tops aren't sliced badly

# 2. Add New Sections HTML after How It Works
how_it_works_end = content.find('</section>', content.find('id="how-it-works"')) + 10

new_html = """

  <!-- NEW SECTION 1: ANY PLACE -->
  <section id="any-place" aria-labelledby="any-place-heading">
    <div class="container">
      <div class="any-place-grid">
        <div class="any-place-text">
          <div class="section-tag">Versatile Cleaning</div>
          <h2 id="any-place-heading">We Will Make Absolutely Any Place Clean, Neat & Tidy.</h2>
          <p>We’ll get your home sparkling: responsibly and sustainably. We use natural cleaning solutions and by-hand clean wherever possible for Hall of Fame results that are kind to the environment.</p>
          <p>We’ll get your home sparkling: responsibly and sustainably. We use natural cleaning solutions and by-hand clean wherever possible for Hall of Fame results that are kind to the environment.</p>
          <a href="/book" class="btn-primary" style="margin-top: 10px;">🎯 BOOK MY CLEANING</a>
        </div>
        <div class="places-list">
          <div class="place-item"><span style="font-size: 1.4rem;">🏠</span> Houses</div>
          <div class="place-item"><span style="font-size: 1.4rem;">🏢</span> Apartment</div>
          <div class="place-item"><span style="font-size: 1.4rem;">🏘️</span> Townhouses</div>
          <div class="place-item"><span style="font-size: 1.4rem;">🏰</span> Estates</div>
          <div class="place-item"><span style="font-size: 1.4rem;">🏗️</span> Renovated buildings</div>
          <div class="place-item"><span style="font-size: 1.4rem;">💼</span> Offices</div>
        </div>
      </div>
    </div>
  </section>

  <!-- NEW SECTION 2: HERE FOR YOU -->
  <section id="here-for-you" aria-labelledby="hfy-heading">
    <div class="container">
      <div class="hfy-header">
        <div class="section-tag dark" style="background: rgba(255,255,255,0.1); color: var(--cyan-bright);">WE HERE FOR YOU</div>
        <h2 id="hfy-heading" class="section-title light">Ottawa Window Cleaning</h2>
        <p class="section-sub light" style="margin: 0 auto;">We are a company dedicated to giving our customers back the time they deserve to enjoy the things they love.</p>
      </div>
      <div class="hfy-grid">
        <div class="hfy-card">
          <h4>Experienced Professional</h4>
          <p>We offers a quality, reliable & professional service you can trust.</p>
        </div>
        <div class="hfy-card">
          <h4>Free Online Quote</h4>
          <p>Fill out our free quote form and we'll get back to you ASAP! Or just call us</p>
        </div>
        <div class="hfy-card">
          <h4>Customer Focused</h4>
          <p>We will provide experienced & well trained cleaning professionals to provide an excellent service & to achieve 100% client satisfaction.</p>
        </div>
        <div class="hfy-card">
          <h4>We Are Committed</h4>
          <p>We offer an operational excellence model, providing a structured & customised cleaning solution to mitigate risk & ensure quality at all times.</p>
        </div>
        <div class="hfy-card" style="grid-column: 1 / -1; max-width: 600px; margin: 0 auto; text-align: center;">
          <h4>Regular & Monthly Cleaning</h4>
          <p>We have a team of highly trained, reliable and friendly staff to offer brilliant cleaning results to suit your individual needs.</p>
        </div>
      </div>
    </div>
  </section>
"""

content = content[:how_it_works_end] + new_html + content[how_it_works_end:]

# 3. Add CSS for new sections
new_css = """
    /* ── NEW SECTIONS ── */
    #any-place { padding: 90px 0; background: var(--off-white); }
    .any-place-grid { display: grid; grid-template-columns: 1.1fr 0.9fr; gap: 60px; align-items: center; }
    #any-place h2 { font-family: 'Outfit', sans-serif; font-size: clamp(2rem, 3vw, 2.5rem); font-weight: 800; color: var(--text-dark); margin-bottom: 24px; line-height: 1.15; }
    .any-place-text p { font-size: 1.05rem; line-height: 1.7; color: var(--text-body); margin-bottom: 20px; }
    .places-list { display: grid; grid-template-columns: 1fr 1fr; gap: 16px; align-content: center; }
    .place-item { display: flex; align-items: center; gap: 12px; background: var(--white); padding: 18px 22px; border-radius: var(--radius-sm); box-shadow: var(--shadow-sm); font-weight: 700; color: var(--text-dark); border-left: 4px solid var(--cyan); transition: transform var(--transition), box-shadow var(--transition); cursor: default; }
    .place-item:hover { transform: translateY(-4px); box-shadow: var(--shadow-md); border-color: var(--cyan-bright); }
    
    #here-for-you { padding: 90px 0; background: linear-gradient(135deg, var(--navy-dark) 0%, var(--navy-mid) 100%); color: var(--white); position: relative; overflow: hidden; }
    #here-for-you::after { content: ''; position: absolute; bottom: -100px; right: -100px; width: 400px; height: 400px; background: radial-gradient(circle, rgba(0,180,216,0.08) 0%, transparent 70%); pointer-events: none; }
    .hfy-header { text-align: center; margin-bottom: 64px; position: relative; z-index: 2; }
    .hfy-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 24px; position: relative; z-index: 2; }
    .hfy-card { background: rgba(255,255,255,0.04); border: 1px solid rgba(255,255,255,0.08); padding: 36px 28px; border-radius: var(--radius-md); transition: transform var(--transition), background var(--transition); text-align: center; }
    .hfy-card:hover { transform: translateY(-5px); background: rgba(0,180,216,0.12); border-color: rgba(0,180,216,0.25); }
    .hfy-card h4 { font-family: 'Outfit', sans-serif; font-size: 1.25rem; color: var(--white); margin-bottom: 14px; }
    .hfy-card p { font-size: 0.92rem; line-height: 1.65; color: rgba(255,255,255,0.65); }
    @media (max-width: 900px) {
      .any-place-grid { grid-template-columns: 1fr; gap: 40px; }
      .hfy-card[style] { grid-column: auto !important; }
    }
"""

css_insert_pos = content.find('/* ── SERVICE AREAS ── */')
if css_insert_pos != -1:
    content = content[:css_insert_pos] + new_css + '\n    ' + content[css_insert_pos:]

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated HTML successfully.")

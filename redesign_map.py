import re

file_path = 'c:/Users/dell/Desktop/MagicPro/website.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Replace the Map CSS
old_css_start = content.find('/* ── MAP SECTION ── */')
old_css_end = content.find('/* ── RESPONSIVE ── */')

if old_css_start != -1 and old_css_end != -1:
    new_css = """
    /* ── MAP SECTION ── */
    #map-section { padding: 90px 0; background: var(--off-white); }
    .map-bento {
      background: var(--white);
      border-radius: 30px;
      overflow: hidden;
      box-shadow: 0 20px 50px rgba(0,0,0,0.06);
      display: grid;
      grid-template-columns: 1fr 1.2fr;
      border: 1px solid rgba(0,0,0,0.04);
    }
    .map-bento-content {
      padding: 64px 50px;
      display: flex;
      flex-direction: column;
      justify-content: center;
    }
    .map-badge {
      display: inline-block;
      background: rgba(0,180,216,0.1);
      color: var(--cyan-bright);
      padding: 6px 16px;
      border-radius: 50px;
      font-size: 0.8rem;
      font-weight: 800;
      letter-spacing: 1px;
      text-transform: uppercase;
      margin-bottom: 20px;
    }
    .map-bento-content h2 { font-family: 'Outfit', sans-serif; font-size: clamp(2rem, 3vw, 2.5rem); color: var(--navy-dark); margin-bottom: 20px; line-height: 1.15; font-weight: 800; }
    .map-bento-content > p { font-size: 1.05rem; color: var(--text-body); margin-bottom: 40px; line-height: 1.6; }
    .map-row { display: flex; align-items: flex-start; gap: 20px; margin-bottom: 30px; }
    .map-icon { font-size: 1.6rem; display: flex; align-items: center; justify-content: center; width: 50px; height: 50px; background: rgba(0,180,216,0.1); border-radius: 14px; position: relative; top: -5px; }
    .map-row-text h4 { font-family: 'Outfit', sans-serif; font-size: 1.15rem; font-weight: 700; color: var(--navy-dark); margin-bottom: 6px; }
    .map-row-text p { color: var(--gray-mid); font-size: 0.95rem; line-height: 1.5; font-weight: 500; }
    .map-iframe-wrapper {
      position: relative;
      width: 100%;
      height: 100%;
      min-height: 500px;
    }
    .map-iframe-wrapper iframe {
      position: absolute;
      top: 0; left: 0;
      width: 100%; height: 100%;
      border: none;
      filter: contrast(1.05) saturate(1.1);
    }
    @media (max-width: 1024px) {
      .map-bento { grid-template-columns: 1fr 1fr; }
      .map-bento-content { padding: 40px; }
    }
    @media (max-width: 900px) {
      .map-bento { grid-template-columns: 1fr; }
      .map-bento-content { padding: 40px 30px; }
      .map-iframe-wrapper { min-height: 400px; }
    }

    """
    content = content[:old_css_start] + new_css + content[old_css_end:]

# 2. Replace the HTML
old_html_start = content.find('<!-- MAP SECTION -->')
old_html_end = content.find('<!-- FOOTER -->')

if old_html_start != -1 and old_html_end != -1:
    new_html = """<!-- MAP SECTION -->
  <section id="map-section" aria-labelledby="map-heading">
    <div class="container">
      <div class="map-bento">
        <!-- Content Side -->
        <div class="map-bento-content">
          <div><span class="map-badge">Locally Owned & Operated</span></div>
          <h2 id="map-heading">Drop By Our Ottawa Headquarters</h2>
          <p>Perfectly situated to dispatch our highly-trained exterior cleaning crews to any neighbourhood in Ottawa with rapid, same-day efficiency.</p>
          
          <div class="map-details">
            <div class="map-row">
              <div class="map-icon">📍</div>
              <div class="map-row-text">
                <h4>Office Location</h4>
                <p>611-230 Woodridge Cres, Nepean,<br>Ottawa, ON K2B 8G2</p>
              </div>
            </div>
            <div class="map-row">
              <div class="map-icon">📞</div>
              <div class="map-row-text">
                <h4>Contact Us Directly</h4>
                <p>+1 613-292-4294<br>info@magicpro.ca</p>
              </div>
            </div>
          </div>
          
          <a href="https://maps.google.com/?q=Magicpro+Window+Cleaning+Ottawa" target="_blank" rel="noopener noreferrer" class="btn-primary" style="display: inline-flex; align-items: center; justify-content: center; gap: 10px;">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polygon points="3 11 22 2 13 21 11 13 3 11"></polygon></svg>
            Get Live Directions
          </a>
        </div>
        <!-- Map Side -->
        <div class="map-iframe-wrapper">
          <iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d359342.1943003921!2d-75.8002569!3d45.28092855!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x4cce0130a83e80db%3A0x5b28f421dfb51862!2sMagicpro%20Window%20Cleaning!5e0!3m2!1sen!2s!4v1776445515582!5m2!1sen!2s" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade" title="MagicPro Office Location"></iframe>
        </div>
      </div>
    </div>
  </section>

  """
    content = content[:old_html_start] + new_html + content[old_html_end:]

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)
print("Map completely redesigned into premium Bento style.")

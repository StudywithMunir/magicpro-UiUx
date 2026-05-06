import re

kanata_path = r'c:\Users\dell\Desktop\Digitalise-Projects-Antigravity\MagicPro\location-pages\kanata.html'
with open(kanata_path, 'r', encoding='utf-8') as f:
    kanata_content = f.read()

# The services snippet to add
services_html = """
  <!-- SERVICES GRID -->
  <section id="services" aria-labelledby="services-heading">
    <div class="container">
      <div class="services-header" style="text-align: center; margin-bottom: 56px;">
        <div class="section-tag">What We Do</div>
        <h2 id="services-heading" class="section-title">Complete Property Maintenance<br />for Kanata Neighborhoods</h2>
        <p class="section-sub" style="margin: 0 auto;">
          From high-reach glass to clogged downspouts, we handle it all. As a trusted local provider of <a href="https://magicpro.ca/" style="color: var(--cyan); text-decoration: underline; font-weight: 600;">Window and Gutter Cleaning Services in Ottawa</a>, we bring our top-rated expertise directly to your Kanata property.
        </p>
      </div>
      <div class="services-grid">
        <article class="service-card" id="service-window-cleaning">
          <div class="service-img-wrapper">
            <img class="service-img" src="../Magic Pro Window Cleaning Images/2-0A4A0035.jpg" alt="Professional window cleaning service in Kanata" loading="lazy" />
          </div>
          <div class="service-content">
            <h3>Window Cleaning</h3>
            <p>Crystal-clear results using professional squeegee systems and streak-free solutions. We service homes, condos, and commercial buildings across the region.</p>
            <a href="../services/window-cleaning.html" class="service-link" style="color: var(--cyan); font-weight: 700;">Learn More →</a>
          </div>
        </article>
        <article class="service-card" id="service-gutter-cleaning">
          <div class="service-img-wrapper">
            <img class="service-img" src="../Magic Pro Window Cleaning Images/6-0A4A0075.jpg" alt="Expert gutter cleaning for Kanata homes" loading="lazy" />
          </div>
          <div class="service-content">
            <h3>Gutter Cleaning</h3>
            <p>Clogged eavestroughs cause water damage and foundation erosion. Our thorough clearing process keeps your drainage system protected year-round.</p>
            <a href="../services/gutter-cleaning.html" class="service-link" style="color: var(--cyan); font-weight: 700;">Learn More →</a>
          </div>
        </article>
        <article class="service-card" id="service-siding-cleaning">
          <div class="service-img-wrapper">
            <img class="service-img" src="../Magic Pro Window Cleaning Images/4-0A4A0053.jpg" alt="Vinyl siding cleaning and restoration Kanata" loading="lazy" />
          </div>
          <div class="service-content">
            <h3>Siding Cleaning</h3>
            <p>Vinyl siding accumulates dirt and stains from seasonal changes. We restore your home's curb appeal safely, without damaging the surface.</p>
            <a href="../services/siding-cleaning.html" class="service-link" style="color: var(--cyan); font-weight: 700;">Learn More →</a>
          </div>
        </article>
        <article class="service-card" id="service-pressure-washing">
          <div class="service-img-wrapper">
            <img class="service-img" src="../Magic Pro Window Cleaning Images/5-0A4A0070.jpg" alt="High-pressure washing for driveways and patios" loading="lazy" />
          </div>
          <div class="service-content">
            <h3>Pressure Washing</h3>
            <p>Driveways, decks, patios, and parking lots: our high-powered pressure washing eliminates years of grime from residential and commercial properties.</p>
            <a href="../services/pressure-washing.html" class="service-link" style="color: var(--cyan); font-weight: 700;">Learn More →</a>
          </div>
        </article>
      </div>
    </div>
  </section>
"""

# The CSS to add for services-grid if not present
services_css = """
    /* ── SERVICES GRID ── */
    #services { padding: 90px 0; background: var(--off-white); }
    .services-grid { display: grid; grid-template-columns: repeat(4, 1fr); gap: 24px; }
    .service-card { background: var(--white); border: 1px solid rgba(0,0,0,0.07); border-radius: var(--radius-md); padding: 0; position: relative; overflow: hidden; transition: transform var(--transition), box-shadow var(--transition), border-color var(--transition); cursor: pointer; }
    .service-card::before { content: ''; position: absolute; top: 0; left: 0; width: 100%; height: 4px; background: linear-gradient(90deg, var(--cyan), var(--cyan-bright)); transform: scaleX(0); transform-origin: left; transition: transform var(--transition); }
    .service-card:hover::before { transform: scaleX(1); }
    .service-card:hover { transform: translateY(-6px); box-shadow: var(--shadow-lg); border-color: rgba(0,180,216,0.2); }
    .service-img-wrapper { width: 100%; aspect-ratio: 1.6; height: auto; overflow: hidden; border-radius: var(--radius-md) var(--radius-md) 0 0; margin-bottom: 0; }
    .service-content { padding: 28px 24px; }
    .service-img { width: 100%; height: 100%; object-fit: cover; transition: transform var(--transition); }
    .service-card:hover .service-img { transform: scale(1.08); }
    .service-card h3 { font-family: 'Outfit', sans-serif; font-size: 1.15rem; font-weight: 700; color: var(--text-dark); margin-bottom: 12px; }
    .service-card p { font-size: 0.9rem; color: var(--gray-mid); line-height: 1.65; margin-bottom: 20px; }
    .service-link { display: inline-flex; align-items: center; gap: 6px; transition: gap var(--transition); }
    .service-link:hover { gap: 10px; }
    @media (max-width: 1024px) { .services-grid { grid-template-columns: repeat(2, 1fr); } }
    @media (max-width: 600px) { .services-grid { grid-template-columns: 1fr; } }
"""

# Inject CSS
if ".services-grid" not in kanata_content:
    kanata_content = kanata_content.replace('/* ── ALTERNATING CATEGORIES ── */', services_css + '\n    /* ── ALTERNATING CATEGORIES ── */')

# Inject HTML after TRUST RIBBON
trust_ribbon_end = kanata_content.find('  <!-- SERVICE BENTO OVERVIEW')
if trust_ribbon_end != -1:
    kanata_content = kanata_content[:trust_ribbon_end] + services_html + '\n' + kanata_content[trust_ribbon_end:]

with open(kanata_path, 'w', encoding='utf-8') as f:
    f.write(kanata_content)

print("Services grid added successfully.")

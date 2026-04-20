import re
import os

with open('c:/Users/dell/Desktop/MagicPro/website.html', 'r', encoding='utf-8') as f:
    orig = f.read()

# EXTRACT COMPONENTS FROM HOMEPAGE
# 1. Head and Global CSS
head_end = orig.find('</head>')
head = orig[:head_end]
head = head.replace('<title>Cleaning Services Ottawa | MagicPro Window & Gutter Cleaning</title>', '<title>Window Cleaning Services Ottawa | MagicPro</title>')
head = head.replace('<meta name="description" content="MagicPro offers trusted cleaning services in Ottawa: window cleaning, gutter cleaning, siding cleaning & pressure washing. Affordable, insured & locally owned. Get a free quote today!" />', '<meta name="description" content="Expert window cleaning services in Ottawa by MagicPro. Residential & commercial window cleaning Ottawa trusts. Affordable, streak-free guaranteed. Get a quote today!" />')
# Update canonical
head = head.replace('<link rel="canonical" href="https://www.magicpro.ca/" />', '<link rel="canonical" href="https://www.magicpro.ca/services/window-cleaning.html" />')
head = head.replace('<meta property="og:url" content="https://www.magicpro.ca/" />', '<meta property="og:url" content="https://www.magicpro.ca/services/window-cleaning" />')
head = head.replace('content="Cleaning Services Ottawa | MagicPro Window & Gutter Cleaning"', 'content="Window Cleaning Services Ottawa | MagicPro"')

# Add our custom Service Page CSS immediately before </style>
service_css = """
    /* ── SUB-HERO ── */
    #sub-hero {
      position: relative;
      background: url('../Magic Pro Window Cleaning Images/12-0A4A0165.jpg') center/cover no-repeat;
      padding: 140px 0 100px;
      color: var(--white);
      text-align: center;
    }
    #sub-hero::before {
      content: ''; position: absolute; inset: 0;
      background: linear-gradient(135deg, rgba(14,30,56,0.92) 0%, rgba(0,180,216,0.85) 100%);
      z-index: 1;
    }
    #sub-hero .container { position: relative; z-index: 2; max-width: 800px; margin: 0 auto; }
    .sub-hero-tag { display: inline-block; padding: 6px 16px; background: rgba(255,255,255,0.15); backdrop-filter: blur(8px); border-radius: 50px; font-weight: 700; letter-spacing: 2px; font-size: 0.85rem; margin-bottom: 24px; text-transform: uppercase; }
    .sub-hero-title { font-family: 'Outfit', sans-serif; font-size: clamp(2.5rem, 5vw, 3.8rem); font-weight: 900; line-height: 1.1; margin-bottom: 20px; }
    .sub-hero-desc { font-size: 1.15rem; color: rgba(255,255,255,0.9); line-height: 1.6; }

    /* ── SERVICE BENTO OVERVIEW ── */
    #service-overview { padding: 90px 0; background: var(--off-white); }
    .bento-overview-grid { display: grid; grid-template-columns: 1.2fr 1fr; gap: 40px; align-items: stretch; }
    .bento-card { background: var(--white); border-radius: 24px; padding: 50px; box-shadow: 0 16px 40px rgba(0,0,0,0.05); }
    .bento-card-dark { background: var(--navy-dark); color: var(--white); border-radius: 24px; padding: 50px; position: relative; overflow: hidden; }
    
    .bento-title { font-family: 'Outfit', sans-serif; font-size: 2.2rem; color: var(--navy-dark); margin-bottom: 20px; font-weight: 800; line-height: 1.2; }
    .bento-desc { font-size: 1.05rem; color: var(--text-body); line-height: 1.7; margin-bottom: 20px; }
    
    .bento-card-dark .bento-title { color: var(--white); }
    .bento-card-dark::after { content: '🪟'; position: absolute; right: -20px; bottom: -30px; font-size: 10rem; opacity: 0.05; transform: rotate(-15deg); }
    .check-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 16px; margin-top: 30px; position: relative; z-index: 2; }
    .check-item { display: flex; align-items: center; gap: 12px; font-weight: 600; font-size: 0.95rem; }
    .check-icon { color: var(--cyan-bright); font-size: 1.2rem; }

    /* ── ALTERNATING CATEGORIES ── */
    #service-categories { padding: 90px 0; }
    .category-row { display: grid; grid-template-columns: 1fr 1fr; gap: 60px; align-items: center; margin-bottom: 90px; }
    .category-row:last-child { margin-bottom: 0; }
    .category-row.reverse .cat-img-wrapper { order: 2; }
    .category-row.reverse .cat-content { order: 1; }
    .cat-img-wrapper { position: relative; border-radius: 24px; overflow: hidden; aspect-ratio: 4/3; box-shadow: 0 20px 40px rgba(0,0,0,0.1); }
    .cat-img-wrapper img { width: 100%; height: 100%; object-fit: cover; }
    .cat-content h2 { font-family: 'Outfit', sans-serif; font-size: 2.3rem; color: var(--navy-dark); margin-bottom: 20px; font-weight: 800; }
    .cat-content p { color: var(--text-body); font-size: 1.05rem; line-height: 1.7; margin-bottom: 24px; }
    
    /* ── PACKAGES & PRICING ── */
    #packages { padding: 90px 0; background: var(--navy-dark); color: var(--white); }
    .pkg-header { text-align: center; margin-bottom: 60px; }
    .pkg-tag { display: inline-block; background: rgba(0,180,216,0.15); color: var(--cyan-bright); padding: 6px 14px; border-radius: 50px; font-weight: 800; text-transform: uppercase; letter-spacing: 1px; font-size: 0.8rem; margin-bottom: 16px; }
    .pkg-header h2 { font-family: 'Outfit', sans-serif; font-size: 2.8rem; font-weight: 900; margin-bottom: 16px; }
    .pkg-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 30px; max-width: 900px; margin: 0 auto; }
    
    .pkg-card { background: rgba(255,255,255,0.05); border: 1px solid rgba(255,255,255,0.1); border-radius: 24px; padding: 40px; backdrop-filter: blur(12px); display: flex; flex-direction: column; transition: transform var(--transition); }
    .pkg-card:hover { transform: translateY(-8px); border-color: rgba(255,255,255,0.25); }
    .pkg-card.deluxe { background: linear-gradient(145deg, rgba(255,255,255,0.08), rgba(0,180,216,0.15)); border-color: var(--cyan); }
    
    .pkg-name { font-family: 'Outfit', sans-serif; font-size: 1.8rem; font-weight: 800; margin-bottom: 12px; }
    .pkg-sub { color: rgba(255,255,255,0.6); font-size: 0.9rem; margin-bottom: 24px; padding-bottom: 24px; border-bottom: 1px solid rgba(255,255,255,0.1); }
    .pkg-list { display: flex; flex-direction: column; gap: 16px; margin-bottom: 30px; flex-grow: 1; }
    .pkg-list-item { display: flex; align-items: flex-start; gap: 12px; font-size: 0.95rem; line-height: 1.5; color: rgba(255,255,255,0.9); }
    
    /* ── PROCESS STEPS ── */
    #our-process { padding: 90px 0; background: var(--white); }
    .process-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 30px; text-align: center; margin-top: 50px; }
    .process-step { padding: 30px; border-radius: 20px; background: var(--off-white); border: 1px solid rgba(0,0,0,0.04); transition: transform var(--transition); }
    .process-step:hover { transform: translateY(-6px); box-shadow: 0 10px 30px rgba(0,0,0,0.06); }
    .process-icon { font-size: 2.5rem; margin-bottom: 20px; display: inline-block; background: rgba(0,180,216,0.1); color: var(--cyan); width: 80px; height: 80px; line-height: 80px; border-radius: 50%; }
    .process-step h3 { font-family: 'Outfit', sans-serif; font-size: 1.4rem; color: var(--navy-dark); margin-bottom: 12px; }
    .process-step p { color: var(--gray-dark); font-size: 0.95rem; line-height: 1.6; }

    @media (max-width: 900px) {
      .bento-overview-grid { grid-template-columns: 1fr; }
      .category-row { grid-template-columns: 1fr; gap: 30px; margin-bottom: 60px; }
      .category-row.reverse .cat-img-wrapper { order: 1; }
      .category-row.reverse .cat-content { order: 2; }
      .pkg-grid { grid-template-columns: 1fr; }
      .process-grid { grid-template-columns: 1fr; gap: 20px; }
    }
"""

style_end = head.rfind('</style>')
head = head[:style_end] + service_css + head[style_end:] + '\n</head>'

# Topbar and Navbar (Modify links to root relative `../`)
body_start = orig.find('<body>') + 6
# Actually, wait, let's just grab the whole body, then we isolate what we need.
body_content = orig[body_start:]

topbar_nav = body_content[:body_content.find('<!-- HERO SECTION -->')]
# Map asset links in navbar/topbar
topbar_nav = topbar_nav.replace('href="/quote"', 'href="../quote.html"')
topbar_nav = topbar_nav.replace('href="/"', 'href="../website.html"')
topbar_nav = topbar_nav.replace('href="/about"', 'href="../about.html"')
topbar_nav = topbar_nav.replace('href="/services"', 'href="../services.html"')
topbar_nav = topbar_nav.replace('Magic-Pro-Logo-New-1024x665.png', '../Magic-Pro-Logo-New-1024x665.png')


# Footer, Map, Scripts
footer_start = body_content.find('<!-- MAP SECTION -->')
footer_content = body_content[footer_start:]
footer_content = footer_content.replace('href="/sitemap.xml"', 'href="../sitemap.xml"')
footer_content = footer_content.replace('href="/"', 'href="../website.html"')
footer_content = footer_content.replace('href="/about"', 'href="../about.html"')
footer_content = footer_content.replace('href="/gallery"', 'href="../gallery.html"')
footer_content = footer_content.replace('href="/reviews"', 'href="../reviews.html"')
footer_content = footer_content.replace('href="/contact"', 'href="../contact.html"')
footer_content = footer_content.replace('href="/window-cleaning"', 'href="window-cleaning.html"')
footer_content = footer_content.replace('href="/gutter-cleaning"', 'href="../gutter-cleaning.html"')
footer_content = footer_content.replace('href="/siding-cleaning"', 'href="../siding-cleaning.html"')
footer_content = footer_content.replace('href="/pressure-washing"', 'href="../pressure-washing.html"')
footer_content = footer_content.replace('Magic-Pro-Logo-New-1024x665.png', '../Magic-Pro-Logo-New-1024x665.png')

# The Trust Ribbon & CTA Banner
trust_ribbon = body_content.split('<!-- TRUST RIBBON -->')[1].split('</section>')[0] + '</section>\n'
cta_banner = body_content.split('<!-- CTA BANNER -->')[1].split('</section>')[0] + '</section>\n'
cta_banner = cta_banner.replace('href="/quote"', 'href="../quote.html"')

# --- NEW PAGE CONTENT ---
service_html = """
  <!-- SUB-HERO -->
  <header id="sub-hero">
    <div class="container">
      <div class="sub-hero-tag">Crystal Clear Expectations</div>
      <h1 class="sub-hero-title">Elite Window Cleaning Services Ottawa</h1>
      <p class="sub-hero-desc">No matter how high up or how large your windows are, our professional window cleaners in Ottawa guarantee spotless, streak-free results that improve your property's energy efficiency and curb appeal.</p>
    </div>
  </header>

  <!-- OVERVIEW BENTO -->
  <section id="service-overview">
    <div class="container">
      <div class="bento-overview-grid">
        <div class="bento-card">
          <div class="section-tag">Unmatched Clarity</div>
          <h2 class="bento-title">Why Choose Our Professional Window Cleaners Ottawa?</h2>
          <p class="bento-desc">MagicPro offers industry-leading window cleaning services Ottawa homeowners and businesses trust. Using advanced stripwashers and high-quality squeegee systems, we completely release grime, debris, and grease from your glass.</p>
          <p class="bento-desc">Beyond just the glass, we meticulously wipe down exterior and interior frames, sills, tracks, and edges. <strong>Bonus:</strong> When you book interior & exterior residential window cleaning Ottawa, we include screen cleaning absolutely free.</p>
        </div>
        <div class="bento-card-dark">
          <h3 class="bento-title">What We Clean</h3>
          <p style="color: rgba(255,255,255,0.7); margin-bottom: 20px;">Our premium service covers all standard and luxury glass installations:</p>
          <div class="check-grid">
            <div class="check-item"><span class="check-icon">✓</span> Exterior Windows</div>
            <div class="check-item"><span class="check-icon">✓</span> Interior Windows</div>
            <div class="check-item"><span class="check-icon">✓</span> Storm Windows</div>
            <div class="check-item"><span class="check-icon">✓</span> Glass Rail Panels</div>
            <div class="check-item"><span class="check-icon">✓</span> Skylights</div>
            <div class="check-item"><span class="check-icon">✓</span> Window Screens</div>
            <div class="check-item"><span class="check-icon">✓</span> Frames & Sills</div>
            <div class="check-item"><span class="check-icon">✓</span> Tracks</div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- CATEGORIES -->
  <section id="service-categories">
    <div class="container">
      <!-- Row 1: Residential -->
      <div class="category-row">
        <div class="cat-img-wrapper">
          <img src="../Magic Pro Window Cleaning Images/29-0A4A0463.jpg" alt="Residential window cleaning Ottawa house" loading="lazy" />
        </div>
        <div class="cat-content">
          <div class="section-tag">For Your Home</div>
          <h2>Residential Window Cleaning Ottawa</h2>
          <p>Your home deserves the absolute best. Our residential crews handle single-story bungalows, multi-level estates, and townhouses with the utmost care. We utilize property-safe ladders, protective booties inside your home, and eco-friendly solutions.</p>
          <p>Enjoy natural light pouring into your living room without staring at hard water stains and bird droppings. Let us elevate the comfort and attractiveness of your residential property.</p>
          <ul style="list-style: none; padding: 0; margin-bottom: 24px;">
            <li style="margin-bottom: 10px;">🛡️ Safe ladder techniques & protocols</li>
            <li style="margin-bottom: 10px;">🏡 Free screen cleaning included on full service</li>
            <li style="margin-bottom: 10px;">✨ Sills and frames wiped perfectly clean</li>
          </ul>
        </div>
      </div>

      <!-- Row 2: Commercial -->
      <div class="category-row reverse">
        <div class="cat-img-wrapper">
          <img src="../Magic Pro Window Cleaning Images/13-0A4A0170.jpg" alt="Commercial window cleaning Ottawa storefront" loading="lazy" />
        </div>
        <div class="cat-content">
          <div class="section-tag">For Your Business</div>
          <h2>Commercial Window Cleaning Ottawa</h2>
          <p>First impressions dictate business success. A sparkling storefront or office building immediately signals professionalism and quality to your clients. We deliver scalable commercial window cleaning Ottawa businesses rely on.</p>
          <p>Whether you manage a boutique bakery, a corporate high-rise, or a multi-unit complex, our team arrives fully insured and equipped with specialized commercial-grade squeegees to deliver flawless panoramas.</p>
          <ul style="list-style: none; padding: 0; margin-bottom: 24px;">
            <li style="margin-bottom: 10px;">🏢 Storefronts, offices & commercial complexes</li>
            <li style="margin-bottom: 10px;">👷 Fully WSIB insured & commercially licensed</li>
            <li style="margin-bottom: 10px;">📅 Flexible scheduling to avoid customer disruption</li>
          </ul>
        </div>
      </div>
    </div>
  </section>

  <!-- PACKAGES -->
  <section id="packages">
    <div class="container">
      <div class="pkg-header">
        <div class="pkg-tag">Transparent Pricing</div>
        <h2>Our Window Cleaning Packages</h2>
        <p style="color: rgba(255,255,255,0.7); max-width: 600px; margin: 0 auto;">Choose the level of detail that fits your property's needs. We guarantee 100% satisfaction on all packages.</p>
      </div>
      <div class="pkg-grid">
        <!-- Basic -->
        <div class="pkg-card">
          <h3 class="pkg-name">Basic Window Cleaning</h3>
          <div class="pkg-sub">Exterior focus to boost instant curb appeal.</div>
          <div class="pkg-list">
            <div class="pkg-list-item"><span class="check-icon">✓</span> Handwash all exterior glass surfaces</div>
            <div class="pkg-list-item"><span class="check-icon">✓</span> Professional squeegee drying</div>
            <div class="pkg-list-item"><span class="check-icon">✓</span> Wipe down exterior frames and ledges</div>
            <div class="pkg-list-item"><span class="check-icon">✓</span> Removal of loose dirt and cobwebs</div>
          </div>
          <a href="../quote.html" class="btn-white" style="text-align:center; display:block;">Get A Quote</a>
        </div>
        
        <!-- Deluxe -->
        <div class="pkg-card deluxe">
          <div class="pkg-tag" style="position:absolute; top: -14px; right: 24px; background: var(--cyan); color: white;">Most Popular</div>
          <h3 class="pkg-name">Deluxe Window Cleaning</h3>
          <div class="pkg-sub">Complete Interior and Exterior glass restoration.</div>
          <div class="pkg-list">
            <div class="pkg-list-item"><span class="check-icon">✓</span> Everything in Basic Package</div>
            <div class="pkg-list-item"><span class="check-icon">✓</span> Handwash all interior glass surfaces</div>
            <div class="pkg-list-item"><span class="check-icon">✓</span> Detailed wipe of interior frames & tracks</div>
            <div class="pkg-list-item"><span class="check-icon">✓</span> Detailed wipe down of all screens</div>
            <div class="pkg-list-item"><span style="color:var(--cyan-bright); font-weight:700;">Bonus:</span> Free screen cleaning included!</div>
          </div>
          <a href="../quote.html" class="btn-primary" style="text-align:center; display:block;">Book Full Service</a>
        </div>
      </div>
    </div>
  </section>

  <!-- HOW WE WORK PROCESS -->
  <section id="our-process">
    <div class="container">
      <div class="pkg-header" style="margin-bottom: 20px;">
        <div class="section-tag">Flawless Process</div>
        <h2 style="color:var(--navy-dark);">How We Work</h2>
        <p style="color: var(--gray-dark); max-width: 600px; margin: 0 auto;">Our systematic approach guarantees perfectly clear, streak-free surfaces.</p>
      </div>
      <div class="process-grid">
        <div class="process-step">
          <div class="process-icon">🧼</div>
          <h3>1. Strip & Scrub</h3>
          <p>We use a specialized stripwasher to evenly wet and deeply scrub the window glass, releasing packed grime, debris, grease, and hard water spots without scratching.</p>
        </div>
        <div class="process-step">
          <div class="process-icon">🪄</div>
          <h3>2. Professional Squeegee</h3>
          <p>The window is then squeegeed with high-quality, professional-grade rubber, instantly stripping the moisture and making the glass surface perfectly clear and invisible.</p>
        </div>
        <div class="process-step">
          <div class="process-icon">✨</div>
          <h3>3. Detail Wipedown</h3>
          <p>We don't just stop at the glass. Your window frames, sills, tracks, and glass edges are all meticulously wiped clean to prevent drip runs and ensure ultimate cleanliness.</p>
        </div>
      </div>
    </div>
  </section>
"""

final_html = head + "\n<body>\n" + topbar_nav + "\n" + service_html + "\n<!-- TRUST RIBBON -->\n" + trust_ribbon + "\n<!-- CTA BANNER -->\n" + cta_banner + "\n" + footer_content
final_path = 'c:/Users/dell/Desktop/MagicPro/services/window-cleaning.html'

os.makedirs(os.path.dirname(final_path), exist_ok=True)
with open(final_path, 'w', encoding='utf-8') as f:
    f.write(final_html)

print("Service page completely generated.")

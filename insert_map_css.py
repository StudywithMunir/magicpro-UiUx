file_path = 'c:/Users/dell/Desktop/MagicPro/website.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

css_code = """
    /* ── MAP SECTION ── */
    #map-section {
      position: relative;
      width: 100%;
      height: 600px;
      overflow: hidden;
    }
    #map-section iframe {
      width: 100%;
      height: 100%;
      border: none;
      filter: contrast(1.1) brightness(0.95);
    }
    .map-card {
      position: absolute;
      top: 50%;
      left: 10%;
      transform: translateY(-50%);
      background: rgba(255, 255, 255, 0.85);
      backdrop-filter: blur(24px);
      -webkit-backdrop-filter: blur(24px);
      border: 1px solid rgba(255, 255, 255, 0.5);
      border-radius: var(--radius-lg);
      padding: 40px;
      box-shadow: 0 20px 40px rgba(0, 0, 0, 0.15);
      width: 90%;
      max-width: 420px;
      z-index: 10;
    }
    .map-card h3 {
      font-family: 'Outfit', sans-serif;
      font-size: 1.8rem;
      color: var(--navy-dark);
      margin-bottom: 8px;
    }
    .map-card p {
      color: var(--gray-dark);
      font-size: 0.95rem;
      line-height: 1.6;
      margin-bottom: 24px;
    }
    .map-card .contact-detail {
        display: flex;
        align-items: center;
        gap: 12px;
        margin-bottom: 16px;
        font-weight: 600;
        color: var(--navy-dark);
    }
    @media (max-width: 768px) {
      #map-section { height: 750px; }
      .map-card {
        top: auto;
        bottom: 24px;
        left: 50%;
        transform: translateX(-50%);
        width: 90%;
        padding: 30px;
      }
    }

    /* ── RESPONSIVE ── */"""

if '/* ── MAP SECTION ── */' not in content:
    content = content.replace('/* ── RESPONSIVE ── */', css_code)
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Map CSS injected successfully.")
else:
    print("Map CSS already exists.")

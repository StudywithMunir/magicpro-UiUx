import re

file_path = 'c:/Users/dell/Desktop/MagicPro/website.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# --- 1) CSS CHUNKS ---
old_reviews_css = """    .reviews-grid {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 24px;
    }"""

new_reviews_css = """    .slider-header {
      display: flex;
      justify-content: space-between;
      align-items: flex-end;
      margin-bottom: 24px;
    }
    .slider-controls { display: flex; gap: 12px; }
    .slider-btn {
      width: 48px; height: 48px; border-radius: 50%;
      background: rgba(255,255,255,0.08); border: 1px solid rgba(255,255,255,0.2);
      color: var(--white); display: flex; align-items: center; justify-content: center;
      cursor: pointer; transition: all var(--transition);
    }
    .slider-btn:hover { background: var(--cyan); border-color: var(--cyan); transform: scale(1.05); }
    .slider-btn:disabled { opacity: 0.3; cursor: not-allowed; }
    
    .reviews-slider-wrapper { overflow: hidden; width: 100%; padding-bottom: 10px; }
    .reviews-track {
      display: flex; gap: 24px; transition: transform 0.5s cubic-bezier(0.25, 1, 0.5, 1);
      will-change: transform;
    }
    .reviews-track .review-card {
      flex: 0 0 calc(33.333% - 16px);
      min-width: calc(33.333% - 16px);
    }
    
    #jump-top {
      position: fixed; bottom: 30px; left: 30px; width: 50px; height: 50px;
      background: var(--navy-dark); color: var(--white);
      border-radius: 50%; display: flex; align-items: center; justify-content: center;
      cursor: pointer; box-shadow: var(--shadow-lg); border: 2px solid rgba(255,255,255,0.1);
      transform: translateY(100px); opacity: 0; transition: all 0.4s ease; z-index: 9999;
    }
    #jump-top.visible { transform: translateY(0); opacity: 1; }
    #jump-top:hover { background: var(--cyan); transform: translateY(-5px); border-color: var(--cyan); }
    @media (max-width: 900px) {
      .reviews-track .review-card { flex: 0 0 calc(50% - 12px); min-width: calc(50% - 12px); }
    }
    @media (max-width: 600px) {
      .slider-header { flex-direction: column; align-items: flex-start; gap: 20px; }
      .reviews-track .review-card { flex: 0 0 100%; min-width: 100%; }
      #jump-top { bottom: 20px; left: 20px; }
    }
"""
if old_reviews_css in content:
    content = content.replace(old_reviews_css, new_reviews_css)

# Remove the old grid responsive css
content = content.replace('.reviews-grid { grid-template-columns: 1fr; }', '')


# --- 2) HTML CHUNKS ---
# The HTML to replace:
old_html = """      <div class="reviews-avg" aria-label="Overall rating">
        <div class="avg-score">5.0</div>
        <div class="avg-right">
          <div class="avg-stars">★★★★★</div>
          <div class="avg-label">Based on 9,500+ Google Reviews</div>
        </div>
      </div>
      <div class="reviews-grid" id="reviews-container">"""

new_html = """      <div class="slider-header">
        <div class="reviews-avg" aria-label="Overall rating" style="margin: 0;">
          <div class="avg-score">5.0</div>
          <div class="avg-right">
            <div class="avg-stars">★★★★★</div>
            <div class="avg-label">Based on 9,500+ Google Reviews</div>
          </div>
        </div>
        <div class="slider-controls">
          <button id="review-prev" class="slider-btn" aria-label="Previous Reviews">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="19" y1="12" x2="5" y2="12"></line><polyline points="12 19 5 12 12 5"></polyline></svg>
          </button>
          <button id="review-next" class="slider-btn" aria-label="Next Reviews">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg>
          </button>
        </div>
      </div>
      <div class="reviews-slider-wrapper">
        <div class="reviews-track" id="reviews-track">"""

content = content.replace(old_html, new_html)

# Add closing divs for the slider wrapper
content = content.replace('</div>\n    </div>\n  </section>\n\n  <!-- GALLERY SECTION -->', '</div>\n      </div>\n    </div>\n  </section>\n\n  <!-- GALLERY SECTION -->')

# Jump to Top Button HTML just before closing body
jump_html = """
  <!-- JUMP TO TOP -->
  <button id="jump-top" aria-label="Jump to top of page" title="Jump to top">
    <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="18 15 12 9 6 15"></polyline></svg>
  </button>
</body>"""
content = content.replace('</body>', jump_html)


# --- 3) JS CHUNKS ---
js_logic = """
    // ── Reviews Slider ──
    const track = document.getElementById('reviews-track');
    const btnPrev = document.getElementById('review-prev');
    const btnNext = document.getElementById('review-next');
    if (track && btnPrev && btnNext) {
      let currentIndex = 0;
      
      const updateSlider = () => {
        const cards = track.querySelectorAll('.review-card');
        if (!cards.length) return;
        
        // Items visible logic
        let visible = 3;
        if (window.innerWidth <= 900) visible = 2;
        if (window.innerWidth <= 600) visible = 1;
        
        const cardWidth = cards[0].offsetWidth;
        const gap = 24; 
        const moveDist = cardWidth + gap;
        
        const maxIndex = Math.max(0, cards.length - visible);
        currentIndex = Math.max(0, Math.min(currentIndex, maxIndex));
        
        track.style.transform = `translateX(-${currentIndex * moveDist}px)`;
        
        btnPrev.disabled = currentIndex === 0;
        btnNext.disabled = currentIndex >= maxIndex;
      };
      
      btnPrev.addEventListener('click', () => { currentIndex--; updateSlider(); });
      btnNext.addEventListener('click', () => { currentIndex++; updateSlider(); });
      window.addEventListener('resize', updateSlider);
      updateSlider();
    }

    // ── Jump to Top ──
    const jumpBtn = document.getElementById('jump-top');
    if (jumpBtn) {
      window.addEventListener('scroll', () => {
        if (window.scrollY > 400) {
          jumpBtn.classList.add('visible');
        } else {
          jumpBtn.classList.remove('visible');
        }
      });
      jumpBtn.addEventListener('click', () => {
        window.scrollTo({ top: 0, behavior: 'smooth' });
      });
    }
  </script>"""

content = content.replace('</script>', js_logic)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)
print("Slider and Jump to Top applied flawlessly.")

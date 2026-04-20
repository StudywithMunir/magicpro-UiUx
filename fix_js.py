import re

file_path = 'c:/Users/dell/Desktop/MagicPro/website.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# The JS we accidentally injected:
js_malformed = """
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

# 1. Clean up from the top Schema section
content = content.replace(js_malformed, '\n  </script>')

# 2. Add it cleanly right before the closing body tag inside its own script
clean_js = """  <script>
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
  </script>
</body>"""

# Check if it was already injected near the bottom (it shouldn't have been since we only replaced the first </script>)
if 'window.scrollTo({ top: 0, behavior: \'smooth\' });' not in content.split('<body')[-1]:
    content = content.replace('</body>', clean_js)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)
print("JS positioning fixed.")

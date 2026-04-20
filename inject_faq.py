import os

file_path = 'c:/Users/dell/Desktop/MagicPro/services/window-cleaning.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

faq_html = """
  <!-- FAQ SECTION -->
  <section id="faq-section" aria-labelledby="faq-heading">
    <div class="container">
      <div class="faq-inner">
        <div class="faq-header">
          <div class="section-tag" style="background: rgba(0,180,216,0.1); color: var(--cyan-bright);">Window Cleaning FAQs</div>
          <h2 id="faq-heading">Common Questions About Our Window Cleaning in Ottawa</h2>
        </div>
        <div class="faq-grid">
          <div class="faq-item">
            <button class="faq-q" aria-expanded="false">
              How often should I get my windows professionally cleaned in Ottawa?
              <span class="faq-icon">▼</span>
            </button>
            <div class="faq-a" hidden>
              <p>For most residential properties in Ottawa, we strongly recommend professional window cleaning twice a year: once in the spring to wash away the harsh winter salt and grime, and once in the fall. Commercial storefronts and offices may require monthly or quarterly services to maintain a pristine, professional appearance.</p>
            </div>
          </div>
          <div class="faq-item">
            <button class="faq-q" aria-expanded="false">
              Do I need to be home when you clean my exterior windows?
              <span class="faq-icon">▼</span>
            </button>
            <div class="faq-a" hidden>
              <p>Not at all! If you book our Basic Package (exterior window cleaning only), our professional window cleaners can complete the entire job while you are out. We just ask that you ensure all gates are unlocked and your window screens are removed beforehand. We will send you an invoice online once the job is flawlessly completed.</p>
            </div>
          </div>
          <div class="faq-item">
            <button class="faq-q" aria-expanded="false">
              Do you clean the tracks and window screens too?
              <span class="faq-icon">▼</span>
            </button>
            <div class="faq-a" hidden>
              <p>Absolutely. If you select our Deluxe Window Cleaning Package (interior & exterior), we meticulously wipe down all visible tracks, sills, and ledges. Furthermore, we include complimentary, free window screen cleaning as part of that premier service to ensure nothing obstructs your crystal-clear view.</p>
            </div>
          </div>
          <div class="faq-item">
            <button class="faq-q" aria-expanded="false">
              Are your window cleaning services fully insured?
              <span class="faq-icon">▼</span>
            </button>
            <div class="faq-a" hidden>
              <p>Yes. MagicPro is fully licensed and carries comprehensive liability insurance. All our window cleaners in Ottawa are rigorously trained in safe ladder operations, providing you with 100% peace of mind while we work on your property.</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

"""

# Insert right before <!-- MAP SECTION -->
content = content.replace('<!-- MAP SECTION -->', faq_html + '<!-- MAP SECTION -->')

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("FAQ Section injected perfectly.")

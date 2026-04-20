import re

file_path = 'c:/Users/dell/Desktop/MagicPro/services/window-cleaning.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# First we strip the BAD FAQ section we just injected
pattern = re.compile(r'<!-- FAQ SECTION -->.*?</section>', re.DOTALL)
content = re.sub(pattern, '', content)

faq_html_correct = """<!-- FAQ SECTION -->
  <section id="faq" aria-labelledby="faq-heading">
    <div class="container">
      <div class="faq-header">
        <div class="section-tag" style="background: rgba(0,180,216,0.1); color: var(--cyan-bright);">Window Cleaning FAQs</div>
        <h2 id="faq-heading" class="section-title">Common Questions About Our<br />Window Cleaning in Ottawa</h2>
      </div>
      <div class="faq-grid" id="faq-list">

        <div class="faq-item" id="faq-w1">
          <div class="faq-q" role="button" tabindex="0" aria-expanded="false">
            How often should I get my windows professionally cleaned in Ottawa?
            <div class="faq-chevron">▼</div>
          </div>
          <div class="faq-a">
            For most residential properties in Ottawa, we strongly recommend professional window cleaning twice a year: once in the spring to wash away the harsh winter salt and grime, and once in the fall. Commercial storefronts and offices may require monthly or quarterly services to maintain a pristine, professional appearance.
          </div>
        </div>

        <div class="faq-item" id="faq-w2">
          <div class="faq-q" role="button" tabindex="0" aria-expanded="false">
            Do I need to be home when you clean my exterior windows?
            <div class="faq-chevron">▼</div>
          </div>
          <div class="faq-a">
            Not at all! If you book our Basic Package (exterior window cleaning only), our professional cleaners can complete the entire job while you are out. We just ask that you ensure all gates are unlocked and your window screens are removed beforehand. We will send you an invoice online once the job is flawlessly completed.
          </div>
        </div>

        <div class="faq-item" id="faq-w3">
          <div class="faq-q" role="button" tabindex="0" aria-expanded="false">
            Do you clean the tracks and window screens too?
            <div class="faq-chevron">▼</div>
          </div>
          <div class="faq-a">
            Absolutely. If you select our Deluxe Window Cleaning Package (interior & exterior), we meticulously wipe down all visible tracks, sills, and ledges. Furthermore, we include complimentary, free window screen cleaning as part of that premier service to ensure nothing obstructs your crystal-clear view.
          </div>
        </div>

        <div class="faq-item" id="faq-w4">
          <div class="faq-q" role="button" tabindex="0" aria-expanded="false">
            Are your window cleaning services fully insured?
            <div class="faq-chevron">▼</div>
          </div>
          <div class="faq-a">
            Yes. MagicPro is fully licensed and carries comprehensive liability insurance. All our window cleaners in Ottawa are rigorously trained in safe ladder operations, providing you with 100% peace of mind while we work on your property.
          </div>
        </div>

      </div>
    </div>
  </section>
"""

# Re-inject perfectly matching layout right before map
content = content.replace('<!-- MAP SECTION -->', faq_html_correct + '\n<!-- MAP SECTION -->')

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("FAQ Markup successfully patched to map onto CSS.")

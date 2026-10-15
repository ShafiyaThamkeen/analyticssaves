# Builds invoice-automation.docx in the HLB HAMT sub-page blueprint format, from the final HTML.
import re, sys
from bs4 import BeautifulSoup
from docx import Document
from docx.shared import Pt, Twips, RGBColor
from docx.oxml import OxmlElement
from docx.oxml.ns import qn

SRC = '/home/user/analyticssaves/invoice-automation.html'
OUT = '/home/user/analyticssaves/invoice-automation.docx'
BLUE, GOLD, INK = '10538F', 'B8761C', '0A1F33'   # exactly as in the sample doc
soup = BeautifulSoup(open(SRC, encoding='utf-8').read(), 'html.parser')
T = lambda el: re.sub(r'\s+', ' ', el.get_text(' ', strip=True)).replace(' ,', ',').replace(' .', '.').replace(' :', ':').strip() if el else ''

doc = Document()
sec = doc.sections[0]
sec.page_width, sec.page_height = Twips(12240), Twips(15840)
sec.top_margin = sec.bottom_margin = Twips(1080); sec.left_margin = sec.right_margin = Twips(1224)
st = doc.styles['Normal']; st.font.name = 'Arial'; st.font.size = Pt(10); st.font.color.rgb = RGBColor.from_string(INK)
st.element.rPr.rFonts.set(qn('w:eastAsia'), 'Arial'); st.element.rPr.rFonts.set(qn('w:cs'), 'Arial')
st.paragraph_format.space_after = Twips(200); st.paragraph_format.line_spacing = 1.15
body = doc.element.body
for p in list(doc.paragraphs): p._element.getparent().remove(p._element)

def spacing(p, before=None, after=None):
    pf = p.paragraph_format
    if before is not None: pf.space_before = Twips(before)
    if after is not None: pf.space_after = Twips(after)
def jc(p, v='both'):
    pPr = p._p.get_or_add_pPr(); j = OxmlElement('w:jc'); j.set(qn('w:val'), v); pPr.append(j)
def border_bottom(p):
    pPr = p._p.get_or_add_pPr(); b = OxmlElement('w:pBdr'); e = OxmlElement('w:bottom')
    for k, v in (('val', 'single'), ('sz', '12'), ('space', '0'), ('color', GOLD)): e.set(qn('w:' + k), v)
    b.append(e); pPr.insert(0, b)
def run(p, text, bold=False, size=None, color=None):
    r = p.add_run(text); r.bold = bold or None
    if size: r.font.size = Pt(size)
    if color: r.font.color.rgb = RGBColor.from_string(color)
    return r
def blank(): doc.add_paragraph()
def title(t):
    p = doc.add_paragraph(); spacing(p, 320, 80); border_bottom(p); jc(p, 'center'); run(p, t, True, 20, BLUE)
def heading(t):
    p = doc.add_paragraph(); spacing(p, 320, 80); border_bottom(p); jc(p); run(p, t, True, 15, BLUE); p.paragraph_format.keep_with_next = True
def bullet(t):
    p = doc.add_paragraph(); spacing(p, None, 0); p.paragraph_format.left_indent = Twips(360); p.paragraph_format.first_line_indent = Twips(-360)
    jc(p); run(p, '● ' + t)
def label(t):
    p = doc.add_paragraph(); spacing(p, None, 120); jc(p); run(p, t); p.paragraph_format.keep_with_next = True
def numbered(i, head, copy):
    p = doc.add_paragraph(); spacing(p, None, 120); p.paragraph_format.left_indent = Twips(360); p.paragraph_format.first_line_indent = Twips(-360)
    jc(p); run(p, f'{i}. {head}', True); run(p, ' - ' + copy)
def qa(q, a):
    p = doc.add_paragraph(); spacing(p, 160, 60); jc(p); run(p, 'Q: ' + q, True)
    p = doc.add_paragraph(); spacing(p, None, 120); jc(p); run(p, a)
def table(headers, rows, widths):
    t = doc.add_table(rows=1 + len(rows), cols=len(headers)); tbl = t._tbl
    pr = tbl.tblPr
    for tag in ('w:tblStyle', 'w:tblW', 'w:tblLayout', 'w:tblBorders'):
        for e in pr.findall(qn(tag)): pr.remove(e)
    w = OxmlElement('w:tblW'); w.set(qn('w:w'), str(sum(widths))); w.set(qn('w:type'), 'dxa'); pr.append(w)
    bd = OxmlElement('w:tblBorders')
    for side in ('top', 'left', 'bottom', 'right', 'insideH', 'insideV'):
        e = OxmlElement('w:' + side)
        for k, v in (('val', 'single'), ('sz', '4'), ('space', '0'), ('color', '000000')): e.set(qn('w:' + k), v)
        bd.append(e)
    pr.append(bd)
    lay = OxmlElement('w:tblLayout'); lay.set(qn('w:type'), 'fixed'); pr.append(lay)
    for gc, wd in zip(tbl.tblGrid.findall(qn('w:gridCol')), widths): gc.set(qn('w:w'), str(wd))
    def fill(cell, lines, hdr, wd):
        tcPr = cell._tc.get_or_add_tcPr()
        for e in tcPr.findall(qn('w:tcW')): tcPr.remove(e)
        tw = OxmlElement('w:tcW'); tw.set(qn('w:w'), str(wd)); tw.set(qn('w:type'), 'dxa'); tcPr.append(tw)
        if hdr:
            sh = OxmlElement('w:shd'); sh.set(qn('w:val'), 'clear'); sh.set(qn('w:color'), 'auto'); sh.set(qn('w:fill'), BLUE); tcPr.append(sh)
        lines = lines if isinstance(lines, list) else [lines]
        for i, ln in enumerate(lines):
            p = cell.paragraphs[0] if i == 0 else cell.add_paragraph()
            jc(p); run(p, ln, hdr, 9, 'FFFFFF' if hdr else None)
    for row in t.rows:
        trPr = row._tr.get_or_add_trPr(); cs = OxmlElement('w:cantSplit'); trPr.append(cs)
    hdr = OxmlElement('w:tblHeader'); t.rows[0]._tr.get_or_add_trPr().append(hdr)
    for c, (h, wd) in enumerate(zip(headers, widths)): fill(t.rows[0].cells[c], h, True, wd)
    for r, row in enumerate(rows):
        for c, (v, wd) in enumerate(zip(row, widths)): fill(t.rows[r + 1].cells[c], v, False, wd)
    blank()

def head_block(sec_el, eyebrow_sel='.eyebrow', h2='h2'):
    e = sec_el.select_one(eyebrow_sel); h = sec_el.select_one(h2); l = sec_el.select_one('.sec-head .lede')
    if e: bullet('Eyebrow: ' + T(e))
    bullet('H2: ' + T(h))
    if l: bullet('Intro: ' + T(l))
def image_line(sec_el):
    for s in sec_el.select('svg.ill'): bullet('Image: ' + s.get('aria-label', ''))
def numlist(items):
    for i, (h, c) in enumerate(items, 1): numbered(i, h, c)
def cards(sec_el, sel):
    return [(T(c.select_one('h3')), T(c.select_one('p'))) for c in sec_el.select(sel)]
def path_items(sec_el):
    return [(T(li.select_one('h3')), T(li.select_one('p'))) for li in sec_el.select('ol.path li')]

n = [0]
def section(t):
    n[0] += 1; heading(f'{n[0]}. {t}')

# ---------------- document ----------------
title('Invoice Automation - AI Document Processing Sub-page')
heading('Page metadata & SEO')
meta_title = T(soup.title); desc = soup.find('meta', attrs={'name': 'description'})['content']
table(['Element', 'Content'], [
    ['Page title', meta_title], ['Meta description', desc],
    ['Menu location', 'AI > Document Processing > Invoice Automation'],
    ['Primary keywords', 'invoice automation'],
    ['Secondary keywords', 'AI invoice automation, invoice processing automation, automated invoice processing, accounts payable automation, intelligent document processing, HAMT AI'],
    ['Supporting keywords', 'invoice processing software, three-way matching, exception handling, invoice data extraction, manual vs automated invoice processing'],
], [2475, 7305])

# 1 Hero
hero = soup.select_one('header.hero')
section('Hero')
bullet('Eyebrow: ' + ' · '.join(T(x) for x in hero.select('.crumbs a, .crumbs [aria-current]')))
bullet('H1: ' + ' '.join(T(x) for x in hero.select('h1 .h1-line')))
bullet('Intro paragraph: ' + T(hero.select_one('p.lede')))
btns = hero.select('.hero-cta .btn')
bullet(f'Buttons: {T(btns[0])} (primary) · {T(btns[1])} (secondary)')
bullet('Hero note: ' + T(hero.select_one('.hero-note')))
blank(); label('Hero side panel (example invoice card)')
inv = hero.select_one('.inv')
bullet('Heading: Example: one supplier invoice moving through the process')
bullet(f"Sub-line: {T(inv.select_one('.inv-type'))} · {T(inv.select_one('.inv-no'))} · " + ' · '.join(f"{T(d.select_one('span'))} {T(d.select_one('b'))}" for d in inv.select('.inv-sums > div')) + ' (illustrative example)')
table(['Item', 'Copy'], [[T(c.select_one('strong')), f"{T(c.select_one('p'))} [{T(c.select_one('.pill'))}]"] for c in inv.select('.chk')], [3150, 6630])
bullet('Footer line: ' + T(inv.select_one('.inv-foot')))
blank()

# 2 Strip
section('At a glance')
label('Four highlights (heading / copy):')
table(['Item', 'Copy'], [[T(i.select_one('.k')), T(i.select_one('.v'))] for i in soup.select('section.strip .strip-item')], [3150, 6630])

# 3 Challenge
sc = soup.select_one('#challenge'); section('Why automate accounts payable')
bullet('Eyebrow: ' + T(sc.select_one('.eyebrow'))); bullet('H2: ' + T(sc.select_one('h2')))
bullet('Intro: ' + ' '.join(T(p) for p in sc.select('.story-text p')))
label('Four cards (heading / copy):')
table(['Item', 'Copy'], [list(x) for x in cards(sc, '.tile')], [3150, 6630])
bullet('Bridge line: ' + T(sc.select_one('.bridge'))); blank()

# 4 Shift
sc = soup.select_one('#shift'); section('What changes')
head_block(sc); bullet('H3: ' + T(sc.select_one('.shift-title')))
label('Six rows (manual today / with HAMT AI):')
table(['Manual today', 'With HAMT AI'], [[T(r.select_one('.from')), T(r.select_one('.to'))] for r in sc.select('.shift')], [4500, 5280])

# 5 Benefits
sc = soup.select_one('#benefits'); section('Benefits')
head_block(sc); image_line(sc)
label('Four cards (heading / copy):')
table(['Item', 'Copy'], [list(x) for x in cards(sc, '.tile')], [3150, 6630])

# 6 Learning
sc = soup.select_one('#learning'); section('The learning cycle')
head_block(sc); image_line(sc)
label('Four steps (heading / copy):'); numlist(path_items(sc))
bullet('H3: ' + T(sc.select('.sub-h3')[0]))
label('Four pillars (letter / heading / copy):')
table(['Tag', 'Heading', 'Copy'], [[T(c.select_one('.icon-sq')), T(c.select_one('h3')), T(c.select_one('p'))] for c in sc.select('.grid-4 .card')], [1260, 2625, 5895])
bullet('H3: ' + T(sc.select('.sub-h3')[1])); bullet('Copy: ' + T(sc.select('.sub-h3')[1].find_next('p')))
for li in sc.select('ul.principles li'): bullet('Point: ' + T(li))
blank()

def cta_section(el):
    section('CTA')
    bullet('H2: ' + T(el.select_one('.cta-title'))); bullet('Button: ' + T(el.select_one('.btn'))); blank()
ctas = soup.select('.cta-band'); 
cta_section(ctas[0])

# 8 How
sc = soup.select_one('#how'); section('How automated invoice processing works')
head_block(sc); image_line(sc)
label('Six-step process (step / heading / copy / points):')
table(['Step', 'Heading', 'Copy', 'Points'], [[T(c.select_one('.step-n')), T(c.select_one('h3')), T(c.select_one('p')), [T(li) for li in c.select('li')]] for c in sc.select('.grid-3 .card')], [720, 2040, 3900, 3120])

# 9 Scale
sc = soup.select_one('#scale'); section('From mid-market to enterprise')
head_block(sc); label('Two tiers (tier / heading / copy and points):')
rows = []
for c in sc.select('.tier'):
    rows.append([T(c.select_one('.tier-label')), T(c.select_one('h3')), [T(c.select_one('p'))] + ['• ' + T(li) for li in c.select('li')]])
table(['Tier', 'Heading', 'Copy'], rows, [1815, 2400, 5565])
bullet('Note (all deployments): ' + T(sc.select_one('.both'))); blank()

# 10 Region
sc = soup.select_one('#region'); section('Built for the UAE, GCC and Middle East')
head_block(sc); image_line(sc); label('Six cards (heading / copy / chips):')
for i, t in enumerate(sc.select('.tile'), 1):
    numbered(i, T(t.select_one('h3')), T(t.select_one('p')) + ' Chips: ' + ' · '.join(T(c) for c in t.select('.chip')))
cta_section(ctas[1])

# 12 Services
sc = soup.select_one('#services'); section('Your services partner')
head_block(sc); label('Four-step process (heading / copy):'); numlist(path_items(sc)); blank()

# 13 Why
sc = soup.select_one('#why-us'); section('Why HLB HAMT')
head_block(sc); label('Four cards (heading / copy):'); numlist(cards(sc, '.tile')); blank()

# 14 Integration
sc = soup.select_one('#integration'); section('ERP integration')
head_block(sc); image_line(sc); label('Three cards (card / covers / copy):')
table(['Card', 'Covers', 'Copy'], [[T(c.select_one('h3')), T(c.select_one('.systems')), T([p for p in c.select('p') if 'systems' not in (p.get('class') or [])][0])] for c in sc.select('.int-card')], [1815, 3300, 4665])
label('Principles:'); numlist([(T(li), '') for li in sc.select('ul.principles li')]) if False else None
for i, li in enumerate(sc.select('ul.principles li'), 1):
    p = doc.add_paragraph(); spacing(p, None, 120); p.paragraph_format.left_indent = Twips(360); p.paragraph_format.first_line_indent = Twips(-360); jc(p); run(p, f'{i}. ' + T(li))
cta_section(ctas[2])

# 16 FAQ
sc = soup.select_one('#faq'); section('FAQ')
bullet('Eyebrow: ' + T(sc.select_one('.eyebrow'))); bullet('H2: ' + T(sc.select_one('h2')))
for d in sc.select('details.faq'): qa(T(d.select_one('summary')), T(d.select_one('.ans')))
blank()

# 17 Notes
section('Items to confirm before publishing')
for t in [
 'Claims carried over from Bala\'s draft and marked [CONFIRM] in the copy: "award-winning", "more than two decades", "more than 150 countries", "within a few weeks", and the UAE e-invoicing dates and AED 50 million threshold.',
 'HAMT AI: the only source detail was the four pillars. Confidence scoring, supervised retraining on approved corrections, review-rate tracking and logged corrections are written for this page and must be checked against how HAMT AI actually works.',
 'Retraining: the page says approved corrections feed the models "for your setup, tested before release". Confirm this matches the real process, and whether training is per client or shared.',
 'Data handling: the page says it is agreed with the client IT team before go-live and that data can stay in the UAE. Confirm both.',
 'The example invoice (INV-26-10482, PO 4500912, GRN-7731, TRN 100234567890003) is illustrative. VAT rates in the region chips come from Bala\'s draft.',
 'Bala\'s ten FAQs are merged into six; every answer point is retained. No ERP, competitor or reference-site names appear anywhere.',
 'Brand colours in the page and images were taken from the HLB HAMT SugarAI CRM page (#005A77, #FBBA00). Please confirm against the official brand guide.',
]: bullet(t)

doc.core_properties.title = 'Invoice Automation - AI Document Processing Sub-page'; doc.core_properties.author = 'HLB HAMT'
doc.save(OUT)
# word count of page copy (everything from the Hero to the FAQ, excluding metadata, image notes and review notes)
print('saved', OUT)

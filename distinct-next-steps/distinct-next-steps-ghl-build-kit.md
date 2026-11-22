# Distinct® Tax Assessment: Next Steps page (GHL build kit)

Post-payment thank-you step for Distinct Tax Consulting Group®. It sits right after the $500 Distinct® Tax Assessment checkout.

- **Layout:** single page, mobile-first, 10 sections. Each section is one GHL **Custom Code** element.
- **Self-contained:** each block carries its own CSS (brand tokens included) and its own small vanilla script where needed. There are no external frameworks. Jost is the only external file, loaded from Google Fonts.
- **Live preview:** `index.html`, the whole page assembled from these same blocks.
- **Paste-ready files:** `ghl-blocks/00-global-head.html` to `ghl-blocks/10-footer.html`. These are the same code as below.

## Brand palette in use

Source: Canva, *DTCG Client - The Distinct Experience Guide (Doc) - 2026*.

| Token | Hex | Used for | Contrast |
|---|---|---|---|
| Teal (ink) | `#003B42` | Headings, body text, primary buttons | 11.6:1 on cream ✔ |
| Cream (canvas) | `#FBF8F2` | Page background, button text | Button text on teal 11.6:1 ✔ |
| Ivory | `#F3EDE1` | Welcome and footer backgrounds, pills | Teal text 10.6:1 ✔ |
| Gold | `#B18132` | Rules, large step numerals, borders, focus ring | 3.3:1. Used only for decoration and large numerals, never for small text |
| Dark gold | `#96691C` | Small uppercase eyebrow labels (on cream and white only) | 4.6:1 on cream ✔ |
| Champagne | `#E6CD96` | Tinted highlight fills (deadline card, notes) | Teal text 7.9:1 ✔ |
| White | `#FFFFFF` | Cards and alternating sections | |

Not used: sage `#8FA5A2` fails text contrast on cream (2.5:1), and white text on gold fails (3.5:1). There is no dark theme anywhere.

**Type:** Jost 700 for headings, 500 for subheads and buttons, 400 for body. **Shape:** 18px corners on cards and video frames, pill-shaped buttons.

## Anchors

`#welcome` · `#steps` · `#welcome-video` · `#taxdome-video` · `#checklist` · `#organizer` · `#deadline` · `#what-next` · `#security` · `#footer`

Every section is a real landmark with a heading, so keyboard and screen-reader users land in the right place when they follow an anchor link. It has `tabindex="-1"` and a `scroll-margin-top` offset.

## Global head code (paste once)

Paste in the funnel step: **Settings → Tracking Code → Head**. It loads Jost, turns on smooth scrolling and keeps this page out of search results.

```html
<!-- Distinct Next Steps: GLOBAL HEAD CODE (paste once in GHL: step Settings > Head tracking code) -->
<meta name="robots" content="noindex, nofollow">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Jost:wght@400;500;700&display=swap" rel="stylesheet">
<style>
  html{scroll-behavior:smooth}
  @media (prefers-reduced-motion:reduce){html{scroll-behavior:auto}}
  body{background:#fbf8f2}
</style>
```

## SECTION 1: Welcome (`#welcome`)

**GHL build note:** Section: full width, background #F3EDE1, padding 0. This is the only H1 on the page. Add a 1-column row, then a **Custom Code** element, and paste the block below. Paste-ready file: `ghl-blocks/01-welcome.html`.

```html
<!-- ===== SECTION 1: WELCOME (#welcome) ===== -->
<section id="welcome" class="dx dx-welcome" tabindex="-1" aria-labelledby="dx-welcome-title">
<style>
@import url('https://fonts.googleapis.com/css2?family=Jost:wght@400;500;700&display=swap');
/* Distinct brand tokens (from The Distinct Experience Guide, 2026) */
.dx{--dx-teal:#003b42;--dx-gold:#b18132;--dx-gold-dk:#96691c;--dx-champ:#e6cd96;--dx-ivory:#f3ede1;--dx-cream:#fbf8f2;--dx-white:#ffffff;--dx-sage:#8fa5a2;--dx-line:rgba(177,129,50,.30);--dx-soft:rgba(0,59,66,.80);--dx-r:18px;--dx-r-sm:12px;
  display:block;box-sizing:border-box;font-family:'Jost',system-ui,-apple-system,'Segoe UI',sans-serif;font-weight:400;font-size:17px;line-height:1.6;color:var(--dx-teal);background:var(--dx-cream);padding:56px 20px;scroll-margin-top:16px;-webkit-font-smoothing:antialiased}
.dx *,.dx *::before,.dx *::after{box-sizing:border-box}
.dx:focus{outline:none}
.dx__in{max-width:980px;margin:0 auto}
.dx h1,.dx h2,.dx h3{font-family:inherit;font-weight:700;color:var(--dx-teal);margin:0;letter-spacing:-.01em}
.dx h2{font-size:clamp(1.65rem,5.2vw,2.4rem);line-height:1.15;margin-bottom:14px}
.dx h3{font-size:1.2rem;line-height:1.3;margin-bottom:6px}
.dx p{margin:0 0 14px}
.dx__eyebrow{display:flex;align-items:center;gap:12px;margin:0 0 12px;font-weight:500;font-size:.78rem;letter-spacing:.16em;text-transform:uppercase;color:var(--dx-gold-dk)}
.dx__eyebrow::before{content:"";flex:0 0 40px;height:2px;border-radius:2px;background:var(--dx-gold)}
.dx__sub{font-weight:500;font-size:1.08rem;color:var(--dx-soft);max-width:640px}
.dx__btn{display:inline-flex;align-items:center;justify-content:center;gap:10px;min-height:52px;padding:14px 26px;border-radius:999px;border:2px solid var(--dx-teal);background:var(--dx-teal);color:var(--dx-cream)!important;font:500 1rem/1.2 'Jost',system-ui,sans-serif;letter-spacing:.02em;text-decoration:none!important;cursor:pointer;transition:transform .2s ease,box-shadow .2s ease;width:100%}
.dx__btn:hover{transform:translateY(-1px);box-shadow:0 10px 24px -12px rgba(0,59,66,.55)}
.dx__btn--ghost{background:transparent;color:var(--dx-teal)!important}
.dx__btn--soft{background:var(--dx-champ);border-color:var(--dx-champ);color:var(--dx-teal)!important}
.dx__btn svg{width:18px;height:18px;flex:none}
.dx a:focus-visible,.dx button:focus-visible,.dx input:focus-visible+label,.dx input:focus-visible{outline:3px solid var(--dx-gold);outline-offset:3px}
.dx__link{color:var(--dx-teal);font-weight:500;text-decoration:underline;text-decoration-color:var(--dx-gold);text-underline-offset:4px}
.dx__card{background:var(--dx-white);border:1px solid var(--dx-line);border-radius:var(--dx-r);padding:24px}
.dx__sr{position:absolute!important;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0);white-space:nowrap}
@media (min-width:640px){.dx{padding:80px 32px}.dx__btn{width:auto}}
@media (prefers-reduced-motion:reduce){.dx *{transition:none!important;animation:none!important}}
.dx-welcome{background:linear-gradient(180deg,var(--dx-ivory) 0%,var(--dx-cream) 100%);padding-top:40px}
.dx-welcome__logo{display:flex;justify-content:center;margin-bottom:40px}
.dx-welcome__logo img{max-width:220px;height:auto;display:block}
.dx-ph{display:flex;align-items:center;justify-content:center;text-align:center;border:2px dashed var(--dx-gold);border-radius:var(--dx-r-sm);background:rgba(230,205,150,.18);color:var(--dx-teal);font:500 .85rem/1.35 'Jost',system-ui,sans-serif;padding:12px}
.dx-ph--logo{width:220px;min-height:84px}
.dx-welcome h1{font-size:clamp(2.1rem,8vw,3.6rem);line-height:1.05;max-width:760px;margin-bottom:22px}
.dx-welcome__note{position:relative;max-width:680px;margin:0 0 30px;padding:22px 22px 20px 24px;background:var(--dx-white);border:1px solid var(--dx-line);border-radius:var(--dx-r)}
.dx-welcome__note::before{content:"";position:absolute;left:0;top:22px;bottom:22px;width:3px;border-radius:3px;background:var(--dx-gold)}
.dx-welcome__note p{font-size:1.05rem}
.dx-welcome__sig{font-weight:500;margin:0!important}
.dx-welcome__sig span{display:block;font-weight:400;font-size:.9rem;color:var(--dx-soft)}
</style>
<div class="dx__in">
  <div class="dx-welcome__logo">
    <!-- LOGO SLOT: replace the placeholder div below with:
         <img src="[LOGO IMAGE URL]" alt="Distinct Tax Consulting Group®" width="220" height="84">
         Use the approved Distinct logo. Do NOT use the version with the gold "I". -->
    <div class="dx-ph dx-ph--logo" role="img" aria-label="Distinct Tax Consulting Group® logo">[LOGO]<br>Distinct Tax Consulting Group®</div>
  </div>
  <p class="dx__eyebrow">Distinct® Tax Assessment · Payment received</p>
  <h1 id="dx-welcome-title">You're in. Here's what happens next.</h1>
  <div class="dx-welcome__note">
    <p>Welcome, and thank you for trusting Distinct Tax Consulting Group® with your Distinct® Tax Assessment.</p>
    <p>Here's how we work: before we ever get on a call, our team reviews your documents. That way, our call is spent on what we found and what we can do about it.</p>
    <p class="dx-welcome__sig">Alysha<span>Founder and Managing Partner</span></p>
  </div>
  <a class="dx__btn" href="#steps">See your 3 steps
    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><path d="M12 5v14M5 12l7 7 7-7"/></svg></a>
</div>
</section>
```

## SECTION 2: Your 3 Steps (`#steps`)

**GHL build note:** Section: full width, background #FBF8F2, padding 0. Step progress is saved in the visitor's own browser only. Add a 1-column row, then a **Custom Code** element, and paste the block below. Paste-ready file: `ghl-blocks/02-steps.html`.

```html
<!-- ===== SECTION 2: YOUR 3 STEPS (#steps) ===== -->
<section id="steps" class="dx dx-steps" tabindex="-1" aria-labelledby="dx-steps-title">
<style>
@import url('https://fonts.googleapis.com/css2?family=Jost:wght@400;500;700&display=swap');
/* Distinct brand tokens (from The Distinct Experience Guide, 2026) */
.dx{--dx-teal:#003b42;--dx-gold:#b18132;--dx-gold-dk:#96691c;--dx-champ:#e6cd96;--dx-ivory:#f3ede1;--dx-cream:#fbf8f2;--dx-white:#ffffff;--dx-sage:#8fa5a2;--dx-line:rgba(177,129,50,.30);--dx-soft:rgba(0,59,66,.80);--dx-r:18px;--dx-r-sm:12px;
  display:block;box-sizing:border-box;font-family:'Jost',system-ui,-apple-system,'Segoe UI',sans-serif;font-weight:400;font-size:17px;line-height:1.6;color:var(--dx-teal);background:var(--dx-cream);padding:56px 20px;scroll-margin-top:16px;-webkit-font-smoothing:antialiased}
.dx *,.dx *::before,.dx *::after{box-sizing:border-box}
.dx:focus{outline:none}
.dx__in{max-width:980px;margin:0 auto}
.dx h1,.dx h2,.dx h3{font-family:inherit;font-weight:700;color:var(--dx-teal);margin:0;letter-spacing:-.01em}
.dx h2{font-size:clamp(1.65rem,5.2vw,2.4rem);line-height:1.15;margin-bottom:14px}
.dx h3{font-size:1.2rem;line-height:1.3;margin-bottom:6px}
.dx p{margin:0 0 14px}
.dx__eyebrow{display:flex;align-items:center;gap:12px;margin:0 0 12px;font-weight:500;font-size:.78rem;letter-spacing:.16em;text-transform:uppercase;color:var(--dx-gold-dk)}
.dx__eyebrow::before{content:"";flex:0 0 40px;height:2px;border-radius:2px;background:var(--dx-gold)}
.dx__sub{font-weight:500;font-size:1.08rem;color:var(--dx-soft);max-width:640px}
.dx__btn{display:inline-flex;align-items:center;justify-content:center;gap:10px;min-height:52px;padding:14px 26px;border-radius:999px;border:2px solid var(--dx-teal);background:var(--dx-teal);color:var(--dx-cream)!important;font:500 1rem/1.2 'Jost',system-ui,sans-serif;letter-spacing:.02em;text-decoration:none!important;cursor:pointer;transition:transform .2s ease,box-shadow .2s ease;width:100%}
.dx__btn:hover{transform:translateY(-1px);box-shadow:0 10px 24px -12px rgba(0,59,66,.55)}
.dx__btn--ghost{background:transparent;color:var(--dx-teal)!important}
.dx__btn--soft{background:var(--dx-champ);border-color:var(--dx-champ);color:var(--dx-teal)!important}
.dx__btn svg{width:18px;height:18px;flex:none}
.dx a:focus-visible,.dx button:focus-visible,.dx input:focus-visible+label,.dx input:focus-visible{outline:3px solid var(--dx-gold);outline-offset:3px}
.dx__link{color:var(--dx-teal);font-weight:500;text-decoration:underline;text-decoration-color:var(--dx-gold);text-underline-offset:4px}
.dx__card{background:var(--dx-white);border:1px solid var(--dx-line);border-radius:var(--dx-r);padding:24px}
.dx__sr{position:absolute!important;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0);white-space:nowrap}
@media (min-width:640px){.dx{padding:80px 32px}.dx__btn{width:auto}}
@media (prefers-reduced-motion:reduce){.dx *{transition:none!important;animation:none!important}}
.dx-steps__head{display:flex;flex-wrap:wrap;align-items:flex-end;justify-content:space-between;gap:16px;margin-bottom:28px}
.dx-steps__progress{min-width:220px;flex:1 1 220px;max-width:320px}
.dx-steps__progress p{font-weight:500;font-size:.92rem;margin:0 0 8px}
.dx-steps__bar{height:8px;border-radius:99px;background:var(--dx-ivory);overflow:hidden}
.dx-steps__bar span{display:block;height:100%;width:0;border-radius:99px;background:var(--dx-gold);transition:width .4s ease}
.dx-steps__list{list-style:none;margin:0;padding:0;display:grid;gap:16px}
.dx-step{position:relative;display:flex;flex-direction:column;gap:6px;background:var(--dx-white);border:1px solid var(--dx-line);border-radius:var(--dx-r);padding:26px 22px 22px;transition:border-color .25s ease,background .25s ease}
.dx-step__num{font-weight:700;font-size:2.6rem;line-height:1;color:var(--dx-gold);margin-bottom:8px;font-variant-numeric:tabular-nums}
.dx-step p{color:var(--dx-soft);margin-bottom:18px;flex:1}
.dx-step__done{display:flex;align-items:center;gap:10px;margin-top:14px;font-size:.92rem;font-weight:500;cursor:pointer;user-select:none}
.dx-step__done input{width:22px;height:22px;accent-color:var(--dx-teal);margin:0;cursor:pointer}
.dx-step.is-done{background:rgba(230,205,150,.22);border-color:var(--dx-gold)}
.dx-step.is-done .dx-step__num::after{content:" ✓";font-size:1.4rem;color:var(--dx-teal)}
@media (min-width:820px){.dx-steps__list{grid-template-columns:repeat(3,1fr)}}
</style>
<div class="dx__in">
  <div class="dx-steps__head">
    <div>
      <p class="dx__eyebrow">Your next steps</p>
      <h2 id="dx-steps-title">Three steps to get ready</h2>
      <p class="dx__sub" style="margin:0">Work through these in order. Each button takes you to the right spot on this page.</p>
    </div>
    <div class="dx-steps__progress">
      <p aria-live="polite"><span data-dx-steps-count>0</span> of 3 steps done</p>
      <div class="dx-steps__bar" aria-hidden="true"><span data-dx-steps-bar></span></div>
    </div>
  </div>
  <ol class="dx-steps__list">
    <li class="dx-step" data-dx-step="1">
      <span class="dx-step__num" aria-hidden="true">01</span>
      <h3><span class="dx__sr">Step 1: </span>Watch the welcome video</h3>
      <p>A short welcome from our team before you get started.</p>
      <a class="dx__btn" href="#welcome-video">Go to step 1</a>
      <label class="dx-step__done"><input type="checkbox" data-dx-step-check> I've done this</label>
    </li>
    <li class="dx-step" data-dx-step="2">
      <span class="dx-step__num" aria-hidden="true">02</span>
      <h3><span class="dx__sr">Step 2: </span>Set up your secure TaxDome portal</h3>
      <p>Your portal is where you'll complete your organizer and upload your documents.</p>
      <a class="dx__btn" href="#taxdome-video">Go to step 2</a>
      <label class="dx-step__done"><input type="checkbox" data-dx-step-check> I've done this</label>
    </li>
    <li class="dx-step" data-dx-step="3">
      <span class="dx-step__num" aria-hidden="true">03</span>
      <h3><span class="dx__sr">Step 3: </span>Complete your organizer and upload your documents</h3>
      <p>See exactly what to gather, what it looks like and where to find it.</p>
      <a class="dx__btn" href="#checklist">Go to step 3</a>
      <label class="dx-step__done"><input type="checkbox" data-dx-step-check> I've done this</label>
    </li>
  </ol>
</div>
<script>
(function(){
  var root=document.getElementById('steps'); if(!root) return;
  var KEY='dx-next-steps-progress', items=root.querySelectorAll('[data-dx-step]');
  var count=root.querySelector('[data-dx-steps-count]'), bar=root.querySelector('[data-dx-steps-bar]');
  var saved={}; try{saved=JSON.parse(localStorage.getItem(KEY)||'{}')||{};}catch(e){}
  function update(){
    var n=0;
    items.forEach(function(li){var cb=li.querySelector('[data-dx-step-check]');li.classList.toggle('is-done',cb.checked);if(cb.checked)n++;saved[li.getAttribute('data-dx-step')]=cb.checked;});
    count.textContent=n; bar.style.width=(n/items.length*100)+'%';
    try{localStorage.setItem(KEY,JSON.stringify(saved));}catch(e){}
  }
  items.forEach(function(li){var cb=li.querySelector('[data-dx-step-check]');cb.checked=!!saved[li.getAttribute('data-dx-step')];cb.addEventListener('change',update);});
  update();
})();
</script>
</section>
```

## SECTION 3: Welcome Video (`#welcome-video`)

**GHL build note:** Section: full width, background #FFFFFF, padding 0. When the video is ready, swap the placeholder for the embed (see the comment in the code). Add a 1-column row, then a **Custom Code** element, and paste the block below. Paste-ready file: `ghl-blocks/03-welcome-video.html`.

```html
<!-- ===== SECTION 3: WELCOME VIDEO (#welcome-video) ===== -->
<section id="welcome-video" class="dx dx-vid" tabindex="-1" aria-labelledby="dx-wv-title">
<style>
@import url('https://fonts.googleapis.com/css2?family=Jost:wght@400;500;700&display=swap');
/* Distinct brand tokens (from The Distinct Experience Guide, 2026) */
.dx{--dx-teal:#003b42;--dx-gold:#b18132;--dx-gold-dk:#96691c;--dx-champ:#e6cd96;--dx-ivory:#f3ede1;--dx-cream:#fbf8f2;--dx-white:#ffffff;--dx-sage:#8fa5a2;--dx-line:rgba(177,129,50,.30);--dx-soft:rgba(0,59,66,.80);--dx-r:18px;--dx-r-sm:12px;
  display:block;box-sizing:border-box;font-family:'Jost',system-ui,-apple-system,'Segoe UI',sans-serif;font-weight:400;font-size:17px;line-height:1.6;color:var(--dx-teal);background:var(--dx-cream);padding:56px 20px;scroll-margin-top:16px;-webkit-font-smoothing:antialiased}
.dx *,.dx *::before,.dx *::after{box-sizing:border-box}
.dx:focus{outline:none}
.dx__in{max-width:980px;margin:0 auto}
.dx h1,.dx h2,.dx h3{font-family:inherit;font-weight:700;color:var(--dx-teal);margin:0;letter-spacing:-.01em}
.dx h2{font-size:clamp(1.65rem,5.2vw,2.4rem);line-height:1.15;margin-bottom:14px}
.dx h3{font-size:1.2rem;line-height:1.3;margin-bottom:6px}
.dx p{margin:0 0 14px}
.dx__eyebrow{display:flex;align-items:center;gap:12px;margin:0 0 12px;font-weight:500;font-size:.78rem;letter-spacing:.16em;text-transform:uppercase;color:var(--dx-gold-dk)}
.dx__eyebrow::before{content:"";flex:0 0 40px;height:2px;border-radius:2px;background:var(--dx-gold)}
.dx__sub{font-weight:500;font-size:1.08rem;color:var(--dx-soft);max-width:640px}
.dx__btn{display:inline-flex;align-items:center;justify-content:center;gap:10px;min-height:52px;padding:14px 26px;border-radius:999px;border:2px solid var(--dx-teal);background:var(--dx-teal);color:var(--dx-cream)!important;font:500 1rem/1.2 'Jost',system-ui,sans-serif;letter-spacing:.02em;text-decoration:none!important;cursor:pointer;transition:transform .2s ease,box-shadow .2s ease;width:100%}
.dx__btn:hover{transform:translateY(-1px);box-shadow:0 10px 24px -12px rgba(0,59,66,.55)}
.dx__btn--ghost{background:transparent;color:var(--dx-teal)!important}
.dx__btn--soft{background:var(--dx-champ);border-color:var(--dx-champ);color:var(--dx-teal)!important}
.dx__btn svg{width:18px;height:18px;flex:none}
.dx a:focus-visible,.dx button:focus-visible,.dx input:focus-visible+label,.dx input:focus-visible{outline:3px solid var(--dx-gold);outline-offset:3px}
.dx__link{color:var(--dx-teal);font-weight:500;text-decoration:underline;text-decoration-color:var(--dx-gold);text-underline-offset:4px}
.dx__card{background:var(--dx-white);border:1px solid var(--dx-line);border-radius:var(--dx-r);padding:24px}
.dx__sr{position:absolute!important;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0);white-space:nowrap}
@media (min-width:640px){.dx{padding:80px 32px}.dx__btn{width:auto}}
@media (prefers-reduced-motion:reduce){.dx *{transition:none!important;animation:none!important}}
.dx-vid{background:var(--dx-white)}
.dx-video{position:relative;width:100%;aspect-ratio:16/9;border-radius:var(--dx-r);overflow:hidden;background:var(--dx-ivory);border:1px solid var(--dx-line);margin:26px 0 24px;box-shadow:0 24px 48px -32px rgba(0,59,66,.45)}
.dx-video iframe,.dx-video video{position:absolute;inset:0;width:100%;height:100%;border:0}
.dx-video__ph{position:absolute;inset:14px;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:12px;text-align:center;border:2px dashed var(--dx-gold);border-radius:var(--dx-r-sm);padding:16px}
.dx-video__play{width:64px;height:64px;border-radius:50%;background:var(--dx-teal);display:grid;place-items:center}
.dx-video__play svg{width:24px;height:24px;margin-left:4px;fill:var(--dx-cream)}
.dx-video__ph strong{font-weight:700;font-size:1.15rem}
.dx-video__ph span{font-size:.85rem;color:var(--dx-soft)}
.dx-vid__nav{display:flex;flex-wrap:wrap;gap:12px}
@supports not (aspect-ratio:16/9){.dx-video{height:0;padding-top:56.25%}}
</style>
<div class="dx__in">
  <p class="dx__eyebrow">Step 1</p>
  <h2 id="dx-wv-title">Watch the welcome video</h2>
  <p class="dx__sub">Start here, before you set anything up.</p>
  <div class="dx-video">
    <!-- VIDEO EMBED GOES HERE: [WELCOME VIDEO EMBED CODE]
         Delete the placeholder div below and paste your embed iframe in its place, e.g.
         <iframe src="[WELCOME VIDEO EMBED URL]" title="Welcome to Distinct Tax Consulting Group®" allow="autoplay; fullscreen; picture-in-picture" allowfullscreen></iframe>
         Keep the outer .dx-video wrapper: it keeps the 16:9 rounded frame. -->
    <div class="dx-video__ph" role="img" aria-label="Welcome video coming soon">
      <div class="dx-video__play" aria-hidden="true"><svg viewBox="0 0 24 24"><path d="M6 4l14 8-14 8z"/></svg></div>
      <strong>Welcome video coming soon</strong>
      <span>[WELCOME VIDEO EMBED CODE]</span>
    </div>
  </div>
  <div class="dx-vid__nav">
    <a class="dx__btn" href="#taxdome-video">Next: set up TaxDome</a>
    <a class="dx__btn dx__btn--ghost" href="#steps">Back to my steps</a>
  </div>
</div>
</section>
```

## SECTION 4: TaxDome Set-Up Video (`#taxdome-video`)

**GHL build note:** Section: full width, background #FBF8F2, padding 0. Leave href="[TAXDOME PORTAL LINK]" until you have the TaxDome login URL. Add a 1-column row, then a **Custom Code** element, and paste the block below. Paste-ready file: `ghl-blocks/04-taxdome-video.html`.

```html
<!-- ===== SECTION 4: TAXDOME SET-UP VIDEO (#taxdome-video) ===== -->
<section id="taxdome-video" class="dx dx-vid dx-vid--alt" tabindex="-1" aria-labelledby="dx-tv-title">
<style>
@import url('https://fonts.googleapis.com/css2?family=Jost:wght@400;500;700&display=swap');
/* Distinct brand tokens (from The Distinct Experience Guide, 2026) */
.dx{--dx-teal:#003b42;--dx-gold:#b18132;--dx-gold-dk:#96691c;--dx-champ:#e6cd96;--dx-ivory:#f3ede1;--dx-cream:#fbf8f2;--dx-white:#ffffff;--dx-sage:#8fa5a2;--dx-line:rgba(177,129,50,.30);--dx-soft:rgba(0,59,66,.80);--dx-r:18px;--dx-r-sm:12px;
  display:block;box-sizing:border-box;font-family:'Jost',system-ui,-apple-system,'Segoe UI',sans-serif;font-weight:400;font-size:17px;line-height:1.6;color:var(--dx-teal);background:var(--dx-cream);padding:56px 20px;scroll-margin-top:16px;-webkit-font-smoothing:antialiased}
.dx *,.dx *::before,.dx *::after{box-sizing:border-box}
.dx:focus{outline:none}
.dx__in{max-width:980px;margin:0 auto}
.dx h1,.dx h2,.dx h3{font-family:inherit;font-weight:700;color:var(--dx-teal);margin:0;letter-spacing:-.01em}
.dx h2{font-size:clamp(1.65rem,5.2vw,2.4rem);line-height:1.15;margin-bottom:14px}
.dx h3{font-size:1.2rem;line-height:1.3;margin-bottom:6px}
.dx p{margin:0 0 14px}
.dx__eyebrow{display:flex;align-items:center;gap:12px;margin:0 0 12px;font-weight:500;font-size:.78rem;letter-spacing:.16em;text-transform:uppercase;color:var(--dx-gold-dk)}
.dx__eyebrow::before{content:"";flex:0 0 40px;height:2px;border-radius:2px;background:var(--dx-gold)}
.dx__sub{font-weight:500;font-size:1.08rem;color:var(--dx-soft);max-width:640px}
.dx__btn{display:inline-flex;align-items:center;justify-content:center;gap:10px;min-height:52px;padding:14px 26px;border-radius:999px;border:2px solid var(--dx-teal);background:var(--dx-teal);color:var(--dx-cream)!important;font:500 1rem/1.2 'Jost',system-ui,sans-serif;letter-spacing:.02em;text-decoration:none!important;cursor:pointer;transition:transform .2s ease,box-shadow .2s ease;width:100%}
.dx__btn:hover{transform:translateY(-1px);box-shadow:0 10px 24px -12px rgba(0,59,66,.55)}
.dx__btn--ghost{background:transparent;color:var(--dx-teal)!important}
.dx__btn--soft{background:var(--dx-champ);border-color:var(--dx-champ);color:var(--dx-teal)!important}
.dx__btn svg{width:18px;height:18px;flex:none}
.dx a:focus-visible,.dx button:focus-visible,.dx input:focus-visible+label,.dx input:focus-visible{outline:3px solid var(--dx-gold);outline-offset:3px}
.dx__link{color:var(--dx-teal);font-weight:500;text-decoration:underline;text-decoration-color:var(--dx-gold);text-underline-offset:4px}
.dx__card{background:var(--dx-white);border:1px solid var(--dx-line);border-radius:var(--dx-r);padding:24px}
.dx__sr{position:absolute!important;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0);white-space:nowrap}
@media (min-width:640px){.dx{padding:80px 32px}.dx__btn{width:auto}}
@media (prefers-reduced-motion:reduce){.dx *{transition:none!important;animation:none!important}}
.dx-vid--alt{background:var(--dx-cream)}
.dx-video{position:relative;width:100%;aspect-ratio:16/9;border-radius:var(--dx-r);overflow:hidden;background:var(--dx-ivory);border:1px solid var(--dx-line);margin:26px 0 24px;box-shadow:0 24px 48px -32px rgba(0,59,66,.45)}
.dx-video iframe,.dx-video video{position:absolute;inset:0;width:100%;height:100%;border:0}
.dx-video__ph{position:absolute;inset:14px;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:12px;text-align:center;border:2px dashed var(--dx-gold);border-radius:var(--dx-r-sm);padding:16px}
.dx-video__play{width:64px;height:64px;border-radius:50%;background:var(--dx-teal);display:grid;place-items:center}
.dx-video__play svg{width:24px;height:24px;margin-left:4px;fill:var(--dx-cream)}
.dx-video__ph strong{font-weight:700;font-size:1.15rem}
.dx-video__ph span{font-size:.85rem;color:var(--dx-soft)}
.dx-tv__login{display:flex;flex-direction:column;gap:16px;align-items:flex-start;background:var(--dx-white);border:1px solid var(--dx-line);border-radius:var(--dx-r);padding:22px}
.dx-tv__login p{margin:0;font-size:1.05rem;font-weight:500}
.dx-tv__next{margin-top:18px}
@supports not (aspect-ratio:16/9){.dx-video{height:0;padding-top:56.25%}}
@media (min-width:760px){.dx-tv__login{flex-direction:row;align-items:center;justify-content:space-between}}
</style>
<div class="dx__in">
  <p class="dx__eyebrow">Step 2</p>
  <h2 id="dx-tv-title">How to set up your TaxDome account</h2>
  <p class="dx__sub">TaxDome is our secure client portal. This walkthrough shows you how to get in.</p>
  <div class="dx-video">
    <!-- VIDEO EMBED GOES HERE: [TAXDOME SET-UP VIDEO EMBED CODE]
         Delete the placeholder div below and paste your embed iframe in its place, e.g.
         <iframe src="[TAXDOME SET-UP VIDEO EMBED URL]" title="How to set up your TaxDome account" allow="autoplay; fullscreen; picture-in-picture" allowfullscreen></iframe>
         Keep the outer .dx-video wrapper: it keeps the 16:9 rounded frame. -->
    <div class="dx-video__ph" role="img" aria-label="TaxDome set-up video coming soon">
      <div class="dx-video__play" aria-hidden="true"><svg viewBox="0 0 24 24"><path d="M6 4l14 8-14 8z"/></svg></div>
      <strong>TaxDome set-up video coming soon</strong>
      <span>[TAXDOME SET-UP VIDEO EMBED CODE]</span>
    </div>
  </div>
  <div class="dx-tv__login">
    <p>Check your email for your secure TaxDome invitation, or log in to your existing portal.</p>
    <a class="dx__btn" href="[TAXDOME PORTAL LINK]" target="_blank" rel="noopener">Log in to TaxDome
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M14 4h6v6M20 4l-9 9M18 14v5a1 1 0 0 1-1 1H5a1 1 0 0 1-1-1V7a1 1 0 0 1 1-1h5"/></svg><span class="dx__sr">(opens in a new tab)</span></a>
  </div>
  <div class="dx-tv__next"><a class="dx__link" href="#checklist">Next: your document checklist →</a></div>
</div>
</section>
```

## SECTION 5: Document Checklist (`#checklist`)

**GHL build note:** Section: full width, background #FFFFFF, padding 0. Swap each image placeholder for your mock-up (see comments). Alysha must confirm the document list. Add a 1-column row, then a **Custom Code** element, and paste the block below. Paste-ready file: `ghl-blocks/05-checklist.html`.

```html
<!-- ===== SECTION 5: DOCUMENT CHECKLIST (#checklist) ===== -->
<!-- ALYSHA TO CONFIRM: starting list is prior tax returns, year-to-date P&L, IRS/state letters.
     To add a document, copy one <li class="dx-doc">…</li> block; the counter updates automatically. -->
<section id="checklist" class="dx dx-check" tabindex="-1" aria-labelledby="dx-check-title">
<style>
@import url('https://fonts.googleapis.com/css2?family=Jost:wght@400;500;700&display=swap');
/* Distinct brand tokens (from The Distinct Experience Guide, 2026) */
.dx{--dx-teal:#003b42;--dx-gold:#b18132;--dx-gold-dk:#96691c;--dx-champ:#e6cd96;--dx-ivory:#f3ede1;--dx-cream:#fbf8f2;--dx-white:#ffffff;--dx-sage:#8fa5a2;--dx-line:rgba(177,129,50,.30);--dx-soft:rgba(0,59,66,.80);--dx-r:18px;--dx-r-sm:12px;
  display:block;box-sizing:border-box;font-family:'Jost',system-ui,-apple-system,'Segoe UI',sans-serif;font-weight:400;font-size:17px;line-height:1.6;color:var(--dx-teal);background:var(--dx-cream);padding:56px 20px;scroll-margin-top:16px;-webkit-font-smoothing:antialiased}
.dx *,.dx *::before,.dx *::after{box-sizing:border-box}
.dx:focus{outline:none}
.dx__in{max-width:980px;margin:0 auto}
.dx h1,.dx h2,.dx h3{font-family:inherit;font-weight:700;color:var(--dx-teal);margin:0;letter-spacing:-.01em}
.dx h2{font-size:clamp(1.65rem,5.2vw,2.4rem);line-height:1.15;margin-bottom:14px}
.dx h3{font-size:1.2rem;line-height:1.3;margin-bottom:6px}
.dx p{margin:0 0 14px}
.dx__eyebrow{display:flex;align-items:center;gap:12px;margin:0 0 12px;font-weight:500;font-size:.78rem;letter-spacing:.16em;text-transform:uppercase;color:var(--dx-gold-dk)}
.dx__eyebrow::before{content:"";flex:0 0 40px;height:2px;border-radius:2px;background:var(--dx-gold)}
.dx__sub{font-weight:500;font-size:1.08rem;color:var(--dx-soft);max-width:640px}
.dx__btn{display:inline-flex;align-items:center;justify-content:center;gap:10px;min-height:52px;padding:14px 26px;border-radius:999px;border:2px solid var(--dx-teal);background:var(--dx-teal);color:var(--dx-cream)!important;font:500 1rem/1.2 'Jost',system-ui,sans-serif;letter-spacing:.02em;text-decoration:none!important;cursor:pointer;transition:transform .2s ease,box-shadow .2s ease;width:100%}
.dx__btn:hover{transform:translateY(-1px);box-shadow:0 10px 24px -12px rgba(0,59,66,.55)}
.dx__btn--ghost{background:transparent;color:var(--dx-teal)!important}
.dx__btn--soft{background:var(--dx-champ);border-color:var(--dx-champ);color:var(--dx-teal)!important}
.dx__btn svg{width:18px;height:18px;flex:none}
.dx a:focus-visible,.dx button:focus-visible,.dx input:focus-visible+label,.dx input:focus-visible{outline:3px solid var(--dx-gold);outline-offset:3px}
.dx__link{color:var(--dx-teal);font-weight:500;text-decoration:underline;text-decoration-color:var(--dx-gold);text-underline-offset:4px}
.dx__card{background:var(--dx-white);border:1px solid var(--dx-line);border-radius:var(--dx-r);padding:24px}
.dx__sr{position:absolute!important;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0);white-space:nowrap}
@media (min-width:640px){.dx{padding:80px 32px}.dx__btn{width:auto}}
@media (prefers-reduced-motion:reduce){.dx *{transition:none!important;animation:none!important}}
.dx-check{background:var(--dx-white)}
.dx-check__top{display:flex;flex-wrap:wrap;justify-content:space-between;align-items:flex-end;gap:12px;margin-bottom:26px}
.dx-check__count{font-weight:500;font-size:.92rem;padding:8px 16px;border-radius:99px;background:var(--dx-ivory);margin:0}
.dx-check__list{list-style:none;margin:0;padding:0;display:grid;gap:18px}
.dx-doc{display:flex;flex-direction:column;background:var(--dx-cream);border:1px solid var(--dx-line);border-radius:var(--dx-r);overflow:hidden;transition:border-color .25s ease}
.dx-doc__img{position:relative;aspect-ratio:4/3;background:var(--dx-ivory);border-bottom:1px solid var(--dx-line)}
.dx-doc__img img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}
.dx-doc__ph{position:absolute;inset:12px;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:8px;text-align:center;border:2px dashed var(--dx-gold);border-radius:var(--dx-r-sm);font-size:.82rem;line-height:1.35;padding:12px}
.dx-doc__ph svg{width:34px;height:34px;stroke:var(--dx-gold)}
.dx-doc__body{padding:20px 20px 18px;display:flex;flex-direction:column;flex:1}
.dx-doc__where{font-size:.95rem;color:var(--dx-soft);flex:1}
.dx-doc__where b{font-weight:500;color:var(--dx-teal)}
.dx-doc__have{display:flex;align-items:center;gap:10px;font-weight:500;font-size:.92rem;cursor:pointer;padding-top:12px;border-top:1px solid var(--dx-line)}
.dx-doc__have input{width:22px;height:22px;margin:0;accent-color:var(--dx-teal);cursor:pointer}
.dx-doc.is-ready{border-color:var(--dx-gold)}
.dx-check__notes{margin-top:24px;display:grid;gap:12px}
.dx-note{display:flex;gap:14px;align-items:flex-start;background:rgba(230,205,150,.25);border-radius:var(--dx-r);padding:18px 20px}
.dx-note svg{flex:none;width:26px;height:26px;stroke:var(--dx-teal);margin-top:2px}
.dx-note p{margin:0}
.dx-note strong{font-weight:700}
@media (min-width:820px){.dx-check__list{grid-template-columns:repeat(3,1fr)}.dx-check__notes{grid-template-columns:1fr 1fr}}
</style>
<div class="dx__in">
  <div class="dx-check__top">
    <div>
      <p class="dx__eyebrow">Step 3</p>
      <h2 id="dx-check-title">Your document checklist</h2>
      <p class="dx__sub" style="margin:0">Here's what each document looks like and where to find it. Upload everything to your TaxDome portal.</p>
    </div>
    <p class="dx-check__count" aria-live="polite"><span data-dx-doc-count>0</span> of <span data-dx-doc-total>3</span> ready</p>
  </div>
  <ul class="dx-check__list">
    <li class="dx-doc">
      <div class="dx-doc__img">
        <!-- IMAGE SLOT: replace the placeholder div with
             <img src="[IMAGE: PRIOR TAX RETURN MOCK-UP]" alt="Sample first page of a prior-year tax return" loading="lazy"> -->
        <div class="dx-doc__ph" role="img" aria-label="Sample first page of a prior-year tax return">
          <svg viewBox="0 0 24 24" fill="none" stroke-width="1.6" aria-hidden="true"><path d="M7 3h7l5 5v13H7z"/><path d="M14 3v5h5M10 13h6M10 17h6"/></svg>
          [IMAGE: PRIOR TAX RETURN MOCK-UP]
        </div>
      </div>
      <div class="dx-doc__body">
        <h3>Prior tax returns</h3>
        <p class="dx-doc__where"><b>Where to find it:</b> your copy from whoever prepared your return, or the PDF saved in your tax software. Include personal and business returns.</p>
        <label class="dx-doc__have"><input type="checkbox" data-dx-doc> I have this ready</label>
      </div>
    </li>
    <li class="dx-doc">
      <div class="dx-doc__img">
        <!-- IMAGE SLOT: replace the placeholder div with
             <img src="[IMAGE: YEAR-TO-DATE PROFIT AND LOSS MOCK-UP]" alt="Sample year-to-date profit and loss report" loading="lazy"> -->
        <div class="dx-doc__ph" role="img" aria-label="Sample year-to-date profit and loss report">
          <svg viewBox="0 0 24 24" fill="none" stroke-width="1.6" aria-hidden="true"><path d="M4 20h16M7 16v-4M12 16V8M17 16v-7"/></svg>
          [IMAGE: YEAR-TO-DATE PROFIT AND LOSS MOCK-UP]
        </div>
      </div>
      <div class="dx-doc__body">
        <h3>Year-to-date profit and loss</h3>
        <p class="dx-doc__where"><b>Where to find it:</b> run a Profit and Loss report in your bookkeeping software, dated from January 1 to today, or ask your bookkeeper for it.</p>
        <label class="dx-doc__have"><input type="checkbox" data-dx-doc> I have this ready</label>
      </div>
    </li>
    <li class="dx-doc">
      <div class="dx-doc__img">
        <!-- IMAGE SLOT: replace the placeholder div with
             <img src="[IMAGE: IRS OR STATE LETTER MOCK-UP]" alt="Sample IRS or state tax notice letter" loading="lazy"> -->
        <div class="dx-doc__ph" role="img" aria-label="Sample IRS or state tax notice letter">
          <svg viewBox="0 0 24 24" fill="none" stroke-width="1.6" aria-hidden="true"><rect x="3" y="5" width="18" height="14" rx="2"/><path d="M3 7l9 6 9-6"/></svg>
          [IMAGE: IRS OR STATE LETTER MOCK-UP]
        </div>
      </div>
      <div class="dx-doc__body">
        <h3>Any IRS or state letters</h3>
        <p class="dx-doc__where"><b>Where to find it:</b> notices mailed to you by the IRS or your state tax agency. The notice number is usually printed in the top right corner.</p>
        <label class="dx-doc__have"><input type="checkbox" data-dx-doc> I have this ready</label>
      </div>
    </li>
  </ul>
  <div class="dx-check__notes">
    <div class="dx-note">
      <svg viewBox="0 0 24 24" fill="none" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M20 6L9 17l-5-5"/></svg>
      <p><strong>Partial uploads are fine.</strong> Upload what you have now and add the rest as you find it.</p>
    </div>
    <div class="dx-note">
      <svg viewBox="0 0 24 24" fill="none" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M4 19h16M6 15l9-9 3 3-9 9H6z"/></svg>
      <p><strong>Books behind?</strong> Upload what you have and note what's missing in the organizer.</p>
    </div>
  </div>
</div>
<script>
(function(){
  var root=document.getElementById('checklist'); if(!root) return;
  var KEY='dx-next-steps-docs', boxes=root.querySelectorAll('[data-dx-doc]');
  var count=root.querySelector('[data-dx-doc-count]'); root.querySelector('[data-dx-doc-total]').textContent=boxes.length;
  var saved=[]; try{saved=JSON.parse(localStorage.getItem(KEY)||'[]')||[];}catch(e){}
  function update(){
    var n=0,state=[];
    boxes.forEach(function(b,i){var li=b.closest('.dx-doc');li.classList.toggle('is-ready',b.checked);if(b.checked)n++;state[i]=b.checked;});
    count.textContent=n; try{localStorage.setItem(KEY,JSON.stringify(state));}catch(e){}
  }
  boxes.forEach(function(b,i){b.checked=!!saved[i];b.addEventListener('change',update);});
  update();
})();
</script>
</section>
```

## SECTION 6: Organizer (`#organizer`)

**GHL build note:** Section: full width, background #FBF8F2, padding 0. The entity counter is a helper only and saves nothing. Add a 1-column row, then a **Custom Code** element, and paste the block below. Paste-ready file: `ghl-blocks/06-organizer.html`.

```html
<!-- ===== SECTION 6: ORGANIZER (#organizer) ===== -->
<section id="organizer" class="dx dx-org" tabindex="-1" aria-labelledby="dx-org-title">
<style>
@import url('https://fonts.googleapis.com/css2?family=Jost:wght@400;500;700&display=swap');
/* Distinct brand tokens (from The Distinct Experience Guide, 2026) */
.dx{--dx-teal:#003b42;--dx-gold:#b18132;--dx-gold-dk:#96691c;--dx-champ:#e6cd96;--dx-ivory:#f3ede1;--dx-cream:#fbf8f2;--dx-white:#ffffff;--dx-sage:#8fa5a2;--dx-line:rgba(177,129,50,.30);--dx-soft:rgba(0,59,66,.80);--dx-r:18px;--dx-r-sm:12px;
  display:block;box-sizing:border-box;font-family:'Jost',system-ui,-apple-system,'Segoe UI',sans-serif;font-weight:400;font-size:17px;line-height:1.6;color:var(--dx-teal);background:var(--dx-cream);padding:56px 20px;scroll-margin-top:16px;-webkit-font-smoothing:antialiased}
.dx *,.dx *::before,.dx *::after{box-sizing:border-box}
.dx:focus{outline:none}
.dx__in{max-width:980px;margin:0 auto}
.dx h1,.dx h2,.dx h3{font-family:inherit;font-weight:700;color:var(--dx-teal);margin:0;letter-spacing:-.01em}
.dx h2{font-size:clamp(1.65rem,5.2vw,2.4rem);line-height:1.15;margin-bottom:14px}
.dx h3{font-size:1.2rem;line-height:1.3;margin-bottom:6px}
.dx p{margin:0 0 14px}
.dx__eyebrow{display:flex;align-items:center;gap:12px;margin:0 0 12px;font-weight:500;font-size:.78rem;letter-spacing:.16em;text-transform:uppercase;color:var(--dx-gold-dk)}
.dx__eyebrow::before{content:"";flex:0 0 40px;height:2px;border-radius:2px;background:var(--dx-gold)}
.dx__sub{font-weight:500;font-size:1.08rem;color:var(--dx-soft);max-width:640px}
.dx__btn{display:inline-flex;align-items:center;justify-content:center;gap:10px;min-height:52px;padding:14px 26px;border-radius:999px;border:2px solid var(--dx-teal);background:var(--dx-teal);color:var(--dx-cream)!important;font:500 1rem/1.2 'Jost',system-ui,sans-serif;letter-spacing:.02em;text-decoration:none!important;cursor:pointer;transition:transform .2s ease,box-shadow .2s ease;width:100%}
.dx__btn:hover{transform:translateY(-1px);box-shadow:0 10px 24px -12px rgba(0,59,66,.55)}
.dx__btn--ghost{background:transparent;color:var(--dx-teal)!important}
.dx__btn--soft{background:var(--dx-champ);border-color:var(--dx-champ);color:var(--dx-teal)!important}
.dx__btn svg{width:18px;height:18px;flex:none}
.dx a:focus-visible,.dx button:focus-visible,.dx input:focus-visible+label,.dx input:focus-visible{outline:3px solid var(--dx-gold);outline-offset:3px}
.dx__link{color:var(--dx-teal);font-weight:500;text-decoration:underline;text-decoration-color:var(--dx-gold);text-underline-offset:4px}
.dx__card{background:var(--dx-white);border:1px solid var(--dx-line);border-radius:var(--dx-r);padding:24px}
.dx__sr{position:absolute!important;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0);white-space:nowrap}
@media (min-width:640px){.dx{padding:80px 32px}.dx__btn{width:auto}}
@media (prefers-reduced-motion:reduce){.dx *{transition:none!important;animation:none!important}}
.dx-org{background:var(--dx-cream)}
.dx-org__grid{display:grid;gap:22px;margin-top:26px}
.dx-org__flow{list-style:none;margin:0;padding:0;display:grid;gap:12px}
.dx-org__flow li{display:flex;gap:14px;align-items:flex-start;background:var(--dx-white);border:1px solid var(--dx-line);border-radius:var(--dx-r);padding:18px 20px}
.dx-org__flow b{flex:none;display:grid;place-items:center;width:34px;height:34px;border-radius:50%;background:var(--dx-teal);color:var(--dx-cream);font-weight:700;font-size:.95rem}
.dx-org__flow p{margin:0}
.dx-org__count{background:var(--dx-white);border:1px solid var(--dx-gold);border-radius:var(--dx-r);padding:24px 22px}
.dx-org__count h3{margin-bottom:4px}
.dx-org__count>p{color:var(--dx-soft);font-size:.95rem}
.dx-org__kinds{list-style:none;margin:0 0 18px;padding:0;display:flex;flex-wrap:wrap;gap:8px}
.dx-org__kinds li{padding:6px 14px;border-radius:99px;background:var(--dx-ivory);font-size:.9rem;font-weight:500}
.dx-org__stepper{display:flex;align-items:center;gap:14px}
.dx-org__stepper button{width:48px;height:48px;border-radius:50%;border:2px solid var(--dx-teal);background:var(--dx-white);color:var(--dx-teal);font:500 1.5rem/1 'Jost',system-ui,sans-serif;cursor:pointer}
.dx-org__stepper button:disabled{opacity:.4;cursor:not-allowed}
.dx-org__n{min-width:56px;text-align:center;font-weight:700;font-size:2.2rem;line-height:1;color:var(--dx-teal)}
.dx-org__result{margin:14px 0 0!important;font-weight:500}
@media (min-width:860px){.dx-org__grid{grid-template-columns:1.1fr .9fr;align-items:start}}
</style>
<div class="dx__in">
  <p class="dx__eyebrow">Step 3 · Your organizer</p>
  <h2 id="dx-org-title">How your organizer works</h2>
  <p class="dx__sub">You'll find your organizer inside your TaxDome portal.</p>
  <div class="dx-org__grid">
    <ol class="dx-org__flow">
      <li><b aria-hidden="true">1</b><p>The organizer first asks how many companies or entities you have.</p></li>
      <li><b aria-hidden="true">2</b><p>It then opens a section for each one, so you can tell us about every entity separately.</p></li>
      <li><b aria-hidden="true">3</b><p><strong>Be thorough.</strong> Include side businesses, rentals and nonprofits.</p></li>
    </ol>
    <div class="dx-org__count">
      <h3 id="dx-org-count-title">Count them before you start</h3>
      <p>Did you include all of these?</p>
      <ul class="dx-org__kinds"><li>Main business</li><li>Side businesses</li><li>Rentals</li><li>Nonprofits</li></ul>
      <div class="dx-org__stepper" role="group" aria-labelledby="dx-org-count-title">
        <button type="button" data-dx-org="-1" aria-label="One fewer entity">−</button>
        <span class="dx-org__n" data-dx-org-n>1</span>
        <button type="button" data-dx-org="1" aria-label="One more entity">+</button>
      </div>
      <p class="dx-org__result" aria-live="polite">Your organizer will open <span data-dx-org-text>1 section</span>.</p>
    </div>
  </div>
</div>
<script>
(function(){
  var root=document.getElementById('organizer'); if(!root) return;
  var n=1, out=root.querySelector('[data-dx-org-n]'), txt=root.querySelector('[data-dx-org-text]'), btns=root.querySelectorAll('[data-dx-org]');
  function draw(){out.textContent=n;txt.textContent=n+(n===1?' section':' sections');btns[0].disabled=n<=1;btns[1].disabled=n>=25;}
  btns.forEach(function(b){b.addEventListener('click',function(){n=Math.min(25,Math.max(1,n+parseInt(b.getAttribute('data-dx-org'),10)));draw();});});
  draw();
})();
</script>
</section>
```

## SECTION 7: 60-Day Deadline (`#deadline`)

**GHL build note:** Section: full width, background #FFFFFF, padding 0. Static text only: no countdown. Add a 1-column row, then a **Custom Code** element, and paste the block below. Paste-ready file: `ghl-blocks/07-deadline.html`.

```html
<!-- ===== SECTION 7: 60-DAY DEADLINE (#deadline) ===== -->
<section id="deadline" class="dx dx-dead" tabindex="-1" aria-labelledby="dx-dead-title">
<style>
@import url('https://fonts.googleapis.com/css2?family=Jost:wght@400;500;700&display=swap');
/* Distinct brand tokens (from The Distinct Experience Guide, 2026) */
.dx{--dx-teal:#003b42;--dx-gold:#b18132;--dx-gold-dk:#96691c;--dx-champ:#e6cd96;--dx-ivory:#f3ede1;--dx-cream:#fbf8f2;--dx-white:#ffffff;--dx-sage:#8fa5a2;--dx-line:rgba(177,129,50,.30);--dx-soft:rgba(0,59,66,.80);--dx-r:18px;--dx-r-sm:12px;
  display:block;box-sizing:border-box;font-family:'Jost',system-ui,-apple-system,'Segoe UI',sans-serif;font-weight:400;font-size:17px;line-height:1.6;color:var(--dx-teal);background:var(--dx-cream);padding:56px 20px;scroll-margin-top:16px;-webkit-font-smoothing:antialiased}
.dx *,.dx *::before,.dx *::after{box-sizing:border-box}
.dx:focus{outline:none}
.dx__in{max-width:980px;margin:0 auto}
.dx h1,.dx h2,.dx h3{font-family:inherit;font-weight:700;color:var(--dx-teal);margin:0;letter-spacing:-.01em}
.dx h2{font-size:clamp(1.65rem,5.2vw,2.4rem);line-height:1.15;margin-bottom:14px}
.dx h3{font-size:1.2rem;line-height:1.3;margin-bottom:6px}
.dx p{margin:0 0 14px}
.dx__eyebrow{display:flex;align-items:center;gap:12px;margin:0 0 12px;font-weight:500;font-size:.78rem;letter-spacing:.16em;text-transform:uppercase;color:var(--dx-gold-dk)}
.dx__eyebrow::before{content:"";flex:0 0 40px;height:2px;border-radius:2px;background:var(--dx-gold)}
.dx__sub{font-weight:500;font-size:1.08rem;color:var(--dx-soft);max-width:640px}
.dx__btn{display:inline-flex;align-items:center;justify-content:center;gap:10px;min-height:52px;padding:14px 26px;border-radius:999px;border:2px solid var(--dx-teal);background:var(--dx-teal);color:var(--dx-cream)!important;font:500 1rem/1.2 'Jost',system-ui,sans-serif;letter-spacing:.02em;text-decoration:none!important;cursor:pointer;transition:transform .2s ease,box-shadow .2s ease;width:100%}
.dx__btn:hover{transform:translateY(-1px);box-shadow:0 10px 24px -12px rgba(0,59,66,.55)}
.dx__btn--ghost{background:transparent;color:var(--dx-teal)!important}
.dx__btn--soft{background:var(--dx-champ);border-color:var(--dx-champ);color:var(--dx-teal)!important}
.dx__btn svg{width:18px;height:18px;flex:none}
.dx a:focus-visible,.dx button:focus-visible,.dx input:focus-visible+label,.dx input:focus-visible{outline:3px solid var(--dx-gold);outline-offset:3px}
.dx__link{color:var(--dx-teal);font-weight:500;text-decoration:underline;text-decoration-color:var(--dx-gold);text-underline-offset:4px}
.dx__card{background:var(--dx-white);border:1px solid var(--dx-line);border-radius:var(--dx-r);padding:24px}
.dx__sr{position:absolute!important;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0);white-space:nowrap}
@media (min-width:640px){.dx{padding:80px 32px}.dx__btn{width:auto}}
@media (prefers-reduced-motion:reduce){.dx *{transition:none!important;animation:none!important}}
.dx-dead{background:var(--dx-white)}
.dx-dead__card{position:relative;display:grid;gap:18px;background:rgba(230,205,150,.32);border:2px solid var(--dx-gold);border-radius:calc(var(--dx-r) + 6px);padding:28px 22px}
.dx-dead__icon{width:64px;height:64px;border-radius:18px;background:var(--dx-white);border:1px solid var(--dx-line);display:grid;place-items:center}
.dx-dead__icon svg{width:32px;height:32px;stroke:var(--dx-teal)}
.dx-dead__card h2{margin-bottom:10px}
.dx-dead__card p{font-size:1.05rem}
.dx-dead__card p:last-child{margin-bottom:0}
@media (min-width:760px){.dx-dead__card{grid-template-columns:auto 1fr;gap:26px;padding:36px 36px}}
</style>
<div class="dx__in">
  <div class="dx-dead__card" role="note">
    <div class="dx-dead__icon" aria-hidden="true">
      <svg viewBox="0 0 24 24" fill="none" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="5" width="18" height="16" rx="3"/><path d="M8 3v4M16 3v4M3 10h18"/><path d="M10 15h4"/></svg>
    </div>
    <div>
      <p class="dx__eyebrow">Important</p>
      <h2 id="dx-dead-title">You have 60 days to upload your documents</h2>
      <p>You have 60 days from your payment date to upload your documents.</p>
      <p>After 60 days, your account goes inactive. To continue, you would pay the consultation fee again at whatever it is that day.</p>
      <p><strong>Your assessment fee is non-refundable.</strong></p>
    </div>
  </div>
</div>
</section>
```

## SECTION 8: What Happens Next (`#what-next`)

**GHL build note:** Section: full width, background #FBF8F2, padding 0. Add a 1-column row, then a **Custom Code** element, and paste the block below. Paste-ready file: `ghl-blocks/08-what-next.html`.

```html
<!-- ===== SECTION 8: WHAT HAPPENS NEXT (#what-next) ===== -->
<section id="what-next" class="dx dx-next" tabindex="-1" aria-labelledby="dx-next-title">
<style>
@import url('https://fonts.googleapis.com/css2?family=Jost:wght@400;500;700&display=swap');
/* Distinct brand tokens (from The Distinct Experience Guide, 2026) */
.dx{--dx-teal:#003b42;--dx-gold:#b18132;--dx-gold-dk:#96691c;--dx-champ:#e6cd96;--dx-ivory:#f3ede1;--dx-cream:#fbf8f2;--dx-white:#ffffff;--dx-sage:#8fa5a2;--dx-line:rgba(177,129,50,.30);--dx-soft:rgba(0,59,66,.80);--dx-r:18px;--dx-r-sm:12px;
  display:block;box-sizing:border-box;font-family:'Jost',system-ui,-apple-system,'Segoe UI',sans-serif;font-weight:400;font-size:17px;line-height:1.6;color:var(--dx-teal);background:var(--dx-cream);padding:56px 20px;scroll-margin-top:16px;-webkit-font-smoothing:antialiased}
.dx *,.dx *::before,.dx *::after{box-sizing:border-box}
.dx:focus{outline:none}
.dx__in{max-width:980px;margin:0 auto}
.dx h1,.dx h2,.dx h3{font-family:inherit;font-weight:700;color:var(--dx-teal);margin:0;letter-spacing:-.01em}
.dx h2{font-size:clamp(1.65rem,5.2vw,2.4rem);line-height:1.15;margin-bottom:14px}
.dx h3{font-size:1.2rem;line-height:1.3;margin-bottom:6px}
.dx p{margin:0 0 14px}
.dx__eyebrow{display:flex;align-items:center;gap:12px;margin:0 0 12px;font-weight:500;font-size:.78rem;letter-spacing:.16em;text-transform:uppercase;color:var(--dx-gold-dk)}
.dx__eyebrow::before{content:"";flex:0 0 40px;height:2px;border-radius:2px;background:var(--dx-gold)}
.dx__sub{font-weight:500;font-size:1.08rem;color:var(--dx-soft);max-width:640px}
.dx__btn{display:inline-flex;align-items:center;justify-content:center;gap:10px;min-height:52px;padding:14px 26px;border-radius:999px;border:2px solid var(--dx-teal);background:var(--dx-teal);color:var(--dx-cream)!important;font:500 1rem/1.2 'Jost',system-ui,sans-serif;letter-spacing:.02em;text-decoration:none!important;cursor:pointer;transition:transform .2s ease,box-shadow .2s ease;width:100%}
.dx__btn:hover{transform:translateY(-1px);box-shadow:0 10px 24px -12px rgba(0,59,66,.55)}
.dx__btn--ghost{background:transparent;color:var(--dx-teal)!important}
.dx__btn--soft{background:var(--dx-champ);border-color:var(--dx-champ);color:var(--dx-teal)!important}
.dx__btn svg{width:18px;height:18px;flex:none}
.dx a:focus-visible,.dx button:focus-visible,.dx input:focus-visible+label,.dx input:focus-visible{outline:3px solid var(--dx-gold);outline-offset:3px}
.dx__link{color:var(--dx-teal);font-weight:500;text-decoration:underline;text-decoration-color:var(--dx-gold);text-underline-offset:4px}
.dx__card{background:var(--dx-white);border:1px solid var(--dx-line);border-radius:var(--dx-r);padding:24px}
.dx__sr{position:absolute!important;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0);white-space:nowrap}
@media (min-width:640px){.dx{padding:80px 32px}.dx__btn{width:auto}}
@media (prefers-reduced-motion:reduce){.dx *{transition:none!important;animation:none!important}}
.dx-next{background:var(--dx-cream)}
.dx-next__line{list-style:none;margin:28px 0 0;padding:0;display:grid;gap:0}
.dx-next__line li{position:relative;padding:0 0 28px 54px}
.dx-next__line li:last-child{padding-bottom:0}
.dx-next__line li::before{content:"";position:absolute;left:17px;top:38px;bottom:4px;width:2px;background:var(--dx-line)}
.dx-next__line li:last-child::before{display:none}
.dx-next__dot{position:absolute;left:0;top:0;width:36px;height:36px;border-radius:50%;background:var(--dx-white);border:2px solid var(--dx-gold);display:grid;place-items:center;font-weight:700;color:var(--dx-teal)}
.dx-next__line h3{padding-top:4px}
.dx-next__line p{color:var(--dx-soft);margin:0}
@media (min-width:860px){
  .dx-next__line{grid-template-columns:repeat(3,1fr);gap:22px}
  .dx-next__line li{padding:52px 0 0 0}
  .dx-next__line li::before{left:44px;right:-22px;top:17px;bottom:auto;width:auto;height:2px}
}
</style>
<div class="dx__in">
  <p class="dx__eyebrow">After you submit</p>
  <h2 id="dx-next-title">What happens next</h2>
  <ol class="dx-next__line">
    <li><span class="dx-next__dot" aria-hidden="true">1</span><h3>Our team reviews your documents</h3><p>Once you submit, our team reviews everything you've uploaded.</p></li>
    <li><span class="dx-next__dot" aria-hidden="true">2</span><h3>We'll tell you if anything is missing</h3><p>If anything is missing, we'll let you know.</p></li>
    <li><span class="dx-next__dot" aria-hidden="true">3</span><h3>You book your assessment call</h3><p>Once everything is ready, we'll email you a private link to book your assessment call.</p></li>
  </ol>
</div>
</section>
```

## SECTION 9: Security (`#security`)

**GHL build note:** Section: full width, background #FFFFFF, padding 0. This block repeats the [TAXDOME PORTAL LINK] button. Add a 1-column row, then a **Custom Code** element, and paste the block below. Paste-ready file: `ghl-blocks/09-security.html`.

```html
<!-- ===== SECTION 9: SECURITY (#security) ===== -->
<section id="security" class="dx dx-sec" tabindex="-1" aria-labelledby="dx-sec-title">
<style>
@import url('https://fonts.googleapis.com/css2?family=Jost:wght@400;500;700&display=swap');
/* Distinct brand tokens (from The Distinct Experience Guide, 2026) */
.dx{--dx-teal:#003b42;--dx-gold:#b18132;--dx-gold-dk:#96691c;--dx-champ:#e6cd96;--dx-ivory:#f3ede1;--dx-cream:#fbf8f2;--dx-white:#ffffff;--dx-sage:#8fa5a2;--dx-line:rgba(177,129,50,.30);--dx-soft:rgba(0,59,66,.80);--dx-r:18px;--dx-r-sm:12px;
  display:block;box-sizing:border-box;font-family:'Jost',system-ui,-apple-system,'Segoe UI',sans-serif;font-weight:400;font-size:17px;line-height:1.6;color:var(--dx-teal);background:var(--dx-cream);padding:56px 20px;scroll-margin-top:16px;-webkit-font-smoothing:antialiased}
.dx *,.dx *::before,.dx *::after{box-sizing:border-box}
.dx:focus{outline:none}
.dx__in{max-width:980px;margin:0 auto}
.dx h1,.dx h2,.dx h3{font-family:inherit;font-weight:700;color:var(--dx-teal);margin:0;letter-spacing:-.01em}
.dx h2{font-size:clamp(1.65rem,5.2vw,2.4rem);line-height:1.15;margin-bottom:14px}
.dx h3{font-size:1.2rem;line-height:1.3;margin-bottom:6px}
.dx p{margin:0 0 14px}
.dx__eyebrow{display:flex;align-items:center;gap:12px;margin:0 0 12px;font-weight:500;font-size:.78rem;letter-spacing:.16em;text-transform:uppercase;color:var(--dx-gold-dk)}
.dx__eyebrow::before{content:"";flex:0 0 40px;height:2px;border-radius:2px;background:var(--dx-gold)}
.dx__sub{font-weight:500;font-size:1.08rem;color:var(--dx-soft);max-width:640px}
.dx__btn{display:inline-flex;align-items:center;justify-content:center;gap:10px;min-height:52px;padding:14px 26px;border-radius:999px;border:2px solid var(--dx-teal);background:var(--dx-teal);color:var(--dx-cream)!important;font:500 1rem/1.2 'Jost',system-ui,sans-serif;letter-spacing:.02em;text-decoration:none!important;cursor:pointer;transition:transform .2s ease,box-shadow .2s ease;width:100%}
.dx__btn:hover{transform:translateY(-1px);box-shadow:0 10px 24px -12px rgba(0,59,66,.55)}
.dx__btn--ghost{background:transparent;color:var(--dx-teal)!important}
.dx__btn--soft{background:var(--dx-champ);border-color:var(--dx-champ);color:var(--dx-teal)!important}
.dx__btn svg{width:18px;height:18px;flex:none}
.dx a:focus-visible,.dx button:focus-visible,.dx input:focus-visible+label,.dx input:focus-visible{outline:3px solid var(--dx-gold);outline-offset:3px}
.dx__link{color:var(--dx-teal);font-weight:500;text-decoration:underline;text-decoration-color:var(--dx-gold);text-underline-offset:4px}
.dx__card{background:var(--dx-white);border:1px solid var(--dx-line);border-radius:var(--dx-r);padding:24px}
.dx__sr{position:absolute!important;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0);white-space:nowrap}
@media (min-width:640px){.dx{padding:80px 32px}.dx__btn{width:auto}}
@media (prefers-reduced-motion:reduce){.dx *{transition:none!important;animation:none!important}}
.dx-sec{background:var(--dx-white)}
.dx-sec__card{display:grid;gap:18px;border:2px solid var(--dx-teal);border-radius:calc(var(--dx-r) + 6px);padding:28px 22px;background:var(--dx-cream)}
.dx-sec__icon{width:64px;height:64px;border-radius:50%;background:var(--dx-teal);display:grid;place-items:center}
.dx-sec__icon svg{width:30px;height:30px;stroke:var(--dx-cream)}
.dx-sec__card p{font-size:1.08rem}
@media (min-width:760px){.dx-sec__card{grid-template-columns:auto 1fr auto;align-items:center;gap:28px;padding:32px 36px}.dx-sec__card p{margin:0}}
</style>
<div class="dx__in">
  <div class="dx-sec__card">
    <div class="dx-sec__icon" aria-hidden="true">
      <svg viewBox="0 0 24 24" fill="none" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><rect x="4" y="10" width="16" height="11" rx="3"/><path d="M8 10V7a4 4 0 0 1 8 0v3"/></svg>
    </div>
    <div>
      <h2 id="dx-sec-title">Keep your documents secure</h2>
      <p>For your security, upload tax documents only in TaxDome. Never send them by regular email or text.</p>
    </div>
    <a class="dx__btn" href="[TAXDOME PORTAL LINK]" target="_blank" rel="noopener">Log in to TaxDome<span class="dx__sr">(opens in a new tab)</span></a>
  </div>
</div>
</section>
```

## SECTION 10: Footer (`#footer`)

**GHL build note:** Section: full width, background #F3EDE1, padding 0. Turn off GHL's default footer, if your funnel has one, to avoid two footers. Add a 1-column row, then a **Custom Code** element, and paste the block below. Paste-ready file: `ghl-blocks/10-footer.html`.

```html
<!-- ===== SECTION 10: FOOTER (#footer) ===== -->
<footer id="footer" class="dx dx-foot" tabindex="-1" aria-label="Distinct Tax Consulting Group® contact information">
<style>
@import url('https://fonts.googleapis.com/css2?family=Jost:wght@400;500;700&display=swap');
/* Distinct brand tokens (from The Distinct Experience Guide, 2026) */
.dx{--dx-teal:#003b42;--dx-gold:#b18132;--dx-gold-dk:#96691c;--dx-champ:#e6cd96;--dx-ivory:#f3ede1;--dx-cream:#fbf8f2;--dx-white:#ffffff;--dx-sage:#8fa5a2;--dx-line:rgba(177,129,50,.30);--dx-soft:rgba(0,59,66,.80);--dx-r:18px;--dx-r-sm:12px;
  display:block;box-sizing:border-box;font-family:'Jost',system-ui,-apple-system,'Segoe UI',sans-serif;font-weight:400;font-size:17px;line-height:1.6;color:var(--dx-teal);background:var(--dx-cream);padding:56px 20px;scroll-margin-top:16px;-webkit-font-smoothing:antialiased}
.dx *,.dx *::before,.dx *::after{box-sizing:border-box}
.dx:focus{outline:none}
.dx__in{max-width:980px;margin:0 auto}
.dx h1,.dx h2,.dx h3{font-family:inherit;font-weight:700;color:var(--dx-teal);margin:0;letter-spacing:-.01em}
.dx h2{font-size:clamp(1.65rem,5.2vw,2.4rem);line-height:1.15;margin-bottom:14px}
.dx h3{font-size:1.2rem;line-height:1.3;margin-bottom:6px}
.dx p{margin:0 0 14px}
.dx__eyebrow{display:flex;align-items:center;gap:12px;margin:0 0 12px;font-weight:500;font-size:.78rem;letter-spacing:.16em;text-transform:uppercase;color:var(--dx-gold-dk)}
.dx__eyebrow::before{content:"";flex:0 0 40px;height:2px;border-radius:2px;background:var(--dx-gold)}
.dx__sub{font-weight:500;font-size:1.08rem;color:var(--dx-soft);max-width:640px}
.dx__btn{display:inline-flex;align-items:center;justify-content:center;gap:10px;min-height:52px;padding:14px 26px;border-radius:999px;border:2px solid var(--dx-teal);background:var(--dx-teal);color:var(--dx-cream)!important;font:500 1rem/1.2 'Jost',system-ui,sans-serif;letter-spacing:.02em;text-decoration:none!important;cursor:pointer;transition:transform .2s ease,box-shadow .2s ease;width:100%}
.dx__btn:hover{transform:translateY(-1px);box-shadow:0 10px 24px -12px rgba(0,59,66,.55)}
.dx__btn--ghost{background:transparent;color:var(--dx-teal)!important}
.dx__btn--soft{background:var(--dx-champ);border-color:var(--dx-champ);color:var(--dx-teal)!important}
.dx__btn svg{width:18px;height:18px;flex:none}
.dx a:focus-visible,.dx button:focus-visible,.dx input:focus-visible+label,.dx input:focus-visible{outline:3px solid var(--dx-gold);outline-offset:3px}
.dx__link{color:var(--dx-teal);font-weight:500;text-decoration:underline;text-decoration-color:var(--dx-gold);text-underline-offset:4px}
.dx__card{background:var(--dx-white);border:1px solid var(--dx-line);border-radius:var(--dx-r);padding:24px}
.dx__sr{position:absolute!important;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0);white-space:nowrap}
@media (min-width:640px){.dx{padding:80px 32px}.dx__btn{width:auto}}
@media (prefers-reduced-motion:reduce){.dx *{transition:none!important;animation:none!important}}
.dx-foot{background:var(--dx-ivory);border-top:1px solid var(--dx-line);padding-bottom:40px}
.dx-foot__grid{display:grid;gap:30px}
.dx-foot__sign{font-size:1.05rem}
.dx-foot__sign .dx-foot__hand{display:block;font-weight:500;font-size:1.5rem;margin-bottom:6px}
.dx-foot__sign strong{display:block;font-weight:700}
.dx-foot__sign span{display:block;color:var(--dx-soft)}
.dx-foot__firm{font-weight:700;font-size:1.1rem;margin-bottom:8px!important}
.dx-foot address{font-style:normal;margin-bottom:14px}
.dx-foot__rule{height:2px;width:48px;border-radius:2px;background:var(--dx-gold);margin:0 0 18px}
.dx-foot__bottom{display:flex;flex-wrap:wrap;justify-content:space-between;gap:12px;margin-top:36px;padding-top:18px;border-top:1px solid var(--dx-line);font-size:.85rem}
.dx-foot__bottom p{margin:0}
@media (min-width:760px){.dx-foot__grid{grid-template-columns:1fr 1fr;gap:48px}}
</style>
<div class="dx__in">
  <div class="dx-foot__grid">
    <div class="dx-foot__sign">
      <div class="dx-foot__rule" aria-hidden="true"></div>
      <span class="dx-foot__hand">Have a distinct day,</span>
      <strong>Alysha Pruitt Harvey, MAcc, EA</strong>
      <span>Founder and Managing Partner</span>
    </div>
    <div>
      <p class="dx-foot__firm">Distinct Tax Consulting Group®</p>
      <address>4751 Best Road, Suite 332<br>Atlanta, GA 30337</address>
      <p><strong>Questions?</strong> Reply to any of our emails.</p>
    </div>
  </div>
  <div class="dx-foot__bottom">
    <p>© <span data-dx-year>2026</span> Distinct Tax Consulting Group®. All rights reserved.</p>
    <p><a class="dx__link" href="#welcome">Back to top ↑</a></p>
  </div>
</div>
<script>(function(){var y=document.querySelector('#footer [data-dx-year]');if(y)y.textContent=new Date().getFullYear();})();</script>
</footer>
```

## Every placeholder still on the page

| # | Placeholder | Where | What to supply |
|---|---|---|---|
| 1 | `[LOGO]` (and `[LOGO IMAGE URL]` in the comment) | Section 1 `#welcome` | The approved Distinct logo, **not** the gold "I" version. Replace the placeholder div with the `<img>` tag in the comment. Alt text is already set: "Distinct Tax Consulting Group®". |
| 2 | `[WELCOME VIDEO EMBED CODE]` / `[WELCOME VIDEO EMBED URL]` | Section 3 `#welcome-video` | The embed iframe once the welcome video is recorded. |
| 3 | `[TAXDOME SET-UP VIDEO EMBED CODE]` / `[TAXDOME SET-UP VIDEO EMBED URL]` | Section 4 `#taxdome-video` | The embed iframe once the TaxDome walkthrough is recorded. |
| 4 | `[TAXDOME PORTAL LINK]` | Section 4 button **and** Section 9 button | Your TaxDome client login URL. Both buttons use it. |
| 5 | `[IMAGE: PRIOR TAX RETURN MOCK-UP]` | Section 5 `#checklist`, card 1 | Redacted or sample mock-up. Alt text: "Sample first page of a prior-year tax return". |
| 6 | `[IMAGE: YEAR-TO-DATE PROFIT AND LOSS MOCK-UP]` | Section 5, card 2 | Mock-up image. Alt text: "Sample year-to-date profit and loss report". |
| 7 | `[IMAGE: IRS OR STATE LETTER MOCK-UP]` | Section 5, card 3 | Mock-up image. Alt text: "Sample IRS or state tax notice letter". |
| 8 | Document list (HTML comment "ALYSHA TO CONFIRM") | Section 5 | Alysha confirms the three documents and their "where to find it" lines. To add a document, copy a `<li class="dx-doc">` block. The counter updates itself. |

Image mock-ups work best at a 4:3 ratio, about 1200 × 900 px. Make sure no real client data is visible.

## Anchor URLs for the reminder emails

Once the page is published, replace `<page URL>` with the step's live URL (for example `https://yourdomain.com/next-steps`):

| Email placeholder | Link to use |
|---|---|
| `[WELCOME VIDEO LINK]` | `<page URL>#welcome-video` |
| `[TAXDOME ACCOUNT VIDEO LINK]` | `<page URL>#taxdome-video` |
| `[CHECKLIST LINK]` | `<page URL>#checklist` |
| `[TAXDOME PORTAL LINK]` | Stays the **TaxDome login URL**, not this page |

Other anchors you can use: `#steps`, `#organizer`, `#deadline`, `#what-next`, `#security`.

## Adding this page as the thank-you step after the $500 checkout

GHL menu labels move between versions. If a name below doesn't match your screen, look for the nearest equivalent.

1. **Open the funnel.** In the Distinct Tax Consulting Group® sub-account, go to **Sites → Funnels** and open the funnel that holds the $500 Distinct® Tax Assessment checkout.
2. **Add the step.** On the **Steps** list, click **+ Add New Step**. Name it `Next Steps` and set the path to `next-steps`, or whatever path you want in the URL.
3. **Put it right after the checkout.** Drag the new step so it sits directly below the checkout step. If you already have an upsell or order-confirmation step, place it after the last step the buyer sees before they're done.
4. **Open the builder.** Click **Edit** on the new step and start from a blank page.
5. **Paste the global head code.** In the builder, open **Settings → Tracking Code → Head**. Paste the *Global head code* block and save. Also set the page background color to `#FBF8F2`.
6. **Build the sections, top to bottom.** For each of the 10 blocks, in order:
   - Add a **Section** and set it to **Full Width**. Set top and bottom padding (and margins) to **0**, because each block has its own spacing.
   - Add a **1-column Row**. Set its padding to 0 and its width to full.
   - Drag in a **Custom Code** element (shown as *Code* or *Custom JS/HTML* in some builder versions). Click **Open Code Editor**, paste the block and save.
   - Optional: rename the section in the left Layers panel, for example `S3 – Welcome Video`, so it's easy to find later.
7. **Hide GHL extras.** Remove any default header or footer GHL added, so the page has one footer (Section 10).
8. **Set the checkout's next step.** Open the checkout step in the builder and select the **Order Form** element. Make sure that after a successful payment it goes to the **next step in the funnel**, which is the default. If it's set to redirect to a URL, change it to this new step or paste this step's URL. Save.
9. **Save and preview.** Use **Preview** at phone and desktop sizes. Tap each step button to confirm it jumps to the right section.
10. **Publish and copy the URL.** Publish the funnel. Copy the Next Steps URL from the step's overview (domain plus funnel path plus `/next-steps`). Use it as `<page URL>` in the anchor links above.
11. **Test a real purchase.** Run a test purchase with your payment provider in test mode, or use a 100% coupon if you use one. Confirm the buyer lands on the Next Steps page after paying.
12. **Swap placeholders as assets arrive.** When the videos, logo, mock-ups and TaxDome link are ready, edit only the matching Custom Code element (see the placeholder table).

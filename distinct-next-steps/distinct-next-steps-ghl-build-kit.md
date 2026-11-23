# Distinct® Tax Assessment: Next Steps page (GHL build kit)

Post-payment thank-you step for Distinct Tax Consulting Group®. It sits right after the $500 Distinct® Tax Assessment checkout.

- **Layout:** single page, mobile-first, 11 sections (1, 1B, then 2 through 10). Each section is one GHL **Custom Code** element.
- **Self-contained:** each block carries its own CSS (brand tokens included) and its own small vanilla script where needed. There are no external frameworks. Jost is the only external file, loaded from Google Fonts.
- **Live preview:** `index.html`, the whole page assembled from these same blocks.
- **Paste-ready files:** `ghl-blocks/00-global-head.html` to `ghl-blocks/10-footer.html` (including `01b-transformation.html`). These are the same code as below.

## Brand palette in use

**Dark teal is the lead color.** The hero, the video, the organizer, "What happens next" and the footer are full teal sections. The step cards, notes, the deadline card and the video frames are teal too. White and a pale teal-gray are used only where people read lists. Gold is the accent. There is no beige.

Colors come from your Canva designs from Nov 5, 2026 onward: Business Cards, Capability Statement, Letterhead, Experience Guide and Referral deck.

| Token | Hex | Used for | Contrast |
|---|---|---|---|
| Teal (lead) | `#003B42` | Main section color, cards, headings on white, buttons on white | Ivory text on it 10.6:1 ✔ |
| Deep teal | `#01262B` | "What happens next" and footer; end of the teal gradient (business cards) | Ivory 13.7:1 ✔ · Champagne 10.3:1 ✔ |
| Teal gradient | `#04333A → #003B42 → #01262B` | Teal sections and cards (business card gradient) | |
| Champagne | `#E6CD96` | Accent words, labels and links on teal | 7.9:1 on teal ✔ |
| Gold gradient | `#F1E2B8 → #E6CD96 → #D9B878` | Buttons and number badges on teal, with teal text (from your QR card gradient) | Teal text 7.9–9.6:1 ✔ |
| Gold | `#B18132` | Accent words on white, rules, diamond bullets, borders | Heading size or decoration only |
| Ivory | `#F3EDE1` | Headings and key text on teal | 10.6:1 ✔ |
| Mist | `#C9D6D2` | Body text on teal (your secondary text on dark) | 8.2:1 ✔ |
| Slate | `#3B4F52` | Body text on white | 8.7:1 ✔ |
| White / pale teal-gray | `#FFFFFF` / `#F2F6F6` | Reading areas: step cards area, checklist, deadline, security | |

**Brand motifs:**
- the double hairline inset frame and concentric circle rings (business cards)
- the gold gradient on numbers and buttons
- one *italic accent word* per heading
- gold diamond bullets
- the tagline *Protect More. Keep More. Build More.*

**Moving parts (no checkboxes, nothing to save):**
- **Turning words:** the hero promise flips through *Highly valued. → Financially redefined. → Peace of mind obtained.* The organizer card cycles *main business → side businesses → rentals → nonprofits.*
- **The transformation (Section 1B, right after the hero):** six tiles start as the burdens people arrive with: *Worry, Confusion, Guessing, Feeling behind, Carrying it alone, Shame.* As the section scrolls into view, a gold line strikes through each one in turn, and it becomes its outcome: *Peace of mind, Clarity, A plan, Moving forward, A team beside you, No judgment.* A soft gold "sunrise" glow rises behind them. It plays once, with a "See it again" button. It is not a loop.
- **Flip cards:** the 3 step cards and 3 document cards turn over on tap or click. The first card gives a small "peek" turn when it comes into view, to show it flips.
- **Scroll-in:** sections slide in gently as visitors scroll.
- **Accessibility:** the turning words have a **Pause motion** button and stop on hover. Visitors who turn on "reduce motion" see the words written out and the transformation already complete, with nothing moving. Nothing strobes, and there are no countdown timers.

**Distinct® keywords on the page and where they come from:**
- **The Distinct® Experience:** Client Onboarding Master Deck p1 and Experience Guide
- **Highly valued. Financially redefined. Peace of mind obtained.:** Experience Guide p1/p3, Master Deck p16
- **Protect More. Keep More. Build More.:** Systems Update deck
- **Judgment-free:** Master Deck p5
- **Clarity · Confidence · Legacy:** DTCG social post, Nov 26
- **Have a distinct day:** your sign-off

**Type:** Jost 700 for headings (700 italic for the accent word), 500 for subheads and buttons, 400 for body. **Shape:** 20px corners on cards and video frames, pill-shaped buttons.

## Anchors

`#welcome` · `#transformation` · `#steps` · `#welcome-video` · `#taxdome-video` · `#checklist` · `#organizer` · `#deadline` · `#what-next` · `#security` · `#footer`

Every section is a real landmark with a heading, so keyboard and screen-reader users land in the right place when they follow an anchor link. It has `tabindex="-1"` and a `scroll-margin-top` offset.

## Global head code (paste once)

Paste in the funnel step: **Settings → Tracking Code → Head**. It loads Jost, turns on smooth scrolling and the gentle scroll-in animation, and keeps this page out of search results. If you skip it, everything still shows, just without the animation.

```html
<!-- Distinct Next Steps: GLOBAL HEAD CODE (paste once in GHL: step Settings > Tracking Code > Head) -->
<meta name="robots" content="noindex, nofollow">
<meta name="theme-color" content="#003b42">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Jost:ital,wght@0,400;0,500;0,700;1,500;1,700&display=swap" rel="stylesheet">
<style>
  html{scroll-behavior:smooth}
  @media (prefers-reduced-motion:reduce){html{scroll-behavior:auto}}
  body{background:#ffffff}
</style>
<script>
/* Scroll-reveal for Distinct sections. Content stays visible if this script is missing. */
(function(){
  if(!('IntersectionObserver' in window)) return;
  document.documentElement.classList.add('dx-js');
  function go(){
    var io=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){e.target.classList.add('is-in');io.unobserve(e.target);}});},{rootMargin:'0px 0px -8% 0px'});
    document.querySelectorAll('.dx [data-reveal]').forEach(function(el){io.observe(el);});
  }
  if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',go);else go();
})();
</script>
```

## SECTION 1: Welcome (`#welcome`)

**GHL build note:** Section: full width, background #003B42, padding 0. Dark-teal hero with the turning promise line and its Pause motion button. This is the only H1 on the page. Add a 1-column row, then a **Custom Code** element, and paste the block below. Paste-ready file: `ghl-blocks/01-welcome.html`.

```html
<!-- ===== SECTION 1: WELCOME (#welcome) ===== -->
<section id="welcome" class="dx dx--teal dx-hero" tabindex="-1" aria-labelledby="dx-welcome-title">
<style>
@import url('https://fonts.googleapis.com/css2?family=Jost:ital,wght@0,400;0,500;0,700;1,500;1,700&display=swap');
/* Distinct brand tokens (DTCG Canva designs, Nov 2026). Dark teal leads; gold accents; white for reading areas. */
.dx{--dx-teal:#003b42;--dx-deep:#01262b;--dx-teal-hi:#04333a;--dx-gold:#b18132;--dx-gold-dk:#96691c;--dx-champ:#e6cd96;--dx-champ-hi:#f1e2b8;--dx-ivory:#f3ede1;--dx-mist:#c9d6d2;--dx-body:#3b4f52;--dx-white:#ffffff;--dx-tint:#f2f6f6;
  --dx-grad:linear-gradient(135deg,#04333a 0%,#003b42 45%,#01262b 100%);
  --dx-goldgrad:linear-gradient(135deg,#f1e2b8 0%,#e6cd96 55%,#d9b878 100%);
  --dx-line:rgba(177,129,50,.35);--dx-line-lt:rgba(230,205,150,.35);--dx-r:20px;--dx-r-sm:14px;
  position:relative;display:block;box-sizing:border-box;overflow:hidden;font-family:'Jost',system-ui,-apple-system,'Segoe UI',sans-serif;font-weight:400;font-size:17px;line-height:1.6;color:var(--dx-body);background:var(--dx-white);padding:64px 20px;scroll-margin-top:12px;-webkit-font-smoothing:antialiased}
.dx *,.dx *::before,.dx *::after{box-sizing:border-box}
.dx:focus{outline:none}
.dx__in{position:relative;z-index:1;max-width:1040px;margin:0 auto}
:where(.dx) h1,:where(.dx) h2,:where(.dx) h3{font-family:inherit;font-weight:700;color:var(--dx-teal);margin:0;letter-spacing:-.015em}
:where(.dx) h2{font-size:clamp(1.9rem,6.2vw,3rem);line-height:1.08;margin-bottom:16px}
:where(.dx) h3{font-size:1.22rem;line-height:1.3;margin-bottom:6px}
:where(.dx) p{margin:0 0 14px}
:where(.dx) strong{color:var(--dx-teal)}
:where(.dx) h1 em,:where(.dx) h2 em{font-style:italic;font-weight:700;color:var(--dx-gold)}
.dx__eyebrow{display:flex;align-items:center;gap:12px;margin:0 0 14px;font-weight:500;font-size:.78rem;letter-spacing:.2em;text-transform:uppercase;color:var(--dx-gold-dk)}
.dx__eyebrow::before{content:"";flex:0 0 44px;height:2px;border-radius:2px;background:var(--dx-gold)}
.dx__sub{font-weight:400;font-size:1.1rem;max-width:640px}
/* Teal sections: the brand's lead surface */
.dx--teal{background:var(--dx-grad);color:var(--dx-mist)}
.dx--deep{background:var(--dx-deep);color:var(--dx-mist)}
.dx--teal h1,.dx--teal h2,.dx--teal h3,.dx--teal strong,.dx--deep h1,.dx--deep h2,.dx--deep h3,.dx--deep strong{color:var(--dx-ivory)}
.dx--teal h1 em,.dx--teal h2 em,.dx--deep h1 em,.dx--deep h2 em{color:var(--dx-champ)}
.dx--teal .dx__eyebrow,.dx--deep .dx__eyebrow{color:var(--dx-champ)}
.dx--teal .dx__eyebrow::before,.dx--deep .dx__eyebrow::before{background:var(--dx-champ)}
.dx--tint{background:var(--dx-tint)}
/* Signature: double hairline frame + concentric circles (business cards, decks) */
.dx__framed{position:relative}
.dx__framed::after{content:"";position:absolute;inset:8px;border:1px solid var(--dx-line);border-radius:calc(var(--dx-r) - 5px);pointer-events:none}
.dx--teal .dx__framed::after,.dx--deep .dx__framed::after,.dx__framed--lt::after{border-color:var(--dx-line-lt)}
.dx__rings{position:absolute;z-index:0;width:560px;height:560px;border-radius:50%;border:1px solid rgba(230,205,150,.22);pointer-events:none}
.dx__rings::before,.dx__rings::after{content:"";position:absolute;border-radius:50%;border:1px solid rgba(230,205,150,.16)}
.dx__rings::before{inset:70px}.dx__rings::after{inset:140px}
/* Buttons */
.dx__btn{display:inline-flex;align-items:center;justify-content:center;gap:10px;min-height:54px;padding:14px 28px;border-radius:999px;border:2px solid var(--dx-teal);background:var(--dx-teal);color:var(--dx-ivory)!important;font:500 1rem/1.2 'Jost',system-ui,sans-serif;letter-spacing:.03em;text-decoration:none!important;cursor:pointer;transition:transform .2s ease,box-shadow .2s ease,background .2s ease;width:100%}
.dx__btn:hover{transform:translateY(-2px);box-shadow:0 14px 30px -14px rgba(1,38,43,.7)}
.dx__btn--gold{background:var(--dx-goldgrad);border-color:transparent;color:var(--dx-teal)!important;font-weight:700}
.dx__btn--gold:hover{box-shadow:0 14px 30px -12px rgba(230,205,150,.55)}
.dx__btn--line{background:transparent;color:var(--dx-teal)!important}
.dx--teal .dx__btn--line,.dx--deep .dx__btn--line{border-color:var(--dx-champ);color:var(--dx-champ)!important}
.dx__btn svg{width:18px;height:18px;flex:none}
.dx__link{color:var(--dx-teal);font-weight:500;text-decoration:underline;text-decoration-color:var(--dx-gold);text-decoration-thickness:2px;text-underline-offset:5px}
.dx--teal .dx__link,.dx--deep .dx__link{color:var(--dx-champ);text-decoration-color:var(--dx-champ)}
.dx a:focus-visible,.dx button:focus-visible,.dx input:focus-visible{outline:3px solid var(--dx-gold);outline-offset:3px}
.dx--teal a:focus-visible,.dx--teal button:focus-visible,.dx--teal input:focus-visible,.dx--deep a:focus-visible,.dx--deep button:focus-visible{outline-color:var(--dx-champ)}
.dx__sr{position:absolute!important;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0);white-space:nowrap}
/* Gentle reveal on scroll (only when the global head script runs) */
.dx-js .dx [data-reveal]{opacity:0;transform:translateY(22px);transition:opacity .7s ease,transform .7s ease}
.dx-js .dx [data-reveal].is-in{opacity:1;transform:none}
@media (min-width:640px){.dx{padding:96px 32px}.dx__btn{width:auto}}
@media (prefers-reduced-motion:reduce){.dx *{transition:none!important;animation:none!important}.dx-js .dx [data-reveal]{opacity:1;transform:none}}
/* ---- Distinct motion kit: flipping words and flip cards ---- */
.dx-rot{display:inline}
.dx-rot__win{display:inline-grid;perspective:700px;vertical-align:bottom}
.dx-rot__w{grid-area:1/1;opacity:0;transform:rotateX(-95deg);transform-origin:50% 100%;transition:transform .75s cubic-bezier(.2,.8,.2,1),opacity .5s ease;white-space:nowrap}
.dx-rot__w.is-on{opacity:1;transform:none}
.dx-rot__w.is-out{opacity:0;transform:rotateX(95deg);transform-origin:50% 0}
.dx__pause{display:inline-flex;align-items:center;gap:8px;min-height:36px;padding:6px 14px;border-radius:999px;border:1px solid currentColor;background:transparent;color:inherit;font:500 .78rem/1 'Jost',system-ui,sans-serif;letter-spacing:.12em;text-transform:uppercase;cursor:pointer;opacity:.85}
.dx__pause:hover{opacity:1}
.dx__pause svg{width:12px;height:12px;fill:currentColor}
/* Flip cards (3D). Without JS both faces simply stack. */
.dx-flips{list-style:none;margin:0;padding:0;display:grid;gap:20px}
.dx-flip{perspective:1400px}
.dx-flip__inner{display:grid}
.dx-flip__face{grid-area:1/1;border-radius:var(--dx-r);overflow:hidden}
.dx-flips.is-live .dx-flip__inner{transition:transform .85s cubic-bezier(.2,.75,.15,1);transform-style:preserve-3d}
.dx-flips.is-live .dx-flip__face{backface-visibility:hidden;-webkit-backface-visibility:hidden}
.dx-flips.is-live .dx-flip__back{transform:rotateY(180deg)}
.dx-flips.is-live .dx-flip.is-flipped .dx-flip__inner{transform:rotateY(180deg)}
.dx-flips:not(.is-live) .dx-flip__face{grid-area:auto}
.dx-flips:not(.is-live) .dx-flip__btn{display:none}
.dx-flips.is-live .dx-flip{cursor:pointer}
.dx-flips.is-live .dx-flip.is-peek .dx-flip__inner{animation:dxPeek 1.4s cubic-bezier(.3,.7,.3,1) .3s 1}
@keyframes dxPeek{0%,100%{transform:none}35%{transform:rotateY(-24deg)}65%{transform:rotateY(8deg)}}
.dx-flip__btn{display:inline-flex;align-items:center;gap:8px;margin-top:auto;padding:10px 0 0;border:0;background:none;color:inherit;font:500 .9rem/1.2 'Jost',system-ui,sans-serif;letter-spacing:.06em;cursor:pointer}
.dx-flip__btn svg{width:18px;height:18px;stroke:currentColor;transition:transform .5s ease}
.dx-flip:hover .dx-flip__front .dx-flip__btn svg{transform:rotate(180deg)}
@media (min-width:640px){.dx-flips--3{grid-template-columns:repeat(3,1fr)}}
@media (max-width:859px) and (min-width:640px){.dx-flips--3{grid-template-columns:1fr 1fr}}
@media (prefers-reduced-motion:reduce){
  .dx-rot__win{display:none}
  .dx-rot .dx__sr{position:static!important;width:auto;height:auto;clip:auto;white-space:normal}
  .dx__pause{display:none}
}
.dx-hero{padding-top:28px;padding-bottom:72px}
.dx-hero .dx__rings{right:-260px;top:-140px}
.dx-hero .dx__rings--b{left:-320px;right:auto;top:auto;bottom:-360px;width:640px;height:640px}
.dx-hero__frame{position:absolute;inset:12px;border:1px solid rgba(230,205,150,.28);border-radius:26px;pointer-events:none;z-index:0}
.dx-hero__logo{display:flex;justify-content:center;margin:18px 0 48px}
.dx-hero__logo img{max-width:230px;height:auto;display:block}
.dx-ph--logo{display:flex;align-items:center;justify-content:center;text-align:center;width:230px;min-height:88px;padding:12px;border:2px dashed var(--dx-champ);border-radius:var(--dx-r-sm);color:var(--dx-champ);font:500 .85rem/1.35 'Jost',system-ui,sans-serif}
.dx-hero__grid{display:grid;gap:34px;align-items:end}
.dx-hero h1{font-size:clamp(2.6rem,11vw,5.2rem);line-height:.98;letter-spacing:-.03em;margin-bottom:22px}
.dx-hero__promise{display:block;margin:30px 0 22px;font-weight:700;font-style:italic;font-size:clamp(1.5rem,5.6vw,2.4rem);line-height:1.15;color:var(--dx-champ)}
.dx-hero__promise small{display:block;font-style:normal;font-weight:500;font-size:.78rem;letter-spacing:.2em;text-transform:uppercase;color:var(--dx-mist);margin-bottom:6px}
.dx-hero__pause{margin:-8px 0 24px;color:var(--dx-champ)}
.dx-hero__lead{font-size:1.15rem;color:var(--dx-ivory);max-width:560px;margin-bottom:30px}
.dx-hero__actions{display:flex;flex-wrap:wrap;gap:12px}
.dx-hero__note{position:relative;background:rgba(243,237,225,.06);border:1px solid rgba(230,205,150,.3);border-radius:var(--dx-r);padding:28px 26px 24px;backdrop-filter:blur(2px)}
.dx-hero__note p{color:var(--dx-ivory);font-size:1.04rem}
.dx-hero__quote{position:absolute;top:-22px;left:22px;width:44px;height:44px;border-radius:50%;background:var(--dx-goldgrad);display:grid;place-items:center}
.dx-hero__quote svg{width:20px;height:20px;fill:var(--dx-teal)}
.dx-hero__sig{display:flex;align-items:center;gap:14px;margin-top:18px;padding-top:16px;border-top:1px solid rgba(230,205,150,.25)}
.dx-hero__sig b{display:block;color:var(--dx-champ);font-weight:500;font-size:1.05rem}
.dx-hero__sig span{display:block;font-size:.88rem;color:var(--dx-mist)}
@media (min-width:900px){.dx-hero{padding-bottom:110px}.dx-hero__grid{grid-template-columns:1.25fr .9fr;gap:56px}}
</style>
<div class="dx-hero__frame" aria-hidden="true"></div>
<div class="dx__rings" aria-hidden="true"></div>
<div class="dx__rings dx__rings--b" aria-hidden="true"></div>
<div class="dx__in">
  <div class="dx-hero__logo">
    <!-- LOGO SLOT: replace the placeholder div below with:
         <img src="[LOGO IMAGE URL]" alt="Distinct Tax Consulting Group®" width="230" height="88">
         Use a light/gold logo that reads on dark teal. Do NOT use the version with the gold "I". -->
    <div class="dx-ph--logo" role="img" aria-label="Distinct Tax Consulting Group® logo">[LOGO]<br>Distinct Tax Consulting Group®</div>
  </div>
  <div class="dx-hero__grid">
    <div data-reveal>
      <p class="dx__eyebrow">Payment received · Your Distinct® Experience begins</p>
      <h1 id="dx-welcome-title">You're in. Here's what happens <em>next.</em></h1>
      <p class="dx-hero__promise"><small>The Distinct® Experience</small>
        <span class="dx-rot" data-rot="2600"><span class="dx__sr">Highly valued. Financially redefined. Peace of mind obtained.</span><span class="dx-rot__win" aria-hidden="true"><span class="dx-rot__w">Highly valued.</span><span class="dx-rot__w">Financially redefined.</span><span class="dx-rot__w">Peace of mind obtained.</span></span></span></p>
      <button type="button" class="dx__pause dx-hero__pause" data-pause aria-pressed="false"><svg viewBox="0 0 12 12" aria-hidden="true"><rect x="2" y="1" width="3" height="10"/><rect x="7" y="1" width="3" height="10"/></svg><span data-pause-label>Pause motion</span></button>
      <p class="dx-hero__lead">Three steps get you ready for your assessment call. Start with step one below.</p>
      <div class="dx-hero__actions">
        <a class="dx__btn dx__btn--gold" href="#steps">See your 3 steps
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" aria-hidden="true"><path d="M12 5v14M5 12l7 7 7-7"/></svg></a>
        <a class="dx__btn dx__btn--line" href="#welcome-video">Watch the welcome video</a>
      </div>
    </div>
    <div class="dx-hero__note" data-reveal>
      <div class="dx-hero__quote" aria-hidden="true"><svg viewBox="0 0 24 24"><path d="M4 18v-5.5C4 8.4 6.2 6 10 5.5v2.6C8 8.6 7.2 9.9 7.1 12H10v6zm10 0v-5.5c0-4.1 2.2-6.5 6-7v2.6c-2 .5-2.8 1.8-2.9 3.9H20v6z"/></svg></div>
      <p>Welcome, and thank you for trusting Distinct Tax Consulting Group® with your Distinct® Tax Assessment.</p>
      <p>Here's how we work: before we ever get on a call, our team reviews your documents. That way, our call is spent on what we found and what we can do about it.</p>
      <div class="dx-hero__sig"><div><b>Alysha</b><span>Founder and Managing Partner</span></div></div>
    </div>
  </div>
</div>
<script>
/* Distinct motion kit: rotating words, pause control, flip cards. Scoped to this section only. */
(function(root){
  if(!root) return;
  var reduce=window.matchMedia&&window.matchMedia('(prefers-reduced-motion: reduce)').matches, paused=false;
  [].forEach.call(root.querySelectorAll('[data-rot]'),function(r){
    var w=r.querySelectorAll('.dx-rot__w'),i=0,hover=false; if(!w.length) return;
    w[0].classList.add('is-on'); if(reduce) return;
    r.addEventListener('mouseenter',function(){hover=true}); r.addEventListener('mouseleave',function(){hover=false});
    setInterval(function(){
      if(paused||hover||document.hidden) return;
      var c=w[i]; c.classList.remove('is-on'); c.classList.add('is-out');
      setTimeout(function(){c.classList.remove('is-out')},800);
      i=(i+1)%w.length; w[i].classList.add('is-on');
    },+r.getAttribute('data-rot')||2600);
  });
  [].forEach.call(root.querySelectorAll('[data-pause]'),function(b){
    b.addEventListener('click',function(){
      paused=!paused; b.setAttribute('aria-pressed',paused);
      b.querySelector('[data-pause-label]').textContent=paused?'Play motion':'Pause motion';
    });
  });
  [].forEach.call(root.querySelectorAll('.dx-flips'),function(list){
    list.classList.add('is-live');
    var cards=list.querySelectorAll('.dx-flip');
    function set(card,on){
      card.classList.toggle('is-flipped',on);
      var f=card.querySelector('.dx-flip__front'), k=card.querySelector('.dx-flip__back');
      (on?f:k).setAttribute('inert',''); (on?k:f).removeAttribute('inert');
      [].forEach.call(card.querySelectorAll('.dx-flip__btn'),function(x){x.setAttribute('aria-expanded',on)});
    }
    [].forEach.call(cards,function(c){
      set(c,false);
      c.addEventListener('click',function(e){
        if(e.target.closest('a')) return;
        var on=!c.classList.contains('is-flipped'); set(c,on);
        if(e.detail===0){var t=c.querySelector(on?'.dx-flip__back .dx-flip__btn':'.dx-flip__front .dx-flip__btn'); if(t) t.focus();}
      });
    });
    if(!reduce&&cards[0]&&'IntersectionObserver' in window){
      var io=new IntersectionObserver(function(es){if(es[0].isIntersecting){cards[0].classList.add('is-peek');io.disconnect();}},{threshold:.6});
      io.observe(cards[0]);
    }
  });
})(document.currentScript&&document.currentScript.closest('.dx'));
</script>
</section>
```

## SECTION 1B: Transformation (`#transformation`)

**GHL build note:** Section: full width, background #01262B, padding 0. The transformation moment: plays once when it scrolls into view, with a See it again button. Paste it directly under Section 1. Add a 1-column row, then a **Custom Code** element, and paste the block below. Paste-ready file: `ghl-blocks/01b-transformation.html`.

```html
<!-- ===== SECTION 1B: TRANSFORMATION (#transformation) ===== -->
<!-- Plays once when it scrolls into view: each burden is struck through and becomes its Distinct® outcome,
     while a gold "sunrise" glow rises behind. "See it again" replays it. Reduced-motion visitors see the final state. -->
<section id="transformation" class="dx dx--deep dx-tx" tabindex="-1" aria-labelledby="dx-tx-title">
<style>
@import url('https://fonts.googleapis.com/css2?family=Jost:ital,wght@0,400;0,500;0,700;1,500;1,700&display=swap');
/* Distinct brand tokens (DTCG Canva designs, Nov 2026). Dark teal leads; gold accents; white for reading areas. */
.dx{--dx-teal:#003b42;--dx-deep:#01262b;--dx-teal-hi:#04333a;--dx-gold:#b18132;--dx-gold-dk:#96691c;--dx-champ:#e6cd96;--dx-champ-hi:#f1e2b8;--dx-ivory:#f3ede1;--dx-mist:#c9d6d2;--dx-body:#3b4f52;--dx-white:#ffffff;--dx-tint:#f2f6f6;
  --dx-grad:linear-gradient(135deg,#04333a 0%,#003b42 45%,#01262b 100%);
  --dx-goldgrad:linear-gradient(135deg,#f1e2b8 0%,#e6cd96 55%,#d9b878 100%);
  --dx-line:rgba(177,129,50,.35);--dx-line-lt:rgba(230,205,150,.35);--dx-r:20px;--dx-r-sm:14px;
  position:relative;display:block;box-sizing:border-box;overflow:hidden;font-family:'Jost',system-ui,-apple-system,'Segoe UI',sans-serif;font-weight:400;font-size:17px;line-height:1.6;color:var(--dx-body);background:var(--dx-white);padding:64px 20px;scroll-margin-top:12px;-webkit-font-smoothing:antialiased}
.dx *,.dx *::before,.dx *::after{box-sizing:border-box}
.dx:focus{outline:none}
.dx__in{position:relative;z-index:1;max-width:1040px;margin:0 auto}
:where(.dx) h1,:where(.dx) h2,:where(.dx) h3{font-family:inherit;font-weight:700;color:var(--dx-teal);margin:0;letter-spacing:-.015em}
:where(.dx) h2{font-size:clamp(1.9rem,6.2vw,3rem);line-height:1.08;margin-bottom:16px}
:where(.dx) h3{font-size:1.22rem;line-height:1.3;margin-bottom:6px}
:where(.dx) p{margin:0 0 14px}
:where(.dx) strong{color:var(--dx-teal)}
:where(.dx) h1 em,:where(.dx) h2 em{font-style:italic;font-weight:700;color:var(--dx-gold)}
.dx__eyebrow{display:flex;align-items:center;gap:12px;margin:0 0 14px;font-weight:500;font-size:.78rem;letter-spacing:.2em;text-transform:uppercase;color:var(--dx-gold-dk)}
.dx__eyebrow::before{content:"";flex:0 0 44px;height:2px;border-radius:2px;background:var(--dx-gold)}
.dx__sub{font-weight:400;font-size:1.1rem;max-width:640px}
/* Teal sections: the brand's lead surface */
.dx--teal{background:var(--dx-grad);color:var(--dx-mist)}
.dx--deep{background:var(--dx-deep);color:var(--dx-mist)}
.dx--teal h1,.dx--teal h2,.dx--teal h3,.dx--teal strong,.dx--deep h1,.dx--deep h2,.dx--deep h3,.dx--deep strong{color:var(--dx-ivory)}
.dx--teal h1 em,.dx--teal h2 em,.dx--deep h1 em,.dx--deep h2 em{color:var(--dx-champ)}
.dx--teal .dx__eyebrow,.dx--deep .dx__eyebrow{color:var(--dx-champ)}
.dx--teal .dx__eyebrow::before,.dx--deep .dx__eyebrow::before{background:var(--dx-champ)}
.dx--tint{background:var(--dx-tint)}
/* Signature: double hairline frame + concentric circles (business cards, decks) */
.dx__framed{position:relative}
.dx__framed::after{content:"";position:absolute;inset:8px;border:1px solid var(--dx-line);border-radius:calc(var(--dx-r) - 5px);pointer-events:none}
.dx--teal .dx__framed::after,.dx--deep .dx__framed::after,.dx__framed--lt::after{border-color:var(--dx-line-lt)}
.dx__rings{position:absolute;z-index:0;width:560px;height:560px;border-radius:50%;border:1px solid rgba(230,205,150,.22);pointer-events:none}
.dx__rings::before,.dx__rings::after{content:"";position:absolute;border-radius:50%;border:1px solid rgba(230,205,150,.16)}
.dx__rings::before{inset:70px}.dx__rings::after{inset:140px}
/* Buttons */
.dx__btn{display:inline-flex;align-items:center;justify-content:center;gap:10px;min-height:54px;padding:14px 28px;border-radius:999px;border:2px solid var(--dx-teal);background:var(--dx-teal);color:var(--dx-ivory)!important;font:500 1rem/1.2 'Jost',system-ui,sans-serif;letter-spacing:.03em;text-decoration:none!important;cursor:pointer;transition:transform .2s ease,box-shadow .2s ease,background .2s ease;width:100%}
.dx__btn:hover{transform:translateY(-2px);box-shadow:0 14px 30px -14px rgba(1,38,43,.7)}
.dx__btn--gold{background:var(--dx-goldgrad);border-color:transparent;color:var(--dx-teal)!important;font-weight:700}
.dx__btn--gold:hover{box-shadow:0 14px 30px -12px rgba(230,205,150,.55)}
.dx__btn--line{background:transparent;color:var(--dx-teal)!important}
.dx--teal .dx__btn--line,.dx--deep .dx__btn--line{border-color:var(--dx-champ);color:var(--dx-champ)!important}
.dx__btn svg{width:18px;height:18px;flex:none}
.dx__link{color:var(--dx-teal);font-weight:500;text-decoration:underline;text-decoration-color:var(--dx-gold);text-decoration-thickness:2px;text-underline-offset:5px}
.dx--teal .dx__link,.dx--deep .dx__link{color:var(--dx-champ);text-decoration-color:var(--dx-champ)}
.dx a:focus-visible,.dx button:focus-visible,.dx input:focus-visible{outline:3px solid var(--dx-gold);outline-offset:3px}
.dx--teal a:focus-visible,.dx--teal button:focus-visible,.dx--teal input:focus-visible,.dx--deep a:focus-visible,.dx--deep button:focus-visible{outline-color:var(--dx-champ)}
.dx__sr{position:absolute!important;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0);white-space:nowrap}
/* Gentle reveal on scroll (only when the global head script runs) */
.dx-js .dx [data-reveal]{opacity:0;transform:translateY(22px);transition:opacity .7s ease,transform .7s ease}
.dx-js .dx [data-reveal].is-in{opacity:1;transform:none}
@media (min-width:640px){.dx{padding:96px 32px}.dx__btn{width:auto}}
@media (prefers-reduced-motion:reduce){.dx *{transition:none!important;animation:none!important}.dx-js .dx [data-reveal]{opacity:1;transform:none}}
/* ---- Distinct motion kit: flipping words and flip cards ---- */
.dx-rot{display:inline}
.dx-rot__win{display:inline-grid;perspective:700px;vertical-align:bottom}
.dx-rot__w{grid-area:1/1;opacity:0;transform:rotateX(-95deg);transform-origin:50% 100%;transition:transform .75s cubic-bezier(.2,.8,.2,1),opacity .5s ease;white-space:nowrap}
.dx-rot__w.is-on{opacity:1;transform:none}
.dx-rot__w.is-out{opacity:0;transform:rotateX(95deg);transform-origin:50% 0}
.dx__pause{display:inline-flex;align-items:center;gap:8px;min-height:36px;padding:6px 14px;border-radius:999px;border:1px solid currentColor;background:transparent;color:inherit;font:500 .78rem/1 'Jost',system-ui,sans-serif;letter-spacing:.12em;text-transform:uppercase;cursor:pointer;opacity:.85}
.dx__pause:hover{opacity:1}
.dx__pause svg{width:12px;height:12px;fill:currentColor}
/* Flip cards (3D). Without JS both faces simply stack. */
.dx-flips{list-style:none;margin:0;padding:0;display:grid;gap:20px}
.dx-flip{perspective:1400px}
.dx-flip__inner{display:grid}
.dx-flip__face{grid-area:1/1;border-radius:var(--dx-r);overflow:hidden}
.dx-flips.is-live .dx-flip__inner{transition:transform .85s cubic-bezier(.2,.75,.15,1);transform-style:preserve-3d}
.dx-flips.is-live .dx-flip__face{backface-visibility:hidden;-webkit-backface-visibility:hidden}
.dx-flips.is-live .dx-flip__back{transform:rotateY(180deg)}
.dx-flips.is-live .dx-flip.is-flipped .dx-flip__inner{transform:rotateY(180deg)}
.dx-flips:not(.is-live) .dx-flip__face{grid-area:auto}
.dx-flips:not(.is-live) .dx-flip__btn{display:none}
.dx-flips.is-live .dx-flip{cursor:pointer}
.dx-flips.is-live .dx-flip.is-peek .dx-flip__inner{animation:dxPeek 1.4s cubic-bezier(.3,.7,.3,1) .3s 1}
@keyframes dxPeek{0%,100%{transform:none}35%{transform:rotateY(-24deg)}65%{transform:rotateY(8deg)}}
.dx-flip__btn{display:inline-flex;align-items:center;gap:8px;margin-top:auto;padding:10px 0 0;border:0;background:none;color:inherit;font:500 .9rem/1.2 'Jost',system-ui,sans-serif;letter-spacing:.06em;cursor:pointer}
.dx-flip__btn svg{width:18px;height:18px;stroke:currentColor;transition:transform .5s ease}
.dx-flip:hover .dx-flip__front .dx-flip__btn svg{transform:rotate(180deg)}
@media (min-width:640px){.dx-flips--3{grid-template-columns:repeat(3,1fr)}}
@media (max-width:859px) and (min-width:640px){.dx-flips--3{grid-template-columns:1fr 1fr}}
@media (prefers-reduced-motion:reduce){
  .dx-rot__win{display:none}
  .dx-rot .dx__sr{position:static!important;width:auto;height:auto;clip:auto;white-space:normal}
  .dx__pause{display:none}
}
.dx-tx{padding-top:80px;padding-bottom:88px}
.dx-tx__glow{position:absolute;left:50%;bottom:-55%;width:150%;height:110%;transform:translateX(-50%);background:radial-gradient(closest-side,rgba(230,205,150,.34),rgba(177,129,50,.14) 45%,rgba(1,38,43,0) 72%);opacity:0;transition:opacity 3.2s ease,bottom 3.6s cubic-bezier(.2,.7,.2,1);pointer-events:none;z-index:0}
.dx-tx.is-go .dx-tx__glow,.dx-tx.is-done .dx-tx__glow{opacity:1;bottom:-30%}
.dx-tx__head{max-width:760px;margin:0 auto 44px;text-align:center}
.dx-tx__head .dx__eyebrow{justify-content:center;max-width:none}
.dx-tx__head .dx__eyebrow::after{content:"";flex:0 0 44px;height:2px;border-radius:2px;background:var(--dx-champ)}
.dx-tx__head p:not(.dx__eyebrow){color:var(--dx-ivory);font-size:1.12rem;margin:0 auto;max-width:620px}
.dx-tx__list{list-style:none;margin:0;padding:0;display:grid;grid-template-columns:1fr 1fr;gap:14px}
.dx-tx__item{position:relative;display:flex;flex-direction:column;justify-content:flex-end;min-height:150px;padding:22px 18px;border-radius:var(--dx-r);background:rgba(243,237,225,.04);border:1px solid rgba(230,205,150,.2);overflow:hidden;transition:background 1s ease,border-color 1s ease}
.dx-tx__from{position:relative;align-self:flex-start;font-weight:500;font-size:.95rem;color:var(--dx-mist);transition:transform .7s cubic-bezier(.2,.7,.2,1),opacity .7s ease,filter .7s ease;transform-origin:left bottom}
.dx-tx__from::after{content:"";position:absolute;left:-2px;right:-2px;top:52%;height:2px;border-radius:2px;background:var(--dx-gold);transform:scaleX(1);transform-origin:left;transition:transform .55s ease}
.dx-tx__to{display:block;margin-top:6px;font-weight:700;font-style:italic;font-size:clamp(1.35rem,4.6vw,1.9rem);line-height:1.1;background:var(--dx-goldgrad);-webkit-background-clip:text;background-clip:text;color:transparent;transition:opacity .9s ease,transform .9s cubic-bezier(.2,.7,.2,1),filter .9s ease}
/* Armed (JS present, waiting): burden shown big, outcome hidden */
.dx-tx.is-armed .dx-tx__from{transform:translateY(34px) scale(1.7);color:var(--dx-ivory)}
.dx-tx.is-armed .dx-tx__from::after{transform:scaleX(0)}
.dx-tx.is-armed .dx-tx__to{opacity:0;transform:translateY(16px);filter:blur(8px)}
/* Go: strike, shrink, reveal — staggered per tile */
.dx-tx.is-go .dx-tx__from{transform:none;color:var(--dx-mist);opacity:.75;transition-delay:calc(var(--i)*.5s + .45s)}
.dx-tx.is-go .dx-tx__from::after{transform:scaleX(1);transition-delay:calc(var(--i)*.5s)}
.dx-tx.is-go .dx-tx__to{opacity:1;transform:none;filter:none;transition-delay:calc(var(--i)*.5s + .65s)}
.dx-tx.is-go .dx-tx__item{background:rgba(230,205,150,.07);border-color:rgba(230,205,150,.42);transition-delay:calc(var(--i)*.5s + .65s)}
.dx-tx__close{margin:44px auto 0;text-align:center;max-width:760px}
.dx-tx__close p{margin:0 0 20px;font-weight:700;font-size:clamp(1.25rem,4.4vw,1.75rem);line-height:1.35;color:var(--dx-ivory)}
.dx-tx__close em{font-style:italic;color:var(--dx-champ)}
.dx-tx__replay{display:inline-flex;align-items:center;gap:8px;min-height:40px;padding:8px 18px;border-radius:999px;border:1px solid rgba(230,205,150,.6);background:transparent;color:var(--dx-champ);font:500 .85rem/1 'Jost',system-ui,sans-serif;letter-spacing:.08em;cursor:pointer}
.dx-tx__replay svg{width:16px;height:16px;stroke:currentColor}
@media (min-width:760px){.dx-tx__list{grid-template-columns:repeat(3,1fr);gap:18px}.dx-tx__item{min-height:170px;padding:26px 24px}}
@media (prefers-reduced-motion:reduce){.dx-tx__replay{display:none}}
</style>
<div class="dx-tx__glow" aria-hidden="true"></div>
<div class="dx__in">
  <div class="dx-tx__head" data-reveal>
    <p class="dx__eyebrow">Your Distinct® Experience</p>
    <h2 id="dx-tx-title">This is where it starts to <em>change.</em></h2>
    <p>Whatever brought you here, whether it's unfiled years, letters from the IRS or books that fell behind, you don't have to carry it alone anymore.</p>
  </div>
  <ul class="dx-tx__list">
    <li class="dx-tx__item" style="--i:0"><span class="dx__sr">Worry becomes peace of mind.</span><span class="dx-tx__from" aria-hidden="true">Worry</span><span class="dx-tx__to" aria-hidden="true">Peace of mind</span></li>
    <li class="dx-tx__item" style="--i:1"><span class="dx__sr">Confusion becomes clarity.</span><span class="dx-tx__from" aria-hidden="true">Confusion</span><span class="dx-tx__to" aria-hidden="true">Clarity</span></li>
    <li class="dx-tx__item" style="--i:2"><span class="dx__sr">Guessing becomes a plan.</span><span class="dx-tx__from" aria-hidden="true">Guessing</span><span class="dx-tx__to" aria-hidden="true">A plan</span></li>
    <li class="dx-tx__item" style="--i:3"><span class="dx__sr">Feeling behind becomes moving forward.</span><span class="dx-tx__from" aria-hidden="true">Feeling behind</span><span class="dx-tx__to" aria-hidden="true">Moving forward</span></li>
    <li class="dx-tx__item" style="--i:4"><span class="dx__sr">Carrying it alone becomes a team beside you.</span><span class="dx-tx__from" aria-hidden="true">Carrying it alone</span><span class="dx-tx__to" aria-hidden="true">A team beside you</span></li>
    <li class="dx-tx__item" style="--i:5"><span class="dx__sr">Shame becomes no judgment.</span><span class="dx-tx__from" aria-hidden="true">Shame</span><span class="dx-tx__to" aria-hidden="true">No judgment</span></li>
  </ul>
  <div class="dx-tx__close" data-reveal>
    <p>Highly valued. Financially redefined. <em>Peace of mind obtained.</em></p>
    <button type="button" class="dx-tx__replay" data-tx-replay><svg viewBox="0 0 24 24" fill="none" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M3 12a9 9 0 1 0 3-6.7L3 8M3 3v5h5"/></svg>See it again</button>
  </div>
</div>
<script>
(function(root){
  if(!root) return;
  var reduce=window.matchMedia&&window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  if(reduce||!('IntersectionObserver' in window)){root.classList.add('is-done');return;}
  root.classList.add('is-armed');
  function play(){root.classList.remove('is-go');void root.offsetWidth;root.classList.add('is-go');}
  var io=new IntersectionObserver(function(es){if(es[0].isIntersecting){play();io.disconnect();}},{threshold:.35});
  io.observe(root.querySelector('.dx-tx__list'));
  var btn=root.querySelector('[data-tx-replay]');
  if(btn) btn.addEventListener('click',function(){root.classList.remove('is-go');setTimeout(play,450);});
})(document.currentScript&&document.currentScript.closest('.dx'));
</script>
</section>
```

## SECTION 2: Your 3 Steps (`#steps`)

**GHL build note:** Section: full width, background #FFFFFF, padding 0. Teal flip cards (tap to turn over). Add a 1-column row, then a **Custom Code** element, and paste the block below. Paste-ready file: `ghl-blocks/02-steps.html`.

```html
<!-- ===== SECTION 2: YOUR 3 STEPS (#steps) ===== -->
<!-- Flip cards: tap/click (or Enter/Space on the flip button) to turn a card over. -->
<section id="steps" class="dx dx-steps" tabindex="-1" aria-labelledby="dx-steps-title">
<style>
@import url('https://fonts.googleapis.com/css2?family=Jost:ital,wght@0,400;0,500;0,700;1,500;1,700&display=swap');
/* Distinct brand tokens (DTCG Canva designs, Nov 2026). Dark teal leads; gold accents; white for reading areas. */
.dx{--dx-teal:#003b42;--dx-deep:#01262b;--dx-teal-hi:#04333a;--dx-gold:#b18132;--dx-gold-dk:#96691c;--dx-champ:#e6cd96;--dx-champ-hi:#f1e2b8;--dx-ivory:#f3ede1;--dx-mist:#c9d6d2;--dx-body:#3b4f52;--dx-white:#ffffff;--dx-tint:#f2f6f6;
  --dx-grad:linear-gradient(135deg,#04333a 0%,#003b42 45%,#01262b 100%);
  --dx-goldgrad:linear-gradient(135deg,#f1e2b8 0%,#e6cd96 55%,#d9b878 100%);
  --dx-line:rgba(177,129,50,.35);--dx-line-lt:rgba(230,205,150,.35);--dx-r:20px;--dx-r-sm:14px;
  position:relative;display:block;box-sizing:border-box;overflow:hidden;font-family:'Jost',system-ui,-apple-system,'Segoe UI',sans-serif;font-weight:400;font-size:17px;line-height:1.6;color:var(--dx-body);background:var(--dx-white);padding:64px 20px;scroll-margin-top:12px;-webkit-font-smoothing:antialiased}
.dx *,.dx *::before,.dx *::after{box-sizing:border-box}
.dx:focus{outline:none}
.dx__in{position:relative;z-index:1;max-width:1040px;margin:0 auto}
:where(.dx) h1,:where(.dx) h2,:where(.dx) h3{font-family:inherit;font-weight:700;color:var(--dx-teal);margin:0;letter-spacing:-.015em}
:where(.dx) h2{font-size:clamp(1.9rem,6.2vw,3rem);line-height:1.08;margin-bottom:16px}
:where(.dx) h3{font-size:1.22rem;line-height:1.3;margin-bottom:6px}
:where(.dx) p{margin:0 0 14px}
:where(.dx) strong{color:var(--dx-teal)}
:where(.dx) h1 em,:where(.dx) h2 em{font-style:italic;font-weight:700;color:var(--dx-gold)}
.dx__eyebrow{display:flex;align-items:center;gap:12px;margin:0 0 14px;font-weight:500;font-size:.78rem;letter-spacing:.2em;text-transform:uppercase;color:var(--dx-gold-dk)}
.dx__eyebrow::before{content:"";flex:0 0 44px;height:2px;border-radius:2px;background:var(--dx-gold)}
.dx__sub{font-weight:400;font-size:1.1rem;max-width:640px}
/* Teal sections: the brand's lead surface */
.dx--teal{background:var(--dx-grad);color:var(--dx-mist)}
.dx--deep{background:var(--dx-deep);color:var(--dx-mist)}
.dx--teal h1,.dx--teal h2,.dx--teal h3,.dx--teal strong,.dx--deep h1,.dx--deep h2,.dx--deep h3,.dx--deep strong{color:var(--dx-ivory)}
.dx--teal h1 em,.dx--teal h2 em,.dx--deep h1 em,.dx--deep h2 em{color:var(--dx-champ)}
.dx--teal .dx__eyebrow,.dx--deep .dx__eyebrow{color:var(--dx-champ)}
.dx--teal .dx__eyebrow::before,.dx--deep .dx__eyebrow::before{background:var(--dx-champ)}
.dx--tint{background:var(--dx-tint)}
/* Signature: double hairline frame + concentric circles (business cards, decks) */
.dx__framed{position:relative}
.dx__framed::after{content:"";position:absolute;inset:8px;border:1px solid var(--dx-line);border-radius:calc(var(--dx-r) - 5px);pointer-events:none}
.dx--teal .dx__framed::after,.dx--deep .dx__framed::after,.dx__framed--lt::after{border-color:var(--dx-line-lt)}
.dx__rings{position:absolute;z-index:0;width:560px;height:560px;border-radius:50%;border:1px solid rgba(230,205,150,.22);pointer-events:none}
.dx__rings::before,.dx__rings::after{content:"";position:absolute;border-radius:50%;border:1px solid rgba(230,205,150,.16)}
.dx__rings::before{inset:70px}.dx__rings::after{inset:140px}
/* Buttons */
.dx__btn{display:inline-flex;align-items:center;justify-content:center;gap:10px;min-height:54px;padding:14px 28px;border-radius:999px;border:2px solid var(--dx-teal);background:var(--dx-teal);color:var(--dx-ivory)!important;font:500 1rem/1.2 'Jost',system-ui,sans-serif;letter-spacing:.03em;text-decoration:none!important;cursor:pointer;transition:transform .2s ease,box-shadow .2s ease,background .2s ease;width:100%}
.dx__btn:hover{transform:translateY(-2px);box-shadow:0 14px 30px -14px rgba(1,38,43,.7)}
.dx__btn--gold{background:var(--dx-goldgrad);border-color:transparent;color:var(--dx-teal)!important;font-weight:700}
.dx__btn--gold:hover{box-shadow:0 14px 30px -12px rgba(230,205,150,.55)}
.dx__btn--line{background:transparent;color:var(--dx-teal)!important}
.dx--teal .dx__btn--line,.dx--deep .dx__btn--line{border-color:var(--dx-champ);color:var(--dx-champ)!important}
.dx__btn svg{width:18px;height:18px;flex:none}
.dx__link{color:var(--dx-teal);font-weight:500;text-decoration:underline;text-decoration-color:var(--dx-gold);text-decoration-thickness:2px;text-underline-offset:5px}
.dx--teal .dx__link,.dx--deep .dx__link{color:var(--dx-champ);text-decoration-color:var(--dx-champ)}
.dx a:focus-visible,.dx button:focus-visible,.dx input:focus-visible{outline:3px solid var(--dx-gold);outline-offset:3px}
.dx--teal a:focus-visible,.dx--teal button:focus-visible,.dx--teal input:focus-visible,.dx--deep a:focus-visible,.dx--deep button:focus-visible{outline-color:var(--dx-champ)}
.dx__sr{position:absolute!important;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0);white-space:nowrap}
/* Gentle reveal on scroll (only when the global head script runs) */
.dx-js .dx [data-reveal]{opacity:0;transform:translateY(22px);transition:opacity .7s ease,transform .7s ease}
.dx-js .dx [data-reveal].is-in{opacity:1;transform:none}
@media (min-width:640px){.dx{padding:96px 32px}.dx__btn{width:auto}}
@media (prefers-reduced-motion:reduce){.dx *{transition:none!important;animation:none!important}.dx-js .dx [data-reveal]{opacity:1;transform:none}}
/* ---- Distinct motion kit: flipping words and flip cards ---- */
.dx-rot{display:inline}
.dx-rot__win{display:inline-grid;perspective:700px;vertical-align:bottom}
.dx-rot__w{grid-area:1/1;opacity:0;transform:rotateX(-95deg);transform-origin:50% 100%;transition:transform .75s cubic-bezier(.2,.8,.2,1),opacity .5s ease;white-space:nowrap}
.dx-rot__w.is-on{opacity:1;transform:none}
.dx-rot__w.is-out{opacity:0;transform:rotateX(95deg);transform-origin:50% 0}
.dx__pause{display:inline-flex;align-items:center;gap:8px;min-height:36px;padding:6px 14px;border-radius:999px;border:1px solid currentColor;background:transparent;color:inherit;font:500 .78rem/1 'Jost',system-ui,sans-serif;letter-spacing:.12em;text-transform:uppercase;cursor:pointer;opacity:.85}
.dx__pause:hover{opacity:1}
.dx__pause svg{width:12px;height:12px;fill:currentColor}
/* Flip cards (3D). Without JS both faces simply stack. */
.dx-flips{list-style:none;margin:0;padding:0;display:grid;gap:20px}
.dx-flip{perspective:1400px}
.dx-flip__inner{display:grid}
.dx-flip__face{grid-area:1/1;border-radius:var(--dx-r);overflow:hidden}
.dx-flips.is-live .dx-flip__inner{transition:transform .85s cubic-bezier(.2,.75,.15,1);transform-style:preserve-3d}
.dx-flips.is-live .dx-flip__face{backface-visibility:hidden;-webkit-backface-visibility:hidden}
.dx-flips.is-live .dx-flip__back{transform:rotateY(180deg)}
.dx-flips.is-live .dx-flip.is-flipped .dx-flip__inner{transform:rotateY(180deg)}
.dx-flips:not(.is-live) .dx-flip__face{grid-area:auto}
.dx-flips:not(.is-live) .dx-flip__btn{display:none}
.dx-flips.is-live .dx-flip{cursor:pointer}
.dx-flips.is-live .dx-flip.is-peek .dx-flip__inner{animation:dxPeek 1.4s cubic-bezier(.3,.7,.3,1) .3s 1}
@keyframes dxPeek{0%,100%{transform:none}35%{transform:rotateY(-24deg)}65%{transform:rotateY(8deg)}}
.dx-flip__btn{display:inline-flex;align-items:center;gap:8px;margin-top:auto;padding:10px 0 0;border:0;background:none;color:inherit;font:500 .9rem/1.2 'Jost',system-ui,sans-serif;letter-spacing:.06em;cursor:pointer}
.dx-flip__btn svg{width:18px;height:18px;stroke:currentColor;transition:transform .5s ease}
.dx-flip:hover .dx-flip__front .dx-flip__btn svg{transform:rotate(180deg)}
@media (min-width:640px){.dx-flips--3{grid-template-columns:repeat(3,1fr)}}
@media (max-width:859px) and (min-width:640px){.dx-flips--3{grid-template-columns:1fr 1fr}}
@media (prefers-reduced-motion:reduce){
  .dx-rot__win{display:none}
  .dx-rot .dx__sr{position:static!important;width:auto;height:auto;clip:auto;white-space:normal}
  .dx__pause{display:none}
}
.dx-steps__head{margin-bottom:34px}
.dx-steps .dx-flip__face{position:relative;display:flex;flex-direction:column;min-height:330px;padding:30px 26px 24px}
.dx-steps .dx-flip__face::after{content:"";position:absolute;inset:8px;border:1px solid rgba(230,205,150,.28);border-radius:15px;pointer-events:none}
.dx-steps .dx-flip__front{background:var(--dx-grad);color:var(--dx-mist);box-shadow:0 30px 60px -34px rgba(1,38,43,.85)}
.dx-steps .dx-flip__back{background:var(--dx-deep);color:var(--dx-mist);box-shadow:0 0 0 2px var(--dx-champ),0 30px 60px -34px rgba(1,38,43,.85)}
.dx-step__num{font-weight:700;font-size:5.4rem;line-height:.82;letter-spacing:-.05em;background:var(--dx-goldgrad);-webkit-background-clip:text;background-clip:text;color:transparent;margin-bottom:auto}
.dx-steps h3{color:var(--dx-ivory)!important;font-size:1.4rem;line-height:1.25;margin:26px 0 4px}
.dx-steps .dx-flip__btn{color:var(--dx-champ);position:relative;z-index:1}
.dx-steps .dx-flip__front .dx-flip__btn{margin-top:18px}
.dx-step__label{font-weight:500;font-size:.75rem;letter-spacing:.22em;text-transform:uppercase;color:var(--dx-champ);margin-bottom:14px}
.dx-steps .dx-flip__back p{color:var(--dx-ivory);font-size:1.08rem;margin-bottom:22px}
.dx-steps .dx-flip__back .dx__btn{position:relative;z-index:1;margin-bottom:6px}
.dx-steps .dx-flip:hover .dx-flip__front{box-shadow:0 0 0 1px var(--dx-champ),0 36px 70px -34px rgba(1,38,43,.9)}
</style>
<div class="dx__in">
  <div class="dx-steps__head" data-reveal>
    <p class="dx__eyebrow">Your Distinct® next steps</p>
    <h2 id="dx-steps-title">Three steps to get <em>ready.</em></h2>
    <p class="dx__sub" style="margin:0">Tap a card to flip it. Each one takes you to the right spot on this page.</p>
  </div>
  <ol class="dx-flips dx-flips--3">
    <li class="dx-flip" data-reveal>
      <div class="dx-flip__inner">
        <div class="dx-flip__face dx-flip__front">
          <span class="dx-step__num" aria-hidden="true">01</span>
          <h3><span class="dx__sr">Step 1: </span>Watch the welcome video</h3>
          <button type="button" class="dx-flip__btn" aria-expanded="false">Flip for details <svg viewBox="0 0 24 24" fill="none" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M3 12a9 9 0 0 1 15.5-6.2L21 8M21 3v5h-5"/></svg></button>
        </div>
        <div class="dx-flip__face dx-flip__back">
          <span class="dx-step__label">Step 1</span>
          <p>A short welcome from our team before you get started.</p>
          <a class="dx__btn dx__btn--gold" href="#welcome-video">Go to step 1</a>
          <button type="button" class="dx-flip__btn" aria-expanded="false">Flip back <svg viewBox="0 0 24 24" fill="none" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M21 12a9 9 0 0 1-15.5 6.2L3 16M3 21v-5h5"/></svg></button>
        </div>
      </div>
    </li>
    <li class="dx-flip" data-reveal>
      <div class="dx-flip__inner">
        <div class="dx-flip__face dx-flip__front">
          <span class="dx-step__num" aria-hidden="true">02</span>
          <h3><span class="dx__sr">Step 2: </span>Set up your secure TaxDome portal</h3>
          <button type="button" class="dx-flip__btn" aria-expanded="false">Flip for details <svg viewBox="0 0 24 24" fill="none" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M3 12a9 9 0 0 1 15.5-6.2L21 8M21 3v5h-5"/></svg></button>
        </div>
        <div class="dx-flip__face dx-flip__back">
          <span class="dx-step__label">Step 2</span>
          <p>Your portal is where you'll complete your organizer and upload your documents.</p>
          <a class="dx__btn dx__btn--gold" href="#taxdome-video">Go to step 2</a>
          <button type="button" class="dx-flip__btn" aria-expanded="false">Flip back <svg viewBox="0 0 24 24" fill="none" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M21 12a9 9 0 0 1-15.5 6.2L3 16M3 21v-5h5"/></svg></button>
        </div>
      </div>
    </li>
    <li class="dx-flip" data-reveal>
      <div class="dx-flip__inner">
        <div class="dx-flip__face dx-flip__front">
          <span class="dx-step__num" aria-hidden="true">03</span>
          <h3><span class="dx__sr">Step 3: </span>Complete your organizer and upload your documents</h3>
          <button type="button" class="dx-flip__btn" aria-expanded="false">Flip for details <svg viewBox="0 0 24 24" fill="none" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M3 12a9 9 0 0 1 15.5-6.2L21 8M21 3v5h-5"/></svg></button>
        </div>
        <div class="dx-flip__face dx-flip__back">
          <span class="dx-step__label">Step 3</span>
          <p>See exactly what to gather, what it looks like and where to find it.</p>
          <a class="dx__btn dx__btn--gold" href="#checklist">Go to step 3</a>
          <button type="button" class="dx-flip__btn" aria-expanded="false">Flip back <svg viewBox="0 0 24 24" fill="none" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M21 12a9 9 0 0 1-15.5 6.2L3 16M3 21v-5h5"/></svg></button>
        </div>
      </div>
    </li>
  </ol>
</div>
<script>
/* Distinct motion kit: rotating words, pause control, flip cards. Scoped to this section only. */
(function(root){
  if(!root) return;
  var reduce=window.matchMedia&&window.matchMedia('(prefers-reduced-motion: reduce)').matches, paused=false;
  [].forEach.call(root.querySelectorAll('[data-rot]'),function(r){
    var w=r.querySelectorAll('.dx-rot__w'),i=0,hover=false; if(!w.length) return;
    w[0].classList.add('is-on'); if(reduce) return;
    r.addEventListener('mouseenter',function(){hover=true}); r.addEventListener('mouseleave',function(){hover=false});
    setInterval(function(){
      if(paused||hover||document.hidden) return;
      var c=w[i]; c.classList.remove('is-on'); c.classList.add('is-out');
      setTimeout(function(){c.classList.remove('is-out')},800);
      i=(i+1)%w.length; w[i].classList.add('is-on');
    },+r.getAttribute('data-rot')||2600);
  });
  [].forEach.call(root.querySelectorAll('[data-pause]'),function(b){
    b.addEventListener('click',function(){
      paused=!paused; b.setAttribute('aria-pressed',paused);
      b.querySelector('[data-pause-label]').textContent=paused?'Play motion':'Pause motion';
    });
  });
  [].forEach.call(root.querySelectorAll('.dx-flips'),function(list){
    list.classList.add('is-live');
    var cards=list.querySelectorAll('.dx-flip');
    function set(card,on){
      card.classList.toggle('is-flipped',on);
      var f=card.querySelector('.dx-flip__front'), k=card.querySelector('.dx-flip__back');
      (on?f:k).setAttribute('inert',''); (on?k:f).removeAttribute('inert');
      [].forEach.call(card.querySelectorAll('.dx-flip__btn'),function(x){x.setAttribute('aria-expanded',on)});
    }
    [].forEach.call(cards,function(c){
      set(c,false);
      c.addEventListener('click',function(e){
        if(e.target.closest('a')) return;
        var on=!c.classList.contains('is-flipped'); set(c,on);
        if(e.detail===0){var t=c.querySelector(on?'.dx-flip__back .dx-flip__btn':'.dx-flip__front .dx-flip__btn'); if(t) t.focus();}
      });
    });
    if(!reduce&&cards[0]&&'IntersectionObserver' in window){
      var io=new IntersectionObserver(function(es){if(es[0].isIntersecting){cards[0].classList.add('is-peek');io.disconnect();}},{threshold:.6});
      io.observe(cards[0]);
    }
  });
})(document.currentScript&&document.currentScript.closest('.dx'));
</script>
</section>
```

## SECTION 3: Welcome Video (`#welcome-video`)

**GHL build note:** Section: full width, background #003B42, padding 0. When the video is ready, swap the placeholder for the embed (see the comment in the code). Add a 1-column row, then a **Custom Code** element, and paste the block below. Paste-ready file: `ghl-blocks/03-welcome-video.html`.

```html
<!-- ===== SECTION 3: WELCOME VIDEO (#welcome-video) ===== -->
<section id="welcome-video" class="dx dx--teal dx-vid" tabindex="-1" aria-labelledby="dx-wv-title">
<style>
@import url('https://fonts.googleapis.com/css2?family=Jost:ital,wght@0,400;0,500;0,700;1,500;1,700&display=swap');
/* Distinct brand tokens (DTCG Canva designs, Nov 2026). Dark teal leads; gold accents; white for reading areas. */
.dx{--dx-teal:#003b42;--dx-deep:#01262b;--dx-teal-hi:#04333a;--dx-gold:#b18132;--dx-gold-dk:#96691c;--dx-champ:#e6cd96;--dx-champ-hi:#f1e2b8;--dx-ivory:#f3ede1;--dx-mist:#c9d6d2;--dx-body:#3b4f52;--dx-white:#ffffff;--dx-tint:#f2f6f6;
  --dx-grad:linear-gradient(135deg,#04333a 0%,#003b42 45%,#01262b 100%);
  --dx-goldgrad:linear-gradient(135deg,#f1e2b8 0%,#e6cd96 55%,#d9b878 100%);
  --dx-line:rgba(177,129,50,.35);--dx-line-lt:rgba(230,205,150,.35);--dx-r:20px;--dx-r-sm:14px;
  position:relative;display:block;box-sizing:border-box;overflow:hidden;font-family:'Jost',system-ui,-apple-system,'Segoe UI',sans-serif;font-weight:400;font-size:17px;line-height:1.6;color:var(--dx-body);background:var(--dx-white);padding:64px 20px;scroll-margin-top:12px;-webkit-font-smoothing:antialiased}
.dx *,.dx *::before,.dx *::after{box-sizing:border-box}
.dx:focus{outline:none}
.dx__in{position:relative;z-index:1;max-width:1040px;margin:0 auto}
:where(.dx) h1,:where(.dx) h2,:where(.dx) h3{font-family:inherit;font-weight:700;color:var(--dx-teal);margin:0;letter-spacing:-.015em}
:where(.dx) h2{font-size:clamp(1.9rem,6.2vw,3rem);line-height:1.08;margin-bottom:16px}
:where(.dx) h3{font-size:1.22rem;line-height:1.3;margin-bottom:6px}
:where(.dx) p{margin:0 0 14px}
:where(.dx) strong{color:var(--dx-teal)}
:where(.dx) h1 em,:where(.dx) h2 em{font-style:italic;font-weight:700;color:var(--dx-gold)}
.dx__eyebrow{display:flex;align-items:center;gap:12px;margin:0 0 14px;font-weight:500;font-size:.78rem;letter-spacing:.2em;text-transform:uppercase;color:var(--dx-gold-dk)}
.dx__eyebrow::before{content:"";flex:0 0 44px;height:2px;border-radius:2px;background:var(--dx-gold)}
.dx__sub{font-weight:400;font-size:1.1rem;max-width:640px}
/* Teal sections: the brand's lead surface */
.dx--teal{background:var(--dx-grad);color:var(--dx-mist)}
.dx--deep{background:var(--dx-deep);color:var(--dx-mist)}
.dx--teal h1,.dx--teal h2,.dx--teal h3,.dx--teal strong,.dx--deep h1,.dx--deep h2,.dx--deep h3,.dx--deep strong{color:var(--dx-ivory)}
.dx--teal h1 em,.dx--teal h2 em,.dx--deep h1 em,.dx--deep h2 em{color:var(--dx-champ)}
.dx--teal .dx__eyebrow,.dx--deep .dx__eyebrow{color:var(--dx-champ)}
.dx--teal .dx__eyebrow::before,.dx--deep .dx__eyebrow::before{background:var(--dx-champ)}
.dx--tint{background:var(--dx-tint)}
/* Signature: double hairline frame + concentric circles (business cards, decks) */
.dx__framed{position:relative}
.dx__framed::after{content:"";position:absolute;inset:8px;border:1px solid var(--dx-line);border-radius:calc(var(--dx-r) - 5px);pointer-events:none}
.dx--teal .dx__framed::after,.dx--deep .dx__framed::after,.dx__framed--lt::after{border-color:var(--dx-line-lt)}
.dx__rings{position:absolute;z-index:0;width:560px;height:560px;border-radius:50%;border:1px solid rgba(230,205,150,.22);pointer-events:none}
.dx__rings::before,.dx__rings::after{content:"";position:absolute;border-radius:50%;border:1px solid rgba(230,205,150,.16)}
.dx__rings::before{inset:70px}.dx__rings::after{inset:140px}
/* Buttons */
.dx__btn{display:inline-flex;align-items:center;justify-content:center;gap:10px;min-height:54px;padding:14px 28px;border-radius:999px;border:2px solid var(--dx-teal);background:var(--dx-teal);color:var(--dx-ivory)!important;font:500 1rem/1.2 'Jost',system-ui,sans-serif;letter-spacing:.03em;text-decoration:none!important;cursor:pointer;transition:transform .2s ease,box-shadow .2s ease,background .2s ease;width:100%}
.dx__btn:hover{transform:translateY(-2px);box-shadow:0 14px 30px -14px rgba(1,38,43,.7)}
.dx__btn--gold{background:var(--dx-goldgrad);border-color:transparent;color:var(--dx-teal)!important;font-weight:700}
.dx__btn--gold:hover{box-shadow:0 14px 30px -12px rgba(230,205,150,.55)}
.dx__btn--line{background:transparent;color:var(--dx-teal)!important}
.dx--teal .dx__btn--line,.dx--deep .dx__btn--line{border-color:var(--dx-champ);color:var(--dx-champ)!important}
.dx__btn svg{width:18px;height:18px;flex:none}
.dx__link{color:var(--dx-teal);font-weight:500;text-decoration:underline;text-decoration-color:var(--dx-gold);text-decoration-thickness:2px;text-underline-offset:5px}
.dx--teal .dx__link,.dx--deep .dx__link{color:var(--dx-champ);text-decoration-color:var(--dx-champ)}
.dx a:focus-visible,.dx button:focus-visible,.dx input:focus-visible{outline:3px solid var(--dx-gold);outline-offset:3px}
.dx--teal a:focus-visible,.dx--teal button:focus-visible,.dx--teal input:focus-visible,.dx--deep a:focus-visible,.dx--deep button:focus-visible{outline-color:var(--dx-champ)}
.dx__sr{position:absolute!important;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0);white-space:nowrap}
/* Gentle reveal on scroll (only when the global head script runs) */
.dx-js .dx [data-reveal]{opacity:0;transform:translateY(22px);transition:opacity .7s ease,transform .7s ease}
.dx-js .dx [data-reveal].is-in{opacity:1;transform:none}
@media (min-width:640px){.dx{padding:96px 32px}.dx__btn{width:auto}}
@media (prefers-reduced-motion:reduce){.dx *{transition:none!important;animation:none!important}.dx-js .dx [data-reveal]{opacity:1;transform:none}}
/* ---- Distinct motion kit: flipping words and flip cards ---- */
.dx-rot{display:inline}
.dx-rot__win{display:inline-grid;perspective:700px;vertical-align:bottom}
.dx-rot__w{grid-area:1/1;opacity:0;transform:rotateX(-95deg);transform-origin:50% 100%;transition:transform .75s cubic-bezier(.2,.8,.2,1),opacity .5s ease;white-space:nowrap}
.dx-rot__w.is-on{opacity:1;transform:none}
.dx-rot__w.is-out{opacity:0;transform:rotateX(95deg);transform-origin:50% 0}
.dx__pause{display:inline-flex;align-items:center;gap:8px;min-height:36px;padding:6px 14px;border-radius:999px;border:1px solid currentColor;background:transparent;color:inherit;font:500 .78rem/1 'Jost',system-ui,sans-serif;letter-spacing:.12em;text-transform:uppercase;cursor:pointer;opacity:.85}
.dx__pause:hover{opacity:1}
.dx__pause svg{width:12px;height:12px;fill:currentColor}
/* Flip cards (3D). Without JS both faces simply stack. */
.dx-flips{list-style:none;margin:0;padding:0;display:grid;gap:20px}
.dx-flip{perspective:1400px}
.dx-flip__inner{display:grid}
.dx-flip__face{grid-area:1/1;border-radius:var(--dx-r);overflow:hidden}
.dx-flips.is-live .dx-flip__inner{transition:transform .85s cubic-bezier(.2,.75,.15,1);transform-style:preserve-3d}
.dx-flips.is-live .dx-flip__face{backface-visibility:hidden;-webkit-backface-visibility:hidden}
.dx-flips.is-live .dx-flip__back{transform:rotateY(180deg)}
.dx-flips.is-live .dx-flip.is-flipped .dx-flip__inner{transform:rotateY(180deg)}
.dx-flips:not(.is-live) .dx-flip__face{grid-area:auto}
.dx-flips:not(.is-live) .dx-flip__btn{display:none}
.dx-flips.is-live .dx-flip{cursor:pointer}
.dx-flips.is-live .dx-flip.is-peek .dx-flip__inner{animation:dxPeek 1.4s cubic-bezier(.3,.7,.3,1) .3s 1}
@keyframes dxPeek{0%,100%{transform:none}35%{transform:rotateY(-24deg)}65%{transform:rotateY(8deg)}}
.dx-flip__btn{display:inline-flex;align-items:center;gap:8px;margin-top:auto;padding:10px 0 0;border:0;background:none;color:inherit;font:500 .9rem/1.2 'Jost',system-ui,sans-serif;letter-spacing:.06em;cursor:pointer}
.dx-flip__btn svg{width:18px;height:18px;stroke:currentColor;transition:transform .5s ease}
.dx-flip:hover .dx-flip__front .dx-flip__btn svg{transform:rotate(180deg)}
@media (min-width:640px){.dx-flips--3{grid-template-columns:repeat(3,1fr)}}
@media (max-width:859px) and (min-width:640px){.dx-flips--3{grid-template-columns:1fr 1fr}}
@media (prefers-reduced-motion:reduce){
  .dx-rot__win{display:none}
  .dx-rot .dx__sr{position:static!important;width:auto;height:auto;clip:auto;white-space:normal}
  .dx__pause{display:none}
}
.dx-vid .dx__rings{left:-300px;top:40%}
.dx-vid__grid{display:grid;gap:30px;align-items:center}
.dx-video{position:relative;width:100%;aspect-ratio:16/9;border-radius:var(--dx-r);overflow:hidden;background:var(--dx-deep);box-shadow:0 0 0 1px rgba(230,205,150,.45),0 0 0 8px rgba(230,205,150,.08),0 40px 70px -30px rgba(0,0,0,.7)}
.dx-video iframe,.dx-video video{position:absolute;inset:0;width:100%;height:100%;border:0}
.dx-video__ph{position:absolute;inset:14px;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:12px;text-align:center;border:1.5px dashed rgba(230,205,150,.55);border-radius:var(--dx-r-sm);padding:16px;color:var(--dx-ivory)}
.dx-video__play{position:relative;width:76px;height:76px;border-radius:50%;background:var(--dx-goldgrad);display:grid;place-items:center}
.dx-video__play::before{content:"";position:absolute;inset:-10px;border-radius:50%;border:1px solid rgba(230,205,150,.5);animation:dxPulse 2.4s ease-out infinite}
.dx-video__play svg{width:26px;height:26px;margin-left:4px;fill:var(--dx-teal)}
.dx-video__ph strong{font-size:1.2rem}
.dx-video__ph span{font-size:.85rem;color:var(--dx-mist)}
@keyframes dxPulse{0%{transform:scale(.85);opacity:1}100%{transform:scale(1.35);opacity:0}}
.dx-vid__nav{display:flex;flex-wrap:wrap;gap:12px;margin-top:8px}
@supports not (aspect-ratio:16/9){.dx-video{height:0;padding-top:56.25%}}
@media (min-width:900px){.dx-vid__grid{grid-template-columns:.8fr 1.4fr;gap:56px}}
</style>
<div class="dx__rings" aria-hidden="true"></div>
<div class="dx__in dx-vid__grid">
  <div data-reveal>
    <p class="dx__eyebrow">Step 1 · Your Distinct® welcome</p>
    <h2 id="dx-wv-title">Watch the welcome <em>video.</em></h2>
    <p class="dx__sub">Start here, before you set anything up.</p>
    <div class="dx-vid__nav">
      <a class="dx__btn dx__btn--gold" href="#taxdome-video">Next: set up TaxDome</a>
      <a class="dx__btn dx__btn--line" href="#steps">Back to my steps</a>
    </div>
  </div>
  <div class="dx-video" data-reveal>
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
</div>
</section>
```

## SECTION 4: TaxDome Set-Up Video (`#taxdome-video`)

**GHL build note:** Section: full width, background #FFFFFF, padding 0. Leave href="[TAXDOME PORTAL LINK]" until you have the TaxDome login URL. Add a 1-column row, then a **Custom Code** element, and paste the block below. Paste-ready file: `ghl-blocks/04-taxdome-video.html`.

```html
<!-- ===== SECTION 4: TAXDOME SET-UP VIDEO (#taxdome-video) ===== -->
<section id="taxdome-video" class="dx dx-tv" tabindex="-1" aria-labelledby="dx-tv-title">
<style>
@import url('https://fonts.googleapis.com/css2?family=Jost:ital,wght@0,400;0,500;0,700;1,500;1,700&display=swap');
/* Distinct brand tokens (DTCG Canva designs, Nov 2026). Dark teal leads; gold accents; white for reading areas. */
.dx{--dx-teal:#003b42;--dx-deep:#01262b;--dx-teal-hi:#04333a;--dx-gold:#b18132;--dx-gold-dk:#96691c;--dx-champ:#e6cd96;--dx-champ-hi:#f1e2b8;--dx-ivory:#f3ede1;--dx-mist:#c9d6d2;--dx-body:#3b4f52;--dx-white:#ffffff;--dx-tint:#f2f6f6;
  --dx-grad:linear-gradient(135deg,#04333a 0%,#003b42 45%,#01262b 100%);
  --dx-goldgrad:linear-gradient(135deg,#f1e2b8 0%,#e6cd96 55%,#d9b878 100%);
  --dx-line:rgba(177,129,50,.35);--dx-line-lt:rgba(230,205,150,.35);--dx-r:20px;--dx-r-sm:14px;
  position:relative;display:block;box-sizing:border-box;overflow:hidden;font-family:'Jost',system-ui,-apple-system,'Segoe UI',sans-serif;font-weight:400;font-size:17px;line-height:1.6;color:var(--dx-body);background:var(--dx-white);padding:64px 20px;scroll-margin-top:12px;-webkit-font-smoothing:antialiased}
.dx *,.dx *::before,.dx *::after{box-sizing:border-box}
.dx:focus{outline:none}
.dx__in{position:relative;z-index:1;max-width:1040px;margin:0 auto}
:where(.dx) h1,:where(.dx) h2,:where(.dx) h3{font-family:inherit;font-weight:700;color:var(--dx-teal);margin:0;letter-spacing:-.015em}
:where(.dx) h2{font-size:clamp(1.9rem,6.2vw,3rem);line-height:1.08;margin-bottom:16px}
:where(.dx) h3{font-size:1.22rem;line-height:1.3;margin-bottom:6px}
:where(.dx) p{margin:0 0 14px}
:where(.dx) strong{color:var(--dx-teal)}
:where(.dx) h1 em,:where(.dx) h2 em{font-style:italic;font-weight:700;color:var(--dx-gold)}
.dx__eyebrow{display:flex;align-items:center;gap:12px;margin:0 0 14px;font-weight:500;font-size:.78rem;letter-spacing:.2em;text-transform:uppercase;color:var(--dx-gold-dk)}
.dx__eyebrow::before{content:"";flex:0 0 44px;height:2px;border-radius:2px;background:var(--dx-gold)}
.dx__sub{font-weight:400;font-size:1.1rem;max-width:640px}
/* Teal sections: the brand's lead surface */
.dx--teal{background:var(--dx-grad);color:var(--dx-mist)}
.dx--deep{background:var(--dx-deep);color:var(--dx-mist)}
.dx--teal h1,.dx--teal h2,.dx--teal h3,.dx--teal strong,.dx--deep h1,.dx--deep h2,.dx--deep h3,.dx--deep strong{color:var(--dx-ivory)}
.dx--teal h1 em,.dx--teal h2 em,.dx--deep h1 em,.dx--deep h2 em{color:var(--dx-champ)}
.dx--teal .dx__eyebrow,.dx--deep .dx__eyebrow{color:var(--dx-champ)}
.dx--teal .dx__eyebrow::before,.dx--deep .dx__eyebrow::before{background:var(--dx-champ)}
.dx--tint{background:var(--dx-tint)}
/* Signature: double hairline frame + concentric circles (business cards, decks) */
.dx__framed{position:relative}
.dx__framed::after{content:"";position:absolute;inset:8px;border:1px solid var(--dx-line);border-radius:calc(var(--dx-r) - 5px);pointer-events:none}
.dx--teal .dx__framed::after,.dx--deep .dx__framed::after,.dx__framed--lt::after{border-color:var(--dx-line-lt)}
.dx__rings{position:absolute;z-index:0;width:560px;height:560px;border-radius:50%;border:1px solid rgba(230,205,150,.22);pointer-events:none}
.dx__rings::before,.dx__rings::after{content:"";position:absolute;border-radius:50%;border:1px solid rgba(230,205,150,.16)}
.dx__rings::before{inset:70px}.dx__rings::after{inset:140px}
/* Buttons */
.dx__btn{display:inline-flex;align-items:center;justify-content:center;gap:10px;min-height:54px;padding:14px 28px;border-radius:999px;border:2px solid var(--dx-teal);background:var(--dx-teal);color:var(--dx-ivory)!important;font:500 1rem/1.2 'Jost',system-ui,sans-serif;letter-spacing:.03em;text-decoration:none!important;cursor:pointer;transition:transform .2s ease,box-shadow .2s ease,background .2s ease;width:100%}
.dx__btn:hover{transform:translateY(-2px);box-shadow:0 14px 30px -14px rgba(1,38,43,.7)}
.dx__btn--gold{background:var(--dx-goldgrad);border-color:transparent;color:var(--dx-teal)!important;font-weight:700}
.dx__btn--gold:hover{box-shadow:0 14px 30px -12px rgba(230,205,150,.55)}
.dx__btn--line{background:transparent;color:var(--dx-teal)!important}
.dx--teal .dx__btn--line,.dx--deep .dx__btn--line{border-color:var(--dx-champ);color:var(--dx-champ)!important}
.dx__btn svg{width:18px;height:18px;flex:none}
.dx__link{color:var(--dx-teal);font-weight:500;text-decoration:underline;text-decoration-color:var(--dx-gold);text-decoration-thickness:2px;text-underline-offset:5px}
.dx--teal .dx__link,.dx--deep .dx__link{color:var(--dx-champ);text-decoration-color:var(--dx-champ)}
.dx a:focus-visible,.dx button:focus-visible,.dx input:focus-visible{outline:3px solid var(--dx-gold);outline-offset:3px}
.dx--teal a:focus-visible,.dx--teal button:focus-visible,.dx--teal input:focus-visible,.dx--deep a:focus-visible,.dx--deep button:focus-visible{outline-color:var(--dx-champ)}
.dx__sr{position:absolute!important;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0);white-space:nowrap}
/* Gentle reveal on scroll (only when the global head script runs) */
.dx-js .dx [data-reveal]{opacity:0;transform:translateY(22px);transition:opacity .7s ease,transform .7s ease}
.dx-js .dx [data-reveal].is-in{opacity:1;transform:none}
@media (min-width:640px){.dx{padding:96px 32px}.dx__btn{width:auto}}
@media (prefers-reduced-motion:reduce){.dx *{transition:none!important;animation:none!important}.dx-js .dx [data-reveal]{opacity:1;transform:none}}
/* ---- Distinct motion kit: flipping words and flip cards ---- */
.dx-rot{display:inline}
.dx-rot__win{display:inline-grid;perspective:700px;vertical-align:bottom}
.dx-rot__w{grid-area:1/1;opacity:0;transform:rotateX(-95deg);transform-origin:50% 100%;transition:transform .75s cubic-bezier(.2,.8,.2,1),opacity .5s ease;white-space:nowrap}
.dx-rot__w.is-on{opacity:1;transform:none}
.dx-rot__w.is-out{opacity:0;transform:rotateX(95deg);transform-origin:50% 0}
.dx__pause{display:inline-flex;align-items:center;gap:8px;min-height:36px;padding:6px 14px;border-radius:999px;border:1px solid currentColor;background:transparent;color:inherit;font:500 .78rem/1 'Jost',system-ui,sans-serif;letter-spacing:.12em;text-transform:uppercase;cursor:pointer;opacity:.85}
.dx__pause:hover{opacity:1}
.dx__pause svg{width:12px;height:12px;fill:currentColor}
/* Flip cards (3D). Without JS both faces simply stack. */
.dx-flips{list-style:none;margin:0;padding:0;display:grid;gap:20px}
.dx-flip{perspective:1400px}
.dx-flip__inner{display:grid}
.dx-flip__face{grid-area:1/1;border-radius:var(--dx-r);overflow:hidden}
.dx-flips.is-live .dx-flip__inner{transition:transform .85s cubic-bezier(.2,.75,.15,1);transform-style:preserve-3d}
.dx-flips.is-live .dx-flip__face{backface-visibility:hidden;-webkit-backface-visibility:hidden}
.dx-flips.is-live .dx-flip__back{transform:rotateY(180deg)}
.dx-flips.is-live .dx-flip.is-flipped .dx-flip__inner{transform:rotateY(180deg)}
.dx-flips:not(.is-live) .dx-flip__face{grid-area:auto}
.dx-flips:not(.is-live) .dx-flip__btn{display:none}
.dx-flips.is-live .dx-flip{cursor:pointer}
.dx-flips.is-live .dx-flip.is-peek .dx-flip__inner{animation:dxPeek 1.4s cubic-bezier(.3,.7,.3,1) .3s 1}
@keyframes dxPeek{0%,100%{transform:none}35%{transform:rotateY(-24deg)}65%{transform:rotateY(8deg)}}
.dx-flip__btn{display:inline-flex;align-items:center;gap:8px;margin-top:auto;padding:10px 0 0;border:0;background:none;color:inherit;font:500 .9rem/1.2 'Jost',system-ui,sans-serif;letter-spacing:.06em;cursor:pointer}
.dx-flip__btn svg{width:18px;height:18px;stroke:currentColor;transition:transform .5s ease}
.dx-flip:hover .dx-flip__front .dx-flip__btn svg{transform:rotate(180deg)}
@media (min-width:640px){.dx-flips--3{grid-template-columns:repeat(3,1fr)}}
@media (max-width:859px) and (min-width:640px){.dx-flips--3{grid-template-columns:1fr 1fr}}
@media (prefers-reduced-motion:reduce){
  .dx-rot__win{display:none}
  .dx-rot .dx__sr{position:static!important;width:auto;height:auto;clip:auto;white-space:normal}
  .dx__pause{display:none}
}
.dx-tv__grid{display:grid;gap:30px;align-items:center}
.dx-video{position:relative;width:100%;aspect-ratio:16/9;border-radius:var(--dx-r);overflow:hidden;background:var(--dx-grad);box-shadow:0 0 0 1px rgba(177,129,50,.5),0 0 0 8px rgba(0,59,66,.06),0 40px 70px -34px rgba(1,38,43,.7)}
.dx-video iframe,.dx-video video{position:absolute;inset:0;width:100%;height:100%;border:0}
.dx-video__ph{position:absolute;inset:14px;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:12px;text-align:center;border:1.5px dashed rgba(230,205,150,.55);border-radius:var(--dx-r-sm);padding:16px;color:var(--dx-ivory)}
.dx-video__play{position:relative;width:76px;height:76px;border-radius:50%;background:var(--dx-goldgrad);display:grid;place-items:center}
.dx-video__play::before{content:"";position:absolute;inset:-10px;border-radius:50%;border:1px solid rgba(230,205,150,.5);animation:dxPulse 2.4s ease-out infinite}
.dx-video__play svg{width:26px;height:26px;margin-left:4px;fill:var(--dx-teal)}
.dx-video__ph strong{font-size:1.2rem;color:var(--dx-ivory)}
.dx-video__ph span{font-size:.85rem;color:var(--dx-mist)}
@keyframes dxPulse{0%{transform:scale(.85);opacity:1}100%{transform:scale(1.35);opacity:0}}
.dx-tv__login{display:grid;gap:18px;margin-top:34px;padding:26px 24px;border-radius:var(--dx-r);background:var(--dx-grad);color:var(--dx-mist)}
.dx-tv__login p{margin:0;font-size:1.12rem;font-weight:500;color:var(--dx-ivory)}
.dx-tv__tips{list-style:none;margin:22px 0 0;padding:0;display:grid;gap:12px}
.dx-tv__tips li{position:relative;padding-left:24px}
.dx-tv__tips li::before{content:"";position:absolute;left:2px;top:.62em;width:9px;height:9px;background:var(--dx-gold);transform:rotate(45deg)}
.dx-tv__next{margin-top:22px}
@supports not (aspect-ratio:16/9){.dx-video{height:0;padding-top:56.25%}}
@media (min-width:900px){.dx-tv__grid{grid-template-columns:1.4fr .8fr;gap:56px}.dx-tv__login{grid-template-columns:1fr auto;align-items:center;padding:30px 34px}}
</style>
<div class="dx__in">
  <div class="dx-tv__grid">
    <div class="dx-video" data-reveal>
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
    <div data-reveal>
      <p class="dx__eyebrow">Step 2 · Your secure portal</p>
      <h2 id="dx-tv-title">How to set up your TaxDome <em>account.</em></h2>
      <p class="dx__sub">TaxDome is our secure client portal. This walkthrough shows you how to get in.</p>
      <ul class="dx-tv__tips">
        <li><strong>Once you're in:</strong> your to-do list is the first thing you see on Home, and your files live under <strong>Docs</strong>.</li>
        <li><strong>On your phone?</strong> The TaxDome Client Portal app for Apple and Android has a built-in document scanner.</li>
      </ul>
    </div>
  </div>
  <div class="dx-tv__login dx__framed" data-reveal>
    <p>Check your email for your secure TaxDome invitation, or log in to your existing portal.</p>
    <a class="dx__btn dx__btn--gold" href="[TAXDOME PORTAL LINK]" target="_blank" rel="noopener">Log in to TaxDome
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M14 4h6v6M20 4l-9 9M18 14v5a1 1 0 0 1-1 1H5a1 1 0 0 1-1-1V7a1 1 0 0 1 1-1h5"/></svg><span class="dx__sr">(opens in a new tab)</span></a>
  </div>
  <div class="dx-tv__next"><a class="dx__link" href="#checklist">Next: your document checklist →</a></div>
</div>
</section>
```

## SECTION 5: Document Checklist (`#checklist`)

**GHL build note:** Section: full width, background #F2F6F6, padding 0. Flip cards: front shows the mock-up, back shows where to find it. Swap each image placeholder for your mock-up (see comments). Alysha must confirm the document list. Add a 1-column row, then a **Custom Code** element, and paste the block below. Paste-ready file: `ghl-blocks/05-checklist.html`.

```html
<!-- ===== SECTION 5: DOCUMENT CHECKLIST (#checklist) ===== -->
<!-- ALYSHA TO CONFIRM: starting list is prior tax returns, year-to-date P&L, IRS/state letters.
     To add a document, copy one <li class="dx-flip dx-doc">…</li> block. Cards flip to show where to find each document. -->
<section id="checklist" class="dx dx--tint dx-check" tabindex="-1" aria-labelledby="dx-check-title">
<style>
@import url('https://fonts.googleapis.com/css2?family=Jost:ital,wght@0,400;0,500;0,700;1,500;1,700&display=swap');
/* Distinct brand tokens (DTCG Canva designs, Nov 2026). Dark teal leads; gold accents; white for reading areas. */
.dx{--dx-teal:#003b42;--dx-deep:#01262b;--dx-teal-hi:#04333a;--dx-gold:#b18132;--dx-gold-dk:#96691c;--dx-champ:#e6cd96;--dx-champ-hi:#f1e2b8;--dx-ivory:#f3ede1;--dx-mist:#c9d6d2;--dx-body:#3b4f52;--dx-white:#ffffff;--dx-tint:#f2f6f6;
  --dx-grad:linear-gradient(135deg,#04333a 0%,#003b42 45%,#01262b 100%);
  --dx-goldgrad:linear-gradient(135deg,#f1e2b8 0%,#e6cd96 55%,#d9b878 100%);
  --dx-line:rgba(177,129,50,.35);--dx-line-lt:rgba(230,205,150,.35);--dx-r:20px;--dx-r-sm:14px;
  position:relative;display:block;box-sizing:border-box;overflow:hidden;font-family:'Jost',system-ui,-apple-system,'Segoe UI',sans-serif;font-weight:400;font-size:17px;line-height:1.6;color:var(--dx-body);background:var(--dx-white);padding:64px 20px;scroll-margin-top:12px;-webkit-font-smoothing:antialiased}
.dx *,.dx *::before,.dx *::after{box-sizing:border-box}
.dx:focus{outline:none}
.dx__in{position:relative;z-index:1;max-width:1040px;margin:0 auto}
:where(.dx) h1,:where(.dx) h2,:where(.dx) h3{font-family:inherit;font-weight:700;color:var(--dx-teal);margin:0;letter-spacing:-.015em}
:where(.dx) h2{font-size:clamp(1.9rem,6.2vw,3rem);line-height:1.08;margin-bottom:16px}
:where(.dx) h3{font-size:1.22rem;line-height:1.3;margin-bottom:6px}
:where(.dx) p{margin:0 0 14px}
:where(.dx) strong{color:var(--dx-teal)}
:where(.dx) h1 em,:where(.dx) h2 em{font-style:italic;font-weight:700;color:var(--dx-gold)}
.dx__eyebrow{display:flex;align-items:center;gap:12px;margin:0 0 14px;font-weight:500;font-size:.78rem;letter-spacing:.2em;text-transform:uppercase;color:var(--dx-gold-dk)}
.dx__eyebrow::before{content:"";flex:0 0 44px;height:2px;border-radius:2px;background:var(--dx-gold)}
.dx__sub{font-weight:400;font-size:1.1rem;max-width:640px}
/* Teal sections: the brand's lead surface */
.dx--teal{background:var(--dx-grad);color:var(--dx-mist)}
.dx--deep{background:var(--dx-deep);color:var(--dx-mist)}
.dx--teal h1,.dx--teal h2,.dx--teal h3,.dx--teal strong,.dx--deep h1,.dx--deep h2,.dx--deep h3,.dx--deep strong{color:var(--dx-ivory)}
.dx--teal h1 em,.dx--teal h2 em,.dx--deep h1 em,.dx--deep h2 em{color:var(--dx-champ)}
.dx--teal .dx__eyebrow,.dx--deep .dx__eyebrow{color:var(--dx-champ)}
.dx--teal .dx__eyebrow::before,.dx--deep .dx__eyebrow::before{background:var(--dx-champ)}
.dx--tint{background:var(--dx-tint)}
/* Signature: double hairline frame + concentric circles (business cards, decks) */
.dx__framed{position:relative}
.dx__framed::after{content:"";position:absolute;inset:8px;border:1px solid var(--dx-line);border-radius:calc(var(--dx-r) - 5px);pointer-events:none}
.dx--teal .dx__framed::after,.dx--deep .dx__framed::after,.dx__framed--lt::after{border-color:var(--dx-line-lt)}
.dx__rings{position:absolute;z-index:0;width:560px;height:560px;border-radius:50%;border:1px solid rgba(230,205,150,.22);pointer-events:none}
.dx__rings::before,.dx__rings::after{content:"";position:absolute;border-radius:50%;border:1px solid rgba(230,205,150,.16)}
.dx__rings::before{inset:70px}.dx__rings::after{inset:140px}
/* Buttons */
.dx__btn{display:inline-flex;align-items:center;justify-content:center;gap:10px;min-height:54px;padding:14px 28px;border-radius:999px;border:2px solid var(--dx-teal);background:var(--dx-teal);color:var(--dx-ivory)!important;font:500 1rem/1.2 'Jost',system-ui,sans-serif;letter-spacing:.03em;text-decoration:none!important;cursor:pointer;transition:transform .2s ease,box-shadow .2s ease,background .2s ease;width:100%}
.dx__btn:hover{transform:translateY(-2px);box-shadow:0 14px 30px -14px rgba(1,38,43,.7)}
.dx__btn--gold{background:var(--dx-goldgrad);border-color:transparent;color:var(--dx-teal)!important;font-weight:700}
.dx__btn--gold:hover{box-shadow:0 14px 30px -12px rgba(230,205,150,.55)}
.dx__btn--line{background:transparent;color:var(--dx-teal)!important}
.dx--teal .dx__btn--line,.dx--deep .dx__btn--line{border-color:var(--dx-champ);color:var(--dx-champ)!important}
.dx__btn svg{width:18px;height:18px;flex:none}
.dx__link{color:var(--dx-teal);font-weight:500;text-decoration:underline;text-decoration-color:var(--dx-gold);text-decoration-thickness:2px;text-underline-offset:5px}
.dx--teal .dx__link,.dx--deep .dx__link{color:var(--dx-champ);text-decoration-color:var(--dx-champ)}
.dx a:focus-visible,.dx button:focus-visible,.dx input:focus-visible{outline:3px solid var(--dx-gold);outline-offset:3px}
.dx--teal a:focus-visible,.dx--teal button:focus-visible,.dx--teal input:focus-visible,.dx--deep a:focus-visible,.dx--deep button:focus-visible{outline-color:var(--dx-champ)}
.dx__sr{position:absolute!important;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0);white-space:nowrap}
/* Gentle reveal on scroll (only when the global head script runs) */
.dx-js .dx [data-reveal]{opacity:0;transform:translateY(22px);transition:opacity .7s ease,transform .7s ease}
.dx-js .dx [data-reveal].is-in{opacity:1;transform:none}
@media (min-width:640px){.dx{padding:96px 32px}.dx__btn{width:auto}}
@media (prefers-reduced-motion:reduce){.dx *{transition:none!important;animation:none!important}.dx-js .dx [data-reveal]{opacity:1;transform:none}}
/* ---- Distinct motion kit: flipping words and flip cards ---- */
.dx-rot{display:inline}
.dx-rot__win{display:inline-grid;perspective:700px;vertical-align:bottom}
.dx-rot__w{grid-area:1/1;opacity:0;transform:rotateX(-95deg);transform-origin:50% 100%;transition:transform .75s cubic-bezier(.2,.8,.2,1),opacity .5s ease;white-space:nowrap}
.dx-rot__w.is-on{opacity:1;transform:none}
.dx-rot__w.is-out{opacity:0;transform:rotateX(95deg);transform-origin:50% 0}
.dx__pause{display:inline-flex;align-items:center;gap:8px;min-height:36px;padding:6px 14px;border-radius:999px;border:1px solid currentColor;background:transparent;color:inherit;font:500 .78rem/1 'Jost',system-ui,sans-serif;letter-spacing:.12em;text-transform:uppercase;cursor:pointer;opacity:.85}
.dx__pause:hover{opacity:1}
.dx__pause svg{width:12px;height:12px;fill:currentColor}
/* Flip cards (3D). Without JS both faces simply stack. */
.dx-flips{list-style:none;margin:0;padding:0;display:grid;gap:20px}
.dx-flip{perspective:1400px}
.dx-flip__inner{display:grid}
.dx-flip__face{grid-area:1/1;border-radius:var(--dx-r);overflow:hidden}
.dx-flips.is-live .dx-flip__inner{transition:transform .85s cubic-bezier(.2,.75,.15,1);transform-style:preserve-3d}
.dx-flips.is-live .dx-flip__face{backface-visibility:hidden;-webkit-backface-visibility:hidden}
.dx-flips.is-live .dx-flip__back{transform:rotateY(180deg)}
.dx-flips.is-live .dx-flip.is-flipped .dx-flip__inner{transform:rotateY(180deg)}
.dx-flips:not(.is-live) .dx-flip__face{grid-area:auto}
.dx-flips:not(.is-live) .dx-flip__btn{display:none}
.dx-flips.is-live .dx-flip{cursor:pointer}
.dx-flips.is-live .dx-flip.is-peek .dx-flip__inner{animation:dxPeek 1.4s cubic-bezier(.3,.7,.3,1) .3s 1}
@keyframes dxPeek{0%,100%{transform:none}35%{transform:rotateY(-24deg)}65%{transform:rotateY(8deg)}}
.dx-flip__btn{display:inline-flex;align-items:center;gap:8px;margin-top:auto;padding:10px 0 0;border:0;background:none;color:inherit;font:500 .9rem/1.2 'Jost',system-ui,sans-serif;letter-spacing:.06em;cursor:pointer}
.dx-flip__btn svg{width:18px;height:18px;stroke:currentColor;transition:transform .5s ease}
.dx-flip:hover .dx-flip__front .dx-flip__btn svg{transform:rotate(180deg)}
@media (min-width:640px){.dx-flips--3{grid-template-columns:repeat(3,1fr)}}
@media (max-width:859px) and (min-width:640px){.dx-flips--3{grid-template-columns:1fr 1fr}}
@media (prefers-reduced-motion:reduce){
  .dx-rot__win{display:none}
  .dx-rot .dx__sr{position:static!important;width:auto;height:auto;clip:auto;white-space:normal}
  .dx__pause{display:none}
}
.dx-check__top{margin-bottom:34px}
.dx-doc .dx-flip__front{display:flex;flex-direction:column;background:var(--dx-white);box-shadow:0 1px 0 rgba(0,59,66,.08),0 26px 50px -36px rgba(1,38,43,.6)}
.dx-doc:hover .dx-flip__front{box-shadow:0 0 0 2px var(--dx-gold),0 30px 56px -36px rgba(1,38,43,.7)}
.dx-doc__img{position:relative;aspect-ratio:4/3;background:var(--dx-grad)}
.dx-doc__img img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}
.dx-doc__ph{position:absolute;inset:12px;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:10px;text-align:center;border:1.5px dashed rgba(230,205,150,.55);border-radius:var(--dx-r-sm);font-size:.8rem;line-height:1.35;padding:12px;color:var(--dx-mist)}
.dx-doc__ph svg{width:40px;height:40px;stroke:var(--dx-champ)}
.dx-doc__tag{position:absolute;left:16px;bottom:-18px;z-index:1;width:42px;height:42px;border-radius:50%;background:var(--dx-goldgrad);display:grid;place-items:center;font-weight:700;color:var(--dx-teal);box-shadow:0 6px 14px -6px rgba(0,0,0,.4)}
.dx-doc__body{display:flex;flex-direction:column;flex:1;padding:32px 22px 20px}
.dx-doc .dx-flip__front .dx-flip__btn{color:var(--dx-teal);font-weight:700}
.dx-doc .dx-flip__back{position:relative;display:flex;flex-direction:column;padding:34px 26px 24px;background:var(--dx-grad);color:var(--dx-ivory);box-shadow:0 0 0 2px var(--dx-champ),0 26px 50px -36px rgba(1,38,43,.7)}
.dx-doc .dx-flip__back::after{content:"";position:absolute;inset:8px;border:1px solid rgba(230,205,150,.28);border-radius:15px;pointer-events:none}
.dx-doc__label{font-weight:500;font-size:.75rem;letter-spacing:.22em;text-transform:uppercase;color:var(--dx-champ);margin-bottom:12px}
.dx-doc .dx-flip__back h3{color:var(--dx-ivory)}
.dx-doc .dx-flip__back p{font-size:1.08rem;margin:10px 0 18px}
.dx-doc .dx-flip__back .dx-flip__btn{color:var(--dx-champ);position:relative;z-index:1}
.dx-check__notes{margin-top:26px;display:grid;gap:14px}
.dx-note{display:flex;gap:16px;align-items:flex-start;background:var(--dx-grad);color:var(--dx-mist);border-radius:var(--dx-r);padding:22px 24px}
.dx-note__ic{flex:none;width:40px;height:40px;border-radius:50%;background:var(--dx-goldgrad);display:grid;place-items:center}
.dx-note__ic svg{width:20px;height:20px;stroke:var(--dx-teal)}
.dx-note p{margin:0}
.dx-note strong{color:var(--dx-champ)}
@media (min-width:860px){.dx-check__notes{grid-template-columns:1fr 1fr}}
</style>
<div class="dx__in">
  <div class="dx-check__top" data-reveal>
    <p class="dx__eyebrow">Step 3 · Judgment-free</p>
    <h2 id="dx-check-title">Your document <em>checklist.</em></h2>
    <p class="dx__sub" style="margin:0">Here's what each document looks like. Flip a card to see where to find it, then upload everything to your TaxDome portal.</p>
  </div>
  <ul class="dx-flips dx-flips--3">
    <li class="dx-flip dx-doc" data-reveal>
      <div class="dx-flip__inner">
        <div class="dx-flip__face dx-flip__front">
          <div class="dx-doc__img">
            <!-- IMAGE SLOT: replace the placeholder div with
                 <img src="[IMAGE: PRIOR TAX RETURN MOCK-UP]" alt="Sample first page of a prior-year tax return" loading="lazy"> -->
            <div class="dx-doc__ph" role="img" aria-label="Sample first page of a prior-year tax return">
              <svg viewBox="0 0 24 24" fill="none" stroke-width="1.5" aria-hidden="true"><path d="M7 3h7l5 5v13H7z"/><path d="M14 3v5h5M10 13h6M10 17h6"/></svg>
              [IMAGE: PRIOR TAX RETURN MOCK-UP]
            </div>
            <span class="dx-doc__tag" aria-hidden="true">1</span>
          </div>
          <div class="dx-doc__body">
            <h3>Prior tax returns</h3>
            <button type="button" class="dx-flip__btn" aria-expanded="false">Where do I find it? <svg viewBox="0 0 24 24" fill="none" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M3 12a9 9 0 0 1 15.5-6.2L21 8M21 3v5h-5"/></svg></button>
          </div>
        </div>
        <div class="dx-flip__face dx-flip__back">
          <span class="dx-doc__label">Where to find it</span>
          <h3>Prior tax returns</h3>
          <p>Your copy from whoever prepared your return, or the PDF saved in your tax software. Include personal and business returns.</p>
          <button type="button" class="dx-flip__btn" aria-expanded="false">Flip back <svg viewBox="0 0 24 24" fill="none" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M21 12a9 9 0 0 1-15.5 6.2L3 16M3 21v-5h5"/></svg></button>
        </div>
      </div>
    </li>
    <li class="dx-flip dx-doc" data-reveal>
      <div class="dx-flip__inner">
        <div class="dx-flip__face dx-flip__front">
          <div class="dx-doc__img">
            <!-- IMAGE SLOT: replace the placeholder div with
                 <img src="[IMAGE: YEAR-TO-DATE PROFIT AND LOSS MOCK-UP]" alt="Sample year-to-date profit and loss report" loading="lazy"> -->
            <div class="dx-doc__ph" role="img" aria-label="Sample year-to-date profit and loss report">
              <svg viewBox="0 0 24 24" fill="none" stroke-width="1.5" aria-hidden="true"><path d="M4 20h16M7 16v-4M12 16V8M17 16v-7"/></svg>
              [IMAGE: YEAR-TO-DATE PROFIT AND LOSS MOCK-UP]
            </div>
            <span class="dx-doc__tag" aria-hidden="true">2</span>
          </div>
          <div class="dx-doc__body">
            <h3>Year-to-date profit and loss</h3>
            <button type="button" class="dx-flip__btn" aria-expanded="false">Where do I find it? <svg viewBox="0 0 24 24" fill="none" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M3 12a9 9 0 0 1 15.5-6.2L21 8M21 3v5h-5"/></svg></button>
          </div>
        </div>
        <div class="dx-flip__face dx-flip__back">
          <span class="dx-doc__label">Where to find it</span>
          <h3>Year-to-date profit and loss</h3>
          <p>Run a Profit and Loss report in your bookkeeping software, dated from January 1 to today, or ask your bookkeeper for it.</p>
          <button type="button" class="dx-flip__btn" aria-expanded="false">Flip back <svg viewBox="0 0 24 24" fill="none" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M21 12a9 9 0 0 1-15.5 6.2L3 16M3 21v-5h5"/></svg></button>
        </div>
      </div>
    </li>
    <li class="dx-flip dx-doc" data-reveal>
      <div class="dx-flip__inner">
        <div class="dx-flip__face dx-flip__front">
          <div class="dx-doc__img">
            <!-- IMAGE SLOT: replace the placeholder div with
                 <img src="[IMAGE: IRS OR STATE LETTER MOCK-UP]" alt="Sample IRS or state tax notice letter" loading="lazy"> -->
            <div class="dx-doc__ph" role="img" aria-label="Sample IRS or state tax notice letter">
              <svg viewBox="0 0 24 24" fill="none" stroke-width="1.5" aria-hidden="true"><rect x="3" y="5" width="18" height="14" rx="2"/><path d="M3 7l9 6 9-6"/></svg>
              [IMAGE: IRS OR STATE LETTER MOCK-UP]
            </div>
            <span class="dx-doc__tag" aria-hidden="true">3</span>
          </div>
          <div class="dx-doc__body">
            <h3>Any IRS or state letters</h3>
            <button type="button" class="dx-flip__btn" aria-expanded="false">Where do I find it? <svg viewBox="0 0 24 24" fill="none" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M3 12a9 9 0 0 1 15.5-6.2L21 8M21 3v5h-5"/></svg></button>
          </div>
        </div>
        <div class="dx-flip__face dx-flip__back">
          <span class="dx-doc__label">Where to find it</span>
          <h3>Any IRS or state letters</h3>
          <p>Notices mailed to you by the IRS or your state tax agency. The notice number is usually printed in the top right corner.</p>
          <button type="button" class="dx-flip__btn" aria-expanded="false">Flip back <svg viewBox="0 0 24 24" fill="none" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M21 12a9 9 0 0 1-15.5 6.2L3 16M3 21v-5h5"/></svg></button>
        </div>
      </div>
    </li>
  </ul>
  <div class="dx-check__notes">
    <div class="dx-note" data-reveal>
      <span class="dx-note__ic" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M20 6L9 17l-5-5"/></svg></span>
      <p><strong>Partial uploads are fine.</strong> Upload what you have now and add the rest as you find it.</p>
    </div>
    <div class="dx-note" data-reveal>
      <span class="dx-note__ic" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 19h16M6 15l9-9 3 3-9 9H6z"/></svg></span>
      <p><strong>Books behind?</strong> We're a judgment-free firm. Upload what you have and note what's missing in the organizer.</p>
    </div>
  </div>
</div>
<script>
/* Distinct motion kit: rotating words, pause control, flip cards. Scoped to this section only. */
(function(root){
  if(!root) return;
  var reduce=window.matchMedia&&window.matchMedia('(prefers-reduced-motion: reduce)').matches, paused=false;
  [].forEach.call(root.querySelectorAll('[data-rot]'),function(r){
    var w=r.querySelectorAll('.dx-rot__w'),i=0,hover=false; if(!w.length) return;
    w[0].classList.add('is-on'); if(reduce) return;
    r.addEventListener('mouseenter',function(){hover=true}); r.addEventListener('mouseleave',function(){hover=false});
    setInterval(function(){
      if(paused||hover||document.hidden) return;
      var c=w[i]; c.classList.remove('is-on'); c.classList.add('is-out');
      setTimeout(function(){c.classList.remove('is-out')},800);
      i=(i+1)%w.length; w[i].classList.add('is-on');
    },+r.getAttribute('data-rot')||2600);
  });
  [].forEach.call(root.querySelectorAll('[data-pause]'),function(b){
    b.addEventListener('click',function(){
      paused=!paused; b.setAttribute('aria-pressed',paused);
      b.querySelector('[data-pause-label]').textContent=paused?'Play motion':'Pause motion';
    });
  });
  [].forEach.call(root.querySelectorAll('.dx-flips'),function(list){
    list.classList.add('is-live');
    var cards=list.querySelectorAll('.dx-flip');
    function set(card,on){
      card.classList.toggle('is-flipped',on);
      var f=card.querySelector('.dx-flip__front'), k=card.querySelector('.dx-flip__back');
      (on?f:k).setAttribute('inert',''); (on?k:f).removeAttribute('inert');
      [].forEach.call(card.querySelectorAll('.dx-flip__btn'),function(x){x.setAttribute('aria-expanded',on)});
    }
    [].forEach.call(cards,function(c){
      set(c,false);
      c.addEventListener('click',function(e){
        if(e.target.closest('a')) return;
        var on=!c.classList.contains('is-flipped'); set(c,on);
        if(e.detail===0){var t=c.querySelector(on?'.dx-flip__back .dx-flip__btn':'.dx-flip__front .dx-flip__btn'); if(t) t.focus();}
      });
    });
    if(!reduce&&cards[0]&&'IntersectionObserver' in window){
      var io=new IntersectionObserver(function(es){if(es[0].isIntersecting){cards[0].classList.add('is-peek');io.disconnect();}},{threshold:.6});
      io.observe(cards[0]);
    }
  });
})(document.currentScript&&document.currentScript.closest('.dx'));
</script>
</section>
```

## SECTION 6: Organizer (`#organizer`)

**GHL build note:** Section: full width, background #003B42, padding 0. Includes the turning-words card with its Pause motion button. Add a 1-column row, then a **Custom Code** element, and paste the block below. Paste-ready file: `ghl-blocks/06-organizer.html`.

```html
<!-- ===== SECTION 6: ORGANIZER (#organizer) ===== -->
<section id="organizer" class="dx dx--teal dx-org" tabindex="-1" aria-labelledby="dx-org-title">
<style>
@import url('https://fonts.googleapis.com/css2?family=Jost:ital,wght@0,400;0,500;0,700;1,500;1,700&display=swap');
/* Distinct brand tokens (DTCG Canva designs, Nov 2026). Dark teal leads; gold accents; white for reading areas. */
.dx{--dx-teal:#003b42;--dx-deep:#01262b;--dx-teal-hi:#04333a;--dx-gold:#b18132;--dx-gold-dk:#96691c;--dx-champ:#e6cd96;--dx-champ-hi:#f1e2b8;--dx-ivory:#f3ede1;--dx-mist:#c9d6d2;--dx-body:#3b4f52;--dx-white:#ffffff;--dx-tint:#f2f6f6;
  --dx-grad:linear-gradient(135deg,#04333a 0%,#003b42 45%,#01262b 100%);
  --dx-goldgrad:linear-gradient(135deg,#f1e2b8 0%,#e6cd96 55%,#d9b878 100%);
  --dx-line:rgba(177,129,50,.35);--dx-line-lt:rgba(230,205,150,.35);--dx-r:20px;--dx-r-sm:14px;
  position:relative;display:block;box-sizing:border-box;overflow:hidden;font-family:'Jost',system-ui,-apple-system,'Segoe UI',sans-serif;font-weight:400;font-size:17px;line-height:1.6;color:var(--dx-body);background:var(--dx-white);padding:64px 20px;scroll-margin-top:12px;-webkit-font-smoothing:antialiased}
.dx *,.dx *::before,.dx *::after{box-sizing:border-box}
.dx:focus{outline:none}
.dx__in{position:relative;z-index:1;max-width:1040px;margin:0 auto}
:where(.dx) h1,:where(.dx) h2,:where(.dx) h3{font-family:inherit;font-weight:700;color:var(--dx-teal);margin:0;letter-spacing:-.015em}
:where(.dx) h2{font-size:clamp(1.9rem,6.2vw,3rem);line-height:1.08;margin-bottom:16px}
:where(.dx) h3{font-size:1.22rem;line-height:1.3;margin-bottom:6px}
:where(.dx) p{margin:0 0 14px}
:where(.dx) strong{color:var(--dx-teal)}
:where(.dx) h1 em,:where(.dx) h2 em{font-style:italic;font-weight:700;color:var(--dx-gold)}
.dx__eyebrow{display:flex;align-items:center;gap:12px;margin:0 0 14px;font-weight:500;font-size:.78rem;letter-spacing:.2em;text-transform:uppercase;color:var(--dx-gold-dk)}
.dx__eyebrow::before{content:"";flex:0 0 44px;height:2px;border-radius:2px;background:var(--dx-gold)}
.dx__sub{font-weight:400;font-size:1.1rem;max-width:640px}
/* Teal sections: the brand's lead surface */
.dx--teal{background:var(--dx-grad);color:var(--dx-mist)}
.dx--deep{background:var(--dx-deep);color:var(--dx-mist)}
.dx--teal h1,.dx--teal h2,.dx--teal h3,.dx--teal strong,.dx--deep h1,.dx--deep h2,.dx--deep h3,.dx--deep strong{color:var(--dx-ivory)}
.dx--teal h1 em,.dx--teal h2 em,.dx--deep h1 em,.dx--deep h2 em{color:var(--dx-champ)}
.dx--teal .dx__eyebrow,.dx--deep .dx__eyebrow{color:var(--dx-champ)}
.dx--teal .dx__eyebrow::before,.dx--deep .dx__eyebrow::before{background:var(--dx-champ)}
.dx--tint{background:var(--dx-tint)}
/* Signature: double hairline frame + concentric circles (business cards, decks) */
.dx__framed{position:relative}
.dx__framed::after{content:"";position:absolute;inset:8px;border:1px solid var(--dx-line);border-radius:calc(var(--dx-r) - 5px);pointer-events:none}
.dx--teal .dx__framed::after,.dx--deep .dx__framed::after,.dx__framed--lt::after{border-color:var(--dx-line-lt)}
.dx__rings{position:absolute;z-index:0;width:560px;height:560px;border-radius:50%;border:1px solid rgba(230,205,150,.22);pointer-events:none}
.dx__rings::before,.dx__rings::after{content:"";position:absolute;border-radius:50%;border:1px solid rgba(230,205,150,.16)}
.dx__rings::before{inset:70px}.dx__rings::after{inset:140px}
/* Buttons */
.dx__btn{display:inline-flex;align-items:center;justify-content:center;gap:10px;min-height:54px;padding:14px 28px;border-radius:999px;border:2px solid var(--dx-teal);background:var(--dx-teal);color:var(--dx-ivory)!important;font:500 1rem/1.2 'Jost',system-ui,sans-serif;letter-spacing:.03em;text-decoration:none!important;cursor:pointer;transition:transform .2s ease,box-shadow .2s ease,background .2s ease;width:100%}
.dx__btn:hover{transform:translateY(-2px);box-shadow:0 14px 30px -14px rgba(1,38,43,.7)}
.dx__btn--gold{background:var(--dx-goldgrad);border-color:transparent;color:var(--dx-teal)!important;font-weight:700}
.dx__btn--gold:hover{box-shadow:0 14px 30px -12px rgba(230,205,150,.55)}
.dx__btn--line{background:transparent;color:var(--dx-teal)!important}
.dx--teal .dx__btn--line,.dx--deep .dx__btn--line{border-color:var(--dx-champ);color:var(--dx-champ)!important}
.dx__btn svg{width:18px;height:18px;flex:none}
.dx__link{color:var(--dx-teal);font-weight:500;text-decoration:underline;text-decoration-color:var(--dx-gold);text-decoration-thickness:2px;text-underline-offset:5px}
.dx--teal .dx__link,.dx--deep .dx__link{color:var(--dx-champ);text-decoration-color:var(--dx-champ)}
.dx a:focus-visible,.dx button:focus-visible,.dx input:focus-visible{outline:3px solid var(--dx-gold);outline-offset:3px}
.dx--teal a:focus-visible,.dx--teal button:focus-visible,.dx--teal input:focus-visible,.dx--deep a:focus-visible,.dx--deep button:focus-visible{outline-color:var(--dx-champ)}
.dx__sr{position:absolute!important;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0);white-space:nowrap}
/* Gentle reveal on scroll (only when the global head script runs) */
.dx-js .dx [data-reveal]{opacity:0;transform:translateY(22px);transition:opacity .7s ease,transform .7s ease}
.dx-js .dx [data-reveal].is-in{opacity:1;transform:none}
@media (min-width:640px){.dx{padding:96px 32px}.dx__btn{width:auto}}
@media (prefers-reduced-motion:reduce){.dx *{transition:none!important;animation:none!important}.dx-js .dx [data-reveal]{opacity:1;transform:none}}
/* ---- Distinct motion kit: flipping words and flip cards ---- */
.dx-rot{display:inline}
.dx-rot__win{display:inline-grid;perspective:700px;vertical-align:bottom}
.dx-rot__w{grid-area:1/1;opacity:0;transform:rotateX(-95deg);transform-origin:50% 100%;transition:transform .75s cubic-bezier(.2,.8,.2,1),opacity .5s ease;white-space:nowrap}
.dx-rot__w.is-on{opacity:1;transform:none}
.dx-rot__w.is-out{opacity:0;transform:rotateX(95deg);transform-origin:50% 0}
.dx__pause{display:inline-flex;align-items:center;gap:8px;min-height:36px;padding:6px 14px;border-radius:999px;border:1px solid currentColor;background:transparent;color:inherit;font:500 .78rem/1 'Jost',system-ui,sans-serif;letter-spacing:.12em;text-transform:uppercase;cursor:pointer;opacity:.85}
.dx__pause:hover{opacity:1}
.dx__pause svg{width:12px;height:12px;fill:currentColor}
/* Flip cards (3D). Without JS both faces simply stack. */
.dx-flips{list-style:none;margin:0;padding:0;display:grid;gap:20px}
.dx-flip{perspective:1400px}
.dx-flip__inner{display:grid}
.dx-flip__face{grid-area:1/1;border-radius:var(--dx-r);overflow:hidden}
.dx-flips.is-live .dx-flip__inner{transition:transform .85s cubic-bezier(.2,.75,.15,1);transform-style:preserve-3d}
.dx-flips.is-live .dx-flip__face{backface-visibility:hidden;-webkit-backface-visibility:hidden}
.dx-flips.is-live .dx-flip__back{transform:rotateY(180deg)}
.dx-flips.is-live .dx-flip.is-flipped .dx-flip__inner{transform:rotateY(180deg)}
.dx-flips:not(.is-live) .dx-flip__face{grid-area:auto}
.dx-flips:not(.is-live) .dx-flip__btn{display:none}
.dx-flips.is-live .dx-flip{cursor:pointer}
.dx-flips.is-live .dx-flip.is-peek .dx-flip__inner{animation:dxPeek 1.4s cubic-bezier(.3,.7,.3,1) .3s 1}
@keyframes dxPeek{0%,100%{transform:none}35%{transform:rotateY(-24deg)}65%{transform:rotateY(8deg)}}
.dx-flip__btn{display:inline-flex;align-items:center;gap:8px;margin-top:auto;padding:10px 0 0;border:0;background:none;color:inherit;font:500 .9rem/1.2 'Jost',system-ui,sans-serif;letter-spacing:.06em;cursor:pointer}
.dx-flip__btn svg{width:18px;height:18px;stroke:currentColor;transition:transform .5s ease}
.dx-flip:hover .dx-flip__front .dx-flip__btn svg{transform:rotate(180deg)}
@media (min-width:640px){.dx-flips--3{grid-template-columns:repeat(3,1fr)}}
@media (max-width:859px) and (min-width:640px){.dx-flips--3{grid-template-columns:1fr 1fr}}
@media (prefers-reduced-motion:reduce){
  .dx-rot__win{display:none}
  .dx-rot .dx__sr{position:static!important;width:auto;height:auto;clip:auto;white-space:normal}
  .dx__pause{display:none}
}
.dx-org .dx__rings{right:-280px;bottom:-300px}
.dx-org__grid{display:grid;gap:26px;margin-top:30px}
.dx-org__flow{list-style:none;margin:0;padding:0;display:grid;gap:14px}
.dx-org__flow li{display:flex;gap:16px;align-items:flex-start;padding:20px 22px;border-radius:var(--dx-r);background:rgba(243,237,225,.06);border:1px solid rgba(230,205,150,.25)}
.dx-org__flow b{flex:none;display:grid;place-items:center;width:40px;height:40px;border-radius:50%;background:var(--dx-goldgrad);color:var(--dx-teal);font-weight:700}
.dx-org__flow p{margin:0;color:var(--dx-ivory);font-size:1.05rem}
.dx-org__count{position:relative;display:flex;flex-direction:column;justify-content:center;min-height:280px;background:var(--dx-white);color:var(--dx-body);border-radius:var(--dx-r);padding:34px 28px;box-shadow:0 40px 70px -40px rgba(0,0,0,.7)}
.dx-org__count h3{color:var(--dx-teal)!important;font-size:.8rem;font-weight:500;letter-spacing:.22em;text-transform:uppercase;margin-bottom:14px}
.dx-org__say{font-weight:700;font-size:clamp(1.7rem,6vw,2.4rem);line-height:1.15;color:var(--dx-teal);margin:0 0 18px!important}
.dx-org__say .dx-rot__w{color:var(--dx-gold);font-style:italic}
.dx-org__count p{margin:0}
.dx-org__count .dx__pause{align-self:flex-start;margin-top:20px;color:var(--dx-teal)}
@media (min-width:880px){.dx-org__grid{grid-template-columns:1.1fr .9fr;align-items:start;gap:40px}}
</style>
<div class="dx__rings" aria-hidden="true"></div>
<div class="dx__in">
  <div data-reveal>
    <p class="dx__eyebrow">Step 3 · Your organizer</p>
    <h2 id="dx-org-title">How your organizer <em>works.</em></h2>
    <p class="dx__sub">You'll find your organizer inside your TaxDome portal.</p>
  </div>
  <div class="dx-org__grid">
    <ol class="dx-org__flow">
      <li data-reveal><b aria-hidden="true">1</b><p>The organizer first asks how many companies or entities you have.</p></li>
      <li data-reveal><b aria-hidden="true">2</b><p>It then opens a section for each one, so you can tell us about every entity separately.</p></li>
      <li data-reveal><b aria-hidden="true">3</b><p><strong>Be thorough.</strong> Include side businesses, rentals and nonprofits.</p></li>
    </ol>
    <div class="dx-org__count dx__framed" data-reveal>
      <h3>Count every entity</h3>
      <p class="dx-org__say">Include your <span class="dx-rot" data-rot="2200"><span class="dx__sr">main business, side businesses, rentals and nonprofits.</span><span class="dx-rot__win" aria-hidden="true"><span class="dx-rot__w">main business.</span><span class="dx-rot__w">side businesses.</span><span class="dx-rot__w">rentals.</span><span class="dx-rot__w">nonprofits.</span></span></span></p>
      <p>Each one gets its own section in your organizer, so nothing gets missed.</p>
      <button type="button" class="dx__pause" data-pause aria-pressed="false"><svg viewBox="0 0 12 12" aria-hidden="true"><rect x="2" y="1" width="3" height="10"/><rect x="7" y="1" width="3" height="10"/></svg><span data-pause-label>Pause motion</span></button>
    </div>
  </div>
</div>
<script>
/* Distinct motion kit: rotating words, pause control, flip cards. Scoped to this section only. */
(function(root){
  if(!root) return;
  var reduce=window.matchMedia&&window.matchMedia('(prefers-reduced-motion: reduce)').matches, paused=false;
  [].forEach.call(root.querySelectorAll('[data-rot]'),function(r){
    var w=r.querySelectorAll('.dx-rot__w'),i=0,hover=false; if(!w.length) return;
    w[0].classList.add('is-on'); if(reduce) return;
    r.addEventListener('mouseenter',function(){hover=true}); r.addEventListener('mouseleave',function(){hover=false});
    setInterval(function(){
      if(paused||hover||document.hidden) return;
      var c=w[i]; c.classList.remove('is-on'); c.classList.add('is-out');
      setTimeout(function(){c.classList.remove('is-out')},800);
      i=(i+1)%w.length; w[i].classList.add('is-on');
    },+r.getAttribute('data-rot')||2600);
  });
  [].forEach.call(root.querySelectorAll('[data-pause]'),function(b){
    b.addEventListener('click',function(){
      paused=!paused; b.setAttribute('aria-pressed',paused);
      b.querySelector('[data-pause-label]').textContent=paused?'Play motion':'Pause motion';
    });
  });
  [].forEach.call(root.querySelectorAll('.dx-flips'),function(list){
    list.classList.add('is-live');
    var cards=list.querySelectorAll('.dx-flip');
    function set(card,on){
      card.classList.toggle('is-flipped',on);
      var f=card.querySelector('.dx-flip__front'), k=card.querySelector('.dx-flip__back');
      (on?f:k).setAttribute('inert',''); (on?k:f).removeAttribute('inert');
      [].forEach.call(card.querySelectorAll('.dx-flip__btn'),function(x){x.setAttribute('aria-expanded',on)});
    }
    [].forEach.call(cards,function(c){
      set(c,false);
      c.addEventListener('click',function(e){
        if(e.target.closest('a')) return;
        var on=!c.classList.contains('is-flipped'); set(c,on);
        if(e.detail===0){var t=c.querySelector(on?'.dx-flip__back .dx-flip__btn':'.dx-flip__front .dx-flip__btn'); if(t) t.focus();}
      });
    });
    if(!reduce&&cards[0]&&'IntersectionObserver' in window){
      var io=new IntersectionObserver(function(es){if(es[0].isIntersecting){cards[0].classList.add('is-peek');io.disconnect();}},{threshold:.6});
      io.observe(cards[0]);
    }
  });
})(document.currentScript&&document.currentScript.closest('.dx'));
</script>
</section>
```

## SECTION 7: 60-Day Deadline (`#deadline`)

**GHL build note:** Section: full width, background #FFFFFF, padding 0. Static text only: no countdown. Add a 1-column row, then a **Custom Code** element, and paste the block below. Paste-ready file: `ghl-blocks/07-deadline.html`.

```html
<!-- ===== SECTION 7: 60-DAY DEADLINE (#deadline) ===== -->
<section id="deadline" class="dx dx-dead" tabindex="-1" aria-labelledby="dx-dead-title">
<style>
@import url('https://fonts.googleapis.com/css2?family=Jost:ital,wght@0,400;0,500;0,700;1,500;1,700&display=swap');
/* Distinct brand tokens (DTCG Canva designs, Nov 2026). Dark teal leads; gold accents; white for reading areas. */
.dx{--dx-teal:#003b42;--dx-deep:#01262b;--dx-teal-hi:#04333a;--dx-gold:#b18132;--dx-gold-dk:#96691c;--dx-champ:#e6cd96;--dx-champ-hi:#f1e2b8;--dx-ivory:#f3ede1;--dx-mist:#c9d6d2;--dx-body:#3b4f52;--dx-white:#ffffff;--dx-tint:#f2f6f6;
  --dx-grad:linear-gradient(135deg,#04333a 0%,#003b42 45%,#01262b 100%);
  --dx-goldgrad:linear-gradient(135deg,#f1e2b8 0%,#e6cd96 55%,#d9b878 100%);
  --dx-line:rgba(177,129,50,.35);--dx-line-lt:rgba(230,205,150,.35);--dx-r:20px;--dx-r-sm:14px;
  position:relative;display:block;box-sizing:border-box;overflow:hidden;font-family:'Jost',system-ui,-apple-system,'Segoe UI',sans-serif;font-weight:400;font-size:17px;line-height:1.6;color:var(--dx-body);background:var(--dx-white);padding:64px 20px;scroll-margin-top:12px;-webkit-font-smoothing:antialiased}
.dx *,.dx *::before,.dx *::after{box-sizing:border-box}
.dx:focus{outline:none}
.dx__in{position:relative;z-index:1;max-width:1040px;margin:0 auto}
:where(.dx) h1,:where(.dx) h2,:where(.dx) h3{font-family:inherit;font-weight:700;color:var(--dx-teal);margin:0;letter-spacing:-.015em}
:where(.dx) h2{font-size:clamp(1.9rem,6.2vw,3rem);line-height:1.08;margin-bottom:16px}
:where(.dx) h3{font-size:1.22rem;line-height:1.3;margin-bottom:6px}
:where(.dx) p{margin:0 0 14px}
:where(.dx) strong{color:var(--dx-teal)}
:where(.dx) h1 em,:where(.dx) h2 em{font-style:italic;font-weight:700;color:var(--dx-gold)}
.dx__eyebrow{display:flex;align-items:center;gap:12px;margin:0 0 14px;font-weight:500;font-size:.78rem;letter-spacing:.2em;text-transform:uppercase;color:var(--dx-gold-dk)}
.dx__eyebrow::before{content:"";flex:0 0 44px;height:2px;border-radius:2px;background:var(--dx-gold)}
.dx__sub{font-weight:400;font-size:1.1rem;max-width:640px}
/* Teal sections: the brand's lead surface */
.dx--teal{background:var(--dx-grad);color:var(--dx-mist)}
.dx--deep{background:var(--dx-deep);color:var(--dx-mist)}
.dx--teal h1,.dx--teal h2,.dx--teal h3,.dx--teal strong,.dx--deep h1,.dx--deep h2,.dx--deep h3,.dx--deep strong{color:var(--dx-ivory)}
.dx--teal h1 em,.dx--teal h2 em,.dx--deep h1 em,.dx--deep h2 em{color:var(--dx-champ)}
.dx--teal .dx__eyebrow,.dx--deep .dx__eyebrow{color:var(--dx-champ)}
.dx--teal .dx__eyebrow::before,.dx--deep .dx__eyebrow::before{background:var(--dx-champ)}
.dx--tint{background:var(--dx-tint)}
/* Signature: double hairline frame + concentric circles (business cards, decks) */
.dx__framed{position:relative}
.dx__framed::after{content:"";position:absolute;inset:8px;border:1px solid var(--dx-line);border-radius:calc(var(--dx-r) - 5px);pointer-events:none}
.dx--teal .dx__framed::after,.dx--deep .dx__framed::after,.dx__framed--lt::after{border-color:var(--dx-line-lt)}
.dx__rings{position:absolute;z-index:0;width:560px;height:560px;border-radius:50%;border:1px solid rgba(230,205,150,.22);pointer-events:none}
.dx__rings::before,.dx__rings::after{content:"";position:absolute;border-radius:50%;border:1px solid rgba(230,205,150,.16)}
.dx__rings::before{inset:70px}.dx__rings::after{inset:140px}
/* Buttons */
.dx__btn{display:inline-flex;align-items:center;justify-content:center;gap:10px;min-height:54px;padding:14px 28px;border-radius:999px;border:2px solid var(--dx-teal);background:var(--dx-teal);color:var(--dx-ivory)!important;font:500 1rem/1.2 'Jost',system-ui,sans-serif;letter-spacing:.03em;text-decoration:none!important;cursor:pointer;transition:transform .2s ease,box-shadow .2s ease,background .2s ease;width:100%}
.dx__btn:hover{transform:translateY(-2px);box-shadow:0 14px 30px -14px rgba(1,38,43,.7)}
.dx__btn--gold{background:var(--dx-goldgrad);border-color:transparent;color:var(--dx-teal)!important;font-weight:700}
.dx__btn--gold:hover{box-shadow:0 14px 30px -12px rgba(230,205,150,.55)}
.dx__btn--line{background:transparent;color:var(--dx-teal)!important}
.dx--teal .dx__btn--line,.dx--deep .dx__btn--line{border-color:var(--dx-champ);color:var(--dx-champ)!important}
.dx__btn svg{width:18px;height:18px;flex:none}
.dx__link{color:var(--dx-teal);font-weight:500;text-decoration:underline;text-decoration-color:var(--dx-gold);text-decoration-thickness:2px;text-underline-offset:5px}
.dx--teal .dx__link,.dx--deep .dx__link{color:var(--dx-champ);text-decoration-color:var(--dx-champ)}
.dx a:focus-visible,.dx button:focus-visible,.dx input:focus-visible{outline:3px solid var(--dx-gold);outline-offset:3px}
.dx--teal a:focus-visible,.dx--teal button:focus-visible,.dx--teal input:focus-visible,.dx--deep a:focus-visible,.dx--deep button:focus-visible{outline-color:var(--dx-champ)}
.dx__sr{position:absolute!important;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0);white-space:nowrap}
/* Gentle reveal on scroll (only when the global head script runs) */
.dx-js .dx [data-reveal]{opacity:0;transform:translateY(22px);transition:opacity .7s ease,transform .7s ease}
.dx-js .dx [data-reveal].is-in{opacity:1;transform:none}
@media (min-width:640px){.dx{padding:96px 32px}.dx__btn{width:auto}}
@media (prefers-reduced-motion:reduce){.dx *{transition:none!important;animation:none!important}.dx-js .dx [data-reveal]{opacity:1;transform:none}}
/* ---- Distinct motion kit: flipping words and flip cards ---- */
.dx-rot{display:inline}
.dx-rot__win{display:inline-grid;perspective:700px;vertical-align:bottom}
.dx-rot__w{grid-area:1/1;opacity:0;transform:rotateX(-95deg);transform-origin:50% 100%;transition:transform .75s cubic-bezier(.2,.8,.2,1),opacity .5s ease;white-space:nowrap}
.dx-rot__w.is-on{opacity:1;transform:none}
.dx-rot__w.is-out{opacity:0;transform:rotateX(95deg);transform-origin:50% 0}
.dx__pause{display:inline-flex;align-items:center;gap:8px;min-height:36px;padding:6px 14px;border-radius:999px;border:1px solid currentColor;background:transparent;color:inherit;font:500 .78rem/1 'Jost',system-ui,sans-serif;letter-spacing:.12em;text-transform:uppercase;cursor:pointer;opacity:.85}
.dx__pause:hover{opacity:1}
.dx__pause svg{width:12px;height:12px;fill:currentColor}
/* Flip cards (3D). Without JS both faces simply stack. */
.dx-flips{list-style:none;margin:0;padding:0;display:grid;gap:20px}
.dx-flip{perspective:1400px}
.dx-flip__inner{display:grid}
.dx-flip__face{grid-area:1/1;border-radius:var(--dx-r);overflow:hidden}
.dx-flips.is-live .dx-flip__inner{transition:transform .85s cubic-bezier(.2,.75,.15,1);transform-style:preserve-3d}
.dx-flips.is-live .dx-flip__face{backface-visibility:hidden;-webkit-backface-visibility:hidden}
.dx-flips.is-live .dx-flip__back{transform:rotateY(180deg)}
.dx-flips.is-live .dx-flip.is-flipped .dx-flip__inner{transform:rotateY(180deg)}
.dx-flips:not(.is-live) .dx-flip__face{grid-area:auto}
.dx-flips:not(.is-live) .dx-flip__btn{display:none}
.dx-flips.is-live .dx-flip{cursor:pointer}
.dx-flips.is-live .dx-flip.is-peek .dx-flip__inner{animation:dxPeek 1.4s cubic-bezier(.3,.7,.3,1) .3s 1}
@keyframes dxPeek{0%,100%{transform:none}35%{transform:rotateY(-24deg)}65%{transform:rotateY(8deg)}}
.dx-flip__btn{display:inline-flex;align-items:center;gap:8px;margin-top:auto;padding:10px 0 0;border:0;background:none;color:inherit;font:500 .9rem/1.2 'Jost',system-ui,sans-serif;letter-spacing:.06em;cursor:pointer}
.dx-flip__btn svg{width:18px;height:18px;stroke:currentColor;transition:transform .5s ease}
.dx-flip:hover .dx-flip__front .dx-flip__btn svg{transform:rotate(180deg)}
@media (min-width:640px){.dx-flips--3{grid-template-columns:repeat(3,1fr)}}
@media (max-width:859px) and (min-width:640px){.dx-flips--3{grid-template-columns:1fr 1fr}}
@media (prefers-reduced-motion:reduce){
  .dx-rot__win{display:none}
  .dx-rot .dx__sr{position:static!important;width:auto;height:auto;clip:auto;white-space:normal}
  .dx__pause{display:none}
}
.dx-dead__card{position:relative;display:grid;gap:24px;align-items:center;background:var(--dx-grad);color:var(--dx-mist);border-radius:28px;padding:34px 24px;overflow:hidden;box-shadow:0 0 0 2px var(--dx-gold),0 50px 80px -44px rgba(1,38,43,.85)}
.dx-dead__card::after{content:"";position:absolute;inset:10px;border:1px solid rgba(230,205,150,.3);border-radius:20px;pointer-events:none}
.dx-dead__big{position:relative;display:flex;flex-direction:column;align-items:center;justify-content:center;width:170px;height:170px;border-radius:50%;border:1px solid rgba(230,205,150,.45);box-shadow:inset 0 0 0 14px rgba(230,205,150,.06)}
.dx-dead__big b{font-weight:700;font-size:4.6rem;line-height:.9;letter-spacing:-.04em;background:var(--dx-goldgrad);-webkit-background-clip:text;background-clip:text;color:transparent}
.dx-dead__big span{font-weight:500;font-size:.8rem;letter-spacing:.24em;text-transform:uppercase;color:var(--dx-champ)}
.dx-dead__card h2{color:var(--dx-ivory)!important;font-size:clamp(1.7rem,5.4vw,2.5rem);margin-bottom:14px}
.dx-dead__card h2 em{color:var(--dx-champ)!important}
.dx-dead__card .dx__eyebrow{color:var(--dx-champ)}
.dx-dead__card .dx__eyebrow::before{background:var(--dx-champ)}
.dx-dead__card p{font-size:1.06rem;color:var(--dx-ivory)}
.dx-dead__card p:last-child{margin:0}
.dx-dead__card strong{color:var(--dx-champ)}
@media (min-width:800px){.dx-dead__card{grid-template-columns:auto 1fr;gap:44px;padding:48px 52px}}
</style>
<div class="dx__in">
  <div class="dx-dead__card" role="note" data-reveal>
    <div class="dx-dead__big" aria-hidden="true"><b>60</b><span>days</span></div>
    <div>
      <p class="dx__eyebrow">Important</p>
      <h2 id="dx-dead-title">You have <em>60 days</em> to upload your documents.</h2>
      <p>You have 60 days from your payment date to upload your documents.</p>
      <p>After 60 days, your account goes inactive. To continue, you would pay the consultation fee again at whatever it is that day.</p>
      <p><strong>Your assessment fee is non-refundable.</strong></p>
    </div>
  </div>
</div>
</section>
```

## SECTION 8: What Happens Next (`#what-next`)

**GHL build note:** Section: full width, background #01262B, padding 0. Add a 1-column row, then a **Custom Code** element, and paste the block below. Paste-ready file: `ghl-blocks/08-what-next.html`.

```html
<!-- ===== SECTION 8: WHAT HAPPENS NEXT (#what-next) ===== -->
<section id="what-next" class="dx dx--deep dx-next" tabindex="-1" aria-labelledby="dx-next-title">
<style>
@import url('https://fonts.googleapis.com/css2?family=Jost:ital,wght@0,400;0,500;0,700;1,500;1,700&display=swap');
/* Distinct brand tokens (DTCG Canva designs, Nov 2026). Dark teal leads; gold accents; white for reading areas. */
.dx{--dx-teal:#003b42;--dx-deep:#01262b;--dx-teal-hi:#04333a;--dx-gold:#b18132;--dx-gold-dk:#96691c;--dx-champ:#e6cd96;--dx-champ-hi:#f1e2b8;--dx-ivory:#f3ede1;--dx-mist:#c9d6d2;--dx-body:#3b4f52;--dx-white:#ffffff;--dx-tint:#f2f6f6;
  --dx-grad:linear-gradient(135deg,#04333a 0%,#003b42 45%,#01262b 100%);
  --dx-goldgrad:linear-gradient(135deg,#f1e2b8 0%,#e6cd96 55%,#d9b878 100%);
  --dx-line:rgba(177,129,50,.35);--dx-line-lt:rgba(230,205,150,.35);--dx-r:20px;--dx-r-sm:14px;
  position:relative;display:block;box-sizing:border-box;overflow:hidden;font-family:'Jost',system-ui,-apple-system,'Segoe UI',sans-serif;font-weight:400;font-size:17px;line-height:1.6;color:var(--dx-body);background:var(--dx-white);padding:64px 20px;scroll-margin-top:12px;-webkit-font-smoothing:antialiased}
.dx *,.dx *::before,.dx *::after{box-sizing:border-box}
.dx:focus{outline:none}
.dx__in{position:relative;z-index:1;max-width:1040px;margin:0 auto}
:where(.dx) h1,:where(.dx) h2,:where(.dx) h3{font-family:inherit;font-weight:700;color:var(--dx-teal);margin:0;letter-spacing:-.015em}
:where(.dx) h2{font-size:clamp(1.9rem,6.2vw,3rem);line-height:1.08;margin-bottom:16px}
:where(.dx) h3{font-size:1.22rem;line-height:1.3;margin-bottom:6px}
:where(.dx) p{margin:0 0 14px}
:where(.dx) strong{color:var(--dx-teal)}
:where(.dx) h1 em,:where(.dx) h2 em{font-style:italic;font-weight:700;color:var(--dx-gold)}
.dx__eyebrow{display:flex;align-items:center;gap:12px;margin:0 0 14px;font-weight:500;font-size:.78rem;letter-spacing:.2em;text-transform:uppercase;color:var(--dx-gold-dk)}
.dx__eyebrow::before{content:"";flex:0 0 44px;height:2px;border-radius:2px;background:var(--dx-gold)}
.dx__sub{font-weight:400;font-size:1.1rem;max-width:640px}
/* Teal sections: the brand's lead surface */
.dx--teal{background:var(--dx-grad);color:var(--dx-mist)}
.dx--deep{background:var(--dx-deep);color:var(--dx-mist)}
.dx--teal h1,.dx--teal h2,.dx--teal h3,.dx--teal strong,.dx--deep h1,.dx--deep h2,.dx--deep h3,.dx--deep strong{color:var(--dx-ivory)}
.dx--teal h1 em,.dx--teal h2 em,.dx--deep h1 em,.dx--deep h2 em{color:var(--dx-champ)}
.dx--teal .dx__eyebrow,.dx--deep .dx__eyebrow{color:var(--dx-champ)}
.dx--teal .dx__eyebrow::before,.dx--deep .dx__eyebrow::before{background:var(--dx-champ)}
.dx--tint{background:var(--dx-tint)}
/* Signature: double hairline frame + concentric circles (business cards, decks) */
.dx__framed{position:relative}
.dx__framed::after{content:"";position:absolute;inset:8px;border:1px solid var(--dx-line);border-radius:calc(var(--dx-r) - 5px);pointer-events:none}
.dx--teal .dx__framed::after,.dx--deep .dx__framed::after,.dx__framed--lt::after{border-color:var(--dx-line-lt)}
.dx__rings{position:absolute;z-index:0;width:560px;height:560px;border-radius:50%;border:1px solid rgba(230,205,150,.22);pointer-events:none}
.dx__rings::before,.dx__rings::after{content:"";position:absolute;border-radius:50%;border:1px solid rgba(230,205,150,.16)}
.dx__rings::before{inset:70px}.dx__rings::after{inset:140px}
/* Buttons */
.dx__btn{display:inline-flex;align-items:center;justify-content:center;gap:10px;min-height:54px;padding:14px 28px;border-radius:999px;border:2px solid var(--dx-teal);background:var(--dx-teal);color:var(--dx-ivory)!important;font:500 1rem/1.2 'Jost',system-ui,sans-serif;letter-spacing:.03em;text-decoration:none!important;cursor:pointer;transition:transform .2s ease,box-shadow .2s ease,background .2s ease;width:100%}
.dx__btn:hover{transform:translateY(-2px);box-shadow:0 14px 30px -14px rgba(1,38,43,.7)}
.dx__btn--gold{background:var(--dx-goldgrad);border-color:transparent;color:var(--dx-teal)!important;font-weight:700}
.dx__btn--gold:hover{box-shadow:0 14px 30px -12px rgba(230,205,150,.55)}
.dx__btn--line{background:transparent;color:var(--dx-teal)!important}
.dx--teal .dx__btn--line,.dx--deep .dx__btn--line{border-color:var(--dx-champ);color:var(--dx-champ)!important}
.dx__btn svg{width:18px;height:18px;flex:none}
.dx__link{color:var(--dx-teal);font-weight:500;text-decoration:underline;text-decoration-color:var(--dx-gold);text-decoration-thickness:2px;text-underline-offset:5px}
.dx--teal .dx__link,.dx--deep .dx__link{color:var(--dx-champ);text-decoration-color:var(--dx-champ)}
.dx a:focus-visible,.dx button:focus-visible,.dx input:focus-visible{outline:3px solid var(--dx-gold);outline-offset:3px}
.dx--teal a:focus-visible,.dx--teal button:focus-visible,.dx--teal input:focus-visible,.dx--deep a:focus-visible,.dx--deep button:focus-visible{outline-color:var(--dx-champ)}
.dx__sr{position:absolute!important;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0);white-space:nowrap}
/* Gentle reveal on scroll (only when the global head script runs) */
.dx-js .dx [data-reveal]{opacity:0;transform:translateY(22px);transition:opacity .7s ease,transform .7s ease}
.dx-js .dx [data-reveal].is-in{opacity:1;transform:none}
@media (min-width:640px){.dx{padding:96px 32px}.dx__btn{width:auto}}
@media (prefers-reduced-motion:reduce){.dx *{transition:none!important;animation:none!important}.dx-js .dx [data-reveal]{opacity:1;transform:none}}
/* ---- Distinct motion kit: flipping words and flip cards ---- */
.dx-rot{display:inline}
.dx-rot__win{display:inline-grid;perspective:700px;vertical-align:bottom}
.dx-rot__w{grid-area:1/1;opacity:0;transform:rotateX(-95deg);transform-origin:50% 100%;transition:transform .75s cubic-bezier(.2,.8,.2,1),opacity .5s ease;white-space:nowrap}
.dx-rot__w.is-on{opacity:1;transform:none}
.dx-rot__w.is-out{opacity:0;transform:rotateX(95deg);transform-origin:50% 0}
.dx__pause{display:inline-flex;align-items:center;gap:8px;min-height:36px;padding:6px 14px;border-radius:999px;border:1px solid currentColor;background:transparent;color:inherit;font:500 .78rem/1 'Jost',system-ui,sans-serif;letter-spacing:.12em;text-transform:uppercase;cursor:pointer;opacity:.85}
.dx__pause:hover{opacity:1}
.dx__pause svg{width:12px;height:12px;fill:currentColor}
/* Flip cards (3D). Without JS both faces simply stack. */
.dx-flips{list-style:none;margin:0;padding:0;display:grid;gap:20px}
.dx-flip{perspective:1400px}
.dx-flip__inner{display:grid}
.dx-flip__face{grid-area:1/1;border-radius:var(--dx-r);overflow:hidden}
.dx-flips.is-live .dx-flip__inner{transition:transform .85s cubic-bezier(.2,.75,.15,1);transform-style:preserve-3d}
.dx-flips.is-live .dx-flip__face{backface-visibility:hidden;-webkit-backface-visibility:hidden}
.dx-flips.is-live .dx-flip__back{transform:rotateY(180deg)}
.dx-flips.is-live .dx-flip.is-flipped .dx-flip__inner{transform:rotateY(180deg)}
.dx-flips:not(.is-live) .dx-flip__face{grid-area:auto}
.dx-flips:not(.is-live) .dx-flip__btn{display:none}
.dx-flips.is-live .dx-flip{cursor:pointer}
.dx-flips.is-live .dx-flip.is-peek .dx-flip__inner{animation:dxPeek 1.4s cubic-bezier(.3,.7,.3,1) .3s 1}
@keyframes dxPeek{0%,100%{transform:none}35%{transform:rotateY(-24deg)}65%{transform:rotateY(8deg)}}
.dx-flip__btn{display:inline-flex;align-items:center;gap:8px;margin-top:auto;padding:10px 0 0;border:0;background:none;color:inherit;font:500 .9rem/1.2 'Jost',system-ui,sans-serif;letter-spacing:.06em;cursor:pointer}
.dx-flip__btn svg{width:18px;height:18px;stroke:currentColor;transition:transform .5s ease}
.dx-flip:hover .dx-flip__front .dx-flip__btn svg{transform:rotate(180deg)}
@media (min-width:640px){.dx-flips--3{grid-template-columns:repeat(3,1fr)}}
@media (max-width:859px) and (min-width:640px){.dx-flips--3{grid-template-columns:1fr 1fr}}
@media (prefers-reduced-motion:reduce){
  .dx-rot__win{display:none}
  .dx-rot .dx__sr{position:static!important;width:auto;height:auto;clip:auto;white-space:normal}
  .dx__pause{display:none}
}
.dx-next .dx__rings{left:-300px;top:-200px}
.dx-next__line{list-style:none;margin:36px 0 0;padding:0;display:grid}
.dx-next__line li{position:relative;padding:0 0 34px 66px}
.dx-next__line li:last-child{padding-bottom:0}
.dx-next__line li::before{content:"";position:absolute;left:23px;top:52px;bottom:6px;width:2px;background:linear-gradient(var(--dx-champ),rgba(230,205,150,.15))}
.dx-next__line li:last-child::before{display:none}
.dx-next__dot{position:absolute;left:0;top:0;width:48px;height:48px;border-radius:50%;background:var(--dx-goldgrad);display:grid;place-items:center;font-weight:700;font-size:1.1rem;color:var(--dx-teal);box-shadow:0 0 0 6px rgba(230,205,150,.12)}
.dx-next__line h3{padding-top:8px;color:var(--dx-ivory)!important}
.dx-next__line p{margin:0}
.dx-next__close{margin-top:48px!important;padding-top:28px;border-top:1px solid rgba(230,205,150,.25);font-weight:500;font-size:clamp(1.2rem,4vw,1.6rem);line-height:1.35;color:var(--dx-ivory)}
.dx-next__close em{font-style:italic;color:var(--dx-champ)}
@media (min-width:880px){
  .dx-next__line{grid-template-columns:repeat(3,1fr);gap:28px}
  .dx-next__line li{padding:72px 0 0 0}
  .dx-next__line li::before{left:60px;right:-28px;top:23px;bottom:auto;width:auto;height:2px}
}
</style>
<div class="dx__rings" aria-hidden="true"></div>
<div class="dx__in">
  <div data-reveal>
    <p class="dx__eyebrow">After you submit · Peace of mind</p>
    <h2 id="dx-next-title">What happens <em>next.</em></h2>
  </div>
  <ol class="dx-next__line">
    <li data-reveal><span class="dx-next__dot" aria-hidden="true">1</span><h3>Our team reviews your documents</h3><p>Once you submit, our team reviews everything you've uploaded.</p></li>
    <li data-reveal><span class="dx-next__dot" aria-hidden="true">2</span><h3>We'll tell you if anything is missing</h3><p>If anything is missing, we'll let you know.</p></li>
    <li data-reveal><span class="dx-next__dot" aria-hidden="true">3</span><h3>You book your assessment call</h3><p>Once everything is ready, we'll email you a private link to book your assessment call.</p></li>
  </ol>
  <p class="dx-next__close" data-reveal>That's the Distinct® Experience: <em>highly valued, financially redefined, peace of mind obtained.</em></p>
</div>
</section>
```

## SECTION 9: Security (`#security`)

**GHL build note:** Section: full width, background #FFFFFF, padding 0. This block repeats the [TAXDOME PORTAL LINK] button. Add a 1-column row, then a **Custom Code** element, and paste the block below. Paste-ready file: `ghl-blocks/09-security.html`.

```html
<!-- ===== SECTION 9: SECURITY (#security) ===== -->
<section id="security" class="dx dx-sec" tabindex="-1" aria-labelledby="dx-sec-title">
<style>
@import url('https://fonts.googleapis.com/css2?family=Jost:ital,wght@0,400;0,500;0,700;1,500;1,700&display=swap');
/* Distinct brand tokens (DTCG Canva designs, Nov 2026). Dark teal leads; gold accents; white for reading areas. */
.dx{--dx-teal:#003b42;--dx-deep:#01262b;--dx-teal-hi:#04333a;--dx-gold:#b18132;--dx-gold-dk:#96691c;--dx-champ:#e6cd96;--dx-champ-hi:#f1e2b8;--dx-ivory:#f3ede1;--dx-mist:#c9d6d2;--dx-body:#3b4f52;--dx-white:#ffffff;--dx-tint:#f2f6f6;
  --dx-grad:linear-gradient(135deg,#04333a 0%,#003b42 45%,#01262b 100%);
  --dx-goldgrad:linear-gradient(135deg,#f1e2b8 0%,#e6cd96 55%,#d9b878 100%);
  --dx-line:rgba(177,129,50,.35);--dx-line-lt:rgba(230,205,150,.35);--dx-r:20px;--dx-r-sm:14px;
  position:relative;display:block;box-sizing:border-box;overflow:hidden;font-family:'Jost',system-ui,-apple-system,'Segoe UI',sans-serif;font-weight:400;font-size:17px;line-height:1.6;color:var(--dx-body);background:var(--dx-white);padding:64px 20px;scroll-margin-top:12px;-webkit-font-smoothing:antialiased}
.dx *,.dx *::before,.dx *::after{box-sizing:border-box}
.dx:focus{outline:none}
.dx__in{position:relative;z-index:1;max-width:1040px;margin:0 auto}
:where(.dx) h1,:where(.dx) h2,:where(.dx) h3{font-family:inherit;font-weight:700;color:var(--dx-teal);margin:0;letter-spacing:-.015em}
:where(.dx) h2{font-size:clamp(1.9rem,6.2vw,3rem);line-height:1.08;margin-bottom:16px}
:where(.dx) h3{font-size:1.22rem;line-height:1.3;margin-bottom:6px}
:where(.dx) p{margin:0 0 14px}
:where(.dx) strong{color:var(--dx-teal)}
:where(.dx) h1 em,:where(.dx) h2 em{font-style:italic;font-weight:700;color:var(--dx-gold)}
.dx__eyebrow{display:flex;align-items:center;gap:12px;margin:0 0 14px;font-weight:500;font-size:.78rem;letter-spacing:.2em;text-transform:uppercase;color:var(--dx-gold-dk)}
.dx__eyebrow::before{content:"";flex:0 0 44px;height:2px;border-radius:2px;background:var(--dx-gold)}
.dx__sub{font-weight:400;font-size:1.1rem;max-width:640px}
/* Teal sections: the brand's lead surface */
.dx--teal{background:var(--dx-grad);color:var(--dx-mist)}
.dx--deep{background:var(--dx-deep);color:var(--dx-mist)}
.dx--teal h1,.dx--teal h2,.dx--teal h3,.dx--teal strong,.dx--deep h1,.dx--deep h2,.dx--deep h3,.dx--deep strong{color:var(--dx-ivory)}
.dx--teal h1 em,.dx--teal h2 em,.dx--deep h1 em,.dx--deep h2 em{color:var(--dx-champ)}
.dx--teal .dx__eyebrow,.dx--deep .dx__eyebrow{color:var(--dx-champ)}
.dx--teal .dx__eyebrow::before,.dx--deep .dx__eyebrow::before{background:var(--dx-champ)}
.dx--tint{background:var(--dx-tint)}
/* Signature: double hairline frame + concentric circles (business cards, decks) */
.dx__framed{position:relative}
.dx__framed::after{content:"";position:absolute;inset:8px;border:1px solid var(--dx-line);border-radius:calc(var(--dx-r) - 5px);pointer-events:none}
.dx--teal .dx__framed::after,.dx--deep .dx__framed::after,.dx__framed--lt::after{border-color:var(--dx-line-lt)}
.dx__rings{position:absolute;z-index:0;width:560px;height:560px;border-radius:50%;border:1px solid rgba(230,205,150,.22);pointer-events:none}
.dx__rings::before,.dx__rings::after{content:"";position:absolute;border-radius:50%;border:1px solid rgba(230,205,150,.16)}
.dx__rings::before{inset:70px}.dx__rings::after{inset:140px}
/* Buttons */
.dx__btn{display:inline-flex;align-items:center;justify-content:center;gap:10px;min-height:54px;padding:14px 28px;border-radius:999px;border:2px solid var(--dx-teal);background:var(--dx-teal);color:var(--dx-ivory)!important;font:500 1rem/1.2 'Jost',system-ui,sans-serif;letter-spacing:.03em;text-decoration:none!important;cursor:pointer;transition:transform .2s ease,box-shadow .2s ease,background .2s ease;width:100%}
.dx__btn:hover{transform:translateY(-2px);box-shadow:0 14px 30px -14px rgba(1,38,43,.7)}
.dx__btn--gold{background:var(--dx-goldgrad);border-color:transparent;color:var(--dx-teal)!important;font-weight:700}
.dx__btn--gold:hover{box-shadow:0 14px 30px -12px rgba(230,205,150,.55)}
.dx__btn--line{background:transparent;color:var(--dx-teal)!important}
.dx--teal .dx__btn--line,.dx--deep .dx__btn--line{border-color:var(--dx-champ);color:var(--dx-champ)!important}
.dx__btn svg{width:18px;height:18px;flex:none}
.dx__link{color:var(--dx-teal);font-weight:500;text-decoration:underline;text-decoration-color:var(--dx-gold);text-decoration-thickness:2px;text-underline-offset:5px}
.dx--teal .dx__link,.dx--deep .dx__link{color:var(--dx-champ);text-decoration-color:var(--dx-champ)}
.dx a:focus-visible,.dx button:focus-visible,.dx input:focus-visible{outline:3px solid var(--dx-gold);outline-offset:3px}
.dx--teal a:focus-visible,.dx--teal button:focus-visible,.dx--teal input:focus-visible,.dx--deep a:focus-visible,.dx--deep button:focus-visible{outline-color:var(--dx-champ)}
.dx__sr{position:absolute!important;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0);white-space:nowrap}
/* Gentle reveal on scroll (only when the global head script runs) */
.dx-js .dx [data-reveal]{opacity:0;transform:translateY(22px);transition:opacity .7s ease,transform .7s ease}
.dx-js .dx [data-reveal].is-in{opacity:1;transform:none}
@media (min-width:640px){.dx{padding:96px 32px}.dx__btn{width:auto}}
@media (prefers-reduced-motion:reduce){.dx *{transition:none!important;animation:none!important}.dx-js .dx [data-reveal]{opacity:1;transform:none}}
/* ---- Distinct motion kit: flipping words and flip cards ---- */
.dx-rot{display:inline}
.dx-rot__win{display:inline-grid;perspective:700px;vertical-align:bottom}
.dx-rot__w{grid-area:1/1;opacity:0;transform:rotateX(-95deg);transform-origin:50% 100%;transition:transform .75s cubic-bezier(.2,.8,.2,1),opacity .5s ease;white-space:nowrap}
.dx-rot__w.is-on{opacity:1;transform:none}
.dx-rot__w.is-out{opacity:0;transform:rotateX(95deg);transform-origin:50% 0}
.dx__pause{display:inline-flex;align-items:center;gap:8px;min-height:36px;padding:6px 14px;border-radius:999px;border:1px solid currentColor;background:transparent;color:inherit;font:500 .78rem/1 'Jost',system-ui,sans-serif;letter-spacing:.12em;text-transform:uppercase;cursor:pointer;opacity:.85}
.dx__pause:hover{opacity:1}
.dx__pause svg{width:12px;height:12px;fill:currentColor}
/* Flip cards (3D). Without JS both faces simply stack. */
.dx-flips{list-style:none;margin:0;padding:0;display:grid;gap:20px}
.dx-flip{perspective:1400px}
.dx-flip__inner{display:grid}
.dx-flip__face{grid-area:1/1;border-radius:var(--dx-r);overflow:hidden}
.dx-flips.is-live .dx-flip__inner{transition:transform .85s cubic-bezier(.2,.75,.15,1);transform-style:preserve-3d}
.dx-flips.is-live .dx-flip__face{backface-visibility:hidden;-webkit-backface-visibility:hidden}
.dx-flips.is-live .dx-flip__back{transform:rotateY(180deg)}
.dx-flips.is-live .dx-flip.is-flipped .dx-flip__inner{transform:rotateY(180deg)}
.dx-flips:not(.is-live) .dx-flip__face{grid-area:auto}
.dx-flips:not(.is-live) .dx-flip__btn{display:none}
.dx-flips.is-live .dx-flip{cursor:pointer}
.dx-flips.is-live .dx-flip.is-peek .dx-flip__inner{animation:dxPeek 1.4s cubic-bezier(.3,.7,.3,1) .3s 1}
@keyframes dxPeek{0%,100%{transform:none}35%{transform:rotateY(-24deg)}65%{transform:rotateY(8deg)}}
.dx-flip__btn{display:inline-flex;align-items:center;gap:8px;margin-top:auto;padding:10px 0 0;border:0;background:none;color:inherit;font:500 .9rem/1.2 'Jost',system-ui,sans-serif;letter-spacing:.06em;cursor:pointer}
.dx-flip__btn svg{width:18px;height:18px;stroke:currentColor;transition:transform .5s ease}
.dx-flip:hover .dx-flip__front .dx-flip__btn svg{transform:rotate(180deg)}
@media (min-width:640px){.dx-flips--3{grid-template-columns:repeat(3,1fr)}}
@media (max-width:859px) and (min-width:640px){.dx-flips--3{grid-template-columns:1fr 1fr}}
@media (prefers-reduced-motion:reduce){
  .dx-rot__win{display:none}
  .dx-rot .dx__sr{position:static!important;width:auto;height:auto;clip:auto;white-space:normal}
  .dx__pause{display:none}
}
.dx-sec__card{display:grid;gap:20px;align-items:center;padding:30px 24px;border-radius:24px;background:var(--dx-white);border:2px solid var(--dx-teal);box-shadow:0 30px 60px -44px rgba(1,38,43,.8)}
.dx-sec__icon{width:72px;height:72px;border-radius:50%;background:var(--dx-grad);display:grid;place-items:center;box-shadow:0 0 0 6px rgba(0,59,66,.08)}
.dx-sec__icon svg{width:32px;height:32px;stroke:var(--dx-champ)}
.dx-sec__card h2{font-size:clamp(1.6rem,5vw,2.2rem);margin-bottom:8px}
.dx-sec__card p{font-size:1.08rem;margin:0}
.dx-sec__app{margin-top:8px!important;font-size:.95rem!important;color:var(--dx-gold-dk);font-weight:500}
@media (min-width:800px){.dx-sec__card{grid-template-columns:auto 1fr auto;gap:30px;padding:36px 40px}}
</style>
<div class="dx__in">
  <div class="dx-sec__card" data-reveal>
    <div class="dx-sec__icon" aria-hidden="true">
      <svg viewBox="0 0 24 24" fill="none" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><rect x="4" y="10" width="16" height="11" rx="3"/><path d="M8 10V7a4 4 0 0 1 8 0v3"/></svg>
    </div>
    <div>
      <h2 id="dx-sec-title">Keep your documents <em>secure.</em></h2>
      <p>For your security, upload tax documents only in TaxDome. Never send them by regular email or text.</p>
      <p class="dx-sec__app">The TaxDome Client Portal app adds PIN, facial recognition and 2-step authentication.</p>
    </div>
    <a class="dx__btn" href="[TAXDOME PORTAL LINK]" target="_blank" rel="noopener">Log in to TaxDome<span class="dx__sr">(opens in a new tab)</span></a>
  </div>
</div>
</section>
```

## SECTION 10: Footer (`#footer`)

**GHL build note:** Section: full width, background #01262B, padding 0. Turn off GHL's default footer, if your funnel has one, to avoid two footers. Add a 1-column row, then a **Custom Code** element, and paste the block below. Paste-ready file: `ghl-blocks/10-footer.html`.

```html
<!-- ===== SECTION 10: FOOTER (#footer) ===== -->
<footer id="footer" class="dx dx--deep dx-foot" tabindex="-1" aria-label="Distinct Tax Consulting Group® contact information">
<style>
@import url('https://fonts.googleapis.com/css2?family=Jost:ital,wght@0,400;0,500;0,700;1,500;1,700&display=swap');
/* Distinct brand tokens (DTCG Canva designs, Nov 2026). Dark teal leads; gold accents; white for reading areas. */
.dx{--dx-teal:#003b42;--dx-deep:#01262b;--dx-teal-hi:#04333a;--dx-gold:#b18132;--dx-gold-dk:#96691c;--dx-champ:#e6cd96;--dx-champ-hi:#f1e2b8;--dx-ivory:#f3ede1;--dx-mist:#c9d6d2;--dx-body:#3b4f52;--dx-white:#ffffff;--dx-tint:#f2f6f6;
  --dx-grad:linear-gradient(135deg,#04333a 0%,#003b42 45%,#01262b 100%);
  --dx-goldgrad:linear-gradient(135deg,#f1e2b8 0%,#e6cd96 55%,#d9b878 100%);
  --dx-line:rgba(177,129,50,.35);--dx-line-lt:rgba(230,205,150,.35);--dx-r:20px;--dx-r-sm:14px;
  position:relative;display:block;box-sizing:border-box;overflow:hidden;font-family:'Jost',system-ui,-apple-system,'Segoe UI',sans-serif;font-weight:400;font-size:17px;line-height:1.6;color:var(--dx-body);background:var(--dx-white);padding:64px 20px;scroll-margin-top:12px;-webkit-font-smoothing:antialiased}
.dx *,.dx *::before,.dx *::after{box-sizing:border-box}
.dx:focus{outline:none}
.dx__in{position:relative;z-index:1;max-width:1040px;margin:0 auto}
:where(.dx) h1,:where(.dx) h2,:where(.dx) h3{font-family:inherit;font-weight:700;color:var(--dx-teal);margin:0;letter-spacing:-.015em}
:where(.dx) h2{font-size:clamp(1.9rem,6.2vw,3rem);line-height:1.08;margin-bottom:16px}
:where(.dx) h3{font-size:1.22rem;line-height:1.3;margin-bottom:6px}
:where(.dx) p{margin:0 0 14px}
:where(.dx) strong{color:var(--dx-teal)}
:where(.dx) h1 em,:where(.dx) h2 em{font-style:italic;font-weight:700;color:var(--dx-gold)}
.dx__eyebrow{display:flex;align-items:center;gap:12px;margin:0 0 14px;font-weight:500;font-size:.78rem;letter-spacing:.2em;text-transform:uppercase;color:var(--dx-gold-dk)}
.dx__eyebrow::before{content:"";flex:0 0 44px;height:2px;border-radius:2px;background:var(--dx-gold)}
.dx__sub{font-weight:400;font-size:1.1rem;max-width:640px}
/* Teal sections: the brand's lead surface */
.dx--teal{background:var(--dx-grad);color:var(--dx-mist)}
.dx--deep{background:var(--dx-deep);color:var(--dx-mist)}
.dx--teal h1,.dx--teal h2,.dx--teal h3,.dx--teal strong,.dx--deep h1,.dx--deep h2,.dx--deep h3,.dx--deep strong{color:var(--dx-ivory)}
.dx--teal h1 em,.dx--teal h2 em,.dx--deep h1 em,.dx--deep h2 em{color:var(--dx-champ)}
.dx--teal .dx__eyebrow,.dx--deep .dx__eyebrow{color:var(--dx-champ)}
.dx--teal .dx__eyebrow::before,.dx--deep .dx__eyebrow::before{background:var(--dx-champ)}
.dx--tint{background:var(--dx-tint)}
/* Signature: double hairline frame + concentric circles (business cards, decks) */
.dx__framed{position:relative}
.dx__framed::after{content:"";position:absolute;inset:8px;border:1px solid var(--dx-line);border-radius:calc(var(--dx-r) - 5px);pointer-events:none}
.dx--teal .dx__framed::after,.dx--deep .dx__framed::after,.dx__framed--lt::after{border-color:var(--dx-line-lt)}
.dx__rings{position:absolute;z-index:0;width:560px;height:560px;border-radius:50%;border:1px solid rgba(230,205,150,.22);pointer-events:none}
.dx__rings::before,.dx__rings::after{content:"";position:absolute;border-radius:50%;border:1px solid rgba(230,205,150,.16)}
.dx__rings::before{inset:70px}.dx__rings::after{inset:140px}
/* Buttons */
.dx__btn{display:inline-flex;align-items:center;justify-content:center;gap:10px;min-height:54px;padding:14px 28px;border-radius:999px;border:2px solid var(--dx-teal);background:var(--dx-teal);color:var(--dx-ivory)!important;font:500 1rem/1.2 'Jost',system-ui,sans-serif;letter-spacing:.03em;text-decoration:none!important;cursor:pointer;transition:transform .2s ease,box-shadow .2s ease,background .2s ease;width:100%}
.dx__btn:hover{transform:translateY(-2px);box-shadow:0 14px 30px -14px rgba(1,38,43,.7)}
.dx__btn--gold{background:var(--dx-goldgrad);border-color:transparent;color:var(--dx-teal)!important;font-weight:700}
.dx__btn--gold:hover{box-shadow:0 14px 30px -12px rgba(230,205,150,.55)}
.dx__btn--line{background:transparent;color:var(--dx-teal)!important}
.dx--teal .dx__btn--line,.dx--deep .dx__btn--line{border-color:var(--dx-champ);color:var(--dx-champ)!important}
.dx__btn svg{width:18px;height:18px;flex:none}
.dx__link{color:var(--dx-teal);font-weight:500;text-decoration:underline;text-decoration-color:var(--dx-gold);text-decoration-thickness:2px;text-underline-offset:5px}
.dx--teal .dx__link,.dx--deep .dx__link{color:var(--dx-champ);text-decoration-color:var(--dx-champ)}
.dx a:focus-visible,.dx button:focus-visible,.dx input:focus-visible{outline:3px solid var(--dx-gold);outline-offset:3px}
.dx--teal a:focus-visible,.dx--teal button:focus-visible,.dx--teal input:focus-visible,.dx--deep a:focus-visible,.dx--deep button:focus-visible{outline-color:var(--dx-champ)}
.dx__sr{position:absolute!important;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0);white-space:nowrap}
/* Gentle reveal on scroll (only when the global head script runs) */
.dx-js .dx [data-reveal]{opacity:0;transform:translateY(22px);transition:opacity .7s ease,transform .7s ease}
.dx-js .dx [data-reveal].is-in{opacity:1;transform:none}
@media (min-width:640px){.dx{padding:96px 32px}.dx__btn{width:auto}}
@media (prefers-reduced-motion:reduce){.dx *{transition:none!important;animation:none!important}.dx-js .dx [data-reveal]{opacity:1;transform:none}}
/* ---- Distinct motion kit: flipping words and flip cards ---- */
.dx-rot{display:inline}
.dx-rot__win{display:inline-grid;perspective:700px;vertical-align:bottom}
.dx-rot__w{grid-area:1/1;opacity:0;transform:rotateX(-95deg);transform-origin:50% 100%;transition:transform .75s cubic-bezier(.2,.8,.2,1),opacity .5s ease;white-space:nowrap}
.dx-rot__w.is-on{opacity:1;transform:none}
.dx-rot__w.is-out{opacity:0;transform:rotateX(95deg);transform-origin:50% 0}
.dx__pause{display:inline-flex;align-items:center;gap:8px;min-height:36px;padding:6px 14px;border-radius:999px;border:1px solid currentColor;background:transparent;color:inherit;font:500 .78rem/1 'Jost',system-ui,sans-serif;letter-spacing:.12em;text-transform:uppercase;cursor:pointer;opacity:.85}
.dx__pause:hover{opacity:1}
.dx__pause svg{width:12px;height:12px;fill:currentColor}
/* Flip cards (3D). Without JS both faces simply stack. */
.dx-flips{list-style:none;margin:0;padding:0;display:grid;gap:20px}
.dx-flip{perspective:1400px}
.dx-flip__inner{display:grid}
.dx-flip__face{grid-area:1/1;border-radius:var(--dx-r);overflow:hidden}
.dx-flips.is-live .dx-flip__inner{transition:transform .85s cubic-bezier(.2,.75,.15,1);transform-style:preserve-3d}
.dx-flips.is-live .dx-flip__face{backface-visibility:hidden;-webkit-backface-visibility:hidden}
.dx-flips.is-live .dx-flip__back{transform:rotateY(180deg)}
.dx-flips.is-live .dx-flip.is-flipped .dx-flip__inner{transform:rotateY(180deg)}
.dx-flips:not(.is-live) .dx-flip__face{grid-area:auto}
.dx-flips:not(.is-live) .dx-flip__btn{display:none}
.dx-flips.is-live .dx-flip{cursor:pointer}
.dx-flips.is-live .dx-flip.is-peek .dx-flip__inner{animation:dxPeek 1.4s cubic-bezier(.3,.7,.3,1) .3s 1}
@keyframes dxPeek{0%,100%{transform:none}35%{transform:rotateY(-24deg)}65%{transform:rotateY(8deg)}}
.dx-flip__btn{display:inline-flex;align-items:center;gap:8px;margin-top:auto;padding:10px 0 0;border:0;background:none;color:inherit;font:500 .9rem/1.2 'Jost',system-ui,sans-serif;letter-spacing:.06em;cursor:pointer}
.dx-flip__btn svg{width:18px;height:18px;stroke:currentColor;transition:transform .5s ease}
.dx-flip:hover .dx-flip__front .dx-flip__btn svg{transform:rotate(180deg)}
@media (min-width:640px){.dx-flips--3{grid-template-columns:repeat(3,1fr)}}
@media (max-width:859px) and (min-width:640px){.dx-flips--3{grid-template-columns:1fr 1fr}}
@media (prefers-reduced-motion:reduce){
  .dx-rot__win{display:none}
  .dx-rot .dx__sr{position:static!important;width:auto;height:auto;clip:auto;white-space:normal}
  .dx__pause{display:none}
}
.dx-foot{padding-bottom:44px;border-top:2px solid var(--dx-gold)}
.dx-foot .dx__rings{right:-300px;top:-260px}
.dx-foot__grid{display:grid;gap:36px}
.dx-foot__hand{display:block;font-weight:500;font-style:italic;font-size:clamp(1.9rem,6vw,2.6rem);line-height:1.1;color:var(--dx-champ);margin-bottom:14px}
.dx-foot__sign strong{display:block;font-weight:700;font-size:1.1rem}
.dx-foot__sign span{display:block}
.dx-foot__tag{margin-top:22px!important;font-weight:500;letter-spacing:.14em;text-transform:uppercase;font-size:.8rem;color:var(--dx-champ)}
.dx-foot__firm{font-weight:700;font-size:1.15rem;color:var(--dx-ivory);margin-bottom:10px!important}
.dx-foot address{font-style:normal;margin-bottom:16px}
.dx-foot__bottom{display:flex;flex-wrap:wrap;justify-content:space-between;gap:12px;margin-top:44px;padding-top:20px;border-top:1px solid rgba(230,205,150,.25);font-size:.85rem}
.dx-foot__bottom p{margin:0}
.dx-foot__legal{font-weight:500;font-size:.72rem;letter-spacing:.16em;text-transform:uppercase}
@media (min-width:780px){.dx-foot__grid{grid-template-columns:1.2fr 1fr;gap:60px;align-items:end}}
</style>
<div class="dx__rings" aria-hidden="true"></div>
<div class="dx__in">
  <div class="dx-foot__grid">
    <div class="dx-foot__sign">
      <span class="dx-foot__hand">Have a distinct day,</span>
      <strong>Alysha Pruitt Harvey, MAcc, EA</strong>
      <span>Founder and Managing Partner</span>
      <p class="dx-foot__tag">Protect More. Keep More. Build More.</p>
    </div>
    <div>
      <p class="dx-foot__firm">Distinct Tax Consulting Group®</p>
      <address>4751 Best Road, Suite 332<br>Atlanta, GA 30337</address>
      <p><strong>Questions?</strong> Reply to any of our emails.</p>
      <p><a class="dx__link" href="https://www.distincttax.com" target="_blank" rel="noopener">www.distincttax.com<span class="dx__sr"> (opens in a new tab)</span></a></p>
    </div>
  </div>
  <div class="dx-foot__bottom">
    <p class="dx-foot__legal">© <span data-dx-year>2026</span> Distinct Tax Consulting Group® · All rights reserved</p>
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

**Logo candidates in Canva.** No variant could be confirmed free of the gold "I" at preview size, so please check before you export:
- The teal knot with a white "DISTINCT" wordmark, stacked over "Distinct Tax Consulting Group", in *DTCG Brand - Letterhead (Doc) - MASTER*. This is the best fit for a light page.
- The white "DISTINCT" wordmark on a dark band, on page 1 of *DTCG Brand - Business Cards (Print) - 2026*. Use this one only on a dark background.

Image mock-ups work best at a 4:3 ratio, about 1200 × 900 px. Make sure no real client data is visible.

## Please confirm before launch: your Canva designs differ from this brief

The page follows your brief's wording. The designs from Nov 5 onward disagree with it, or don't cover it, in these places:

| # | Topic | Brief / page says | Your Canva designs say | Source |
|---|---|---|---|---|
| 1 | Name of the $500 offer | Distinct® Tax Assessment | "Tax Strategy Consultation", $500, or **$250 for real estate professionals** (slide marked IN PROGRESS). The onboarding decks call step 1 the "Distinct Tax and CFO Sales Assessment Call". | Systems Update deck p136; Client Onboarding Master Deck p2 |
| 2 | Booking order | Pay → upload → review → private booking link by email | "The price is built into the calendar". That reads as paying when booking in GHL. The decks also book calls through portal or newsletter links. | Systems Update deck p136; Master Deck p77 |
| 3 | Refunds | "Your assessment fee is non-refundable." | No policy stated. Refund requests go to Monday's huddle. | Systems Update deck p59 |
| 4 | 60-day window and paying again | 60 days, then inactive, pay the fee again | Not mentioned anywhere | none |
| 5 | Sign-off credentials | Alysha Pruitt Harvey, MAcc, EA, Founder and Managing Partner | "Alysha Harvey, EA, CTS, CTP, CTC – Founder & CEO" | Master Deck p27 |
| 6 | ® usage | Distinct Tax Consulting Group® and Distinct® everywhere | No ® on Distinct in any design. Footers read "© 2026 DISTINCT TAX CONSULTING GROUP · ALL RIGHTS RESERVED". Only "THE TAX ADVIZHER®" carries ®. | All brand designs |
| 7 | Email and text for documents | "Never send them by regular email or text." | "Please use your secure portal" for documents, but the decks also list text and email as normal channels | Master Deck p13 |
| 8 | Organizer opens a section per entity | Stated on page | Not described. The business organizer is "one organizer for 1120S, 1120 and 1065". | Systems Update deck p100 |
| 9 | Document checklist and videos | Prior returns, YTD P&L, IRS/state letters; two videos | No assessment checklist or videos exist in the designs yet | none |

Available but not added, because your footer brief didn't include them: phone **770-742-9136**, **contact@distincttax.com** and office hours (Master Deck p36). The phone line is moving into GHL with an AI booking agent (Systems Update deck p136).

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
6. **Build the sections, top to bottom.** For each of the 11 blocks, in order (1, 1B, 2 … 10):
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

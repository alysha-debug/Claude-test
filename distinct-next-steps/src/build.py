"""Assemble the Distinct Next Steps page: GHL paste blocks, standalone preview, and build kit."""
import pathlib, re
ROOT = pathlib.Path(__file__).resolve().parent.parent
SRC = ROOT / "src"
base = (SRC / "base.css").read_text().strip()
motion = (SRC / "motion.js").read_text().strip()
sections = sorted((SRC / "sections").glob("*.html"))

HEAD_BLOCK = """<!-- Distinct Next Steps: GLOBAL HEAD CODE (paste once in GHL: step Settings > Tracking Code > Head) -->
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
</script>"""

blocks = []
outdir = ROOT / "ghl-blocks"; outdir.mkdir(exist_ok=True)
for f in sections:
    code = f.read_text().replace("/*BASE*/", base).replace("/*MOTION*/", motion).strip()
    (outdir / f.name).write_text(code + "\n")
    title = re.search(r"SECTION (\d+[A-Z]?): ([^(]+)\((#[\w-]+)\)", code)
    blocks.append((f.name, title.group(1), title.group(2).strip(), title.group(3), code))
(outdir / "00-global-head.html").write_text(HEAD_BLOCK + "\n")

preview = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Next Steps | Distinct Tax Consulting Group®</title>
<meta name="description" content="Your next steps after purchasing the Distinct® Tax Assessment.">
{HEAD_BLOCK}
<style>body{{margin:0}}</style>
</head>
<body>
<main>
""" + "\n\n".join(b[4] for b in blocks if not b[0].startswith("10-")) + "\n</main>\n\n" + \
    next(b[4] for b in blocks if b[0].startswith("10-")) + "\n</body>\n</html>\n"
(ROOT / "index.html").write_text(preview)

notes = {
 "1": "Section: full width, background #003B42, padding 0. Dark-teal hero with the turning promise line and its Pause motion button. This is the only H1 on the page.",
 "1B": "Section: full width, background #01262B, padding 0. The transformation moment: plays once when it scrolls into view, with a See it again button. Paste it directly under Section 1.",
 "2": "Section: full width, background #FFFFFF, padding 0. Teal flip cards (tap to turn over).",
 "3": "Section: full width, background #003B42, padding 0. When the video is ready, swap the placeholder for the embed (see the comment in the code).",
 "4": "Section: full width, background #FFFFFF, padding 0. Leave href=\"[TAXDOME PORTAL LINK]\" until you have the TaxDome login URL.",
 "5": "Section: full width, background #F2F6F6, padding 0. Flip cards: front shows the mock-up, back shows where to find it. Swap each image placeholder for your mock-up (see comments). Alysha must confirm the document list.",
 "6": "Section: full width, background #003B42, padding 0. Includes the turning-words card with its Pause motion button.",
 "7": "Section: full width, background #FFFFFF, padding 0. Static text only: no countdown.",
 "8": "Section: full width, background #01262B, padding 0.",
 "9": "Section: full width, background #FFFFFF, padding 0. This block repeats the [TAXDOME PORTAL LINK] button.",
 "10": "Section: full width, background #01262B, padding 0. Turn off GHL's default footer, if your funnel has one, to avoid two footers.",
}
md = [(ROOT / "src" / "kit-intro.md").read_text().strip(), "",
      "## Global head code (paste once)", "",
      "Paste in the funnel step: **Settings → Tracking Code → Head**. It loads Jost, turns on smooth scrolling and the gentle scroll-in animation, and keeps this page out of search results. If you skip it, everything still shows, just without the animation.", "",
      "```html", HEAD_BLOCK, "```", ""]
for name, n, t, anchor, code in blocks:
    md += [f"## SECTION {n}: {t.title().replace("Taxdome","TaxDome")} (`{anchor}`)", "",
           f"**GHL build note:** {notes[n]} Add a 1-column row, then a **Custom Code** element, and paste the block below. Paste-ready file: `ghl-blocks/{name}`.", "",
           "```html", code, "```", ""]
md.append((ROOT / "src" / "kit-outro.md").read_text().strip())
(ROOT / "distinct-next-steps-ghl-build-kit.md").write_text("\n".join(md) + "\n")
print("built", len(blocks), "sections")

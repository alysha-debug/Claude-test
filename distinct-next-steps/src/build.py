"""Assemble the Distinct Next Steps page: GHL paste blocks, standalone preview, and build kit."""
import pathlib, re
ROOT = pathlib.Path(__file__).resolve().parent.parent
SRC = ROOT / "src"
base = (SRC / "base.css").read_text().strip()
sections = sorted((SRC / "sections").glob("*.html"))

HEAD_BLOCK = """<!-- Distinct Next Steps: GLOBAL HEAD CODE (paste once in GHL: step Settings > Head tracking code) -->
<meta name="robots" content="noindex, nofollow">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Jost:wght@400;500;700&display=swap" rel="stylesheet">
<style>
  html{scroll-behavior:smooth}
  @media (prefers-reduced-motion:reduce){html{scroll-behavior:auto}}
  body{background:#fbf8f2}
</style>"""

blocks = []
outdir = ROOT / "ghl-blocks"; outdir.mkdir(exist_ok=True)
for f in sections:
    code = f.read_text().replace("/*BASE*/", base).strip()
    (outdir / f.name).write_text(code + "\n")
    title = re.search(r"SECTION (\d+): ([^(]+)\((#[\w-]+)\)", code)
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
 "1": "Section: full width, background #F3EDE1, padding 0. This is the only H1 on the page.",
 "2": "Section: full width, background #FBF8F2, padding 0. Step progress is saved in the visitor's own browser only.",
 "3": "Section: full width, background #FFFFFF, padding 0. When the video is ready, swap the placeholder for the embed (see the comment in the code).",
 "4": "Section: full width, background #FBF8F2, padding 0. Leave href=\"[TAXDOME PORTAL LINK]\" until you have the TaxDome login URL.",
 "5": "Section: full width, background #FFFFFF, padding 0. Swap each image placeholder for your mock-up (see comments). Alysha must confirm the document list.",
 "6": "Section: full width, background #FBF8F2, padding 0. The entity counter is a helper only and saves nothing.",
 "7": "Section: full width, background #FFFFFF, padding 0. Static text only: no countdown.",
 "8": "Section: full width, background #FBF8F2, padding 0.",
 "9": "Section: full width, background #FFFFFF, padding 0. This block repeats the [TAXDOME PORTAL LINK] button.",
 "10": "Section: full width, background #F3EDE1, padding 0. Turn off GHL's default footer, if your funnel has one, to avoid two footers.",
}
md = [(ROOT / "src" / "kit-intro.md").read_text().strip(), "",
      "## Global head code (paste once)", "",
      "Paste in the funnel step: **Settings → Tracking Code → Head**. It loads Jost, turns on smooth scrolling and keeps this page out of search results.", "",
      "```html", HEAD_BLOCK, "```", ""]
for name, n, t, anchor, code in blocks:
    md += [f"## SECTION {n}: {t.title().replace("Taxdome","TaxDome")} (`{anchor}`)", "",
           f"**GHL build note:** {notes[n]} Add a 1-column row, then a **Custom Code** element, and paste the block below. Paste-ready file: `ghl-blocks/{name}`.", "",
           "```html", code, "```", ""]
md.append((ROOT / "src" / "kit-outro.md").read_text().strip())
(ROOT / "distinct-next-steps-ghl-build-kit.md").write_text("\n".join(md) + "\n")
print("built", len(blocks), "sections")

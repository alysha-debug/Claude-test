# Distinct® Tax Assessment: Next Steps page (GHL build kit)

Post-payment thank-you step for Distinct Tax Consulting Group®. It sits right after the $500 Distinct® Tax Assessment checkout.

- **Layout:** single page, mobile-first, 10 sections. Each section is one GHL **Custom Code** element.
- **Self-contained:** each block carries its own CSS (brand tokens included) and its own small vanilla script where needed. There are no external frameworks. Jost is the only external file, loaded from Google Fonts.
- **Live preview:** `index.html`, the whole page assembled from these same blocks.
- **Paste-ready files:** `ghl-blocks/00-global-head.html` to `ghl-blocks/10-footer.html`. These are the same code as below.

## Brand palette in use

Source: your Canva designs from Nov 5, 2026 onward. These are *The Distinct Experience Guide*, *Capability Statement*, *Letterhead MASTER*, *Business Cards 2026*, *Client Roadmap*, *Referral Program deck* and recent DTCG social posts. All eight colors below appear across them. Text is set the way your light designs set it: teal headings over the slate body color.

| Token | Hex | Used for | Contrast |
|---|---|---|---|
| Teal (ink) | `#003B42` | Headings, primary buttons, bold text | 11.6:1 on cream ✔ |
| Slate (body) | `#3B4F52` | Body and secondary text (Capability Statement body color) | 8.2:1 on cream ✔ |
| Cream (canvas) | `#FBF8F2` | Page background, button text | Button text on teal 11.6:1 ✔ |
| Ivory | `#F3EDE1` | Welcome and footer backgrounds, pills | Teal text 10.6:1 ✔ |
| Gold | `#B18132` | Rules, the italic accent word in headings, large numerals, diamond bullets, borders, focus ring | 3.3:1. Used only at heading size or as decoration, never for small text |
| Dark gold | `#96691C` | Small uppercase eyebrow labels (on cream and white only) | 4.6:1 on cream ✔ |
| Champagne | `#E6CD96` | Tinted highlight fills (deadline card, notes) | Teal text 7.9:1 ✔ |
| White | `#FFFFFF` | Cards and alternating sections | |

Not used: sage `#8FA5A2` fails text contrast on cream (2.5:1), and white text on gold fails (3.5:1). There is no dark theme anywhere.

**Brand motifs carried over:** a short gold rule before labels, one *italic gold accent word* per heading (from your serif headings, set here in Jost Bold Italic), the double hairline inset frame (business cards and decks), gold diamond bullets (Capability Statement), and the tagline *Protect More. Keep More. Build More.*

**Type:** Jost 700 for headings, 500 for subheads and buttons, 400 for body. **Shape:** 18px corners on cards and video frames, pill-shaped buttons.

## Anchors

`#welcome` · `#steps` · `#welcome-video` · `#taxdome-video` · `#checklist` · `#organizer` · `#deadline` · `#what-next` · `#security` · `#footer`

Every section is a real landmark with a heading, so keyboard and screen-reader users land in the right place when they follow an anchor link. It has `tabindex="-1"` and a `scroll-margin-top` offset.

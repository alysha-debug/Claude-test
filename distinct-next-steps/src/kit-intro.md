# Distinct® Tax Assessment: Next Steps page (GHL build kit)

Post-payment thank-you step for Distinct Tax Consulting Group®. It sits right after the $500 Distinct® Tax Assessment checkout.

- **Layout:** single page, mobile-first, 10 sections. Each section is one GHL **Custom Code** element.
- **Self-contained:** each block carries its own CSS (brand tokens included) and its own small vanilla script where needed. There are no external frameworks. Jost is the only external file, loaded from Google Fonts.
- **Live preview:** `index.html`, the whole page assembled from these same blocks.
- **Paste-ready files:** `ghl-blocks/00-global-head.html` to `ghl-blocks/10-footer.html`. These are the same code as below.

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

**Moving parts:**
- step cards that check off, with a progress ring
- a floating progress pill that always links to your next unfinished step
- a document checklist counter
- an entity counter in the organizer section
- a gentle scroll-in animation (turned off for visitors who reduce motion)
- no countdown timers

**Type:** Jost 700 for headings (700 italic for the accent word), 500 for subheads and buttons, 400 for body. **Shape:** 20px corners on cards and video frames, pill-shaped buttons.

## Anchors

`#welcome` · `#steps` · `#welcome-video` · `#taxdome-video` · `#checklist` · `#organizer` · `#deadline` · `#what-next` · `#security` · `#footer`

Every section is a real landmark with a heading, so keyboard and screen-reader users land in the right place when they follow an anchor link. It has `tabindex="-1"` and a `scroll-margin-top` offset.

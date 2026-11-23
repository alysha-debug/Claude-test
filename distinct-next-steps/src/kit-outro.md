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

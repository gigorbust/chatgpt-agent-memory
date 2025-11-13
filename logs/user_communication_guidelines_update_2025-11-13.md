# User Communication Guidelines – Update (13 Nov 2025)

This update supplements the existing communication guidelines with UI nuances and process tips discovered during the 2025‑11‑13 session.  It aims to ensure smoother navigation of the Wix Studio editor and clearer communication about common pitfalls.

## New UI Nuances

1. **Layers panel for precise selection:** The left‑hand Layers panel lists all elements on a page (headers, sections, repeaters, etc.).  Use this panel to select nested elements like repeaters and avoid mis‑clicking on the canvas.  Selecting a repeater in the Layers panel keeps the dataset connection intact.

2. **Breadcrumb navigation:** At the bottom of the editor, a breadcrumb trail shows the hierarchy of the current selection (e.g. `Page → Section → Repeater → Item`).  Clicking on `Repeater` in this trail returns focus to the entire repeater.  This is useful after editing an individual item.

3. **Dataset resets on item edit:** Double‑clicking a repeater item detaches the dataset connection and switches the selection to `Item`.  If this happens, use the undo arrow (top toolbar) or `Cmd+Z` to revert, then re‑select the repeater via the Layers panel.

4. **Undo functionality:** The undo arrow in the top toolbar reliably restores previous states, including dataset connections and design changes.  Use it immediately after unintended modifications.  `Cmd+Z` (macOS) or `Ctrl+Z` (Windows) performs the same action.

5. **Add panel location:** To insert new elements (images, headings, text, buttons) into a repeater item, locate the Add panel (plus‑icon) on the left toolbar.  Be aware that other icons (Site Pages, Global Sections, Site Styles) appear similar; move the cursor slowly to ensure the correct panel opens.  Once open, choose appropriate elements and drag them into the repeater item.

6. **Avoid duplicate datasets:** When binding elements inside a repeater, always use the existing dataset (e.g. `Services dataset`).  Do not add new datasets unless absolutely necessary.  Confirm the dataset connection in the right‑hand **Connect Repeater** panel.

## Tone and Style Reminders

* Continue to communicate directly and truthfully, focusing on practical steps.  Provide clear, actionable instructions limited to two or three steps at a time.
* Use full code blocks or detailed descriptions when guiding the user through technical actions.  Avoid unnecessary repetition and maintain a concise, forward‑thinking tone.

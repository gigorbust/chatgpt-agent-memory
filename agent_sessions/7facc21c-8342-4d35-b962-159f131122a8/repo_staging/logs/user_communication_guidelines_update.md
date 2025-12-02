# MezTal Project – Additional Communication & UI Handling Guidelines

This update supplements the existing **User Communication Guidelines** by capturing recurring operational tips and UX nuances when working in the Wix Studio editor. Add these details to future sessions to maintain consistency and minimize errors.

## Interface Management

- **Layers Panel for Element Selection:** When the page becomes crowded with sections, repeaters, or datasets, use the **Layers** panel to select specific elements without clicking through overlapping layers. This helps avoid accidentally deleting or moving the wrong component.

- **Close Unused Panels:** To reduce clutter and ensure you’re always working on the correct element, close unused overlays (e.g., App Market, Code panel, Layers panel) before opening another. This keeps the workspace manageable and prevents accidental clicks.

## Drag‑and‑Drop Best Practices

- **Be Deliberate:** When dragging elements (e.g., inserting a Repeater or moving sections), click and hold for a moment before moving. Wix sometimes responds slowly; releasing the mouse too soon can drop the element in an unintended place or fail to insert it.

- **Wait for Highlight/Anchor:** Do not release the drag until you see the highlight or anchor zone on the page that confirms where the element will be placed. If nothing highlights, slowly move the cursor until it does.

- **Assume Slow Wi‑Fi:** If the editor seems unresponsive, pause briefly after each drag or click to allow the interface to catch up. Avoid rapid multiple clicks, which can lead to duplicate elements.

## Keyboard Shortcuts & Efficiency

- **Save via Enter:** When adding fields in the CMS, the **Save** button sometimes does not respond. Press **Enter** after typing the field name to save reliably.

- **Undo (Ctrl + Z):** Use **Ctrl + Z** (Cmd + Z on Mac) to undo the last action if you accidentally delete or move an element.

- **Multi‑Action Edits:** When entering text (such as URLs or field names), use **Ctrl + A** to select all before typing a new value. This avoids leftover text from previous entries.

## Dataset & Repeater Binding

- **Dataset Anchor:** On dynamic pages, each Repeater has a small vertical cylinder (dataset anchor) on its left. Click this anchor to open the **Connect Repeater** panel and choose the correct dataset (e.g., `solutions`). If the page selects the Section instead, use the Layers panel to select the Repeater first.

- **Avoid Duplicate Datasets:** Dynamic pages already include a dataset for their collection; adding another can create confusion. Connect repeaters to the existing dataset instead of creating new ones.

## Error Recovery & Duplicates

- **Delete Mistakes Immediately:** If you insert an extra dataset or repeater by mistake, select it via the Layers panel and press **Delete** to remove it. This prevents later confusion.

- **One Source of Truth:** Do not create duplicate collections or fields in the CMS. Always verify the collection list before creating a new one. Remove unused fields to avoid clutter.

## Logging & Nuance Preservation

- **Capture New Tips:** When you learn a new UI nuance (e.g., pressing Enter to save, using Layers to select nested items), add it to this document or the user communication guidelines. This prevents memory drift.

- **Respect Tone and Intent:** Always align responses with the user’s direct, concise, practical style. Do not add unnecessary instructions, and avoid generic or filler language.

## Using This Document

- Reference this update in each new session alongside the main **User Communication Guidelines**.  
- When the user provides new process insights, add them here and commit to the repository.

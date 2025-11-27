# MezTal Dynamic Pages – Binding & QA Checklist (2025‑11‑13)

**Purpose:**  
This checklist is the step‑by‑step script that a human or a future agent with Wix Studio access should follow to:

- Verify and complete data binding for all core dynamic list + item pages.
- Confirm SEO patterns are correctly wired.
- Reduce mis‑clicks and UI thrash while doing it.
- Feed clean status updates back into `/logs` (`open_tasks`, session summaries, and session logs).

Use this together with:

- `meztal_agent_operating_manual_2025-11-13.md`
- `meztal_open_tasks_addendum_2025-11-13_chatgpt-atlas.md`
- Any existing `open_tasks*.md` and `session_summary_*.md` files.

---

## 0. Pre‑Flight: How to Work in Wix Studio

Before doing **any** binding work:

1. **Open MezTal (Sandbox) in Wix Studio**
   - Go to `manage.wix.com` in your own browser.
   - Log in manually (AI must not handle credentials).
   - Open the **MezTal (Sandbox)** site and click **Edit Site** to enter Wix Studio.

2. **Editor Setup**
   - Open the **Layers** panel and keep it visible.
   - Set zoom to **70–90%** so repeaters and sections are fully visible.
   - Close any unused panels/overlays that clutter the canvas.

3. **Interaction Rules**
   - Use **Layers panel** for selection as much as possible.
   - **Hover** icons (chain/link, database, gear, etc.) before clicking.
   - **Avoid double‑clicking** unless explicitly needed.

4. **Logging Setup**
   - Have `/logs` open in GitHub or locally.
   - Plan to log:
     - What pages you touched.
     - What bindings you changed.
     - Any errors or weird behavior (with exact wording).

---

## 1. Global Dataset & Page Sanity Check

You’ll do a quick pass on core datasets before binding specific pages.

### 1.1 Collections to locate

In **Content Manager → Collections**, confirm existence (or lack) of these collections:

- `services`
- `solutions` (if separate from services)
- `industries`
- `case_studies`
- `resources` (or blog‑equivalent)
- `locations`

For each collection:

- Confirm it has these kinds of fields (names may vary, note exact names):

  - **Services / Solutions‑like collections**
    - `name` or `title`
    - `short_description`
    - `thumbnail_image`
    - `meta_description` (optional but ideal)
    - Slug / URL field (for dynamic item pages)

  - **Industries**
    - Display name field (e.g., `industry_name`)
    - `short_description`
    - Image field (e.g., `thumbnail_image`)
    - `meta_description` (if present)
    - Slug / URL

  - **Case Studies**
    - `title`
    - `client_name` (if exists)
    - `project_name` (if exists)
    - `cover_image`
    - `description` / `summary`
    - `meta_description`
    - Slug / URL

  - **Resources**
    - `title`
    - `excerpt`
    - `cover_image`
    - `meta_description`
    - Slug / URL

  - **Locations**
    - `Title` / `city_name` / similar
    - Short blurb field
    - Image field
    - `meta_description` (if present)
    - Slug / URL

> **If any collection is missing or clearly different:**
> - Do **not** create new collections lightly.
> - Write down exactly what you see.
> - Add a task in `open_tasks_update_YYYY-MM-DD_addendum*.md`:
>   - e.g., `industries collection missing – blocked` or `services collection uses field "ServiceName" instead of "name"`.

---

## 2. Solutions (List) – Binding & QA

Assumes: “Solutions (List)” is a dynamic list page bound to **services** or a similar collection.

### 2.1 Navigate

1. In the Pages / Sitemap panel:
   - Go to **Solutions Pages (Dynamic) → Solutions (List)**.
   - Confirm the page label at top says **Solutions (List)** and marks it as **Dynamic**.

2. If you see a warning like **“This page is no longer dynamic”**:
   - **Stop.**
   - Capture exact text.
   - Add a `blocked` task in open tasks and describe what you see.
   - Do not try to “fix” by rebuilding the page without planning.

### 2.2 Dataset and Repeater Structure

1. Check **datasets** on the page:
   - There should be **one main dataset** for this list (likely `services` or similar).
   - Confirm:
     - `Read` mode
     - Correct collection chosen
     - Filter and sort are reasonable (or default for now).

2. In the **Layers** panel, drill down to repeater:

   - `Page → [Section Grid] → [Cell] → [Repeater] → [Item] → [Stack or container]`
   - Inside the item, identify:
     - Image element
     - Title text element (H2)
     - Paragraph text element
     - Button element

### 2.3 Bindings

For the **repeater item template**:

- **Image**
  - Click the image → dataset / connect icon.
  - Bind **Image Source** to: `thumbnail_image` (or actual image field used for solutions).
  - Bind **Alt Text** to: `title` (fallback `name` if `title` not present).

- **Title (H2)**
  - Connect to: `title` (fallback `name` / `solution_name`).

- **Paragraph**
  - Connect to: `short_description` (or best available summary field).

- **Button**
  - Set **label** to a temporary but meaningful string:
    - `"Start Now"` (can refine later).
  - Set **link**:
    - Preferred: “**This item’s dynamic page**.”
    - If Wix says “No item pages yet”:
      - Use the link / chain icon.
      - Manually choose the dynamic item page for this collection (likely something like `Services (Item) (Dynamic)`).

> **QA:**  
> - Preview the page.  
> - Confirm:
>   - Each card shows a *different* solution.  
>   - Images look right and fit.  
>   - Descriptions are not obviously truncated mid‑sentence (field selection check).  
>   - Buttons go to the correct dynamic item pages.

Log any weirdness (e.g., same data repeated, broken images) with exact field names.

---

## 3. Services (List) – Binding & QA

If **Services (List)** is separate from **Solutions (List)**:

### 3.1 Navigate

- Go to **Services (List)** in the Pages panel.
- Confirm it is marked **Dynamic** and is bound to the appropriate dataset (likely `services`).

### 3.2 Dataset & Repeater

- Same approach as Solutions:
  - Confirm a single dataset connected to `services`.
  - Use Layers to locate repeater → item → inner stack.

### 3.3 Bindings

- **Image:** `thumbnail_image` + alt text from `name`.
- **Title:** `name`.
- **Paragraph:** `short_description`.
- **Button:**
  - Label: `"Get Service"`.
  - Link: “This item’s dynamic page” → `Services (Item) (Dynamic)`.

Preview and test:

- Each service shows correct info.
- Button click → expected service detail page.

---

## 4. Industries (List) – Binding & QA

### 4.1 Navigate & Collection Check

- Go to **Industries (List)** in Pages.
- Confirm dynamic status and dataset:

  - If dataset is missing or shows something generic:
    - Check Content Manager for an **industries** collection.
    - If missing: log `blocked – industries dataset missing`.

### 4.2 Repeater Binding

If industries collection exists and is attached:

- **Image:**
  - Source: `thumbnail_image` or primary image field.
  - Alt: industry display name (`industry_name` or equivalent).

- **Title:**
  - Bind to the industry display name field.

- **Paragraph:**
  - Bind to `short_description` or an equivalent summary.

- **Button:**
  - Label: `"Explore Industry"`.
  - Link: “This item’s dynamic page” → `Industries (Item) (Dynamic)`.

Preview:

- Confirm different industries show correctly.
- Check at least 2–3 items to ensure no mismatched fields.

If the **Industries (Item)** dynamic page is missing entirely:

- Log a task: `Create Industries dynamic item page + connect to industries collection (blocked until spec confirmed).`

---

## 5. Case Studies (List) – Binding & QA

### 5.1 Navigate

- Open **Case Studies (List)**.
- Confirm dynamic status and dataset likely named `case_studies`.

### 5.2 Binding

Inside repeater item:

- **Image:**
  - `cover_image`.
  - Alt text: `title`, or combined `client_name – project_name` if both exist.

- **Title:**
  - `title` (or best available combined field, e.g., `client_name – project_name`).

- **Paragraph:**
  - `description` or dedicated `summary` field.

- **Button:**
  - Label: `"Read Case Study"`.
  - Link: “This item’s dynamic page” → item page (e.g., `Case_studies (Item) (Dynamic)`).

Preview:

- Click 2–3 case study cards.
- Ensure item pages load with correct case study, not a random record.

---

## 6. Resources (List) – Binding & QA

### 6.1 Navigate & Dataset

- Open **Resources (List)**.
- Confirm dataset is a resources/blog collection (`resources`, `blog_posts`, etc.).

### 6.2 Binding

- **Image:**
  - `cover_image`.
  - Alt: `title`.

- **Title:**
  - `title`.

- **Paragraph:**
  - `excerpt` or short summary field.

- **Button:**
  - Label: `"Read Article"` or `"Learn More"` (pick **one** and keep consistent).
  - Link: “This item’s dynamic page” → `Resources (Item) (Dynamic)`.

Preview:

- Confirm each card goes to the right resource article.

---

## 7. Locations (List) – Binding & QA

### 7.1 Navigate & Dataset

- Open **Locations (List)**.
- Confirm dynamic status and dataset `locations` (or equivalent).

### 7.2 Binding

- **Image:**
  - Source: location image field.
  - Alt: `Title` or `city_name`.

- **Title:**
  - `Title` or `city_name` (whatever is main display).

- **Paragraph:**
  - Short blurb / summary field.

- **Button:**
  - Label: `"View Location"`.
  - Link: “This item’s dynamic page” → `Locations (Item)`.

Preview:

- Ensure each location card leads to a distinct location page.

---

## 8. Dynamic Item Pages – SEO & Content Check

For each dynamic item page (services, industries, case studies, resources, locations, solutions):

### 8.1 Navigate

- In Pages, find each item template, e.g.:
  - `Services (Item)`
  - `Solutions (Item)` (if exists)
  - `Industries (Item)`
  - `Case Studies (Item)`
  - `Resources (Item)`
  - `Locations (Item)`

### 8.2 SEO Patterns

In the page’s **SEO settings**:

- **Title pattern:**
  - Prefer: `{{name}} | MezTal`
  - Fallback: `{{title}} | MezTal`

- **Description pattern:**
  - Prefer: `{{meta_description}}`
  - Fallback: `{{short_description}}`

- **Slug:**
  - Confirm slug comes from a clean field (slug or name), not some internal ID.

> If Wix Studio has limitations on SEO patterns:
> - Note exactly what’s possible and what’s not.
> - Write it down in `session_summary_YYYY-MM-DD.md`.

### 8.3 Item Page Content Layout

For each template, open 2–3 items in **Preview** and check:

- Hero/title section shows correct record name.
- Body layout looks reasonable with real data (no obvious overflow or clipping).
- CTAs (buttons) link logically (back to list, to contact, etc.).

Document any layout issues as discrete tasks in `open_tasks_update_*.md`.

---

## 9. Logging: How to Record What You Did

As you execute this checklist:

1. **Session Summary**
   - Create or update `session_summary_YYYY-MM-DD*.md`:
     - Pages visited.
     - Collections checked.
     - What bindings you fixed and how.
     - Any blocked items (with exact Wix messages).

2. **Session Log Addendum**
   - `meztal_session_log_YYYY-MM-DD_addendumN.md`:
     - Short timestamped entries, e.g.:

       ```text
       [2025-11-13 18:05 UTC] Bound Solutions (List) repeater image/title/description/button to services collection.
       [2025-11-13 18:20 UTC] Configured SEO title/description patterns for Services (Item) dynamic page.
       ```

3. **Open Tasks Addendum**
   - `open_tasks_update_YYYY-MM-DD_addendumN.md`:
     - Mark tasks as `done` when verified.
     - Add new tasks for:
       - Missing datasets.
       - Broken dynamic pages.
       - Layout/UX issues discovered while previewing.

4. **Optional: ZIP Packaging**
   - Bundle today’s new/updated log files (session summary, session log addendum, open tasks addendum) into:
     - `meztal_logs_YYYY-MM-DD_sessionN.zip`
   - Commit this ZIP along with the raw `.md` files to `/logs`.

---

## 10. When to Stop and Escalate

Stop the checklist and escalate (to George or a future agent) if:

- A dynamic list page shows **“This page is no longer dynamic”** and you don’t know why.
- A required collection (e.g., `industries`) is missing and you’re not sure if it should be re‑created or restored.
- SEO patterns cannot be set as described due to Wix constraints.
- You hit consistent network/editor errors.

In each case, log:

- Exact error/issue text.
- Which page/collection it happened on.
- What you tried (if anything) before stopping.

This ensures the next agent has an accurate starting point instead of guessing.

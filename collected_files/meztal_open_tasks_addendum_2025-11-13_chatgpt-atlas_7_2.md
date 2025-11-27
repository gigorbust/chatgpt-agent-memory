# Open Tasks Addendum – 2025‑11‑13 (ChatGPT Atlas)

**Important context:**  
This addendum was created from an environment **without direct access** to the GitHub `/logs` folder or the live Wix Studio editor.  
- All task statuses below are therefore marked as **“status unknown – assume open until verified.”**  
- Once a future agent can see both the repo and the live site, these tasks should be reconciled with `open_tasks.md` and its existing addenda.

---

## Legend

- **Status** values used here:
  - `unknown (assume open)` – could not verify; treat as open until checked.  
  - `blocked – network` – blocked by network / environment issues.  
  - `blocked – missing dataset/page` – blocked because the required Wix collection or dynamic page is not present.  
  - `planned` – design/intention is documented but has not been executed yet (in this session).

- **Priority** values:
  - `P0` – critical for core navigation / UX.  
  - `P1` – important but not blocking basic site use.  
  - `P2` – nice‑to‑have / cleanup / logging improvements.

---

## A. Dynamic List Page Data‑Binding

These tasks are derived directly from the master prompt and represent the intended binding state for MezTal’s dynamic list pages.

### A1. Solutions (List) repeater binding

- **Task:** Ensure **Solutions (List)** (under “Solutions Pages (Dynamic)”) uses a repeater bound to the **`services` dataset**, with:
  - Image → `thumbnail_image` (alt: `title` fallback `name`; no link)  
  - Title (H2) → `title` (fallback `name`)  
  - Paragraph → `short_description`  
  - Button label → `"Start Now"` (or a later refined label)  
  - Button link → “This item’s dynamic page” → `Services (Item) (Dynamic)`  
- **Status:** `unknown (assume open)`  
- **Priority:** `P0`  
- **Notes:** Confirm that binding is applied at the **repeater item template** level and that no duplicate datasets are added to the page.

### A2. Services (List) binding

- **Task:** On **Services (List)**:
  - Bind repeater to the services collection (likely `services`).  
  - Image → `thumbnail_image` (meaningful alt text).  
  - Title → `name`.  
  - Description → `short_description`.  
  - Button label → `"Get Service"`  
  - Button link → `Services (Item) (Dynamic)` for the current item.  
- **Status:** `unknown (assume open)`  
- **Priority:** `P0`  
- **Notes:** Confirm that the dataset is configured for read‑only access appropriate for a public site.

### A3. Industries (List) binding and dataset health

- **Task:** On **Industries (List)**:
  - Bind repeater to the **industries** dataset (if it exists).  
  - Image → `thumbnail_image` (alt: industry display name).  
  - Title → the industry name field.  
  - Description → `short_description` or equivalent.  
  - Button label → `"Explore Industry"`  
  - Button link → `Industries (Item) (Dynamic)` item page.  
- **Status:** `unknown (assume open)`  
- **Priority:** `P0`  
- **Special condition:**  
  - If the industries dataset or dynamic item page is missing, record:
    - `blocked – missing dataset/page` in the next addendum.  
    - The exact dataset/page names observed in Wix.

### A4. Case Studies (List) binding

- **Task:** On **Case Studies (List)**:
  - Bind repeater to the case‑studies collection.  
  - Image → `cover_image` (alt: `title` or `client_name – project_name`).  
  - Title → `title` (or best combined label).  
  - Description → `description` or summary field.  
  - Button label → `"Read Case Study"`  
  - Button link → `Case_studies (Item) (Dynamic)` page.  
- **Status:** `unknown (assume open)`  
- **Priority:** `P1`

### A5. Resources (List) binding

- **Task:** On **Resources (List)**:
  - Bind repeater to the resources/blog collection.  
  - Image → `cover_image` (alt: `title`).  
  - Title → `title`.  
  - Description → `excerpt` (or short summary).  
  - Button label → `"Read Article"` or `"Learn More"` (choose one consistent convention).  
  - Button link → `Resources (Item) (Dynamic)` page.  
- **Status:** `unknown (assume open)`  
- **Priority:** `P1`

### A6. Locations (List) binding

- **Task:** On **Locations (List)**:
  - Bind repeater to the locations collection.  
  - Image → location image field (alt: `Title` or `city_name`).  
  - Title → `Title` or `city_name`.  
  - Description → short blurb field.  
  - Button label → `"View Location"`  
  - Button link → `Locations (Item)` item page.  
- **Status:** `unknown (assume open)`  
- **Priority:** `P1`

---

## B. Dynamic Item Page SEO Patterns

### B1. Configure SEO title/description patterns

- **Task:** For each dynamic **item page** template (services, industries, case studies, resources, locations, solutions, etc.), ensure:

  - **Title pattern:**  
    - Primary: `{{name}} | MezTal`  
    - Fallback: `{{title}} | MezTal`  

  - **Description pattern:**  
    - Primary: `{{meta_description}}`  
    - Fallback: `{{short_description}}`  

  - **Slug:** Confirm it is generated from the appropriate dataset field (e.g., a slug or name field, not an internal ID).

- **Status:** `unknown (assume open)`  
- **Priority:** `P0`  
- **Notes:** Any deviations or limitations in Wix Studio’s SEO pattern system should be documented in the next session summary.

---

## C. Editor UX and Reliability Tasks

These tasks are about **how** work gets done in Wix Studio, meant to reduce friction and mistakes.

### C1. Enforce Layers‑panel‑first selection

- **Task:** Adopt and maintain a norm that element selection is done via the **Layers panel**, not by clicking arbitrarily on the canvas.  
- **Status:** `planned`  
- **Priority:** `P1`  
- **Notes:** If a future session catches itself mis‑clicking frequently, log this and reaffirm the Layers‑panel rule.

### C2. Hover‑before‑click discipline

- **Task:** Always hover icons (database, chain, gear, etc.) to read tooltips before clicking, to avoid activating the wrong control.  
- **Status:** `planned`  
- **Priority:** `P1`

### C3. Avoid double‑clicking in the editor

- **Task:** Treat double‑clicks as dangerous unless there is a deliberate reason (e.g., Wix documentation explicitly requires it).  
- **Status:** `planned`  
- **Priority:** `P1`  
- **Notes:** If a double‑click causes an unwanted state change, record it in the session log with a short description.

### C4. Standardize zoom levels

- **Task:** Use a consistent zoom range (70–90%) when working on repeaters and dynamic pages, to minimize scrolling and mis‑clicks.  
- **Status:** `planned`  
- **Priority:** `P2`

---

## D. Network and Access Diagnostics

These tasks are required whenever the environment has trouble reaching Wix or GitHub.

### D1. Document network failures to Wix

- **Task:** If the agent encounters any error (e.g., `ERR_TUNNEL_CONNECTION_FAILED`) when loading Wix Studio or `manage.wix.com`:
  - Capture the exact error text.  
  - Note whether it was consistent across retries.  
  - Record it in:
    - The same‑day session summary.  
    - The next open‑tasks addendum under `blocked – network`.
- **Status:** `planned`  
- **Priority:** `P0`

### D2. Document repository access limitations

- **Task:** If the GitHub `/logs` directory cannot be accessed (missing connector, private repo, etc.):
  - Explicitly state this in the session summary.  
  - Do **not** guess or “pretend” to have updated files.  
  - Fall back to documentation‑first behavior (design new addenda instead of modifying existing ones).  
- **Status:** `planned`  
- **Priority:** `P0`

---

## E. Logging and Knowledge‑Management Tasks

### E1. Normalize daily logging output

- **Task:** Ensure every working session produces at least:
  - One `session_summary_YYYY-MM-DD*.md` file.  
  - One `meztal_session_log_YYYY-MM-DD_addendum*.md` file with timestamped steps.  
  - One `open_tasks_*_addendum*.md` file reflecting any new or updated tasks.  
- **Status:** `planned`  
- **Priority:** `P1`

### E2. Package session artifacts into a ZIP

- **Task:** Bundle all new/updated `.md` files for a session into a ZIP (e.g., `meztal_logs_YYYY-MM-DD_sessionN.zip`) so the human can easily download and commit to GitHub.  
- **Status:** `planned` (this session has already done this for today).  
- **Priority:** `P1`

### E3. Reconcile this addendum with real open_tasks.md

- **Task (for a future, better‑connected session):**
  - Read `open_tasks.md` and all previous addenda.  
  - Merge the tasks described in this addendum into the canonical list, updating statuses from `unknown` to their true values.  
  - Remove duplicates and inconsistencies.  
- **Status:** `unknown (assume open)`  
- **Priority:** `P0`

---

## Summary

This addendum encodes **intended work** rather than confirmed site changes.  
Until a future agent can see both the GitHub `/logs` directory and the MezTal Wix Studio site, treat every task here as **open by default** and adjust only after verification.

# MezTal IA + Sitemap Finalization Log  
**File:** MEZTAL_SITEMAP_FINAL_LOG_2025-11-24.md  
**Scope:** Canonical sitemap + IA decisions as of 2025-11-24

---

## 1. Purpose

This log captures the **current, canonical state** of MezTal’s information architecture and sitemap.

It exists so future work (by humans or AI) does NOT:

- Re-ingest the same spreadsheets from scratch
- Re-open dead branches (bad industries, bad locations, synonym pages)
- Drift from the user’s explicit strategy and non-negotiables

The **source of truth** for all URLs is:

- `meztal_sitemap_final.xml` (this repo) – generated from `meztal_sitemap_updated.xml` with targeted cleanup and additions.

---

## 2. Non‑negotiable rules (global)

These rules override ANYTHING in any source file.

1. **Brand & Geo**
   - Company: **MezTal** (no “FlexTal” on site).
   - Delivery hubs: **Guadalajara and Mexico City** – always mentioned together when describing delivery footprint.
   - Value framing: **“overlapping business hours with the US”**  
     - Never: “same time zone”
     - Houston is allowed as a **US office location only**, not as the core of the nearshore value story.

2. **Savings claim**
   - Use: **“around 40% cost savings vs equivalent US hires”**  
   - Do NOT use 50%+ unless explicitly updated.

3. **Canonical service naming**
   - Primary concept: **“Augmented Workforce Solutions”**.
   - The following are **synonyms**, NOT separate Solution URLs:
     - staff augmentation
     - supplemental workforce staffing
     - contingent workforce
     - temporary staffing
     - workforce solutions
   - Synonyms can be:
     - Headings and keyword variants **on the Augmented Workforce Solutions page**
     - Included in **comparison pages** and educational content  
     - **Not** standalone service URLs under `/solutions/`.

4. **Blog vs Resources**
   - **Blog** = posts, news, commentary, updates, thought leadership.
   - **Resources** = case studies, comparison pages, pricing explainer, deep guides/FAQs, tools/checklists.
   - They are **separate nav hubs**.  
   - Do NOT merge them into “Blog/Resources” or similar.

5. **Locations & “Why” content**
   - No Cancun: `/locations/staffing-solutions-cancun` is deprecated and MUST NOT reappear.
   - We now use:
     - `/why-mexico` – high-level Why Mexico hub.
     - `/why-mexico/why-guadalajara`
     - `/why-mexico/why-mexico-city`
   - These pages must present **Guadalajara and Mexico City together** in the Mexico narrative.

---

## 3. Allowed data sources (for future AI runs)

Only these files (plus this log + other logs in this repo) are allowed as structured input:

1. `________ MEZTAL_SEO_MASTER_Minimal_2025-09-22_R3.xlsx`  
   - **Use only** the tab: `Architecture — Cleaned Map`  
   - Columns: `Primary Keyword`, `Secondary Keywords`, `Topic Cluster`, `Proposed URL`, `Page Type`, `Content Type`, `Funnel Stage`, `Persona`.
   - Some rows are marked “SKIPPED - Synonym” – those must **not** become pages.

2. `MezTal HUBSPOT copilot seo chat session_.txt`  
   - HubSpot-informed strategy, industries, service clusters.

3. `Report of HubSpot Closed Won Report January 2023-August 2024 2.xlsx`  
   - Real revenue: industries, deal types, ACV, role signals.

4. `LinkedIn MezTal Content - meztal_content_1754583488887 2.xlsx`  
   - Ignore metrics/analytics tabs.
   - Use content topics to inform **Blog categories** and **theme clusters**.

5. `Workable Job Openings for KW Strategy - 8_20_25 .xlsx`  
   - Role taxonomy and phrasing for **role/“Hire X” pages** and **Careers** content.

6. `Fellou -- MezTal.docx` and `Fellou -- MezTal.txt`  
   - Additional strategic/contextual copy (value props, ICP shaping).

7. `MezTal Competitor Analysis - Expanded.docx`  
   - Structural patterns from competitors: Solutions, Industries, Why-location, Resources, Careers, etc.
   - **Use only for structure inspiration**, never to invent services MezTal doesn’t offer.

8. `Report of Competitors.xlsx`  
   - Contains competitor list and metadata; used for high-level structural benchmarking.

9. **GitHub logs** in this repo  
   - Including: `MEZTAL_IA_SEO_MASTER_LOG_2025-11-23.md` and this file.

**Explicitly excluded:**

- Any older “MezTal SEO Master Aggregation” or “MezTal HubSpot-Informed SEO.xlsx” variants not listed above.
- Any references to “professional sports” or other bogus industries.

---

## 4. Sitemap: canonical file and key changes

### 4.1 Canonical sitemap file

- **File in repo:** `meztal_sitemap_final.xml`  
- **Current URL count:** 417  
- **Role:** Single source of truth for:
  - Relume IA generation
  - Wix site structure
  - SEO architecture

### 4.2 Canonicalization & cleanup applied

These changes were applied when generating `meztal_sitemap_final.xml` from `meztal_sitemap_updated.xml`:

1. **Trailing slash normalization**
   - All URLs normalized to **no trailing slash**, except:
     - Root: `https://meztal.com`
   - Example:
     - `/solutions/augmented-workforce/` → `/solutions/augmented-workforce`
     - `/industries/agetech/elder-care-tech/` → `/industries/agetech/elder-care-tech`

2. **Removed legacy / incorrect URLs**
   - Removed:
     - `/locations/why-mexico`
     - `/locations/why-guadalajara`
     - `/company/houston`
     - `/locations/houston-texas`
     - `/services/jobs-hiring`
     - `/services/developer-jobs`
     - `/solutions/supplemental-workforce` + `/solutions/supplemental-workforce/`  
       (this was explicitly marked SKIPPED in the SEO master to avoid cannibalization)

3. **Added missing core URLs**
   - Added:
     - `/faq` – global FAQ (nearshore, process, cost structure, passthrough fee, etc.)
     - `/apply-now` – candidate apply page (candidate CTA endpoint)
     - `/why-mexico` – main “Why Mexico” hub
     - `/why-mexico/why-guadalajara`
     - `/why-mexico/why-mexico-city`
     - `/company/linkedin` – LinkedIn embed hub (company-focused)
     - `/company/locations/houston` – US office location page (no nearshore value framing)

4. **Suppressed forbidden location**
   - Confirmed: **no Cancun URLs** present.
   - If any new “staffing-solutions-[city]” pages are ever generated, **Cancun must remain excluded**.

5. **Professional sports removed**
   - Confirmed: **no “professional sports” industry URLs** are present.
   - Any future suggestion of “professional sports” as an industry is a hard error and must be rejected.

---

## 5. IA structure: hubs and clusters (high-level)

This section is intentionally **structural**. Detailed leaf URLs live in `meztal_sitemap_final.xml`.

### 5.1 Main hubs (top-level)

These hubs are present as URLs and are expected to appear in some version of main nav:

- `/` – Home
- `/solutions` – Solutions hub (nav label: “Solutions”; may link into underlying **/services** URLs for SEO)
- `/services` – Services index (SEO-friendly “services” wording in URL)
- `/industries` – Industries hub
- `/why-mexico` – Why Mexico hub
- `/resources` – Resources hub (case studies, comparisons, guides, tools)
- `/blog` – Blog hub (posts, news, updates)
- `/company` – Company hub
- `/contact` – Contact page
- `/careers` – Careers hub (candidate-focused)
- `/faq` – Global FAQ
- `/apply-now` – Direct apply path

### 5.2 Key clusters under hubs

**Solutions / Services**

- IT / Data / Software:
  - `/services/it-staffing`
  - `/solutions/it-staffing-development`
  - `/solutions/application-development-outsourcing`
  - `/solutions/software-development` (parent)
  - `/solutions/web-development`
  - `/solutions/app-development`
  - `/nearshore-it-staffing/...` role-focused “Hire X” pages  
    (e.g., hire data governance engineer, hire Azure data engineer, hire Databricks engineer, hire business analyst, hire Oracle Hyperion developer)

- Accounting & Finance:
  - `/solutions/accounting-finance`
  - `/services/accounting-outsourcing`
  - `/services/payroll-outsourcing`
  - `/services/tax-services`
  - `/services/accounting-services`
  - Industry-specific: `/industries/senior-living/accounting` (Senior Living accounting services)

- HR / Talent / Augmented Workforce:
  - `/solutions/hr-talent-acquisition`
  - `/solutions/augmented-workforce`
  - `/solutions/talent-sourcing`
  - `/solutions/clinical-recruitment` (clinical recruitment services)
  - `/solutions/human-relations-support` (outsourced HR support)
  - `/solutions/senior-living/rpo` (RPO for senior living; also under Senior Living cluster)

- Marketing & Creative:
  - `/solutions/digital-marketing`
  - `/nearshore-marketing/hire-marketing-assistant`
  - `/nearshore-creative/hire-ui-designer`

- Operations / Admin / Workflow:
  - `/solutions/administrative-outsourcing`
  - `/solutions/workflow-automation`
  - `/solutions/workflow-automation/outsourcing`

- Customer Support / Call Center:
  - `/solutions/call-center-outsourcing`
  - `/nearshore-staffing-mexico`, `/remote-workers-mexico`, `/mexico-outsourcing`, `/remote-teams-mexico` (geo/nearshore landers)

- Employer of Record:
  - `/employer-of-record-mexico` – EOR-focused lander

**Industries**

- `/industries/senior-living`
  - `/industries/senior-living/accounting`
  - Connected: `/solutions/senior-living/rpo`

- `/industries/agetech`
  - `/industries/agetech/software-development`
  - `/industries/agetech/elder-care-tech`

- `/industries/financial-services`  
  - `/industries/financial-services/sarbanes-oxley-compliance-outsourcing`

Other industries present in the SEO master are filtered to only what MezTal truly serves; **no professional sports**.

**Why Mexico**

- `/why-mexico`
  - `/why-mexico/why-guadalajara`
  - `/why-mexico/why-mexico-city`

This replaces the old `/locations/why-mexico` and `/locations/why-guadalajara` structure.

**Company**

- `/company/about`
- `/company/team`
- `/company/locations`
  - `/company/locations/houston`
- `/company/linkedin`

**Resources**

- `/resources` hub with child URLs including:
  - Accounting/finance compliance & GAAP guides
  - Nearshoring vs offshoring comparisons
  - Nearshore team management guides
  - Mexico-specific strategic content (e.g., Mexico’s “Silicon Valley” story)
  - Comparison-style guides (e.g., best recruitment agencies) where they are framed as **resources**, not just comparison tables.

**Blog**

- `/blog` hub with posts reflecting LinkedIn content themes:
  - Nearshore strategy
  - Senior Living & AgeTech
  - Talent and workforce strategy
  - MezTal team/culture highlights
  - Events & conferences

---

## 6. Comparison pages strategy

- Comparison URLs live primarily under `/comparison/...` and some under `/resources/...` and `/services/...` as mapped in `Architecture — Cleaned Map`.
- Intent: **capture search/LLM traffic** for:
  - “best X companies”
  - “offshore vs nearshore vs onshore”
  - “staff augmentation vs managed services”
- UX strategy:
  - These **should not** be prominent in main nav to avoid over-exposing competitors.
  - Internal linking:
    - From comparison pages → core Solutions, Industries, Why Mexico, and Contact.
- “Staff augmentation firm” comparison pages are allowed as **comparison content**, even though the service term is a synonym; the canonical service page remains **Augmented Workforce Solutions**.

---

## 7. Corrections & guardrails

1. **Professional sports removed**
   - There is no “Professional Sports” industry in the sitemap.
   - If any tooling or AI proposes “professional sports” again, it must be rejected as off-strategy.

2. **Service vs Solutions wording**
   - URLs like `/services/...` are acceptable and often preferred for SEO (containing the word “services”).
   - Main nav can still use the label **“Solutions”** pointing into these services.
   - Do **not** create duplicate `/solutions/...` and `/services/...` versions of the same page unless explicitly defined as separate concepts.

3. **MezTal vs FlexTal**
   - All external-facing copy and pages: **MezTal** only.
   - Any legal “FlexTal” naming is kept to privacy/terms as necessary but not used in navigation or primary brand messaging.

---

## 8. How to use this log (for future work)

1. **If you’re an AI agent:**
   - Before doing ANY IA/SEO work, load:
     - This file
     - `MEZTAL_IA_SEO_MASTER_LOG_2025-11-23.md`
     - `meztal_sitemap_final.xml`
   - Treat these as **canon**.
   - Do NOT re-request the source spreadsheets unless new data is required.

2. **If you’re a human:**
   - Use `meztal_sitemap_final.xml` as the input to:
     - Relume sitemap import
     - Figma/Wix structure planning
   - Any change to IA must:
     - Update the sitemap file
     - Add a new dated log entry describing what changed and why

---

## 9. Next recommended steps

1. **Commit**:
   - `meztal_sitemap_final.xml`
   - This log file (`MEZTAL_SITEMAP_FINAL_LOG_2025-11-24.md`)

2. **Then**:
   - Use `meztal_sitemap_final.xml` + your 5000-character Relume prompt to generate the UX wireframes.
   - After Relume generates a sitemap/wireframe structure, run a **QA pass** against:
     - This log
     - `meztal_sitemap_final.xml`
   - Any discrepancy (missing hub, wrong Why Mexico nesting, Blog/Resources merged, etc.) should be documented in a new log and corrected BEFORE design work proceeds.

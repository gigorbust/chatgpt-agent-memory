# MezTal Canonical Source Index (READ THIS FIRST)

**Purpose:**  
This file defines the ONLY approved source documents and constraints for MezTal’s website IA/SEO/content work.  
Any ChatGPT/agent work on MezTal **must** treat this as the single source of truth for inputs and ignore older/unnamed SEO docs.

---

## 1. Canonical Non‑Negotiables (Global Rules)

- Brand: **MezTal** (do **not** use “FlexTal” in any new content).
- Positioning: US‑facing **nearshore staffing / augmented workforce solutions** provider.
- Delivery hubs: **Guadalajara and Mexico City** (always mentioned **together**).
- Value props:
  - ~**40% cost savings** vs equivalent US hires (not “50%”).
  - **Overlapping business hours with the US** (never say “same time zone”).
  - Strong English, cultural fit, long‑term dedicated teams.
- Canonical service label: **“Augmented Workforce Solutions”**.
  - Synonyms (staff augmentation, supplemental workforce, contingent workforce, temporary staffing, workforce solutions) = **on‑page language only**, not separate URLs.
- Blog vs Resources:
  - **Blog** = posts, news, updates, thought leadership.
  - **Resources** = case studies, comparisons, pricing explainer, deep guides/FAQs, tools.
  - They must **not** be merged into “Blog/Resources”.
- Locations:
  - Focus: **Guadalajara and Mexico City** as nearshore hubs.
  - Houston: **US office / HQ** page is allowed, but **not** the core value story.
  - **Cancún is deprecated**: `/locations/staffing-solutions-cancun` is a **redirect-only legacy URL**, not a live page.
- “Why” pages:
  - We must have **Why Mexico** plus **Why Guadalajara** (nested under Why Mexico) and content that also references Mexico City.
- No placeholders:
  - No “Other…”, “Misc…”, “Additional…”, “etc.” buckets.
  - Every IA node must be concrete and justified by these sources or explicit user instruction.

---

## 2. Canonical Data Files (ONLY THESE)

These are the **only files** future agents are allowed to treat as source data for MezTal IA/SEO/content.  
Older “Meztal_SEO_Master_Aggregation” / random exports are **deprecated** unless explicitly re‑authorized.

> Repo convention (recommended, not enforced):  
> Store all of them under `/data/` and reference exact filenames below.

### 2.1 Architecture & SEO Structure

**File:** `________ MEZTAL_SEO_MASTER_Minimal_2025-09-22_R3.xlsx`  
**Tab to use:** `Architecture — Cleaned Map` **only**  
**Role:**
- Master list of **Proposed URL**, **Topic Cluster**, and funnel stage.
- Primary source for:
  - Final sitemap URLs.
  - Cluster → pillar → spoke relationships.
  - Comparison vs services vs resources URL patterns.
- **Instructions:**
  - Treat this as the **canonical URL/cluster inventory**.
  - If there is any conflict between this sheet and older SEO docs, this sheet wins (unless overridden by the user in this repo’s logs).
  - Do **not** use any other tabs in this workbook without explicit user approval.

---

### 2.2 HubSpot Strategy & Copy

**File:** `MezTal HUBSPOT copilot seo chat session_.txt`  
**Role:**
- Long-form HubSpot AI chat export describing:
  - How to position MezTal by service and industry.
  - Topic clusters and example copy directions.
  - FAQ ideas, page-level messaging, and keyword angles.
- **Use for:**
  - Copy direction and messaging nuance for key pages.
  - Confirming which topics belong in **Resources** vs **Blog**.
- **Do not use for:**
  - New URL structures that contradict `Architecture — Cleaned Map`.
  - Inventing new services beyond what’s already agreed.

---

### 2.3 Revenue Reality (Closed‑Won Deals)

**File:** `Report of HubSpot Closed Won Report January 2023-August 2024 2.xlsx`  
**Role:**
- Actual closed‑won deals by:
  - Industry / vertical.
  - Role/title.
  - Deal/company type.
- **Use for:**
  - Prioritizing which **industries** and **role families** deserve pillar pages.
  - Validating that Accounting/Finance, HR/Talent, and IT/Data are truly core.
  - Guiding **case study** and **resource** topics (e.g., Senior Living, Healthcare, Real Estate, SaaS/Tech).
- **Never** override these signals with pure keyword volume alone.

---

### 2.4 LinkedIn Content (Content Themes)

**File:** `LinkedIn MezTal Content - meztal_content_1754583488887 2.xlsx`  
**Role:**
- Export of MezTal’s LinkedIn posts and content.
- **Use for:**
  - Deriving **Blog categories** and recurring themes:
    - Future of Work & AI
    - Nearshore & Talent Strategy
    - Senior Living / Healthcare / Aging industries
    - MezTal team & culture
    - Company news & events
  - Identifying which posts should be repurposed as:
    - Blog posts
    - News/Announcements
    - Social proof snippets.
- **Ignore completely:**
  - Any metrics/analytics tab; do **not** use likes/impressions as a primary signal.

---

### 2.5 Role / Job Reality (Workable)

**File:** `Workable Job Openings for KW Strategy - 8_20_25 .xlsx`  
**Role:**
- Snapshot of actual MezTal job openings by role.
- **Use for:**
  - Validating which **roles** MezTal actually hires for repeatedly.
  - Informing **Role page** templates (e.g., Hire Staff Accountant, Hire Data Engineer).
  - Checking that IA covers core role families (Accounting, HR, IT/Data, Customer Support, etc.).
- **Important:**
  - Legal entity may appear as “FlexTal Staffing LLC” in raw text; branding on the site must always be **MezTal**.
  - Treat this as **role signal**, not as copy to paste verbatim.

---

### 2.6 Fellou Output (Job Text Dump)

**Files:**
- `Fellou -- MezTal.docx`
- `Fellou -- MezTal.txt`  

**Role:**
- Misformatted but complete **job description text dump** (pasted from Workable).
- **Use for:**
  - Mining **responsibilities, requirements, and role language** to inform:
    - Role templates.
    - Service-page “Sample responsibilities” sections.
  - Cross-checking that the job families match HubSpot deals.
- **Do not use for:**
  - URL structure.
  - High-level IA decisions.
  - Naming the company “FlexTal” or similar.

---

### 2.7 Competitor Qualitative Notes

**File:** `MezTal Competitor Analysis - Expanded.docx`  
**Role:**
- Handwritten / narrative competitor analysis:
  - Which companies (Microsourcing, Emapta, Intugo, Near, Andela, BairesDev, etc.).
  - How they structure nav, “Why [Location]”, Industries, Resources, Careers.
- **Use for:**
  - **Structural inspiration** only:
    - Confirm we have: Why Mexico / Why Guadalajara, Industries, Solutions, Resources, Careers, etc.
    - Spot missing content types (e.g., case studies).
  - Identifying positioning opportunities (e.g., compliance, EOR content as guides).
- **Do NOT:**
  - Copy their offers.
  - Add services MezTal does not actually provide.

---

### 2.8 Competitor Structured List

**File:** `Report of Competitors.xlsx`  
**Role:**
- Tabular list of competitor companies, regions, and URLs.
- **Use for:**
  - Quick reference of who we’re benchmarking against.
  - Mapping which geos (Philippines, India, LatAm) are covered by which competitors.
- **Not for:**
  - Direct URL scraping inside this project.
  - Overriding MezTal’s service scope.

---

## 3. Canonical Log Files (GitHub)

These are the **primary historical logs** that must be respected before creating new ones.

1. **Wix/SEO Page Inventory + Hierarchy**  
   - `logs/COMET_ASSISTANT_meztal_seo_hierarchy_optimization_2025-11-17.md`  
   - Role:
     - Final audited list of **existing Wix pages** at that time.
     - Canonical decisions on:
       - URL fixes (`/apply-now`, `/faq`, etc.).
       - Parent/child page structure.
       - Geo phrasing constraints (Guadalajara + Mexico City, overlapping business hours).
       - Keyword cannibalization decisions (e.g., “Augmented Workforce Solutions” vs synonym pages).
   - **Rule:** Any new IA must not contradict the decisions recorded there unless explicitly superseded in a newer log.

2. **Later IA / Gap Logs**  
   - Any newer `logs/MEZTAL_*.md` you create (e.g., IA gap analysis, Relume prompt versions) should:
     - **Reference this Canonical Source Index file by name.**
     - Clearly mark which older logs they supersede (e.g., “Supersedes: COMET_ASSISTANT_… for URL structure only; keeps geo constraints”).

---

## 4. How Future Agents Should Use This File

1. **Read this file first.**  
   Before asking the user for uploads or starting new IA/SEO work, load and read this file.

2. **Do NOT re‑ask for these docs.**  
   If you must inspect the raw content:
   - Use the paths and filenames here.
   - Ask the user for a *specific* excerpt or a link to that file in GitHub, instead of “reupload everything”.

3. **Source Priority (if conflicts):**
   1. Explicit user instructions in this repo’s logs.
   2. `Architecture — Cleaned Map` tab in `________ MEZTAL_SEO_MASTER_Minimal_2025-09-22_R3.xlsx`.
   3. COMET SEO hierarchy log.
   4. HubSpot closed‑won + Workable roles.
   5. LinkedIn content themes.
   6. Competitor analysis (structure only).

4. **No new sources**  
   Do not introduce new SEO spreadsheets or random exports into the “canon” without:
   - Adding them to this file, and
   - Explicit user approval.

---

## 5. Deprecated / IGNORE

- Any file named like:
  - `Meztal_SEO_Master_Aggregation*.xlsx`
  - `Meztal_SEO_Master_Part*.xlsx`
  - `Meztal.com SEO Strategy Master Aggregation*.xlsx`
- Any log or doc that predates `________ MEZTAL_SEO_MASTER_Minimal_2025-09-22_R3.xlsx` **unless** this file explicitly tells you to use it.
- Any leftover mention of:
  - “FlexTal” as brand.
  - “Same time zone” vs. overlapping hours.
  - Location pages for **Cancún**.

These are legacy and must **not** influence current IA or content decisions.

---

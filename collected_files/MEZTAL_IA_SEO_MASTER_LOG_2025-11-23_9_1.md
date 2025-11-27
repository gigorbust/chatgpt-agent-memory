# MezTal IA + SEO Master Log (Canonical)

Last updated: 2025-11-23  
Owner: MezTal_IA_SEO_System (use this log as the *first* thing to read in any future session)

---

## 0. Purpose

This log is the **single source of truth** for MezTal’s website information architecture (IA), SEO structure, and page templates.

It exists so future ChatGPT sessions don’t waste tokens re‑discovering the same things or asking for the same files. If an assistant deviates from this log, it’s wrong.

This log does **not** restate every line of every spreadsheet (too large); instead it defines:
- Canonical constraints + rules
- Canonical files + what each is for
- Hubs, clusters, leaf types (IA)
- Required page templates for Relume/Wix
- Sitemap structure at the **pattern level** (what kinds of URLs we have and how they relate)

For individual keywords/rows, the **source spreadsheets remain canonical**.

---

## 1. Non‑Negotiable Rules

**Business reality**

- MezTal = US‑facing **nearshore staffing partner**.
- Builds **long‑term dedicated teams** in **Guadalajara and Mexico City**.
- Value props:
  - ~**40% cost savings** vs equivalent US hires.
  - **Overlapping business hours with the US** (never say “same time zone”).
  - Strong cultural fit and English‑proficient talent.

**Service clusters (functions)**

All IA/SEO must map back to these real offerings (no hallucinated services):

- Accounting & Finance (incl. SOX, GAAP, senior living accounting)
- IT / Data / Software Development / Nearshore IT Staffing
- Marketing & Creative
- HR / Talent / Augmented Workforce / RPO / Clinical Recruitment / Talent Sourcing
- Operations / Admin
- Customer Support / Call Center
- Workflow / Business Process Automation

**Geography constraints**

- Always reference **“Guadalajara and Mexico City”** together in core nearshore value copy.
- **Houston** is allowed only as:
  - US office / sales HQ / relationship hub.
  - Not as the “center” of the nearshore value proposition.
- **Cancun is banned**:
  - `/locations/staffing-solutions-cancun` is deprecated and must NOT appear in new IA or sitemap.
- “Why Guadalajara”:
  - Must exist as a distinct page.
  - Conceptually lives **under “Why Mexico”**.
  - Copy must still position Guadalajara and Mexico City together as dual hubs.

**Brand and naming**

- Legal entity may be FlexTal, but public brand is **MezTal** only.  
  → No “FlexTal” anywhere on the public site.
- Canonical service name: **“Augmented Workforce Solutions”**.
  - Synonyms (staff augmentation, supplemental workforce, contingent workforce, temporary staffing, workforce solutions) are **on‑page copy and H2/H3 only**, NOT separate URLs.

**Content types**

- **Blog** and **Resources** are always distinct nav hubs:
  - **Blog** = news, updates, thought leadership, opinion, LinkedIn‑style content.
  - **Resources** = case studies, comparisons, pricing explainers, deep guides/whitepapers, tools/checklists.
  - Do NOT merge them into “Blog/Resources” unless explicitly ordered.

**No placeholders**

- No “Other…”, “Misc…”, “Additional…”, “etc.” buckets.
- Every IA node must be a concrete page or template type.
- We can use CMS templates for repeating patterns (Roles, Case Studies, etc.), but those are explicit collections, not hand‑wavey buckets.

---

## 2. Canonical Files (Only These)

When rebuilding context, ALWAYS load these first:

1. `________ MEZTAL_SEO_MASTER_Minimal_2025-09-22_R3.xlsx`
   - Use **only** the tab: `Architecture — Cleaned Map`.
   - Columns: `Primary Keyword`, `Secondary Keywords`, `Topic Cluster`, `Proposed URL`, `Page Type`, `Content Type`, `Funnel Stage`, `Persona`.
   - This defines the **SEO target inventory**: comparison pages, guides, nearshore landers, industries, role pages, etc.
   - Some rows were known to be messy; treat this as **signal**, not infallible truth. Cross‑check with this log and later decisions.

2. `MezTal HUBSPOT copilot seo chat session_.txt` :contentReference[oaicite:0]{index=0}  
   - Contains **role clusters**, personas, and messaging patterns for:
     - AP/AR Specialist, FP&A/Finance Analyst, Accountant, Asset Manager,
       Data Analyst, Recruiter/HR, IT & Engineering, Marketing/Creative, Operations/Admin.
   - These inform **Role page** strategy + section content patterns.

3. `Report of HubSpot Closed Won Report January 2023-August 2024 2.xlsx`
   - Closed‑won deal data: confirms which industries/functions produce real revenue.
   - Priority verticals (from pattern): Senior Living & Post‑Acute, AgeTech/Elder Care Tech, Healthcare & Health Services, Financial Services, B2B SaaS/Tech, Real Estate/Property.

4. `LinkedIn MezTal Content - meztal_content_1754583488887 2.xlsx`
   - **Ignore metrics tab** entirely.
   - Use post content to derive **Blog categories**:
     - Nearshoring & Mexico talent strategy
     - Senior Living / Aging & Elder Care
     - MezTal team & culture
     - Thought leadership / hiring strategy
     - Events & conferences

5. `Workable Job Openings for KW Strategy - 8_20_25 .xlsx`
   - Real roles MezTal recruits for.
   - Use to:
     - Validate Role categories.
     - Inform copy for Careers & Role templates.

6. `Fellou -- MezTal.docx` + `Fellou -- MezTal.txt` :contentReference[oaicite:1]{index=1}  
   - Contains detailed IA decisions (e.g., how to handle blue rows 489–498 in Architecture sheet).
   - Confirms:
     - Creation of specific IT “Hire [Role] in Mexico” pages.
     - Decision to align URLs under **Nearshore IT Staffing** vs generic IT.
     - Positioning tweaks and SEO rationale.

7. `MezTal Competitor Analysis - Expanded.docx` :contentReference[oaicite:2]{index=2}  
   - Deep breakdown of category competitors (Microsourcing, Emapta, Intugo, Near, Andela, BairesDev, Crossover, etc.)
   - Use **only** for:
     - Structural inspiration (how they organize Solutions, Industries, Why‑location, Resources, Careers).
     - Identifying **missing patterns** (e.g., “How it works / Our Model”, “Engagement Models”, robust Why‑location content).
   - Never invent offerings MezTal doesn’t have just to match them.

8. `Report of Competitors.xlsx`
   - Structured competitor list (offshore vs nearshore, geos, sites).
   - Use to cross‑check patterns from the expanded analysis doc.

9. Prior COMET/Wix IA logs (pasted in this chat)
   - Especially the log that details 40+ static pages, URL fixes, and the introduction of `Software Development`, `Web Development`, `App Development`, `Augmented Workforce Solutions`, `Outsourced Human Relations Support`, `Nearshore for Elder Care Technology`, etc.

---

## 3. IA Model (Hubs → Clusters → Leafs)

We use a **hub / cluster / leaf** model.

### 3.1 Hubs (Top Level)

These must exist as primary sections:

- `/` – **Home**
- `/solutions` – **Hire Talent (Solutions Hub)**
- `/industries` – **Industries Hub**
- `/why-mexico` – **Why Mexico Hub**
- `/resources` – **Resources Hub** (guides, comparisons, tools, case studies)
- `/blog` – **Blog Hub** (thought leadership & news)
- `/company` – **Company Hub**
- `/contact` – **Contact**
- `/careers` – **Careers / Apply**
- `/legal` – **Legal** (Terms, Privacy Policy, etc.)

### 3.2 Core Clusters (under hubs)

**Solutions / Hire Talent (`/solutions`):**

- `/solutions/it-staffing-development` (Nearshore IT & Engineering)
- `/solutions/software-development` (parent)
  - `/software-development/web-development`
  - `/software-development/app-development`
- `/solutions/call-center-outsourcing`
- `/solutions/finance-accounting-outsourcing`
- `/solutions/accounting-finance` (cluster parent)
  - `/accounting-finance/accounting-outsourcing`
  - `/accounting-finance/payroll-outsourcing`
  - `/accounting-finance/tax-services`
  - `/accounting-finance/accounting-services`
- `/solutions/hr-talent-acquisition` (parent)
  - `/solutions/hr-talent-acquisition/augmented-workforce` (canonical Augmented Workforce Solutions)
  - `/solutions/hr-talent-acquisition/human-relations-support`
  - `/solutions/hr-talent-acquisition/talent-sourcing`
  - `/solutions/hr-talent-acquisition/clinical-recruitment`
  - `/solutions/hr-talent-acquisition/senior-living-rpo`
- `/solutions/digital-marketing`
- `/solutions/administrative-outsourcing`
- `/solutions/design-outsourcing`
- `/solutions/workflow-automation`
  - `/solutions/workflow-automation/outsourcing`
- `/solutions/sales-solutions` (sales support / SDR, etc.)
- Legacy `/services` URL can exist as a **redirected landing index** if needed for SEO hygiene.

**Industries (`/industries`):**

- `/industries/senior-living` (Nearshore for Senior Living)
  - `/industries/senior-living/accounting`
- `/industries/agetech`
  - `/industries/agetech/software-development`
  - `/industries/agetech/elder-care-tech`
- `/industries/financial-services` (for SOX, GAAP, etc.)
- `/industries/healthcare` (if supported by closed‑won data)
- `/industries/saas-tech` or `/industries/technology` (B2B SaaS/Tech)
- `/industries/real-estate-property`

**Why Mexico (`/why-mexico`):**

- `/why-mexico` – main hub (why Mexico nearshoring, Guadalajara *and* Mexico City, overlapping business hours, talent pool, cost).
- `/why-mexico/guadalajara` – “Why Guadalajara”
- `/why-mexico/mexico-city` – “Why Mexico City”

**Company (`/company`):**

- `/company/about`
- `/company/team`
- `/company/locations`
  - `/company/locations/houston` (US office / HQ page)
- `/company/linkedin-hub` (LinkedIn content hub / embed)
- `/company/workable-jobs` (Workable jobs hub + embed)
- `/company/testimonials` (optional, or handled via CMS)

**Geographic / Nearshore SEO Landers (standalone):**

- `/nearshore-staffing-mexico`
- `/remote-workers-mexico`
- `/mexico-outsourcing`
- `/remote-teams-mexico`
- `/employer-of-record-mexico`
- `/nearshore-it-staffing/nearshoring-software-development`

**Comparison & Foundational SEO (`/comparison`) – from Architecture sheet:**

Under `/comparison/…`:

- `/comparison/payroll-company`
- `/comparison/best-it-staffing-companies`
- `/comparison/business-outsourcing`
- `/comparison/development-company`
- `/comparison/offshore-accounting`
- `/comparison/offshore-companies`
- `/comparison/offshore-it`
- `/comparison/staff-augmentation-firm` (for comparison intent; still on‑page we anchor “Augmented Workforce Solutions” as MezTal service)
- `/comparison/best-it-staffing-agencies`
- `/comparison/offshoring`
- `/comparison/cost-of-living-in-guadalajara-vs-mexico-city`
- `/comparison/best-recruitment-agencies`
- `/comparison/executive-recruiting-firms`
- `/comparison/offshore-recruitment`
- `/comparison/recruiting-firms`
- `/comparison/custom-software-development-company`
- `/comparison/it-company`
- `/comparison/it-recruiting-firms`
- `/comparison/it-services-near-me`
- `/comparison/it-staffing-agencies-near-me`
- `/comparison/software-house`
- `/comparison/software-outsourcing-company`
- `/comparison/nearshoring-vs-offshoring`
- `/comparison/staff-augmentation-vs-managed-services`

**Resources (`/resources`) – Guides, Whitepapers, Tools:**

- Mirrors many comparison topics but framed as guides:
  - `/resources/best-it-staffing-companies`
  - `/resources/business-outsourcing`
  - `/resources/development-company`
  - `/resources/staff-augmentation-firm`
  - `/resources/best-it-staffing-agencies`
  - `/resources/peo`
  - `/resources/best-recruitment-agencies`
  - `/resources/executive-recruiting-firms`
  - `/resources/talent-acquisition`
  - `/resources/custom-software-development-company`
  - `/resources/it-company`
  - `/resources/it-recruiting-firms`
  - `/resources/it-services-near-me`
  - `/resources/it-staffing-agencies-near-me`
  - `/resources/software-house`
  - `/resources/software-outsourcing-company`
- Accounting/Compliance:
  - `/resources/sarbanes-oxley-compliance-outsourcing`
  - `/resources/us-gaap-for-nearshore-accounting-teams`
- Nearshore strategy:
  - `/resources/nearshoring-vs-offshoring` (guide version)
  - `/resources/how-to-hire-developers-in-mexico`
  - `/resources/how-to-manage-a-nearshore-team`
- Generic high‑value:
  - `/resources/gartner-magic-quadrant-for-it-services`
  - `/resources/mexico-s-silicon-valley`
  - `/resources/software-engineering`

**Role / Hire pages (pattern):**

Parent: **Nearshore IT Staffing** (or equivalent IT cluster; see Fellou doc) :contentReference[oaicite:3]{index=3}  

Pattern:

- `/nearshore-it-staffing/hire-data-governance-engineer`
- `/nearshore-it-staffing/hire-azure-data-engineer`
- `/nearshore-it-staffing/hire-databricks-engineer`
- `/nearshore-it-staffing/hire-business-analyst`
- `/nearshore-it-staffing/hire-oracle-hyperion-developer`

Additional roles (from HubSpot copilot + Workable + Architecture sheet) should map into **Role CMS** and reuse the same template, e.g.:

- `/roles/ap-ar-specialist`
- `/roles/fpa-analyst`
- `/roles/accountant`
- `/roles/asset-manager`
- `/roles/data-analyst`
- `/roles/recruiter`
- `/roles/it-engineer`
- `/roles/marketing-specialist`
- `/roles/operations-admin`
- etc.

**Utility / Trust:**

- `/contact` (form; strong CTA)
- `/careers` (candidate‑facing; Workable embed; can absorb prior `apply-now` and `career page`)
- `/faq`
- `/pricing` (pricing model + 40% savings vs US; explain passthrough fee)
- `/legal/privacy-policy`
- `/legal/terms-of-use`

---

## 4. Page Templates for Relume (Critical)

Relume must create **one template per page type**. Templates can be reused across many URLs but must exist distinctly.

At minimum:

1. **Home Template**
   - Hero, core value prop, “How it works”, key solutions, key industries, nearshore Mexico (Guadalajara and Mexico City), testimonials, CTAs.

2. **Solutions Hub Template** (`/solutions`)
   - Grid of solution clusters + high‑level filters by function (Accounting & Finance, IT/Data, Marketing & Creative, HR/Talent, Ops/Admin, Call Center).

3. **Solution Detail Template** (reused for all `/solutions/*` and `/accounting-finance/*`)
   - Hero (solution name + value).
   - Pain points & outcomes.
   - “How it works” / engagement model.
   - Roles you can hire via this solution.
   - Industries served.
   - Why Mexico (Guadalajara and Mexico City, overlapping business hours, ~40% savings).
   - FAQs.
   - CTA to Contact / Book a consult.

4. **Software Development Cluster Template** (parent)  
   - For `/software-development`, with sub‑sections linking to Web Dev, App Dev, Hire Developers in Mexico, Nearshore Software Development.

5. **Industry Hub Template** (`/industries`)
   - Cards for Senior Living, AgeTech, Financial Services, Healthcare, SaaS/Tech, Real Estate, etc.

6. **Industry Detail Template**
   - Used by all `/industries/*` leaf pages:
     - Senior Living, AgeTech, Elder Care Tech, Financial Services, etc.
   - Structure:
     - Industry‑specific pains, use cases, and proof.
     - Relevant functions (Accounting, IT, HR, Ops, Call Center).
     - Relevant role examples.
     - Case studies / resources.
     - CTA.

7. **Geographic / Why Mexico Hub Template** (`/why-mexico`)
   - Story of Mexico as nearshore hub; benefits, cost, cultural alignment, overlapping hours.
   - Links to city pages.

8. **City Detail Template**
   - Used for:
     - `/why-mexico/guadalajara`
     - `/why-mexico/mexico-city`
   - Each has:
     - Talent profile, universities, infrastructure, sample roles, cost advantages vs US.
     - Both must still anchor the *dual‑hub* narrative.

9. **Location Listing Template**
   - `/company/locations` listing Houston + Mexico hubs.

10. **Houston Location Template**
    - `/company/locations/houston` – focus on HQ/office, trust, not as nearshore value anchor.

11. **Comparison Page Template** (`/comparison/*`)
    - Side‑by‑side matrices, pros/cons, when to choose MezTal vs X.
    - Strong CTA segments.
    - SEO‑friendly FAQ.

12. **Resource Guide / Whitepaper Template** (`/resources/*`)
    - Long‑form guide structure (TOC, scannable sections, inline CTAs).
    - Used for GAAP/SOX, how‑to‑hire, how‑to‑manage, etc.

13. **Case Study Template** (CMS)
    - `/case-studies/[slug]` (or via Resources CMS).
    - Problem → Approach → Results; industry, function, roles, location.

14. **Blog Hub + Post Templates**
    - `/blog` hub (filters by category).
    - `/blog/[slug]` post layout, with related posts, crosslink to Solutions & Industries.

15. **Role Detail Template** (CMS)
    - For `/nearshore-it-staffing/hire-[role]` and/or `/roles/[slug]`.
    - Sections:
      - What this role does.
      - Why hire it in Guadalajara and Mexico City.
      - Example profiles / responsibilities.
      - Industry‑specific use cases.
      - Hiring process and SLA.
      - FAQ + CTA.

16. **Careers / Workable Template**
    - `/careers` with Workable job listing embed + “Why work at MezTal” + culture content.

17. **LinkedIn Hub Template**
    - `/company/linkedin-hub` with embedded LinkedIn feed + category context (how to use posts).

18. **Contact Template**
    - `/contact` with form, contact info, simple “Book a Consult” flow; global trust signals.

19. **Company Template**
    - Reused for `/company/about`, `/company/team` (with team CMS), etc.

20. **Legal Template**
    - For `/legal/*`.

These templates are what Relume must generate. Sitemap depth and SEO specifics then plug into these.

---

## 5. Navigation Strategy (For Relume / Wix)

**Home header nav (simplified, top‑of‑funnel):**

- Logo
- Home
- Hire Talent (links to `/solutions`)
- Industries
- Why Mexico
- Contact
- [Button] **Book a Consult**
- Text link: Careers (goes to `/careers`)
- Blog/Resources can live in footer + contextual links on page.

**Deep pages (SEO landers, role pages, resources, blog posts):**

- Home
- Hire Talent
- Industries
- Why Mexico
- Resources
- Blog
- Company
- Contact
- Careers (text link)
- [Button] Book a Consult

**Careers / candidate‑facing pages:**

- Logo
- Careers
- About
- Team
- Blog
- Contact

All of this should be explicitly described in the 5000‑char Relume prompt.

---

## 6. Known Deprecated / Redirect Needs

- `/locations/staffing-solutions-cancun` → **deprecated** (no new equivalent; 404 or redirect to `/why-mexico` if absolutely needed).
- Old `/blank-*` placeholders → map to real pages or 301 to the closest hub.
- `/services` → may 301 to `/solutions` or act as a thin index page (for SEO hygiene).

---

## 7. How Future Assistants Must Use This Log

1. Load this log first.
2. Load all canonical files listed in §2.
3. When asked to adjust IA/SEO:
   - Do **not** invent services or cities.
   - Do **not** merge Blog & Resources.
   - Respect the “Augmented Workforce Solutions” rule.
   - Respect the Mexico + Guadalajara + Mexico City + Houston constraints.
4. If relume prompt needs updating:
   - Adjust nav, templates, or clusters **here first**, then re‑boil into a 5000‑character prompt.

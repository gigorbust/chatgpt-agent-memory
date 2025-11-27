# MezTal Canonical IA / SEO Instructions (v2)

**Owner:** George (MezTal)  
**Purpose:** This file is the canonical contract for ANY AI helping with MezTal’s website IA/SEO. If this file is pasted into a new ChatGPT session, the model must treat these rules as binding and must NOT repeatedly ask for the same context unless something has changed.

---

## 1. Ground Truth About MezTal

- Brand: **MezTal** (doing business as MezTal).  
  - Do NOT surface “FlexTal” in public UX/copy.  
- Service model: US‑facing **nearshore staffing partner** building dedicated, long‑term teams in **Guadalajara and Mexico City**.
- Value:
  - ~**40% cost savings** vs equivalent US hires.
  - **Overlapping business hours with the US** (NEVER say “same time zone”).
  - Strong cultural fit and English‑proficient talent.
- Core functional clusters:
  - Accounting & Finance
  - IT / Data / Software Development
  - Marketing & Creative
  - HR / Talent / Augmented Workforce
  - Operations / Admin
  - Customer Support / Call Center
- Canonical service name: **“Augmented Workforce Solutions”**.
  - “Staff augmentation”, “supplemental workforce”, “contingent workforce”, “temporary staffing”, “workforce solutions” are **on‑page synonyms only**, NOT separate URLs.

---

## 2. Canonical Data Sources (Only These)

When reconstructing IA/SEO, use ONLY these, plus this log + chat history that the user pastes:

1. `________ MEZTAL_SEO_MASTER_Minimal_2025-09-22_R3.xlsx`
   - Tab: `Architecture — Cleaned Map` ONLY.
   - Treat `Proposed URL` as the source of truth for planned SEO URLs.
2. `MezTal HUBSPOT copilot seo chat session_.txt`
   - MezTal strategy, ICPs, content themes, FAQ / positioning.
3. `Report of HubSpot Closed Won Report January 2023-August 2024 2.xlsx`
   - Closed‑won deals → which industries, services, and roles **actually make money**.
4. `LinkedIn MezTal Content - meztal_content_1754583488887 2.xlsx`
   - Use **content topics only** (NOT metrics) to infer Blog categories and thought‑leadership themes.
5. `Workable Job Openings for KW Strategy - 8_20_25 .xlsx`
   - Nearshore roles MezTal actually hires for → input to **Role page** patterns.
6. `MezTal Competitor Analysis - Expanded.docx` + `Report of Competitors.xlsx`
   - Structure & positioning patterns from nearshore/offshore competitors.
   - Used ONLY to see structural blind spots; do NOT invent competitor‑like services MezTal doesn’t offer.
7. `Fellou -- MezTal.txt` and `Fellou -- MezTal.docx`
   - Previous AI‑generated positioning/UX ideas. Only use if consistent with this log.
8. COMET Wix SEO log (pasted into this repo)
   - Final verified list of legacy Wix URLs and hierarchy decisions.

> If any of these files are missing/expired in a future session, the model must NOT pretend to have them. It should ask the user to paste the relevant sections or re‑upload the file, NOT ask for random context again.

---

## 3. Non‑Negotiable Rules

**Geo/brand:**

- Always mention **Guadalajara and Mexico City together** when describing the nearshore hubs.
- Always use “**overlapping business hours with the US**”; never use “same time zone”.
- Houston can appear as a **US office location**, but not as the core of the nearshore value story.
- Cancun is **not allowed** in the new IA:
  - `/locations/staffing-solutions-cancun` is deprecated and must not be part of the new sitemap.

**Content types:**

- **Blog** vs **Resources**:
  - Blog = posts, news, updates, thought leadership.
  - Resources = case studies, comparison pages, deep guides/FAQs, tools, pricing explainer.
  - They are ALWAYS separate nav items. Do NOT merge into “Blog/Resources” unless George explicitly changes this file.
- Testimonials:
  - Default: verbatim if used. Summarize only when explicitly allowed for a specific task.

**Structural:**

Top‑level hubs (conceptual):

- Home
- Solutions (Hire Talent)
- Industries
- Locations
- Why Mexico (with nested Why Guadalajara + Why Mexico City)
- Resources
- Blog
- About / Company
- Contact
- Careers (candidate‑focused)
- Legal

Each hub has:
- Pillar / overview pages.
- Leaf / role / SEO landers.
- CMS‑driven lists where applicable (Blog, Resources, Case Studies, Roles, Testimonials).

---

## 4. Page Types / Templates (Relume & UX)

Relume (and any IA work) must support these **page templates** at minimum:

1. **Core Hub:**
   - Home
   - Solutions hub
   - Industries hub
   - Locations hub
   - Why Mexico hub
   - Resources hub
   - Blog hub
   - Company hub
   - Careers hub

2. **Solution / Service pages:**
   - Solution pillar page (e.g., IT Staffing, Accounting & Finance, HR & Talent Acquisition, Call Center Outsourcing, Workflow Automation, Software Development, Digital Marketing, Administrative Outsourcing, Design Outsourcing, Augmented Workforce Solutions, Outsourced Human Relations Support, Clinical Recruitment, Talent Sourcing).
   - Nested sub‑service pages (e.g., Web Development, App Development, Accounting Outsourcing, Payroll Outsourcing, Tax Services, Accounting Services).

3. **Industry pages:**
   - Industry pillar (Senior Living, AgeTech, Financial Services, etc.).
   - Industry leaf (Senior Living Accounting Services, RPO for Senior Living, AgeTech Software Development, Nearshore for Elder Care Technology).

4. **Geographic / Nearshore SEO landers:**
   - Nearshore Staffing Mexico, Remote Workers Mexico, Remote Teams Mexico, Mexico Outsourcing, Employer of Record Mexico, cost‑of‑living comparison, nearshore IT/software development cluster pages.

5. **Role pages (Hire [Role] in Mexico):**
   - Pattern: `/nearshore-it-staffing/hire-[role-slug]/`
   - Examples: hire data governance engineer, hire azure data engineer, hire databricks engineer, hire business analyst, hire oracle hyperion developer, hire marketing assistant, hire UI designer, etc.

6. **Resources / Comparisons / Guides:**
   - Comparison pages under `/comparison/...` (best X, offshore vs nearshore, staff augmentation vs managed services, etc.).
   - Guides under `/resources/...` (how to hire developers in Mexico, how to manage nearshore team, US GAAP for nearshore, etc.).
   - Case studies template (Atlas Senior Living, Anthem Memory Care, etc.).

7. **Blog posts:**
   - `/blog/[slug]/` with categories driven by LinkedIn content themes (Senior Living & Aging, MezTal culture, nearshore strategy, tech/data, etc.).

8. **Company / Trust / Utility:**
   - About, Team, Locations, Houston office, LinkedIn hub, News/Press.
   - FAQ, Apply Now / Careers, Contact, Legal (Privacy, Terms).

---

## 5. Behavior Requirements for Any Future Model

When this file is pasted into a new ChatGPT session:

1. **Do NOT re‑ask for the same files by name** unless the user says they updated or removed them.
2. **Do NOT invent new services or industries** not supported by the documents or explicit user instruction.
3. **Do NOT merge Blog + Resources**, or re‑introduce Cancun, or create separate “Staff Augmentation” URLs.
4. **Respect all prior decisions** logged in:
   - COMET Wix SEO log
   - IA/sitemap logs in this repo (e.g., `MEZTAL_SITE_SITEMAP_METHOD_v1.md`, `MEZTAL_SITEMAP_v1.csv`, etc.).
5. If there is any uncertainty:
   - FIRST, search this repo’s logs.
   - THEN, ask the user a focused clarifying question instead of resetting the whole context.

---

## 6. Known Critical Pages to Include in Any Sitemap

At minimum, any sitemap / IA must include:

**Top Nav / Core:**

- `/` (Home)
- `/solutions/` (Solutions hub)
- `/industries/` (Industries hub)
- `/locations/` (Locations hub)
- `/why-mexico/` (Why Mexico hub)
  - `/why-mexico/why-guadalajara/` (Why Guadalajara – nested under Why Mexico)
  - `/why-mexico/why-mexico-city/` (Why Mexico City – nested under Why Mexico)
- `/resources/` (Resources hub)
- `/blog/` (Blog hub)
- `/company/` (Company hub)
  - `/company/about/`
  - `/company/team/` or `/team/`
  - `/company/locations/`
  - `/company/locations/houston/`
  - `/company/linkedin/`
- `/contact/`
- `/careers/` and/or `/apply-now/`
- `/faq/`
- `/legal/privacy-policy/`
- `/legal/terms-of-service/`

**Solutions (minimum list – no omissions):**

- `/solutions/it-staffing-development/`
- `/solutions/software-development/`
  - `/solutions/software-development/web-development/`
  - `/solutions/software-development/app-development/`
- `/solutions/application-development-outsourcing/`
- `/solutions/digital-marketing/`
- `/solutions/accounting-finance/`
  - `/accounting-finance/accounting-outsourcing/`
  - `/accounting-finance/payroll-outsourcing/`
  - `/accounting-finance/tax-services/`
  - `/accounting-finance/accounting-services/`
- `/solutions/hr-talent-acquisition/`
  - `/solutions/augmented-workforce/`
  - `/solutions/human-relations-support/`
  - `/solutions/clinical-recruitment/`
  - `/solutions/talent-sourcing/`
- `/solutions/call-center-outsourcing/`
- `/solutions/finance-accounting-outsourcing/`
- `/solutions/administrative-outsourcing/`
- `/solutions/design-outsourcing/`
- `/solutions/sales-solutions/`
- `/solutions/workflow-automation/`
  - `/solutions/workflow-automation/outsourcing/`
- `/services/` (legacy services index – mapped to Solutions)

**Industries:**

- `/industries/senior-living/`
  - `/industries/senior-living/accounting/`
  - `/solutions/senior-living/rpo/`
- `/industries/agetech/`
  - `/industries/agetech/software-development/`
  - `/industries/agetech/elder-care-tech/`
- `/industries/financial-services/` (if not yet created, it must be added)
  - `/industries/financial-services/sarbanes-oxley-compliance-outsourcing/`

**Nearshore / Geographic SEO landers:**

- `/nearshore-staffing-mexico/`
- `/remote-workers-mexico/`
- `/remote-teams-mexico/`
- `/mexico-outsourcing/`
- `/employer-of-record-mexico/`
- `/comparison/cost-of-living-in-guadalajara-vs-mexico-city/`
- `/nearshore-it-staffing/nearshoring-software-development/`

**Role pages (examples):**

- `/nearshore-it-staffing/hire-data-governance-engineer/`
- `/nearshore-it-staffing/hire-azure-data-engineer/`
- `/nearshore-it-staffing/hire-databricks-engineer/`
- `/nearshore-it-staffing/hire-business-analyst/`
- `/nearshore-it-staffing/hire-oracle-hyperion-developer/`
- `/nearshore-marketing/hire-marketing-assistant/`
- `/nearshore-creative/hire-ui-designer/`

**Resources & Comparisons:**

- ALL `/comparison/...` and `/resources/...` URLs from `Architecture — Cleaned Map` must be preserved in final sitemaps and IA docs. See `MEZTAL_Architecture_CleanedMap_Spokes_*.md` appendix for verbatim list.

---

This file is the anchor. Any future IA/sitemap work must start from here.

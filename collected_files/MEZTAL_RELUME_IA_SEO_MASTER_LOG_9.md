---

# 🧠 MezTal Relume IA/SEO Master Log

> Canonical record of info architecture, SEO strategy, and Relume prompt design for MezTal.com

---

## 0. Meta

**Project:** MezTal Website Rebuild (Relume → Webflow/Wix)
**Owner:** George (Silent Storm)
**Assistant mode:** `MezTal_Expert_Mode` (GPT‑5)
**Goal:** Design a **fresh, SEO‑driven, conversion‑focused** site architecture and Relume prompt that:

* Aligns with real revenue/HubSpot/SEO data
* Respects COMET zero‑tolerance documentation rules
* Separates Blog vs Resources
* Uses Mexico nearshore positioning correctly
* Is scalable & CMS‑driven (50+ pages without chaos)

---

## 1. MezTal Ground Truth (Brand & Positioning)

### 1.1 What MezTal is

* US‑facing **nearshore staffing partner**.
* Builds **dedicated, long‑term teams** in Mexico (not gig/short‑term outsourcing).
* Delivery hubs: **Guadalajara and Mexico City**

  * These must **always be mentioned together** when describing delivery locations.

### 1.2 Value Proposition

* ~**40% cost savings** vs equivalent US hires (updated from earlier 50%).
* Teams work in **overlapping business hours with the US**.

  * ❌ Never use “same time zone”.
* Strong cultural alignment and English proficiency.
* Clients:

  * **You make the hiring decisions**
  * **You train on your processes**
  * **You control the systems**
* MezTal handles:

  * HR
  * Payroll
  * Office setup
  * IT, equipment
  * Recruiting
  * Compliance

### 1.3 Functional Clusters (Service “Families”)

These functions recur in HubSpot, LinkedIn, Workable, and existing site:

* **Accounting & Finance**
* **IT / Data / Software Development**
* **Digital Marketing & Creative**
* **HR, Talent & Augmented Workforce**
* **Operations / Admin / Back‑Office**
* **Customer Support / Call Center**

Design & Sales appear as smaller satellites and should only be treated as separate clusters when the data explicitly supports them.

### 1.4 Primary ICPs & Vertical Focus

**Personas** (from HubSpot & SEO table):

* CFO, Controller, VP Finance
* COO, Head of Operations
* CIO, CTO, VP of Engineering, IT Director, Head of Data
* CHRO, HR Director, Head of Talent/People
* Founder/CEO in some cases

**Verticals**:

* Senior Living & Post‑Acute
* AgeTech
* Elder Care Technology (distinct from AgeTech at large)
* Healthcare & Health Services
* B2B SaaS/Tech
* Real Estate & Property Management
* Some Financial Services (e.g., SOX, US GAAP content)

---

## 2. Canonical Sources & Files

These are the **authoritative sources** you referenced during this work. Many have expired in this environment, so you’ll need to re‑upload them in future sessions if you want the model to see them again.

### 2.1 Text / Links explicitly used

* **COMET SEO Hierarchy GitHub Log** (pasted in full)

  * `COMET_ASSISTANT_meztal_seo_hierarchy_optimization_2025-11-17.md`
  * Contains:

    * Full Wix static-page inventory (51 static + 13 dynamic templates)
    * Parent/URL/meta corrections
    * Geographic/meta rules (Guadalajara, Mexico City, overlapping business hours)
    * Newly created pages:

      * Software Development, Web Development, App Development
      * Augmented Workforce Solutions
      * Outsourced Human Relations Support
      * Nearshore for Elder Care Technology
    * Cannibalization decisions (e.g., deleting Supplemental Workforce Staffing as a separate URL)
* **Current Meztal.com content (hand‑extracted)**

  * Home page (hero, “You make the hiring decisions…” etc., testimonials, employee quote, CTA)
  * Meet Our Team page
  * FAQ page (Why Guadalajara, cost, passthrough fee, control)
  * Contact page (form, phone, email)
* **Old Relume‑generated structure** (pasted)

  * Pages like:

    * Home, About Us, Services, Team, Savings, Management, Staffing
    * Testimonials, Client Testimonial, Why Guadalajara? (with Benefits, Cost, Location subpages)
    * Contact, Blog, Blog Post, Careers, FAQs, Pricing, Legal
  * Used as a starting but **not authoritative** IA pattern.
* **SEO Mapping Table (pasted)**

  * Columns: `Primary Keyword | Secondary Keywords | Topic Cluster | Proposed URL | Page Type | Content Type | Funnel Stage | Persona`
  * Key clusters: Comparison, Foundational Solutions, Accounting Solutions, IT Staffing, HR Solutions, Nearshore Accounting, Nearshore IT Staffing, Senior Living, AgeTech, etc.
  * Includes:

    * Comparison pages like `/comparison/best-it-staffing-companies`, `/comparison/offshore-accounting`, `/comparison/staff-augmentation-firm`
    * Guides and resources under `/resources/...`
    * Service/commercial pages under `/services/...`
    * Industry and solution pages under `/industries/...` and `/solutions/...`
    * Role‑level pages (hire Azure data engineer, hire business analyst, hire marketing assistant, hire UI designer, hire data governance engineer, etc.)
* **Self‑prompt definition** (`MezTal_Expert_Mode`)

  * All constraints about:

    * Geography language
    * Canonical Augmented Workforce Solutions
    * Blog vs Resources separation
    * Hub → Cluster → Leaf structure
    * Funnel‑aware navigation
    * Zero tolerance for placeholders / vague buckets
    * No speculative services/industries
    * Behavior as ruthless mentor

### 2.2 Uploaded files referenced by name

These **were uploaded** in this session. Some are now expired in tools, so re‑upload if needed:

* `Report of HubSpot Closed Won Report January 2023-August 2024.xlsx`
* `MezTal HubSpot-Informed SEO.xlsx`
* `Silent Storm MezTal doc aggregate.xlsx`
* `Meztal_SEO_Master_Part3.xlsx`
* `Copy of Meztal_SEO_Master_Part3 (locked, without dupes from part 1 and 2).xlsx`
* `MezTal HUBSPOT copilot seo chat session: 9.3.25.docx`
* `MezTal HUBSPOT copilot seo chat session_9.3.25.docx`
* `MezTal HUBSPOT copilot seo chat session_9.3.25.pdf`
* `LinkedIn MezTal Content - meztal_content_1754583488887.xlsx`

> **Note:** In this environment, many of these were **not fully readable** via tools (e.g., “not accessible with myfiles_browser” or expired). Most of the IA/SEO logic that refers to them comes from:
>
> * Your descriptions (e.g., “Architecture — Cleaned Map” tab)
> * Pasted excerpts (e.g., SEO mapping table)
>   rather than direct parsing of the xlsx/docx.

You should treat these filenames as your **canonical list to re‑upload** when needed.

---

## 3. Hard Global Rules (We Enforced)

### 3.1 Geography & Messaging

* Always say **“Guadalajara and Mexico City”** when referencing delivery locations.
* Always use **“overlapping business hours with the US”**.
* Never use **“same time zone”**.
* Houston may be referenced as a **US office**, not the core of the nearshore value proposition.

### 3.2 Canonical Augmented Workforce Solutions

* Single canonical page: **`/solutions/augmented-workforce/`**.
* Synonyms like:

  * staff augmentation
  * supplemental workforce staffing
  * contingent workforce
  * temporary staffing
  * workforce solutions
    are **on‑page headings/keywords**, not separate URLs.
* Reason: avoid SEO cannibalization and fragmented equity.

### 3.3 Blog vs Resources

Non‑negotiable separation:

* **Blog**

  * Chronological posts (news, updates, thought leadership, repurposed LinkedIn content).
  * Categories mapped to service clusters and industries.
  * NOT the home for case studies or comparison pages.

* **Resources**

  * Evaluation / proof / deep‑dive assets:

    * Case Studies
    * Comparison pages (best X companies, nearshoring vs offshoring, staff augmentation vs managed services, etc.)
    * Pricing/cost explainers
    * Whitepapers/guides (e.g., US GAAP for nearshore teams; SOX compliance outsourcing; how to hire developers in Mexico)
    * Buyer FAQ library
    * Tools/checklists/calculators
  * CMS‑driven; sits closer to BOFU than Blog.

* Never call anything “Blog/Resources”; never merge them.

### 3.4 Zero Placeholders / No Lazy Buckets

We obey COMET’s strict rules:

* No “Other Services”, “More Industries”, “Misc”, “etc.”, “and more”.
* No generic catch‑alls like “Other Operations‑Intensive Industries” unless we enumerate which ones.
* Every node in IA has a clear, named purpose.

### 3.5 No Speculative Offerings

* We **do not introduce** new industries, services, or roles just because they’re common in B2B.
* Everything must be grounded in:

  * COMET/Wix log
  * Architecture — Cleaned Map
  * HubSpot/SEO table
  * LinkedIn content
  * Workable roles
  * Or explicit instructions from you.
* If we float a speculative idea, we mark it **OPTIONAL/FUTURE** and keep it out of core IA.

---

## 4. Navigation Strategy (Funnel‑Aware)

We defined **nav variants** to match funnel stage and page type.

### 4.1 Core Hubs

Top‑level conceptual hubs:

* Home
* Hire Talent (Solutions)
* Industries
* Why Mexico
* Resources
* Blog
* Company
* Contact
* Careers (candidate‑focused, secondary)

### 4.2 Nav Variant A – Home (Focused Conversion Nav)

Used on: **Home page only**.

* Items:

  * Logo (Home)
  * Solutions (Hire Talent)
  * Industries
  * Why Mexico
  * Contact
* CTAs:

  * Primary: **“Book a Consult”** (button)
  * Secondary: **Careers** (small text link, visually subordinate)
* Blog and Resources:

  * Available in footer or sections, but **not dominant** in the header.

**Goal:**
Make it brutally obvious what MezTal does and where to go next (Solutions/Industries/Why Mexico/Contact) for cold traffic.

### 4.3 Nav Variant B – Full Nav (Context Nav)

Used on:

* Solutions hub, cluster pages, role pages
* Industries hub + vertical pages
* Why Mexico pillar + all nearshore/geo SEO pages
* Resources hub + all case studies, comparisons, guides
* Blog hub + posts
* Company pages (About, Team, Locations, LinkedIn Hub, Testimonials)
* Contact

Items:

* Home
* Solutions
* Industries
* Why Mexico
* Resources
* Blog
* Company
* Contact
* Careers (small text link)
* Primary CTA: **“Book a Consult”**

**Goal:**
If a visitor lands deep (via SEO, referrals, social), they see **full context** and multiple high‑intent paths (Solutions, Industries, Resources, Contact).

### 4.4 Nav Variant C – Candidate Nav (Careers / Jobs)

Used on:

* Careers hub
* Role/job postings (if surfaced)
* Candidate FAQ pages

Items (example):

* Logo (Home)
* Careers
* About
* Team
* Blog
* Contact
* Primary CTA: “View Open Roles”
* Secondary CTA: “Apply / Send CV”

**Goal:**
Serve Mexico‑based candidate personas without polluting buyer flows.

---

## 5. Information Architecture (Hub → Cluster → Leaf)

### 5.1 Hubs

* **Home**
* **Hire Talent (Solutions)**
* **Industries**
* **Why Mexico**
* **Resources**
* **Blog**
* **Company**
* **Contact**
* **Careers** (secondary)

### 5.2 Hire Talent (Solutions) – Clusters & Leafs

**Hire Talent hub**
Explains the MezTal model and routes into function clusters.

Major **function clusters** (pillar pages):

* Nearshore Accounting & Finance
* Nearshore IT / Data / Software Staffing
* Nearshore Software Development (subcluster under IT/Data)
* Nearshore Marketing & Creative
* Nearshore HR, Talent & Augmented Workforce
* Nearshore Operations & Admin Support
* Nearshore Customer Support & Call Center
* Workflow Automation (where supported by SEO table)

Each cluster page includes:

* Hero (outcome + roles + geography)
* Who it’s for (persona + industry ties)
* Roles we staff (linked to role pages)
* 3–5 step process (discover → shortlist → interviews → onboarding → ongoing support)
* Why Guadalajara and Mexico City for this function
* Proof band (logos, testimonials placeholders)
* FAQ block
* CTA (“Book a Consult”, “Request Candidate Profiles”)

**Role‑level leaf pages** (from SEO table + Workable):

Examples:

* `/nearshore-it-staffing/hire-data-governance-engineer/`
* `/nearshore-it-staffing/hire-azure-data-engineer/`
* `/nearshore-it-staffing/hire-databricks-engineer/`
* `/nearshore-it-staffing/hire-business-analyst/`
* `/nearshore-it-staffing/hire-oracle-hyperion-developer/`
* `/nearshore-marketing/hire-marketing-assistant/`
* `/nearshore-creative/hire-ui-designer/`

Role page template:

* Hero (Hire [Role] in Guadalajara and Mexico City)
* Who hires this role (persona + vertical examples)
* Responsibilities/value for nearshore model
* Typical tools/tech stack (where appropriate)
* Why Mexico (GDL + CDMX, overlapping business hours with the US, cost, talent)
* Example use cases / case snippets
* FAQs
* CTA (Book a consult / Request profiles)

### 5.3 Industries – Pillars & Leafs

**Industries hub** with cards for:

* Senior Living & Post‑Acute
* AgeTech
* Elder Care Technology
* Healthcare & Health Services
* SaaS & Technology
* Real Estate & Property Management
* (Financial Services where explicitly supported)

Examples (from COMET + SEO):

* `/industries/senior-living/` (pillar)

  * `/industries/senior-living/accounting/` (senior living accounting services leaf)
* `/industries/agetech/` (pillar)

  * `/industries/agetech/software-development/` (AgeTech Software Development leaf)
  * `/industries/agetech/elder-care-tech/` (Nearshore for Elder Care Technology leaf)

Industry page template:

* Hero (Nearshore teams for [Industry] in Guadalajara and Mexico City)
* Pain points (turnover, cost, coverage hours, tech debt, etc.)
* How MezTal helps (mapping clusters + roles to this vertical)
* Example roles (links to role pages)
* Case snippets / proof
* Industry‑specific FAQs
* CTA

### 5.4 Why Mexico & Geo SEO Landers

**Why Mexico pillar page**:

* Why nearshore vs offshore vs US in general
* Why Guadalajara and Mexico City:

  * Proximity to US
  * Overlapping business hours with the US
  * Talent & education
  * English proficiency
  * Tech ecosystem (Guadalajara as “Mexico’s Silicon Valley”)

**SEO landers** (leaf pages, often under /why-mexico or /nearshore paths):

From SEO & earlier work:

* Nearshore Staffing Mexico
* Remote Workers Mexico
* Remote Teams Mexico
* Mexico Outsourcing
* Hire Developers in Mexico
* Employer of Record Mexico
* Nearshore Software Development
* Staff Augmentation vs Managed Services
* Nearshoring vs Offshoring

Each as a focused landing page: hero, who it’s for, nearshore vs alternatives, why GDL + CDMX, relevant roles, FAQs, CTA.

### 5.5 Resources (Non‑Blog)

**Resources hub** with CMS collections:

* **Case Studies**

  * E.g., Senior Living digital marketing performance, accounting teams, IT teams.
  * Template: background → challenge → solution → roles provided → outcomes/metrics → testimonial → CTA.

* **Comparison pages** (from SEO table):

  * Examples:

    * `/comparison/best-it-staffing-companies`
    * `/comparison/best-it-staffing-agencies`
    * `/comparison/software-outsourcing-company`
    * `/comparison/offshore-accounting`
    * `/comparison/recruiting-firms`
    * `/comparison/staff-augmentation-firm`
    * `/comparison/nearshoring-vs-offshoring`
    * `/comparison/staff-augmentation-vs-managed-services`
    * `/comparison/offshore-companies`
    * `/comparison/offshore-it`
    * `/comparison/custom-software-development-company`
    * `/comparison/it-company`
    * `/comparison/it-recruiting-firms`
    * `/comparison/it-services-near-me`
  * Roles: mostly MOFU/BOFU; targeted at decision makers comparing providers / models.

* **Guides / Whitepapers / Glossary**:

  * `US GAAP for nearshore accounting teams`
  * `Sarbanes-Oxley compliance outsourcing`
  * `How to hire developers in Mexico`
  * `How to manage a nearshore team`
  * `Gartner magic quadrant for IT services` (interpretation/summary)
  * `Mexico’s Silicon Valley` (Guadalajara tech ecosystem)
  * `PEO` and other definitional content.

* **Pricing / Cost**:

  * Explain ~40% savings vs US and “passthrough fee” contents (office, computer, onboarding, overhead).
  * Clarify what sits in base salary vs passthrough vs MezTal margin.

* **FAQ Library**:

  * Why GDL + CDMX?
  * Cost and billing model
  * Passthrough fee details
  * Control over team members
  * Onboarding/training
  * Tools and security
  * Compliance (e.g. SOX, US GAAP references)

### 5.6 Blog

**Blog hub** + posts (CMS):

* Categories:

  * By function (Accounting & Finance, IT/Data, Marketing, HR/Talent, Ops/Admin, Support).
  * By industry (Senior Living, AgeTech, Elder Care Tech, Healthcare, SaaS/Tech, Real Estate, etc.).
* Content types:

  * Thought leadership on nearshore staffing, Mexico market, remote team management.
  * “What we’re seeing” posts in specific verticals or roles.
  * Repurposed LinkedIn posts.
* Each blog post:

  * Hero (title, date, category)
  * Body
  * Key takeaways
  * Related posts
  * CTAs / links into relevant Solutions, Industries, or Resources.

### 5.7 Company

**Company** hub includes:

* **About**: MezTal story, mission, why nearshore, why Guadalajara and Mexico City, mention of Houston office.
* **Team**: leadership bios (Sarah Thomas, Vincent Gerbec, Luis Alcaraz, Noemi Esparza, Chris Geno, etc.).
* **Locations**: Guadalajara, Mexico City, Houston.
* **LinkedIn Hub**: description of content themes + embedded LinkedIn company feed.
* **Testimonials / Proof**: structured grid of client and employee testimonials (no verbatim text in Relume prompt to save space, but slots are reserved).

### 5.8 Careers

**Careers hub** (candidate‑facing, secondary nav):

* Hero with copy like: “Do you want to be part of a growing team who cares about you?”
* Content:

  * Culture, benefits, growth.
  * Employee testimonials.
  * Embedded Workable jobs list (`apply.workable.com/flextal-staffing-llc/`).
  * Candidate FAQ.
  * Simple candidate contact form.

---

## 6. Self‑Prompt (“MezTal_Expert_Mode”) Summary

We wrote a detailed **system prompt** that defines how GPT‑5 must behave for MezTal:

* Use the canonical sources in strict priority:

  * User instructions
  * Architecture — Cleaned Map
  * COMET GitHub log
  * HubSpot SEO
  * LinkedIn & Workable
* Enforce:

  * Geography language
  * Canonical Augmented Workforce page
  * Blog vs Resources separation
  * No placeholders
  * No speculative offerings
  * Funnel‑aware navigation variants
  * Hub → cluster → leaf discipline
  * No recombination of user‑distinct nodes (e.g. Blog + Resources)
* For Relume prompts:

  * 5000 chars max
  * Dense markdown, no hex colors
  * Navigation variants + mapping
  * Sitemap, CMS collections, page templates
  * Focus on structure/constraints over marketing copy
* Interaction style:

  * Ruthless mentor, tests ideas
  * Only asks clarifying questions when truly blocked
  * Best‑effort answers with explicit assumptions

---

## 7. Known Gaps / Open Work (Future)

* Fully enumerating every single row of the SEO mapping table into a final IA is not done here (would blow token budget); instead we defined **patterns**:

  * `/comparison/...` → Resources > Comparison
  * `/resources/...` → Resources > Guides/Whitepapers
  * `/services/...` → Solutions > Service/offer pages
  * `/industries/...` and `/solutions/...` cross‑linked as appropriate.
* Final decisions on which **comparison URLs** to keep vs merge for cannibalization may require spreadsheet‑driven analysis.
* Content for case studies and blog posts will need to be written/curated separately.

---

## 8. Documents to Re‑Upload in Future Sessions

If you want future GPT sessions to recreate this level of fidelity, re‑upload these:

1. `Report of HubSpot Closed Won Report January 2023-August 2024.xlsx`
2. `MezTal HubSpot-Informed SEO.xlsx`
3. `Silent Storm MezTal doc aggregate.xlsx`
4. `Meztal_SEO_Master_Part3.xlsx`
5. `Copy of Meztal_SEO_Master_Part3 (locked, without dupes from part 1 and 2).xlsx`
6. `MezTal HUBSPOT copilot seo chat session: 9.3.25.docx`
7. `MezTal HUBSPOT copilot seo chat session_9.3.25.docx`
8. `MezTal HUBSPOT copilot seo chat session_9.3.25.pdf`
9. `LinkedIn MezTal Content - meztal_content_1754583488887.xlsx`

Plus, keep the following as **text/markdown files** in the repo:

* `MEZTAL_EXPERT_MODE_SYSTEM_PROMPT.md` (the self‑prompt you pasted)
* `MEZTAL_RELUME_PROMPT_FINAL_5000CHARS.md` (once we generate it)
* `COMET_ASSISTANT_meztal_seo_hierarchy_optimization_2025-11-17.md` (or similar)
* `MEZTAL_SEO_MAPPING_TABLE_EXCERPT.md` (the table you pasted)

---

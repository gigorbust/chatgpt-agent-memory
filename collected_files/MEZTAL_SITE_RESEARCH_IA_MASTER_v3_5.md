# MezTal.com Redesign – Research & IA Strategy Log (v3, Canonical)

**Owner:** MezTal / George  
**Strategic Lead:** GPT‑5 (MezTal_Expert_Mode)  
**Purpose:** Final, data‑grounded IA/SEO/UX research log for the MezTal site rebuild + Relume setup.

---

## 0. Canonical Inputs & Precedence

This v3 log is based ONLY on:

1. **This chat** (your instructions override everything).
2. **COMET Wix/SEO hierarchy log** (page inventory and decisions).
3. **MEZTAL_SEO_MASTER_Minimal_2025‑09‑22_R3 – Architecture — Cleaned Map (CSV)**  
   - File: `________ MEZTAL_SEO_MASTER_Minimal_2025-09-22_R3 - Architecture — Cleaned Map (1).csv`  
   - Columns: `Primary Keyword, Secondary Keywords, Topic Cluster, Proposed URL, Page Type, Content Type, Funnel Stage, Persona, Triangulated Priority Score`.
4. **HubSpot Closed‑Won deals (Jan 2023–Aug 2024)**  
   - File: `Report of HubSpot Closed Won Report January 2023-August 2024 2.xlsx`  
   - Sheet: `Closed Won`.
5. **MezTal HubSpot‑Informed SEO (Copilot Chat)**  
   - File: `MezTal HUBSPOT copilot seo chat session_.txt`.
6. **LinkedIn Content Export**  
   - File: `LinkedIn MezTal Content - meztal_content_1754583488887 2.xlsx`  
   - Sheet: `All posts` (header row at index 1).  
   - `Metrics` tab explicitly ignored as requested.

Explicitly **ignored as inputs** (unless you later say otherwise):

- Any “Meztal.com SEO Strategy Master Aggregation”.
- Any tabs in `MEZTAL_SEO_MASTER_Minimal` other than **Architecture — Cleaned Map**.
- Any previous SEO artifacts not in the list above.

---

## 1. Business Model & Hard Rules

### 1.1 What MezTal Actually Is

From current site copy, Closed‑Won, Copilot SEO:

- A **US‑facing nearshore staffing partner**, NOT a generic BPO or freelance marketplace.
- Builds **dedicated, long‑term remote teams** in **Guadalajara and Mexico City**.
- Engagement model:
  - Client: **makes hiring decisions**, **trains on their processes**, **controls the systems**.
  - MezTal: handles **HR, IT, office, payroll, recruiting** – “the messy stuff”.

### 1.2 Value Prop – Locked Phrasing

New standard language (replacing legacy wording where needed):

- **Cost:** “around **40% cost savings** vs equivalent US hires.”  
  (Legacy “50% savings” on current site is treated as outdated. New site standard is ~40%.)
- **Time zone:** Always **“overlapping business hours with the US”**.  
  Never “same time zone”.
- **Location:** Always say **“Guadalajara and Mexico City”** when describing delivery hubs.
- **Cultural fit:** English‑proficient, US‑aligned professionals.

### 1.3 Service Scope Fence

We only treat services as “real” if backed by:

- Current site,  
- COMET log,  
- Closed‑Won roles,  
- Architecture — Cleaned Map,  
- Copilot SEO transcript.

Confirmed **functional clusters**:

1. **Accounting & Finance**
2. **IT / Data / Software Development**
3. **Marketing & Creative**
4. **HR / Talent / Augmented Workforce / EOR**
5. **Operations & Admin**
6. **Customer Support / Call Center**
7. **Sales & RevOps** (supported by “Sales Solutions” in COMET + SEO Map)

No Legal, Insurance, or random stuff just because competitors do it.

### 1.4 Synonym / Cannibalization Rules

From COMET and your SEO strategy:

- Canonical service page: **Augmented Workforce Solutions**.
- Synonyms that MUST NOT become separate service URLs:
  - staff augmentation
  - supplemental workforce staffing
  - contingent workforce
  - temporary staffing
  - workforce solutions
- Use these only as:
  - H2/H3 headings,
  - FAQ content,
  - Body copy keywords,
  - Resource/Blog topics.

---

## 2. Data Reality Check – Roles & Verticals

### 2.1 Closed‑Won Roles – Parsed, Not Guessed

From `Closed Won` sheet (71 deals):

We classified **Job Title/Role** into functional clusters via explicit keyword mapping:

- **Accounting & Finance:** 44 deals  
  - Accountant (7)  
  - Staff Accountant (7)  
  - AP Specialist (6)  
  - Sr. Accountant (5)  
  - Plus Controller, Assistant Controller, Accounting Manager, Accounting Specialist, Junior Accountant, AP, Tax roles, FP&A, Billing, etc.
- **IT / Data / Software:** 10 deals  
  - Full Stack Developer, Web Developer, Data Scientist, Implementation Specialist, IT Help Desk, etc.
- **Marketing & Creative:** 8 deals  
  - PPC Marketing Specialist, Marketing Assistant, Sr. Marketing Specialist, Graphic Designer, SEO & Content Creator, Web Designer/Developer.
- **HR / Talent:** 6 deals  
  - Recruiter, HR Generalist, HR Coordinator, etc.
- **Operations & Admin:** 2 deals  
  - Administrative Assistant, Executive Assistant.
- **Customer Support:** 1 deal  
  - Customer Service Representative.

**Takeaway:**  
Accounting & Finance is the clear money engine. IT/Data and Marketing are meaningful. HR/Talent, Ops/Admin, and Support are important but smaller.

> Note: there is **zero reason** to pretend “47 roles” is sacred. The data clearly clusters into a handful of **canonical role families**. That’s what we architect around.

### 2.2 Verticals from Closed‑Won Company Names

We classified `Associated Company` into verticals:

- **Senior Living & Aging Services:** 51/71 deals  
  - Names like Trustwell Living, Lifespace Communities, Anthem Memory Care, Milestone Retirement Communities, Sunrise Senior Living, Asbury, Sona, etc.
- **Digital / Marketing / SaaS:** 10 deals  
  - Companies like Wyld, Markentum, Choice Digital.
- **Healthcare & Health Services:** 4 deals  
  - Infinium HealthCare, Accushield, etc.
- **AgeTech / Elder Care Tech:** 2 deals  
  - Rendever (explicit AgeTech).
- **Other / General Services:** 4 deals  
  - Global Importing Group, hospitality groups, misc.

**Takeaway:**  
The new site must be unapologetically anchored on **Senior Living & Aging**, with **Healthcare**, **AgeTech**, and **Digital/SaaS** as visible but secondary verticals.

---

## 3. Architecture — Cleaned Map (Minimal SEO Master)

### 3.1 What’s In There

The `Architecture — Cleaned Map` CSV contains:

- Hundreds of rows of:
  - `Primary Keyword`, `Secondary Keywords`
  - `Topic Cluster`
  - `Proposed URL`
  - `Page Type` (Pillar / Leaf / Spoke)
  - `Content Type` (Landing Page, Comparison, Guide, etc.)
  - `Funnel Stage`, `Persona`
  - `Triangulated Priority Score` (priority metric).

**High‑volume Topic Clusters:**

- IT Staffing
- HR Solutions
- Nearshore IT Staffing
- Nearshore Accounting
- Geographic Hubs
- Comparison
- Foundational Solutions
- Sales Solutions
- Resources
- Industries
- Solutions for Agencies / Partners / Startups / Private Equity
- Support Solutions
- Creative Services / Creative Solutions
- Marketing Solutions
- Operations Solutions
- Travel & Hospitality
- Venture Capital Solutions (etc.)

### 3.2 How We Use This (Without Letting It Drive Us Off a Cliff)

We treat the Architecture map as:

- A **keyword + topic inventory**, not a final sitemap.
- Evidence of:
  - Which **services** and **verticals** you *intended* to support.
  - Which **search intents** you want to rank for (Comparisons, Guides, Role pages).
  - Which **personas** (CFO, CTO, HR Director, Founder, Job Seeker) are targeted.

Core clusters that align with **now**:

- Accounting Solutions / Nearshore Accounting
- IT Staffing / Nearshore IT Staffing
- HR Solutions
- Marketing Solutions / Creative Services
- Sales Solutions
- Geographic Hubs
- Senior Living / AgeTech / Industries
- Careers (candidate SEO)

Clusters that are **real but Phase 2/optional** for IA v1:

- Solutions for Startups
- Solutions for Agencies
- Solutions for Partners
- Solutions for Private Equity & VC
- Travel & Hospitality
- Enterprise Solutions

We **log them** so we don’t forget them, but we do **not** blow up the nav with every aspiration.

### 3.3 Role Count Reality

The Architecture map implies dozens of specific “Hire X” roles (e.g., hire data governance engineer, hire azure data engineer, hire marketing assistant, hire UI designer, etc.).

**We are not optimizing for any magic role count (47, 60, whatever).**

Instead:

- We define **canonical roles** per cluster (e.g., Staff Accountant, Controller, FP&A Analyst, Data Engineer, Business Analyst, Marketing Manager, Recruiter, etc.).
- We treat near‑duplicate titles as:
  - Synonyms on the same page,
  - FAQ variants,
  - On‑page H2/H3, not separate URLs.

---

## 4. Copilot SEO Transcript – Cluster Logic

The `MezTal HUBSPOT copilot seo chat session_.txt` file confirms and expands:

### 4.1 Core Service Clusters

Copilot breaks it down exactly the way we want:

- **A. Accounting & Finance Staffing**
- **B. IT, Analytics & Engineering Recruitment**
- **C. Marketing, Content & Creative Recruitment**
- **D. HR, Recruiting & Admin Talent**

Each cluster comes with:

- Pillar page concepts (“Accounting & Finance Staffing for Senior Living & Healthcare”).
- Role examples per cluster.
- Blog topic suggestions per role family.
- UX recommendations:
  - “Roles we staff” galleries,
  - FAQs per cluster,
  - Strong CTAs.

This directly aligns with our **Hire Talent** cluster design.

### 4.2 Industry & Funnel Signals

Copilot also confirms:

- Most demand is in **Senior Living / Healthcare / Property Management**, plus SaaS and agencies.
- Recommended content split:
  - Cluster pillar pages,
  - Role‑specific BOFU landing pages,
  - Comparisons and guides for MOFU/TOFU.

This matches both Closed‑Won and Architecture — Cleaned Map.

---

## 5. LinkedIn Content – Actual Behavior, Not Assumptions

From `All posts` sheet:

- 56 posts total parsed (recent sample).
- We classified `Post title` into rough themes:

  - **Events & Conferences**  
    - ASHA, NIC, Argentum, SLIF, forums, panels, midyear events.  
    - ≈ 24 posts.

  - **MezTal Team & Culture**  
    - “Happy Friday”, mental health awareness, internal yoga sessions, team highlights, new hires.  
    - ≈ 21 posts.

  - **Senior Living & Aging**  
    - Posts that talk directly about senior living, aging, AgeTech, caregiving, future of aging.  
    - ≈ 11 posts.

AI & Future of Work, Nearshore, Mexico, etc. mostly appear inside these categories, not as a separate major category.

**Implications for Blog IA:**

- Blog categories should mirror how you actually post:
  - Senior Living & Aging
  - Events & Conferences
  - MezTal Team & Culture
  - (Optional) Nearshore & Talent Strategy as a cross‑cutting tag/category.
- “AI & Future of Care” can be a theme inside Senior Living / Strategy, not its own top‑level category yet.

---

## 6. Final Structural Model (Hubs → Clusters → Leaves)

### 6.1 Hubs (Top‑Level)

1. **Home**
2. **Hire Talent**
3. **Industries**
4. **Why Mexico**
5. **Resources**
6. **Blog**
7. **Company**
8. **Contact**
9. **Careers**

### 6.2 Hire Talent – Functional Clusters

Clusters (backed by Closed‑Won + SEO + Copilot):

- **Accounting & Finance Staffing**
- **IT & Data Staffing**
- **Marketing & Creative Staffing**
- **HR & Talent / Augmented Workforce / EOR**
- **Operations & Admin Support**
- **Customer Support & Call Center**
- **Sales & RevOps** (to align with “Sales Solutions” in COMET/SEO; likely Phase 1.5 priority)

Each cluster gets:

- A **cluster hub page**.
- A flexible number of **role pages** (NOT capped to 47 or any specific number).  
  - Focus on roles with:
    - Repeated Closed‑Won presence, and/or
    - High SEO priority scores.

### 6.3 Industries

Phase 1 industries (because they’re clearly present in data):

- **Senior Living & Long‑Term Care**  
  (majority Closed‑Won vertical)
- **AgeTech & Elder Care Technology**
- **Healthcare & Health Services**
- **B2B SaaS / Technology**
- **Real Estate & Property Management**  
  (inferred from senior living investment/community operators)

Phase 2 / future industries (present in Architecture map, not yet justified by Closed‑Won volume):

- Travel & Hospitality
- Agencies & Partners
- Startups
- Private Equity / Venture Capital

We log them, but do **not** put them all in nav v1.

### 6.4 Why Mexico + SEO Landers

**Why Mexico** hub:

- Story of Guadalajara and Mexico City.
- Cost of living and ~40% savings logic.
- Overlapping business hours.
- Talent, universities, English level.
- “Silicon Valley of Latin America” position for Guadalajara.

SEO landers (from COMET + Architecture CSV):

- Nearshore Staffing Mexico
- Remote Workers Mexico
- Mexico Outsourcing
- Remote Teams Mexico
- Employer of Record Mexico
- Cost of living in Guadalajara vs Mexico City (comparison/resource)

These pages live under/adjacent to Why Mexico and cross‑link into Hire Talent and Industries.

### 6.5 Resources vs Blog (Strict Split)

**Resources:**

- Comparison pages:
  - best it staffing companies
  - best recruitment agencies
  - offshoring vs nearshoring
  - staff augmentation vs managed services
  - offshore companies / offshore IT
- Guides/whitepapers:
  - how to hire developers in Mexico
  - how to manage a nearshore team
  - SOX compliance outsourcing
  - US GAAP for nearshore accounting teams
  - PEO explained
- Case studies:
  - Atlas Senior Living
  - Anthem Memory Care
  - Future detailed outcomes.
- Pricing and FAQ resources.

**Blog:**

- Categories:
  - Senior Living & Aging
  - Events & Conferences
  - MezTal Team & Culture
  - Nearshore & Talent Strategy (as a cross‑cutting category/tag)
  - Leadership & Insights

No merging. No “Blog/Resources” mush.

---

## 7. Navigation Strategy (Home vs SEO vs Careers)

### 7.1 Home – Minimal, Buyer‑Focused Nav

Header on **Home**:

- Logo
- Home
- Hire Talent
- Industries
- Why Mexico
- Contact
- Primary CTA: **Book a Consult**
- Careers as a small text link (not a big callout)
- Resources/Blog in footer or minimal header links if needed.

Rationale: keep cold visitors laser‑focused on the main buyer paths.

### 7.2 SEO + Deep Pages – Full Nav

Header on:

- Role pages
- Industry pages
- Why Mexico + geo landers
- Resource pages
- Blog posts

Use **full nav**:

- Home
- Hire Talent
- Industries
- Why Mexico
- Resources
- Blog
- Company
- Contact
- Careers (small text link)
- Primary CTA: **Book a Consult**

Rationale: SEO visitors land mid‑funnel and need full context, not a trimmed nav.

### 7.3 Careers / Candidate Pages – Candidate Nav

Header on:

- Careers hub
- Workable jobs hub (embed)
- Candidate FAQs

Use candidate‑tuned nav:

- Logo
- Careers
- About
- Team
- Blog
- Contact
- Primary CTA: **View Open Roles**

These pages still link back into the buyer IA but are tuned for job seekers.

---

## 8. LinkedIn & Workable Hub Pages

### 8.1 LinkedIn Hub (Under Company)

- Page goal: centralize social proof + ongoing content.
- Sections:
  - Hero: “Follow MezTal on LinkedIn”
  - Embedded LinkedIn feed
  - Curated top posts (Senior Living insights, conference clips, culture moments)
  - Short copy explaining how MezTal uses LinkedIn (thought leadership + community)
  - CTA: Follow

### 8.2 Workable Jobs Hub (Under Company or Careers)

- Embeds Workable job list (load more behavior).
- Reuses language from current Contact page:
  - “Do you want to be a part of a growing team who cares about you?”
- Includes:
  - Employee testimonial (e.g., Linda, Senior Controller)
  - Candidate FAQ
  - Space for connected **contact form** (Name, Email, Subject, Message)
- Linked clearly from:
  - Careers hub,
  - Home footer,
  - Contact.

---

## 9. Role Strategy – Kill the “47 Roles” Mental Trap

The data (Closed‑Won + Architecture CSV + Copilot SEO) collectively show:

- Many **role titles** (~dozens).
- A smaller set of **role families** that actually matter.

**We do NOT:**

- Aim for “47 role pages”.
- Hard‑code any role count as a success metric.

**We DO:**

- Create **canonical role pages** where:
  - Role appears repeatedly in Closed‑Won *and/or*
  - Has high SEO priority *and*
  - MezTal actually fills it.
- Treat near‑duplicate titles as:
  - Alternate H1/H2 wording,
  - On‑page synonyms,
  - FAQ entries.

Example:

- A single **Staff Accountant** page can absorb:
  - Staff Accountant,
  - Junior Accountant,
  - Senior Accountant (if appropriate),
  - “Senior living accountant”, etc.  
  …with clear sections, not 5 separate URLs.

The CMS and IA must support **expansion** over time, but v1 will focus on the 10–20 most valuable role families, not an arbitrary spreadsheet count.

---

## 10. Future‑Phase Expansion Rules

To avoid hallucinating services just because they appear in the SEO sheet or competitor sites:

- New **industry** page only when:
  - There is real Closed‑Won or active pipeline in that vertical, and
  - We have or can get a real case study/story.

- New **role** page only when:
  - MezTal actually fills that role,
  - It shows up in deals or high‑intent search data,
  - It deserves its own landing page beyond being a synonym.

- New **solution cluster** (e.g., dedicated “Solutions for Private Equity”) only when:
  - More than one real client + clear strategy,
  - It justifies its own positioning, not just a single deal.

All future‑phase items (Startups, Agencies, PE/VC, Travel & Hospitality) stay in the research log and Architecture CSV, but **not** in v1 main nav.

---

## 11. Status

- v3 log = **canonical** IA/SEO research spine.
- Supersedes all previous IA/SEO logs and ad‑hoc notes.
- Next step (separate output): compress this into a **~5,000 character Relume prompt** that encodes:
  - Hubs
  - Clusters
  - Role strategy
  - Nav variants
  - CMS collections
  - Hard rules (Guadalajara + Mexico City, overlapping hours, 40% savings, Blog ≠ Resources, Augmented Workforce rules).


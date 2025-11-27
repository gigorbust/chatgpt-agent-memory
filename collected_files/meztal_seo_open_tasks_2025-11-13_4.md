# MezTal SEO – Open Tasks & Backlog (2025-11-13)  

_This backlog consolidates the recommendations and task lists from the prior GPT‑5 “Client SEO information request” session into a concrete, trackable format. It is intentionally conservative about status — assume items still require verification and/or real data before being treated as complete._  

Status legend (for this document):  

- **Planned (AI)** – Designed in prior sessions, but no evidence of real‑world execution from this environment.  
- **In Progress (AI Simulation)** – Partially explored conceptually; still needs real tools and data.  
- **Needs Verification** – May already exist in user’s own sheets or tools; verify before re‑doing.  
- **Blocked** – Cannot proceed without specific access (e.g., GA4, GSC, Ahrefs credentials).  

---

## 1. Technical SEO & Crawl Tasks  

| ID | Task | Description | Owner Role | Status | Notes |
|----|------|-------------|-----------|--------|-------|
| T‑01 | Full site crawl | Run a full crawl of MezTal.com (incl. key subpages), export data to CSV. | Technical SEO Architect | Needs Verification | Previous session defined this as a top priority but only a simulated crawl was performed from within ChatGPT. Confirm whether a real Screaming Frog / Ahrefs / Semrush crawl already exists. |
| T‑02 | Populate `Pages_Crawl` | Create or update the `Pages_Crawl` table with URL, title, meta, H1/H2, indexability, status code, internal links. | Technical SEO Architect | Planned (AI) | Table schema is defined in `meztal_seo_architecture_2025-11-13.md`. Needs actual data import. |
| T‑03 | Indexation & canonical audit | Identify non‑indexable pages, duplicate URLs, and canonical issues. | Technical SEO Architect | Planned (AI) | Dependent on T‑01 and T‑02. |
| T‑04 | XML sitemap & robots review | Validate XML sitemaps, robots.txt directives, and ensure all priority URLs are discoverable. | Technical SEO Architect | Planned (AI) | Requires access to live site and GSC. |
| T‑05 | Core Web Vitals review | Assess LCP, CLS, INP/FID for key templates and pages. | Technical SEO Architect | Blocked | Needs access to PageSpeed Insights / CrUX / Core Web Vitals reports. |

---

## 2. Keyword Research & Superbase Build  

| ID | Task | Description | Owner Role | Status | Notes |
|----|------|-------------|-----------|--------|-------|
| K‑01 | Initialize `Keyword_Bank` | Create the Keyword Bank table with the schema defined in the SEO architecture doc. | Semantic Strategist | Needs Verification | Prior session defined the structure but actual Google Sheet / DB may exist (e.g., MezTal_SSOT_Cleaned). Verify before creating new. |
| K‑02 | Import SSOT keywords | Import existing keyword data from `MezTal_SSOT_Cleaned_v5.0.xlsx` (or equivalent) into `Keyword_Bank`. | Semantic Strategist | Blocked | File is referenced but content is not visible here. Human needs to export/import. |
| K‑03 | Tool‑based keyword expansion | Use GKP / Ahrefs / Semrush to expand keyword list for all service lines and key geographies. | Semantic Strategist | Planned (AI) | Prior conversation outlined this but did not execute tool calls. |
| K‑04 | Assign categories, intent, funnel stage | For each keyword, assign category (service/theme), intent (informational/transactional/etc.), and funnel stage (TOFU/MOFU/BOFU). | Semantic Strategist | Planned (AI) | Can be partly automated via rules; final QA by human/agent. |
| K‑05 | Identify low‑competition “low‑hanging fruit” | Filter Keyword Bank to surface high‑value, low‑difficulty keywords and push into `Low_Hanging_Fruit`. | Semantic Strategist | In Progress (AI Simulation) | Prior session sketched a top‑10 list conceptually but without real metrics. Needs real KD/volume and validation. |

---

## 3. Competitor Intelligence & Gap Analysis  

| ID | Task | Description | Owner Role | Status | Notes |
|----|------|-------------|-----------|--------|-------|
| C‑01 | Define competitor set | Finalize list of 3–5 core direct competitors and 3–5 indirect/adjacent ones. | Competitor Analyst | Needs Verification | Some candidates were discussed previously but no final canonical list is logged in this environment. |
| C‑02 | Pull competitor keyword exports | Use Ahrefs/Semrush/SpyFu to export top keywords for each competitor. | Competitor Analyst | Planned (AI) | Requires tool access. |
| C‑03 | Populate `Competitor_Keywords` | Load competitor keyword data into the Competitor_Keywords table and align with clusters. | Competitor Analyst | Planned (AI) | Dependent on C‑02 and K‑04. |
| C‑04 | Build competitor gap view | Identify keywords where competitors rank but MezTal does not, especially in high‑value clusters. | Competitor Analyst + Semantic Strategist | Planned (AI) | Outputs feed directly into `Low_Hanging_Fruit` and `Content_Map`. |

---

## 4. Topic Clusters & Content Architecture  

| ID | Task | Description | Owner Role | Status | Notes |
|----|------|-------------|-----------|--------|-------|
| CL‑01 | Define initial clusters | Confirm initial priority clusters (Nearshore Staffing, IT Staffing, Finance & Accounting Outsourcing, Call Center, HR, etc.). | Semantic Strategist | Needs Verification | Cluster concepts exist in prior plan; convert into a formal list with definitions. |
| CL‑02 | Assign keywords to clusters | For every keyword in `Keyword_Bank`, assign a cluster. | Semantic Strategist | Planned (AI) | Can be semi‑automated once categories are set. |
| CL‑03 | Identify pillar pages per cluster | For each cluster, choose 1–2 pillar pages (existing or new) to act as hubs. | Content Architect + Semantic Strategist | Planned (AI) | Should leverage Fellou “MezTal Markdown Strategy” + Notion Website Proposal. |
| CL‑04 | Map supporting pages | Define 3–10 supporting pages per cluster (guides, FAQs, comparisons, case studies). | Content Architect | Planned (AI) | These become the core backlog of new content work. |
| CL‑05 | Build `Content_Map` | Implement the Content_Map table and populate mappings between keywords, clusters, and target URLs. | Semantic Strategist + Content Architect | Planned (AI) | Central to preventing cannibalization and tracking who owns what. |

---

## 5. Content Production, Optimization & CRO  

| ID | Task | Description | Owner Role | Status | Notes |
|----|------|-------------|-----------|--------|-------|
| CT‑01 | Align Fellou Markdown drafts with clusters | Map existing Markdown drafts (Homepage, Services hub, etc.) to clusters and primary keywords. | Content Architect | Needs Verification | Requires reviewing the Fellou MezTal Markdown Strategy doc and ensuring alignment with Keyword_Bank and Content_Map. |
| CT‑02 | On‑page optimization for existing pages | For core pages already on MezTal.com, optimize titles, metas, H1/H2s, body copy, and internal links according to keyword assignments. | Content Architect | Planned (AI) | Depends on Pages_Crawl + Content_Map. |
| CT‑03 | Create priority new pillar pages | Draft and publish the highest‑impact pillar pages for top clusters. | Content Architect | Planned (AI) | Use Fellou Markdown as base where possible. |
| CT‑04 | Create supporting articles & resources | Produce supporting guides, FAQs, comparisons, and case studies for each cluster. | Content Architect | Planned (AI) | These are key for topical authority. |
| CT‑05 | Integrate conversion strategy into content | Add clear CTAs (book call, request quote, contact, etc.), forms, and proof elements on all key pages. | Content Architect | Planned (AI) | CRO considerations must be integrated with SEO from the start. |

---

## 6. Programmatic SEO (Optional, Later Phase)  

| ID | Task | Description | Owner Role | Status | Notes |
|----|------|-------------|-----------|--------|-------|
| P‑01 | Design programmatic page templates | Define templates for scalable landing pages (e.g., “Hire [Role] in [Location]”). | Programmatic SEO Lead | Planned (AI) | Only after core clusters are in good shape. |
| P‑02 | Define variable sets | Decide which dimensions (role, seniority, location, industry, etc.) will be used for programmatic pages. | Programmatic SEO Lead + Semantic Strategist | Planned (AI) | Needs careful guardrails to avoid thin/duplicative content. |
| P‑03 | Establish quality & governance rules | Define rules for uniqueness, on‑page depth, and manual QA for generated pages. | Programmatic SEO Lead | Planned (AI) | Prevents low‑quality mass generation. |
| P‑04 | Implement initial batch | Launch a small batch of programmatic pages and monitor performance & indexation. | Programmatic SEO Lead + Technical SEO Architect | Planned (AI) | Treat as an experiment before scaling. |

---

## 7. Monitoring, Analytics & Reporting  

| ID | Task | Description | Owner Role | Status | Notes |
|----|------|-------------|-----------|--------|-------|
| M‑01 | Set up `Performance_Tracker` | Implement the Performance_Tracker table and connect it to GSC/GA4 exports. | Monitoring Engineer | Planned (AI) | Schema defined in SEO architecture doc. |
| M‑02 | Establish rank tracking | Configure rank tracking for priority keywords (by cluster). | Monitoring Engineer | Blocked | Needs access to a rank tracking tool (Ahrefs, Semrush, Nightwatch, etc.). |
| M‑03 | Build reporting dashboards | Build Looker Studio / Data Studio dashboards for stakeholders. | Monitoring Engineer | Planned (AI) | Inputs: Performance_Tracker + Keyword_Bank + Content_Map. |
| M‑04 | Define review cadence | Set monthly/quarterly cadence for reviewing traffic, rankings, and conversions by cluster. | Monitoring Engineer + Strategic Oversight | Planned (AI) | Should result in concrete iteration decisions. |

---

## 8. Schema, E‑E‑A‑T, & Trust Signals  

| ID | Task | Description | Owner Role | Status | Notes |
|----|------|-------------|-----------|--------|-------|
| S‑01 | Schema strategy | Define which schema types to implement (Organization, Service, FAQ, Article, Breadcrumb, etc.). | Technical SEO Architect | Planned (AI) | Previous session explicitly called out schema as a strategic lever. |
| S‑02 | Implement schema on key pages | Add structured data to pillars and important support pages. | Technical SEO Architect | Planned (AI) | Should be coordinated with Content Architect. |
| S‑03 | Author & entity signals | Ensure authorship, company info, and trust badges are present on key content. | Technical SEO Architect + Content Architect | Planned (AI) | Supports E‑E‑A‑T for competitive topics. |

---

## 9. Governance & Next Actions  

1. **Do not assume anything here is fully complete.**  
   - Many tasks were *architected* in the prior GPT‑5 session but not executed with live tools.  

2. **First action for a future agent/human:**  
   - Confirm whether a real **crawl export**, **keyword bank spreadsheet**, and **performance dashboards** already exist.  
   - If they do, **connect them to this backlog** and update statuses accordingly (rather than re‑creating work).  

3. **After verification:**  
   - Prioritize: Technical crawl + Keyword Bank + Low‑Hanging‑Fruit mapping.  
   - Then move into cluster mapping, content production, and measurement.  

This document should be treated as the **SEO task ledger** for MezTal going forward. Add dated addenda rather than overwriting, so the `/logs` directory can serve as a historical record of decisions and progress.

# MezTal SEO & Site Planning – External Sources Index  
_Date: 2025-11-13_  

This document lists the key **external artifacts** (Google Drive, Dropbox, Notion, GitHub, etc.) that influence MezTal’s SEO and site planning. Its purpose is to help future agents and collaborators quickly locate the upstream materials referenced in other `/logs` documents.  

> Note: Paths, titles, and roles are based on what is visible from this environment. Treat this as a navigational map, not a direct permission grant.  

---

## 1. Google Drive  

### 1.1 “CHAT GPT 5 SESSION — Client SEO information request” (PDF)  

- **Type:** PDF export of a ChatGPT GPT‑5 session.  
- **Location:** Google Drive.  
- **Role:**  
  - Primary transcript of the earlier SEO strategy conversation for MezTal.  
  - Defines:  
    - Client intake questions.  
    - SEO keyword strategy framework.  
    - The “Superbase” SEO database idea (Pages_Crawl, Keyword_Bank, etc.).  
    - Expert roles (Technical SEO Architect, Semantic Strategist, Competitor Analyst, Content Architect, Programmatic SEO Lead).  
    - High‑level backlog of tasks and status tracking philosophy.  
- **How to use it now:**  
  - Treat this PDF as the **raw historical record**.  
  - Use `meztal_seo_architecture_2025-11-13.md` and `meztal_seo_open_tasks_2025-11-13.md` as the **operational summary** so you don’t need to reread the entire transcript.  

### 1.2 “Fellou AI MezTal Markdown Strategy” (Google Doc)  

- **Type:** Google Doc; Markdown‑style content and strategy.  
- **Location:** Google Drive.  
- **Role:**  
  - Contains **long‑form, SEO‑aware drafts** for MezTal’s key pages, including:  
    - Homepage (`/`).  
    - Services hub (`/services`).  
    - Multiple service pillars (IT staffing, accounting solutions, BPO, etc.).  
  - Includes metadata recommendations, H1/H2 structures, internal linking notes, and schema examples.  
- **How to use it now:**  
  - As the **primary content source** when building or rewriting MezTal’s top‑priority pages.  
  - Align each section with keywords and clusters in the **Keyword_Bank** and **Content_Map** tables.  
  - Keep the Google Doc as a draft workspace; treat the live site + Superbase as the **source of truth** once published.  

---

## 2. Dropbox  

### 2.1 “MezTal_SSOT_Cleaned_v5.0.xlsx”  

- **Type:** Excel spreadsheet (master SEO / site SSOT).  
- **Location:** Dropbox.  
- **Role:**  
  - Appears to be a **cleaned master spreadsheet** of MezTal’s SEO and site data (likely including pages, keywords, and priorities).  
  - May contain earlier versions of what we now call the **Superbase** tables.  
- **How to use it now:**  
  - **Do not ignore it.** Before creating new tracking sheets, check whether this already implements part of the Superbase.  
  - Recommended approach:  
    1. Export relevant tabs to CSV.  
    2. Map columns into `Pages_Crawl`, `Keyword_Bank`, etc.  
    3. Keep the original file archived but **migrate to a single live environment** (e.g., Google Sheets).  

---

## 3. Notion  

### 3.1 “Website Proposal” (MezTal Digital & Referral Partner Strategy workspace)  

- **Type:** Notion page.  
- **Role:**  
  - Contains the **proposed sitemap and wireframe** for MezTal’s website, including:  
    - Home, About, Services, Team, Why Guadalajara?, Testimonials, Pricing, FAQs, Careers, Blog, Contact, Legal, etc.  
    - Section‑by‑section breakdowns for the Homepage and key subpages.  
  - References external tools like Relume for visual site building and Gamma for landing pages/presentations.  
- **How to use it now:**  
  - As the **information architecture (IA) blueprint** for the site.  
  - Cross‑map Notion’s page list to:  
    - Wix Studio pages and dynamic templates.  
    - `Pages_Crawl` entries.  
    - Keyword clusters and target pages in `Content_Map`.  
  - Any future IA changes should be captured both in Notion and in the `/logs` directory (via addenda).  

### 3.2 Other Notion Strategy Pages (Context Only)  

There are additional Notion pages related to MezTal’s broader digital and referral strategy. From this environment we only see partial snippets, but they may contain:  

- Broader marketing strategy.  
- Referral / partnership plans.  
- Additional structural notes about content or funnels.  

**Recommendation:** when doing high‑impact revisions to SEO or IA, a human should review those Notion pages directly and then log any *new* decisions into `/logs` as addenda documents.  

---

## 4. GitHub  

### 4.1 `gigorbust/chatgpt-agent-memory` Repository  

- **Type:** GitHub repo.  
- **Role:**  
  - **Persistent memory + error/work log for ChatGPT agent mode.**  
  - Intended to store:  
    - Project context docs (e.g., `meztal_project_context.md`).  
    - Open task lists (e.g., `open_tasks.md`).  
    - Session summaries and log addenda.  
    - Communication guidelines and logging improvements.  
- **How to use it now:**  
  - Place this document and other new `.md` files into the `/logs` folder.  
  - Treat `/logs` as the **canonical audit trail** of all agent‑level work on MezTal (and related projects).  
  - When new external assets are introduced (new Sheets, Docs, etc.), add them here with a short description and relationship to the existing system.  

---

## 5. Other Referenced Assets (Non‑SEO but Relevant)  

Some artifacts in this environment relate to other projects (e.g., Silent Storm / Party Headphones). While not directly tied to MezTal SEO, they may inform **content style, authority, or cross‑business learnings**. For completeness:  

- **“The Ultimate Guide – Party Headphones.pdf”**  
  - A comprehensive guide to silent disco events, planning, and equipment.  
  - Useful as a reference for **long‑form educational content structure** (H2/H3 hierarchy, FAQs, checklists) that could inspire future MezTal resources, even though the subject matter is different.  

These non‑MezTal artifacts should **not** be treated as sources of factual content for MezTal, but they can be mined for **formatting, structure, and tone ideas** when appropriate.  

---

## 6. Usage Guidelines  

1. **Always prefer structured logs over scattered links.**  
   - When new documents significantly affect MezTal SEO or IA, create or update an `.md` file in `/logs` that summarizes *what changed* and *how it should be used*.  

2. **Avoid duplicate tracking systems.**  
   - Before building a new spreadsheet or database, check:  
     - Google Drive (Fellou Markdown + any SEO Sheets).  
     - Dropbox (`MezTal_SSOT_Cleaned_v5.0.xlsx`).  
     - GitHub `/logs`.  
   - If a partial system exists, **migrate and consolidate** rather than fork.  

3. **Keep this index updated via addenda.**  
   - When new upstream documents are created (e.g., “MezTal SEO Dashboard v2”, “Programmatic Landing Page Templates”), add a short entry here or in a dated addendum file.  

This index is intentionally high‑level; its job is to prevent future sessions from “rediscovering” the same work repeatedly and to anchor all work back to known, named artifacts.

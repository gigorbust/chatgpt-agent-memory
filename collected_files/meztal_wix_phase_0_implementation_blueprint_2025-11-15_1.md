# PHASE 0: IMMEDIATE WIX FOUNDATION BLUEPRINT
**Status:** Foundation must be complete before any other work
**Effort Estimate:** 4-6 hours

---

## TASK 1: CREATE 7 KEYWORD LANDING PAGES

### Structure (Template for each page)
- URL slug: /[keyword-slug]
- Page title: [Keyword - specific value prop]
- Meta description: 150-160 chars, includes keyword
- H1: Keyword-focused heading
- Content: 800-1200 words
- Internal links: To relevant topical hub (mandatory)
- Image: Optimized with ALT text including keyword
- CTA: Appropriate to buyer stage

### Pages to create:

1. **Nearshore Staffing Mexico**
   - URL: /nearshore-staffing-mexico
   - Target keyword: "nearshore staffing mexico" (890/mo)
   - Hub link: Nearshore Staffing hub
   - Content angle: Cost savings + talent quality

2. **Remote Workers Mexico**
   - URL: /remote-workers-mexico
   - Target keyword: "remote workers mexico" (1,200/mo)
   - Hub link: Remote Work in Mexico hub
   - Content angle: Time zone alignment + cultural fit

3. **Mexico Outsourcing**
   - URL: /mexico-outsourcing
   - Target keyword: "mexico outsourcing" (1,100/mo)
   - Hub link: Outsourcing hub
   - Content angle: Business process outsourcing benefits

4. **Hire Developers Mexico**
   - URL: /hire-developers-mexico
   - Target keyword: "hire developers mexico" (720/mo)
   - Hub link: Hiring Developers Mexico hub
   - Content angle: Technical talent + cost efficiency

5. **Remote Teams Mexico**
   - URL: /remote-teams-mexico
   - Target keyword: "remote teams mexico" (580/mo)
   - Hub link: Remote Work in Mexico hub
   - Content angle: Building distributed teams

6. **Employer of Record Mexico**
   - URL: /employer-of-record-mexico
   - Target keyword: "employer of record mexico" (340/mo)
   - Hub link: Employer of Record hub
   - Content angle: Legal/tax handling + compliance

7. **Hiring in Mexico**
   - URL: /hiring-in-mexico
   - Target keyword: "hiring in mexico" (450/mo)
   - Hub link: Multiple hubs (link to most relevant)
   - Content angle: Complete hiring process guide

---

## TASK 2: CREATE 5 TOPICAL HUB PAGES

### Structure (Template for each hub)
- URL slug: /[hub-slug]
- H1: Hub topic (not keyword-stuffed)
- Purpose: Content cluster center for semantic authority
- Content: 1500-2000 words covering topic breadth
- Internal structure:
  - 2-3 links to related keyword landing pages
  - 1-2 links to guides/resources
  - 1 link to case studies collection
  - Breadcrumb navigation
- Schema: BreadcrumbList + Topic schema

### Hubs to create:

1. **Remote Work in Mexico Hub**
   - URL: /remote-work-mexico
   - Cluster pages: Remote Workers Mexico, Remote Teams Mexico
   - Key subtopics: Time zones, culture, infrastructure
   - Resources: Setup guide, team building guide

2. **Nearshore Staffing Hub**
   - URL: /nearshore-staffing
   - Cluster pages: Nearshore Staffing Mexico, Cost savings angle
   - Key subtopics: Cost comparison, talent pool, quality
   - Resources: Cost calculator, staffing playbook

3. **Employer of Record Hub**
   - URL: /employer-of-record
   - Cluster pages: Employer of Record Mexico
   - Key subtopics: Legal structure, tax implications, compliance
   - Resources: Legal guide, tax calculator

4. **Outsourcing Hub**
   - URL: /outsourcing-guide
   - Cluster pages: Mexico Outsourcing
   - Key subtopics: Business process outsourcing, IT outsourcing, staffing models
   - Resources: Outsourcing checklist, comparison guide

5. **Hiring Developers Mexico Hub**
   - URL: /hiring-developers-mexico
   - Cluster pages: Hire Developers Mexico
   - Key subtopics: Tech talent pool, skills available, hiring process
   - Resources: Tech hiring checklist, skills guide

---

## TASK 3: SET UP WIX DATA COLLECTIONS

### Collection 1: Case Studies
**Fields:**
- Title (text) - Client name/project title
- Industry (select) - Finance, Tech, Healthcare, etc.
- Challenge (long text) - Client's initial problem
- Solution (long text) - How MezTal helped
- Results (long text) - Quantified outcomes
- Cost Savings (text) - Percentage or $ amount
- Team Size (number) - How many hired
- Image (image) - Client logo or project screenshot
- Testimonial Quote (text) - Client quote
- Client Name (text) - For display
- Status (select) - Published/Draft

**Test Data:** Create 2-3 dummy cases to test display

### Collection 2: Testimonials  
**Fields:**
- Quote (text)
- Author Name (text)
- Author Title (text)
- Company (text)
- Image (image) - Author photo (optional)
- Related Case Study (reference) - Link to case study (optional)
- Status (select) - Published/Draft

**Relationship:** Can link multiple testimonials to same case study

### Collection 3: Resources
**Fields:**
- Title (text) - Guide/tool name
- Type (select) - Guide, Tool, Calculator, Checklist
- Description (text) - Brief description
- URL (text) - Link to resource or form
- Related Hub (select) - Which hub this belongs to
- Image (image) - Icon or cover
- Status (select) - Published/Draft

**Purpose:** Aggregate all guides, tools, calculators

### Collection 4: FAQ Entries
**Fields:**
- Question (text)
- Answer (long text)
- Category (select) - Pricing, Hiring, Legal, Process, etc.
- Related Landing Page (reference) - Link to page that expands
- Order (number) - Sort order
- Status (select) - Published/Draft

**Purpose:** Expandable without creating new pages

---

## TASK 4: IMPLEMENT SCHEMA MARKUP

### Required Schemas (in <head> or via Wix SEO settings):

1. **Organization Schema**
   - Company name: MezTal / FlexTal Staffing LLC
   - Logo: https://www.meztal.com/logo.png
   - Contact: Info@meztal.com, 1-832-224-3580
   - Social profiles: LinkedIn
   - Address: Guadalajara, Mexico

2. **LocalBusiness Schema**
   - Business type: StaffingAgency
   - Address: Guadalajara, Jalisco, Mexico
   - Phone: 1-832-224-3580
   - Hours: Mon-Fri 9AM-6PM CST

3. **BreadcrumbList Schema**
   - Applied to all pages
   - Path: Home > Hub > Landing Page
   - Auto-generate from Wix URL structure

4. **FAQPage Schema**
   - Applied to FAQ page
   - Question/Answer pairs from FAQ collection
   - Auto-expand with new collection items

5. **JobPosting Schema** (future)
   - For recruitment/apply pages
   - Fields: Title, Description, Company, Location

---

## TASK 5: IMPLEMENT INTERNAL LINKING TOPOLOGY

### Linking Rules (MANDATORY):

1. **Landing Page → Hub Link**
   - Every landing page MUST link to its primary hub
   - Anchor text: Hub name (natural context)
   - Position: Body text, natural context
   - Example: "Learn more about [Hub Name]"

2. **Hub → Landing Page Links**
   - Hub links to 2-3 of its cluster pages
   - Anchor text: Page-specific topic (not generic)
   - Position: In content sections where relevant

3. **Hub → Hub Links**
   - Link between related hubs only
   - Example: Remote Work hub → Hiring Developers hub
   - Only when contextually relevant

4. **FAQ → Landing Page Links**
   - FAQ questions link TO detailed landing pages
   - NOT vice versa
   - Example: FAQ answer ends with "Read our full guide on [Landing Page]"

5. **Resources → Hub Links**
   - Each guide/tool links back to parent hub
   - Anchor text: Hub name
   - Position: At end of resource

6. **Case Studies → Landing Page Links**
   - Case studies link to relevant landing pages
   - Example: "See how we hired developers in Mexico" links to "Hire Developers Mexico" page

### Validation:
- No orphaned pages (every page has at least 1 internal link)
- No broken links
- Consistent anchor text (not over-optimized)

---

## TASK 6: VERIFY TECHNICAL FOUNDATION

### SEO Setup Checklist:
- ✅ Domain: meztal.com (verified)
- ✅ SSL/HTTPS: Configured (verified)
- ✅ Mobile responsive: Check (verified)
- [ ] robots.txt: Verify Wix default
- [ ] Sitemap: Verify includes all new pages
- [ ] Meta robots tag: noindex removed from main content
- [ ] Duplicate content: Check canonical tags
- [ ] Structured data: Validate with Google Schema tester

### Google Search Console Setup:
- [ ] Verify ownership
- [ ] Submit sitemap.xml
- [ ] Request indexing for all Phase 0 pages
- [ ] Monitor crawl errors
- [ ] Monitor core web vitals

---

## COMPLETION CHECKLIST (Phase 0 DONE)

### Pages
- [ ] 7 keyword landing pages created and linked to hubs
- [ ] 5 topical hub pages created with cluster links
- [ ] All pages have unique titles, descriptions, H1s
- [ ] All pages have at least 1 internal link incoming/outgoing
- [ ] All pages published and indexed

### Collections
- [ ] 4 data collections created in Wix
- [ ] 2-3 test items in each collection
- [ ] Collections tested (items display correctly)
- [ ] Future content plan: Add real cases + testimonials

### Technical
- [ ] Schema markup validated (Google Rich Results test passes)
- [ ] Sitemap includes all new pages
- [ ] Google Search Console shows 0 indexing errors
- [ ] Mobile responsive tested on 3+ devices
- [ ] Page speed acceptable (PageSpeed Insights > 50)

### Internal Linking
- [ ] Every landing page links to relevant hub
- [ ] Every hub links to 2-3 cluster pages
- [ ] FAQ questions link to landing pages (not vice versa)
- [ ] No orphaned pages
- [ ] Navigation breadcrumbs consistent

---

## NEXT PHASES (Do NOT start until Phase 0 complete)

**Phase 1:** On-page SEO optimization + additional linking
**Phase 2:** Content creation (guides, tools, case studies) + dynamic binding

**Foundation must be sound before proceeding.**

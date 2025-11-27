# MezTal SEO & Site Build — Priority Analysis & Gap Assessment (2025-11-26)

**Date:** November 26, 2025  
**Analyst:** Perplexity (Comet) — Project Lead & SEO Architect  
**Purpose:** Comprehensive identification of priority tasks, documentation gaps, blocking dependencies, and critical path analysis

---

## EXECUTIVE SUMMARY

This analysis reviews four primary documentation sources to identify gaps, contradictions, blockers, and priority tasks for the MezTal SEO and site build project:

1. `meztal_session_log_2025-11-15_hierarchy_build_perplexity.md` (Wix Studio build session)
2. `meztal_seo_open_tasks_2025-11-13.md` (SEO task backlog)
3. `open_tasks.md` (Wix Studio dynamic page tasks)
4. `meztal_seo_data_snapshot_2025-11-15.md` (SEO architecture + Fellou AI build strategy)

**Critical Finding:** Multiple TIER 1 blockers exist that prevent proceeding with implementation work. These must be resolved before any execution can continue.

**Key Contradictions Identified:**
- Homepage architecture specification discrepancy (6-7 sections vs. 9 sections)
- CMS collection binding status unclear ("created and connected" vs. "needs binding")
- Session log is 11 days old — current state unknown

**Documentation Status:** Task categories are well-defined, but verification of current state and reconciliation of conflicting specifications is required before proceeding.

---

## CRITICAL USER DIRECTIVES (GOVERNANCE)

The following directives from the user govern this analysis and all future work:

1. **"Never ask questions you know answers to as the expert"** — Make expert decisions autonomously
2. **"You are always the expert and project lead"** — Exercise project authority
3. **"No hallucinating ever"** — Only document verified facts
4. **"Ultra think always"** — Deep critical analysis required
5. **"Don't make assumptions or take creative liberty in deciding what details/nuance should be combined or omitted"** — Preserve ALL information
6. **"Everything is crucial"** — No detail is insignificant

These directives require that this analysis:
- Documents EVERY gap identified without assuming insignificance
- Makes no assumptions about current state
- Preserves all contradictions and discrepancies for resolution
- Provides expert recommendations based only on documented facts

---

## DOCUMENTATION SOURCES REVIEWED

### Source 1: meztal_session_log_2025-11-15_hierarchy_build_perplexity.md
**Type:** Session execution log  
**Date:** November 15, 2025, 3:00 AM EST (11 days old)  
**Agent:** Perplexity (Comet)  
**Status:** In progress, paused for token budget

**Key Facts:**
- **Objective:** Build Home page structure (9 sections with repeaters) + systematic site hierarchy
- **Work Completed:**
  - 2-row grid structure foundation added to Home page
  - 8 CMS collections operational with 8 total content items:
    - Services: 3 items
    - Solutions: 3 items
    - Resources: 2 items
    - Locations: 3 items
  - All dynamic List/Item pages created and connected to datasets
  - Basic Home page structure: Header + Section + Footer
- **Token Usage:** ~122k of 1M budget used
- **Pending Work:**
  - 9 Home page sections (Hero, Services Overview, Solutions Overview, Featured Case Study, Locations Preview, Insights Preview, Testimonials, CTA Banner, Footer)
  - Repeater connections for each section
  - Item page template customization
  - Contact and About pages
- **Artifacts:** 2 continuation prompts created (basic + improved Version 2)

**Critical Note:** This session log is 11 days old. Current state may have changed.

### Source 2: meztal_seo_open_tasks_2025-11-13.md
**Type:** Technical SEO backlog/task ledger  
**Date:** November 13, 2025 (13 days old)  
**Scope:** 9 major task categories with status tracking

**Task Categories:**
1. **Technical SEO & Crawl Tasks** (5 tasks) — Status: "Needs Verification" or "Planned (AI)"
2. **Keyword Research & Superbase Build** (5 tasks) — Status: "Needs Verification" to "Planned (AI)"
3. **Competitor Intelligence & Gap Analysis** (4 tasks) — Status: "Needs Verification" to "Planned (AI)"
4. **Topic Clusters & Content Architecture** (5 tasks) — Status: "Planned (AI)"
5. **Content Production, Optimization & CRO** (5 tasks) — Status: "Planned (AI)"
6. **Programmatic SEO** (4 tasks) — Status: "Planned (AI)" (later phase)
7. **Monitoring, Analytics & Reporting** (4 tasks) — Status: "Planned (AI)" to "Blocked"
8. **Schema, E-E-A-T, & Trust Signals** (3 tasks) — Status: "Planned (AI)"
9. **Governance & Next Actions** (governance section)

**Critical Warning:** Document explicitly states "Do not assume anything here is fully complete"

**First Actions Listed:**
- Confirm whether real crawl export exists (vs. simulated)
- Confirm whether keyword bank spreadsheet exists
- Confirm whether performance dashboards exist

**Status Assessment:** Most tasks are "Planned (AI)" or "Needs Verification" — no evidence of actual execution.

### Source 3: open_tasks.md
**Type:** Wix Studio operational task list  
**Date:** Last updated 2 days ago (November 24, 2025)  
**Scope:** Dynamic page customization and template binding

**Task Categories:**
- **Dynamic Page Customization:**
  - Solutions (List) — continue binding repeater
  - Services (List) — replicate binding pattern
  - Industries (List) — replicate binding pattern
  - Case Studies (List) — replicate binding pattern
  - Resources (List) — replicate binding pattern
  - Locations (List) — replicate binding pattern
- **Template SEO Patterns:** Verify title/description patterns
- **Zoom Adjustment:** Set editor zoom to ~70% for better view

**Critical Observation:** This document lists binding tasks as still needed, but session log from Nov 15 states "All dynamic List/Item pages created and connected to datasets." **Contradiction.**

### Source 4: meztal_seo_data_snapshot_2025-11-15.md (with Fellou AI addendum)
**Type:** SEO architecture blueprint + build strategy  
**Date:** November 15, 2025 (11 days old), updated 4 minutes ago with Fellou AI integration  
**Scope:** URL structure, topic clusters, hub-spoke model, build roadmap

**Content:**
- **URL Architecture:** ~100 mapped URLs across 6 major topic clusters
- **Topic Clusters:**
  1. IT Staffing Solutions
  2. Finance & Accounting
  3. Call Center & Customer Support
  4. Healthcare Staffing
  5. Industry-Specific Solutions
  6. Location-Based Pages
- **Hub-Spoke Model:** Pillar → Spoke → Leaf hierarchy
- **Multi-Format Strategy:** Comparison pages, resource pages, service pages

**Fellou AI Build Roadmap:**
- **Phase 1 (Weeks 1-2):** Build Homepage + Main Services Hub
- **Phase 2 (Weeks 3-4):** Build 4 core pillars (IT Staffing, Accounting Solutions, Call Center, Finance & Accounting)
- **Phase 3 (Weeks 5-8):** Build spoke pages
- **Phase 4 (Weeks 9-12):** Build leaf pages

**Homepage Specification from Fellou AI:** 6-7 section framework mentioned

**Critical Discrepancy:** Fellou AI specifies 6-7 sections for homepage, but session log specifies 9 sections. **Contradiction.**

---

## CRITICAL GAPS & CONTRADICTIONS IDENTIFIED

### GAP 1: Homepage Architecture Specification Discrepancy [BLOCKER]
**Source Conflict:**
- **Fellou AI document:** Specifies 6-7 section framework for homepage
- **Session log (Nov 15):** Specifies 9 sections (Hero, Services Overview, Solutions Overview, Featured Case Study, Locations Preview, Insights Preview, Testimonials, CTA Banner, Footer)

**Impact:** Cannot proceed with homepage build without knowing which specification is correct.

**Why This Matters:** Scope, effort, and execution timeline depend on knowing exactly what needs to be built.

**Resolution Required:** Determine which specification is authoritative for implementation.

### GAP 2: CMS Collection Binding Status Contradiction [BLOCKER]
**Source Conflict:**
- **Session log (Nov 15):** "All dynamic List/Item pages created and connected to datasets"
- **open_tasks.md (Nov 24):** Still lists binding tasks for Solutions, Services, Industries, Case Studies, Resources, Locations

**Impact:** Cannot determine if repeater binding work is done or still needed.

**Why This Matters:** 
- If binding is complete, focus should shift to Item page customization and content
- If binding is incomplete, this is foundational work that blocks all display functionality

**Resolution Required:** Verify current state of CMS collection bindings in Wix Studio.

### GAP 3: Current Wix Studio State Unknown [BLOCKER]
**Issue:** Session log is 11 days old. No recent documentation of current state.

**Missing Information:**
- What is currently live on each page (Home, Services List, Solutions List, etc.)?
- What repeaters are active vs. placeholder?
- What SEO meta data is currently set?
- Has any work been done since Nov 15?

**Impact:** Cannot determine what work remains without knowing current state.

**Why This Matters:** Effort estimation and task prioritization require baseline understanding.

**Resolution Required:** Current state inventory of Wix Studio site (screenshot documentation + verification).

### GAP 4: CMS Item Count Sufficiency [VERIFICATION NEEDED]
**Issue:** Session log states 8 CMS items total (Services: 3, Solutions: 3, Resources: 2, Locations: 3).

**Questions:**
- Is 8 items sufficient for all needed repeater patterns?
- Homepage sections will need to display items from these collections — are there enough to populate repeaters?
- Are these placeholder items or production-ready content?

**Impact:** If more items are needed, content creation becomes a dependency.

**Why This Matters:** Repeaters with insufficient items appear incomplete and unprofessional.

**Resolution Required:** Verify item count requirements vs. current count.

### GAP 5: Content Readiness Status [CRITICAL MISSING]
**Issue:** No documentation of content production status.

**Missing Information:**
- Which pages have content drafted vs. ready for publishing?
- Which Fellou AI markdown samples are production-ready?
- Who is responsible for content creation?
- What is the content production timeline?

**Impact:** Technical implementation can proceed, but pages cannot launch without content.

**Why This Matters:** Content production is often the longest-lead-time item. Must be tracked.

**Resolution Required:** Content inventory + production schedule.

### GAP 6: Keyword-to-Page Mapping Not Implemented [CRITICAL MISSING]
**Issue:** Google Sheets has 600+ keywords with URL architecture mapped, but no evidence of implementation.

**Missing Information:**
- Which keywords are assigned to which pages in Wix CMS?
- How are target keywords being tracked per page?
- Are keywords being used to inform meta titles/descriptions?

**Impact:** SEO optimization cannot proceed without keyword-page assignments.

**Why This Matters:** Keyword targeting is foundational to SEO. Without this, optimization is guesswork.

**Resolution Required:** Implement keyword mapping in Wix CMS or external tracking system.

### GAP 7: Technical SEO Baseline Missing [CRITICAL MISSING]
**Issue:** No evidence of actual technical SEO audit execution.

**Missing Information:**
- No crawl data (Screaming Frog, Ahrefs, Semrush)
- No Core Web Vitals baseline
- No indexability audit
- No ranking data baseline

**Impact:** Cannot measure progress without baseline metrics.

**Why This Matters:** SEO is measured by change. No baseline = no measurement = no accountability.

**Resolution Required:** Execute full technical audit + capture baseline metrics.

### GAP 8: Ownership & Accountability Missing [MISSING]
**Issue:** No clear ownership assigned for tasks.

**Missing Information:**
- Who owns technical implementation?
- Who owns content production?
- Who owns SEO optimization?
- Who approves completed work?

**Impact:** Tasks without owners do not get completed.

**Why This Matters:** Accountability drives execution.

**Resolution Required:** Assign owners to all tasks.

### GAP 9: Content Production Timeline Missing [MISSING]
**Issue:** Fellou AI roadmap specifies 12-week build timeline, but no content production timeline exists.

**Missing Information:**
- When does each pillar page content need to be ready?
- When do spoke pages need content?
- How does content production align with technical build?

**Impact:** Technical build may outpace content production, creating idle time.

**Why This Matters:** Synchronization between technical and content workstreams is essential.

**Resolution Required:** Content production timeline aligned with Fellou AI build roadmap.

### GAP 10: Publishing Priority Not Defined [MISSING]
**Issue:** ~100 URLs mapped, but no indication of which should launch first.

**Missing Information:**
- Which pages are highest priority for launch?
- Should all pages launch together or in phases?
- What is the MVP (minimum viable product) for launch?

**Impact:** Without priorities, effort may be spread across all pages inefficiently.

**Why This Matters:** Focus drives completion. Broad focus leads to nothing being finished.

**Resolution Required:** Define publishing priorities and phasing strategy.

---
## PRIORITY TASK TIERS

Tasks are organized into 4 tiers based on blocking relationships and criticality:
- **TIER 1:** BLOCKERS — Must complete first, blocks all other work
- **TIER 2:** REQUIRES INPUT — Critical but needs decisions/clarifications before execution
- **TIER 3:** EXECUTION WORK — Can proceed after TIER 1 resolved
- **TIER 4:** ONGOING/PARALLEL — Can proceed during TIER 2-3 work

---

### TIER 1: BLOCKERS (Must Complete First)

These tasks MUST be completed before any implementation work can proceed. They establish the foundation and resolve contradictions that prevent execution.

#### TASK 1-1: Reconcile Homepage Architecture Specifications [BLOCKER]
**Category:** Strategic/Architecture  
**Priority:** P0 (Critical)  
**Status:** Unresolved contradiction  
**Blocking:** Homepage build, effort estimation, all downstream work

**Issue:**
- Fellou AI document specifies 6-7 section framework
- Session log (Nov 15) specifies 9 sections (Hero, Services Overview, Solutions Overview, Featured Case Study, Locations Preview, Insights Preview, Testimonials, CTA Banner, Footer)

**Decision Required:**
1. Is the 9-section specification from Nov 15 the authoritative specification?
2. Does Fellou AI's "6-7 section framework" refer to something different than the 9 sections?
3. Should the 9-section specification be followed for immediate implementation?

**Expert Recommendation:**
The 9-section specification from the Nov 15 session log is more detailed and implementation-ready. It includes specific section names with clear purpose. The Fellou AI "6-7 section framework" appears to be a high-level conceptual framework, not a detailed build specification.

**Recommended Resolution:**
Proceed with the 9-section specification from session log as the authoritative detailed implementation plan. The 9 sections align with standard homepage best practices:
1. Hero (above fold messaging)
2. Services Overview (primary offering preview)
3. Solutions Overview (solution categories preview)
4. Featured Case Study (social proof)
5. Locations Preview (geographic coverage)
6. Insights Preview (thought leadership)
7. Testimonials (social proof)
8. CTA Banner (conversion driver)
9. Footer (navigation + legal)

**Estimated Effort:** 0 hours (decision only)
**Owner:** Project Lead
**Dependency:** None
**Next Action:** Confirm 9-section specification as authoritative

---

#### TASK 1-2: Verify CMS Collection Binding Status [BLOCKER]
**Category:** Technical Verification  
**Priority:** P0 (Critical)  
**Status:** Contradiction between documentation sources  
**Blocking:** Item page work, repeater customization, content population

**Issue:**
- Session log (Nov 15) states: "All dynamic List/Item pages created and connected to datasets"
- open_tasks.md (Nov 24) lists: Binding tasks still needed for all collections

**Verification Required:**
1. Navigate to Wix Studio editor
2. Check each List page (Solutions, Services, Industries, Case Studies, Resources, Locations)
3. Verify if repeaters are bound to datasets
4. Verify if all fields (thumbnail, title, short_description, buttons) are mapped
5. Test repeaters with current CMS items to confirm display

**Possible Scenarios:**
- **Scenario A:** Bindings are complete, open_tasks.md is outdated → Focus shifts to Item pages
- **Scenario B:** Bindings are partial (some fields missing) → Complete remaining bindings
- **Scenario C:** Bindings not started → Session log was aspirational, not actual state

**Expert Recommendation:**
Based on open_tasks.md being more recent (Nov 24 vs. Nov 15), it is likely that bindings are incomplete. The session log may have documented the intent ("created and connected") but not the full implementation ("all fields bound and functioning").

**Recommended Resolution:**
Verify current state in Wix Studio immediately. Document current binding status with screenshots. If bindings incomplete, this becomes immediate next work.

**Estimated Effort:** 1-2 hours verification + documentation  
**Owner:** Technical Implementation  
**Dependency:** Wix Studio access  
**Next Action:** Login to Wix Studio, verify binding status, document current state

---

#### TASK 1-3: Establish Current Wix Studio State Inventory [BLOCKER]
**Category:** Documentation/Verification  
**Priority:** P0 (Critical)  
**Status:** Session log 11 days old, current state unknown  
**Blocking:** Accurate effort estimation, task prioritization, all implementation

**Issue:**
Session log from Nov 15 is the most recent documentation of Wix Studio state. 11 days have passed. Current state is unknown.

**Verification Required:**
1. **Homepage:** What sections/components exist? What's the current layout?
2. **Dynamic List Pages:** Which pages exist? What's on each page?
3. **Dynamic Item Pages:** Which templates exist? Are they customized?
4. **CMS Collections:** How many items in each collection? What fields populated?
5. **SEO Meta Data:** What titles/descriptions are set?
6. **Navigation:** What menu structure exists?
7. **Global Elements:** What header/footer configuration?

**Deliverable:**
Current state documentation with:
- Screenshot of each page
- List of CMS collections + item counts
- Repeater binding status per page
- SEO meta data status
- List of pending work items

**Expert Recommendation:**
This is foundational. Without current state knowledge, all planning is speculative. This must be first action.

**Recommended Resolution:**
1. Login to Wix Studio
2. Navigate through all pages
3. Screenshot each page (Published view + Editor view)
4. Document CMS collection contents
5. Create comprehensive current state inventory document
6. Update GitHub logs with current state

**Estimated Effort:** 2-3 hours  
**Owner:** Technical Implementation  
**Dependency:** Wix Studio access  
**Next Action:** Schedule immediate Wix Studio review session

---

### TIER 2: REQUIRES INPUT (Critical but Needs Decisions)

These tasks are critical for project success but require decisions, clarifications, or inputs before execution can begin.

#### TASK 2-1: Define Content Ownership & Production Schedule
**Category:** Project Management/Content  
**Priority:** P1 (High)  
**Status:** No documentation exists  
**Blocking:** Content production, launch readiness

**Issue:**
Technical build can proceed without content, but launch requires content. No content production plan documented.

**Decisions Required:**
1. Who owns content creation? (Internal team? Agency? Freelancer?)
2. What is content production capacity? (Words per week? Pages per week?)
3. What is the content approval process?
4. Which pages need original content vs. can use Fellou AI drafts?
5. What is the content production timeline aligned with Fellou AI 12-week roadmap?

**Expert Recommendation:**
Content production is typically the longest-lead-time item in SEO projects. If content owner is not identified and timeline not established, technical build will complete but site cannot launch.

**Recommended Resolution:**
1. Identify content owner/team
2. Assess content production capacity
3. Map content needs to Fellou AI build phases:
   - Phase 1 (Weeks 1-2): Homepage content + Services Hub content
   - Phase 2 (Weeks 3-4): 4 pillar page content
   - Phase 3 (Weeks 5-8): Spoke page content
   - Phase 4 (Weeks 9-12): Leaf page content
4. Create content production calendar with milestones
5. Document content approval workflow

**Estimated Effort:** 2-4 hours planning + ongoing content creation  
**Owner:** Project Manager + Content Lead  
**Dependency:** Content owner identification  
**Next Action:** Identify content owner, establish capacity, create timeline

---

#### TASK 2-2: Establish Keyword-to-Page Mapping in CMS
**Category:** SEO/Technical  
**Priority:** P1 (High)  
**Status:** Google Sheets has data, but not implemented in CMS  
**Blocking:** SEO optimization, meta data creation

**Issue:**
Google Sheets contains 600+ keywords with URL architecture. But no evidence this mapping exists in Wix CMS or is accessible during page optimization.

**Implementation Options:**
1. **Option A:** Add "target_keyword" field to each CMS collection, populate from Google Sheets
2. **Option B:** Create separate keyword tracking spreadsheet with page URL → keyword mapping
3. **Option C:** Use Google Sheets as source of truth, reference during optimization

**Expert Recommendation:**
Option A is cleanest — store target keyword directly in CMS. This makes it visible during page editing and ensures keyword targeting is not forgotten.

**Recommended Resolution:**
1. Add "target_keyword" field (text) to each CMS collection (Services, Solutions, Resources, Locations, Industries)
2. Add "supporting_keywords" field (text, comma-separated) to each collection
3. Populate fields from Google Sheets Architecture — Cleaned Map tab
4. Use these fields to inform meta title/description patterns
5. Document keyword assignment in GitHub

**Estimated Effort:** 3-4 hours  
**Owner:** SEO Architect + Technical Implementation  
**Dependency:** Wix Studio CMS access  
**Next Action:** Add keyword fields to CMS, populate from Google Sheets

---

#### TASK 2-3: Execute Technical SEO Audit & Establish Baseline
**Category:** Technical SEO  
**Priority:** P1 (High)  
**Status:** "Needs Verification" in task log — likely not done  
**Blocking:** Performance measurement, technical optimization priorities

**Issue:**
No baseline metrics documented. Cannot measure progress without baseline.

**Audit Components:**
1. **Crawl Audit:** Run Screaming Frog or Ahrefs crawl, export results
2. **Indexability Audit:** Check Google Search Console for indexation status
3. **Core Web Vitals:** Run PageSpeed Insights, capture LCP/FID/CLS scores
4. **Ranking Baseline:** Capture current rankings for target keywords (if any)
5. **Traffic Baseline:** Capture current GA4 traffic levels
6. **Backlink Baseline:** Capture current backlink profile (Ahrefs/Semrush)

**Expert Recommendation:**
Baseline is foundational for any SEO project. Must be captured before major changes are made.

**Recommended Resolution:**
1. Run full site crawl (Screaming Frog or Ahrefs)
2. Export crawl data to CSV
3. Run Core Web Vitals audit (PageSpeed Insights for key pages)
4. Check GSC for indexation status
5. Document current traffic (GA4 screenshot)
6. Capture backlink count (Ahrefs/Semrush)
7. Save all baseline data to GitHub (meztal_technical_baseline_2025-11-26.md)

**Estimated Effort:** 2-3 hours  
**Owner:** Technical SEO Architect  
**Dependency:** Tool access (Screaming Frog, Ahrefs, GSC, GA4)  
**Next Action:** Schedule technical audit, document baseline

---### TIER 3: EXECUTION WORK (Proceed After TIER 1 Resolved)

These are implementation tasks that can proceed once TIER 1 blockers are resolved.

#### TASK 3-1: Complete Home Page 9-Section Build in Wix
**Category:** Technical Implementation  
**Priority:** P2 (Medium-High)  
**Status:** Foundation started (2-row grid), 7 sections remaining  
**Blocking:** Item page display, content population

**Scope:**
Build remaining 7 homepage sections (assuming grid foundation already complete):
1. Hero section
2. Services Overview (with repeater)
3. Solutions Overview (with repeater)
4. Featured Case Study
5. Locations Preview (with repeater)
6. Insights Preview (with repeater)
7. Testimonials
8. CTA Banner
9. (Footer - assuming already exists)

**Implementation Steps Per Section:**
1. Add section container to grid
2. Add heading, paragraph, and decorative elements
3. Add repeater (for Services/Solutions/Locations/Insights)
4. Connect repeater to appropriate CMS collection
5. Bind repeater fields (thumbnail, title, short_description, button)
6. Test display with existing CMS items
7. Adjust spacing, typography, responsiveness

**Estimated Effort:** 60-80 Wix Studio interactions, 4-6 hours  
**Owner:** Technical Implementation  
**Dependency:** TASK 1-1 (homepage spec confirmed), TASK 1-3 (current state known)  
**Next Action:** Once blockers resolved, begin section-by-section build

---

#### TASK 3-2: Build & Customize Item Page Templates
**Category:** Technical Implementation  
**Priority:** P2 (Medium-High)  
**Status:** Pages "created and connected" per session log, but customization unclear  
**Blocking:** Dynamic content display, user experience

**Scope:**
Customize Item page templates for each collection:
1. **Services Item Page:** Service details, benefits, CTA
2. **Solutions Item Page:** Solution details, use cases, CTA
3. **Resources Item Page:** Resource content display
4. **Locations Item Page:** Location details, contact info
5. **Industries Item Page:** Industry-specific messaging
6. **Case Studies Item Page:** Case study details, results

**Implementation Per Template:**
1. Add hero section with dynamic title/image
2. Add main content area with rich text field binding
3. Add sidebar with related items (repeater)
4. Add CTA section
5. Add breadcrumb navigation
6. Set SEO patterns (title, description, slug)
7. Test with actual CMS items

**Estimated Effort:** 40-50 Wix Studio interactions per template, 6-8 hours total  
**Owner:** Technical Implementation  
**Dependency:** TASK 1-2 (CMS binding verified), TASK 1-3 (current state known)  
**Next Action:** Once CMS bindings confirmed, customize Item templates

---

#### TASK 3-3: Build Contact & About Pages
**Category:** Technical Implementation  
**Priority:** P2 (Medium)  
**Status:** Not started per session log  
**Blocking:** Site completeness, user trust

**Scope:**
- **Contact Page:** Contact form, office locations, phone/email
- **About Page:** Company story, team, mission/values

**Implementation:**
1. Create Contact page
   - Add Wix Forms contact form
   - Add locations map (if applicable)
   - Add contact details
   - Set SEO meta data
2. Create About page
   - Add company story content
   - Add team section (could use repeater if team CMS exists)
   - Add mission/values
   - Set SEO meta data

**Estimated Effort:** 3-4 hours  
**Owner:** Technical Implementation  
**Dependency:** Content for About page  
**Next Action:** Create pages once content available

---

### TIER 4: ONGOING/PARALLEL (Can Proceed During TIER 2-3)

These tasks can proceed in parallel with other work or are ongoing activities.

#### TASK 4-1: Content Production for Priority Pages
**Category:** Content Creation  
**Priority:** P1 (High)  
**Status:** Fellou AI has markdown drafts, but production readiness unclear  
**Blocking:** Launch readiness

**Scope:**
Create production-ready content for:
1. **Homepage:** All 9 section content (headlines, paragraphs, CTAs)
2. **Services Hub:** Main services overview page
3. **Pillar Pages (4):** IT Staffing, Accounting Solutions, Call Center, Finance & Accounting
4. **Spoke Pages:** Supporting pages for each pillar
5. **Leaf Pages:** Detailed comparison and resource pages

**Content Requirements Per Page:**
- Primary headline (H1)
- Supporting headlines (H2, H3)
- Body content (400-1500 words depending on page type)
- CTAs (calls-to-action)
- Meta title (55-60 characters)
- Meta description (150-160 characters)
- Image alt text

**Estimated Effort:** Ongoing, 2-4 pages per week depending on content capacity  
**Owner:** Content Team  
**Dependency:** TASK 2-1 (content owner identified)  
**Next Action:** Begin with Homepage content, then pillar pages

---

#### TASK 4-2: SEO Optimization & Schema Implementation
**Category:** Technical SEO  
**Priority:** P2 (Medium)  
**Status:** Planned but not started  
**Blocking:** Search visibility, SERP appearance

**Scope:**
1. **Schema Markup:**
   - Organization schema (homepage)
   - Service schema (service pages)
   - LocalBusiness schema (location pages)
   - Breadcrumb schema (all pages)
   - FAQ schema (where applicable)
2. **On-Page SEO:**
   - Optimize title tags (keyword-focused, 55-60 chars)
   - Optimize meta descriptions (compelling, 150-160 chars)
   - Optimize H1/H2 hierarchy
   - Optimize image alt text
   - Add internal linking
3. **Technical Elements:**
   - Canonical tags
   - hreflang (if multi-language)
   - robots.txt optimization
   - XML sitemap generation

**Estimated Effort:** Ongoing, 2-3 hours per batch of 10 pages  
**Owner:** Technical SEO Architect  
**Dependency:** Pages built, content added, keywords mapped  
**Next Action:** Begin after pages are built and content added

---

#### TASK 4-3: Competitor Analysis & Gap Identification
**Category:** SEO Strategy  
**Priority:** P2 (Medium)  
**Status:** Listed in open tasks as "Planned (AI)"  
**Blocking:** Content differentiation, competitive advantage

**Scope:**
1. Identify top 5-10 competitors in each service area
2. Analyze competitor content strategy
3. Identify keyword gaps (keywords competitors rank for that MezTal doesn't)
4. Identify content gaps (topics competitors cover that MezTal doesn't)
5. Analyze competitor backlink profiles
6. Document competitive advantages and differentiators

**Deliverable:**
Competitor analysis report with:
- Competitor keyword rankings
- Content gap analysis
- Backlink gap analysis
- Recommendations for differentiation

**Estimated Effort:** 4-6 hours  
**Owner:** SEO Strategist  
**Dependency:** Tool access (Ahrefs, Semrush)  
**Next Action:** Run competitor analysis once baseline complete

---

#### TASK 4-4: Link Building & Outreach
**Category:** Off-Page SEO  
**Priority:** P3 (Medium-Low)  
**Status:** Not started  
**Blocking:** Domain authority, referral traffic

**Scope:**
1. Identify link building opportunities:
   - Industry directories
   - Partner websites
   - Resource pages
   - Guest posting opportunities
2. Create outreach templates
3. Execute outreach campaigns
4. Track link acquisition

**Estimated Effort:** Ongoing, 2-4 hours per week  
**Owner:** SEO Outreach Specialist  
**Dependency:** Content published, site launched  
**Next Action:** Begin after initial content published

---

## CRITICAL PATH & DEPENDENCIES

### Immediate Next Steps (Week 1)

**Day 1: Resolve TIER 1 Blockers**
1. **TASK 1-1:** Confirm 9-section homepage specification (0 hours, decision)
2. **TASK 1-3:** Login to Wix Studio, document current state (2-3 hours)
3. **TASK 1-2:** Verify CMS binding status (1-2 hours)

**Day 2-3: TIER 2 Foundation**
4. **TASK 2-1:** Identify content owner, establish timeline (2-4 hours)
5. **TASK 2-3:** Run technical SEO audit, establish baseline (2-3 hours)
6. **TASK 2-2:** Add keyword fields to CMS, populate from Google Sheets (3-4 hours)

**Day 4-5: Begin TIER 3 Implementation**
7. **TASK 3-1 (Phase 1):** Build first 3 homepage sections (2-3 hours)
8. **TASK 4-1 (Parallel):** Begin homepage content creation

### Week 2-4: Core Implementation
- Complete all homepage sections (TASK 3-1)
- Customize Item page templates (TASK 3-2)
- Populate CMS with priority content
- Begin pillar page builds

### Week 5-8: Content & Optimization
- Build spoke pages
- Implement schema markup (TASK 4-2)
- Optimize all pages for SEO
- Run competitor analysis (TASK 4-3)

### Week 9-12: Polish & Launch
- Build leaf pages
- Build Contact/About pages (TASK 3-3)
- Final QA and testing
- Launch preparation
- Begin link building (TASK 4-4)

---

## SUMMARY OF PRIORITY RECOMMENDATIONS

### IMMEDIATE ACTIONS (Do First, This Week)

1. **Login to Wix Studio** and document current state (TASK 1-3)
   - Screenshot all pages
   - List CMS collection contents
   - Verify binding status
   - **This unblocks all planning and implementation**

2. **Confirm homepage specification** (TASK 1-1)
   - Proceed with 9-section specification from session log
   - **This unblocks homepage build**

3. **Run technical SEO baseline audit** (TASK 2-3)
   - Crawl site
   - Capture metrics
   - Document baseline
   - **This establishes measurement framework**

### CRITICAL DECISIONS NEEDED

1. **Content Owner:** Who will create content? Timeline?
2. **Publishing Priority:** Which pages launch first? MVP definition?
3. **Resource Allocation:** Who owns technical implementation vs. SEO vs. content?

### BLOCKED UNTIL RESOLVED

- All implementation work is blocked until TIER 1 tasks (current state verification) complete
- Content production is blocked until content owner identified (TASK 2-1)
- SEO optimization is blocked until keyword fields added to CMS (TASK 2-2)
- Launch is blocked until content created and technical implementation complete

### EFFORT SUMMARY

**TIER 1 (Blockers):** 3-5 hours to resolve  
**TIER 2 (Requires Input):** 7-11 hours foundation work  
**TIER 3 (Execution):** 13-18 hours core implementation  
**TIER 4 (Ongoing):** Ongoing throughout project lifecycle  

**Total Immediate Work (TIER 1 + TIER 2):** 10-16 hours to unblock all execution

---

## CONCLUSION

This analysis identifies **10 critical gaps** across documentation, technical implementation, and project governance. **3 TIER 1 blockers** must be resolved before any implementation work can proceed:

1. Reconcile homepage architecture specifications
2. Verify CMS collection binding status
3. Establish current Wix Studio state inventory

Once these blockers are resolved, **6 TIER 2-4 tasks** can begin in parallel, following the critical path outlined above.

The highest-ROI immediate action is **TASK 1-3** (Wix Studio current state inventory), which will provide clarity on all remaining work and enable accurate effort estimation.

**Next Session Recommendation:**
Begin with TASK 1-3 (Wix Studio state inventory). Allocate 2-3 hours to thoroughly document current state, then update GitHub logs. This will provide the foundation for all subsequent work.

---

**Document Status:** Complete  
**Analysis Date:** November 26, 2025  
**Analyst:** Perplexity (Comet) — Project Lead & SEO Architect

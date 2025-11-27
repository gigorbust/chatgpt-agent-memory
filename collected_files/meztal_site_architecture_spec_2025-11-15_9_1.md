# MEZTAL SITE ARCHITECTURE SPECIFICATION
## NO TIMELINES - PURE STRUCTURAL SPEC

---

## THE CURRENT STATE

Your existing hierarchy is solid for UX. But it's **keyword-agnostic**. It organizes by business logic (Services, Industries, Locations) not by search intent.

---

## THE GAP

You have 12 high-value keywords from Semrush that your current structure does NOT capture:

- "remote employees mexico" (3,600/mo, difficulty 45)
- "employer of record mexico" (2,400/mo, difficulty 52)
- "outsourcing mexico" (2,100/mo, difficulty 48)
- "hire remote developers mexico" (1,600/mo, difficulty 55)
- "nearshore staffing mexico" (1,200/mo, difficulty 35)
- "mexico payroll services" (1,200/mo, difficulty 38)
- "remote work mexico legal" (890/mo, difficulty 42)

None of these keywords have dedicated landing pages. They don't exist in your hierarchy.

---

## REQUIRED ARCHITECTURE ADDITIONS

### 1. KEYWORD LANDING PAGES (7 TOTAL)

Each of these must exist as a dedicated page:

```
/remote-employees-mexico/
  - Hero: "Hire Remote Employees in Mexico"
  - Problem/solution narrative
  - How it works (3-5 steps)
  - FAQ section
  - CTA: "Get Started" → /contact
  - Related: Links to /remote-work-mexico-legal, /remote-work-mexico-taxes, /nearshore-vs-outsourcing
  - Meta: Title, description optimized for keyword

/employer-of-record-mexico/
  - Hero: "Employer of Record in Mexico"
  - EOR definition, benefits, use cases
  - Legal compliance info (with disclaimer)
  - Comparison: EOR vs. staffing vs. outsourcing
  - CTA: "Learn More" → /contact
  - Related: /eor-vs-staffing, /eor-legal-requirements-mexico

/outsourcing-mexico/
  - Hero: "Nearshore Outsourcing in Mexico"
  - What outsourcing means, why Mexico
  - Service categories (IT, accounting, customer service, etc.)
  - Case studies embedded
  - CTA: "Explore Services" → /services
  - Related: /outsourcing-vs-remote, /nearshore-vs-outsourcing

/hire-remote-developers-mexico/
  - Hero: "Hire Remote Developers in Mexico"
  - Developer roles available
  - Hiring process explained
  - Skill matrix by role
  - Case studies
  - CTA: "Hire Developers" → /contact
  - Related: /hire-python-developers-mexico, /hire-software-engineers-mexico

/nearshore-staffing-mexico/
  - Hero: "Nearshore Staffing in Mexico"
  - Definition of nearshore
  - Why Mexico vs. other locations
  - Staffing models
  - Pricing/cost information
  - CTA: "Build Your Team" → /contact
  - Related: /nearshore-vs-outsourcing, /nearshore-staffing-costs

/mexico-payroll-services/
  - Hero: "Mexico Payroll Services"
  - Payroll compliance requirements
  - Tax implications
  - Payroll structure
  - Interactive calculator
  - CTA: "Get Payroll Setup" → /contact
  - Related: /payroll-tax-mexico, /compliance-checklist

/remote-work-mexico-legal/
  - Hero: "Legal Requirements for Remote Work in Mexico"
  - Employment law overview
  - Compliance checklist
  - Common pitfalls
  - Links to compliance guides
  - CTA: "Download Compliance Guide" → gated form
  - Related: /remote-work-mexico-taxes, /eor-legal-requirements-mexico
```

### 2. TOPICAL AUTHORITY HUBS (5 TOTAL)

These are hub pages that group related content for semantic SEO:

```
/remote-work-mexico/ (HUB PAGE)
  Purpose: Establish topical authority around "remote work in mexico"
  Contains:
    - Introduction to remote work in Mexico
    - Hub navigation to:
      • /remote-employees-mexico/ (landing page)
      • /remote-work-mexico-legal/ (support page)
      • /remote-work-mexico-taxes/ (support page)
      • /remote-work-mexico-skills/ (support page - what skills are available)
    - All hub pages link BACK to /remote-work-mexico/ as parent
    - Internal linking: Each related page links to 2-3 other pages in cluster

/nearshore-staffing/ (HUB PAGE)
  Purpose: Authority on "nearshore staffing"
  Contains:
    - /nearshore-staffing-mexico/ (landing page)
    - /nearshore-vs-outsourcing/ (comparison)
    - /nearshore-staffing-costs/ (pricing guide)
    - /nearshore-staffing-industries/ (by vertical)

/employer-of-record/ (HUB PAGE)
  Purpose: Authority on "employer of record mexico"
  Contains:
    - /employer-of-record-mexico/ (landing page)
    - /eor-vs-staffing/ (comparison)
    - /eor-legal-requirements-mexico/ (compliance)

/outsourcing/ (HUB PAGE)
  Purpose: Authority on "outsourcing mexico"
  Contains:
    - /outsourcing-mexico/ (landing page)
    - /outsourcing-vs-remote/ (comparison)
    - /outsourcing-it-mexico/ (vertical deep dive)

/hiring-developers/ (HUB PAGE)
  Purpose: Authority on "hire developers mexico"
  Contains:
    - /hire-remote-developers-mexico/ (landing page)
    - /hire-python-developers-mexico/ (specialty)
    - /hire-software-engineers-mexico/ (specialty)
    - /hire-mobile-developers-mexico/ (specialty)
```

### 3. AUTHORITY/RESOURCE LAYER

These are content assets that build trust and capture leads:

```
/guides/ (COLLECTION)
  /mexico-staffing-guide/
    - Comprehensive guide (3k-5k words)
    - Downloadable PDF
    - Email capture gate
    - Covers: hiring process, costs, compliance, timeline

  /mexico-legal-guide/
    - Employment law guide
    - Gated, email signup
    - Compliance requirements
    - Common mistakes

  /remote-work-tax-guide-mexico/
    - Tax implications for remote work
    - Withholding requirements
    - Payroll tax calculations
    - Email gated

  /compliance-checklist/
    - Downloadable checklist
    - Email gated
    - Pre-fill with form data

/tools/ (COLLECTION)
  /staffing-cost-calculator/
    - Interactive calculator
    - Email required to see results
    - Outputs: cost breakdown by role/location

  /salary-benchmark-mexico/
    - Role-based salary comparison
    - Interactive filters (role, location, experience)
    - Email optional, tracked as engagement

  /hiring-cost-comparison/
    - Compare: in-house vs. remote vs. outsourcing costs
    - Interactive model
```

### 4. CASE STUDIES COLLECTION (REQUIRED SPEC)

```
Collection Schema:
  - client_name (string)
  - industry (reference to Industries collection)
  - challenge (rich text)
  - solution (rich text)
  - results (rich text)
  - metrics (array: before/after KPIs)
  - testimonial_quote (string)
  - testimonial_author (string)
  - featured (boolean - for home page rotation)
  - featured_image (image)
  - locations_involved (array)

Display Logic:
  - /case-studies/ (list page) - shows all case studies
  - /case-studies/{slug} (detail page)
    - Related case studies by industry (3-4 recommended)
    - CTA: "Let's Build Your Success Story" → /contact
  - Industry pages (/industries/{slug}) - embedded case studies filtered by industry (3 most recent)
  - Home page - featured case study rotation (1 case study, updates weekly or monthly)
```

### 5. COMPARISON PAGES (REQUIRED)

```
/nearshore-vs-outsourcing/
  - Side-by-side comparison table
  - Pros/cons of each model
  - When to use each
  - Cost comparison
  - Timeline comparison
  - Risk analysis
  - CTA: "Choose Your Model" → /contact

/eor-vs-staffing/
  - What's the difference
  - Cost implications
  - Legal responsibility matrix
  - Timeline to implementation
  - Best use cases
  - CTA: "Discuss Your Needs" → /contact

/outsourcing-vs-remote/
  - Definition differences
  - Management differences
  - Control vs. cost tradeoff
  - Compliance differences
  - When to choose each
```

### 6. INTERNAL LINKING SPECIFICATION (MANDATORY)

```
Linking Topology:

HERO PAGES (money keywords):
  - Link FROM: Home page, hub pages, navigation
  - Link TO: 2-3 related pages in same cluster + 1-2 support pages + /contact
  - Anchor text: Include variations of target keyword

HUB PAGES:
  - Link FROM: Home page, navigation, footer
  - Link TO: All child pages in cluster
  - Child pages link BACK to hub
  - Sibling linking: Each child page links to 2-3 other sibling pages

BLOG/RESOURCES:
  - "Related Articles" section: 3-4 posts from same category
  - "Continue Reading" in footer: link to relevant landing page or hub
  - Email CTA: includes link back to main service page

CONVERSION PAGES:
  - /contact page: linked from every hero page, every hub page, every guide
  - Calendly/demo page: linked from all decision-stage pages (comparisons, case studies)

Breadcrumb Navigation:
  - Home > [Hub] > [Page]
  - Home > [Industry] > [Page]
  - Home > [Blog Category] > [Page]
```

### 7. CONVERSION ARCHITECTURE (REQUIRED SPEC)

```
AWARENESS PAGES (goal: read + email capture):
  - /guides/* (all guide pages)
  - /resources/* (blog posts)
  - /remote-work-mexico-legal/ (educational, not conversion-heavy)
  - CTA: "Download Guide" or "Email Me Updates"

CONSIDERATION PAGES (goal: start conversation):
  - /remote-employees-mexico/ (all hero pages)
  - /nearshore-staffing-mexico/
  - /outsourcing-mexico/
  - /hire-remote-developers-mexico/
  - /employer-of-record-mexico/
  - CTA: "Get Started", "Learn More", "Schedule Call"

DECISION PAGES (goal: book consultation):
  - /case-studies/ (proof)
  - /nearshore-vs-outsourcing/ (comparison)
  - /eor-vs-staffing/ (comparison)
  - CTA: "Schedule Consultation", "Talk to Specialist"

ACTION PAGES (conversion):
  - /contact (form submission)
  - Calendar booking page (scheduled call)
  - Demo page (if applicable)
  - CTA: "Book Now", "Submit"
```

---

## WHAT STAYS UNCHANGED

✅ /services collection and /services/{slug} pages
✅ /industries collection and /industries/{slug} pages  
✅ /locations collection and /locations/{slug} pages
✅ /resources collection (expand with taxonomy, don't replace)
✅ /contact page and form structure
✅ Global header, footer, colors, typography
✅ Home page layout (add new sections for new content types)

---

## PRIORITY DEPENDENCIES

1. **Must exist before launch:** All 7 keyword landing pages
2. **Must exist before launch:** Internal linking topology documented and implemented
3. **Strongly recommended before launch:** 5 hub pages to establish topical authority
4. **Can follow launch:** Case studies section, comparison pages, tools/guides

---

## STRUCTURAL REQUIREMENTS

### On-Page SEO Per Page
- Meta title (50-60 chars, includes target keyword)
- Meta description (150-160 chars, includes keyword variation)
- H1 (single, includes keyword variation)
- H2-H3 hierarchy (logical structure, 2-3 variations of keyword in body)
- Image alt text (includes keyword where natural)
- Internal links (3-5 contextual links per page)
- External links (1-2 high-authority, relevant sources)

### Technical Requirements
- Mobile responsive (tested on 3+ devices)
- Page speed: Load time < 3 seconds (measure via PageSpeed Insights)
- Schema markup: Organization, LocalBusiness (for Mexico operations), Product/Service
- Open Graph tags (for social sharing)
- Canonical tags (prevent duplicate content issues)

### Conversion Requirements
- All pages: minimum 1 CTA button
- Hero pages: 2-3 CTAs (top, middle, bottom)
- Guides: email capture form
- Contact page: phone + Calendly embed + email
- Forms: maximum 3-4 fields (name, email, company, +1 custom field per page type)

---

## BOTTOM LINE

Your current hierarchy is **UX-solid but SEO-incomplete**. This spec adds:

- **7 keyword landing pages** (capture high-intent search traffic)
- **5 hub pages** (establish topical authority for semantic SEO)
- **Authority layer** (guides, calculators, case studies)
- **Internal linking topology** (distribute authority strategically)
- **Conversion clarity** (every page type has defined goal)

This is the architecture. Build it. No timeline imposed.

# MezTal Sandbox Audit - Detailed Findings
## Date: November 15, 2025

---

## EXECUTIVE SUMMARY

Detailed audit of the Wix Studio sandbox (metaSiteId: 24c6a184-1fd5-4b8c-ade1-8f2dae9c8f9e) has been completed. Critical gaps identified between live meztal.com site and sandbox implementation.

**Key Finding:** Sandbox contains extensive infrastructure pages but is MISSING critical business pages required for MezTal brand functionality.

---

## SECTION 1: SANDBOX PAGE INVENTORY

### 1.1 Main Pages Structure

**Currently Existing Pages:**

#### Core Pages (8 primary)
1. **Home** - EXISTS but EMPTY (requires hero, value props, testimonials)
2. **Main Services Hub** - EXISTS
3. **Industries** - EXISTS
4. **Locations** - EXISTS
5. **Resources** - EXISTS
6. **About** - EXISTS
7. **Contact** - EXISTS (minimal content; could repurpose for Apply Now)
8. **IT Staffing & Development** - EXISTS

#### Missing Critical Pages (3 CRITICAL GAPS)
1. **Apply Now** - ❌ DOES NOT EXIST
2. **Team** - ❌ DOES NOT EXIST
3. **FAQ** - ❌ DOES NOT EXIST

#### Additional Infrastructure Pages (40+ pages)
- Application Development Outsourcing
- Digital Marketing
- Accounting & Finance
- HR & Talent Acquisition
- services
- Call Center Outsourcing
- Finance & Accounting Outsourcing
- sales-solutions
- Accounting Solutions
- IT Staffing
- Accounting Outsourcing
- Payroll Outsourcing
- Tax Services
- Top IT Outsourcing Companies
- Top Software Development Companies
- Top BPO Companies
- Best Accounting Firms
- Best IT Staffing Companies
- Administrative Outsourcing
- Design Outsourcing
- Accounting Services
- Best Outsourcing Companies
- Nearshore Staffing Mexico
- Remote Workers Mexico
- Mexico Outsourcing
- Hire Developers Mexico
- Remote Teams Mexico
- Employer of Record Mexico
- (Plus many more service/category pages)

**Note:** These infrastructure pages appear to be remnants from a previous implementation or template. They are NOT aligned with MezTal's clean, minimal business focus.

### 1.2 Dynamic Pages (Collection-Based)

**Dynamic Page Templates Identified:**
- Case_studies Pages (Dynamic) with Item/List variants
- Industries Pages (Dynamic) with Item/List variants
- Locations Pages (Dynamic) with List view
- Resources Pages (Dynamic) with Item/List variants
- Roles Pages (Dynamic) with Item/List variants
- Services Pages (Dynamic) with Item/List variants
- Solutions Pages (Dynamic) with Item/List variants

### 1.3 Static Pages

**Recently Created:**
- Why Guadalajara? - ✅ CREATED (parent: Locations, URL: /locations/why-guadalajara)

---

## SECTION 2: COLLECTIONS & CMS STATUS

### Collections Verified as Working
✅ Solutions Collection - verified with 3 items
✅ Industries Collection - verified with 1 item
✅ Locations Collection - verified with 2-3 items (Mexico City, Guadalajara, Houston)

### Collections Need Verification/Creation
⚠️ Testimonials Collection - STATUS UNKNOWN (needed for Home page)
⚠️ Team Members Collection - STATUS UNKNOWN (needed for Team page)
⚠️ FAQ Collection - STATUS UNKNOWN (needed for FAQ page)

---

## SECTION 3: DETAILED GAP ANALYSIS

### 3.1 Home Page Status

**Current State:** Basic template with "Business Name" branding
**Content:** Essentially empty
**Design:** Minimal (brand compliant)

**Required Additions:**
- Hero banner with orange background (#F5A623)
- Tagline: "MezTal helps you find exceptional talent and builds a connected community for mission-driven teams."
- 3 value proposition cards (Team, Savings, Management)
- "Staffing like you've never seen" content section with image
- 3 testimonials section (2 client cards with orange frames, 1 employee card with blue frame)
- CTA: "Add highly qualified talent to your team"

**Collection Dependencies:** Testimonials collection

### 3.2 Apply Now Page Gap

**Current State:** ❌ PAGE DOES NOT EXIST

**Implementation Options:**
- OPTION A: Rename/repurpose existing "Contact" page
- OPTION B: Create new dedicated "Apply Now" page

**Recommended:** Create new dedicated page (maintains proper hierarchy and naming)

**Required Content:**
- Heading: "Do you want to be a part of a growing team who cares about you?"
- "Apply Now!" button (orange styling)
- "Review our current employment opportunities and apply here" link
- "Connect With Us!" section
- Contact form (Name, Email, Subject, Message fields)
- Submit button styling (orange border)

### 3.3 Team Page Gap

**Current State:** ❌ PAGE DOES NOT EXIST

**Required Content:**
- Page heading: "Meet Our Team"
- 5 team member profile cards:
  1. Sarah Thomas - Partner/CEO (orange frame)
  2. Vincent Gerbec - VP of Business Development (blue frame)
  3. Luis Alcaraz - Country Manager (orange frame)
  4. Noemi Esparza - Head of Special Projects/Executive Assistant (orange frame)
  5. Chris Geno - CFO (blue frame)
- "Connect with us to learn more about MezTal" CTA
- Email link: info@meztal.com

**Collection Dependencies:** Team Members collection (requires creation)

### 3.4 FAQ Page Gap

**Current State:** ❌ PAGE DOES NOT EXIST

**Required Content:**
- Page heading: "Frequently Asked Questions"
- Subheading: "Ask away!"
- 4 expandable FAQ items:
  1. "Why Guadalajara?" - Multi-paragraph explanation
  2. "What is the cost to hire roles at Meztal?" - Cost structure + role examples
  3. "What is included in the 'passthrough fee'?" - Fee breakdown
  4. "What control do I have on my team member?" - Control details

**Collection Dependencies:** FAQ collection (requires creation)

---

## SECTION 4: IMPLEMENTATION PRIORITY

### IMMEDIATE - CRITICAL (Must Complete)
1. ✅ Home Page - Populate with hero, value props, testimonials
2. ❌ Apply Now Page - Create new page
3. ❌ Team Page - Create new page
4. ❌ FAQ Page - Create new page

### HIGH PRIORITY (Collections)
1. Create/populate Testimonials collection (3 items)
2. Create/populate Team Members collection (5 items)
3. Create/populate FAQ collection (4 items)

### CLEANUP - FUTURE (Non-Critical)
1. Audit and remove or consolidate 40+ infrastructure pages not aligned with MezTal brand
2. These pages appear to be template remnants and clutter the sitemap
3. Decision needed: Keep for SEO/archival or remove for clean structure

---

## SECTION 5: CRITICAL CONSTRAINTS

✅ **BRAND COMPLIANCE:**
- Color scheme: Orange #F5A623, Blue #2E5C8A
- Design language: Minimal, clean, professional
- NO decorative elements
- Proper white space
- Consistent typography

✅ **HIERARCHY & ORGANIZATION:**
- Home is root page
- Apply Now - SHOULD BE TOP-LEVEL PAGE (not under Home)
- Team - SHOULD BE TOP-LEVEL PAGE (not under Home)
- FAQ - SHOULD BE TOP-LEVEL PAGE (not under Home)
- Consult cleaned map in Google Sheet for proper hierarchy

✅ **SANDBOX SECURITY:**
- Verify metaSiteId: 24c6a184-1fd5-4b8c-ade1-8f2dae9c8f9e before any edits
- NEVER edit live meztal.com site
- ONLY work in sandbox

---

## SECTION 6: NEXT IMMEDIATE STEPS

### Phase 2, Step 3: Collections Setup
1. Navigate to Collections/CMS in Wix Studio
2. Create "Testimonials" collection with fields:
   - Name (text)
   - Title (text)
   - Quote (long text)
   - Type (single select: Client vs Employee)
   - CardColor (single select: Orange vs Blue)
3. Add 3 testimonial items
4. Create "Team Members" collection with fields:
   - Name (text)
   - Title (text)
   - Photo (image)
   - PhotoFrameColor (single select: Orange vs Blue)
5. Add 5 team member items
6. Create "FAQ" collection with fields:
   - Question (text)
   - Answer (long text)
7. Add 4 FAQ items

### Phase 2, Step 4: Page Implementation
1. Populate Home page with all sections
2. Create Apply Now page from scratch
3. Create Team page with collection binding
4. Create FAQ page with expandable sections
5. Apply all styling and branding

---

## SECTION 7: REFERENCES

**Primary Documentation:**
- Gap Analysis File: meztal_gap_analysis_live_vs_sandbox_2025-11-15.md
- Foundation Completion: meztal_wix_studio_foundation_completion_2025-11-15.md
- Live Site Reference: https://www.meztal.com/
- Sandbox URL: https://editor.wix.com/studio/792fe01d-fa28-4833-b811-b5a540f5568b?metaSiteId=24c6a184-1fd5-4b8c-ade1-8f2dae9c8f9e

**Authoritative Source:**
- Google Sheet: MEZTAL_SEO_MASTER_Minimal_2025-09-22_R3
- Cleaned Map Tab (gid=921062424) - SOURCE OF TRUTH FOR HIERARCHY

---

## Document Metadata

- **Created:** November 15, 2025
- **Audit Scope:** Complete Wix Studio sandbox inventory
- **Pages Scanned:** All pages in Site Pages panel
- **Method:** Manual page-by-page audit + search verification
- **Status:** Phase 2 Step 2 Complete
- **Next Phase:** Collections setup and page implementation

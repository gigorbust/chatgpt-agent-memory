# MezTal Wix Studio Site Architecture Analysis
## Foundation Phase - Session 2025-11-15

### Executive Summary
This document outlines critical findings from analyzing the MezTal Wix Studio sandbox site structure against the authoritative "Architecture — Cleaned Map" in the MEZTAL_SEO_MASTER Google Sheet. The 7 Mexico-focused pages currently exist at the HOME level with no parent page hierarchy, requiring reorganization to align with proper information architecture.

---

## Critical Context
- **Project**: MezTal website rebuild in Wix Studio (sandbox environment only)
- **Client Base**: 100% USA-focused
- **Value Proposition**: Mexico-based team delivery for USA companies
- **Priority**: NOT geographic hubs (city-by-city within Mexico), but country-level value proposition pages
- **Key Instruction**: RIGHT-CLICK and DOUBLE-CLICK do NOT work in browser environments - use context menus and left-click only

---

## Current State Analysis

### Sandbox Pages (7 Mexico Pages)
Located at HOME level with URLs:
1. `/nearshore-staffing-mexico` → "Nearshore Staffing Mexico"
2. `/remote-workers-mexico` → "Remote Workers Mexico"
3. `/mexico-outsourcing` → "Mexico Outsourcing"
4. `/hire-developers-mexico` → "Hire Developers Mexico"
5. `/remote-teams-mexico` → "Remote Teams Mexico"
6. `/employer-of-record-mexico` → "Employer of Record Mexico"
7. (7th page - needs identification)

**Current Parent**: ALL pages = HOME
**Current Status**: NO parent page hierarchy

### Authoritative Source: Cleaned Map Analysis

#### What EXISTS in Cleaned Map:
- **Geographic Hubs** (15+ locations): `/locations/staffing-solutions-CITY`
  - Examples: Cancun, Culiacan, Hermosillo, Juarez, Leon, Merida, Mexicali, Monterrey, Puebla, Querétaro, Saltillo, San Luis Potosí, Tijuana, Torreon, Tusla, Villaahermosa
  - **Topic Cluster**: Geographic Hubs
  - **NOT Priority** per user clarification

- **Mexico City Comparison**: `/comparison/cost-of-living-in-guadalajara-vs-mexico-city`
  - **Topic Cluster**: Geographic Hubs
  - **Page Type**: Spoke (comparison)
  - Single Mexico-specific comparison page

#### What DOES NOT Exist in Cleaned Map:
- "Nearshore Staffing" pages (0 results)
- "Remote Workers" pages (0 results)
- Any country-level Mexico staffing value proposition pages

**Implication**: The 7 sandbox pages represent STRATEGIC VALUE PROPOSITION PAGES beyond the initial cleaned map scope. They're intentionally different from geographic hubs.

---

## Cleaned Map URL Architecture Patterns

The authoritative source uses SERVICE-BASED hierarchies, NOT LOCATION-BASED:

```
/services/[service-type]                    (Pillar Pages)
/comparison/[solution-comparison]           (Comparison Pages)
/resources/[guides-glossaries]              (Resource Pages)
```

**NOT**:
```
/mexico/[service-type]                      (Location subdirectory)
/locations/staffing-solutions-[city]        (Only for geographic hubs, lower priority)
```

---

## Key Findings

### Finding 1: Parent Page Hierarchy Missing
- The 7 Mexico pages have NO parent page assignments (all showing "Home" as parent)
- This violates the architectural principle: "The parent of every page cannot be HOME"
- **Action Required**: Assign appropriate parent pages

### Finding 2: URL Structure Strategy
- Current flat URLs (`/nearshore-staffing-mexico`) are acceptable for value proposition pages
- No need to relocate to `/services/` or `/locations/` routes
- These are distinct from the cleaned map's geographic hub approach

### Finding 3: Topic Cluster Classification
- The 7 pages likely belong to **HR Solutions** or **Staffing Solutions** topic cluster
- They represent entry points for USA businesses seeking Mexico-based talent
- Different from geographic hubs (Cancun, Monterrey, etc.)

---

## Recommendation: Parent Page Strategy

### Option A (Recommended):
Create a **"HR Solutions"** or **"Staffing Solutions"** parent page:
```
Parent: HR Solutions / Staffing Solutions (new parent page)
  ├── Nearshore Staffing Mexico
  ├── Remote Workers Mexico
  ├── Hire Developers Mexico
  ├── Remote Teams Mexico  
  ├── Employer of Record Mexico
  ├── Mexico Outsourcing
  └── [7th page]
```

**Benefits**:
- Proper page hierarchy
- Improved SEO through internal linking topology
- Clear organizational structure
- Aligns with cleaned map's approach (service-based organization)

### Option B (Keep Flat):
If keeping at HOME level:
- Still requires verification that HOME is the correct parent
- Must ensure these are treated as strategic landing pages, not sub-pages
- Alternative: Create a "Mexico Solutions" nav/menu structure without changing page hierarchy

---

## Cleaned Map Sheet Details

**File**: MEZTAL_SEO_MASTER_Minimal_2025-09-22_R3
**URL**: https://docs.google.com/spreadsheets/d/1Jx4Oo3lN_DlSynVBVUycGU3dwWC3NmOqgXkCceheOI4/edit?gid=921062424
**Tab**: Architecture — Cleaned Map (gid=921062424)

**Key Columns**:
- A: Primary Keyword
- B: Secondary Keywords
- C: Topic Cluster
- D: Proposed URL
- E: Page Type (Spoke, Pillar, Leaf)
- F: Content Type
- G: Funnel Stage (TOFU, MOFU, BOFU)
- H: Persona
- I: Triangulated Priority Score

---

## Critical Browser Interaction Rules

**DO NOT use in Wix Studio**:
- ❌ Right-click menus (will not work in browser)
- ❌ Double-click for editing (will not open editors)
- ❌ Keyboard shortcuts for page manipulation

**INSTEAD use**:
- ✅ Left-click on context menu buttons (three dots)
- ✅ Navigate through Settings panels
- ✅ Use "Edit" button from context menus
- ✅ Use "Rename" function from menu options

---

## Next Steps

### Immediate Actions:
1. **Verify**: Confirm whether 7th Mexico page exists and identify it
2. **Decide**: Parent page strategy (Option A or Option B)
3. **Implement**: Assign parent pages to all 7 Mexico pages
4. **Validate**: Ensure no "all pages under HOME" anti-pattern

### Implementation Process:
1. Open Wix Studio sandbox
2. Access each Mexico page settings (left-click menu → Settings)
3. Check "Parent page (hierarchy)" field
4. Update to appropriate parent page
5. Verify URL structure remains correct
6. Document completion in next session log

---

## References

### Google Sheet Analysis:
- Cleaned Map Tab: 921062424
- Total keywords: 300+
- Mexico-specific entries: 1 (cost-of-living comparison)
- Geographic hubs: 15+ cities
- Search term "Mexico": 2 of 8 instances
- Search term "nearshore": 349 instances (various contexts)
- Search term "nearshore staffing": 0 instances
- Search term "remote workers": 0 instances

### Sandbox URLs:
- Sandbox Wix Studio: https://editor.wix.com/studio/792fe01d-fa28-4833-b811-b5a540f5568b
- Meta Site ID: 24c6a184-1fd5-4b8c-ade1-8f2dae9c8f9e

### Live Site (Reference Only - NEVER EDIT):
- Live URL: https://www.meztal.com
- Purpose: Information gathering only
- Status: Will be replaced by sandbox version

---

## Session Log

**Date**: November 15, 2025 - 6-7 AM EST  
**Analyst**: Comet (AI Agent)  
**Status**: Analysis complete, awaiting strategic decision on parent page approach  
**Duration**: ~1 hour analysis + documentation

---

## Quick Reference Checklist

- [x] Accessed cleaned map authoritative source
- [x] Searched for "Mexico" in cleaned map (8 instances found)
- [x] Searched for "nearshore" in cleaned map (349 instances, various contexts)
- [x] Verified 7 Mexico pages do NOT exist in cleaned map
- [x] Identified geographic hubs as lower priority
- [x] Clarified business context (USA clients, Mexico delivery)
- [x] Documented current state of sandbox pages
- [ ] Determine parent page strategy (pending user decision)
- [ ] Implement page hierarchy reorganization
- [ ] Validate completed implementation

# MezTal — Immediate Implementation Actions (2025-11-15)

**Session:** Perplexity (Comet) — Expert Implementation  
**Scope:** Tasks executable within 12 hours  
**Date:** November 15, 2025, 4:00 AM EST  
**Status:** Active Implementation Plan

---

## CRITICAL ISSUE: Dynamic Button Text Implementation

### Problem Statement
Current implementation uses static "Start Now" button text across all collection repeaters (Services, Solutions, Industries, Resources, Locations). This creates poor UX as the button text doesn't match the destination page type.

### Solution: Collection-Aware Dynamic Button Text

**Implementation Options (Choose One):**

#### Option A: Add Custom Button Text Field to CMS (RECOMMENDED)
**Complexity:** Low  
**Flexibility:** High  
**Maintenance:** Low

**Steps:**
1. Add new field to each CMS collection: `button_text` (text field)
2. Populate field with collection-appropriate text:
   - Services: "View Service Details"
   - Solutions: "Explore Solution"
   - Industries: "Learn More"
   - Resources: "Read Resource"
   - Locations: "View Location"
   - Case Studies: "Read Case Study"
3. In repeater binding, connect button text to `button_text` field instead of static text
4. Test all repeaters to confirm dynamic text displays correctly

**Estimated Time:** 45 minutes

#### Option B: Use Universal Action-Oriented Text
**Complexity:** Very Low  
**Flexibility:** Low  
**Maintenance:** None

**Universal Button Text Options:**
- "Learn More" (most generic, works for all)
- "View Details" (slightly more specific)
- "Explore" (modern, action-oriented)

**Steps:**
1. Change all repeater button text from "Start Now" to chosen universal text
2. Test all repeaters

**Estimated Time:** 10 minutes

#### Option C: Conditional Logic Based on Collection Type (ADVANCED)
**Complexity:** High  
**Flexibility:** Very High  
**Maintenance:** Medium

**Note:** Requires Wix Velo code. May be overkill for current needs.

**Steps:**
1. Add Velo code to repeater `onItemReady` event
2. Detect collection type
3. Set button text dynamically:
```javascript
$w.onReady(function () {
  $w("#repeater1").onItemReady(($item, itemData, index) => {
    // Detect collection and set button text
    const collectionName = itemData._type; // or detect via other means
    let buttonText = "Learn More"; // default
    
    if (collectionName === "Services") {
      buttonText = "View Service";
    } else if (collectionName === "Solutions") {
      buttonText = "Explore Solution";
    } else if (collectionName === "Resources") {
      buttonText = "Read Resource";
    } else if (collectionName === "Locations") {
      buttonText = "View Location";
    } else if (collectionName === "Industries") {
      buttonText = "Learn More";
    } else if (collectionName === "CaseStudies") {
      buttonText = "Read Case Study";
    }
    
    $item("#button").label = buttonText;
  });
});
```
4. Apply code to each page with repeaters
5. Test thoroughly

**Estimated Time:** 2-3 hours

---

## RECOMMENDED IMPLEMENTATION PATH

### Immediate Action (Next 2 Hours)

**STEP 1: Quick Fix (10 minutes)**
1. Login to Wix Studio
2. Navigate to each List page (Services, Solutions, Industries, Resources, Locations, Case Studies)
3. Change all "Start Now" button text to "Learn More"
4. Publish changes
5. **This resolves the immediate UX issue**

**STEP 2: Proper Solution (45 minutes)**
1. Add `button_text` field to each CMS collection
2. Populate with appropriate text per collection
3. Update repeater bindings to use `button_text` field
4. Test all pages
5. Publish
6. **This creates sustainable, maintainable solution**

**STEP 3: Documentation (15 minutes)**
1. Update `open_tasks.md` to mark button text task as DONE
2. Document button text field in CMS collection documentation
3. Update session log

**Total Time:** 70 minutes (1 hour 10 minutes)

---

## ADDITIONAL IMMEDIATE TASKS (12-Hour Scope)

### Task 1: Complete CMS Collection Binding Verification
**Priority:** P0 (Critical)  
**Estimated Time:** 1-2 hours

**Steps:**
1. Login to Wix Studio
2. For each List page, verify repeater bindings:
   - Solutions (List)
   - Services (List)
   - Industries (List)
   - Case Studies (List)
   - Resources (List)
   - Locations (List)
3. Check that all fields are bound:
   - `thumbnail_image` → Image element
   - `title` or `name` → Heading element
   - `short_description` → Paragraph element
   - `button_text` → Button label
   - Button link → Dynamic page (Item page for that collection)
4. Test repeater display with existing CMS items
5. Document binding status in `open_tasks.md`

**Completion Criteria:**
- All repeaters display data correctly
- All buttons link to correct Item pages
- No "undefined" or blank fields

### Task 2: Verify Item Page Templates Exist
**Priority:** P0 (Critical)  
**Estimated Time:** 30 minutes

**Steps:**
1. In Wix Studio, navigate to Pages panel
2. Verify dynamic Item pages exist for:
   - Services (Item)
   - Solutions (Item)
   - Industries (Item)
   - Case Studies (Item)
   - Resources (Item)
   - Locations (Item)
3. For each Item page, verify it's connected to correct collection
4. Test navigation from List page button to Item page
5. Document status

**Completion Criteria:**
- All Item pages exist
- All Item pages are connected to datasets
- Navigation from List to Item works

### Task 3: Set Editor Zoom to ~70%
**Priority:** P3 (Low)  
**Estimated Time:** 2 minutes

**Steps:**
1. In Wix Studio editor, use zoom controls
2. Set zoom to approximately 70%
3. Verify more content visible on screen

**Completion Criteria:**
- Editor zoom set for better workflow

### Task 4: Update open_tasks.md
**Priority:** P1 (High)  
**Estimated Time:** 15 minutes

**Steps:**
1. Mark completed tasks as DONE
2. Add button text fix as priority task
3. Update binding verification status
4. Remove outdated tasks
5. Commit changes to GitHub

**Completion Criteria:**
- open_tasks.md reflects current actual state
- No stale or completed items listed as pending

---

## EXECUTION CHECKLIST

### Hour 1-2: Button Fix + Binding Verification
- [ ] Quick fix: Change all "Start Now" to "Learn More"
- [ ] Publish quick fix
- [ ] Add `button_text` field to all CMS collections
- [ ] Populate `button_text` field for all existing items
- [ ] Update repeater bindings to use `button_text` field
- [ ] Test all repeaters
- [ ] Publish proper solution
- [ ] Verify all CMS collection bindings complete
- [ ] Document binding status

### Hour 2-3: Item Page Verification + Documentation
- [ ] Verify all Item pages exist
- [ ] Test List → Item navigation
- [ ] Document Item page status
- [ ] Set editor zoom to ~70%
- [ ] Update open_tasks.md with completion status
- [ ] Commit documentation updates to GitHub

### Hour 3-4: Homepage Section Build (IF TIME PERMITS)
**Note:** Only proceed if above tasks complete ahead of schedule

- [ ] Begin Homepage Hero section build
- [ ] Add Services Overview repeater section
- [ ] Connect Services repeater to Services collection
- [ ] Test Services section display
- [ ] Document progress in session log

---

## SUCCESS CRITERIA FOR THIS SESSION

**Minimum Success (Must Complete):**
1. ✓ Button text issue resolved (either quick fix OR proper solution)
2. ✓ CMS binding verification complete and documented
3. ✓ open_tasks.md updated to reflect current state

**Full Success (Target):**
1. ✓ All minimum success items
2. ✓ Proper button text solution implemented (button_text field)
3. ✓ Item pages verified and tested
4. ✓ Documentation updated in GitHub

**Stretch Success (If Time Allows):**
1. ✓ All full success items
2. ✓ First Homepage section (Hero) built
3. ✓ Services Overview section with repeater added

---

## TECHNICAL NOTES

### Wix Studio Site URL
```
https://editor.wix.com/studio/792fe01d-fa28-4833-b811-b5a540f5568b
```

### CMS Collections (Current State)
- Services: 3 items
- Solutions: 3 items
- Resources: 2 items
- Locations: 3 items
- Industries: (count TBD)
- Case Studies: (count TBD)

### Fields to Verify in Repeater Bindings
- `thumbnail_image` (image)
- `title` or `name` (text)
- `short_description` (text)
- `button_text` (text) — NEW FIELD TO ADD

### Button Text Recommendations by Collection
| Collection | Recommended Button Text |
|------------|------------------------|
| Services | "View Service" or "Explore Service" |
| Solutions | "Explore Solution" or "Learn More" |
| Industries | "View Industry Details" or "Learn More" |
| Case Studies | "Read Case Study" or "View Story" |
| Resources | "Read Resource" or "Access Resource" |
| Locations | "View Location" or "Contact Office" |

---

## DEPENDENCIES & BLOCKERS

**No Blockers Identified** — All tasks are executable immediately with Wix Studio access.

**Dependencies:**
- Wix Studio login access
- CMS collections already exist (confirmed)
- Dynamic pages already created (per session log)

---

## NEXT SESSION CONTINUATION POINTS

**After This Session:**
1. Homepage section build (9 sections total, prioritize sections 1-3)
2. Item page template customization
3. Content population in CMS
4. SEO meta patterns implementation

**Do NOT Continue Into:**
- Long-term planning
- Week-by-week roadmaps
- Content strategy (beyond immediate CMS needs)
- Analytics baseline (requires separate session)

---

**Document Status:** Active Implementation Plan  
**Session Start:** 4:00 AM EST  
**Estimated Completion:** 6-8:00 AM EST (2-4 hours)  
**Owner:** Perplexity (Comet) — Expert AI Implementation

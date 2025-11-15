# Open Tasks

This file tracks outstanding work for the MezTal Wix Studio project. Tasks are prioritized by impact and executability.

---

## PRIORITY 1: FIX BUTTON TEXT (CRITICAL UX ISSUE)

**Status:** Ready to execute  
**Estimated Time:** 10 minutes (quick fix) OR 45 minutes (proper solution)  
**Blocker:** Requires Wix Studio login

### Problem
All repeater buttons currently use static "Start Now" text, which doesn't match the destination page type. Poor UX.

### Solution Options

#### QUICK FIX (Recommended First Step - 10 min)
1. Login to Wix Studio: https://editor.wix.com/studio/792fe01d-fa28-4833-b811-b5a540f5568b
2. Navigate to each List page:
   - Solutions (List)
   - Services (List)
   - Industries (List)
   - Case Studies (List)
   - Resources (List)
   - Locations (List)
3. For each page, select the repeater button
4. Change text from "Start Now" to "Learn More"
5. Publish site
6. Mark this task as DONE

#### PROPER SOLUTION (Sustainable - 45 min)
1. In Wix Studio, go to CMS
2. For each collection (Services, Solutions, Industries, Resources, Locations, Case Studies):
   - Add new field: `button_text` (Text field)
   - Populate field for each item:
     * Services items: "View Service"
     * Solutions items: "Explore Solution"
     * Industries items: "Learn More"
     * Resources items: "Read Resource"
     * Locations items: "View Location"
     * Case Studies items: "Read Case Study"
3. For each List page, update repeater button binding:
   - Connect button text to `button_text` field (not static text)
4. Test all pages
5. Publish site
6. Mark this task as DONE

**Reference:** See `meztal_immediate_actions_2025-11-15.md` for full details

---

## Dynamic Page Customization

### Solutions (List) — continue binding the repeater:
* Use the Add panel to insert an image, heading, paragraph and button into the repeater item.
* Bind the image to `thumbnail_image` (set alt text to `title` or `name`), the heading to `title`/`name`, the paragraph to `short_description` and the button to `button_text` field (if added) or use generic "Learn More"
* Button link should point to the item's dynamic page
* Use the Layers panel and breadcrumb navigation to avoid detaching the dataset when editing items.
* Confirm that the bindings replicate across all repeater items without duplicating the dataset.

### Replicate binding pattern across list templates 

After completing the Solutions (List) page, apply the same pattern to:

* **Services (List)** — bind `thumbnail_image`, `name`, `short_description` and button with dynamic link
* **Industries (List)** — bind `thumbnail_image`, industry name, `short_description` and button
* **Case Studies (List)** — bind `cover_image`, `client_name - project_name`, short summary, and button
* **Resources (List)** — bind `cover_image`, `title`, `excerpt`, and button
* **Locations (List)** — bind `city_name`, short blurb, and button

### Template SEO patterns 

Verify that each list template and item template uses the correct SEO patterns:

* Title pattern: `{{name}} | MezTal` (fallback to `{{title}}` if `name` is absent).
* Description pattern: `{{meta_description}}` (fallback to `{{short_description}}`).
* URL slugs: use dataset slugs; do not hard-code slugs.

### Zoom adjustment

Once bindings are complete, adjust the editor zoom to ~70 % to view more content on screen.

---

## Content Import & Home/Navigation

### Data imports

Confirm that all collections (services, solutions, industries, locations, case studies, resources) are fully populated with accurate content. If any collection is incomplete, prepare CSV files for import and request user confirmation before uploading.

### Home page & navigation design

Design the home page and main navigation:

* Hero section with value proposition
* Services overview section (repeater bound to Services collection)
* Solutions overview section (repeater bound to Solutions collection)
* Featured case study or testimonial
* Locations preview (repeater bound to Locations collection)
* Resources/insights preview (repeater bound to Resources collection)
* CTA section
* Footer with navigation links

**Note:** Homepage structure defined in `meztal_session_log_2025-11-15_hierarchy_build_perplexity.md` - 9 sections total

---

## NEXT ACTIONS PRIORITY LIST

1. **[P0 - CRITICAL]** Fix button text (see PRIORITY 1 above)
2. **[P0 - CRITICAL]** Verify CMS collection bindings are complete
3. **[P1 - HIGH]** Complete Homepage section build (sections 1-3 minimum)
4. **[P2 - MEDIUM]** Customize Item page templates
5. **[P2 - MEDIUM]** Verify SEO meta patterns
6. **[P3 - LOW]** Adjust editor zoom to 70%

---

**Last Updated:** 2025-11-15, 4:00 AM EST  
**Updated By:** Perplexity (Comet)

# Open Tasks

This file tracks outstanding work for the MezTal Wix Studio project.  Tasks are grouped by category and prioritised based on impact.  Completed items should be marked as **DONE** in the next session summary once finished.

## Dynamic page customisation

* **Solutions (List)** – continue binding the repeater:
  * Use the Add panel to insert an image, heading, paragraph and button into the repeater item.  
  * Bind the image to `thumbnail_image` (set alt text to `title` or `name`), the heading to `title`/`name`, the paragraph to `short_description` and the button text to “Start Now” with a link to the item’s dynamic page.  
  * Use the Layers panel and breadcrumb navigation to avoid detaching the dataset when editing items.  
  * Confirm that the bindings replicate across all repeater items without duplicating the dataset.

* **Replicate binding pattern across list templates** – after completing the Solutions (List) page, apply the same pattern to:
  * **Services (List)** – bind `thumbnail_image`, `name`, `short_description` and dynamic button link.
  * **Industries (List)** – bind `thumbnail_image`, industry name, `short_description` and dynamic button.
  * **Case Studies (List)** – bind `cover_image`, `client_name – project_name`, a short summary, and dynamic button.
  * **Resources (List)** – bind `cover_image`, `title`, `excerpt`, and dynamic button.
  * **Locations (List)** – bind `city_name`, a short blurb, and dynamic button.

* **Template SEO patterns** – verify that each list template and item template uses the correct SEO patterns:
  * Title pattern: `{{name}} | MezTal` (fallback to `{{title}}` if `name` is absent).
  * Description pattern: `{{meta_description}}` (fallback to `{{short_description}}`).
  * URL slugs: use dataset slugs; do not hard‑code slugs.

* **Zoom adjustment** – once bindings are complete, adjust the editor zoom to ~70 % to view more content on screen.

## Content import & home/navigation

* **Data import** – confirm that all collections (services, solutions, industries, locations, case studies, resources) are fully populated with accurate content.  If any collection is incomplete, prepare CSV files for import and request user confirmation before uploading.

* **Home page & navigation design** – design the home page and main navigation:
  * Structure the home page with clear sections that introduce MezTal’s services, solutions, industries, locations, case studies and resources.  
  * Create call‑to‑action buttons linking to each dynamic hub.
  * Ensure the navigation menu links to the dynamic list pages and any static pages (About, Contact) defined in the site hierarchy.

## Logging & documentation

* **Logging improvements** – continue refining the session log format: organise actions by category (e.g. navigation, binding, issues encountered), include metadata (status, duration, tool used) and summarise learnings at the end of each session.

* **Repeater‑binding guide** – develop a step‑by‑step guide (with screenshots) for binding repeaters in Wix Studio.  Include tips on using the Layers panel, breadcrumb navigation, the Add panel, dataset connections and undo functionality.

* **Communication guidelines update** – append new UI nuances to `user_communication_guidelines_update.md`, such as:
  * Using the Layers panel to select nested elements and avoid mis‑clicks.
  * Navigating via the breadcrumb trail (Page → Section → Repeater → Item) to switch between the repeater and its items.
  * Recognising that double‑clicking an item resets the dataset connection; use the undo arrow or `Cmd+Z` to recover.
  * Locating and using the Add panel to insert elements into repeaters.

## Process refinement & automation

* **Automation for context retrieval** – draft a script or checklist to automatically fetch the latest project context (open tasks, session summaries, logs) at the start of a new session.  This will reduce manual overhead and ensure continuity across sessions.

* **Task management** – integrate the open tasks file into a lightweight task management system (e.g. a Kanban board or issue tracker) to track progress and assignments.  Determine whether GitHub Issues or a separate tool is more appropriate.

## Research tasks

* **Advanced Wix Studio resources** – Research and summarise external resources about advanced Wix Studio techniques.  A new file, `advanced_wix_studio_resources.md`, has been created to compile insights from accessible blogs and articles (e.g. custom animations, grid/flexbox layouts, branding, navigation, AI tools).  Future tasks should:
  * Review the summary file and incorporate relevant design practices into the site’s layout and component customisation.
  * Update communication guidelines or process documents to reflect new best practices (e.g. using gridlines, custom fonts, anchor links, AI tools).  
  * Continue exploring additional blogs, forums or tutorials (especially dynamic or Wix‑hosted pages) using the computer tool; if new insights are found, append them to the `advanced_wix_studio_resources.md` file.

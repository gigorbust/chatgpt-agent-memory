# Open Tasks for MezTal/Wix Studio Project (as of 2025‑11‑11)

This checklist tracks unresolved tasks and pending items for the MezTal website rebuild.  Update this file at the end of each work session to reflect completed steps and new actions.  Keeping this list current will prevent memory drift and ensure continuity across sessions.

## 1. Dynamic Page Customisation

- [ ] **Bind repeaters to datasets:** Connect the repeater on the Solutions (services) list page to the `services` dataset using the dataset anchor and “Connect Repeater” panel.  Repeat for other list pages (Industries, Case Studies, Resources, Locations, People).
- [ ] **Design list item cards:** Within the repeater, map fields like title, short description and thumbnail image to collection fields; add a CTA button linking to the corresponding item page.
- [ ] **Design item pages:** For each collection, customise the item page layout to showcase key content (e.g. service description, images, related items, case study results) and include a clear CTA to contact MezTal.
- [ ] **Home page and navigation:** Build the Home page with hero section, service and solution previews, case study highlights, resource teasers, location map and testimonials.  Configure the global navigation menu with links to Services, Solutions, Case Studies, Resources, Locations, About and Contact pages.
- [ ] **Contact and About:** Create well-designed static pages for Contact (form, contact details, social links) and About (story, team bios, mission, values, testimonials).

## 2. Content Import & Population

- [ ] **Review import CSVs:** Examine the `meztal_wix_import.csv` and architecture spreadsheets to ensure they align with the current collection fields.  Prepare to map columns to fields (e.g. service names, descriptions, industry tags).
- [ ] **User confirmation:** Wait for user approval before importing data.  Once confirmed, use Wix Studio’s CSV import feature to populate each collection.
- [ ] **Add case studies:** Populate the `case_studies` collection with at least two initial items and link them to relevant services and industries.

## 3. Logging & Documentation

- [ ] **Update log formats:** Incorporate `status`, `duration`, `tool_used` and `category` into each log entry, following the recommendations in `logging_improvements.md`.
- [ ] **Generate session summary:** At the end of each session, write a concise `session_summary.md` summarising tasks completed, obstacles faced, and next steps.  Store it under the date-specific folder.
- [ ] **Maintain this open_tasks.md:** Check off completed items and add new tasks as they arise.  Keep it synchronized with the session summaries.

## 4. Process Refinement

- [ ] **Develop a repeater-binding guide:** Draft a short how-to section describing precisely how to connect a repeater to a dataset in Wix Studio.  Include screenshots or numbered steps if possible.
- [ ] **Automate context retrieval:** Implement or script a function at session start that loads the latest `session_summary.md` and `open_tasks.md` from GitHub (read‑only) to reconstruct context before starting work.
- [ ] **Confirm tool capabilities:** Verify at session start whether any external connectors (e.g. GitHub) support write operations.  Default to local log creation if not.

## 5. Future Enhancements

- [ ] **SEO auditing:** After content import and page design, run an SEO audit on key pages to ensure meta descriptions, alt tags and headings follow best practices.
- [ ] **Performance optimisation:** Use Wix’s performance tools to test load times and adjust images, caching, or scripts as needed.
- [ ] **Analytics setup:** Plan for Google Analytics or Wix Analytics integration to track site visits, conversions and user behaviour once the site is live.
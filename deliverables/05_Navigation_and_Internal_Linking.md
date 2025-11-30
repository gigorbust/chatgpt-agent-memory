# Deliverable 05: Structured Internal Linking and Navigation

**Date:** November 30, 2025
**Status:** ✅ Completed (Strategy) / 🏗️ In Progress (Implementation)
**SOW Item:** 5. Structured Internal Linking and Navigation

---

## Executive Summary

This deliverable defines the navigation strategy and internal linking structure for the new MezTal.com. The strategy adopts a **"Minimalist + SEO"** approach, ensuring a clean user experience while maintaining crawlability for hundreds of targeted SEO landing pages.

---

## Navigation Strategy

### 1. The "Iceberg" Concept
*   **Visible (Above Water):** A streamlined top-level menu with only 5 core items to reduce cognitive load and guide users to conversion points.
*   **Hidden (Below Water):** Hundreds of specific SEO landing pages (e.g., "Nearshore Staffing Mexico", "Best IT Staffing Agencies") that are **hidden from the main menu** but accessible via:
    *   Footer Links
    *   Contextual Internal Links
    *   "Resources" or "Locations" Hubs
    *   Direct Search Traffic

### 2. Top-Level Menu Structure (Visible)

1.  **Solutions** (Mega Menu)
    *   *Tech & Development* (Software Dev, IT Staffing, App Dev)
    *   *Finance & Operations* (Accounting, Payroll, Admin)
    *   *Growth & Support* (Marketing, CX, HR)
2.  **Industries**
    *   Senior Living
    *   AgeTech
    *   (Other Verticals)
3.  **Why MezTal**
    *   Why Guadalajara?
    *   The Nearshore Advantage
    *   About Us / Team
4.  **Resources**
    *   Blog, Case Studies, Comparisons
5.  **Contact** (CTA Button)

---

## Internal Linking Architecture

### 1. Hub-and-Spoke Model
*   **Hub Pages:** "Solutions", "Industries", "Locations" act as parent pages.
*   **Spoke Pages:** Specific service or location pages link back to the Hub and to related Spokes.
    *   *Example:* "Software Development" (Hub) links to "Hire Python Developers" (Spoke) and "Hire React Developers" (Spoke).

### 2. Cross-Linking Strategy
*   **Service <-> Industry:** Service pages will link to relevant Industry pages (e.g., "IT Staffing" links to "AgeTech").
*   **Location <-> Service:** Location pages will highlight key services available in that region.
*   **Comparison <-> Service:** "Best X vs Y" pages will link to the relevant MezTal Service page as the solution.

### 3. Footer Navigation
The footer will serve as a secondary navigation map, exposing key "Hidden" SEO pages to search engines:
*   **Popular Searches:** Links to top-tier SEO pages (e.g., "Nearshore Staffing Mexico").
*   **Locations:** Links to city-specific pages.
*   **Services:** Links to all child service pages.

---

## Sitemap Visualization

The complete sitemap contains **417 pages**. Below is a high-level overview of the hierarchy:

```text
- / (Home)
- company
    - about
    - locations
    - team
- comparison (Competitor/Service comparisons - 40+ pages)
- industries
    - senior-living
    - agetech
    - ...
- nearshore-it-staffing (Deep hierarchy of roles - 40+ pages)
- resources (Educational content)
- services (Core service offerings - 100+ pages)
- solutions (Business problem focused)
- why-mexico
```

*Note: The full hierarchical tree is available in `MEZTAL_FULL_SITEMAP_TREE.md`.*

---

## Implementation Plan

1.  **Wix Menu Setup:** Configure the 5 top-level items.
2.  **Mega Menu Design:** Build the "Solutions" dropdown using Wix Studio's mega menu container.
3.  **"Hide from Menu":** Set the "Hide from menu" property for all SEO landing pages in Wix Page Settings.
4.  **Footer Construction:** Manually build the footer columns to include the strategic SEO links.

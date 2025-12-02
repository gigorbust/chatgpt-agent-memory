# Navigation Restructure Plan: Minimalist & SEO-Rich

## Goal
Create a clean, minimalist main navigation for MezTal.com that reduces cognitive load for users while keeping hundreds of "targeted" SEO pages accessible to search engines (but hidden from the top-level visual menu).

## User Review Required
> [!IMPORTANT]
> **"Hidden" Pages Strategy**: Pages marked "Hidden" will **NOT** appear in the top menu but **WILL** still be indexed by Google and accessible via internal links (footer, body content) and direct URLs. This is critical for your "targeted keywords" strategy.

## Proposed Menu Structure

### 1. Top-Level Menu (Visible)
We will reduce the top bar to just **5 core items**:

1.  **Solutions** (Dropdown/Mega Menu)
    *   *Grouped by Function (Clean)*:
        *   **Tech & Development**
            *   Software Development (Parent)
            *   IT Staffing
            *   App Development
            *   Web Development
        *   **Finance & Operations**
            *   Accounting & Finance (Parent)
            *   Finance Outsourcing
            *   Payroll Services
            *   Admin Outsourcing
        *   **Growth & Support**
            *   Digital Marketing
            *   Call Center / CX
            *   Sales Solutions
            *   HR & Talent Acquisition

2.  **Industries** (Dropdown)
    *   **Senior Living** (Key Vertical)
    *   **AgeTech** (Key Vertical)
    *   *Other Industries* (Future expansion)

3.  **Why MezTal** (Dropdown)
    *   **Why Guadalajara?** (Elevated from "Locations")
    *   **The Nearshore Advantage** (Content page)
    *   **About Us**
    *   **Team**

4.  **Resources** (Simple Link)
    *   (Links to Blog, Case Studies, Comparisons)

5.  **Contact** (Button / CTA)

---

### 2. "Hidden" SEO Pages (The "Iceberg" Strategy)
These pages exist for SEO but are **removed from the Main Menu**. They will be linked from the **Footer** or **Parent Pages**.

#### Geographic SEO Landing Pages (Hide from Menu)
*   `Nearshore Staffing Mexico`
*   `Remote Workers Mexico`
*   `Mexico Outsourcing`
*   `Hire Developers Mexico`
*   `Remote Teams Mexico`
*   `Employer of Record Mexico`

**Where to link them?**
*   **Footer**: Create a "Popular Searches" or "Locations" column in the footer.
*   **Body Content**: Link to "Hire Developers Mexico" from the "Software Development" page text.

#### Comparison Pages (Hide from Menu)
*   `Top IT Outsourcing Companies`
*   `Best Accounting Firms`
*   (All "Best X vs Y" pages)

**Where to link them?**
*   **Resources Page**: List them as "Buyer's Guides".

---

## Implementation Steps in Wix
1.  **Open "Pages & Menu"** panel.
2.  **Group Items**: Create "Submenus" (Folders) for *Tech*, *Finance*, *Growth* under "Solutions".
3.  **Hide Pages**:
    *   Right-click SEO pages (e.g., "Remote Workers Mexico").
    *   Select **"Hide from menu"**.
    *   *Verify*: Ensure "Show in search results" is still ON in SEO Settings (it usually is by default).
4.  **Update Footer**: Add text links to the hidden SEO pages to ensure crawlability.

## Visual Reference
```mermaid
graph TD
    Nav[Main Navigation]
    Nav --> Sol[Solutions]
    Nav --> Ind[Industries]
    Nav --> Why[Why MezTal]
    Nav --> Res[Resources]
    Nav --> CTA[Contact]

    Sol --> Tech[Tech & Dev]
    Sol --> Fin[Finance & Ops]
    Sol --> Growth[Growth & Support]

    Tech --> SD[Software Dev]
    Tech --> IT[IT Staffing]
    
    subgraph Hidden SEO Layer
    SEO1[Nearshore Staffing Mexico]
    SEO2[Remote Workers Mexico]
    SEO3[Comparison Pages]
    end
    
    Footer --> SEO1
    Footer --> SEO2
    Footer --> SEO3
    SD -.->|Internal Link| SEO1
```

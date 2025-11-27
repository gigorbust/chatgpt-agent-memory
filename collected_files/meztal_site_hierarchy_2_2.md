# MezTal Site Architecture & Page Hierarchy (latest)

This document records the full site structure for the MezTal.com rebuild in Wix Studio.  It consolidates the latest architecture from our planning sessions and should be referenced in future sessions to guide page creation and navigation.  Use this hierarchy to ensure new pages align with the overall structure and avoid duplication or drift.

## Home (Static Page)
- **Hero Section** – H1 “Build Your Nearshore Team in Mexico” and a concise positioning statement.  Primary CTA links to the Services section (`/services`).
- **Services Overview** – Dynamic preview of the **Services** collection showing each service category.
- **Solutions Overview** – Dynamic preview of the **Solutions/Industries** collection.
- **Featured Case Study** – Highlights a single case study (pinned) from the **Case Studies** collection.
- **Locations Preview** – Dynamic preview of the **Locations** collection (nearshore hubs).
- **Insights Preview** – Dynamic preview of the **Resources** collection (blogs, guides, etc.).
- **Testimonials Section** – Static or semi‑dynamic client testimonials.
- **CTA Banner** – “Let’s Build Your Nearshore Team” linking to `/contact`.
- **Footer** – Global footer with copyright notice, privacy policy, terms, cookie policy and social links.

## Services (Dynamic List)
A dynamic list page summarising each service category (pillar) with dynamic item pages for each specific service.  The primary categories (pillars) and example spokes/leaf pages are:

1. **IT Staffing & Development**
   - Developers for Hire
   - Hire a Back‑End Developer
   - Hire a Front‑End Developer
   - Hire a Full‑Stack Developer
   - Hire a Mobile App Developer
   - Hire a Python Developer
   - Hire an SAP Consultant
   - … (other technology‑specific roles)
2. **Application Development Outsourcing**
   - Custom Software Development
   - Application Modernization
   - ERP Implementation
3. **Digital Marketing**
   - SEO Services
   - Paid Media Management
   - Social Media Management
   - … (other marketing services)
4. **Accounting & Finance**
   - Accounts Payable Outsourcing
   - Payroll Outsourcing
   - Tax Services
   - Hire a Bookkeeper
   - … (other finance services)
5. **HR & Talent Acquisition**
   - Recruiting Services
   - Staff Augmentation
   - Talent Acquisition Specialist
   - HR Outsourcing
6. **Sales & Customer Service**
   - Sales Outsourcing
   - Customer Service Outsourcing
   - Call Center Outsourcing
7. **Foundational Solutions**
   - Managed IT Services
   - Marketing Outsourcing
   - Procurement Outsourcing
   - Supply Chain Outsourcing
   - … (other core functions)

Each service item page includes:
- Hero section with service name and hero image.
- Summary of the service with long description.
- Key outcomes or benefits.
- Related services and related solutions (via multi‑reference fields).
- Related case studies.
- Lead‑generation CTA linking to `/contact`.

## Solutions / Industries (Dynamic List)
Dynamic list page that showcases solutions/industry clusters.  Example clusters:

- **AgeTech & Senior Care** – Items include Senior Living Tech Solutions, Home Care Apps, etc.
- **Healthcare & Life Sciences** – Items like Telehealth Solutions, Medical Device Software.
- **SaaS & Technology Startups** – Items like Product Development, Growth Marketing.
- **Media & Entertainment** – Specific media solutions.
- **Other Verticals** – Additional industry pages as the business grows.

Each solution item page covers:
- Hero with solution/industry name.
- Problem → outcome overview.
- Long description of how MezTal supports that industry.
- Relevant services (referenced from **Services** collection).
- Relevant case studies.
- CTA (“Get matched with a team”) linking to `/contact`.

## Locations (Dynamic List)
Dynamic list page showing nearshore hubs in Mexico:

- Guadalajara
- Monterrey
- Mexicali
- Culiacán
- León
- Saltillo
- Mérida
- … (additional hubs)

Each location item page includes:
- Hero section with city name.
- “Why [City]?” section explaining the benefits of nearshoring there.
- Time zone & collaboration information.
- Map embed or local imagery.
- Local CTA (“Start in [City]”) linking to `/contact`.

## Comparisons (Static or Dynamic Cluster)
Optional cluster for comparative pages (not yet built):
- Nearshore vs Offshore
- Offshore vs Outsourcing
- Top BPO Companies
- Top Outsourcing Companies
- Cost of Living in Guadalajara vs Mexico City
- Offshore Services vs Offshore Staffing
- … (other comparisons)

These pages can be used for SEO and educational content.

## Insights & Resources (Dynamic List)
Dynamic list page for blog posts, guides and other resources.  Filter by type (e.g. articles, guides, case studies).  Each resource item page shows:
- Hero with article title.
- Metadata (published date, author).
- Body (rich text with headings and images).
- Related services and solutions.
- CTA (“Contact MezTal”).

## Case Studies (Dynamic List)
Dynamic list page summarising each case study.  Each item page includes:
- Hero section with client name and project name.
- Challenge, solution and results sections.
- Cover image.
- Related services and solutions.
- CTA (“Let’s Talk About Your Project”).

## About (Static Page)
Comprised of several sections:
- Our Story – MezTal’s founding mission and history.
- Leadership Team – Profiles from the **People** collection (dynamic list or static section).
- Careers – Information about joining MezTal and a link to external applicant portal.
- Client Testimonials – Additional testimonials (if not shown on Home).
- FAQs – Answers to common questions about nearshoring and MezTal’s process.

## Contact (Static Page)
- Hero section (“Let’s Build Your Nearshore Team”).
- Contact form (Name, Email, Company, Message) with inbox automation.
- Alternative contact methods (schedule a call via Calendly, direct email, phone number).
- Office locations and map (e.g. Guadalajara HQ).
- Social media links.

## Utility & Legal Pages
Static pages accessible via the footer:
- Privacy Policy
- Terms of Service
- Cookie Policy
- Sitemap

## Notes & Recommendations
- **Dynamic Page Design:** Each collection’s list page should include a repeater bound to its dataset and visually appealing cards summarising key fields.  Item pages should use a consistent layout with CTAs.
- **Navigation:** The global header should link to top‑level pages: Home, Services, Solutions, Case Studies, Resources, About and Contact.  Consider a secondary menu or mega‑menu for subservices and industries.
- **Expandability:** This hierarchy is designed to scale; new services or industries can be added by creating new items in the respective collection, automatically generating new pages.


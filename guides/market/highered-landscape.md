# Higher Education Landscape

**Answers:** What rules and systems shape whether a US college or university can adopt your product? Use this guide when you scope a higher-ed product. It covers accreditation, accessibility law, LMS integration, and the policy trends behind buyer priorities.

**Audience:** Higher education, United States. International systems differ significantly. How institutions buy is covered in the [procurement guide](../selling/procurement-guide.md), and who buys in [buyer personas](../demand/buyer-personas.md). For the vendors you will meet, see the [competitive landscape](competitive-landscape.md).

## Accreditation

**What it is:** The quality-assurance process for higher education institutions. Accrediting agencies evaluate whether institutions meet standards for academic quality. Institutions need accreditation from an agency recognized by the US Department of Education to take part in federal student aid.

**Why it matters for edtech founders (practitioner view):**
- If your product delivers or assesses academic content, the institution may need to show accreditors how it supports learning outcomes.
- If your product replaces or augments a core academic function, such as assessment, advising, or course delivery, find out how accreditors evaluate that function.

**Institutional accreditors:** Since July 1, 2020, Department of Education [regulations](https://www.federalregister.gov/documents/2019/11/01/2019-23129/student-assistance-general-provisions-the-secretarys-recognition-of-accrediting-agencies-the) no longer distinguish between "regional" and "national" accreditors. The six formerly regional agencies still accredit most nonprofit colleges:
- HLC (Higher Learning Commission)
- SACSCOC (Southern Association of Colleges and Schools Commission on Colleges)
- MSCHE (Middle States Commission on Higher Education)
- NECHE (New England Commission of Higher Education)
- NWCCU (Northwest Commission on Colleges and Universities)
- WSCUC (WASC Senior College and University Commission)

**Changing landscape:** Public university systems in Florida, Georgia, North Carolina, South Carolina, Tennessee, and Texas formed a new accreditor, the Commission for Public Higher Education (CPHE). It was not federally recognized as of October 2026; the Department was running negotiated rulemaking on accreditor recognition in 2026. Recognition timelines in press coverage vary, so check the [Department's list of recognized accreditors](https://ope.ed.gov/dapip/) before relying on any agency's status.

**Practical guidance:** You don't need accreditation approval to sell your product. But your product should help institutions show they meet accreditation standards, not create problems for them.

## Accessibility in Higher Ed

**Legal requirements:**
- Section 504 of the Rehabilitation Act applies to all institutions receiving federal funds.
- ADA Title II applies to public institutions and Title III to private institutions.
- The Department of Justice's [2024 ADA Title II web rule](https://www.ada.gov/resources/2024-03-08-web-rule/) requires public colleges and universities to make web content and mobile apps conform to **WCAG 2.1 Level AA**, including content provided through contractors and vendors. An [April 20, 2026 interim final rule](https://www.federalregister.gov/documents/2026/04/20/2026-07663/extension-of-compliance-dates-for-nondiscrimination-on-the-basis-of-disability-accessibility-of-web) moved the compliance dates to **April 26, 2027** for public entities with a total population of 50,000 or more, and **April 26, 2028** for smaller entities and special district governments ([28 CFR 35.200](https://www.ecfr.gov/current/title-28/chapter-I/part-35/subpart-H/section-35.200)). Which date applies to a given institution depends on how the rule classifies it; the institution's counsel decides that.
- The Office for Civil Rights (OCR) investigates accessibility complaints against universities.

**Standards:**
- WCAG 2.1 AA is the legal standard for public institutions under the Title II rule and the usual benchmark for private ones.
- Some institutions also ask about WCAG 2.2 (practitioner observation, not measured).
- VPATs (Voluntary Product Accessibility Templates) are commonly required during procurement.

**Common procurement requirements:**
- Completed VPAT
- Accessibility statement on your website
- Documented process for addressing accessibility issues
- Some institutions require third-party accessibility audits

**Practical guidance (practitioner view):** An incomplete or missing VPAT can disqualify you from consideration. Invest in accessibility early.

## LMS Integration

**The major LMSs:**
- **Canvas (Instructure)**
- **Blackboard** (the company formerly called Anthology, which [emerged from Chapter 11 as Blackboard](https://blackboard.com/news/blackboard-formerly-anthology-emerges-debt-free-and-focused) on March 2, 2026)
- **D2L Brightspace**
- **Moodle**: open source

For ownership, market notes, and other vendors, see the [competitive landscape](competitive-landscape.md).

**Integration standards:**
- **LTI (Learning Tools Interoperability)** is the primary standard for integrating external tools into an LMS.
  - LTI 1.1: basic launch and grade passback
  - LTI 1.3 / Advantage: the current standard, with improved security (OAuth 2.0), deep linking, names and roles, and assignment and grade services
  - **Build for LTI 1.3.** LTI 1.1 is legacy.
- **SIS integration:** Student Information System integration via OneRoster, SIF, or custom APIs
- **xAPI / Caliper:** Learning analytics standards for tracking learner activity across systems

**Practical guidance (practitioner view):**
- If you sell to US higher ed, make LTI 1.3 integration with Canvas your first priority.
- Canvas REST API is well documented and widely used for deeper integrations.
- A listing in the LMS's app marketplace reduces friction.
- Single sign-on (SSO) via SAML or the institution's identity provider is often required.

## Selling to Higher Ed

The [procurement guide](../selling/procurement-guide.md) covers purchase thresholds, the budget calendar, and how higher ed differs from K-12. [Buyer personas](../demand/buyer-personas.md) profiles the CIO, Provost, Department Chair, and individual faculty.

Two points specific to higher ed (practitioner view):
- Individual faculty often have the autonomy to try new tools, especially free or freemium ones. That is the fastest adoption path but the hardest to scale.
- Security reviews can take months at large institutions. Ask about the review process, such as a HECVAT, early.

## Key Trends

- **Enrollment pressure:** WICHE's [*Knocking at the College Door*](https://www.wiche.edu/knocking/) (December 2024) projects that US high school graduates peak in 2025 at about 3.9 million, then fall to about 3.4 million by 2041, 13% below the 2025 peak. Institutions facing smaller pools put more weight on retention and completion.
- **Short-term credentials:** The Working Families Tax Cuts Act (signed July 4, 2025, and also called the One Big Beautiful Bill Act) created **Workforce Pell Grants**. These fund eligible workforce programs of 150–599 clock hours that run 8 to 15 weeks. The programs must be approved by a governor and the Department and must meet annual outcome metrics. Grants were available from July 1, 2026 ([final rule, May 19, 2026](https://www.federalregister.gov/documents/2026/05/19/2026-10013/accountability-in-higher-education-and-access-through-demand-driven-workforce-pell-pell-grant)). Products that help institutions run, document, or report on these programs serve a new, funded line of work.
- **AI policy (practitioner observation):** Institutions are writing AI use policies. Your product needs to fit within them.
- **OPM unbundling (practitioner observation):** Institutions are moving away from bundled online program management contracts toward modular services. See the [competitive landscape](competitive-landscape.md) for OPM company status.
- **Transfer and articulation (practitioner observation):** Policy attention to credit transfer between institutions continues.

---
*Originally updated 2026-03-31. Rechecked 2026-10-30 against the sources linked above: the ED accreditation rule, the DOJ Title II rule and its 2026 extension, the Workforce Pell final rule, WICHE projections, and Blackboard's announcement. Items labeled "practitioner view" or "practitioner observation" are judgment, not sourced data. CPHE status rests on press coverage. US-focused.*

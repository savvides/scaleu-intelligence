# Higher Education Landscape

## Accreditation

**What it is:** The quality assurance process for higher education institutions. Accreditation bodies evaluate whether institutions meet established standards for academic quality.

**Why it matters for edtech founders:**
- Accredited institutions must demonstrate that technology used in instruction supports learning outcomes
- If your product delivers or assesses academic content, it may be evaluated during accreditation reviews
- Accreditors increasingly look at how technology is integrated into the curriculum, not just whether it exists

**Regional accreditors (now "institutional accreditors"):**
- HLC (Higher Learning Commission) — Midwest and West
- SACSCOC — Southern states
- MSCHE — Mid-Atlantic states
- NECHE — New England
- NWCCU — Northwest
- WASC/WSCUC — California, Hawaii, Pacific

**Practical guidance:** You don't need accreditation approval to sell your product. But your product should help institutions demonstrate compliance with accreditation standards, not create problems for them. If your product replaces or augments a core academic function (assessment, advising, course delivery), understand how that function is evaluated during accreditation.

## Accessibility in Higher Ed

**Legal requirements:**
- Section 504 of the Rehabilitation Act (all institutions receiving federal funds)
- ADA Title II (public institutions) and Title III (private institutions)
- OCR (Office for Civil Rights) actively investigates accessibility complaints against universities

**Standards:**
- WCAG 2.1 AA is the de facto standard
- Many institutions are moving toward WCAG 2.2
- VPATs (Voluntary Product Accessibility Templates) are commonly required during procurement

**Common procurement requirements:**
- Completed VPAT
- Accessibility statement on your website
- Documented process for addressing accessibility issues
- Some institutions require third-party accessibility audits

**Practical guidance:** Higher ed takes accessibility more seriously than K-12 in procurement. An incomplete or missing VPAT can disqualify you from consideration. Invest in accessibility early.

## LMS Integration

**The big four:**
- **Canvas (Instructure)** — dominant and growing, especially at large institutions
- **Blackboard (Anthology)** — legacy market share, declining
- **D2L Brightspace** — strong in community colleges and Canadian institutions
- **Moodle** — open source, popular internationally and at smaller institutions

**Integration standards:**
- **LTI (Learning Tools Interoperability)** — the primary standard for integrating external tools into an LMS
  - LTI 1.1: basic launch and grade passback
  - LTI 1.3 / Advantage: modern standard with improved security (OAuth 2.0), deep linking, names and roles, assignment and grade services
  - **Build for LTI 1.3.** LTI 1.1 is legacy. Most institutions want 1.3.
- **SIS Integration:** Student Information System integration via SIF, OneRoster, or custom APIs
- **xAPI / Caliper:** Learning analytics standards for tracking learner activity across systems

**Practical guidance:**
- LTI 1.3 integration with Canvas should be your first priority if selling to US higher ed
- Canvas REST API is well-documented and widely used for deeper integrations
- Getting listed on the Canvas App Center or similar marketplace significantly reduces friction
- Single Sign-On (SSO) via SAML or institutional identity providers is often required

## Procurement in Higher Ed

**How it works (simplified):**
1. **Faculty champion:** A professor or department finds your product and wants to use it
2. **Department approval:** Department chair or program director signs off
3. **IT review:** Institutional IT evaluates security, privacy, accessibility, and integration
4. **Procurement/legal:** Contracts, pricing, terms negotiated
5. **Budget approval:** Funding source identified (department budget, grant, provost office)

**Key differences from K-12:**
- Individual faculty often have more autonomy to try new tools (especially free/freemium)
- Procurement thresholds matter: under $5K-$10K may be a departmental decision; over that triggers formal procurement
- Security reviews can take months at large institutions
- Multi-year contracts are common for institution-wide adoption

**Selling to different levels:**
- **Individual faculty:** Fastest adoption, smallest deal, hardest to scale
- **Department:** Medium deal size, requires chair support, often tied to curriculum decisions
- **College/school:** Larger deal, requires dean-level buy-in, longer cycle
- **Institution-wide:** Largest deal, longest cycle (12-24 months), requires IT, provost, and procurement alignment

**Practical guidance:** Start with faculty champions. Let them use it in their courses. Gather evidence of impact. Then use that evidence to pitch department or college-level adoption. Bottom-up adoption is faster than top-down sales in higher ed.

## Higher Ed Buyer Personas

See `buyer-personas.md` for detailed profiles of:
- Chief Information Officer (CIO)
- Provost / VP Academic Affairs
- Department Chair
- Individual Faculty
- Director of Online Learning
- Instructional Designer
- Dean of Students

## Key Trends (2025-2026)

- **AI policy:** Institutions are rapidly developing AI use policies. Your product needs to align with or support institutional AI policies.
- **OPM transition:** The unbundling of Online Program Management (OPM) contracts creates opportunities for modular solutions
- **Enrollment pressure:** Demographic cliff hitting many institutions. Products that demonstrably improve retention and completion have a strong value proposition.
- **Micro-credentials:** Growing interest in shorter, stackable credentials. Products that support this model have tailwind.
- **Transfer and articulation:** Increasing policy focus on credit transfer between institutions. Products that facilitate this address a real pain point.

---
*Last updated: 2026-03-31. US-focused. International higher ed landscapes differ significantly.*

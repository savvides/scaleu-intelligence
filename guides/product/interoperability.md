# Interoperability: what to connect to, and in what order

A school or university adopts a product only after it signs users in, loads rosters, and sits inside the systems staff already use. Build sign-on first, rostering or LMS launch second, and everything else when a signed customer asks for it.

**Applies to:** K-12 and higher ed, with a note on workforce. United States.

## What buyers expect, by segment

"When to build" is ScaleU's view. The rest is drawn from the linked standards bodies and vendors.

| Segment | Integration | Why the buyer needs it | When to build |
|---|---|---|---|
| All | Sign in with Google and Microsoft (OpenID Connect) | No new passwords; accounts die when the school disables them | Before the first pilot |
| K-12 | Clever and ClassLink single sign-on and rostering | Classes appear without teachers typing names; IT controls what data you receive | Before the first district-wide deal |
| K-12 | OneRoster 1.2 (CSV, then REST) | Covers districts that export rosters straight from the SIS | When a district outside Clever and ClassLink asks |
| K-12 | Google Classroom add-on or LTI 1.3 for Canvas and Schoology | Teachers assign and grade without leaving the LMS | When teachers must assign work daily |
| Higher ed | LTI 1.3 with LTI Advantage | Faculty launch the tool from a course; grades return to the gradebook | Before the first course-level pilot |
| Higher ed | SAML single sign-on, later InCommon | Central IT requires the campus identity provider for anything outside the LMS | When a tool has users outside the LMS |
| Either | Direct SIS or ERP integration | Writes official records: enrollment, final grades, billing | Last, and only under contract |
| Workforce | SCORM, xAPI, or cmi5 packaging | The corporate LMS tracks completion | Before the first enterprise deal |
| Credentials | Open Badges 3.0, CLR 2.0 | Learners carry verifiable records elsewhere | Only if you issue credentials |

## Single sign-on

SAML and OpenID Connect (OIDC) are the two protocols underneath every option here. Google and Microsoft sign-in use OIDC and take days, not weeks (practitioner estimate); build both, because most schools run one or the other.

In K-12, districts expect the product in their portal. [Clever](https://www.clever.com/about) reports more than 111,000 schools and 95 of the 100 largest districts. [ClassLink](https://www.classlink.com/) reports more than 3,300 school systems and 25 million students and staff. Both figures are vendor claims.

In higher ed, the campus identity provider speaks SAML, and many campuses belong to a federation. [InCommon](https://incommon.org/federation/) is the US federation, and it connects to [eduGAIN](https://technical.edugain.org/), which listed 84 national federations and about 6,600 identity providers when checked. A company joins InCommon as a sponsored partner: a one-time $700 registration fee, then $2,500 a year for companies under $10 million in revenue ([fee schedule](https://incommon.org/federation/fees/)). Membership saves per-campus metadata exchange once you serve dozens of campuses. Before that, configure SAML campus by campus.

## Rostering

Rostering loads schools, classes, teachers, students, and enrollments, and keeps them current as students move.

- **Clever.** Free for schools. Application partners pay to roster through Secure Sync, at quoted prices, and may not pass that fee to schools ([Clever pricing](https://www.clever.com/pricing)). Budget for it as a cost of sale.
- **ClassLink.** Roster Server delivers rosters from the district using open standards ([ClassLink](https://www.classlink.com/)).
- **OneRoster.** The 1EdTech standard. [Version 1.2](https://www.1edtech.org/standards/oneroster) is current and defines rostering, gradebook, and resource services, each available as REST or CSV. CSV import is the cheapest fallback you can offer.
- **Ed-Fi.** A [data standard](https://www.ed-fi.org/) that states and districts use to join SIS, assessment, and attendance data. It matters when you sell to a state agency or feed a district data warehouse. Skip it otherwise.

## LMS integration

Learning Tools Interoperability (LTI) is how a tool launches inside an LMS. [LTI 1.3](https://www.1edtech.org/standards/lti) is the current version, built on OAuth 2.0 and JSON Web Tokens. 1EdTech [ended all support](https://www.1edtech.org/lti-security-announcement-and-deprecation-schedule) for LTI 1.1 and earlier on June 30, 2022. Do not build 1.1.

LTI Advantage adds three services. Build them in this order (ScaleU's view):

1. **Names and Role Provisioning Services.** The tool reads the course roster and roles, so no separate rostering is needed for course-based products.
2. **Assignment and Grade Services.** The tool creates gradebook columns and posts scores. Faculty ask for this first.
3. **Deep Linking.** An instructor picks a specific item in your tool and places it in the course.

Which LMS to test first depends on segment. In US higher ed, Edutechnica's [14th annual update](https://edutechnica.com/2026/09/27/14th-annual-lms-data-update/) (September 27, 2026) reports that Canvas takes almost all switching institutions, Brightspace is close to passing Blackboard Learn for second place by institution count, and Moodle's decline is accelerating; exact shares are sold, not published. In K-12, [LISTedTECH](https://listedtech.com/blog/k-12-lms-market-update-insights-may-2026/) (May 2026) puts Google Classroom at 31% of tracked implementations, Canvas at 24%, Schoology at 19%, and Moodle at 7%. That is a share of implementations, not of students. Vendor ownership and status are in the [higher-ed landscape](../market/highered-landscape.md#lms-integration) and the [competitive landscape](../market/competitive-landscape.md).

Google Classroom has its own [add-ons framework](https://developers.google.com/workspace/classroom/add-ons) and API. Add-ons work only for teachers whose district licenses the Teaching and Learning or Plus edition of Google Workspace for Education, so confirm the edition before promising the integration.

## SIS and ERP integration

The student information system holds the official record. In K-12 the names you will hear are PowerSchool, Infinite Campus, and Skyward. In higher ed they are Ellucian Banner and Colleague, Workday Student, and Oracle PeopleSoft Campus Solutions. Anthology's SIS and ERP business, with more than 260 customers, now belongs to Ellucian; the sale [closed December 31, 2025](https://campustechnology.com/Articles/2026/01/05/Ellucian-Officially-Acquires-Anthologys-SIS-and-ERP-Business.aspx).

Avoid direct SIS integration early (ScaleU's view). Each SIS has its own API and partner program, each customer runs a different version with local customizations, and the registrar or district data office treats write access as a risk to be refused. A direct integration is a per-customer project with a per-customer support burden. Clever, ClassLink, OneRoster, and LTI exist so that you can read rosters and return grades without touching the SIS. Go direct when your product is the system of action for enrollment, billing, or advising, and then start with nightly file exchange before real-time APIs.

## Content, assessment, and learning data

Build these when a named customer or channel partner requires them. The last column is ScaleU's view.

| Standard | What it carries | Who asks for it |
|---|---|---|
| [QTI 3.0](https://www.1edtech.org/standards/qti) | Assessment items, tests, and results | Assessment vendors, state testing programs |
| [Common Cartridge 1.4](https://www.1edtech.org/standards/cc) and Thin Common Cartridge | Course content packages; the thin form carries only LTI links | Publishers, K-12 curriculum adoptions |
| [Caliper Analytics 1.2](https://www.1edtech.org/standards/caliper) | Learning activity events | Universities with a learning-data warehouse |
| [xAPI](https://standards.ieee.org/ieee/9274.1.1/7321/) (IEEE 9274.1.1-2023) | Activity statements sent to a learning record store | Corporate L&D, military, some universities |
| cmi5 | The rules for launching xAPI content from an LMS ([xAPI overview](https://xapi.com/overview/)) | Corporate LMS buyers moving off SCORM |
| SCORM | Packaged courses with completion and score | Nearly every [corporate LMS](../market/corporate-ld.md) |
| [CASE 1.1](https://www.1edtech.org/standards/case) | Machine-readable academic standards and competencies, each with a unique identifier | K-12 content and assessment products that align to state standards |

## Credentials

If the product issues a credential, issue it in a portable format. [Open Badges 3.0](https://www.1edtech.org/standards/open-badges) credentials are signed as W3C Verifiable Credentials. The [Verifiable Credentials Data Model 2.0](https://www.w3.org/TR/vc-data-model-2.0/) became a W3C Recommendation on May 15, 2025. [CLR Standard 2.0](https://www.1edtech.org/standards/clr) bundles many achievements into one record and can contain Open Badges. A product that issues no credentials can ignore all three.

## AI-era integrations

The Model Context Protocol (MCP) is an [open standard](https://modelcontextprotocol.io/docs/getting-started/intro) for connecting AI applications to outside tools and data. Three things were verifiable when this page was checked:

- Instructure said in [July 2025](https://www.instructure.com/press-release/instructure-launches-igniteai-simplify-and-seamlessly-transform-ai-integration) that partners would connect their agents to its Canvas agent through MCP. It launched [IgniteAI Agent](https://www.instructure.com/press-release/instructure-delivers-its-agentic-ai-promise-launch-igniteai-agent) on March 12, 2026; that release does not mention MCP, and we found no generally available Instructure MCP server.
- 1EdTech [announced](https://www.1edtech.org/1edtech-article/1edtech-leads-collaborative-effort-to-shape-responsible-ai-in-education/411336) on October 21, 2025, a cross-sector effort, building on MCP, to give AI models educational context. No finished specification had been published when checked.
- LTI 1.3 remains the standard that 1EdTech certifies for placing a tool inside a course.

ScaleU's view: ship LTI 1.3 now. Expose a clean, permissioned API so that an MCP server is a thin layer when an LMS vendor opens its agent to partners.

## 1EdTech membership and certification

1EdTech lists three [supplier membership](https://1edtech.org/about/membership/supplier) levels: Contributing, Affiliate, and Alliance. It publishes no dues and asks suppliers to request pricing. Product certification is a member benefit. The specifications themselves are public, so you can build to LTI 1.3 or OneRoster without joining. Join when RFPs or district app-vetting lists start asking for certification; see [vendor review readiness](../selling/vendor-review-readiness.md).

## Build order for a seed-stage company

ScaleU's view, for a company with one or two engineers.

1. **Google and Microsoft sign-in.** Every segment, before any pilot.
2. **The one integration your first ten customers share.** K-12: Clever, then ClassLink. Higher ed: LTI 1.3 launch on Canvas, then roster, grade return, and deep linking.
3. **A CSV roster import in OneRoster format.** It closes deals with customers who fit none of the above.
4. **The second LMS or the second roster provider**, chosen from your pipeline, not from market-share tables.
5. **SAML**, when a campus requires its identity provider for users outside the LMS.
6. **1EdTech certification**, when procurement asks for it in writing.
7. **Data standards, credentials, and direct SIS work**, each only against a signed contract that pays for it.

Two tests keep the order honest. Ask each prospect which systems the product must connect to on day one, and build what three prospects name. Refuse custom integration work that the next customer cannot reuse.

## Related guides

- [Higher-ed landscape](../market/highered-landscape.md): LMS vendors, accessibility, accreditation
- [K-12 landscape](../market/k12-landscape.md)
- [Vendor review readiness](../selling/vendor-review-readiness.md): security, privacy, and accessibility paperwork
- [Procurement guide](../selling/procurement-guide.md)
- [Corporate learning and development](../market/corporate-ld.md)
- [Defensibility](defensibility-moats.md): when integrations create switching costs
- [AI-native framework](ai-native-framework.md)

---
*Facts checked 2026-11-11 against the linked sources. Figures labeled as practitioner estimates are judgment, not data.*

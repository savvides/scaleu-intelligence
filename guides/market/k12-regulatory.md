# K-12 regulatory landscape

Before a US district signs, your product must satisfy two federal privacy laws (FERPA and COPPA), the student privacy law of the district's state, and federal accessibility law. Design to the strictest rule you will face, sign the standard data privacy agreement unmodified if you can, and keep a current VPAT.

**Applies to:** K-12, United States. International rules such as GDPR are not covered here; see [international markets](international-markets.md).

## How to use this page

Start with the checklist, then read the section behind any item you cannot yet tick. The page covers federal law and example states. Treat it as a starting point, and have counsel confirm what applies to you. For the documents a district will ask for, see [vendor review readiness](../selling/vendor-review-readiness.md); for purchasing thresholds and the budget calendar, see the [procurement guide](../selling/procurement-guide.md).

## Checklist for K-12 founders

1. A privacy policy that addresses FERPA, COPPA (including the 2025 amendments), and the state laws where you sell
2. A data governance agreement template ready for districts
3. A decision on the NDPA: whether you can sign the standard agreement and Exhibit E
4. Data minimization: collect only what the educational purpose requires
5. A written data retention and deletion policy
6. A written information security program
7. No advertising or other commercial use of student data
8. Breach notification procedures
9. WCAG 2.1 AA conformance and a current VPAT
10. If the product is directed at children, every user treated as under 13, with school authorization or parental consent
11. An answer to how the product fits a district's AI-use policy, and whether the state reviews AI tools

## Dates to watch

| Date | What happens | Source |
|---|---|---|
| April 22, 2026 (passed) | Compliance deadline for most operators under the amended COPPA Rule | [Federal Register](https://www.federalregister.gov/documents/2025/04/22/2025-05904/childrens-online-privacy-protection-rule) |
| July 1, 2026 (passed) | Ohio districts and schools had to adopt an AI-use policy | [ORC 3301.24](https://codes.ohio.gov/ohio-revised-code/section-3301.24) |
| April 26, 2027 | ADA Title II web rule applies to public entities with a population of 50,000 or more | [Interim final rule](https://www.federalregister.gov/documents/2026/04/20/2026-07663/extension-of-compliance-dates-for-nondiscrimination-on-the-basis-of-disability-accessibility-of-web) |
| June 30, 2027 | North Carolina public school units must adopt AI-use policies | [S.L. 2026-41](https://www.ncleg.gov/EnactedLegislation/SessionLaws/PDF/2025-2026/SL2026-41.pdf) |
| April 26, 2028 | ADA Title II web rule applies to smaller public entities and special district governments | Interim final rule, above |
| August 1, 2028 | Tennessee teachers in grades 6–12 must have completed an approved AI course | [Public Chapter 1056](https://wapp.capitol.tn.gov/apps/BillInfo/Default.aspx?BillNumber=HB0545&GA=114) |

## FERPA (Family Educational Rights and Privacy Act)

FERPA, a federal law, protects the privacy of student education records. It applies to schools and agencies that receive funds from US Department of Education programs, as nearly every public K-12 school does. The regulations are at [34 CFR Part 99](https://www.ecfr.gov/current/title-34/subtitle-A/part-99); the Department's [Student Privacy Policy Office](https://studentprivacy.ed.gov/) publishes guidance for vendors.

What it means for founders:

- A school may not disclose personally identifiable information from education records to you without written consent from a parent (or an eligible student, 18 or older) unless an exception applies.
- The school official exception is the most common path. Under [34 CFR 99.31(a)(1)(i)(B)](https://www.ecfr.gov/current/title-34/subtitle-A/part-99/subpart-D/section-99.31), a school may treat a contractor as a school official if the contractor performs a service for which the school would otherwise use employees, is under the school's direct control with respect to the records, and follows the use and redisclosure limits in [34 CFR 99.33](https://www.ecfr.gov/current/title-34/subtitle-A/part-99/subpart-D/section-99.33).
- Under 99.33 you may use the data only for the purposes for which the school disclosed it, and you may not pass it on without consent. Advertising and other non-educational uses fall outside those purposes.
- Expect a contract that names the data you will receive, why you receive it, and how you will protect it. FERPA sets no deletion deadline for school officials, but most state laws and data privacy agreements require you to return or delete data when the contract ends.

Common mistakes:

- Assuming that parental consent is always required, when the school official exception often applies
- Accessing student data before a data governance agreement is signed
- Keeping student data longer than the agreement allows
- Using student data for advertising or other non-educational purposes

## COPPA (Children's Online Privacy Protection Act)

COPPA, a federal law, governs the online collection of personal information from children under 13. The FTC enforces it. The rule is at [16 CFR Part 312](https://www.ecfr.gov/current/title-16/chapter-I/subchapter-C/part-312).

**The 2025 amendments.** The FTC [amended the COPPA Rule](https://www.federalregister.gov/documents/2025/04/22/2025-05904/childrens-online-privacy-protection-rule) (published April 22, 2025; effective June 23, 2025). Most operators had to comply by April 22, 2026. Among the changes, operators now need:

- Separate verifiable parental consent before disclosing children's information to third parties, such as for targeted advertising, unless the disclosure is integral to the service
- A written data retention policy; children's data may not be kept indefinitely
- A written children's information security program

The FTC proposed rules for edtech and school authorization but left them out of the final rule. The Department of Education had said it intended to propose FERPA amendments, and the FTC wanted to avoid a conflict. A search of the Federal Register on November 11, 2026, found no proposed FERPA rule. The FTC said it will continue to enforce COPPA in schools under its existing guidance, described below.

What it means for founders:

- COPPA applies if your product is directed at children under 13, or if you have actual knowledge that a user is under 13.
- You must obtain verifiable parental consent before collecting personal information, unless the school authorizes collection as described below.
- You must post a clear privacy policy describing your data practices.
- Parents must be able to review their child's information and have it deleted.

**School authorization** (FTC [COPPA FAQ](https://www.ftc.gov/business-guidance/resources/complying-coppa-frequently-asked-questions), section N):

- A school may consent in place of parents only in the educational context, when you collect the data for the use and benefit of the school and for no other commercial purpose.
- You must give the school full notice of your collection, use, and disclosure practices.
- The FAQ recommends, as a best practice, that schools make those notices available to parents.

**Age screening.** Under FAQ D.4, a service directed to children must usually treat every user as a child. Age screening is for general-audience or mixed-audience services that want to identify users under 13; it does not exempt a child-directed product.

Common mistakes:

- Collecting more data from children than the service needs
- Using behavioral advertising in products directed at children
- Treating an age gate as a way out of COPPA for a product built for children
- Assuming that an educational purpose covers any feature you want to build

## State student privacy laws

Most states have their own student privacy laws, and many are stricter than FERPA. We found no current, dated national count. The [Future of Privacy Forum](https://fpf.org/issue/education/), which absorbed Student Privacy Compass, tracks state laws. Four commonly cited examples:

| State and law | Main requirements |
|---|---|
| California: SOPIPA, [Bus. & Prof. Code 22584](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=BPC&sectionNum=22584) | No targeted advertising and no profiles built for non-educational purposes; no sale of student data; reasonable security; deletion at the school's request |
| New York: [Education Law 2-d](https://www.nysenate.gov/legislation/laws/EDN/2-D) | Every contract with a vendor that receives student data must include a data security and privacy plan; each school publishes a parents' bill of rights for data privacy and security on its website and includes it with every such contract; parents can file complaints about possible breaches |
| Colorado: [Student Data Transparency and Security Act](https://www.cde.state.co.us/dataprivacyandsecurity) | Transparency about the data elements vendors collect; no targeted advertising; breach notification |
| Illinois: SOPPA, [105 ILCS 85](https://www.ilga.gov/legislation/ilcs/ilcs3.asp?ActID=3806&ChapterID=17) | A written agreement between school and vendor before data sharing; schools must post a list of vendors, a copy of each written agreement, and a list of breaches; a vendor must notify the school within 30 calendar days of determining that a breach occurred |

The California, New York, and Illinois rows were checked against the statutes on November 11, 2026. The Colorado row was not: the linked Department of Education page names the act (House Bill 16-1423) but does not summarize it.

Practitioner view: if you sell to K-12 nationally, design to the strictest requirements you will face. Many founders treat California and New York as a baseline, then check each new state.

## Student Data Privacy Consortium (SDPC)

The SDPC is a [special interest group of the Access 4 Learning (A4L) Community](https://privacy.a4l.org/) in which districts, states, and vendors use shared data privacy agreements.

- Many districts will ask you to sign the National Data Privacy Agreement (NDPA). State-specific versions add state law requirements.
- When you sign the standard NDPA with one district, you also sign Exhibit E, the General Offer of Privacy Terms. Other districts covered by that agreement can then subscribe to the same privacy terms without renegotiating ([NDPA v2 usage guide](https://files.a4l.org/privacy/NDPA/NDPAv2_Usage_Guide_and_Development_Process.pdf)). Price and other commercial terms are still negotiated separately.
- Search the [SDPC Resource Registry](https://privacy.a4l.org/sdpc-resource-registry/) to see which agreements you or your competitors have already signed.

Read the NDPA template early. A vendor that signs it unmodified clears one of procurement's slowest steps (practitioner view).

## Accessibility requirements

**Section 504 and the ADA.** Schools must give students with disabilities equal access to education, including the digital tools they use.

**ADA Title II web rule.** The Department of Justice's [2024 rule](https://www.ada.gov/resources/2024-03-08-web-rule/) requires state and local government entities, including public school districts, to make web content and mobile apps conform to WCAG 2.1 Level AA. It covers content provided through contractors. An [interim final rule published April 20, 2026](https://www.federalregister.gov/documents/2026/04/20/2026-07663/extension-of-compliance-dates-for-nondiscrimination-on-the-basis-of-disability-accessibility-of-web) extended the compliance dates:

- April 26, 2027, for public entities with a total population of 50,000 or more
- April 26, 2028, for public entities with a population under 50,000, and for special district governments

Which date applies depends on the population of the jurisdiction the district serves ([28 CFR 35.200](https://www.ecfr.gov/current/title-28/chapter-I/part-35/subpart-H/section-35.200)). The standard did not change, and DOJ said it may revisit the rule, so check the current text. The regulation and the Department's page both showed these two dates on November 11, 2026.

**Voluntary Product Accessibility Template (VPAT).** During procurement, many districts and states require a completed VPAT, which documents how your product conforms to accessibility standards.

## AI-specific federal guidance

We found no federal statute specific to AI in schools as of October 2026. Two Department of Education actions affect how districts may spend federal money on AI:

- A [July 22, 2025 guidance letter](https://www.ed.gov/about/news/press-release/us-department-of-education-issues-guidance-artificial-intelligence-use-schools-proposes-additional-supplemental-priority) on using existing federal grant funds for AI tools, tutoring, and advising.
- A [final supplemental grant priority on advancing AI in education](https://www.federalregister.gov/documents/2026/04/13/2026-07087/final-priority-and-definitions-secretarys-supplemental-priority-and-definitions-on-advancing), effective May 13, 2026, which the Department may apply to its discretionary grant competitions.

Many states and districts publish their own AI guidance; check the state where you sell. For product-level risk, see [AI risk and trust](../product/ai-risk-and-trust.md).

## State AI requirements

Some states have turned AI guidance into law. In SETDA's [2026 State EdTech Trends Report](https://www.setda.org/priorities/state-trends/), 23% of state agency respondents said their state's AI guidance is now required by law, up from 4% in 2024 ([field note](../../sources/notes/2026-10-30-setda-state-edtech-trends-2026.md)). Three examples, checked at the source on November 11, 2026:

- **Ohio** ([ORC 3301.24](https://codes.ohio.gov/ohio-revised-code/section-3301.24)): each school district, community school, and STEM school had to adopt a policy on AI use by July 1, 2026. Schools may adopt the state's model policy.
- **North Carolina** ([S.L. 2026-41](https://www.ncleg.gov/EnactedLegislation/SessionLaws/PDF/2025-2026/SL2026-41.pdf), section 7.39):
  - Public school units must adopt AI-use policies by June 30, 2027. The model policy they review must cover data privacy and security, including protection of personally identifiable information.
  - The Department of Public Instruction must keep a framework for evaluating generative AI tools on privacy, standards alignment, and accessibility, and publish the list of tools it has reviewed.
  - The Department must also set procurement guidance and qualified vendor lists that favor reviewed tools, and publish a list of every AI tool used in public school units.
- **Tennessee** ([Public Chapter 1056](https://wapp.capitol.tn.gov/apps/BillInfo/Default.aspx?BillNumber=HB0545&GA=114), 2026): teachers in grades 6–12 must complete a department-approved AI course by August 1, 2028, or within two years of licensure, whichever is later.

What it means for founders: a district with an AI-use policy will ask how your product fits it. In North Carolina, the state's review list and vendor lists are meant to steer districts toward reviewed tools. Before you sell in a state, find out whether it reviews AI tools, and on what criteria.

## Related guides

- [K-12 landscape](k12-landscape.md)
- [Vendor review readiness](../selling/vendor-review-readiness.md)
- [Procurement guide](../selling/procurement-guide.md)
- [AI risk and trust](../product/ai-risk-and-trust.md)
- [Trust packet checklist](../templates/trust-packet-checklist.md)

---
*Facts checked 2026-10-30 against the linked primary sources, with an independent spot-check on 2026-11-11 of the COPPA amendment's effective and compliance dates and the FTC's COPPA FAQ; the Title II dates in 28 CFR 35.200, the interim final rule, and ADA.gov; the California, New York, and Illinois statutes; ORC 3301.24, S.L. 2026-41 section 7.39, and Tennessee's page for HB 545; the AI grant priority's effective date; and the Federal Register for a proposed FERPA rule (none found). Not rechecked on 2026-11-11: the FERPA regulations' text, the NDPA documents, the July 2025 guidance letter, and the Colorado row. The 23% figure is from SETDA's survey (page 11). Items labeled practitioner view are judgment, not data.*

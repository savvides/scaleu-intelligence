# K-12 Regulatory Landscape

**Answers:** Which privacy and accessibility rules must a US K-12 product meet before a district will sign? Use this guide when you scope a K-12 product, write a privacy policy, or prepare for a district's data privacy and security review.

**Audience:** K-12, United States. It covers federal law and four example states; it is a starting checklist, not legal advice. Confirm current requirements at the linked primary sources and with counsel. For purchasing thresholds and the budget calendar, see the [procurement guide](../selling/procurement-guide.md).

## FERPA (Family Educational Rights and Privacy Act)

**What it is:** Federal law that protects the privacy of student education records. It applies to schools and agencies that receive funds from US Department of Education programs, which includes virtually all public K-12 schools. Regulations: [34 CFR Part 99](https://www.ecfr.gov/current/title-34/subtitle-A/part-99). Guidance for vendors: the Department's [Student Privacy Policy Office](https://studentprivacy.ed.gov/).

**What it means for edtech founders:**
- A school may not disclose personally identifiable information (PII) from education records to you without written consent from a parent (or an eligible student, 18 or older) unless an exception applies.
- The "school official" exception is the most common path. Under [34 CFR 99.31(a)(1)(i)(B)](https://www.ecfr.gov/current/title-34/subtitle-A/part-99/subpart-D/section-99.31), a contractor can be treated as a school official if it performs a service the school would otherwise use employees for, is under the school's direct control with respect to the records, and follows the use and redisclosure limits in [34 CFR 99.33](https://www.ecfr.gov/current/title-34/subtitle-A/part-99/subpart-D/section-99.33).
- Under 99.33 you may use the data only for the purposes for which the school disclosed it, and you may not pass it on without consent. Advertising or other non-educational use falls outside those purposes.
- Expect a contract that names the data you'll receive, why, and how you'll protect it. FERPA itself does not spell out a deletion deadline for school officials, but most state laws and data privacy agreements require you to return or delete data when the contract ends.

**Common mistakes:**
- Assuming parental consent is always required (the school official exception often applies)
- Accessing student data before a data governance agreement is signed
- Keeping student data longer than the agreement allows
- Using student data for advertising or other non-educational purposes

## COPPA (Children's Online Privacy Protection Act)

**What it is:** Federal law that governs the online collection of personal information from children under 13. Enforced by the FTC. Rule: [16 CFR Part 312](https://www.ecfr.gov/current/title-16/chapter-I/subchapter-C/part-312).

**2025 amendments:** The FTC [amended the COPPA Rule](https://www.federalregister.gov/documents/2025/04/22/2025-05904/childrens-online-privacy-protection-rule) (published April 22, 2025; effective June 23, 2025). Most operators had to comply by **April 22, 2026**. Among the changes, operators now need:
- Separate verifiable parental consent before disclosing children's information to third parties, such as for targeted advertising, unless the disclosure is integral to the service
- A written data retention policy; children's data may not be kept indefinitely
- A written children's information security program

The FTC proposed codifying rules for edtech and school authorization but did not finalize them. The Department of Education had said it intended to propose FERPA amendments, and the FTC wanted to avoid a conflict. No FERPA proposed rule had appeared in the Federal Register by the October 2026 recheck. It said it will continue to enforce COPPA in schools under its existing guidance (below).

**What it means for edtech founders:**
- If your product is directed at children under 13, or you have actual knowledge that a user is under 13, COPPA applies.
- You must obtain verifiable parental consent before collecting personal information, unless the school authorizes collection as described below.
- You must post a clear privacy policy describing your data practices.
- Parents must be able to review their child's information and have it deleted.

**The school authorization mechanism** (FTC [COPPA FAQ](https://www.ftc.gov/business-guidance/resources/complying-coppa-frequently-asked-questions), section N):
- A school may consent in place of parents only in the educational context, when you collect the data for the use and benefit of the school and for no other commercial purpose.
- You must give the school full notice of your collection, use, and disclosure practices.
- The FAQ recommends, as a best practice, that schools make those notices available to parents.

**Age screening:** Under FAQ D.4, a service directed to children must in most cases treat every user as a child. Age screening is for general-audience or mixed-audience services that want to identify users under 13; it does not exempt a child-directed product.

**Common mistakes:**
- Collecting more data than necessary from children
- Using behavioral advertising in products directed at children
- Treating an age gate as a way out of COPPA for a product built for children
- Assuming "educational purpose" covers any feature you want to build

## State Student Privacy Laws

**The patchwork problem:** Most states have their own student privacy laws, and many are stricter than FERPA. No current, dated national count was found during the October 2026 recheck. The [Future of Privacy Forum](https://fpf.org/issue/education/), which absorbed Student Privacy Compass, tracks state laws. Four commonly cited examples:

**California (SOPIPA, [Bus. & Prof. Code 22584](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=BPC&sectionNum=22584)):**
- Cannot use student data for targeted advertising or to build profiles for non-educational purposes
- Cannot sell student data
- Must maintain reasonable security
- Must delete student data at the school's request

**New York ([Education Law 2-d](https://www.nysenate.gov/legislation/laws/EDN/2-D)):**
- Every contract with a vendor that receives student data must include a data security and privacy plan
- Each school publishes a parents' bill of rights for data privacy and security on its website and includes it with every such contract
- Parents can file complaints about possible breaches

**Colorado ([Student Data Transparency and Security Act](https://www.cde.state.co.us/dataprivacyandsecurity)):**
- Requires transparency about the data elements vendors collect
- Prohibits use of student data for targeted advertising
- Requires breach notification

**Illinois (SOPPA, [105 ILCS 85](https://www.ilga.gov/legislation/ilcs/ilcs3.asp?ActID=3806&ChapterID=17)):**
- Requires a written agreement between the school and the vendor before data sharing
- Schools must post a list of vendors, a copy of each written agreement, and a list of breaches
- Specific breach notification requirements

The New York and Illinois points were rechecked against the statutes in October 2026. The California and Colorado points were not.

**Practical guidance (practitioner view):** If you sell to K-12 nationally, design to the strictest requirements you will face. Many founders treat California and New York as a baseline, then check each new state.

## Student Data Privacy Consortium (SDPC)

**What it is:** A [special interest group of the Access 4 Learning (A4L) Community](https://privacy.a4l.org/) where districts, states, and vendors use shared data privacy agreements.

**Why it matters for founders:**
- Many districts will ask you to sign the National Data Privacy Agreement (NDPA). State-specific versions add state law requirements.
- Once you sign the standard NDPA with one district, you also sign Exhibit E, the General Offer of Privacy Terms. Other districts covered by that agreement can then subscribe to the same privacy terms without renegotiating ([NDPA v2 usage guide](https://files.a4l.org/privacy/NDPA/NDPAv2_Usage_Guide_and_Development_Process.pdf)). Price and other commercial terms are still negotiated separately.
- Search the [SDPC Resource Registry](https://privacy.a4l.org/sdpc-resource-registry/) to see which agreements you or your competitors have already signed.

**Practical guidance:** Read the NDPA template early. If you can sign it without modifications, you remove a major procurement blocker.

## Accessibility Requirements

**Section 504 & ADA:** Schools must give students with disabilities equal access to education, and that includes the digital tools they use.

**ADA Title II web rule:** The Department of Justice's [2024 rule](https://www.ada.gov/resources/2024-03-08-web-rule/) requires state and local government entities, including public school districts, to make web content and mobile apps conform to **WCAG 2.1 Level AA**. It covers content provided through contractors. An [interim final rule published April 20, 2026](https://www.federalregister.gov/documents/2026/04/20/2026-07663/extension-of-compliance-dates-for-nondiscrimination-on-the-basis-of-disability-accessibility-of-web) extended the compliance dates:
- **April 26, 2027** for public entities with a total population of 50,000 or more
- **April 26, 2028** for public entities with a population under 50,000, and for special district governments

Which date applies depends on the population of the jurisdiction the district serves ([28 CFR 35.200](https://www.ecfr.gov/current/title-28/chapter-I/part-35/subpart-H/section-35.200)). The standard did not change, and DOJ said it may revisit the rule, so check the current text.

**Voluntary Product Accessibility Template (VPAT):** Many districts and states require a completed VPAT during procurement. It documents how your product conforms to accessibility standards.

## AI-Specific Federal Guidance

No federal statute specific to AI in schools was found during the October 2026 recheck. Two Department of Education actions affect how districts may spend federal money on AI:
- A [July 22, 2025 guidance letter](https://www.ed.gov/about/news/press-release/us-department-of-education-issues-guidance-artificial-intelligence-use-schools-proposes-additional-supplemental-priority) on using existing federal grant funds for AI tools, tutoring, and advising.
- A [final supplemental grant priority on advancing AI in education](https://www.federalregister.gov/documents/2026/04/13/2026-07087/final-priority-and-definitions-secretarys-supplemental-priority-and-definitions-on-advancing), effective May 13, 2026, which the Department may apply to its discretionary grant competitions.

Many states and districts publish their own AI guidance; check the state you are selling into. For product-level risk, see [AI risk and trust](../product/ai-risk-and-trust.md).

## State AI requirements

Some states have turned AI guidance into law. In SETDA's [2026 State EdTech Trends Report](https://www.setda.org/priorities/state-trends/), 23% of state agency respondents said their state's AI guidance is now required by law, up from 4% in 2024 ([field note](../../sources/notes/2026-10-30-setda-state-edtech-trends-2026.md)). Three examples, checked at the source in October 2026:

- **Ohio** ([ORC 3301.24](https://codes.ohio.gov/ohio-revised-code/section-3301.24)): each school district, community school, and STEM school had to adopt a policy on AI use by July 1, 2026. Schools may adopt the state's model policy.
- **North Carolina** ([S.L. 2026-41](https://www.ncleg.gov/EnactedLegislation/SessionLaws/PDF/2025-2026/SL2026-41.pdf), section 7.39):
  - Public school units must adopt AI-use policies by June 30, 2027. The model policy they review must cover data privacy and security, including protection of personally identifiable information.
  - The Department of Public Instruction must keep a framework for evaluating generative AI tools on privacy, standards alignment, and accessibility, and publish the list of tools it has reviewed.
  - The Department must also set procurement guidance and qualified vendor lists that favor reviewed tools, and publish a list of every AI tool used in public school units.
- **Tennessee** ([Public Chapter 1056](https://wapp.capitol.tn.gov/apps/BillInfo/Default.aspx?BillNumber=HB0545&GA=114), 2026): teachers in grades 6–12 must complete a department-approved AI course by August 1, 2028, or within two years of licensure, whichever is later.

**What it means for edtech founders:** A district with an AI-use policy will ask how your product fits it. In North Carolina, the state's review list and vendor lists are meant to steer districts toward reviewed tools. Find out whether a state reviews AI tools, and on what criteria, before you sell there.

## Practical Checklist for K-12 Edtech Founders

1. [ ] Privacy policy that addresses FERPA, COPPA (including the 2025 amendments), and the state laws where you sell
2. [ ] Data governance agreement template ready for districts
3. [ ] NDPA familiarity (can you sign the standard agreement and Exhibit E?)
4. [ ] Data minimization: only collect what you need for educational purposes
5. [ ] Written data retention and deletion policy
6. [ ] Written information security program
7. [ ] No advertising or commercial use of student data
8. [ ] Breach notification procedures in place
9. [ ] WCAG 2.1 AA conformance and a current VPAT
10. [ ] If the product is directed at children, treat every user as under 13 and use school authorization or parental consent

---
*Originally updated 2026-03-31. Rechecked 2026-10-30 against the primary sources linked above: FERPA regulations, the COPPA Rule and FAQ, the New York and Illinois statutes, the SDPC/NDPA documents, the DOJ Title II rule and its 2026 extension, and the Department of Education AI actions. California and Colorado details were not rechecked. US-focused. International rules such as GDPR are not covered in this library.*

*Edited 2026-10-30: added state AI requirements. The Ohio, North Carolina, and Tennessee provisions were checked against ORC 3301.24, S.L. 2026-41 section 7.39, and the Tennessee General Assembly's page for HB 545 / SB 677. The 23% figure is from SETDA's survey (page 11).*

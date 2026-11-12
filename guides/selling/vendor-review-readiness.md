# Vendor review readiness

Security, privacy, and accessibility reviewers can stop a deal the buyer already wants. Prepare the free documents before your first demo, buy an audit when a signed deal depends on it, and never claim a control you lack.

**Applies to:** K-12 and higher ed. United States.

## What to prepare, in priority order

Effort and cost figures are practitioner estimates for a company of 5 to 30 people, not sourced data.

| # | Item | Who asks | When in the deal | Effort (estimate) |
|---|---|---|---|---|
| 1 | Privacy policy and terms that match what the product does | Everyone; rating bodies read them unasked | Before the first demo | 1–2 weeks; $2,000–$10,000 if counsel drafts |
| 2 | Data inventory, data-flow diagram, subprocessor list | K-12 privacy officer, higher-ed security office | First technical conversation | 2–5 days, founder time |
| 3 | Signable data privacy agreement (NDPA and state versions) | K-12 district | Before any student data moves | Days to read; free to sign |
| 4 | Accessibility Conformance Report (completed VPAT) | Higher ed always; K-12 increasingly | First serious meeting | 2–4 weeks; $5,000–$20,000 with an outside audit |
| 5 | Security questionnaire: HECVAT (higher ed), K-12CVAT or the district's form | IT security | After the champion says yes | 20–40 hours the first time |
| 6 | AI statement | Any buyer of an AI feature | Same time as the questionnaire | 1–2 days |
| 7 | Penetration test summary | IT security; SOC 2 auditors | Contract stage | 2–4 weeks; $5,000–$25,000 |
| 8 | Cyber liability insurance certificate | Procurement, contract terms | Contract stage | 1–3 weeks; premium varies with revenue and data held |
| 9 | SOC 2 Type I, then Type II | Large districts, universities, employers | Enterprise deals | Type I: 2–4 months, $15,000–$40,000. Type II: add a 3–12 month observation period, $25,000–$60,000 a year |
| 10 | ISO/IEC 27001 certification | International buyers, some enterprises | When a buyer names it | 6–12 months; $30,000–$75,000 |
| 11 | Third-party privacy or trust badges | Some districts; marketing | Optional | Varies; fees mostly unpublished |

Items 1 through 6 cost time and little money. Do them first: together they answer most of what a district or department asks. The [trust packet checklist](../templates/trust-packet-checklist.md) turns this table into a folder.

## K-12 privacy paperwork

**The law.** FERPA's school official exception, COPPA, and the state statutes are covered in [K-12 regulation](../market/k12-regulatory.md). This page covers the documents that prove you comply.

**The National Data Privacy Agreement.** The Student Data Privacy Consortium's [NDPA](https://privacy.a4l.org/national-dpa/) is the contract most districts send. The current standard is version 2.2. The Consortium reports more than 230,000 signed agreements across 13,000 districts and 35 state alliances. State alliances publish their own versions with state-law terms added, so ask which version your buyer uses. Sign it unmodified if you can: each change sends the agreement to the district's lawyer. The regulatory guide explains [Exhibit E](../market/k12-regulatory.md#student-data-privacy-consortium-sdpc), which lets other districts adopt terms you have already signed.

**The Student Privacy Pledge is retired.** The Future of Privacy Forum [retired the pledge](https://fpf.org/student-privacy-pledge/) on April 25, 2025, ten years after it began, and asked signatories to remove every reference to it. Take the badge off your site. FPF points companies to the NDPA and to CISA's K-12 Education Technology Secure by Design Pledge instead.

**State requirements you will meet most often.**

- **New York.** [Education Law 2-d](https://www.nysenate.gov/legislation/laws/EDN/2-D) requires every contract to carry a data security and privacy plan and a signed copy of the district's parents' bill of rights. Staff with access to the data must be trained on confidentiality law. The statute sets civil penalties and lets the state bar a vendor from receiving data for up to five years. The regulation, [8 NYCRR 121.9](https://www.law.cornell.edu/regulations/new-york/8-NYCRR-121.9), requires practices aligned with the NIST Cybersecurity Framework and encryption of personal data in motion and at rest, and bans sale or commercial use. Expect each district to send its own rider.
- **Texas.** [Education Code 32.152](https://texas.public.law/statutes/tex._educ._code_section_32.152) bars operators from targeted advertising based on school-purpose data, from building student profiles for non-school purposes, and from selling or renting student information. Neighboring sections cover protection and deletion. Public universities and state agencies may also require certification under [TX-RAMP](https://dir.texas.gov/information-security/texas-risk-and-authorization-management-program-tx-ramp), the state's assessment program for cloud services; ask the institution whether your product falls in scope.
- **California and Illinois.** SOPIPA and SOPPA are summarized in the [regulatory guide](../market/k12-regulatory.md#state-student-privacy-laws). Illinois districts must post each vendor agreement publicly, so competitors and other buyers can read your signed terms. Neither statute's site could be reopened on November 11, 2026, so rely on that guide's dated check.

**K-12 security questionnaire.** CoSN's [K-12CVAT](https://www.cosn.org/tools-and-resources/resource/k-12cvat/) (Lite version 4.1) is a free questionnaire modeled on higher ed's HECVAT Lite. Complete it once and send the same file to every district.

## Higher-ed security review

**HECVAT.** EDUCAUSE's [Higher Education Community Vendor Assessment Toolkit](https://www.educause.edu/hecvat) is a questionnaire on cybersecurity, privacy, IT accessibility, and compliance. The current version is 4.1.6, and version 4 added privacy and AI questions. EDUCAUSE publishes it free. Fill it out before anyone asks. Answer "no" where the answer is no, and add a date by which it becomes "yes." Reviewers forgive gaps in a young company and do not forgive a false answer in a document attached to a contract.

**SOC 2.** A SOC 2 report is a CPA firm's examination of your controls against the AICPA's trust services criteria: security, availability, processing integrity, confidentiality, and privacy ([AICPA](https://www.aicpa-cima.com/topic/audit-assurance/audit-and-assurance-greater-than-soc-2)). A Type I report assesses the design of your controls as of one date. A Type II report tests whether those controls worked over a period of months, and it is the one enterprise buyers want (the audit firm KirkpatrickPrice [explains the difference](https://kirkpatrickprice.com/video/soc-2-type-i-vs-soc-2-type-ii/); the AICPA page linked above does not spell it out). ScaleU's view: start Type I when a buyer worth more than the audit asks for it in writing, and tell every earlier buyer your timeline.

**ISO/IEC 27001.** The [2022 edition](https://www.iso.org/standard/27001) sets requirements for an information security management system, and an accredited body certifies you against it. US schools seldom require it. Buyers abroad often prefer it to SOC 2.

**Penetration test.** An outside firm attacks your application and reports what it found. Buyers want the summary letter and proof that you fixed the serious findings, dated within the past 12 months.

**Cyber insurance.** Contracts often set a minimum cyber liability limit; $1M to $5M is common (practitioner estimate). Read the insurance clause before you quote a price, because the premium is a cost of that deal.

## Accessibility

A VPAT is the Information Technology Industry Council's blank template; the filled-in document is an Accessibility Conformance Report. The [current template](https://www.itic.org/policy/accessibility/vpat) is version 2.5Rev (April 2025). Use the WCAG edition, which covers WCAG 2.0, 2.1, and 2.2, unless a buyer asks for the Section 508 or EU edition.

Public buyers now face their own deadline. The Justice Department's ADA Title II rule requires state and local government web content and mobile apps to meet WCAG 2.1 Level AA. An [interim final rule of April 20, 2026](https://www.federalregister.gov/documents/2026/04/20/2026-07663/extension-of-compliance-dates-for-nondiscrimination-on-the-basis-of-disability-accessibility-of-web) moved the compliance date from April 24, 2026, to April 26, 2027, for entities with a population of 50,000 or more, and from April 26, 2027, to April 26, 2028, for smaller entities and special district governments. [ADA.gov](https://www.ada.gov/resources/2024-03-08-web-rule/) shows the same dates. The obligation falls on the school or college, which passes it to you by contract. See the regulatory guide's [accessibility section](../market/k12-regulatory.md#accessibility-requirements).

Write the report from real testing with a screen reader and a keyboard. Mark criteria "partially supports" where that is true, and attach a dated plan to fix them. A report that claims full support on every line tells a reviewer that nobody tested.

## Badges and ratings

The law requires none of these. Pursue one when a buyer names it.

| Program | What it is | What it takes |
|---|---|---|
| [1EdTech TrustEd Apps](https://www.1edtech.org/program/trustedapps) | Rubrics for data privacy, security practices, accessibility, and generative AI data, shown in a product directory districts consult | Vetting or self-attestation. The [generative AI rubric](https://www.1edtech.org/standards/ai-rubric) is open only to 1EdTech member organizations and should be redone each year |
| [Common Sense privacy ratings](https://privacy.commonsense.org/resource/privacy-ratings) | A Pass, Warning, or Fail rating drawn from your public privacy policy and terms | Nothing; you may be rated without asking. A Pass requires policies that rule out selling data, targeted ads, third-party tracking, and commercial profiling |
| [iKeepSafe](https://ikeepsafe.org/certifications/) | Certifications for FERPA, COPPA Safe Harbor, California student privacy, and independent schools (ATLIS) | A technical assessment of your data flows against your policy; fees are not published |

Check your Common Sense rating now. A Warning usually comes from a policy that says nothing on a practice, and a clear sentence fixes it.

## AI vetting questions

Buyers now add AI questions to every review, and they doubt vendor answers. The [procurement guide](procurement-guide.md#what-state-edtech-offices-told-setda-k-12-2026) reports that most state agency respondents find AI claims hard to verify. Three frameworks shape what they ask:

- **EDSAFE AI Alliance.** The [SAFE Benchmarks Framework](https://www.edsafeai.org/safe), begun in 2021, groups expectations under safety, accountability, fairness and transparency, and efficacy.
- **1EdTech.** The generative AI data rubric asks whether users are told when AI is in use, whether they can opt in or out, whether the privacy policy describes AI use, where the data comes from, and whether the model is yours or a third party's.
- **CoSN and the Council of the Great City Schools.** The [K-12 Gen AI Readiness Checklist](https://www.cosn.org/tools-and-resources/resource/k12-generative-ai-gen-ai-readiness-checklist-questionnaire/) is written for districts, and districts turn its questions on vendors.

Some states now review AI tools themselves; see [state AI requirements](../market/k12-regulatory.md#state-ai-requirements).

Write one page that answers the questions these frameworks share (ScaleU's synthesis):

1. Which features use AI, and which model provider receives the data?
2. Does any customer or student data train a model, yours or the provider's?
3. How long does the provider keep prompts and outputs?
4. Can a district turn AI features off, by school or by grade?
5. What does a human review before a student sees output?
6. How did you test for bias and for wrong answers, and what did you find?
7. What evidence shows the feature improves learning? See [evidence tiers](../evidence/evidence-tiers.md).

Product-level guidance is in [AI risk and trust](../product/ai-risk-and-trust.md).

## The trust packet

Hand a buyer one folder on day one, with an index page and a named contact:

1. Privacy policy, terms, and a one-page data inventory.
2. Signed or signable NDPA, plus the state versions you have executed.
3. Completed HECVAT or K-12CVAT.
4. Accessibility Conformance Report with test method and a dated plan for gaps.
5. Security overview, data-flow diagram, and subprocessor list.
6. AI statement.
7. Penetration test summary and SOC 2 report, or the date you expect each.
8. Insurance certificate.
9. Incident response and breach notification commitment.

Date every document within the past 12 months. The [trust packet checklist](../templates/trust-packet-checklist.md) is the working version. Once the packet clears review, the remaining work is the sale: see [go-to-market](go-to-market.md).

## Related guides

- [Go-to-market](go-to-market.md)
- [Procurement guide](procurement-guide.md)
- [K-12 regulation](../market/k12-regulatory.md)
- [Interoperability](../product/interoperability.md)
- [AI risk and trust](../product/ai-risk-and-trust.md)
- [Trust packet checklist](../templates/trust-packet-checklist.md)

---
*Facts checked 2026-11-11 against the linked sources, with an independent spot-check the same day of the NDPA figures, the pledge's retirement, the HECVAT and K-12CVAT versions, the VPAT edition, the ADA Title II dates (against the Federal Register and ADA.gov), the New York regulation, the Texas statute, and the badge programs. The SOC 2 Type I and Type II distinction rests on an audit firm's explanation, not an AICPA page. The spot-check could not reopen the New York Senate, ISO, or TX-RAMP pages, which refused automated access. Figures labeled as practitioner estimates are judgment, not data. Not legal advice.*

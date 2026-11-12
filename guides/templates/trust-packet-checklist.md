# Trust packet checklist

This checklist names the security, privacy, and accessibility documents to assemble before a first enterprise conversation. A good packet lives in one folder, is dated within the last 12 months, and goes out the day a buyer asks. [Vendor review readiness](../selling/vendor-review-readiness.md) explains each document, what reviewers look for, and what to do when you lack one; this page only lists them.

**Applies to:** K-12 and higher ed in the United States. Employers ask for the security and privacy items and rarely the education-specific ones. ScaleU template: no law prescribes this list, and each buyer sets its own.

## Checklist

Mark each item ready, in progress, or not applicable, with the document's date and its owner.

### Security

- [ ] Completed security questionnaire. In higher ed this is usually EDUCAUSE's HECVAT; in K-12, CoSN's K-12CVAT or the district's own form; employers send their own. [date] [owner]
- [ ] Independent assurance: a SOC 2 report, or, until you have one, a recent penetration-test summary and a letter stating your audit timeline. [date] [owner]
- [ ] Security overview, two pages: hosting, encryption in transit and at rest, access control, logging, backups. [date] [owner]
- [ ] Architecture and data-flow diagram showing where student data enters, rests, and leaves. [date] [owner]
- [ ] Subprocessor list, including AI model providers, with what each receives. [date] [owner]
- [ ] Incident response plan and breach-notification commitment. [date] [owner]
- [ ] Single sign-on and rostering support, with the standards you implement (see [interoperability](../product/interoperability.md)). [date] [owner]

### Privacy

- [ ] Privacy policy and terms of service that match what the product does. [date] [owner]
- [ ] Data inventory: every data element collected, why, where stored, and how long kept. [date] [owner]
- [ ] Data privacy agreement you can sign. In K-12, be ready for the district's own form or the Student Data Privacy Consortium's [National Data Privacy Agreement](https://privacy.a4l.org/national-dpa/) and state addenda. [date] [owner]
- [ ] FERPA statement: how the product meets the three conditions for a contractor acting as a school official ([34 CFR 99.31(a)(1)(i)(B)](https://www.law.cornell.edu/cfr/text/34/99.31)), which [K-12 regulation](../market/k12-regulatory.md) lists. [date] [owner]
- [ ] If children under 13 use the product: how you handle the Children's Online Privacy Protection Rule, which defines a child as an individual under 13 ([16 CFR 312.2](https://www.law.cornell.edu/cfr/text/16/312.2)). See [K-12 regulation](../market/k12-regulatory.md). [date] [owner]
- [ ] Data deletion and return procedure, with the time limit you commit to. [date] [owner]
- [ ] AI statement: which features use AI models, whether customer data trains any model, and what a human reviews (see [AI risk and trust](../product/ai-risk-and-trust.md)). [date] [owner]

### Accessibility

- [ ] Accessibility Conformance Report: the completed form of the Information Technology Industry Council's [VPAT](https://www.itic.org/policy/accessibility/vpat). The current template is version 2.5Rev (April 2025), in WCAG, Section 508, EU, and international editions. [date] [owner]
- [ ] Who tested, how, and when: internal audit or third party, with assistive technologies used. [date] [owner]
- [ ] Roadmap for known gaps, with dates. [date] [owner]
- [ ] Accessibility contact and the process for handling a reported barrier. [date] [owner]

Expect public buyers to ask for WCAG 2.1 Level AA conformance in writing. The Justice Department's ADA Title II rule requires it of their web content and mobile apps by April 26, 2027, for entities with a population of 50,000 or more, and by April 26, 2028, for smaller entities and special district governments ([interim final rule, April 20, 2026](https://www.govinfo.gov/content/pkg/FR-2026-04-20/html/2026-07663.htm)).

### Commercial

- [ ] Order form or master agreement, and the terms you will accept on the buyer's paper. [date] [owner]
- [ ] Ability to accept a purchase order and issue an invoice; W-9; vendor registration details. [date] [owner]
- [ ] Certificate of insurance, including cyber liability if the buyer requires it. [date] [owner]
- [ ] Two reference customers who have agreed to take a call. [date] [owner]

## Common mistakes

- Starting the packet after the buyer asks. Timelines stretch in review, and an empty folder adds weeks.
- Answering a questionnaire with what you plan to build. Reviewers verify, and a wrong answer in a signed document is a contract problem.
- Sending an accessibility report that claims full support for every criterion. Reviewers read an untested report as no report.
- Letting documents go stale. A report dated two versions ago invites a full re-review.
- Leaving out AI subprocessors. Buyers now ask where student data goes when the product calls a model.

## Related guides

- [Vendor review readiness](../selling/vendor-review-readiness.md)
- [K-12 regulation](../market/k12-regulatory.md)
- [AI risk and trust](../product/ai-risk-and-trust.md)
- [Interoperability](../product/interoperability.md)
- [Procurement guide](../selling/procurement-guide.md)
- [All templates](README.md)

---
*Facts checked 2026-11-11 against the linked sources, with an independent spot-check the same day. The list itself is ScaleU's view; each buyer sets its own requirements.*

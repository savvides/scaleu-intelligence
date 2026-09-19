# K-12 Regulatory Landscape

## FERPA (Family Educational Rights and Privacy Act)

**What it is:** Federal law that protects the privacy of student education records. Applies to all schools that receive federal funding (virtually all public K-12 schools).

**What it means for edtech founders:**
- You cannot access personally identifiable information (PII) from student records without written parental consent OR a qualifying exception
- The "school official" exception is the most common path: the school designates your company as a school official with a legitimate educational interest
- This requires a contract or agreement specifying the data you'll access, why, and how you'll protect it
- You must return or destroy data when the contract ends

**Common mistakes:**
- Assuming parental consent is always required (the school official exception often applies)
- Not having a clear data governance agreement before accessing any student data
- Storing student data longer than necessary
- Using student data for advertising or non-educational purposes (this violates FERPA)

## COPPA (Children's Online Privacy Protection Act)

**What it is:** Federal law that governs the collection of personal information from children under 13. Enforced by the FTC.

**What it means for edtech founders:**
- If your product is directed at children under 13 OR you have actual knowledge that users are under 13, COPPA applies
- You must obtain verifiable parental consent before collecting personal information
- Schools can consent on behalf of parents for educational purposes (but only for educational use of the data)
- You must post a clear privacy policy describing your data practices
- You must provide parents access to their child's data and the ability to delete it

**The school consent mechanism:**
- Schools can provide consent on behalf of parents when the data is used solely for an educational purpose
- This does NOT extend to commercial use of the data
- You should still have a direct notice to parents about your data practices

**Common mistakes:**
- Collecting more data than necessary from children
- Using behavioral advertising in products directed at children
- Not having age-gating or age verification mechanisms
- Assuming "educational purpose" covers any feature you want to build

## State Student Privacy Laws

**The patchwork problem:** Over 40 states have enacted their own student data privacy laws, many stricter than FERPA. Key states to know:

**California (SOPIPA):**
- Cannot use student data for non-educational purposes
- Cannot sell student data
- Cannot use student data for targeted advertising
- Must delete data when no longer needed for educational purposes
- Must maintain reasonable security

**New York (Education Law 2-d):**
- Requires a Data Privacy and Security Plan
- Parents have the right to file complaints
- Schools must publish contracts with edtech vendors
- Specific data security standards

**Colorado (Student Data Transparency and Security Act):**
- Requires data inventory
- Prohibits use of student data for targeted advertising
- Requires breach notification

**Illinois (SOPPA):**
- Requires agreements between schools and vendors before data sharing
- Annual data review requirements
- Specific breach notification requirements

**Practical guidance:** If you sell to K-12 nationally, you need to comply with the strictest state requirements. This effectively means California and New York standards are your baseline.

## Student Data Privacy Consortium (SDPC)

**What it is:** A collaborative of schools, districts, and states that standardized student data privacy agreements.

**Why it matters for founders:**
- Many districts will ask you to sign the National Data Privacy Agreement (NDPA)
- Having a pre-signed NDPA with a state significantly accelerates procurement
- The NDPA covers FERPA, COPPA, and state-specific requirements in one agreement
- Check studentprivacycompass.org for participating states and districts

**Practical guidance:** Get familiar with the NDPA template early. If you can sign it without modifications, you remove a major procurement blocker.

## Accessibility Requirements

**Section 504 & ADA:** Schools must provide equal access to education for students with disabilities. Your product must be accessible.

**WCAG 2.1 AA:** The de facto standard for digital accessibility in education. Many districts require WCAG 2.1 AA compliance as a procurement requirement.

**Voluntary Product Accessibility Template (VPAT):** Many districts and states require a completed VPAT as part of the procurement process. This documents your product's accessibility conformance.

## Practical Checklist for K-12 Edtech Founders

1. [ ] Privacy policy that addresses FERPA, COPPA, and state laws
2. [ ] Data governance agreement template ready for districts
3. [ ] NDPA familiarity (can you sign the standard agreement?)
4. [ ] Data minimization: only collect what you need for educational purposes
5. [ ] Data retention and deletion policy documented
6. [ ] No advertising or commercial use of student data
7. [ ] Breach notification procedures in place
8. [ ] VPAT or accessibility conformance documentation
9. [ ] Age-gating or age verification if product serves under-13 users
10. [ ] Security practices documented (encryption, access controls, etc.)

---
*Last updated: 2026-03-31. US-focused. International regulations (GDPR, etc.) covered separately.*

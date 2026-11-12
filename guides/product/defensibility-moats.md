# Defensibility: what survives when an LLM can copy your features

Assume a buyer's own IT team can rebuild most software features with a current model in about two weeks. Your product is defensible only if its core value sits outside the model: in data, integration, a network, or approvals that a new entrant cannot reproduce.

**Applies to:** higher ed first, since the framework comes from a talk on selling to colleges and universities and the examples are drawn from them. The logic carries to K-12 districts and corporate L&D. United States.

This is a practitioner framework, not a research finding. Its timelines, the two-week sprint included, are estimates and were never measured.

*Source: "Cracking Higher Ed: Why Startups Miss the Mark" — Philippos Savvides, SXSW EDU 2026. Licensed CC BY 4.0.*

This guide is the maintained home of the moat framework. The [original SXSW EDU version](../../sources/events/2026-sxsw-edu/README.md#5-build-the-moat-that-ai-cant-replicate) keeps its presentation context. Where the two differ, follow this guide: it corrects the original's description of regulated access as "FERPA, HIPAA, or credentialing compliance."

## The AI-substitution durability test

Ask one question of your product:

> **Does this product survive an LLM plus a competent IT team's roughly two-week prompt-engineering sprint?**

Picture a district CTO or a university IT team with a current model and two weeks. If they can rebuild your core value, you have a feature, and your exposure is high whatever your pitch says.

The sprint fails against a real moat. The team can reproduce your interface and your prompts. It cannot reproduce your longitudinal dataset, your write-back already wired into the registrar's workflow, your roster of employers and mentors, or the approvals you already hold. Those live outside the model, so a better model does not help the attacker.

Buyers run this test on you. The [pilot playbook](../selling/edtech-pilot-playbook/README.md) gives it to institutions as the moat durability test, with the same question and the same four moats in one-line form. Its summaries are looser than the definitions below; where the wording differs, this page governs.

## The exposure spectrum

Place your product on this spectrum before you plan anything else.

| Exposure | What it looks like | Timeline |
|----------|--------------------|----------|
| High | Content generation, summarization, Q&A, template output | Replicable in 12 to 18 months |
| Moderate | AI embedded in a workflow or dataset with switching costs | Replicable in 2 to 4 years |
| Low | A structural moat that AI substitution cannot dissolve | Defensible for 3 years or more |

The timelines are the SXSW framework's practitioner estimates, and the bands overlap. Use them to rank your exposure, not to forecast. They estimate how long until substitutes crowd the market. The two-week sprint asks a different question: whether one buyer's IT team could rebuild your core value today.

**High** exposure sets a clock. An essay-feedback tool, a study-guide generator, and a syllabus Q&A bot all sit here. The framework estimates that pure software without structural defensibility faces substitution within 18 months. The labs themselves now give away general-purpose versions of several of these; see [what the labs already sell to schools](ai-native-framework.md#what-the-labs-already-sell-to-schools).

**Moderate** exposure means you have earned time. The AI is wired into a faculty grading workflow, or sits on a dataset the institution has come to rely on. In the framework's estimate, those switching costs buy 2 to 4 years.

**Low** exposure means your value lies outside the AI. You have created a dependency inside the institution that a new model cannot reproduce.

## "AI-powered" is not a moat

The label describes a layer of features, the part of a product most exposed to substitution. If your edge is "we use AI to generate feedback" or "we summarize student work," a competent IT team can stand up something close enough.

Building on the best model does not change this. When the model improves, it improves for your competitors at the same rate. Being [AI-native](ai-native-framework.md) describes how a product is built and says nothing about whether it can be copied.

## The four moats

Each of the four lives outside the model, so an LLM cannot manufacture it.

### 1. Proprietary data network

Longitudinal data that improves with use and that a new entrant cannot reconstruct.

A competitor can buy the model you use. It cannot buy three years of student-outcome data in which each cohort's results sharpen the next prediction. The value compounds, and a newcomer starts at zero however good its prompts are. A memory feature or a feedback loop is the mechanism that gathers such data; [architecture that compounds](ai-native-framework.md#architecture-that-compounds) covers how to build one.

*Example:* An advising platform has tracked which course sequences led to graduation and which to withdrawal, across several cohorts at one university. That record of what happened to real students there gives its recommendations their value. Nobody else holds it, and nobody can backfill it.

### 2. Deep integration

LTI and SIS write-back that makes switching cost more than the product does.

When your product writes grades into the SIS, syncs rosters through LTI, and sits inside the registrar's daily work, removing it costs the institution more than the contract is worth. That is the test: switching cost must exceed price. An LLM can copy your features. It cannot copy a write-back already wired into the system of record that the registrar and the provost depend on. See [interoperability](interoperability.md) for the standards involved.

*Example:* A degree-planning tool writes approved course plans into the SIS and feeds the official degree audit. A rival might generate a better plan in isolation, but to switch, the university would have to rebuild the integration, test it, and retrain staff.

### 3. Supply-side network effects

Each added provider, mentor, or contributor raises quality for every existing user.

A new entrant with an identical model still has an empty network. It can copy your software in two weeks and still have nobody on the other side.

*Example:* A career-transition platform connects graduates to employers. Each added employer makes the platform more useful to every student, and each placement makes it more attractive to the next employer. A competitor can copy the matching interface but not the employers and mentors who have shown up. The SXSW framework calls this phase, Graduate & Beyond, the least researched and least served stretch of the learner lifecycle. The scarce asset there is the employer relationship.

### 4. Regulated access

Student-privacy, security, and credentialing approvals that a thin LLM wrapper has not earned.

Before a product touches student records, an institution wants a signed data-privacy agreement, a completed security review (in higher ed often EDUCAUSE's [HECVAT](https://www.educause.edu/hecvat) questionnaire, sometimes with a SOC 2 report), and an accessibility review. Each takes time, process, and a track record. The institution's own approval chain of IT security, legal, procurement, and accessibility becomes your moat, because a competitor with better AI must still pass through every step. [Vendor review readiness](../selling/vendor-review-readiness.md) covers the paperwork.

Be exact about what this buys you:

- **No federal FERPA certification exists.** A training presentation by the Department of Education's Student Privacy Policy Office, [hosted by NEACRAO](https://neacrao.memberclicks.net/assets/docs/Programs/NEACRAO%20Vetting%20EdTech.pdf) and marked as not official guidance, lists an "Official Department of Education FERPA seal of approval" among things that do not exist. FERPA obligations sit with the institution, which passes them to you by contract.
- **FERPA covers colleges as well as schools.** At a college the rights belong to the student, [not the parents](https://studentprivacy.ed.gov/faq/what-ferpa). For FERPA, COPPA, and state privacy laws as they apply to schools, see [K-12 regulation](../market/k12-regulatory.md).
- **HIPAA rarely applies.** The HIPAA Privacy Rule excludes student health records that FERPA already covers as education records ([ED–HHS joint guidance](https://studentprivacy.ed.gov/resources/joint-guidance-application-ferpa-and-hipaa-student-health-records), updated December 2019).
- **The paperwork is a head start, not a wall.** A funded competitor can complete a HECVAT or commission a SOC 2 audit in months. The durable part is the approvals already granted at each institution and the integrations built on them.

*Example:* A student-data analytics product holds a signed data-privacy agreement, a reviewed HECVAT, and IT approval at an institution before any system touches student records. A wrapper that would ingest the same data without clearing those gates cannot be deployed there, however good its output.

## Pitch the dependency

Founders lead with "AI-powered" because the AI is what they built and what feels new. Every product now makes that claim, and it names the part most exposed to substitution. Lead with the dependency you create: the data only you hold, the write-back the registrar relies on, the network nobody else has filled, the approvals you have already cleared. Tell the buyer what it would cost to operate without you.

The same assets matter at exit. ScaleU's view is that an acquirer can build or buy features, so what it pays for is what it cannot: the data, the installed integrations, and the contracts. See [exits and acquirers](../business/exits-and-acquirers.md).

## Related guides

- [AI-native or bolted-on](ai-native-framework.md)
- [AI risk and trust](ai-risk-and-trust.md)
- [Pilot playbook](../selling/edtech-pilot-playbook/README.md)
- [Interoperability](interoperability.md)
- [Vendor review readiness](../selling/vendor-review-readiness.md)
- [Exits and acquirers](../business/exits-and-acquirers.md)

---
*Facts checked 2026-10-30 against the linked sources (the regulated-access facts on FERPA, HIPAA, and HECVAT). An independent review on 2026-11-11 reread the NEACRAO presentation and the FERPA page and edited for style; it could not open the HECVAT page or the text of the ED–HHS guidance. The exposure timelines and the two-week sprint are the framework's estimates and were never measured.*

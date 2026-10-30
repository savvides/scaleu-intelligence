# Defensibility Moats: Staying Alive When LLMs Can Copy Your Features

How an edtech product stays defensible when a competitor, or the buyer's own IT team, can rebuild its features with an LLM in a couple of weeks. Use it when you need to know whether your core value survives substitution or evaporates with the next model release, and before you pitch "AI-powered" as your advantage.

**Audience.** The framework comes from a talk about selling to higher education, and the examples are colleges and universities. The same logic applies to K–12 districts and corporate L&D; for K–12 privacy rules, see [K–12 regulation](../market/k12-regulatory.md).

**Evidence type.** This is a practitioner framework, not a research finding. The timelines are the framework's estimates, not measured rates.

*Source: "Cracking Higher Ed: Why Startups Miss the Mark" — Philippos Savvides, SXSW EDU 2026. Licensed CC BY 4.0.*

This guide is the maintained home for the moat framework; the [original SXSW EDU version](../../sources/events/2026-sxsw-edu/README.md#5-build-the-moat-that-ai-cant-replicate) keeps its presentation context. Where they differ, follow this guide: it corrects the original's description of regulated access as "FERPA, HIPAA, or credentialing compliance." For the architecture side of the question — compounding memory, the data flywheel, and AI-native pricing — read [ai-native-framework.md](ai-native-framework.md). The two are companions: that file asks whether your product is genuinely AI-native; this one asks whether anything stops a competitor from rebuilding it.

## "AI-powered" is not a moat

It's a feature layer, exposed to the same substitution risk it claims to solve. The SXSW framework estimates that pure software without structural defensibility faces substitution risk within 18 months. If your edge is "we use AI to generate feedback" or "we summarize student work," a competent district CTO or college IT team with an LLM and a couple of weeks can put up something close enough.

Riding the model curve doesn't change that. When the underlying model improves, it improves for your competitors at the same rate. Being AI-native, in the sense of [ai-native-framework.md](ai-native-framework.md), describes how your product is built; it is not a moat on its own.

So the question isn't whether your product uses AI. It's whether your core value survives replication. Two things make that true: knowing how exposed you are, and building one of the moats that doesn't dissolve when the model improves.

## The exposure spectrum

Locate your product on this spectrum first. It tells you how much time you actually have.

| Exposure | What it looks like | Timeline |
|----------|--------------------|----------|
| **High** | Content generation, summarization, Q&A, template output | Replicable in 12-18 months |
| **Moderate** | AI embedded in a workflow or dataset with switching costs | Replicable in 2-4 years |
| **Low** | A structural moat that AI substitution cannot dissolve | Defensible for 3+ years |

The timelines are the SXSW framework's practitioner estimates, and the bands overlap. Use them to rank your exposure, not as a forecast. They measure how long until substitutes crowd the market. The two-week sprint in the [durability test](#the-ai-substitution-durability-test) below asks a different question: could one buyer's IT team rebuild your core value today?

High exposure isn't a death sentence, but it sets a clock. An AI essay-feedback tool, a study-guide generator, a syllabus-to-Q&A bot — these sit at High. The model that powers them gets better for your competitors at the same rate it gets better for you, and nothing stops a new entrant from starting fresh next quarter.

Moderate means you've earned some time. The AI is wired into a faculty grading workflow or sits on top of a dataset the institution has come to rely on. In the framework's estimate, switching costs buy you 2-4 years.

Low means the thing that makes you valuable isn't the AI at all. It's a dependency you've created inside the institution that a new model can't reproduce.

## The four moats

Four structural moats move you down the spectrum toward defensibility. Each one is something an LLM cannot manufacture, because each one lives outside the model.

### 1. Proprietary data network

Longitudinal data that improves with usage and cannot be reconstructed by a new entrant.

A competitor can buy the same model you use. They cannot buy the three years of student-outcome data you've accumulated, where each cohort's results sharpen your next prediction. The value compounds with usage, and a new entrant starts from zero no matter how good their prompts are.

*Edtech example:* An advising platform that has tracked which course sequences led to graduation versus withdrawal across multiple cohorts at a university. The recommendation engine isn't valuable because of the model behind it. It's valuable because of the longitudinal record of what actually happened to real students at that institution — a record nobody else has and nobody can backfill.

### 2. Deep integration

LTI/SIS write-back that creates operational switching costs exceeding the product's price.

When your product writes grades back into the SIS, syncs rosters through LTI, and lives inside the registrar's daily workflow, ripping it out costs the institution more than the contract is worth. That's the test: switching cost has to exceed price. An LLM can copy your features. It can't copy the fact that your write-back is already wired into the system of record that the registrar and the provost depend on.

*Edtech example:* A degree-planning tool that writes approved course plans back into the SIS and feeds the institution's official degree audit. A competitor's LLM might generate a better plan in isolation, but the university would have to re-integrate, re-test, and re-train staff to switch. The integration is the moat, not the planning logic.

### 3. Supply-side network effects

More providers, mentors, or contributors increase quality for every existing user.

Each new participant on the supply side makes the product more valuable for everyone already on it. A new entrant with an identical model still has an empty network. They can replicate your software in two weeks and still have nobody on the other side of it.

*Edtech example:* A career-transition platform connecting graduates to employers. Every additional employer relationship makes the platform more useful to every student, and every successful placement makes the platform more attractive to the next employer. A competitor can copy the matching interface but not the roster of employers and mentors who have shown up. (This is the Graduate & Beyond phase, which the SXSW framework calls the least researched and least served stretch of the learner lifecycle. Employer relationships are the scarce asset there, not the software.)

### 4. Regulated access

Student-privacy, security, and credentialing approvals that a thin LLM wrapper hasn't earned.

Compliance is a barrier to entry that no prompt clears. Before a product touches student records, the institution wants a signed data-privacy agreement, a completed security review (in higher ed, often EDUCAUSE's [HECVAT](https://www.educause.edu/hecvat) questionnaire, sometimes with a SOC 2 report), and an accessibility review. Each takes time, process, and a track record. The institution's own approval chain becomes your moat: IT security, legal, procurement, accessibility review. A competitor with better AI still has to walk through every one of those doors.

Be precise about what this buys you. There is no federal FERPA certification to hold. A training presentation by the Department of Education's Student Privacy Policy Office, [hosted by NEACRAO](https://neacrao.memberclicks.net/assets/docs/Programs/NEACRAO%20Vetting%20EdTech.pdf) and marked as not official guidance, lists an "Official Department of Education FERPA seal of approval" among things that don't exist. FERPA obligations sit with the institution, which passes them to you through contract terms. FERPA applies to colleges as well as schools; at a college, the rights belong to the student, [not the parents](https://studentprivacy.ed.gov/faq/what-ferpa). See [K–12 regulation](../market/k12-regulatory.md) for FERPA, COPPA, and state privacy laws as they apply to schools. HIPAA rarely applies: the HIPAA Privacy Rule excludes student health records that FERPA already covers as education records ([ED–HHS joint guidance](https://studentprivacy.ed.gov/resources/joint-guidance-application-ferpa-and-hipaa-student-health-records), updated December 2019). And a funded competitor can complete a HECVAT or commission a SOC 2 audit in months. The paperwork is a head start, not a wall. The durable part is the approvals already granted at each institution and the integrations built on top of them.

*Edtech example:* A student-data analytics product that has a signed data-privacy agreement, a reviewed HECVAT, and IT approval at the institution before any system touches student records. An LLM wrapper that ingests the same data without clearing those gates can't be deployed there, regardless of how good its output is. The regulated access is the moat — the model is interchangeable.

## The AI-substitution durability test

One practical lens for the AI era. Run your product through it:

> **Does this product survive an LLM plus a competent IT team's roughly two-week prompt-engineering sprint?**

Imagine a district CTO or a university IT team sits down with a current model and two weeks. If they can rebuild your core value, you don't have a moat — you have a feature, and you're on the High end of the exposure spectrum whether you admit it or not.

If your value comes from one of the four moats, the sprint fails. The team can reproduce your interface and your prompts. They cannot reproduce your longitudinal dataset, your SIS write-back already wired into the registrar's workflow, your network of employers and mentors, or the privacy and security approvals you already hold. Those live outside the model, so a better model doesn't help the attacker.

Apply it honestly. The point of the test is to find out which side of the line you're on before a competitor does.

## The reframe

Lead with the institutional dependency you create, not the technology you use.

Founders pitch the model. They lead with "AI-powered" because it's what they built and what feels new. But "AI-powered" is what every product claims now, and it's the part most exposed to substitution. The durable story is the dependency: the data only you hold, the write-back the registrar relies on, the network nobody else has filled, the compliance gates you've already cleared.

When you talk to a buyer, don't sell the reasoning engine. Sell what it would cost them to live without you. That's the moat. The AI is just how you got there.

---
*Last updated: 2026-10-30. Regulated-access facts (FERPA, HIPAA, HECVAT) rechecked against the linked sources on that date. The exposure timelines are the framework's estimates and were not re-measured.*

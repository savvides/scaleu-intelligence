# AI-native or bolted-on: how central AI should be

Decide whether AI is the engine of your product or a feature on it, then price, pitch, and build accordingly. Either answer can make a good company; the costly mistake is telling buyers and investors one while building the other.

**Applies to:** K-12, higher ed, and workforce products sold in the United States. The pricing advice addresses institutional buyers.

This page is ScaleU's practitioner framework, not a research finding. Figures marked as illustrations or rules of thumb are judgment. Vendor terms and prices in the model section were read on the vendors' pages on November 11, 2026, and will change. Two companion guides cover what this one leaves out: [defensibility](defensibility-moats.md) asks what stops a competitor from copying you, and [AI risk and trust](ai-risk-and-trust.md) asks what a student-facing model does to learners.

## The removal test

Remove every AI component from your product. Ask whether it still solves the customer's problem.

| Answer | What you have | How you compete |
|---|---|---|
| Yes | A conventional edtech product with AI features | Distribution and evidence |
| No | An AI-native product | Output quality, plus one of the structural [moats](defensibility-moats.md), because your competitors can buy the same models |

## Four marks of an AI-native product

1. **Cost scales with usage.** Your cost of goods sold rises with tokens consumed, not seats sold. A student who uses the product ten times as much costs you ten times the compute, so your price should capture more of the value that student receives.
2. **Better models make the product better.** When a new frontier model ships, you swap it in, rerun your evaluations, and the product improves with little other engineering. Test before you switch, because a new model can regress on your task. The same improvement reaches your competitors, so this mark makes you AI-native, not [defensible](defensibility-moats.md).
3. **The AI is load-bearing.** Take the model out and the product stops working.
4. **Users work differently.** They do the job in a new way, and the old way starts to feel obsolete. Working faster in the old way does not count.

## Five signs the AI is bolted on

1. **A button on the side.** AI appears as a discrete "summarize" or "rewrite" action outside the core workflow.
2. **A chat sidebar.** A chatbot answers questions about the product. Delete it and the product still solves the problem.
3. **No memory.** Every session starts from zero, with no record of the user's history, preferences, or learning patterns.
4. **Novelty drop-off.** Users try the feature once and return to the old way. A common pattern, offered as a rule of thumb and not a measured benchmark: usage peaks in week 1 and is gone by week 3.
5. **No gain from better models.** The product wraps a fixed API call, so a stronger model changes nothing.

## When bolted-on is the right call

Do not force AI into a job that does not need it. Keep it a feature when:

- the core problem is structural (procurement, scheduling, payments) and needs no reasoning engine;
- AI only speeds up a mature product; or
- your buyers distrust algorithms they cannot inspect.

Bolted-on products win through sales and distribution. AI-native products win through better results and lower cost at scale.

## Architecture that compounds

**Memory.** A product that remembers improves with use. A tutor that adapts to one student's sticking points across a semester is the plain example, and it raises the cost of switching. One student's history is not a moat, since a competitor can build the same feature. It becomes one when records across many students and cohorts form a [proprietary data network](defensibility-moats.md#1-proprietary-data-network) that a new entrant cannot reconstruct. Memory also means you hold student data over time, which buyers will examine; see [what institutional buyers will ask](ai-risk-and-trust.md#what-institutional-buyers-will-ask). The tutor here illustrates an architecture; it is not a recommendation to build one. Several summit speakers quoted in the risk guide argue for aiming AI at the teacher until outcome data says otherwise. If you build a student-facing tutor, plan for the friction and evidence questions it raises.

**Feedback loops.** Each interaction should improve the system. When a teacher corrects a generated lesson plan, the correction should shape the next one. Without that loop you have an API bill and nothing accumulating. The loop becomes a moat only when the data it produces cannot be rebuilt by someone else.

**Model independence.** Build so you can change providers as the lead changes. Your value should sit in your data and your orchestration of the models, not in access to any one of them.

## Model choices and costs in late 2026

### Three ways to get a model

The table is ScaleU's view of the trade-offs, not vendor data.

| Route | Choose it when | What it costs you |
|---|---|---|
| Frontier API (OpenAI, Anthropic, Google) | You are still finding the product, or quality on hard reasoning decides the sale | Per-token fees, a dependency on the lab's terms, and a subprocessor every district will ask about |
| Open-weight model you host (for example Google's [Gemma](https://deepmind.google/models/gemma) family, which runs on anything from cloud servers to laptops) | A buyer requires that student data stay in your environment, or volume is high and the task is narrow | Engineering and hosting you now own, and usually weaker performance on the hardest tasks |
| Fine-tuning, on either | You have thousands of graded examples of a narrow task and a smaller model must match a larger one on it | The labeled data, an evaluation suite, and retraining whenever the base model changes |

Start on a frontier API with a model-independent design. Move a workload to a smaller or self-hosted model only after your evaluations show it holds quality. Fine-tune last. Most early teams that fine-tune are compensating for missing evaluations and prompts.

Model size is the main cost lever. On November 11, 2026, [OpenAI's price list](https://developers.openai.com/api/docs/pricing) showed its current flagship family running from $0.10 per million input tokens and $0.50 per million output tokens for the smallest model to $10 and $50 for the largest: a hundredfold spread. Route each task to the cheapest model that passes your evaluation, and recheck prices before you set your own.

### Data terms education buyers will ask about

Districts and universities ask whether student data trains a model, how long the provider keeps it, and whether minors may use the product at all. The answers differ by lab.

| Provider | Training on API data | Retention | Minors |
|---|---|---|---|
| OpenAI API | Not used to train unless you opt in ([data controls](https://developers.openai.com/api/docs/guides/your-data)) | Abuse-monitoring logs kept up to 30 days; zero data retention requires OpenAI's approval | [Under-18 guidance](https://developers.openai.com/api/docs/guides/safety-checks/under-18-api-guidance) requires added safeguards and legal compliance. Do not process personal data of children under 13 without zero data retention in place |
| Anthropic API | Commercial inputs and outputs not used to train by default; feedback you submit is the exception ([policy](https://privacy.claude.com/en/articles/7996868-is-my-data-used-for-model-training), updated August 18, 2026) | [Zero data retention](https://privacy.claude.com/en/articles/8956058-i-have-a-zero-data-retention-agreement-with-anthropic-what-products-does-it-apply-to) by arrangement, subject to Anthropic's approval | [Guidance for organizations serving minors](https://support.claude.com/en/articles/9307344-responsible-use-of-anthropic-s-models-guidelines-for-organizations-serving-minors) (March 16, 2026) expects added safety measures, compliance with laws such as COPPA, and disclosure that the user is talking to an AI |
| Google Gemini API | Paid tier: prompts and responses not used to improve products. Unpaid tier: content is used, and human reviewers may read it ([terms](https://aistudio.google.com/docs/terms), effective March 23, 2026) | Paid tier logs prompts and responses for a limited period | The same terms bar using the service in an application directed to, or likely to be accessed by, people under 18 |

Three consequences follow. Never run student data through an unpaid tier. If children under 13 will use the product, settle zero data retention with the provider before the first pilot, since approval is not automatic. And read the age clause before you choose a provider for a K-12 student-facing product: the Gemini API terms above exclude that use. Google Cloud sells its models under separate terms that this page did not check. For the laws behind these questions, see [K-12 regulation](../market/k12-regulatory.md).

### What the labs already sell to schools

| Product | What it is | Price and terms as published |
|---|---|---|
| ChatGPT study mode and ChatGPT Edu (OpenAI) | Study mode asks questions and withholds direct answers until the student engages. It launched July 29, 2025, on the Free, Plus, Pro, and Team plans, with ChatGPT Edu, the plan institutions buy, to follow ([TechCrunch](https://techcrunch.com/2025/07/29/openai-launches-study-mode-in-chatgpt/)) | Study mode is in the free plan |
| ChatGPT for Teachers (OpenAI) | A workspace for teachers, developed with a cohort of school districts and announced November 19, 2025 ([THE Journal](https://thejournal.com/articles/2025/11/19/openai-unveils-chatgpt-for-teachers.aspx)) | Free through June 2027; workspace data not used for training by default |
| [Gemini for Education](https://edu.google.com/intl/ALL_us/ai/gemini-for-education/) (Google) | The Gemini app for schools, open to all ages with added guardrails under 18 | No cost in every Google Workspace for Education edition; Google states the data is not human-reviewed or used to train models. A paid add-on is listed at $20 per user per month on an annual commitment |
| [Claude for Education](https://www.anthropic.com/news/introducing-claude-for-education) (Anthropic) | A version of Claude for higher education institutions, announced April 2, 2025. Its learning mode guides a student's reasoning instead of giving answers | Institutional agreements |
| [Khanmigo](https://www.khanmigo.ai/pricing) (Khan Academy) | AI tutor and teaching assistant | Free for teachers; $4 per month or $44 per year for learners and parents; district pricing on request |

OpenAI's own product pages refused automated access on the check date, so the two OpenAI rows cite press coverage.

ScaleU's view: the price of a general-purpose chat tutor and of a lesson-plan generator is now zero, and the seller is a company your buyer already has a contract with. A startup should not sell either. Sell what the labs leave undone: write-back into the district's systems of record, alignment to the adopted curriculum, the controls and reporting a district needs, compliance for the youngest students, and evidence of learning from your own deployments. Those are the moats in [defensibility](defensibility-moats.md), and the [competitive landscape](../market/competitive-landscape.md) tracks who else is selling.

## Pricing an AI product

[Business models and pricing](../business/business-models-and-pricing.md) covers pricing in general. Two points are specific to AI.

**Flat per-seat pricing can lose money on your best customers.** To illustrate with hypothetical numbers: a power user who consumes $50 of tokens on a $10-per-month seat costs you $40 a month. Pricing by token, session, or outcome keeps revenue in step with cost. Model the margin per active user in [unit economics](../business/unit-economics.md) before you quote a price.

**Institutions need a fixed line item.** K-12 and higher ed [procurement](../selling/procurement-guide.md) is built around a predictable annual budget, and pure usage pricing fits it badly. ScaleU's view: sell a hybrid. An annual base subscription gets the contract through procurement, and a block of usage credits for the AI features protects your margin. The buyer gets predictability and you get a cap on what any one account can cost you.

## Related guides

- [Defensibility](defensibility-moats.md)
- [AI risk and trust](ai-risk-and-trust.md)
- [Business models and pricing](../business/business-models-and-pricing.md)
- [Unit economics](../business/unit-economics.md)
- [Competitive landscape](../market/competitive-landscape.md)
- [K-12 regulation](../market/k12-regulatory.md)

---
*Facts last checked: 2026-04-27 (framework text; figures in it are illustrations or rules of thumb and were never measured). Rewritten for clarity 2026-11-11; the model, data-terms, and lab-product facts in "Model choices and costs in late 2026" were added and checked that day against the linked pages. Nothing else was rechecked.*

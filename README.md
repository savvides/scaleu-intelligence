# ScaleU Intelligence

A working library for edtech founders: how education buyers decide, how to sell and pilot, what counts as evidence, what learning research supports, and how to price, fund, and defend the company.

Philippos Savvides, who runs [ASU ScaleU](https://scaleu.org), Arizona State University's edtech accelerator, maintains the library. The guides draw on accelerator work, conferences, published research, statutes, and official data, and they say which is which.

[Start here](guides/start-here.md) · [All guides](guides/README.md) · [Download a release](https://github.com/savvides/scaleu-intelligence/releases/latest) · [What's changed](CHANGELOG.md) · [Get help](.github/SUPPORT.md)

## Start with your decision

| You are deciding | Start here | Go deeper |
|---|---|---|
| Whether the problem is worth solving | [Demand validation](guides/demand/demand-validation.md) | [Buyer interviews](guides/demand/jtbd-interviews.md) · [Founder traps](guides/demand/founder-traps.md) · [Higher-ed jobs atlas](guides/demand/higher-ed-jobs-atlas.md) |
| Whom to sell to, and how | [Go-to-market](guides/selling/go-to-market.md) | [Buyer personas](guides/demand/buyer-personas.md) · [Procurement](guides/selling/procurement-guide.md) · [Demand signals](guides/demand/buyer-demand-signals.md) |
| How to run a pilot that ends in a purchase | [EdTech pilot playbook](guides/selling/edtech-pilot-playbook/README.md) | [Pilot benchmarks](guides/selling/pilot-benchmarks.md) · [Pilot agreement outline](guides/templates/pilot-agreement.md) |
| How to pass security, privacy, and accessibility review | [Vendor review readiness](guides/selling/vendor-review-readiness.md) | [K-12 regulation](guides/market/k12-regulatory.md) · [Interoperability](guides/product/interoperability.md) |
| What evidence you need | [Evidence tiers](guides/evidence/evidence-tiers.md) | [Evidence roadmap](guides/evidence/evidence-roadmap.md) · [Logic model template](guides/templates/logic-model.md) |
| What to build so that people learn | [Learning science](guides/product/learning-science.md) | [Research collections](sources/research/README.md) |
| What AI should do in the product | [AI-native framework](guides/product/ai-native-framework.md) | [AI risk and trust](guides/product/ai-risk-and-trust.md) · [Defensibility](guides/product/defensibility-moats.md) |
| How to charge and what the numbers must show | [Business models and pricing](guides/business/business-models-and-pricing.md) | [Unit economics](guides/business/unit-economics.md) |
| Whether and how to raise money | [Fundraising](guides/business/fundraising.md) | [Funding landscape](guides/market/funding-landscape.md) · [Exits and acquirers](guides/business/exits-and-acquirers.md) |
| Which market to enter | [K-12](guides/market/k12-landscape.md) · [Higher ed](guides/market/highered-landscape.md) · [Workforce](guides/market/corporate-ld.md) · [Consumer](guides/market/consumer-learning.md) | [International](guides/market/international-markets.md) · [Market data](guides/market/market-data-sources.md) · [Competitors](guides/market/competitive-landscape.md) |
| Where else to look | [Resources](guides/resources.md) | [Glossary](guides/glossary.md) · [Templates](guides/templates/README.md) |

## What's in the library

- **[Guides](guides/README.md):** answers to founder questions about demand, selling, evidence, product, business, and market, with a [roadmap by company stage](guides/start-here.md), a [glossary](guides/glossary.md), [templates](guides/templates/README.md), and a [directory of outside resources](guides/resources.md).
- **[Sources](sources/README.md):** the evidence underneath.
  - [Learning research](sources/research/README.md): 19 topic collections with paper citations and DOIs.
  - [Events](sources/events/README.md): ASU+GSV 2026 reports and transcripts, and the SXSW EDU 2026 higher-ed framework.
  - [Field notes](sources/notes/README.md): dated observations from meetings, reading, and other ScaleU work.
- **[About](LICENSE.md):** licenses and the [field-note template](about/templates/field-note.md).

## Use it with your AI assistant

Everything here is plain Markdown. You install nothing and run nothing.

```sh
git clone https://github.com/savvides/scaleu-intelligence.git
```

- **Point your assistant at [`guides/`](guides/README.md) first.** The guides answer founder questions and link to the evidence behind them. [`AGENTS.md`](AGENTS.md) tells an assistant how to read the library.
- **Let it follow links into [`sources/`](sources/README.md) for detail.** Sources are large; an assistant need not read them all.
- **Ask it to cite** the guide, the underlying source, and its date, and to keep evidence apart from interpretation.

## Read the evidence in context

The guides keep four kinds of evidence apart. Research summaries point to papers. Laws and official statistics link to the statute, regulation, or dataset. Conference transcripts record what speakers said; a speaker's claim about a product is not a verified result. The guides label practitioner estimates as estimates.

Each guide ends with the date its facts were last checked and what the check covered. Regulations, funding programs, and company status change. Confirm them at the linked primary source before you act. Nothing here is legal, financial, or investment advice.

## Cite and reuse

Use `main` for the latest edits or a [tagged release](https://github.com/savvides/scaleu-intelligence/releases) for a stable snapshot. Each release includes the complete library as ZIP and tar.gz downloads under **Assets**.

Cite the library with the version or commit you used:

> Savvides, P. (2026). *ScaleU Intelligence* (Version 3.0.0). https://github.com/savvides/scaleu-intelligence/releases/tag/v3.0.0

Cite individual authors, speakers, and original papers when you draw on their work; the library citation does not replace those credits. Reuse follows the [license for the relevant collection](LICENSE.md): this repository combines MIT and CC BY 4.0 material.

## Work with ScaleU

If you are building an edtech company and want an institutional pilot, [learn about ASU ScaleU and get in touch](https://scaleu.org). This library shares the questions and evidence behind that work.

## Keep it growing

To add a finding, a correction, or a useful source, follow the [contribution guide](.github/CONTRIBUTING.md). Contributors follow the [code of conduct](.github/CODE_OF_CONDUCT.md). For exposed private information or security concerns, use the [private reporting route](.github/SECURITY.md).

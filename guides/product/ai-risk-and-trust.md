# AI risk and trust for edtech founders

The controlled evidence so far points one way: unrestricted AI help raises performance while the tool is open and can lower it once the tool is gone, and tools built with pedagogical guardrails or aimed at the tutor or teacher do better. Design for unaided learning, measure it, and be ready for a buyer's questions about minors, data, and law.

**Applies to:** K-12, higher ed, and corporate L&D in the United States, with a note on the EU. Read each finding with its population in mind. Most of the developmental material concerns children and adolescents; the Gallup poll covers ages 14 to 29, the closest evidence here for a college or workforce product.

This page keeps four kinds of evidence apart. Research findings cite the paper. Laws and official actions cite the agency or statute. Speaker claims come from the ASU+GSV 2026 summit (April 12–15, 2026) and are not verified results. ScaleU's view is labeled where it appears.

*Source for the summit material: ASU+GSV 2026 Summit Intelligence — ScaleU. CC BY 4.0. Practitioner signals, not peer-reviewed research.*

## What the research shows

### The evidence base is thin

Lily Fesler, JP Martinez Claeys, Chris Agnew, and Susanna Loeb reviewed it in [*The Evidence Base on AI in K-12: A 2026 Review*](https://scale.stanford.edu/sites/default/files/The%20Evidence%20Base%20on%20AI%20in%20K-12%20Report.pdf) (AI Hub for Education, Stanford SCALE Initiative, 2026). They screened the more than 800 papers in their repository as of October 2025. Those papers cover AI in K-12 education, not only LLMs, and are mostly preprints. Twenty offered strong causal evidence. None was a high-quality causal study of US K-12 students; much of the work studies people over 18, outside the US, in short sessions. The authors report these findings and call them preliminary:

- AI tools improved students' performance on math practice, programming, and writing while students had access to them.
- When students were assessed without AI, the effects were mixed.
- Making work easier can come at the expense of deeper thinking.
- Tools with pedagogical guardrails showed more promise than general-purpose tools.
- Teachers who used AI for lesson planning spent less time without losing quality.
- Regular automated AI feedback to human tutors improved instructional quality and student outcomes, especially for less experienced and lower-rated tutors.

### The studies buyers cite

Effect directions are as the papers report them. Preprints have not been peer reviewed.

| Study | Who and what | Result |
|---|---|---|
| Bastani et al. (2025), *PNAS*, [doi:10.1073/pnas.2422633122](https://doi.org/10.1073/pnas.2422633122) | Randomized field experiment with nearly 1,000 high school math students in Turkey. Practice with a ChatGPT-style GPT-4 interface, with a GPT-4 tutor given teacher-designed guardrails, or with no AI; then an exam without AI | During practice, grades rose 48% with the plain interface and 127% with the guarded tutor. On the unaided exam, the plain-interface group scored 17% below students who never had AI. The guarded tutor largely removed that harm |
| Kestin et al. (2025), *Scientific Reports*, [doi:10.1038/s41598-025-97652-6](https://doi.org/10.1038/s41598-025-97652-6) | Randomized trial in Harvard's largest introductory physics course, fall 2023; 194 students analyzed. A custom AI tutor built on the course's own teaching practices, compared with in-class active learning | Students learned significantly more in less time with the AI tutor, and reported more engagement and motivation. One selective university, one course, two weeks |
| Wang et al. (2024), preprint, [doi:10.48550/arXiv.2410.03017](https://doi.org/10.48550/arXiv.2410.03017) | Preregistered randomized trial of Tutor CoPilot, which suggests responses to human tutors in real time; 900 tutors and 1,800 K-12 students in Title I schools | Students whose tutors had the tool were 4 percentage points more likely to master topics; 9 points for students of lower-rated tutors. The authors put the cost at $20 per tutor per year. Tutors noted that some suggestions were not grade-appropriate |
| LearnLM Team, Eedi, et al. (2025), preprint, [doi:10.48550/arXiv.2512.23633](https://doi.org/10.48550/arXiv.2512.23633) | Exploratory randomized trial; 165 students in five UK secondary schools. Expert tutors supervised and could revise every message a pedagogy-tuned model drafted | Students did at least as well as with human tutors alone on every outcome, and were 5.5 percentage points more likely to solve novel problems on later topics (66.2% against 60.7%). Tutors approved 76.4% of drafts with no or minimal edits |
| Fan et al. (2024), *British Journal of Educational Technology*, [doi:10.1111/bjet.13544](https://doi.org/10.1111/bjet.13544) | Randomized experiment; 117 university students on a writing task, supported by ChatGPT, a human expert, writing analytics, or nothing | The ChatGPT group improved its essay scores most, but knowledge gain and transfer did not differ significantly. The authors warn of "metacognitive laziness" |
| Liu, Christian, Dumbalska, Bakker, and Dubey (2026), preprint, ["AI Assistance Reduces Persistence and Hurts Independent Performance"](https://arxiv.org/abs/2604.04721) | Three randomized experiments; 1,222 US adults recruited online, not students in a course. Single sessions of about 13 to 15 minutes on fraction problems or SAT-style reading questions, with or without an AI assistant | Afterward, working without AI, the AI groups solved fewer problems than controls in all three experiments. They skipped more problems in two of the three; in the second experiment the difference was not statistically significant |
| Shaw and Nave (2026), preprint, [*Thinking—Fast, Slow, and Artificial*](https://papers.ssrn.com/abstract=6097646) | Three preregistered experiments (N = 1,372) on reasoning problems | Accuracy rose when the AI was right and fell when it was wrong. The authors name the pattern "cognitive surrender": adopting an AI's output with minimal scrutiny |
| Cheng et al. (2026), *Science*, ["Sycophantic AI decreases prosocial intentions and promotes dependence"](https://doi.org/10.1126/science.aec8352) | Eleven AI models; adults, not children | The models affirmed users' actions 49% more often than humans did |
| Contractor and Reyes (2026), preprint, [doi:10.48550/arXiv.2607.08849](https://doi.org/10.48550/arXiv.2607.08849) | Proctored, in-person randomized experiment; undergraduates studied an unfamiliar topic and wrote an essay with or without off-the-shelf AI, then took unaided tests immediately and a week later | AI access raised test scores, and a smaller gain persisted a week later. Gains held for students who used AI as a tutor and faded for those who had it write for them |

### What to take from it

ScaleU's view: three patterns recur across these studies, and none is settled.

1. Performance with the tool open tells you little. Bastani and Fan both found gains during the task that vanished or reversed when students worked alone. Measure learning without the tool.
2. Design decides the direction. The same model harmed unaided performance through a plain chat interface and did not through a guarded one. How students use it matters as much: tutoring use held up in Contractor and Reyes, and ghostwriting faded.
3. The strongest K-12 results so far put a human between the model and the student. Tutor CoPilot and the LearnLM trial both kept a tutor in the loop.

[Learning science](learning-science.md) covers the underlying research on practice, feedback, and effort. To produce outcome data of your own, see the [evidence roadmap](../evidence/evidence-roadmap.md).

## What speakers said at ASU+GSV 2026

The cognition question was the most contested theme of the week, and platform companies and practitioners were not in the same room on it. Everything in this section is a speaker claim or operator signal unless a source is linked. The summit transcripts are machine-generated and carry no speaker labels. Names follow each session's speaker list, the summit report, and context; where the speaker is unclear, this page credits the session.

### The 800-studies claim (speaker claim, checked)

Ben Riley (Cognitive Resonance) cited Stanford SCALE's review of 800 studies of LLMs in education and said only 20 showed causal impact, and virtually none of those were positive ([transcript](../../sources/events/2026-asu-gsv/transcripts/64-does-ai-expand-human-intelligence-or-atrophy-it.md)). The review, summarized above, bears out the count but not the direction: its findings are mixed, not negative.

Riley also said that, by OpenAI's own account, roughly 500 million students were already using one tool before any longitudinal data existed. The figure is his and was not checked. His framing is worth keeping even if you reject his conclusion. A founder who waits for the trials decides five years late. A founder who deploys without measuring becomes the data. Choose which error you will risk.

### Cognitive automation (speaker claim, checked)

Riley called the behavior "cognitive automation," a term he credited to François Chollet, in place of the gentler "cognitive offloading." He described Carnegie Mellon and UCLA work in which students who had grown used to AI gave up sooner when they later tried to learn without it, and said the researchers call this "cognitive surrender" (same transcript).

The study that matches his description is the Liu et al. preprint in the table; its first and last authors are at Carnegie Mellon and UCLA. Its participants were adults in single online sessions, not students in a course, and it does not use the term "cognitive surrender." That term comes from the separate preprint by Steven Shaw and Gideon Nave of the Wharton School, also in the table.

On another panel, a speaker said Sal Khan's chief learning officer had reported students typing "IDK" into Khanmigo instead of engaging with it ([transcript](../../sources/events/2026-asu-gsv/transcripts/80-is-ai-amplifying-cognition-or-dismantling-it.md)). The speakers feared more than students thinking less while using AI. They feared the capacity itself eroding.

### Students and chatbot tutors (operator signal)

Dan Meyer (Amplify) watches one benchmark: whether kids want to talk to a chatbot tutor. He said it has sat flat at roughly 5% for three years. His build rule follows: "not AI direct to student," but AI through the teacher, as an analytical layer. Joe Davis (KAIT Lab) is working toward the same end with AI-powered infrared pens that show where students get stuck inside a problem set, so that productive struggle stays central ([transcript](../../sources/events/2026-asu-gsv/transcripts/80-is-ai-amplifying-cognition-or-dismantling-it.md)).

### Killing the butterfly (operator signal)

Larry Berger (Amplify) said AI has remarkable capabilities, but the implementations he sees are "killing the butterfly": the moment of collective wonder that pollinates the next thousand moments of learning. His board gave him six months to step back from running the company and work out whether AI can keep the butterfly alive. A couple of months in, he said he had no answers yet. A serious operator with every incentive to be bullish is openly unsure ([transcript](../../sources/events/2026-asu-gsv/transcripts/63-learning-amplified-with-larry-berger-and-russlynn-ali.md)).

### Sycophancy and praise (speaker claim, source not found)

Isabelle Hau (Stanford Accelerator for Learning) shared a figure from one of her visiting scholars: AI models praise children 13 times more often than humans do. She did not name the study, and no published source for the figure was found as of 2026-10-30. The closest published work is the Cheng et al. study in the table, which concerns adults and is not the source of her figure. Her reading as a parent: a child praised 13 times more by a model than by a parent comes to expect it, and human relationships shift to match ([transcript](../../sources/events/2026-asu-gsv/transcripts/48-every-student-should-have-an-ai-learning-companion.md)).

The structural problem lies underneath. Companies are rewarded for engagement, and sycophancy reliably produces it. Your retention metric and the learner's development can point in opposite directions.

### Anthropomorphism and development (operator signal)

Prateek Maheshwari (Physics Wallah) described "mega classrooms" in which 100,000 students learn in one live, teacher-led session, with AI handling their questions, at about $40 for a year. The student feedback he hears keeps returning to one line: "AI is not judging us" ([transcript](../../sources/events/2026-asu-gsv/transcripts/49-the-billion-student-ambition-scaling-education-in-the-age-of-choice.md)). That line states both the appeal and the hazard.

On the anthropomorphism panel, Tanya Gamby (Southern New Hampshire University) said real relationships depend on "rupture and repair." Matthew Biel (Georgetown) described interactions with AI as "not mutual" but "transactional," and warned that adolescents learn relationships through that friction, which a model that never judges and never pushes back cannot supply. The moderator, whom the summit report names as Paul LeBlanc, was blunter: "AI is going to make social media look like a day at the beach" ([transcript](../../sources/events/2026-asu-gsv/transcripts/84-living-learning-with-aliens-the-complex-psychology-of-ai-anthropomorphism.md)).

### Adult tools in children's hands (operator signal)

Lovable builds software for "the 99%" of people who are not developers. Introducing Anton Osika, the moderator said Lovable had "allegedly" reached $400M in annual recurring revenue within two years. The company later confirmed it crossed $400M in February 2026 ([TechCrunch, March 11, 2026](https://techcrunch.com/2026/03/11/lovable-says-it-added-100m-in-revenue-last-month-alone-with-just-146-employees/)). In the same session, a speaker described nine-year-old entrepreneurs selling real products from sites they built with it. Imagi partners with Lovable to bring it into K-12 classrooms as the layer for younger users ([transcript](../../sources/events/2026-asu-gsv/transcripts/94-fireside-chat-with-lovable-and-imagi.md)).

The underlying tools were not built for children. If your product reaches minors, directly or because a teacher points it at a class, assume the base model was tuned for adults. You build the age-appropriateness layer; you do not inherit it. ScaleU's view is that district-grade versions of that layer will become a product category.

### The optimist case (speaker claim)

James Donovan, head of learning and cognitive outcomes at OpenAI, argued that the question is how the model is tuned, not whether AI helps cognition. Model behavior elicits a human behavior, that behavior adds up to cognitive outcomes over time, and a model tuned toward pedagogical alignment yields metacognitive gains. He pointed to a 20,000-student research deployment in Estonia as the model for generating evidence ([transcript](../../sources/events/2026-asu-gsv/transcripts/64-does-ai-expand-human-intelligence-or-atrophy-it.md)).

OpenAI's [announcement](https://openai.com/index/the-next-phase-of-education-for-countries/) (May 20, 2026) describes a nationwide ChatGPT Edu deployment that Estonia's Ministry of Education leads through the AI Leap Foundation, reaching more than 20,000 students and 4,600 teachers. It says OpenAI is working with AI Leap, the University of Tartu, and Stanford to study how AI affects those students' learning, and has committed to publishing the findings. As of 2026-10-30, no study design or results had been published. This is a stated thesis and a study still running, not a result.

Omar Abbosh (Pearson) summed up both camps: "If you use it wrong, you will absolutely get dumber. If you use it right, you can get smarter" ([transcript](../../sources/events/2026-asu-gsv/transcripts/71-is-ai-eating-education-interview-series-with-kevin-roose-casey-newton.md)). Enforcing the difference is the institution's job and your product's.

## How young people feel about AI (survey finding)

Kevin Roose (NYT) and Casey Newton (Platformer) raised a Gallup survey, run with the Walton Family Foundation and GSV Ventures, of 1,572 people aged 14 to 29, fielded February 24 to March 4, 2026. [Gallup reports](https://news.gallup.com/poll/708224/gen-adoption-steady-skepticism-climbs.aspx):

| Feeling about AI | Share | Change in a year |
|---|---|---|
| Hopeful | 18% | Down 9 points |
| Excited | 22% | Down 14 points |
| Angry | 31% | Up 9 points |
| Anxious | 42% | Unchanged |

Usage held steady: 51% use generative AI at least weekly. In the same session, Garrett Lord (Handshake) warned of an "agency divide" between people who manage AI and people AI manages ([transcript](../../sources/events/2026-asu-gsv/transcripts/71-is-ai-eating-education-interview-series-with-kevin-roose-casey-newton.md)). Your learners are not uniformly excited. A large share are anxious or angry, and they can tell which side of that divide a product puts them on.

## Design responses

Each of these was described at the summit as something being built. None is a proven outcome.

**Build in friction and limits.** Ann Wang described OMA Play, a screenless audio device for children aged three to five, still in early research and development. It has no face. It naps during the day, shuts off at night, and parents control when it engages. Wang said it "might interact with you" about 60% of the time and will never give an answer right away ([transcript](../../sources/events/2026-asu-gsv/transcripts/84-living-learning-with-aliens-the-complex-psychology-of-ai-anthropomorphism.md)). The principle reaches past toddlers. In a student-facing tutor, a time limit is part of the pedagogy: it protects productive struggle and shows a buyer that you are not maximizing a learner's screen time. Decide what friction you build in on purpose, and how you will detect when praise or agreement retains a learner at the learner's expense.

**Keep the human as the user while the evidence is thin.** Meyer's "AI through the teacher" is a starting posture, not a permanent limit. Until your own outcome data says otherwise, aim the model at the teacher or instructor, where it shows who is stuck, drafts feedback, and flags patterns. That carries less developmental risk than aiming it at the learner, and it matches the K-12 trial results above. ScaleU's practitioner read, not a measured result, is that a teacher-facing design also clears an institution's AI review faster.

**Adopt the institutional default as a product stance.** ScaleU's [summit report](../../sources/events/2026-asu-gsv/synthesis/summit-intelligence-report.md#theme-7-ais-effect-on-cognition) proposes a default for buyers; it is ScaleU's synthesis of the cognition sessions, not a speaker's claim. Assume model defaults push toward cognitive automation. Demand productive friction in the student-facing layer. Invest in teacher capability before chatbot seats. Build the tool that makes the institution's enforcement job easier.

## What institutional buyers will ask

Buyers also review your AI as a vendor risk. Each item links to the guide that covers it.

- **Student data.** Who sees it, where it goes, and whether it trains a model. Federal and state privacy law (FERPA, COPPA, state student-privacy laws) is in [K-12 regulation](../market/k12-regulatory.md). FERPA covers colleges too: once a student turns 18 or enters a postsecondary institution at any age, the rights [transfer from the parents to the student](https://studentprivacy.ed.gov/faq/what-ferpa). Colleges often send EDUCAUSE's [HECVAT](https://www.educause.edu/hecvat) security questionnaire. See [procurement](../selling/procurement-guide.md) for where the IT and privacy review sits in a deal, and [data terms education buyers will ask about](ai-native-framework.md#data-terms-education-buyers-will-ask-about) for what each model provider commits to.
- **Security.** Whether the model can be tricked into leaking records. See the next section.
- **Evidence of learning impact.** What your outcome data shows, and how strong it is. See [evidence tiers](../evidence/evidence-tiers.md).
- **Fit with institutional policy.** Colleges are writing AI-use and academic-integrity policies. Accessibility review and VPATs apply to AI features too. See the [higher-ed landscape](../market/highered-landscape.md).
- **Funding.** On July 22, 2025, the U.S. Department of Education [told grantees](https://www.ed.gov/about/news/press-release/us-department-of-education-issues-guidance-artificial-intelligence-use-schools-proposes-additional-supplemental-priority) that federal grant funds may support AI-enhanced high-impact tutoring, AI-based instructional materials, and AI for college and career advising, provided the use meets each program's rules. The guidance also set principles for responsible use, including attention to privacy and to engaging parents and other stakeholders.
- **Chatbots and minors.** Whether your product is a companion chatbot under state law, and what it does when a student raises self-harm. See below.

### Chatbots, minors, and the law

**Federal.** On September 11, 2025, the FTC [ordered seven companies](https://www.ftc.gov/news-events/news/press-releases/2025/09/ftc-launches-inquiry-ai-chatbots-acting-companions) (Alphabet, Character Technologies, Instagram, Meta, OpenAI, Snap, and xAI) to report how they measure, test, and monitor the effects of companion chatbots on children and teens, including how they monetize engagement and comply with the COPPA Rule. The orders were issued under Section 6(b) of the FTC Act. That makes this a study, not an enforcement action. It also shows the questions a regulator asks.

**States.** California's SB 243, signed October 13, 2025, and effective January 1, 2026 ([TechCrunch](https://techcrunch.com/2025/10/13/california-becomes-first-state-to-regulate-ai-companion-chatbots/)), regulates companion chatbots. According to the Future of Privacy Forum's [analysis](https://fpf.org/blog/understanding-the-new-wave-of-chatbot-legislation-california-sb-243-and-beyond/), an operator that knows a user is a minor must disclose that the user is talking to AI, prompt a break every three hours, and take reasonable steps to prevent sexually explicit content. Every operator needs a self-harm protocol with crisis referrals, and the law gives injured users a private right of action with damages of at least $1,000. Other states followed. A law-firm survey from April 2026 ([Orrick](https://www.orrick.com/en/Insights/2026/04/2026-State-Chatbot-Laws-Key-Provisions-and-Regulatory-Trends)) lists New York's companion law, in effect since November 5, 2025; Oregon and Washington laws effective January 1, 2027; and Nebraska and Idaho laws effective July 1, 2027. These are secondary summaries. Read the statute for any state you sell in.

ScaleU's view: these laws target chatbots that sustain a human-like relationship, and a tutor that stays on its subject is probably outside the definitions. A named persona that remembers a student, chats socially, and encourages return visits moves toward them. Decide which you are building, write it down, and have counsel confirm. Whatever the answer, build the self-harm protocol; a district will ask for it.

**European Union.** The EU AI Act treats four education uses as high-risk: deciding admission or placement, evaluating learning outcomes, assessing the level of education a person should receive, and monitoring students during tests ([Annex III, point 3](https://artificialintelligenceact.eu/annex/3/)). It prohibits AI that infers emotions in education institutions, except for medical or safety reasons; that ban has applied since February 2, 2025 ([Article 5](https://artificialintelligenceact.eu/article/5/)). The high-risk obligations were due on August 2, 2026. An amending regulation published in the Official Journal on July 24, 2026, moved them to December 2, 2027 ([Garrigues](https://www.garrigues.com/en_GB/garrigues-digital/ai-digital-omnibus-regulation-has-been-published-redefining-deadlines-and)). An AI grader or proctor sold in the EU falls under these rules. See [international markets](../market/international-markets.md).

## Security: the lethal trifecta

The trust risk has a security twin. Simon Willison calls it the ["lethal trifecta"](https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/): a model with access to private data, exposure to untrusted content, and the ability to communicate externally can be tricked into leaking that data. A student-facing model that touches FERPA records, reads student-supplied content, and can send email or post has all three. Willison argues that guardrails which catch most attacks are not enough: "in web application security 95% is very much a failing grade." Remove the exfiltration path in the architecture; do not trust a prompt to behave.

## Related guides

- [AI-native or bolted-on](ai-native-framework.md). The deeper AI sits in your product, the more of the questions on this page are yours to answer and not the model lab's.
- [Defensibility](defensibility-moats.md)
- [Learning science](learning-science.md)
- [Evidence tiers](../evidence/evidence-tiers.md) and the [evidence roadmap](../evidence/evidence-roadmap.md)
- [K-12 regulation](../market/k12-regulatory.md)
- [International markets](../market/international-markets.md)

---
*Facts last checked: 2026-10-30 (speaker claims against the linked transcripts; the Gallup survey, Lovable's revenue, Willison's post, and ED's guidance against the linked sources; claims about academic research against the SCALE review and the Liu, Shaw and Nave, and Cheng papers; no published source was found for the "13 times" figure, and the Estonia study had published no results). Rewritten for clarity 2026-11-11; added and checked that day: the Bastani, Kestin, Wang, LearnLM, Fan, and Contractor studies (through Consensus), the FTC orders, the state chatbot laws (through the linked secondary sources, not the statutes), and the EU AI Act provisions and delay. Nothing else was rechecked.*

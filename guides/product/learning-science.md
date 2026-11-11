# Learning science for product decisions

Build the product around retrieval, spacing, explanatory feedback, and support that fades as the learner improves; those findings hold up best. Treat adaptivity, gamification, and AI tutoring as design bets whose results depend on implementation, and skip learning-styles matching.

**Applies to:** K-12, higher ed, workforce, and consumer learning products. Research settings are named with each finding; most are not specific to the United States.

## How to read this page

Findings are the papers', reported with the effect sizes they report (g and d are standardized mean differences). Each line marked "Implication" is ScaleU's view, not a research finding. The library's topic files in [sources/research](../../sources/research/README.md) list more papers per topic; they inherit their paper selection from another collection and are not systematic reviews. A finding from a lab or a single course is a reason to test a feature, not proof that yours works: see the [evidence roadmap](../evidence/evidence-roadmap.md).

| Design decision | State of the evidence | Rule of thumb (ScaleU's view) |
|---|---|---|
| Retrieval practice | Consistent in classrooms | Make learners recall, not reread |
| Spacing | Consistent; fewer classroom studies | Schedule reviews; measure delayed retention |
| Feedback | Consistent for explanations | Explain; a bare right-or-wrong mark adds little |
| Worked examples and fading | Consistent for novices, reverses for experts | Start with examples, remove them with skill |
| Multimedia and cognitive load | Consistent for a known set of principles | Cut what does not teach; signal what matters |
| Mastery and adaptivity | Mixed | Prove adaptive beats a fixed sequence |
| Gamification | Small effects, unstable for motivation | Use for practice volume, not as the learning claim |
| Active learning | Consistent in undergraduate STEM | Design for doing during class time |
| Transfer | Far transfer rarely found | Teach and assess the target skill itself |
| Learning styles | Matching not supported | Do not build it |
| AI tutoring and feedback | Early, mixed, design-dependent | Guard against answer-giving; test unassisted |

## Practice and retrieval

- **Found.** A review of 50 classroom experiments (n = 5,374) reported medium or large benefits of retrieval practice in 57% of effect sizes ([Agarwal et al., 2021](https://doi.org/10.1007/s10648-021-09595-9)). A meta-analysis of 222 classroom studies put the effect of quizzing on achievement at g = 0.499 ([Yang et al., 2021](https://doi.org/10.1037/bul0000309)). Library file: [spaced repetition and retrieval practice](../../sources/research/spaced-repetition.md).
- **Limits.** Only 6% of the experiments Agarwal reviewed came from non-Western countries. Yang found the effect varied with corrective feedback, number of repetitions, and what the comparison group did.
- **Implication.** Default to questions the learner must answer from memory, with feedback, in place of summaries and rereading.

## Spacing

- **Found.** Across 317 experiments, spaced study beat massed study, and the best gap between sessions grew with how long the material had to be remembered ([Cepeda et al., 2006](https://doi.org/10.1037/0033-2909.132.3.354)). In classrooms, a meta-analysis of 22 reports found d = 0.54 for distributed over massed practice ([Mawson and Kang, 2025](https://doi.org/10.3390/bs15060771)). Library file: [spaced repetition](../../sources/research/spaced-repetition.md).
- **Limits.** The 2006 synthesis covers verbal recall, mostly in labs. The classroom meta-analysis had too few studies to test moderators. In second-language learning, shorter and longer spacing did equally well on immediate tests; longer spacing won only on delayed tests ([Kim and Webb, 2022](https://doi.org/10.1111/lang.12479)).
- **Implication.** Set review intervals from the date the learner needs the knowledge, and judge the scheduler on a delayed test. Same-session accuracy will mislead you.

## Feedback timing and type

- **Found.** In computer-based learning (40 studies), feedback that explained produced larger effects (0.49) than giving the correct answer (0.32) or marking right or wrong (0.05) ([Van der Kleij et al., 2015](https://doi.org/10.3102/0034654314564881)). In elementary and secondary school, comments outperformed grades on both achievement and motivation ([Koenka et al., 2019](https://doi.org/10.1080/01443410.2019.1659939)). Library files: [formative assessment](../../sources/research/formative-assessment.md), [automated feedback](../../sources/research/automated-feedback.md).
- **Limits.** Van der Kleij's effects ranged from −0.78 to 2.29 and were larger in mathematics than in other subjects. Delayed feedback lowered effects overall; the suggestion that immediate feedback suits lower-order learning and delayed suits higher-order was not statistically significant. A meta-analysis of 435 feedback studies (d = 0.48) concluded that feedback is not one consistent treatment ([Wisniewski et al., 2020](https://doi.org/10.3389/fpsyg.2019.03087)).
- **Implication.** Spend engineering on the explanation. Ship immediate feedback by default and test delay only for complex tasks.

## Worked examples and fading

- **Found.** Worked examples improved mathematics performance, g = 0.48 across 55 studies from elementary to postsecondary ([Barbieri et al., 2023](https://doi.org/10.1007/s10648-023-09745-1)). Learners with low prior knowledge learned more from high-assistance instruction (d = 0.505); learners with high prior knowledge learned more from low assistance (d = −0.428) ([Tetzlaff et al., 2025](https://doi.org/10.1016/j.learninstruc.2025.102142)). Library file: [worked examples](../../sources/research/worked-examples.md).
- **Limits and conflicts.** In Barbieri, adding self-explanation prompts lowered the effect, and correct examples alone beat mixes with incorrect ones. Against example-first teaching, problem solving before instruction outperformed instruction first, g = 0.36 across 53 studies, but not for grades 2 to 5 or for domain-general skills ([Sinha and Kapur, 2021](https://doi.org/10.3102/00346543211019105)). Tetzlaff found weaker evidence for younger students and for humanities and language learning.
- **Implication.** Measure prior knowledge at entry, show full solutions to novices, and withdraw steps as accuracy rises. Help that never fades will slow your best users.

## Cognitive load and multimedia design

- **Found.** An overview of 29 reviews (1,189 studies) found 11 multimedia design principles with significant positive effects on learning. The largest were captioning second-language video, placing related words and pictures together in time and space, and signaling what matters ([Noetel et al., 2021](https://doi.org/10.3102/00346543211052329)). Library files: [multimedia principles](../../sources/research/multimedia-principles.md), [cognitive load](../../sources/research/cognitive-load.md).
- **Limits.** Design mattered more for complex material and for system-paced formats such as lectures than for self-paced ones. Applying a principle does not guarantee the result: in a randomized trial with 18 novice medical students, a worked example followed by a completion exercise raised cognitive load and lowered performance in virtual-reality surgical training ([Andersen et al., 2016](https://doi.org/10.1186/s41077-016-0022-1)).
- **Implication.** Remove decoration, keep text beside the thing it explains, and let learners control pace. Check each screen of video and simulation first; self-paced text forgives more.

## Mastery and adaptivity

- **Found.** Mastery learning programs raised exam performance in 108 controlled evaluations, more for weaker students ([Kulik et al., 1990](https://doi.org/10.3102/00346543060002265)). AI-enabled adaptive systems outperformed non-adaptive instruction, g = 0.70 across 45 studies ([Wang et al., 2024](https://doi.org/10.1177/07356331241240459)). Library files: [adaptive learning](../../sources/research/adaptive-learning.md), [mastery-based grading](../../sources/research/mastery-based-grading.md).
- **Limits and conflicts.** Kulik also found mastery programs can increase time on task, and self-paced versions often lowered completion rates in college classes. A reply argued the effect on standardized measures was close to zero ([Slavin, 1990](https://doi.org/10.3102/00346543060002300)). Wang's effect varied with research design and publication type. In a large randomized trial in Dutch secondary schools, adaptive practice produced no average test-score gain over static practice, and static practice helped higher-ability students by 0.08 SD ([van Klaveren et al., 2017](https://doi.org/10.1016/j.econedurev.2017.04.003)).
- **Implication.** Adaptivity is a hypothesis to test against your own fixed sequence on an independent measure. Watch completion: self-pacing without deadlines loses students.

## Motivation and gamification

- **Found.** Gamification showed small effects on cognitive (g = .49), motivational (g = .36), and behavioral (g = .25) outcomes ([Sailer and Homner, 2019](https://doi.org/10.1007/s10648-019-09498-w)). Library file: [self-determination and gamification](../../sources/research/self-determination-gamification.md).
- **Limits.** In Sailer and Homner's higher-rigor studies only the cognitive effect held. A later meta-analysis of 35 interventions found a small effect on intrinsic motivation (g = 0.257) and minimal effect on perceived competence ([Li et al., 2024](https://doi.org/10.1007/s11423-023-10337-7)).
- **Implication.** Use points and streaks to increase practice you already know works. Do not sell them as motivation, and check whether use survives once the novelty fades.

## Active learning

- **Found.** In 225 studies of undergraduate STEM courses, active learning raised exam scores by 0.47 SD, and students in traditional lectures were 1.5 times more likely to fail ([Freeman et al., 2014](https://doi.org/10.1073/pnas.1319030111)). Achievement gaps for underrepresented students narrowed only in high-intensity active learning ([Theobald et al., 2020](https://doi.org/10.1073/pnas.1916903117)). Library file: [active learning](../../sources/research/active-learning.md).
- **Limits.** The evidence is undergraduate STEM, compared with traditional lecture. A 2026 meta-analysis found larger effects at medium and high intensity than at low (g = 0.583 and 0.593 against 0.246) but notes intensity may be confounded with other course redesign ([Xu et al., 2026](https://doi.org/10.3390/educsci16071044)).
- **Implication.** For higher-ed courseware, the unit of value is class time spent doing. Report it to instructors.

## Transfer

- **Found.** Across cognitive-training programs (working memory, video games, music, chess), far transfer to other skills was zero once placebo effects and publication bias were controlled; near transfer to similar tasks was real ([Sala et al., 2019](https://doi.org/10.1525/collabra.203)). Library file: [transfer of learning](../../sources/research/transfer-of-learning.md), which mostly covers outcomes of learning technologies and says little on transfer itself.
- **Limits.** The finding concerns general cognitive training, not subject teaching.
- **Implication.** Claim the skill you teach and assess. Avoid promises that practice in your product improves general reasoning or grades in other subjects unless you have measured it.

## Matching instruction to learning styles

- **Found.** A meta-analysis of 21 studies found a small overall benefit of matching instruction to modality styles (g = 0.31), but only 26% of outcome measures showed the crossover pattern the matching hypothesis predicts; the authors judged the benefit too small and infrequent, and the studies too weak, to justify adoption ([Clinton-Lisell and Litzinger, 2024](https://doi.org/10.3389/fpsyg.2024.1428732)). Library file: [learning styles](../../sources/research/learning-styles.md).
- **Implication.** Do not build a style quiz or style-based content routing. Offer formats as learner choice and accessibility, and adapt on prior knowledge, which has evidence (see worked examples).

## AI tutoring and automated feedback

- **Found.** Automated writing feedback improved writing performance, g = 0.55 across 20 studies, with large variation ([Fleckenstein et al., 2023](https://doi.org/10.3389/frai.2023.1162454)). In a field experiment with nearly 1,000 high school math students, a standard GPT-4 chat interface raised practice grades by 48% but left students 17% worse than no-access peers once it was removed; a tutor with safeguards raised practice grades by 127% and largely avoided the later loss ([Bastani et al., 2025](https://doi.org/10.1073/pnas.2422633122)). In a randomized trial in a Harvard course, students learned more in less time with a purpose-built AI tutor than in an active-learning class ([Kestin et al., 2025](https://doi.org/10.1038/s41598-025-97652-6)). Giving human tutors AI suggestions raised K-12 students' topic mastery by 4 percentage points, 9 for students of lower-rated tutors (900 tutors, 1,800 students; [Wang et al., 2024, preprint](https://doi.org/10.48550/arxiv.2410.03017)).
- **Limits.** A review of 69 ChatGPT experiments found improved performance but flagged missing power analyses and posttests that may measure the tool's output more than the student's learning ([Deng et al., 2024](https://doi.org/10.1016/j.compedu.2024.105224)). Evidence is thin on retention after months, on young children, on standardized outcomes, and on independent replication of any one product. Kestin is one course; the tutoring study is not yet peer reviewed.
- **Implication.** Make the tutor withhold answers and ask for the learner's attempt first, keep a human in the loop where you can, and evaluate on unassisted performance after access ends. See [AI risk and trust](ai-risk-and-trust.md).

## Checklist for a feature

1. Which finding above does the feature rely on, and does the study population match your users?
2. Does the learner produce an answer before seeing one?
3. Does feedback explain, and arrive while the attempt is fresh?
4. Does support shrink as the learner's accuracy rises?
5. Is there a delayed, unassisted measure of learning, not only in-session accuracy or engagement?
6. Have you compared the feature with the simpler version (fixed sequence, no points, no AI)?
7. Does marketing claim only the skill you measured?

## Related guides

- [Evidence roadmap](../evidence/evidence-roadmap.md)
- [Evidence tiers](../evidence/evidence-tiers.md)
- [AI-native framework](ai-native-framework.md)
- [AI risk and trust](ai-risk-and-trust.md)
- [Logic model template](../templates/logic-model.md)

---
*Facts checked 2026-11-11 against the linked sources. Figures labeled as practitioner estimates are judgment, not data.*

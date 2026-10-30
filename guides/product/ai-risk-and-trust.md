# AI risk and trust for edtech founders

What AI does to learners, and to the trust between learners and the people around them, before you ship a student-facing model. For founders selling into K-12 districts, universities, and corporate L&D.

*Note: these are practitioner signals from the ASU+GSV 2026 summit, not peer-reviewed evidence.* Where a claim is research-backed versus a panel assertion, this file says which. As of the ASU+GSV 2026 summit, the cognition question was the most contested theme of the week, and platform companies and practitioners were not in the same room on it.

*Source: ASU+GSV 2026 Summit Intelligence — ScaleU. CC BY 4.0. Practitioner signals, not peer-reviewed research.*

---

## The honest caveat, up front

The single most-cited number at the summit cuts against the hype. Ben Riley (Cognitive Resonance) pointed to Stanford SCALE's review of 800 studies of LLMs in education: only 20 showed causal impact, and virtually none of those were positive. So the research base is thin, and what causal evidence exists is not on the model's side yet. That is research-backed (it's a review of studies). Almost everything else below is panel assertion — operators reporting what they see, not controlled trials. Treat it as signal worth designing around, not proof.

Riley's framing is the one to hold even if you reject his conclusion: a tool was deployed to roughly 500 million students before the longitudinal data exists. Wait for the RCTs to settle and you decide with a five-year lag. Deploy now without measurement and you become the data. Pick your error on purpose.

---

## The cognition and trust risks

### Cognitive automation, not offloading (research-backed lean)
Riley named the behavior "cognitive automation," not the gentler "cognitive offloading." He pointed to Carnegie Mellon and UCLA work showing "cognitive surrender" — students lose the ability to do the work once they try without the tool. The field datapoint: Sal Khan's own chief learning officer reported students typing "IDK" into Khanmigo rather than engaging with it. The risk isn't that students think less while using AI. It's that the capacity erodes. — Ben Riley (Cognitive Resonance)

### Kids don't want the chatbot tutor (operator signal)
Dan Meyer (Amplify) watches one benchmark: whether kids actually want to talk to a chatbot tutor. It has sat flat at roughly 5% for three years. His build rule follows from it — AI as an analytical layer for teachers, never direct-to-student. Joe Davis (KAIT Lab) goes the other direction with the same goal: AI-powered infrared pens that surface where students get stuck inside a problem set, so productive struggle stays the load-bearing part. — Dan Meyer (Amplify), Joe Davis (KAIT Lab)

### Killing the butterfly (operator signal)
Larry Berger (Amplify) gave the most evocative warning. The capabilities exist, he said, but every AI implementation he sees is "killing the butterfly" — the moment of collective wonder that pollinates the next thousand moments of learning. His board gave him six months to step back from running the company and figure out whether AI can keep the butterfly alive. He does not have an answer yet. That last part matters: a serious operator with every incentive to be bullish is openly unsure. — Larry Berger (Amplify)

### Sycophancy and the praise problem (operator signal)
Isabelle Hau (Stanford Accelerator for Learning) shared a stat from a visiting scholar: AI models praise children 13 times more often than humans do. Her read as a parent — if a model praises my child 13 times more than I do, kids start to expect it, and human-to-human relationships shift to match. The structural problem underneath: companies are incentivized to optimize for engagement, and sycophancy is a reliable way to get it. Your retention metric and the learner's development can point in opposite directions. — Isabelle Hau (Stanford Accelerator for Learning)

### Anthropomorphism and developmental risk (operator signal)
Scale makes this urgent. Prateek Maheshwari (Physics Wallah) runs mega-classrooms — 100,000 students in a single live AI session at $40 ARPU — and the student feedback keeps returning to one line: "AI is not judging us." That's the appeal and the hazard in one sentence. Matthew Biel (Georgetown pediatric psychiatry) frames these as "non-mutual transactional" relationships and warns that adolescent development requires rupture and repair, which a model that never judges and never pushes back cannot provide. Paul LeBlanc was blunter: "AI is going to make social media look like a day at the beach." — Prateek Maheshwari (Physics Wallah), Matthew Biel (Georgetown), Paul LeBlanc

### Tools built for adults, handed to kids (operator signal)
Anton Osika said Lovable hit $400M ARR in two years serving "the 99%" of non-developers, including nine-year-olds running real e-commerce sites. The underlying tools were not built for kids. Imagi exists as the safety wrapper for exactly that reason. If your product reaches minors — directly or because a teacher points it at a class — assume the base model was tuned for adults and the age-appropriateness layer is yours to build. — Anton Osika (Lovable)

### Falling hope, rising anger (operator signal)
Kevin Roose (NYT) and Casey Newton (Platformer) landed a different datapoint: a Gallup/Walton/GSV poll of 14-to-29-year-olds showed hope about AI down 9 points to 18% in one year, with a third of Gen Z AI users reporting anger. Garrett Lord coined the line that stuck — an "agency divide" between people who manage AI and people AI manages. The learners you serve are not uniformly excited. A meaningful share are anxious or angry, and they can tell which side of that divide a product puts them on. — Kevin Roose (NYT), Casey Newton (Platformer), Garrett Lord

### The other side of the table (the optimist case, for honesty)
The bull case came from James Donovan, head of learning and cognitive outcomes at OpenAI. His argument: the question isn't whether AI helps cognition but how the model is tuned. Model behavior elicits a human behavior, that behavior ladders up to cognitive outcomes over time, and tuned toward pedagogical alignment you get metacognitive gains. He pointed to a 20,000-student RCT in Estonia (University of Tartu and Stanford) as the model for generating real evidence. Note what this is and isn't: a stated thesis plus a study still running, not a result. Omar Abbosh (Pearson) gave the cleanest synthesis of both camps: "If you use it wrong, you will absolutely get dumber. If you use it right, you can get smarter." The institution's job — and your product's job — is enforcing the difference. — James Donovan (OpenAI), Omar Abbosh (Pearson)

---

## The design responses founders can adopt

These came up at the summit as concrete moves, not theory. Each is a panel assertion about what's being built, not a proven outcome.

### Refusal by design
OMA Play's response to the developmental risk for the youngest learners is a screenless device for ages three to five with no face, that takes naps, shuts off at night, and refuses to engage 40% of the time on purpose. The design principle generalizes past toddlers: build friction in deliberately. The product question Hau's anthropomorphism work forces on every tutoring builder — what friction do you build in on purpose, and how do you measure when sycophancy is hurting the learner instead of just retaining them? — OMA Play

### Age gates and an age-appropriate wrapper
Imagi sits as the safety layer because the frontier tools underneath weren't built for kids. If your product touches minors, the age-appropriateness layer is a thing you build, not a thing you inherit. Expect district-grade equivalents for K-12 to be a category, not a feature.

### Time caps and screen-time limits
The OMA Play device caps engagement structurally — naps, nighttime shutoff, a designed-in refusal rate. Time limits are a design lever, not just a parental-controls afterthought. For a student-facing tutor, the cap is part of the pedagogy: it protects productive struggle and signals to a district buyer that you are not optimizing a child's screen time to the ceiling.

### Keep the human as the user, when the evidence is thin
Meyer's "analytical layer for teachers, never direct-to-student" is a posture, not a constraint you're stuck with. Until your own outcome data says otherwise, aiming the model at the teacher (where it surfaces who's stuck, drafts feedback, flags patterns) carries less developmental risk than aiming it at the child. It also clears district AI review faster.

### The defensible institutional posture
The summit's cleanest default for a buyer, which you can adopt as a product stance: assume model defaults push toward cognitive automation, not learning. Demand productive friction in the student-facing layer. Invest in teacher capability, not chatbot seats. Build the tool that makes the institution's enforcement job easier, not the one that quietly does the thinking for the student.

---

## Cross-links

- The trust risk has a security twin. A student-facing model that touches FERPA records, reads untrusted content, and can send data out is the "lethal trifecta" — see the data-exfiltration point in [operator-lessons.md](https://github.com/savvides/edtechfounderstack/blob/800fcaf5fcc187b3ee3c35f4224cbcdc560548a6/data/operator-lessons.md). Prompt-injection filters top out around 97%, a failing grade, so architect the exfiltration path away rather than trusting a prompt to behave.
- Whether AI is your product's load-bearing wall or a bolted-on chatbot changes how much of this risk you own. See [ai-native-framework.md](ai-native-framework.md). The deeper the AI sits in the product, the more the cognition and trust questions on this page are yours to answer, not the model lab's.

*Last updated: 2026-05-30*

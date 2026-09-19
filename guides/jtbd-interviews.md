# JTBD Switch interviews for edtech

How to discover and validate real demand by interviewing the people who already switched — and reading the four forces that pushed them. For edtech founders selling to K-12 districts, universities, or corporate L&D who keep hearing "this sounds great" and want to know whether anyone will actually buy.

*Adapted from the JTBD Switch toolkit (github.com/savvides/jtbd, MIT), itself based on Bob Moesta's Jobs-to-be-Done "Switch" method.*

People don't buy products. They hire them to make progress. A registrar had a routine before your tool showed up — transcripts in a shared drive, a wait-list spreadsheet, a part-time evaluator. It was terrible, and they were getting the job done anyway. Then something broke. They looked around, picked one option, and switched. Reconstruct that whole story and you learn exactly what to build and how to sell it. Survey the concept and you learn nothing. See [operator-lessons.md](https://github.com/savvides/edtechfounderstack/blob/800fcaf5fcc187b3ee3c35f4224cbcdc560548a6/data/operator-lessons.md): count the workaround, don't survey the concept.

## The four forces

Every switch is driven by four forces. Two push the buyer to change. Two hold them back. The switch only happens when push plus pull overwhelms anxiety plus habit.

```
DRIVING THE SWITCH                 RESISTING THE SWITCH
==================                 ====================

Push of the current      ──►     ◄──  Anxiety of the new
situation                                solution
"what is broken now"               "what if it doesn't work"

Pull of the new          ──►     ◄──  Habit of the present
solution
"what is attracting me"            "what I am used to"
```

Score each force you find on a 1-10 intensity scale: 10 is the dominant driver of the decision, 1 is barely relevant. The number is directional, not precise — a 3 versus an 8 is meaningful, a 6 versus a 7 is noise. The point is to rank what actually moved the buyer, not to grade them.

### Push — what is breaking now

Push is what is actively failing in the status quo. It's always tied to a specific event or pattern, never a vague feeling. "It was frustrating" is not a push. "The transcript backlog blew past the enrollment deadline and we lost the student" is a push.

- A provost: "Our 7.5-week courses had a 30% drop rate and the board started asking why."
- A transfer student: "My GPA dropped a full point the term I didn't have an advisor who could tell me what to take next."
- A district CTO: "The old gradebook went down during the last week of the term and teachers couldn't post finals."
- An L&D lead: "Completion on our compliance training sat at 40% and audit season was coming."
- A registrar: "Manual credit evaluation took three weeks and students were committing to the competitor that answered first."

### Pull — what the new thing promises

Pull is the magnetic appeal of the alternative. It's about an imagined future state, not a feature list. Buyers aren't attracted to "real-time articulation" — they're attracted to the idea that they can tell an admitted student their credit status before the deadline without anyone waiting three weeks.

- A registrar: "I pictured students seeing exactly which credits would count the day they applied, not a month later."
- A provost: "I wanted to see the drop-risk numbers myself, without asking institutional research to pull a report."
- An L&D lead: "I imagined onboarding a new hire to job-ready in half the time, and being able to show that number to my VP."
- A faculty member teaching 200 online students: "I pictured giving every student real feedback without working until midnight."

When you hear a pull, keep asking "why does that matter?" until you hit the emotional payoff. The payoff — credibility, not being the bottleneck, looking good to leadership — is the real pull.

### Anxiety — what scares them about switching

Anxiety is everything that makes the buyer hesitate. It's the silent killer. People rarely volunteer it, so you have to ask directly: "What almost stopped you?"

- A registrar: "What if we lose three years of transcript data in the migration?"
- A district CTO: "What if this thing touches FERPA records and we end up with a breach during the pilot?"
- A provost: "What if faculty hate it and I've spent political capital pushing a tool nobody uses?"
- An L&D lead: "What if procurement classifies it high-risk and it sits in security review for six months?"
- A dean: "What if the vendor turns out worse than what we already have, and now I own that decision?"

### Habit — the comfort of the familiar

Habit is the pull of the way things already are. People tolerate enormous pain to avoid changing their behavior. Habit is the most underprobed force, because buyers build elaborate workarounds and forget they're workarounds.

- A registrar: "Every evaluator had their own way of dealing with the old system's quirks. Retraining them felt brutal."
- An advising office: "Our whole intake process was built around the degree-audit tool nobody can read. Someone's entire job was translating it into plain English for students."
- A district: "Teachers had years of materials inside the old LMS. Moving felt like starting over."
- An L&D team: "We had reports the CFO expected in a specific format. Rebuilding them was its own project."

When someone describes a workaround — "my analyst had a whole process for that" — you've found both a habit force (the comfort of the routine) and a push force (the routine exists because the tool is broken). Probe both.

## Job stories, not user stories

The standard "As a user, I want X so that Y" template hides the thing that matters: the situation. It assumes the persona and skips the trigger. A job story puts the moment first.

Format: **When [situation], I want [motivation], so I can [outcome].**

The situation is the trigger — the specific moment the job shows up. The motivation is what they reach for. The outcome is the progress they're trying to make. Derived from jobs in [higher-ed-jobs-atlas.md](higher-ed-jobs-atlas.md):

> **When** a transfer student applies and hasn't seen their credit articulation, **I want** to show them exactly which credits count before the enrollment deadline, **so I can** stop losing them to the competitor that answered first.

> **When** I'm teaching 200 online students and can't give any of them real feedback, **I want** to draft high-quality feedback at scale that I review and send, **so I can** stop students feeling ignored without working until midnight.

Notice what the job story forces you to know that a user story lets you skip: the exact moment, the stakes, the alternative they'd otherwise choose. "As an instructor, I want better feedback tools" tells you nothing. The job story tells you when to show up and what you're replacing.

## The backward-timeline interview

Every switch follows the same timeline. Your job is to reconstruct it, and the trick is to start at the end and walk backward. People remember decisions; they reconstruct the path from there.

```
FIRST        PASSIVE       ACTIVE        DECIDING      CONSUMING
THOUGHT      LOOKING       LOOKING
  │             │             │             │             │
  ▼             ▼             ▼             ▼             ▼
"something    "casually     "actively     "chose this   "using the
 is wrong"     noticing"     evaluating"   one"          new thing"
```

- **First thought:** the exact moment they realized things could be different — usually a specific event, like a gradebook going down during finals.
- **Passive looking:** casual awareness. They ask peers, read comparison threads, notice tools exist. Not searching yet.
- **Active looking:** something escalated the urgency. Now they're booking demos and running trials. Find out *what changed*.
- **Deciding:** the moment they picked one. The deciding factor is rarely the feature matrix — it's often emotional or contextual (a dean sat in on the demo and said "buy it").
- **Consuming:** onboarding, migration, adoption. This is where anxiety becomes real — like realizing you have to re-enter a term of data by hand.

### How to walk the timeline

Open with: *"Tell me about the last time you switched from one [category] to another."* If they haven't switched, ask about the last time they seriously considered it. Then walk backward:

1. **Decision:** "What did you end up choosing? When was that? Who else was in the room?"
2. **Active looking:** "Before that, what else did you evaluate? How did you find them? What triggered you to go from annoyed to actively searching?"
3. **Passive looking:** "Before you were actively searching, were you aware alternatives existed? How long were you in that 'I know there's better but I'm not doing anything' phase?"
4. **First thought:** "Take me back to the very first moment you thought 'maybe I should look for something different.' What happened?"
5. **Consuming:** "After you decided, what was onboarding like? What was harder than expected?"

The trigger from passive to active is gold. It's usually a specific event — a missed deadline, a bad board meeting, a public embarrassment in front of a superintendent. Probe until you get the story. And shut up: the best interviewers talk about 20% of the time. Ask, then wait.

### Four interview contexts

Who you talk to changes the framing.

**Switched TO you.** The default. Reconstruct their full timeline and all four forces. This tells you why your wedge works and what almost stopped them.

**Switched AWAY (churned).** Flip the framing: the "old way" is your product, the "new thing" is whatever they left for. The push forces are your failures. Painful, and the most valuable interview you'll run. Add: "What would have kept you?" and "When did you first think about leaving?" Note that "too expensive" is almost never the real reason — a buyer who paid had already accepted the price. Dig past the excuse.

**Switched between competitors (not you).** They never considered you. You learn the forces in your category without your own product distorting the story. Ask what made them look, what they evaluated, and why you weren't on the list.

**Currently evaluating (hasn't decided).** Focus on the old way, the first thought, and push and pull. Skip "deciding" — it hasn't happened. Add: "What would need to be true for you to make a change?" and "What's stopping you right now?" The thing stopping them is your anxiety or habit force, live.

### Probe each force directly

The timeline surfaces some forces naturally. This fills the gaps.

- **Push:** "What was the most frustrating thing about the old way? Tell me about a specific time it let you down. What did that cost you?"
- **Pull:** "What first caught your attention? When you imagined using it, what did you picture being different?"
- **Anxiety:** "What almost stopped you? Was there a moment you nearly backed out?" Let silence sit. If they say "nothing," try "if you had to name one risk, even a small one…"
- **Habit:** "Was there anything about the old way you'd miss? Did anyone on your team resist? What workarounds did you have to give up?"

## Red flags

These tell you you're getting speculation, not memory. Redirect on the spot.

| Red flag | Sounds like | Redirect |
|----------|-------------|----------|
| **Hypothetical language** | "I would…", "I think I'd…" | "I want what actually happened. Take me back to that moment." |
| **Vague emotion** | "It was frustrating." | "Tell me about a specific time. What happened?" |
| **Category answer** | "We needed better analytics." | "What specifically couldn't you do? Walk me through the last time it was a problem." |
| **No dates or people** | "At some point we decided…" | "Was that before or after [event]? Who was in the room?" |
| **Feature list** | "It has dashboards and an API and…" | "Which mattered most to you? Why that one?" |
| **Pleasing you** | "Your product is great because…" | "I appreciate that, but I'm after the messy middle. What almost stopped you?" |

The big one is **"I would."** Hypothetical language means they're inventing an answer, not recalling a behavior. "I would definitely use a tool that does X" is a wish, not evidence. The same problem shows up in surveys: "would you use this" predicts nothing, while a count of people already hacking a workaround predicts everything (see [operator-lessons.md](https://github.com/savvides/edtechfounderstack/blob/800fcaf5fcc187b3ee3c35f4224cbcdc560548a6/data/operator-lessons.md)). Switch interviews are trustworthy precisely because they ask what someone *did*, in a setting where one buyer decides — which is exactly the institutional buying setup. "I surveyed eight teachers" is noise; the registrar who already runs a manual workaround is signal.

After three or more interviews, patterns emerge: the same push event, the same anxiety blocking the same buyers, the same habit you have to break. That repeated pattern — not any single story — is the job your product actually serves.

Switch interviews are the behavioral half of validating demand — the questions in [demand-validation.md](demand-validation.md) tell you whether the demand is real before the build; the timeline reconstruction here tells you the story behind it. For the structural reasons edtech founders mistake enthusiasm for demand, see [founder-traps.md](founder-traps.md). For the validated jobs to anchor your job stories against, see [higher-ed-jobs-atlas.md](higher-ed-jobs-atlas.md).

*Last updated: 2026-05-30*

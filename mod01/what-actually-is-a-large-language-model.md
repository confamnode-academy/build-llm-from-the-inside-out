# 01 — What Actually Is a Large Language Model?
Series: Building a Large Language Model From the Inside Out
Companion to blog post: "I Thought I Understood LLMs. Then I Asked What One Actually Does."
(academy.confamnode.com/blog/i-thought-i-understood-llms)

Tutorial URL: academy.confamnode.com/tutorials/what-actually-is-a-large-language-model

Repo folder: mod01

Note: Module 01 has no code, and this page isn't trying to invent any. It's the
structured, reference version of the ideas the blog post walks through narratively —
something to scan back to later, not a one-time read.

---

## What you'll understand by the end of this page

- What an LLM is actually trained to do — in one sentence
- Why "predict the next token" is enough to produce something that looks like understanding
- What self-supervised learning means, concretely
- What "loss" is, and what a wrong prediction actually looks like
- Where the Transformer and attention fit into this picture — and where they don't (yet)
- Why the scale and diversity of training data matters

### The one-sentence answer

Strip away everything else, and an LLM is trained to do exactly one thing: given the
tokens so far, predict the next one. Every other capability — answering questions,
summarizing, translating, holding a conversation — is a downstream consequence of a model
getting very good at that single task.

### Before LLMs: one model per job

Traditional NLP built a separate model for every task:

```
Email       -> spam classifier    -> SPAM / NOT SPAM
Review      -> sentiment model    -> POSITIVE / NEGATIVE
```

Each model was built and trained for its one job, and couldn't do anything else. An LLM
breaks that pattern — one model can classify a complaint, summarize it, and draft a reply,
without being separately trained for any of those three tasks. The natural question:
if it isn't trained separately for each task, how does it learn to do all of them?

### The training objective: next-token prediction

During pretraining, an LLM sees fragments of real text and is asked, at every single
position, to guess what comes next:

```
"I"              -> "dey"
"I dey"          -> "go"
"I dey go"       -> "Lagos"
"I dey go Lagos" -> "tomorrow"
```

Nobody labels any of this by hand. The next actual word in the real text **is** the
label — the text supplies its own answer key. That's what self-supervised learning
means: the supervision comes from the structure of the data itself, not from a human
annotator.

### Why something this simple produces real language ability

This is the part that isn't obvious on first encounter: predicting the next word sounds
almost too basic to matter. But predicting it *well* turns out to require actually
understanding quite a lot.

Consider: "The POS stopped working because there was no ___."

Getting "network" right — rather than some unrelated word — requires the model to have
picked up a real association between POS machines and network connectivity, purely from
having seen enough examples where those concepts co-occur. Nobody programmed that
association in. It's a side effect of needing to predict correctly, over and over, across
enormous amounts of text.

```
Massive text -> next-token prediction -> forced to learn real language
patterns to do that well -> better predictions -> capabilities that
look like understanding
```

The objective is one sentence. What it takes to actually satisfy that objective, at
scale, is where all the complexity lives.

### What "being wrong" actually looks like

Given the text "I transferred ₦50,000 but the money," a model might distribute its
guesses like this:

```
entered   70%
arrived   15%
never      5%
worked     5%
```

If the real next word is "never," the model was confidently wrong. That gap between what
it predicted and what actually came next is called the **loss**. Training is the repeated
loop of: predict, measure how wrong, adjust the model's internal numbers slightly, repeat —
billions of times, until "a little less wrong" compounds into fluency.

### Where the Transformer and attention actually fit

Worth being precise about something that's easy to blur: **next-token prediction is the
objective. The Transformer is the architecture that processes the token sequence and
produces the prediction.** They are not the same thing — the objective is the "what,"
the Transformer is the "how."

The Transformer's core mechanism is **attention**: the ability to weigh some earlier
tokens as more relevant than others when processing a given token, instead of treating
everything in the context equally. Take a genuinely ambiguous sentence:

> "Chinedu sent Emeka ₦100,000 because he was owed money."

Who does "he" refer to? Resolving that requires weighing which earlier words — Chinedu,
Emeka, sent, owed — actually bear on the pronoun. That weighing process is what attention
does. The full mechanics (query, key, value, attention scores) are covered in Chapter 3 —
for now, the intuition is the important part: attention lets the model decide what context
matters, rather than treating the whole input equally.

### Why data scale and diversity matter

Train on a narrow slice of text, and the model only has a narrow slice of patterns to
learn from. Train on a large and varied mix — different topics, registers, formal English,
Pidgin, code — and the model gets far more exposure to how language actually behaves
across contexts.

This diversity isn't sorted into separate goals like "learn translation" or "learn
Pidgin." The objective never changes: predict the next token. Scale and diversity are what
let abilities like translation, summarization, and handling informal registers *emerge*
from that one unchanged objective, without ever being explicitly taught as separate
skills.

### One important limit, before moving on

Pretraining alone produces a model that's good at predicting text — not a model that's
good at *helping* someone. A freshly pretrained model won't reliably give a polite,
accurate reply to a customer, or refuse to make things up. That takes additional stages —
instruction tuning and preference training — which come later in this series (Chapters
6–7).

---

## Summary

- An LLM's entire training objective is next-token prediction, given everything before it.
- No human labels the training data — the next real word in the text is the label
  (self-supervised learning).
- Predicting well, at scale, forces the model to pick up real patterns of grammar,
  meaning, and context as a side effect.
- Loss measures the gap between a prediction and what actually came next; training is the
  repeated process of shrinking that gap.
- The Transformer is the architecture that produces the prediction; attention is its core
  mechanism for weighing which earlier tokens matter.
- Scale and diversity of training data are what let capabilities emerge from one fixed
  objective — they are not optional extras.
- Pretraining alone doesn't produce a helpful assistant — that takes further stages
  covered later in this series.

[Continue to Module 2 — Handling Text Data →](academy.confamnode.com/tutorials/handling-text-data)

[Read the narrative version this page is built from →](academy.confamnode.com/blog/i-thought-i-understood-llms)
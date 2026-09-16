# Building a Large Language Model From the Inside Out

> **Understanding and building LLMs from first principles, one concept at a time.**

This repository is a hands-on learning and implementation journey into the inner workings of Large Language Models (LLMs).

Rather than treating an LLM as a black box, we progressively break down the components that make modern language models work — from handling raw text and tokenization to embeddings, attention, Transformers, and eventually a working GPT-style language model.

The goal is not just to **use** LLMs, but to understand **how they work and how to build them**.

---

## What You'll Learn

Throughout this series, we will progressively explore:

- How language models learn from text
- Next-token prediction
- Training objectives and loss
- Text tokenization and vocabulary
- Token IDs and embeddings
- Positional information
- Attention mechanisms
- Self-attention
- Causal attention
- Transformer architecture
- GPT-style language models
- Pretraining
- Instruction fine-tuning
- Model evaluation
- Other fundamental concepts behind modern LLMs

Each chapter introduces a concept, develops the intuition behind it, and then moves toward a practical implementation.

---

## Modules

| Module | Topic | Status |
|---|---|---|
| 01 | [What Actually Is a Large Language Model?](./mod01/what-actually-is-a-large-language-model.md) | ✅ Completed |

More chapters will be added as the series progresses.

---

## Learning Philosophy

The approach is simple:

```text
Understand
    ↓
Implement
    ↓
Experiment
    ↓
Explain
    ↓
Build
```

The objective is to develop a strong mental model of what is happening inside an LLM rather than simply reproducing code from a framework or tutorial.

Whenever possible, concepts are explored through small experiments before being combined into larger systems.

---

## Why This Repository?

Modern LLMs can feel like complicated black boxes.

Libraries such as PyTorch, Transformers, vLLM, and other frameworks make it possible to use powerful models with relatively little code — but abstraction can sometimes hide the underlying mechanics.

This project takes the opposite approach.

We progressively move closer to the underlying computation:

```text
Human Language
      ↓
Text Processing
      ↓
Tokens
      ↓
Token IDs
      ↓
Embeddings
      ↓
Attention
      ↓
Transformer
      ↓
GPT
      ↓
Language Model
```

By the end of the journey, the goal is to understand what each stage is doing and how the pieces fit together.

---

## Nigerian Context

Where appropriate, the tutorials use Nigerian English, Nigerian Pidgin, and familiar Nigerian contexts to make abstract concepts more concrete.

For example:

```text
Abeg, my transfer never enter.
```

and:

```text
The POS stopped working because there was no network.
```

These examples are used to investigate concepts such as language modeling, tokenization, and representation while keeping the learning experience grounded in language and situations that are familiar to us.

---

## Companion Content

This repository is part of the **Building a Large Language Model From the Inside Out** series by **JoTeq the First**.

📖 **Articles:** [ConfamNode Academy](https://academy.confamnode.com/blog)  
🎥 **YouTube:** [JoTeq the First](https://youtube.com/@josaikono)

The articles provide the conceptual explanations, while the notebooks provide the hands-on implementation.

---

## References

The series draws inspiration from established resources on deep learning, natural language processing, and large language models, including:

- *Build a Large Language Model (From Scratch)* — Sebastian Raschka
- *Stanford CME295 Transformers & LLMs | Autumn 2025* — Stanford Online
- *AI Engineering* — Chip Huyen
- Research papers and technical reports from the broader LLM research community

This repository is an independent learning and implementation project. It is not an official implementation of any of the referenced books or projects.

---

## License

The code and original implementations in this repository are licensed under the [Apache-2.0 License](./LICENSE).

Third-party datasets, texts, and other referenced materials remain subject to their respective licenses and terms.
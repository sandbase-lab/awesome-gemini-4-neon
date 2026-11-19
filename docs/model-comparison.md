# Gemini 4 Neon vs GPT-6.2 Sol, Gemini 4 Carbon, Gemini 4 Argon and Claude Opus 5.5

English · [简体中文](zh-CN/model-comparison.md) · [← Back to the collection](../README.md)

Two kinds of evidence, kept apart:

1. **What we measured.** The Lab [Evals boards][evals] show Artificial Analysis data, and the Lab [Pelican Test][pelican] runs the same fixed prompt on every model and scores the result. Small samples, but the same conditions for everyone.
2. **What creators reported.** Posts on X with their own prompts, costs and numbers. Useful context, not verified by us.

Gemini 4 Neon was announced on November 18, 2026. The measured side has no Neon result yet, and the creator side is small: the collection has 35 posts, 7 of them tagged as comparisons, and 6 that share a prompt.

## What we measured: Lab Evals boards and Pelican Test

**There is no Gemini 4 Neon row in the Evals or Pelican Test data this list was built from.** We have not re-read the live boards for this build, so check the [Evals boards][evals] and [Pelican Test][pelican] for a newer row. The tables below are rival rows from the sibling Gemini list's model comparison, so you can see where the field stood before Neon. They are not Neon results.

Evals boards, Artificial Analysis snapshot of 2026-10-19:

| Model (row on the board) | Intelligence Index | Cost per task |
|---|---|---|
| **Gemini 4 Neon** | **not in this data** | — |
| Claude Opus 5.5 (Max) | 57.6 (#1) | $5.98 (#188) |
| Gemini 4 Argon (High) | 52.6 (#9) | $1.99 (#158) |
| DeepSeek V4.1 Flash 1017 (Max) | 45.1 (#36) | $0.262 (#74) |

Pelican Test, leaderboard read 2026-10-20:

| Rank | Model | Results | Score | Avg cost |
|---|---|---|---|---|
| — | **google/gemini-4-neon** | **none in this data** | — | — |
| 2 | google/gemini-4-argon | 4 | 3.75 | $0.150 |
| 4 | anthropic/claude-opus-5.5 | 6 | 3.46 | $0.223 |
| 5 | deepseek/deepseek-v4.1-flash | 6 | 3.44 | $0.017 |

What this says, and what it doesn't:

- **Nothing about Neon's score.** Both snapshots predate Neon's announcement by about a month. Until a Lab board or the Pelican Test lists it, every claim about where Neon ranks comes from a creator.
- **Argon is the one Gemini model on both boards.** It is the natural row to compare against once Neon has one.

## What creators reported

Same-prompt posts on X. Numbers are as the creator stated them: different settings, often one run. Click through to see both results.

| Creator | Task | Gemini 4 Neon | Rival | Creator's words |
|---|---|---|---|---|
| [@jan_volad][jan] | "Build a huge haunted vampire cathedral", same prompt | $2.67 | GPT-6.2 Sol: $1.69 | "Honestly can't pick a winner, which one would you take?" |
| [@analogalok][analogalok] | Neon vs Gemini 4 Carbon, one prompt, one HTML file, pure Three.js | no cost in post | Gemini 4 Carbon | "Genuinely looks like Google Earth until you remember an LLM just one shotted the code." |
| [@DesignArena][designarena] | Mont Blanc ski simulator setting, Neon and Gemini 4 Argon | pricing only: $3 input, $15 output, $0.15 cached input per million | Gemini 4 Argon | Platform announcement; the visible text has no result |
| [@cfenghub][cfenghub] | Three.js + GLSL page | 2 min 40 s | — | Prompt in the reply thread |
| [@tspy][tspy] | Pelican riding a bicycle, Three.js 3D scene | — | — | "My pelican looks a bit strange!" (translated) |

Claims in the posts that we have not checked:

- [@analogalok][analogalok] quotes Artificial Analysis Intelligence Index figures: Neon 61, up from Carbon's 60, against Opus 5.5 at 59 and GPT-6.2 Astra at 62. These are the creator's numbers. We have not matched them to the Lab Evals boards.

What this says:

- **One priced pair.** On the cathedral prompt, the Neon run cost $2.67 and the Sol run $1.69: $0.98 more for Neon, on one run each.
- **No verdict.** The one creator who ran both sides could not pick a winner.

## Rerun before you trust a comparison

Results move with the setup, and the creator figures above are one run each. Paste the prompt into the [Lab text arena][arena] with Gemini 4 Neon and a rival selected, or see the [tutorial](tutorial.md).

## More measurements

- [Lab Evals boards][evals]: Artificial Analysis data. Search for "Gemini 4 Neon" to see whether a row has appeared since this list was built.
- [Lab Pelican Test][pelican]: same prompt on every model, scored the same way, with the drawings on screen.
- [All AI video collections on SandBase Lab][collections], including the sibling lists [Gemini 4 Argon](https://github.com/sandbase-lab/awesome-gemini4-argon) and [DeepSeek V4.1 Flash 1017](https://github.com/sandbase-lab/awesome-deepseek-v4.1-flash).

---

Lab data: [Evals boards][evals] (Artificial Analysis, snapshot 2026-10-19) and [Pelican Test][pelican] (read 2026-10-20), both taken from the sibling Gemini list and not re-read for this build. Creator data: their posts, linked; not independently verified.

[evals]: https://www.sandbase.ai/leaderboards?utm_source=github&utm_medium=docs&utm_campaign=awesome-gemini-4-neon
[pelican]: https://www.sandbase.ai/arena/pelican-test?utm_source=github&utm_medium=docs&utm_campaign=awesome-gemini-4-neon
[arena]: https://www.sandbase.ai/arena/text?models=google%2Fgemini-4-neon&utm_source=github&utm_medium=docs&utm_campaign=awesome-gemini-4-neon
[collections]: https://www.sandbase.ai/lab/ai-videos?utm_source=github&utm_medium=docs&utm_campaign=awesome-gemini-4-neon
[jan]: https://x.com/jan_volad/status/2123205954649100424
[analogalok]: https://x.com/analogalok/status/2123183353436475636
[designarena]: https://x.com/DesignArena/status/2123220446074253768
[cfenghub]: https://x.com/cfenghub/status/2123162154132242885
[tspy]: https://x.com/tspy/status/2123222507977375770

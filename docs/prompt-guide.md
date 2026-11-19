# Gemini 4 Neon prompt guide: how to prompt Gemini 4 Neon for video

English · [简体中文](zh-CN/prompt-guide.md) · [← Back to the collection](../README.md)

Gemini 4 Neon doesn't output video. In the posts here it writes code — a self-contained web page built with Three.js or GLSL — and the creator records that page playing. The patterns below come from the prompts creators shared with their posts, and from how creators described their builds. Each one links to the post it came from.

There are four patterns because the prompts shared so far support four. Only three of the six posts with a shared prompt quote its text; the others describe the build, or put the prompt in a reply. This guide grows as more creators share prompts.

## 1. Name the file and the renderer

Say what you want back and what draws it. The three builds posted so far all do this:

- "使用 Three.js 创作一个“一只正在骑自行车的鹈鹕”的3D互动网页场景，直接输出完整可运行的单文件HTML代码。" (Use Three.js to create a 3D interactive web scene of "a pelican riding a bicycle", and output the complete, runnable single-file HTML code directly.) ([@tspy][tspy], translated)
- "One prompt. One HTML file. Pure Three.js." ([@analogalok][analogalok]), in the creator's own words about their build.
- "Three.js + GLSL 代码直出 耗时 2分40秒" (Three.js and GLSL, code output directly, 2 min 40 s) ([@cfenghub][cfenghub], translated). The post says the prompt is in the replies.

Naming the renderer decides what the page is built from. Three.js and GLSL are the two named here.

## 2. Keep the brief to one subject

Two of the prompts shared on this list are one line each, and each names one subject:

- "Make a pelican SVG" ([@Inmerson][inmerson]), with the question of whether the result is Gemini 4 Neon.
- "Build a huge haunted vampire cathedral" ([@jan_volad][jan]).

One subject gives the page one thing to build. The posts don't show a longer version of either prompt, so there is no measured comparison of short and long briefs here.

## 3. Run one prompt on several models

Creators put the same prompt through Neon and a rival, then compare the results and the bill:

- "Gemini 4 Neon vs GPT-6.2 Sol, same prompt: 'Build a huge haunted vampire cathedral'. Neon $2.67, Sol $1.69. Honestly can't pick a winner" ([@jan_volad][jan]).
- "Gemini 4 Neon vs. Gemini 4 Carbon. One prompt. One HTML file." ([@analogalok][analogalok]).

Keep the prompt identical across models, so the only difference is the model. The cost is in the bill; the quality call is yours. Each comparison is a single run.

## 4. Reuse a launch-day scene as a fixed test

At launch, Google DeepMind showed Gemini 4 Neon building a Mont Blanc ski simulator. DesignArena then gave Neon and Gemini 4 Argon a similar setting to compare ([@DesignArena][designarena]). A scene you keep reusing works like the Lab Pelican Test does for one drawing: the same brief on every model, so you can compare the pages over time as well as side by side.

## Settings

- **Output budget.** Output tokens bill at $15 per million, so a long page costs more than a short one. The [tutorial](tutorial.md) sets `max_tokens` to 128,000 in its API example. The model's own output limit is not in this list's data; `sandbase inspect google/gemini-4-neon` shows it.
- **Settings and harnesses.** None of the posts here names a reasoning setting or a coding harness, so none of these patterns depends on one.

## A prompt to start from

```text
Build [subject] as ONE self-contained HTML file.

Renderer: [Three.js or GLSL].
Scene: [what is on screen, style, lighting, colors].
Motion: [what moves and how; autoplay a [10]-second camera move, then loop].
Interaction: [mouse or keys, or none].
Rules: [numbers the scene must respect].

No external images, fonts or audio: build everything in code.
Return the complete HTML, from <!DOCTYPE html> to </html>, and nothing else.
```

Try it in the [Lab text arena][arena] with Gemini 4 Neon selected, or with the API in the [tutorial](tutorial.md).

---

Quotes are short excerpts credited to their authors; follow the links for the full posts. Translations from Chinese are ours.

[analogalok]: https://x.com/analogalok/status/2123183353436475636
[cfenghub]: https://x.com/cfenghub/status/2123162154132242885
[tspy]: https://x.com/tspy/status/2123222507977375770
[jan]: https://x.com/jan_volad/status/2123205954649100424
[inmerson]: https://x.com/Inmerson/status/2122954421050933355
[designarena]: https://x.com/DesignArena/status/2123220446074253768
[arena]: https://www.sandbase.ai/arena/text?models=google%2Fgemini-4-neon&utm_source=github&utm_medium=docs&utm_campaign=awesome-gemini-4-neon

# Gemini 4 Neon tutorial: from prompt to video

English · [简体中文](zh-CN/tutorial.md) · [← Back to the collection](../README.md)

From a prompt to an MP4 in four steps. Gemini 4 Neon writes a web page; you play it and record it.

## 1. Start from a video you like

Open any title in the [collection](../README.md) to reach its page on [SandBase Lab][lab]: the video, the original post and, when the creator shared one, the prompt. Press **Recreate**. Lab opens the text arena with the post loaded and Gemini 4 Neon selected. Sign in, run it, and you get the HTML back, with a live preview.

No prompt shared? Write one with the [prompt guide](prompt-guide.md). It has a fill-in template.

## 2. Compare models on the same prompt

In the [text arena][arena], add one or two more models next to Gemini 4 Neon, for example GPT-6.2 Sol or Gemini 4 Argon, and run once. That is how the creator in [this post][jan] compared Neon with GPT-6.2 Sol on one prompt: $2.67 for Neon, $1.69 for Sol, and no clear winner. It is also the quickest way to check a claim from the [comparison page](model-comparison.md) on your own task.

## 3. Or call the API

Gemini 4 Neon is `google/gemini-4-neon` on SandBase, OpenAI-compatible. It was announced on November 18, 2026.

1. Create a key in the [console][keys] and export it: `export SANDBASE_API_KEY=<your key>`
2. Save your prompt as `prompt.txt`.
3. Run:

```bash
jq -n --rawfile prompt prompt.txt '{
  model: "google/gemini-4-neon",
  max_tokens: 128000,
  messages: [{role: "user", content: $prompt}]
}' |
curl -sS --max-time 900 https://api.sandbase.ai/v1/chat/completions \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d @- > response.json

jq -r '.choices[0].message.content' response.json | sed '/^```/d' > gemini-4-neon.html
jq '.usage' response.json
```

- `max_tokens: 128000`: the ceiling for the reply, and output bills at $15 per million tokens. A page needs room to finish, or you get a truncated file and still pay for the tokens. The model's own limit is not in this list's data; `sandbase inspect google/gemini-4-neon` shows it.
- `--max-time 900`: a page can take a while. One creator reported 2 min 40 s for a Three.js and GLSL page ([@cfenghub][cfenghub]), so give the call room.
- `sed '/^```/d'` removes Markdown fences if the model added them.
- `usage` shows what you were billed for. Input is $3 per million tokens, output $15 per million, and cached input $0.15 per million. The cost of one call is (prompt tokens × $3 + completion tokens × $15) ÷ 1,000,000 dollars. The [model page][model] has the prices.

Open `gemini-4-neon.html` in a browser. If it is blank, open the developer console: the usual causes are a truncated file (raise `max_tokens`) or a CDN that did not load (ask for everything inline).

### With the SandBase CLI

The same call through the [SandBase CLI](https://www.npmjs.com/package/@sandbaseai/cli), which reads `SANDBASE_API_KEY` as well:

```bash
npx -y @sandbaseai/cli@latest inspect google/gemini-4-neon   # input fields and price, free
jq -n --rawfile prompt prompt.txt '{max_tokens: 128000, messages: [{role: "user", content: $prompt}]}' > input.json
npx -y @sandbaseai/cli@latest run sandbase_google_gemini_4_neon -f input.json --timeout 900 -o result.json
```

`-o result.json` saves the response; the page is in the assistant message, as with the API.

## 4. Turn the page into a video

You can screen-record the page yourself. To get the same clip every time, record it headlessly with [`scripts/record.mjs`](../scripts/record.mjs):

```bash
npm i -D playwright@1.56.1
npx playwright install chromium          # or use your installed Chrome: export RECORD_CHANNEL=chrome
node scripts/record.mjs gemini-4-neon.html gemini-4-neon.mp4 12 1920 1080   # 12 seconds at 1080p
```

It opens the page at the size you give, records for that many seconds, and converts to H.264 MP4 with ffmpeg. For a clean result, ask in the prompt for an autoplay camera move or a fixed-length loop (see [prompt guide, pattern 4](prompt-guide.md#4-reuse-a-launch-day-scene-as-a-fixed-test)), so nothing depends on a mouse.

The recording is picture only. Add audio in the edit.

## Run generated code safely

The HTML is code you haven't read. Opening it from disk is usually fine for a single-file page, but it can still load scripts and make network requests. For anything you don't trust, or to run many pages automatically, use a [SandBase Sandbox][sandbox]: an isolated environment with a time limit and no access to your files or keys.

## Share it

Post your video on X with the prompt and mention Gemini 4 Neon. To have it added here, [submit it](https://github.com/sandbase-lab/awesome-gemini-4-neon/issues/new?template=submit-video.yml); accepted posts go into the Lab collection and show up in this list on the next daily sync.

[lab]: https://www.sandbase.ai/lab/ai-videos/gemini-4-neon?utm_source=github&utm_medium=docs&utm_campaign=awesome-gemini-4-neon
[arena]: https://www.sandbase.ai/arena/text?models=google%2Fgemini-4-neon&utm_source=github&utm_medium=docs&utm_campaign=awesome-gemini-4-neon
[keys]: https://www.sandbase.ai/console/keys?utm_source=github&utm_medium=docs&utm_campaign=awesome-gemini-4-neon
[model]: https://www.sandbase.ai/model/google/gemini-4-neon?utm_source=github&utm_medium=docs&utm_campaign=awesome-gemini-4-neon
[sandbox]: https://www.sandbase.ai/landing/sandbox?utm_source=github&utm_medium=docs&utm_campaign=awesome-gemini-4-neon
[jan]: https://x.com/jan_volad/status/2123205954649100424
[cfenghub]: https://x.com/cfenghub/status/2123162154132242885

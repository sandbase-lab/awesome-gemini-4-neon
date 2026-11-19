# Gemini 4 Neon 教程：从提示词到视频

[English](../tutorial.md) · 简体中文 · [← 返回合集](../../README.zh-CN.md)

四步把提示词变成 MP4。Gemini 4 Neon 写网页，你来播放并录制。

## 1. 从喜欢的视频开始

在[合集](../../README.zh-CN.md)里点任意标题，进入它在 [SandBase Lab][lab] 的页面：视频、原帖，以及作者公开的提示词（如果有）。点 **复刻**，Lab 会打开文本竞技场，自动填好帖子内容并选中 Gemini 4 Neon。登录后运行，就能拿到 HTML，并带实时预览。

作者没有公开提示词？照[提示词写法](prompt-guide.md)自己写一条，里面有填空模板。

## 2. 用同一个提示词对比模型

在[文本竞技场][arena]里，在 Gemini 4 Neon 旁边再加一两个模型，例如 GPT-6.2 Sol 或 Gemini 4 Argon，跑一次。[这条帖子][jan]的作者就是这样用同一个提示词对比 Neon 和 GPT-6.2 Sol 的：Neon 花费 $2.67，Sol 花费 $1.69，作者说分不出哪个更好。这也是在你自己的任务上验证[对比页](model-comparison.md)结论的最快方式。

## 3. 或者直接调用 API

Gemini 4 Neon 在 SandBase 上的模型 ID 是 `google/gemini-4-neon`，兼容 OpenAI。它于 2026 年 11 月 18 日宣布。

1. 在[控制台][keys]创建 Key 并导出：`export SANDBASE_API_KEY=<你的 Key>`
2. 把提示词保存为 `prompt.txt`。
3. 运行：

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

- `max_tokens: 128000`：回复的上限。输出按每百万 token $15 计费。如果上限太小，页面会被截断，而费用照样要付。
- `--max-time 900`：一个页面可能要跑一阵子。有作者报告 Three.js + GLSL 直出耗时 2 分 40 秒（[@cfenghub][cfenghub]），所以给调用留足时间。
- `sed '/^```/d'` 去掉模型可能加上的 Markdown 代码围栏。
- `usage` 显示你被计费的用量。输入每百万 token $3，输出每百万 $15，缓存的输入每百万 $0.15。一次调用的费用为（输入 token × $3 + 输出 token × $15）÷ 1,000,000 美元。价格见[模型页][model]。

用浏览器打开 `gemini-4-neon.html`。如果一片空白，打开开发者工具：常见原因是被截断的文件（加大 `max_tokens`），或页面依赖的外部资源没有加载（尽量让所有资源内联）。

### 用 SandBase CLI

同一个模型也可以用 [SandBase CLI](https://www.npmjs.com/package/@sandbaseai/cli) 调用，工具名为 `sandbase_google_gemini_4_neon`：

```bash
npx -y @sandbaseai/cli run sandbase_google_gemini_4_neon --help
```

运行 `--help` 查看参数格式，再按 `max_tokens: 128000` 和你的提示词填写。响应里的页面与 API 相同，在 assistant 消息中。

## 4. 把页面录成视频

你可以自己录屏。想每次得到一样的片段，可以用 [`scripts/record.mjs`](../../scripts/record.mjs)：

```bash
node scripts/record.mjs gemini-4-neon.html gemini-4-neon.mp4 12 1920 1080   # 12 秒，1080p
```

参数依次为：HTML 文件、输出 MP4、录制秒数、宽、高。想要干净的效果，就在提示词里要求自动镜头移动或定长循环（见[提示词写法 §4](prompt-guide.md#4-把发布当天的场景当固定测试)），让整个画面不依赖鼠标。

## 安全运行生成的代码

这段 HTML 是你没读过的代码。单文件页面从本地打开通常没问题，但它仍然可以加载脚本、发起网络请求。对于不完全信任的内容，或者要批量运行很多页面，请使用 [SandBase Sandbox][sandbox]：一个隔离环境，接触不到你的本地文件和 Key。

## 分享

把视频发到 X，附上提示词并 @ Gemini 4 Neon。想被收录，就[提交给我们](https://github.com/sandbase-lab/awesome-gemini-4-neon/issues/new?template=submit-video.yml)。

[lab]: https://www.sandbase.ai/lab/ai-videos/gemini-4-neon?utm_source=github&utm_medium=docs&utm_campaign=awesome-gemini-4-neon
[arena]: https://www.sandbase.ai/arena/text?models=google%2Fgemini-4-neon&utm_source=github&utm_medium=docs&utm_campaign=awesome-gemini-4-neon
[keys]: https://www.sandbase.ai/console/keys?utm_source=github&utm_medium=docs&utm_campaign=awesome-gemini-4-neon
[model]: https://www.sandbase.ai/model/google/gemini-4-neon?utm_source=github&utm_medium=docs&utm_campaign=awesome-gemini-4-neon
[sandbox]: https://www.sandbase.ai/landing/sandbox?utm_source=github&utm_medium=docs&utm_campaign=awesome-gemini-4-neon
[jan]: https://x.com/jan_volad/status/2123205954649100424
[cfenghub]: https://x.com/cfenghub/status/2123162154132242885

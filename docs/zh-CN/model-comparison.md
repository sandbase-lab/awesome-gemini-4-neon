# Gemini 4 Neon 模型对比

[English](../model-comparison.md) · 简体中文 · [← 返回合集](../../README.zh-CN.md)

这一页分两类证据，互不混用：

- **Lab 测得的数据**：SandBase 的评测与基准数据。
- **创作者报告的数据**：作者在 X 上发布的内容。这些是单次运行的结果，不是对照实验。

## Lab 测得的数据

下面的表格来自 SandBase 数据快照。Gemini 4 Neon 的编程评测成绩不在本次数据中，因此表中没有它的行。

**Evals（编程/综合评测，快照 2026-10-19）**

| 模型 | 分数 | 排名 | 每百万输出 token |
| --- | ---: | ---: | ---: |
| Gemini 4 Neon | 不在本次数据中 | — | $15 |
| Claude Opus 5.5 | 57.6 | #1 | $5.98 |
| Gemini 4 Argon | 52.6 | #9 | $1.99 |
| DeepSeek V4.1 Flash | 45.1 | #36 | $0.262 |

**Pelican 测试（快照 2026-10-20）**

| 模型 | 分数 | 说明 |
| --- | ---: | --- |
| Gemini 4 Neon | 不在本次数据中 | — |
| Gemini 4 Argon | 3.75 | 同为 Gemini 系列 |
| Claude Opus 5.5 | 3.46 | — |
| DeepSeek V4.1 Flash | 3.44 | — |

以上两个快照都是 SandBase 对其他模型的测量，Gemini 4 Neon 没有对应行。你可以在 [Evals 排行榜](https://www.sandbase.ai/leaderboards?utm_source=github&utm_medium=docs&utm_campaign=awesome-gemini-4-neon)和 [Pelican 测试](https://www.sandbase.ai/arena/pelican-test?utm_source=github&utm_medium=docs&utm_campaign=awesome-gemini-4-neon)查看实时数据，那里的数字可能比这里更新。

Gemini 4 Argon 是这两个快照里唯一的 Gemini 模型，因此它是最接近的参照。

## 创作者报告的数据

这些是 X 帖子里的内容，每条都是单次运行，不构成可靠的排名依据。

| 作者 | 对比 | 他们说了什么 |
| --- | --- | --- |
| [@jan_volad][jan] | Neon vs GPT-6.2 Sol，同一提示词"Build a huge haunted vampire cathedral" | Neon $2.67，Sol $1.69；作者说分不出哪个更好 |
| [@analogalok][analogalok] | Neon vs Gemini 4 Carbon，同一提示词、单个 Three.js HTML | 作者认为画面"像 Google Earth"；帖子中提到 Neon 在 Artificial Analysis 智能指数上得 61（Carbon 为 60） |
| [@DesignArena][designarena] | 在 DesignArena 上比较 Neon 与 Argon，"Mont Blanc 滑雪模拟器"场景 | 同一设定，两个模型分别生成 |
| [@cfenghub][cfenghub] | Three.js + GLSL 代码直出 | 耗时 2 分 40 秒 |
| [@tspy][tspy] | Neon Extra 生成"骑自行车的鹈鹕" 3D 场景 | 作者称鹈鹕"看上去好像有点奇怪" |
| [@Inmerson][inmerson] | 提示词"Make a pelican SVG" | 作者问"这是 Gemini 4 Neon 吗？" |

注意：analogalok 帖子中的 Artificial Analysis 指数数字（61 / 60 / 59 / 62）尚未在 Lab 数据中核实，请勿当作已验证的结果引用。

## 如何使用这些数据

- 想要可比较的数字，看 Lab 测得的部分，并去实时排行榜确认。
- 想知道某个具体任务上的表现，用同一个提示词跑一遍（见[教程 §2](tutorial.md#2-用同一个提示词对比模型)）。
- 上面的创作者结果都是单次运行，换一次提示词或一次随机种子，结果可能不同。

[jan]: https://x.com/jan_volad/status/2123205954649100424
[analogalok]: https://x.com/analogalok/status/2123183353436475636
[designarena]: https://x.com/DesignArena/status/2123220446074253768
[cfenghub]: https://x.com/cfenghub/status/2123162154132242885
[tspy]: https://x.com/tspy/status/2123222507977375770
[inmerson]: https://x.com/Inmerson/status/2122954421050933355

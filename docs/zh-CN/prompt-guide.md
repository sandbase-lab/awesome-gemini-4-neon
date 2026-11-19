# Gemini 4 Neon 提示词写法：如何为视频提示 Gemini 4 Neon

[English](../prompt-guide.md) · 简体中文 · [← 返回合集](../../README.zh-CN.md)

Gemini 4 Neon 不直接输出视频。这里的作品里，它写的是代码——用 Three.js 或 GLSL 做的独立网页——作者再把页面播放过程录下来。下面的写法来自作者随视频公开的提示词，以及作者对自己作品的描述。每条都链接到它来自的帖子。

这里只有 4 条写法，因为目前公开的提示词只能支撑 4 条。在带公开提示词的 6 条帖子里，只有 3 条引用了提示词原文；其他的要么描述作品，要么把提示词放在回复里。随着更多作者公开提示词，这份指南会继续增加。

## 1. 说清楚要什么文件，用什么渲染

点明要返回的内容和用来绘制的技术。目前发布的三个作品都是这样做的：

- "使用 Three.js 创作一个“一只正在骑自行车的鹈鹕”的3D互动网页场景，直接输出完整可运行的单文件HTML代码。"（[@tspy][tspy]）
- "One prompt. One HTML file. Pure Three.js."（[@analogalok][analogalok]），是作者对自己作品的描述。
- "Three.js + GLSL 代码直出 耗时 2分40秒"（[@cfenghub][cfenghub]）。帖子说提示词在回复里。

点明渲染方式，决定了页面用什么搭建。这里点名的是 Three.js 和 GLSL。

## 2. 需求只写一个主体

本列表公开的提示词里，有两条只有一行，且各只写了一个主体：

- "Make a pelican SVG"（[@Inmerson][inmerson]），附带的问题是结果是不是 Gemini 4 Neon。
- "Build a huge haunted vampire cathedral"（[@jan_volad][jan]）。

一个主体，让页面只需要搭一样东西。这些帖子里没有这两条提示词的更长版本，所以这里没有关于长短需求的实测对比。

## 3. 同一个提示词跑多个模型

作者把同一个提示词分别交给 Neon 和对手模型，然后比较结果和账单：

- "Gemini 4 Neon vs GPT-6.2 Sol, same prompt: 'Build a huge haunted vampire cathedral'. Neon $2.67, Sol $1.69. Honestly can't pick a winner"（[@jan_volad][jan]）。
- "Gemini 4 Neon vs. Gemini 4 Carbon. One prompt. One HTML file."（[@analogalok][analogalok]）。

每个模型的提示词保持一致，这样差别只来自模型本身。花费体现在账单上；质量由你自己判断。每组对比都只是单次运行。

## 4. 把发布当天的场景当固定测试

发布时，Google DeepMind 展示了 Gemini 4 Neon 搭建一个勃朗峰滑雪模拟器。随后 DesignArena 给 Neon 和 Gemini 4 Argon 设置了相近的场景来对比（[@DesignArena][designarena]）。反复使用同一个场景，效果类似 Lab 的 Pelican Test 对一幅画的做法：每个模型拿到同样的需求，既可以并排比较，也可以随时间比较。

## 参数设置

- **输出预算。** 输出 token 按每百万 $15 计费，所以长页面比短页面贵。[教程](tutorial.md)的 API 示例把 `max_tokens` 设为 128000。这个模型自身的输出上限不在本列表的数据里，可运行 `sandbase inspect google/gemini-4-neon` 查看。
- **推理设置与 harness。** 这里的帖子都没有提到推理设置或编码 harness，因此上面的写法都不依赖它们。

## 可以直接用的提示词

```text
把 [主题] 做成一个独立的 HTML 文件。

渲染：[Three.js 或 GLSL]。
画面：[屏幕上有什么，风格，光照，配色]。
运动：[什么在动、怎么动；加载后自动播放 [10] 秒的镜头移动，然后循环]。
交互：[鼠标或按键，或无]。
规则：[场景必须遵守的数字]。

不要外部图片、字体或音频：所有内容都用代码生成。
只返回完整的 HTML，从 <!DOCTYPE html> 到 </html>，不要其他内容。
```

可以到 [Lab 文本竞技场][arena] 里选中 Gemini 4 Neon 运行，也可以按[教程](tutorial.md)用 API。

---

引文均为短摘录并注明作者，完整帖子请点链接。中文原文的翻译为我们所做。

[analogalok]: https://x.com/analogalok/status/2123183353436475636
[cfenghub]: https://x.com/cfenghub/status/2123162154132242885
[tspy]: https://x.com/tspy/status/2123222507977375770
[jan]: https://x.com/jan_volad/status/2123205954649100424
[inmerson]: https://x.com/Inmerson/status/2122954421050933355
[designarena]: https://x.com/DesignArena/status/2123220446074253768
[arena]: https://www.sandbase.ai/arena/text?models=google%2Fgemini-4-neon&utm_source=github&utm_medium=docs&utm_campaign=awesome-gemini-4-neon

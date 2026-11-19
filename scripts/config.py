"""Every model-specific value for this list. The other scripts are generic and read from here."""
import os

ORIGIN = os.environ.get('LAB_ORIGIN', 'https://www.sandbase.ai').rstrip('/')
SITE = 'https://www.sandbase.ai'  # public links in READMEs and docs always use the canonical host

SLUG = 'gemini-4-neon'
REPO = 'sandbase-lab/awesome-gemini-4-neon'

CFG = dict(
    slug=SLUG,
    name='Gemini 4 Neon',
    short='Gemini 4 Neon',  # how the prose refers to the model after the first mention
    vendor='Google',
    model_id='google/gemini-4-neon',
    repo=REPO,
    repo_url=f'https://github.com/{REPO}',
    campaign='awesome-gemini-4-neon',
    lab_collection=f'{SITE}/lab/ai-videos/{SLUG}',
    lab_data=f'{ORIGIN}/lab/data/ai-videos/{SLUG}.json',
    media_prefix=f'{SITE}/lab/media/x/{SLUG}/',
    model_page=f'{SITE}/model/google/gemini-4-neon',
    arena=f'{SITE}/arena/text?models=google%2Fgemini-4-neon',
    evals=f'{SITE}/leaderboards',
    pelican=f'{SITE}/arena/pelican-test',
    keys=f'{SITE}/console/keys',
    sandbox=f'{SITE}/landing/sandbox',
    lab_home=f'{SITE}/lab/',
    all_collections=f'{SITE}/lab/ai-videos',
    user_agent=f'awesome-gemini-4-neon-sync/1.0 (+https://github.com/{REPO})',
    html_out='gemini-4-neon.html',
    # Output limit for the curl example. Every output token bills at $15 per million, so a long
    # page costs more than a short one (see the model page).
    max_tokens=128000,
    # Not in this list's facts: confirm with `sandbase inspect google/gemini-4-neon --json` before publishing.
    max_tokens_limit=None,
    context_length=1048576,
    guide_patterns=4,  # numbered sections in docs/prompt-guide.md
    banner_title='Awesome Gemini 4 Neon',
    banner_sub='Videos · prompts · tutorial · model comparison',
    # Finished pieces only on the banner: no comparisons or other models' names.
    banner_skip=('vs', 'versus', 'comparison', 'compar', 'benchmark', 'test', 'opus', 'claude', 'sonnet',
                 'haiku', 'gpt', 'gemini', 'argon', 'deepseek', 'kimi', 'grok', 'qwen', 'glm'),
    not_affiliated={'en': 'Not affiliated with or endorsed by Google.', 'zh-CN': '与 Google 无隶属或背书关系。'},
    # No SandBase blog post on this model is in this list's facts. build_readme.py skips the
    # reading section while this is empty — do not invent links here.
    reading=[],
)

# README and prompt-index copy. Placeholders in {braces} are filled by build_readme.py
# ({name}, {short}, {model_id}, {html_out}, links such as {lab_stats} or {model_page}, counts {n}/{a}/{p}).
# Every fact here is sourced: `sandbase inspect google/gemini-4-neon`, the Lab collection's own
# posts (linked), the creator posts linked in docs/model-comparison.md, and the Lab Evals and
# Pelican Test pages, which have no row for this model in this list's facts.
COPY = {
    'en': {
        'switch': 'English · [简体中文](README.zh-CN.md)',
        'tagline': 'A curated list of **Gemini 4 Neon examples**: videos, prompts and demos made with Gemini 4 Neon, a model from Google DeepMind announced on November 18, 2026. Three.js and GLSL 3D scenes, games, motion graphics and same-prompt comparisons, many of them written as one self-contained HTML page from a prompt, each one credited to its creator and linked to the original post.',
        'alt': 'Awesome Gemini 4 Neon: videos, prompts, tutorial and model comparison',
        'stats': '**{n} videos** from **{a} creators** · **{p}** with the creator\'s prompt · synced daily from [SandBase Lab]({lab_stats})',
        'start': 'Start here',
        'start_rows': [
            ('Watch the videos', '[Browse by category](#contents) below, or [play them full-size on SandBase Lab]({lab_quickstart})'),
            ('Copy a prompt', '[Prompt index](docs/prompts.md): every video that comes with its prompt'),
            ('Write your own prompt', '[Prompt guide](docs/prompt-guide.md): {guide_patterns} patterns and a fill-in template'),
            ('Make a video', '[Tutorial](docs/tutorial.md): prompt → HTML → MP4, with the API and a recording script'),
            ('Pick a model', '[Gemini 4 Neon vs GPT-6.2 Sol, Gemini 4 Carbon, Gemini 4 Argon and Claude Opus 5.5](docs/model-comparison.md)'),
            ('Try it now', '[Run Gemini 4 Neon in the Lab arena]({arena_quickstart}), next to other models'),
        ],
        'goal': 'I want to…', 'where': 'Go to',
        'how': 'Click a preview to play the video. Click a title for the post, the prompt and **Recreate** on SandBase Lab. **@handle** links to the creator\'s post on X.',
        'contents': 'Contents',
        'featured': 'Featured',
        'show_all': 'Show all {n}',
        'recreate': 'Recreate a video with {name}',
        'recreate_body': [
            'Every video page on [SandBase Lab]({lab_recreate}) has a **Recreate** button: it sends the post to {short} in the Lab text arena and returns the code, ready to play in the browser.',
            '',
            'With the API, {name} is `{model_id}` on SandBase (OpenAI-compatible). Put a prompt in `prompt.txt`, create a key in the [console]({keys}), and run:',
        ],
        'recreate_after': 'Open `{html_out}` in a browser, or run it in a [SandBase Sandbox]({sandbox}) to keep generated code isolated. The example asks for up to 128,000 output tokens, and output bills at $15 per million. Full walkthrough: [tutorial](docs/tutorial.md). Pricing: [model page]({model_page}).',
        'prompt_tag': 'prompt',
        'more': '**[See all {n} on SandBase Lab →]({lab_section})**',
        'faq': 'FAQ',
        'faq_items': [
            ('What is Gemini 4 Neon?', "Gemini 4 Neon is a model from Google DeepMind, announced on November 18, 2026. It has a 1,048,576-token context window. On SandBase it is `{model_id}`. For the output limit, run `sandbase inspect google/gemini-4-neon`; the vendor and list prices are also in the [DesignArena post](https://x.com/DesignArena/status/2123220446074253768)."),
            ('How are these Gemini 4 Neon videos made?', "The model doesn't render video. In the examples here it writes a self-contained web page, usually one HTML file that uses Three.js or GLSL shaders; the page runs in a browser and the result is shared as a video. The [tutorial](docs/tutorial.md) shows how to record one."),
            ('Where do I find the prompt for a video?', 'Videos tagged **prompt** come with the creator\'s prompt on their Lab page. The [prompt index](docs/prompts.md) lists all of them.'),
            ('How do I write a good Gemini 4 Neon prompt?', 'Name one self-contained HTML file and the renderer you want (Three.js or GLSL), describe the scene and what moves, and ask for the complete HTML back. Details and a template: [prompt guide](docs/prompt-guide.md).'),
            ('How do I use the Gemini 4 Neon API?', 'On SandBase the model id is `{model_id}` on the OpenAI-compatible `https://api.sandbase.ai/v1/chat/completions` endpoint, and one key works for every model. See [Recreate](#recreate) and the [model page]({model_page}).'),
            ('Is Gemini 4 Neon better than GPT-6.2 Sol, Gemini 4 Carbon, Gemini 4 Argon or Claude Opus 5.5?', "Measured: no Lab Evals or Pelican Test row for Gemini 4 Neon is in the data this list was built from, so nothing here measures it against the others. Reported by creators: one posted a same-prompt test against GPT-6.2 Sol and could not pick a winner; another posted Artificial Analysis Intelligence Index figures of 61 for Neon, 60 for Gemini 4 Carbon, 59 for Claude Opus 5.5 and 62 for GPT-6.2 Astra, which this list has not checked. Details: [model comparison](docs/model-comparison.md)."),
            ('How much does one video cost?', "One creator reported $2.67 for a haunted vampire cathedral scene made with Gemini 4 Neon, against $1.69 for GPT-6.2 Sol on the same prompt. The list price on SandBase is $3 per million input tokens, $15 per million output tokens and $0.15 per million cached input tokens. A call costs (prompt tokens × $3 + completion tokens × $15) ÷ 1,000,000 dollars."),
            ('Can I reuse these videos?', 'No, not by default. They belong to their creators. See [MEDIA-RIGHTS](MEDIA-RIGHTS.md).'),
        ],
        'contribute': 'Suggest a video',
        'contribute_body': 'Know a Gemini 4 Neon creation that should be here? [Open a submission]({repo_url}/issues/new?template=submit-video.yml) with the original X post. Accepted posts are added on SandBase Lab and show up here on the next daily sync. If this list helped you, a ⭐ helps others find it.',
        'credits': 'Credits & rights',
        'credits_body': [
            'Every video, prompt and post belongs to its creator. Cards credit the author and link to the original post. The MIT license covers this repository\'s scripts only. To correct a credit or remove a video, see [MEDIA-RIGHTS](MEDIA-RIGHTS.md).',
            '{not_affiliated}',
        ],
        'footer': 'Maintained by [SandBase Lab]({lab_home}) · [All AI video collections]({all_collections})',
        'p_title': 'Gemini 4 Neon prompts',
        'p_switch': 'English · [简体中文](zh-CN/prompts.md) · [← Back to the collection](../README.md)',
        'p_intro': '{n} Gemini 4 Neon videos whose creators shared the prompt. Open one to read the prompt, watch the video and **Recreate** it with {short} on SandBase Lab. New to prompting {short}? Start with the [prompt guide](prompt-guide.md).',
        'p_note': 'Each entry quotes the creator\'s post as published on X, where the prompt is shared. Some creators describe the task rather than pasting the whole prompt, and some put the full text in a reply: open the post on X to read the thread. Posts keep the creator\'s language.',
        'p_watch': 'Watch',
        'p_open': 'Recreate on SandBase Lab',
    },
    'zh-CN': {
        'switch': '[English](README.md) · 简体中文',
        'tagline': '精选 **Gemini 4 Neon 案例**合集：用 Gemini 4 Neon（Google DeepMind 的模型，2026 年 11 月 18 日宣布）做出的视频、提示词和演示。包括 Three.js 与 GLSL 3D 场景、游戏、动效和同提示词对比，许多是模型根据提示词写成的单文件网页，均注明作者并链接原帖。',
        'alt': 'Awesome Gemini 4 Neon：视频、提示词、教程和模型对比',
        'stats': '共 **{n} 条视频**，来自 **{a} 位创作者** · **{p} 条**附作者提示词 · 每天从 [SandBase Lab]({lab_stats}) 同步',
        'start': '从这里开始',
        'start_rows': [
            ('看视频', '在下方 [按分类浏览](#contents)，或 [在 SandBase Lab 大屏播放]({lab_quickstart})'),
            ('复制提示词', '[提示词索引](docs/zh-CN/prompts.md)：所有附带提示词的视频'),
            ('自己写提示词', '[提示词写法](docs/zh-CN/prompt-guide.md)：{guide_patterns} 条写法和一个填空模板'),
            ('做一个视频', '[教程](docs/zh-CN/tutorial.md)：提示词 → HTML → MP4，含 API 和录屏脚本'),
            ('选模型', '[Gemini 4 Neon 对比 GPT-6.2 Sol、Gemini 4 Carbon、Gemini 4 Argon 和 Claude Opus 5.5](docs/zh-CN/model-comparison.md)'),
            ('马上试试', '[在 Lab 竞技场运行 Gemini 4 Neon]({arena_quickstart})，和其他模型并排对比'),
        ],
        'goal': '我想…', 'where': '去这里',
        'how': '点击预览图播放视频；点击标题前往 SandBase Lab 查看原帖、提示词，并一键 **复刻**；**@作者** 链接到 X 原帖。',
        'contents': '目录',
        'featured': '精选',
        'show_all': '展开全部 {n} 条',
        'recreate': '用 {name} 复刻视频',
        'recreate_body': [
            '[SandBase Lab]({lab_recreate}) 的每个视频页都有 **复刻** 按钮：在 Lab 文本竞技场把帖子内容发给 {short}，返回可在浏览器直接播放的代码。',
            '',
            '用 API 的话，{name} 在 SandBase 上的模型 ID 是 `{model_id}`（兼容 OpenAI）。把提示词写进 `prompt.txt`，在 [控制台]({keys}) 创建 Key，然后运行：',
        ],
        'recreate_after': '用浏览器打开 `{html_out}`，或在 [SandBase Sandbox]({sandbox}) 中运行，让生成的代码保持隔离。示例请求最多输出 128,000 token，输出按每百万 $15 计费。完整步骤见 [教程](docs/zh-CN/tutorial.md)，价格见 [模型页]({model_page})。',
        'prompt_tag': '提示词',
        'more': '**[在 SandBase Lab 查看全部 {n} 条 →]({lab_section})**',
        'faq': '常见问题',
        'faq_items': [
            ('Gemini 4 Neon 是什么？', 'Gemini 4 Neon 是 Google DeepMind 的模型，2026 年 11 月 18 日宣布。它的上下文窗口为 1,048,576 token。在 SandBase 上它是 `{model_id}`；输出上限可运行 `sandbase inspect google/gemini-4-neon` 查看。供应商与标价也可见 [DesignArena 的帖子](https://x.com/DesignArena/status/2123220446074253768)。'),
            ('这些 Gemini 4 Neon 视频是怎么做出来的？', '模型不直接渲染视频。这里的例子大多是它写出的一个独立网页（通常是一个用 Three.js 或 GLSL 的单文件 HTML）；页面在浏览器里运行，作者再把结果分享成视频。见 [教程](docs/zh-CN/tutorial.md)。'),
            ('在哪里找到视频的提示词？', '标有 **提示词** 的视频，其 Lab 页面上有作者的提示词。[提示词索引](docs/zh-CN/prompts.md) 列出了全部。'),
            ('怎么写好 Gemini 4 Neon 提示词？', '指定一个独立运行的 HTML 文件和渲染方式（Three.js 或 GLSL），描述场景和需要动起来的部分，并要求返回完整的 HTML。详细写法和模板见 [提示词写法](docs/zh-CN/prompt-guide.md)。'),
            ('怎么调用 Gemini 4 Neon API？', '在 SandBase 上模型 ID 是 `{model_id}`，使用兼容 OpenAI 的 `https://api.sandbase.ai/v1/chat/completions` 接口，一个 Key 调用所有模型。见 [复刻](#recreate) 和 [模型页]({model_page})。'),
            ('Gemini 4 Neon 比 GPT-6.2 Sol、Gemini 4 Carbon、Gemini 4 Argon 或 Claude Opus 5.5 更强吗？', '实测方面：本列表的数据里没有 Gemini 4 Neon 的 Lab Evals 或 Pelican Test 记录，因此这里没有任何实测结果能把它和其他模型比较。创作者报告方面：一位作者用同一提示词对比了 GPT-6.2 Sol，说分不出谁赢；另一位作者发布的 Artificial Analysis 智能指数为 Neon 61、Gemini 4 Carbon 60、Claude Opus 5.5 59、GPT-6.2 Astra 62，本列表未核实这些数字。详见 [模型对比](docs/zh-CN/model-comparison.md)。'),
            ('做一个视频要花多少钱？', '有作者报告：同一个提示词（哥特吸血鬼大教堂场景），Gemini 4 Neon 花费 $2.67，GPT-6.2 Sol 为 $1.69。SandBase 标价为每百万输入 token $3、每百万输出 token $15，缓存的输入 token 每百万 $0.15。一次调用的费用为（输入 token × $3 + 输出 token × $15）÷ 1,000,000 美元。'),
            ('可以转用这些视频吗？', '默认不可以，视频归作者所有。见 [MEDIA-RIGHTS](MEDIA-RIGHTS.md)。'),
        ],
        'contribute': '推荐作品',
        'contribute_body': '发现了应该收录的 Gemini 4 Neon 作品？附上 X 原帖 [提交给我们]({repo_url}/issues/new?template=submit-video.yml)。通过后会先加入 SandBase Lab，下一次每日同步时出现在这里。觉得有用的话，点个 ⭐ 能让更多人看到。',
        'credits': '致谢与权利',
        'credits_body': [
            '所有视频、提示词和帖子归作者所有。每张卡片都注明作者并链接原帖。MIT 许可证只覆盖本仓库的脚本。更正署名或下架视频请见 [MEDIA-RIGHTS](MEDIA-RIGHTS.md)。',
            '{not_affiliated}',
        ],
        'footer': '由 [SandBase Lab]({lab_home}) 维护 · [全部 AI 视频合集]({all_collections})',
        'p_title': 'Gemini 4 Neon 提示词',
        'p_switch': '[English](../prompts.md) · 简体中文 · [← 返回合集](../../README.zh-CN.md)',
        'p_intro': '共 {n} 条 Gemini 4 Neon 视频，作者公开了提示词。打开即可查看提示词、观看视频，并在 SandBase Lab 上用 {short} 一键 **复刻**。第一次写 {short} 提示词？先看 [提示词写法](prompt-guide.md)。',
        'p_note': '每条都按 X 上发布的原文引用作者帖子。有的作者描述的是任务而不是完整提示词，有的把全文放在回复里，请打开 X 原帖查看讨论串。帖子原文保留作者语言。',
        'p_watch': '观看',
        'p_open': '在 SandBase Lab 复刻',
    },
}

# Labels mirror shared/ai-videos.ts VIDEO_CATEGORIES in the Lab repo.
CATEGORIES = {
    '3d-scene': ('3D scenes', '3D 场景'),
    'motion-graphics': ('Motion graphics', '动效'),
    'game': ('Games', '游戏'),
    'ui-demo': ('Product UI', '产品界面'),
    'particles': ('Particles & shapes', '粒子与形状'),
    'data-viz': ('Charts & diagrams', '图表图解'),
    'kinetic-type': ('Kinetic type', '文字动效'),
    'explainer': ('Explainers', '讲解'),
    'launch-film': ('Launch films', '发布片'),
    'short-film': ('Short films', '短片'),
    'music-video': ('Music videos', '音乐视频'),
    'anime': ('Anime', '动画'),
    'action': ('Action', '动作'),
    'ad': ('Ads', '广告'),
    'comparison': ('Tests & comparisons', '测试对比'),
    'showcase': ('Model showcases', '模型展示'),
}


def utm(medium, content=None):
    q = f'utm_source=github&utm_medium={medium}&utm_campaign={CFG["campaign"]}'
    return q + (f'&utm_content={content}' if content else '')

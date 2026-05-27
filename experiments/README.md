# experiments/

单次 LLM 实验的记录、对比与评测。每次实验一个文件夹,**快照**性质。

## 约定

```
experiments/
└── YYYY-MM-DD-<topic>/
    ├── README.md       # 问题、方法、用了哪个 LLM/版本、结论摘要
    ├── transcript.md   # 对话记录(prompt + 回复)
    └── results.md      # 详细结论:哪行哪不行、需人工修什么
```

## 可复现性

LLM 能力随版本变化,所以每个实验 README 必须记录:

- **日期** 和 **LLM + 版本**(如 ChatGPT GPT-4o 2026-05、Claude Opus 4.7)。
- **任务** 和 **成功标准**。
- **用到的 prompt**(若来自 `prompts/`,链接过去;若实验中提炼出好 prompt,反哺到 `prompts/`)。
- **结论**:成功/失败/部分成功,以及人工干预了多少。

## 命名

`YYYY-MM-DD-<topic>`,例如 `2026-06-01-sd-bass-diffusion`。日期前缀让目录按时间排序,便于追踪能力演化。

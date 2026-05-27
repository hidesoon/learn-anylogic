# models/

被研究的 AnyLogic 模型,每个模型一个文件夹。

## 约定

```
models/
└── <model-name>/
    ├── *.alp / *.alpx        # 模型文件(.alpx 多文件格式更适合 git diff)
    ├── README.md             # 这个模型是什么、研究目的、谁/哪个 LLM 帮写的、改了啥
    └── exports/              # (可选)导出的 Java 代码片段
```

## 每个模型 README 建议记录

- **目的**:研究什么问题。
- **方法学类型**:agent-based / discrete-event / system dynamics。
- **LLM 参与度**:哪些部分是 LLM 写的、用的哪个模型/版本、人工改了什么。
- **关联实验**:链接到 `experiments/` 里相关的实验记录。

> 提示:`.alpx` 是多文件格式,比单文件 `.alp` 更适合版本管理和让 LLM 读结构。

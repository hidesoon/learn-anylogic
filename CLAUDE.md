# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repo is

A **research repository** studying **LLM-assisted simulation modeling**, with AnyLogic as the primary subject. It collects original research write-ups, external reference material, the AnyLogic models under study, reusable prompts, and reproducible LLM experiment logs.

It is **not a software project** — there is no build, lint, or test tooling, and no application to run. Content is Markdown, text, and (eventually) AnyLogic model files (`.alp`/`.alpx`). Work here means writing/organizing research artifacts, not compiling code.

## Organizing principle (the thing to get right)

The repo is organized **by content type**, and two conventions drive where everything goes. Both are easy to violate without reading the per-folder READMEs:

1. **`reports/` vs `references/` is the original-vs-cited line.** `reports/` is **what the user wrote** (analyses, syntheses, findings). `references/` is **external material** (papers, video transcripts, link collections). Never mix them — a summary the user authored goes in `reports/`, even if it summarizes a reference.

2. **`models/<name>/` and `experiments/<name>/` are self-contained and must carry their own `README.md`.** These folders exist for **reproducibility** of LLM-modeling results, so each one records provenance: which LLM + version was used, the task, the prompt, what worked, and what required manual fixing. When creating one, write its README — don't leave a bare folder. The convention details live in [models/README.md](models/README.md) and [experiments/README.md](experiments/README.md).

## Naming conventions

- Folders use `kebab-case`.
- Experiments and time-sensitive reports take a `YYYY-MM-DD-` prefix (e.g. `experiments/2026-06-01-sd-bass-diffusion/`). The date prefix is deliberate: LLM capability changes across model versions, and the prefix lets the directory sort chronologically to track that evolution.

## Keep the index current

The top-level [README.md](README.md) is the human-facing index (research goal, directory map, an "索引"/index section listing key files, and a progress checklist). When you add a notable report, prompt, or reference, **add a line to the README index** and update the progress checklist so it stays the navigation entry point.

The user writes primarily in **Chinese**; existing reports and prompts are in Chinese. Match the language of the surrounding documents.

## Literature review entries

[reports/literature-review.md](reports/literature-review.md) uses a fixed annotated-entry template: each source is an `### [Ln]` heading with `####` sub-headings (出处 / 类型 / 内容摘要 / 核心贡献 / 与本研究的相关性 / 批判性评估 / 可延伸的研究问题). Reuse this template for new entries, and always classify **source type** (peer-reviewed vs. industry/gray literature) — assessing evidence quality is the point of the review.

Repeating the `####` field names across entries is intentional; [.markdownlint.json](.markdownlint.json) sets `MD024: siblings_only` so it does not warn (and disables `MD013` line-length for CJK prose). When a new reference introduces foreign author names or tool/API terms, add them to [cspell.json](cspell.json) to keep the spell-checker quiet.

## Adding reference transcripts

The existing webinar transcript was produced with `yt-dlp` (already installed). To add another video transcript to `references/transcripts/`, download the captions and strip the VTT timing/markup into clean prose:

```bash
yt-dlp --write-auto-subs --write-subs --sub-lang "en.*" --skip-download --sub-format vtt -o "name.%(ext)s" "<VIDEO_URL>"
```

Then de-duplicate the rolling-caption lines and remove `<...>` inline tags before saving the clean `.txt`.

## Reusable prompts

[prompts/](prompts/) holds prompt templates refined across experiments — notably [prompts/anylogic-priming-template.md](prompts/anylogic-priming-template.md), the "seeding" prompt that maps generic Java to AnyLogic's API. When an experiment yields a prompt worth reusing, promote it into `prompts/` and link back from the experiment.

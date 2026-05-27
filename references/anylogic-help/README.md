# AnyLogic 官方文档(本地 Markdown 镜像)

AnyLogic 官方帮助文档 <https://anylogic.help> 的**本地清洁 Markdown 副本**,用于离线阅读、检索、引用和喂给 LLM。属于**外部资料**(引用,非原创),放在 `references/` 下。

> 这是厂商文档的存档转换件,**非原创内容**。每个 `.md` 顶部都保留了 `来源 (Source)` 原文链接;请以官网最新版为准。

## 快照信息

| 项 | 值 |
|---|---|
| 来源 | <https://anylogic.help> |
| 快照日期 | 2026-05-27 |
| 抓取工具 | [fetch.py](fetch.py)(`urllib` + `BeautifulSoup` + `markdownify`) |

已抓取章节:

| 目录 | 章节 | 页数 | 大小 |
|---|---|---|---|
| [advanced/](advanced/) | **Advanced Modeling with Java**(`/advanced/`,散文教程) | 207 | ~1.1 MB |
| [api/](api/) | **AnyLogic API Reference**(`/api/`,引擎 Javadoc 类参考) | 826 | ~4.1 MB |

## 目录结构:advanced/

`advanced/` 完整镜像了官网 `/advanced/` 的目录树。各章节入口(对应官网侧边栏):

| 章节 | 入口 | 页数 |
|---|---|---|
| Java basics for AnyLogic(Java 基础) | [advanced/code/index.md](advanced/code/index.md) | code/ 共 39 |
| AnyLogic functions(内置函数参考) | [advanced/functions/index.md](advanced/functions/index.md) | functions/ 共 105 |
| AnyLogic constants(常量) | [advanced/functions/constants-index.md](advanced/functions/constants-index.md) | — |
| AnyLogic class reference(类/API 参考) | [advanced/code/elements-api.md](advanced/code/elements-api.md) | — |
| Debugging a model(调试) | [advanced/debug/index.md](advanced/debug/index.md) | debug/ 共 16 |
| Creating custom libraries(自定义库) | [advanced/libraries/index.md](advanced/libraries/index.md) | libraries/ 共 14 |
| Adding Java classes(加 Java 类) | [advanced/code/resources-index.md](advanced/code/resources-index.md) | — |
| Team development(Git / SVN 协作) | [advanced/teamwork/index.md](advanced/teamwork/index.md) | teamwork/ 共 13 |
| Action charts(可视化算法) | [advanced/actionchart/index.md](advanced/actionchart/index.md) | actionchart/ 共 12 |
| Integration(Python / Omniverse / JNI 等) | [advanced/integrations-index.md](advanced/integrations-index.md) | omniverse/ 共 6 |

总入口:[advanced/index.md](advanced/index.md)。

## 目录结构:api/

`api/` 是引擎的 Javadoc 类参考(`com.anylogic.engine.*` 等),按 Java 包路径分目录。每个包都有一张 `package-summary.md` 作为类索引(23 个包)。常用入口:

| 包 | 内容 | 入口 |
|---|---|---|
| `com.anylogic.engine` | 核心:Agent、Statechart、Engine 等 | [api/com/anylogic/engine/package-summary.md](api/com/anylogic/engine/package-summary.md) |
| `…engine.markup` | 流程图 / 物料搬运等 block(类最多) | [api/com/anylogic/engine/markup/package-summary.md](api/com/anylogic/engine/markup/package-summary.md) |
| `…engine.presentation` | 可视化 / UI 元素 | [api/com/anylogic/engine/presentation/package-summary.md](api/com/anylogic/engine/presentation/package-summary.md) |
| 全部 | 类总览 | [api/index.md](api/index.md) |

> **API 是精简版**:Javadoc 单页极大(基类 `Agent`/`Utilities` 原文各 ~230 KB),所以只保留**类说明 + 字段/构造器/方法 summary 表**(签名 + 一句话描述),丢掉了逐方法的完整 detail 和「inherited from」继承成员列表。要看某方法的完整参数/返回说明,点页顶 `来源` 链接看官网。

## 转换约定(fetch.py 做了什么)

- **只保留正文**:抽取每页的 `.page-content`,剥掉侧边栏导航、面包屑、脚本、样式和「How can we improve this article?」反馈控件。
- **Javadoc 精简(仅 `/api/`)**:页面含 `section.summary` 时判定为 API 页,删掉 `section.details`、页内方法目录(`.content-nav`)和 `.inherited-list` 继承列表,只留 summary。
- **站内链接 → 相对 `.md`**:指向**同章节**其他已下载页面的链接改写为相对路径(可本地点开互跳);Java SDK 类型链接改写为 Oracle 文档绝对 URL。
- **跨章节链接 → 绝对 URL**:指向未一起抓取的章节(如 `advanced/` ↔ `api/` 互链、`/cloud/`)保留为 `https://anylogic.help/...`,联网可点。
- **图片 → 绝对 URL**:截图不下载二进制,`src` 改写为绝对地址,联网时仍能显示。

## 刷新 / 扩展

原始 HTML 缓存在 `.cache/`(约 140 MB,已 gitignore,可删)。重跑会复用缓存,只重新转换:

```bash
cd references/anylogic-help
pip install beautifulsoup4 markdownify   # 一次性
python3 fetch.py                 # 默认刷新 advanced 章节
python3 fetch.py api             # 刷新 api 章节(Javadoc 自动精简)
python3 fetch.py <section>       # 抓其他章节,如 anylogic、cloud
```

`fetch.py` 会从该章节 `index.html` 自动发现页面集合,因此无需手工维护 URL 列表。要新增章节,直接传章节名即可,产物会落在同名子文件夹。

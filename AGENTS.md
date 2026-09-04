# 野生流动内容工作台工程规则

- 本 Git 根仅维护 wildflow-studio。先执行 `git rev-parse --show-toplevel` 与 `git status --short --branch`，保留已有修改。
- 实现任务使用独立 worktree；一个任务只修改明确范围，分支默认 `codex/*`，只暂存明确文件。
- 产品覆盖图文、音频、视频及组合；以知识库驱动的人机协作、修改、审核和交付为主要使用方式。不与其他开箱包合并成统一产品。
- 优先使用 DeepSeek Harness 的扩展机制；按实际安装版本验证，不默认维护核心 Fork。
- 产品边界、实施顺序与候选方案以 [产品方案](docs/product-plan.md) 及其引用的最新决策为准；固定源码与兼容证据见 [UPSTREAM](UPSTREAM.md)。不能把候选方案当作实施授权，把上游的视频流程当作所有媒体的必经阶段，或未经验证组合不同 DSH 版本的插件。
- 通用能力保持唯一权威源码，项目专属 Skill 使用 `.agents/skills/`，不在多个工具目录维护镜像。
- OB 模板与本机 `.obsidian/` 分离；配置合并先预览与备份，卸载保留用户笔记和成品。
- 不提交凭据、真实业务资料、媒体成品、缓存、模型权重或工具索引；现阶段不加入业务案例、项目模板或素材，后续展示另行批准。
- 模型用户/账务归 wildflow-api，GPU/推理 Job/Artifact/Recovery 归 wildflow-inference；不复制其职责。
- Markdown、配置与日志查询使用原生文本搜索。结构化代码若有本仓 CodeGraph，先核对索引 Project 等于 Git 根；没有索引时使用原生工具，不使用父仓索引。
- PR 前运行 `bash scripts/check.sh`，记录候选 SHA、验证范围和未验证项；应用实现加入后补真实 lint/test/build 与安装、升级、恢复测试。
- 普通 CI 仅手动触发；不得把没有 checks 解释成通过，也不得声称本地门禁等于服务端分支保护。
- 后续修改走 PR，不直接推送或强推 main；低风险合并按负责人常设授权执行，其余需明确授权。
- 本仓已获准按 MIT 开源；许可变更、Tag、Release、付费调用、业务内容发布和生产部署仍需明确授权。
- 先读 [README](README.md)、[SECURITY](SECURITY.md)、[贡献规则](CONTRIBUTING.md)与[版本边界](docs/releases.md)。

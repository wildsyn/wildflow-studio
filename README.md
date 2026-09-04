# 野生流动内容工作台

wildflow-studio 是独立的内容生产开箱包，以知识库驱动的人机协作、修改、审核和交付为主要使用方式。
覆盖图文、音频、视频及其组合，不按媒体类型限制产品范围。

2026-09-05 决策明确：当前优先持续打磨 [wildflow-factory](https://github.com/wildsyn/wildflow-factory)
内容工厂，为内部 AI 图书带货完善由 Skills 和自动驱动流程组成的自动化视频生产。
工厂一直在推进，与既有“视频自动化”线并行，业务和产品边界不合并。

先通过具体业务内容工作台交付积累经验，再归纳自有内容工作台产品；后置的是本仓产品化，
不影响业务工作台交付。自有工作台具体体系尚未开始搭建；
[dsh-oil-creator](https://github.com/oil-oil/dsh-oil-creator) 是形态参照，不能替代业务交付经验。
此前的 Mac、Electron 和 DSH Desktop 方案保留为候选，尚未确定采用或启动实施。

Harness 是基于 DeepSeek Harness 搭建的插件系统基础；工厂与后续工作台主要使用自有模型服务。
模型服务当前先供内部使用、内部充值，不先对外商业化；待内部使用稳定，且有自持固定卡或可长期
租用的固定卡保障稳定供给后，再考虑对外，不承诺日期。公开 MIT 仓库不代表模型服务已经对外商业化。
本页提供当前方向摘要，内部跨仓记录见 [内部 ADR-0015（需主仓权限）](https://github.com/wildsyn/wildflow/blob/main/docs/adr/0015-internal-factory-first.md)，
本仓边界与后续候选见[产品方案](docs/product-plan.md)及[集成验收清单](docs/integration-checklist.md)。

当前仅建立公开 MIT 仓库与治理骨架。没有可启动客户端、安装器、后台服务或已验证业务链路；
不要把建仓理解为开箱即用能力已经交付。本次公开范围仅为原创仓库骨架，产品安装包与发行方式尚未完成。

## 产品责任

- 组合适合本产品的 Skills、DSH 插件、OB 模板、案例和安装/诊断能力。
- 与另一个内容开箱包保持独立 UI、运行配置、依赖版本和发布节奏；不强制统一客户端。
- 共用技能和插件按权威来源引用，避免复制成多套实现。
- 用户知识库、账号、真实媒体、凭据和生成结果与发行源码隔离。
- 现阶段不发布业务案例、项目模板或素材；后续案例展示须另行明确批准。
- 本项目不是前代 WildFlow Studio 的恢复，不继承其工作流平台和旧版本路线。

## 不承载的能力

不实现第二套模型账户、API Key 管理、计费账本或 GPU 调度。
模型公共接口由 wildflow-api 承担，推理 Job、Artifact 和 Recovery 由 wildflow-inference 承担。
本产品未来可维护内容生产流程状态，但不冒充模型任务 Owner。
不默认自动发布内容、付费调用或修改用户现有 Vault。

## 本地验证

目前没有产品启动命令。安装 Git、Python 3.10+、Bash 和 gitleaks 8.30.1 后运行：

```bash
bash scripts/check.sh
```

这里只验证仓库基线，不验证应用构建、安装或内容质量。

## 文档

- [产品方案](docs/product-plan.md)与[集成验收清单](docs/integration-checklist.md)
- [工程规则](AGENTS.md)与[贡献方式](CONTRIBUTING.md)
- [架构边界](docs/architecture.md)与[仓库治理](docs/governance.md)
- [安全与数据](SECURITY.md)、[上游来源](UPSTREAM.md)、[许可状态](LICENSE.md)
- [版本与发行](docs/releases.md)
- [Issues](https://github.com/wildsyn/wildflow-studio/issues)与[PR](https://github.com/wildsyn/wildflow-studio/pulls)

个人使用的开箱包暂不建仓。本仓不包含真实客户内容或私人配置。

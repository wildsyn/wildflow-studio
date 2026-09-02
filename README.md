# 野生流动内容工作台

wildflow-studio 是独立的内容生产开箱包，以知识库驱动的人机协作、修改、审核和交付为主要使用方式。
覆盖图文、音频、视频及其组合，不按媒体类型限制产品范围。

产品方向已经确认：先建设工作台，以 Mac 客户端为主要入口，以
[dsh-oil-creator](https://github.com/oil-oil/dsh-oil-creator) 为内容工作台功能基础，
在本地文件与 Obsidian 知识库之上连接内容项目、AI 对话和可选 Skills。
Electron 是优先技术路线，DSH Desktop 是首选桌面复用候选；具体组合版本须先验证。
详见[产品方案](docs/product-plan.md)与[集成验收清单](docs/integration-checklist.md)。

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

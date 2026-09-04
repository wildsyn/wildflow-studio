# 上游与来源

2026-09-05 更新：内容工厂持续打磨；先通过具体业务内容工作台交付积累经验，再归纳自有工作台产品。
本仓具体体系尚未开始搭建。以下来源及旧源码快照作为后续参照，不替代业务交付经验；
具体决策见[产品方案](docs/product-plan.md)。

| 对象 | 来源 | 当前处理 |
|---|---|---|
| dsh-oil-creator | https://github.com/oil-oil/dsh-oil-creator | 后续内容工作台的形态参考；具体复用范围未定，尚未安装或复制源码 |
| DSH Desktop | https://github.com/anywhere-labs/dsh-desktop | 此前 Electron 桌面方案的复用候选；不是 DeepSeek 官方项目，是否采用及版本均未冻结 |
| DeepSeek Harness | https://github.com/deepseek-ai/deepseek-harness | 执行底座方向已选定；尚未选择或安装运行版本，未复制源码 |
| Obsidian | https://obsidian.md/ | 外部应用依赖；不随本仓再分发应用本体 |
| 通用 Skills、DSH/OB 插件 | 各自的权威仓库或作者发行渠道 | 按需选取；尚未冻结清单，不复制整套用户配置 |

未来每项依赖须登记精确版本或 commit、许可、来源、校验值、安装方式及兼容验证。
DSH 源码分支与 npm 发行标签可能不同；不得仅按最新文档声称安装版兼容。

Git 仓库、npm 包、DSH Bundle、Skill 和 OB 插件是不同单位。目录存在不等于可安装；
依赖安装不等于运行配置已经启用；安装成功不等于真实业务任务完成。

## 2026-08-30 源码核对快照

本表是文档与依赖声明核对，不是安装测试、供应链审计或兼容认证。实施时重新核对；固定 commit
只用于复核本次证据，不是已经批准的应用发行组合。

| 对象 | 核对源码 | 声明与发现 |
|---|---|---|
| dsh-oil-creator | [`03f8d09ce9a298578ba850c0fc5dc3ff44b568ec`](https://github.com/oil-oil/dsh-oil-creator/tree/03f8d09ce9a298578ba850c0fc5dc3ff44b568ec) | package 0.1.0，MIT，Node >=22.19.0，DSH peerDependencies 为 0.1.0-rc.6 或 rc.7；内含 Host、Web Client 与 Bundle patch |
| DSH Desktop | [`b9758b4346f6a806e4407873c5269b9989a39fbe`](https://github.com/anywhere-labs/dsh-desktop/tree/b9758b4346f6a806e4407873c5269b9989a39fbe) | desktop package 2.0.4，MIT，依赖 DSH 0.1.2-alpha.1 和 Electron 43.3.0；该源码组合与 oil creator 声明范围不一致 |

### 可复核的证据

- oil creator：[包声明](https://github.com/oil-oil/dsh-oil-creator/blob/03f8d09ce9a298578ba850c0fc5dc3ff44b568ec/package.json)、[许可](https://github.com/oil-oil/dsh-oil-creator/blob/03f8d09ce9a298578ba850c0fc5dc3ff44b568ec/LICENSE)、[文件约定](https://github.com/oil-oil/dsh-oil-creator/blob/03f8d09ce9a298578ba850c0fc5dc3ff44b568ec/docs/files.md)、[实现与限制](https://github.com/oil-oil/dsh-oil-creator/blob/03f8d09ce9a298578ba850c0fc5dc3ff44b568ec/docs/implementation.md)、[侧栏 patch](https://github.com/oil-oil/dsh-oil-creator/blob/03f8d09ce9a298578ba850c0fc5dc3ff44b568ec/cordis.patch.yml)。
- Desktop：[包声明](https://github.com/anywhere-labs/dsh-desktop/blob/b9758b4346f6a806e4407873c5269b9989a39fbe/dsh-plugin-desktop/package.json)、[架构](https://github.com/anywhere-labs/dsh-desktop/blob/b9758b4346f6a806e4407873c5269b9989a39fbe/docs/architecture.md)、[端口与更新行为](https://github.com/anywhere-labs/dsh-desktop/blob/b9758b4346f6a806e4407873c5269b9989a39fbe/docs/user-guide.md)。

### 后续采用该组合时必须解决

1. 为 Desktop、DSH 与 oil creator 选择一组通过测试的版本，或完成最小兼容适配；不能忽略 peer 冲突直接强制安装。
2. oil creator 会替换 `ui-sidebar`，Desktop 的部分模式也接管布局；必须验证共存、切换和卸载还原，不能只以页面打开作为通过。
3. 上游以视频阶段、作者风格与特定外部工具为中心；本产品要扩展为多媒体独立流程，能力缺失时只降级对应环节。
4. 上游默认状态目录、应用标识、更新源、配置与浏览器 origin 不能直接成为本产品的共享全局状态。

### 复用与许可处理

优先使用固定版本插件并在本仓维护产品适配。仅在公开扩展接口不足时，才评估对 oil creator 插件
做可追溯的受控修改；不预先复制整仓或默认 Fork DSH 核心。复用 MIT 代码时保留作者版权、许可与
来源，改动单独记录。每个可选 Skill、外部应用、字体和素材单独核对许可，不继承其宿主的 MIT 结论。

本次仅新增产品与集成文档，无第三方代码、素材、应用或运行配置进入仓库。

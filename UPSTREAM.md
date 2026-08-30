# 上游与来源

| 对象 | 来源 | 当前处理 |
|---|---|---|
| DeepSeek Harness | https://github.com/deepseek-ai/deepseek-harness | 优先集成方向；尚未选择或安装运行版本，未复制源码 |
| Obsidian | https://obsidian.md/ | 外部应用依赖；不随本仓再分发应用本体 |
| 通用 Skills、DSH/OB 插件 | 各自的权威仓库或作者发行渠道 | 按需选取；尚未冻结清单，不复制整套用户配置 |

未来每项依赖须登记精确版本或 commit、许可、来源、校验值、安装方式及兼容验证。
DSH 源码分支与 npm 发行标签可能不同；不得仅按最新文档声称安装版兼容。

Git 仓库、npm 包、DSH Bundle、Skill 和 OB 插件是不同单位。目录存在不等于可安装；
依赖安装不等于运行配置已经启用；安装成功不等于真实业务任务完成。

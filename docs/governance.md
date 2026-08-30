# 仓库治理

## Owner 与权限

[CODEOWNERS](../.github/CODEOWNERS) 指向组织现有团队 `@wildsyn/wildflow-developers`，
该团队拥有仓库 Write 权限，组织管理员保留管理职责。成员变化由组织统一管理。
仓库为 Public，原创骨架按 [MIT](../LICENSE) 开源，不公开业务资料或凭据。

## 主分支保护

- 首次 seed commit 建立默认分支；后续修改必须走 PR，至少一名 CODEOWNER 批准。
- 新提交使旧批准失效，合并前解决全部 Review 对话。
- 管理员也执行保护，禁止 Force Push 和删除，不以直接 Push 或自审代替批准。
- 必须通过 `baseline` 检查并基于最新 main；提交者对候选分支手动运行 `Repository baseline`。
- 工作流仅 `workflow_dispatch`，不会在 push/PR 后自动消耗 runner；未触发检查就不满足合并条件。
- 普通 PR 默认 Squash，合并后删除功能分支；不常规绕过门禁。

这些是目标规则，是否已经启用须从 GitHub 当前设置回读验证；本地脚本不能替代服务端保护。

## 初始化边界

只创建两个经确认的内容开箱包仓；个人开箱包不建仓。
未定义名称与职责的共用能力仓不在本次范围内。共用能力按稳定版本引用，
不因建仓而创建通用平台、插件市场或复制业务知识库。

两仓独立发布、独立运行、独立验收。建仓和通过基线检查不表示应用已经可用。

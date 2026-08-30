# 贡献与验证

使用独立 Git 根和干净 worktree，分支以 `codex/` 或维护者指定名称开始。
先读取 [AGENTS.md](AGENTS.md)，保留已有修改。只暂存本任务的明确文件，不使用 `git add -A`。

本地依赖：Git、Python 3.10+、Bash、gitleaks 8.30.1。先将本任务文件加入暂存区，再运行：

```bash
bash scripts/check.sh
```

该门禁检查治理文件、JSON/Python 语法、Markdown 本地链接、禁止跟踪的本机数据、
工作区及暂存区空白错误，以及 Git 历史和未提交 diff 的密钥风险。它不是业务测试或构建。
应用实现加入后，必须同步补充真实 lint、test、build 和安装/恢复验证。

普通 CI 仅支持手动触发，遵循 WildFlow 的 runner 使用规则，不在 push/PR 时自动运行。
手动 CI 使用同一本地门禁，结果绑定实际 revision。

首次建仓 seed commit 建立默认分支；后续变更通过 PR，记录改动理由、完整验证命令和 SHA、
未验证项与回退方法。默认 Squash，不通过直接 push 或强推代替评审。
至少由一名 CODEOWNER 批准；不得用自审、管理员绕过或聊天确认替代服务端要求。
CI 是手动触发的 required check，提交者须对候选分支主动运行，等待通过后合并。
治理要求见 [治理说明](docs/governance.md)。

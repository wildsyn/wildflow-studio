"""Check tracked repository content without running a product or reading credentials."""
from pathlib import Path
import ast
import json
import re
import subprocess
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = (
    "README.md", "AGENTS.md", "CONTRIBUTING.md", "SECURITY.md", "LICENSE.md",
    "UPSTREAM.md", "LICENSE", ".github/CODEOWNERS", ".github/workflows/ci.yml",
    "docs/architecture.md", "docs/governance.md", "docs/releases.md",
)
BLOCKED = {
    ".obsidian", ".dsh", ".dsh-state", ".agent-teams", ".codegraph",
    ".venv", "node_modules", "__pycache__", ".cache",
    "output", "outputs", "artifacts", "data", "logs",
}
LINK = re.compile(r"!?(?:\[[^\]]*\])\(([^\s)]+)(?:\s+[\"'][^)]*)?\)")


def git_paths(*args: str) -> list[str]:
    result = subprocess.check_output(["git", *args, "-z"], cwd=ROOT)
    return [item.decode("utf-8") for item in result.split(b"\0") if item]


def main() -> int:
    tracked = git_paths("ls-files")
    untracked = git_paths("ls-files", "--others", "--exclude-standard")
    errors = []
    if untracked:
        errors.append("Stage intended files before validation; untracked files remain.")
    for name in REQUIRED:
        path = ROOT / name
        if name not in tracked or not path.is_file() or not path.stat().st_size:
            errors.append(f"Missing tracked governance file: {name}")
    for name in tracked:
        path = ROOT / name
        relative = Path(name)
        if BLOCKED.intersection(relative.parts):
            errors.append(f"Local state or business data is tracked: {name}")
        if relative.name.startswith(".env") and relative.name not in {".env.example", ".env.template"}:
            errors.append(f"Environment file is tracked: {name}")
        if relative.suffix.lower() in {".pem", ".key", ".p12", ".pfx"}:
            errors.append(f"Credential container is tracked: {name}")
        if path.is_symlink():
            errors.append(f"Symlinks require a reviewed packaging policy: {name}")
            continue
        if not path.is_file():
            errors.append(f"Tracked file missing from working tree: {name}")
            continue
        if path.suffix not in {".md", ".py", ".json", ".yml", ".yaml", ".sh"}:
            continue
        content = path.read_text(encoding="utf-8")
        if path.suffix == ".py":
            ast.parse(content, filename=name)
        if path.suffix == ".json":
            json.loads(content)
        if path.suffix == ".md":
            for raw in LINK.findall(content):
                url = urlsplit(raw.strip("<>"))
                if url.scheme or url.netloc or not url.path:
                    continue
                target = (path.parent / unquote(url.path)).resolve()
                if not target.is_relative_to(ROOT) or not target.exists():
                    errors.append(f"Broken or external local link in {name}: {raw}")
    for error in errors:
        print(f"ERROR {error}")
    print(f"Checked {len(tracked)} tracked files; {len(errors)} errors.")
    return int(bool(errors))


if __name__ == "__main__":
    raise SystemExit(main())

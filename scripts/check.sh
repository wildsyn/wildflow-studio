#!/usr/bin/env bash
set -euo pipefail
ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT_DIR"
command -v gitleaks >/dev/null || {
  echo 'Missing gitleaks; install version 8.30.1 before validation.' >&2
  exit 1
}
python3 scripts/check_repository.py
git diff --check
git diff --cached --check
if git rev-parse --verify HEAD >/dev/null 2>&1; then
  gitleaks git --redact --no-banner --log-opts=--all .
fi
git diff --cached --no-ext-diff | gitleaks stdin --redact --no-banner
git diff --no-ext-diff | gitleaks stdin --redact --no-banner
echo 'Repository baseline passed; product build, installation and business journey remain unverified.'

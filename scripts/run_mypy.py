"""Run mypy with a local search-path alias for the stub-only package."""

from __future__ import annotations

import os
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MYPY = ROOT / ".venv" / "bin" / "mypy"


def main() -> int:
    with tempfile.TemporaryDirectory(prefix="galpy-mypy-") as directory:
        stub_root = Path(directory)
        (stub_root / "galpy").symlink_to(ROOT / "galpy-stubs", target_is_directory=True)
        environment = {**os.environ, "MYPYPATH": str(stub_root)}
        return subprocess.run([str(MYPY), *sys.argv[1:]], env=environment).returncode


if __name__ == "__main__":
    raise SystemExit(main())

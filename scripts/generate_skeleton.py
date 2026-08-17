"""Generate the initial galpy stub tree with basedpyright.

The generator runs outside the repository so pyright's temporary output cannot
be confused with the distributable package while it is being created.
"""

from __future__ import annotations

import json
import shutil
import subprocess
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PYRIGHT = ROOT / ".venv" / "bin" / "basedpyright"
TARGET = ROOT / "galpy-stubs" / "galpy"


def main() -> None:
    with tempfile.TemporaryDirectory(prefix="galpy-stubgen-") as directory:
        worktree = Path(directory)
        (worktree / "pyrightconfig.json").write_text(
            json.dumps(
                {
                    "venvPath": str(ROOT),
                    "venv": ".venv",
                    "pythonPlatform": "All",
                }
            ),
            encoding="utf-8",
        )
        subprocess.run(
            [str(PYRIGHT), "--createstub", "galpy"],
            cwd=worktree,
            check=True,
        )
        generated = worktree / "typings" / "galpy"
        if not generated.is_dir():
            raise RuntimeError("basedpyright did not create a galpy directory")
        if TARGET.exists():
            shutil.rmtree(TARGET)
        shutil.move(str(generated), str(TARGET))
        (TARGET / "py.typed").write_text(
            "# PEP 561 marker for the nested galpy stub package.\n",
            encoding="utf-8",
        )
    print(f"generated {TARGET.relative_to(ROOT)}")


if __name__ == "__main__":
    main()

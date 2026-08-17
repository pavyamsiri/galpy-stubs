# Working on `galpy-stubs`

This repository publishes third-party type stubs for the `galpy` runtime
package. The supported runtime currently comes from `galpy>=1.12.0` and the
project targets Python 3.13.

## Layout

- `galpy-stubs/` mirrors the importable `galpy` module tree. It is named with
  the `<package-name>-stubs` convention so type checkers associate it with
  the separately installed `galpy` runtime package.
- `tests/typing/` contains small consumer-facing typing fixtures.
- `scripts/` contains reproducible generation and inspection helpers.
- `docs/` records overload audits and runtime findings.
- `docs/module-roadmap.md` orders modules by stub difficulty and user value.

The declarations currently originate from `basedpyright --createstub galpy`.
That output is only a skeleton: generated names, signatures, return types,
array shapes, and overloads must be checked against galpy's source and safe
runtime probes before being treated as an API contract.

## Runtime inspection

Use the project environment, where the supported galpy version is installed:

```bash
.venv/bin/python
```

For public objects, inspect `dir`, `inspect.signature`,
`inspect.getattr_static`, `type`, and `inspect.getfile`. Prefer small probes
with representative scalar, list, and NumPy-array inputs. Read galpy's Python
source and tests when behavior is not safely observable at runtime. Treat
runtime behavior as authoritative, including parameter names, defaults,
properties, descriptors, and positional-only or keyword-only markers.

Do not expose private implementation details merely because the generator
found them. Keep public re-exports explicit and keep `.pyi` files concise.

## Typing style

Use the repository-local `modern-python-typing` skill for stub work. Use Python
3.13 syntax, `Self`, `Protocol`, `Literal`, overloads, and `optype`'s shaped
NumPy types where they describe real behavior. Prefer a precise domain type or
`object` over `Any`; use `Any` only for genuinely dynamic runtime behavior.
Preserve array rank and dtype behavior instead of using an unshaped array for
every numerical API.

## Workflow

```bash
just sync       # install/update the development environment
just skeleton   # regenerate the pyright baseline in a temporary directory
just format
just check      # formatting, linting, and configured type checks
just build      # build the stub wheel
```

Edit generated skeleton files only after confirming their runtime contract.
Add `assert_type` examples for corrected or newly modelled public APIs. The
eventual full check should cover all stubs and fixtures with basedpyright,
basedmypy, ty, and pyrefly; while coverage is being developed, `just check`
also reports the generated baseline's known incompleteness clearly.

Before finishing, run `git diff --check`, inspect the wheel contents, and
review the diff for stale generated declarations, private APIs, broad `Any`,
and unrelated edits.

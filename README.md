# galpy-stubs

Type stubs for [galpy](https://github.com/jobovy/galpy).

The repository keeps the stubs directly in `galpy-stubs/`. Stub-only
distributions use this `<package-name>-stubs` layout so type checkers
automatically associate the installed declarations with `galpy`.

The initial declarations are a `basedpyright --createstub` skeleton generated
from galpy 1.12.0. They are being refined through source analysis, runtime
inspection, and consumer typing fixtures. See `AGENTS.md` for the development
workflow, `docs/module-roadmap.md` for the module work order, and
`docs/overload-audit.md` for overload priorities.

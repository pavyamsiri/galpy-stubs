# galpy overload audit

The generated declarations are a broad inventory, not a finished API
contract. This audit records the first areas where source analysis and runtime
probes should replace generated `Any`, ellipsis defaults, and scalar/batch
ambiguity.

The installed baseline is galpy 1.12.0. Public runtime modules include
`actionAngle`, `df`, `orbit`, `potential`, and `util`; `potential` is the
largest surface (159 public names in the initial inventory).

## Priority order

1. `galpy.potential`: base `Potential`/`Force`, concrete potential
   constructors, evaluation helpers, and scalar versus array return values.
2. `galpy.orbit`: `Orbit` construction, coordinate representations, and
   shape-preserving properties and methods.
3. `galpy.actionAngle`: action/angle result tuples and the common scalar/batch
   dispatch used by action-angle classes.
4. `galpy.df`: distribution-function constructors and calls, especially
   derivative flags and stream/distribution helpers.
5. `galpy.util`: public numerical utilities and optional-dependency branches.

## Method

For each public declaration:

- read the corresponding galpy implementation and tests;
- compare `inspect.signature`, descriptors, and inherited members;
- probe representative scalar, list, float-array, and integer-array inputs;
- record output rank, dtype, tuple ordering, and exceptions;
- add focused `assert_type` fixtures before broadening the declaration.

Use overloads where a literal flag, input rank, or constructor discriminator
changes the return type. Use `optype` for established NumPy rank/dtype
contracts. Keep runtime value constraints out of overloads unless they affect
dispatch.

The current generated skeleton has 7844 basedpyright diagnostics, mostly
unresolved generator placeholders and missing annotations. This number is a
baseline for the refinement work, not an intended quality target.

Runtime note: `HomogeneousSpherePotential` and `SphericalShellPotential` do
not accept vectorized coordinate arrays even though they inherit the common
`Potential` interface. The current hierarchy intentionally keeps the broad
base signature; a future scalar/vectorized protocol split should model this
without introducing an incompatible subclass override.

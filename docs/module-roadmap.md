# galpy module stub roadmap

This roadmap orders work by a combination of:

- **ease**: how directly signatures and return types can be established;
- **value**: how often users import the API and how much precise typing helps;
- **risk**: dynamic dispatch, optional dependencies, C extensions, and
  scalar/batch shape changes.

The baseline is galpy 1.12.0 on Python 3.13. The generated package currently
contains 153 `.pyi` files in seven public areas. The file count is not a
priority measure: `potential` is large because it has many related concrete
classes, while `orbit.Orbit` is one very large and difficult contract.

## Area-level order

| Priority | Area | Files | Ease | Value | Main reason |
| --- | --- | ---: | :---: | :---: | --- |
| P0 | `galpy` | 1 | Easy | Medium | Small re-export and version/config surface |
| P0 | `galpy.potential` foundations | 10-ish core modules | Medium | Very high | Shared base classes make later classes cheaper |
| P0 | `galpy.util.config`, `multi`, `quadpack` | 3 | Easy | Medium | Mostly ordinary functions with fixed results |
| P1 | Simple `galpy.potential` classes | ~35 | Easy–medium | Very high | Repeated constructor and scalar evaluation patterns |
| P1 | `galpy.df` analytic/spherical classes | ~12 | Medium | High | Reusable DF base and predictable numerical calls |
| P1 | `galpy.util.coords` | 1 large module | Medium | High | Pure coordinate transforms, but many array-rank variants |
| P2 | `galpy.orbit` integrator helpers | 3 | Medium | High | C-backed signatures are inspectable; arrays are shape-sensitive |
| P2 | `galpy.potential` wrappers and composites | ~20 | Medium–hard | High | Inheritance is useful, but composition and accepted inputs vary |
| P2 | `galpy.util.conversion` | 1 | Hard | High | Decorators preserve callable signatures and alter physical units |
| P3 | `galpy.actionAngle` base and simple classes | ~8 | Hard | High | Shared result conventions, scalar/batch and flag dispatch |
| P3 | `galpy.df` disk and quasi-isothermal classes | ~8 | Hard | High | Many optional models and action-angle dependencies |
| P3 | `galpy.orbit.Orbit` | 1 | Very hard | Very high | Coordinate modes, arbitrary shapes, integration state, overloads |
| P3 | `galpy.potential` expansion/interpolation classes | ~15 | Hard | Medium–high | Constructor schemas and multidimensional arrays are complex |
| P4 | `galpy.df` stream classes | ~8 | Very hard | Medium | Deep object coupling and model-specific arrays |
| P4 | `galpy.snapshot` | 3 | Hard | Low–medium | `directnbody` is optional and unavailable in the current environment |
| P4 | `galpy.util.plot` and `leung_dop853` | 2 | Hard | Low | Optional plotting and implementation-oriented numerical helpers |
| P4 | `potential.amuse` and other optional modules | — | Very hard | Low | External packages are not part of the core dependency contract |

The P0/P1 work should establish the shared aliases, protocols, and NumPy
conventions that make P2/P3 work faster. P4 modules remain inventoried, but
should not block a useful first release.

## Detailed work sequence

### P0 — establish reusable contracts

1. Clean the root and package `__init__.pyi` files: explicit public
   re-exports, version/config types, and no accidental implementation names.
2. Model the potential hierarchy: `Force`, `Potential`, `SphericalPotential`,
   `planarPotential`, `linearPotential`, `WrapperPotential`, and composite
   types. Define shared numeric input aliases and physical-unit protocols.
3. Correct `util.config`, `util.multi`, and `util.quadpack` using signatures
   and small runtime probes.
4. Add fixtures for construction, scalar evaluation, and one-dimensional
   array evaluation.

### P1 — high-value, regular APIs

1. Type simple potential families first: Miyamoto–Nagai, Plummer, Isochrone,
   logarithmic, spherical power-law, NFW/Hernquist/Jaffe aliases, and other
   classes with ordinary constructor parameters.
2. Add shared constructor aliases and inherited methods instead of copying
   the same declarations into every concrete class.
3. Type analytic DF classes with fixed constructor forms and calls.
4. Replace broad array types in `util.coords` with `optype` rank-aware types,
   starting with functions whose input and output rank are identical.

### P2 — composition and C-backed APIs

1. Type orbit integration helper functions and their output arrays.
2. Type potential wrappers and composite operators, checking whether they
   accept one object, a sequence, or a callable.
3. Type physical-conversion decorators with `ParamSpec`/`Concatenate` only
   where runtime signature preservation is confirmed; otherwise expose the
   narrowest documented callable protocol.
4. Add overloads for potential evaluation flags and scalar versus batch input.

### P3 — dispatch-heavy public APIs

1. Establish common action-angle result aliases and overloads for action,
   angle, and frequency flags.
2. Refine `Orbit` incrementally: construction, shape-preserving properties,
   fixed-coordinate accessors, then integration and plotting methods.
3. Refine disk/quasi-isothermal DFs and potential expansion/interpolation
   classes from runtime probes and source branches.
4. Generate overloads only after a small handwritten representative set has
   established the actual dispatch matrix.

### P4 — optional and highly dynamic surfaces

Handle stream DFs, snapshots, plotting, AMUSE integration, and low-level
numerical helpers after the core package has useful coverage. These modules
need optional-dependency test environments or deliberately documented narrow
fallback types.

## Per-module completion criteria

A module moves to the next status only when:

1. public exports match `dir(module)` after excluding private implementation
   names and optional names unavailable under the supported dependency set;
2. signatures preserve parameter names, defaults, and keyword-only markers;
3. representative runtime probes establish scalar/batch rank and dtype;
4. public classes include initialized attributes and descriptors;
5. realistic `assert_type` fixtures pass with basedpyright and basedmypy; and
6. remaining broad types are either narrowed or recorded with a specific
   runtime reason in the audit.

The next concrete slice after the completed foundations is the regular P1
potential constructors, followed by wrappers and composite operators.

## Progress

- **P0.1 complete:** cleaned root exports and typed `util.config`,
  `util.multi`, `util.quadpack`, and the small numerical helpers in
  `util.__init__`. Added focused consumer fixtures and verified the slice with
  basedpyright and basedmypy.
- **P0.2 foundations complete:** typed the shared `Force`, `Potential`,
  dissipative, planar, linear, spherical, wrapper, and composite base classes,
  including reusable scalar/array aliases and core flags. Concrete potential
  modules and the generated `potential.__init__` re-export surface remain for
  the next slice.
- **P1 started:** narrowed the regular constructors for Miyamoto–Nagai,
  Plummer, Isochrone, logarithmic halo, power-law, Kepler, Dehnen, Hernquist,
  and NFW potentials. Their inherited scalar/array evaluation contracts now
  have focused typing and runtime fixtures.
- **P1 continued:** narrowed Burkert, Einasto, exponentially truncated NFW,
  pseudo-isothermal, homogeneous sphere, Kuzmin disk, double-exponential disk,
  flattened power, and spherical-shell constructors. Runtime probes recorded
  that homogeneous-sphere and spherical-shell evaluation is scalar-only.
- **P1 continued:** narrowed razor-thin exponential, elliptical, ring,
  Henon–Heiles, isothermal-disk, Kuijken–Gilmore, steady/transient logarithmic
  spiral, and softened-needle-bar constructors. Focused type-checking and
  runtime smoke tests pass for this disk, planar, and linear slice.
- **P1 continued:** narrowed `NullPotential`, `CosmphiDiskPotential`, and
  `LopsidedDiskPotential`, with focused type-checking and scalar runtime smoke
  tests passing.
- **P2 started:** narrowed the fixed-signature amplitude wrappers
  `DehnenSmoothWrapperPotential`, `GaussianAmplitudeWrapperPotential`, and
  `TimeDependentAmplitudeWrapperPotential`. Wrapper inputs now accept a
  potential or potential list, and the arbitrary amplitude callback uses a
  typed callable protocol. Runtime smoke tests pass; the dynamic wrapper
  factory is represented explicitly with a broad `__new__` return.
- **P2 continued:** narrowed `SolidBodyRotationWrapperPotential`,
  `CorotatingRotationWrapperPotential`, and
  `CylindricallySeparablePotentialWrapper`. Focused type-checking and runtime
  evaluation pass for the rotation and separability wrappers.
- **P2 continued:** narrowed `KuzminLikeWrapperPotential`, including its
  spherical-potential input and scale parameters. Focused type-checking and a
  scalar runtime probe pass.
- **P2 continued:** narrowed `DehnenBarPotential` and
  `RotateAndTiltWrapperPotential`. The bar’s pattern-speed/time accessors and
  the rotation wrapper’s coordinate-vector aliases are typed, with focused
  checks and scalar runtime probes passing.
- **P2 continued:** narrowed `OblateStaeckelWrapperPotential` and added a
  reusable coordinate-pair alias for its scalar-`u0` and `(R, z)` reference
  forms. Both constructor forms pass focused typing and runtime probes.
- **P2 continued:** narrowed `interpSphericalPotential` and `KingPotential`.
  The interpolated spherical force accepts either a typed callable or a
  potential input, and both forms pass runtime probes; `interpRZPotential`
  remains for a separate option-heavy pass.
- **P2 continued:** replaced the unfinished generated `interpRZPotential`
  surface with a clean constructor stub covering the R/Z grid specification,
  interpolation flags, potential input, and runtime options. A small
  potential-backed interpolation build passes, while its low-level C helper
  functions remain deliberately deferred for a separate audit.
- **P2 continued:** narrowed `ChandrasekharDynamicalFrictionForce`,
  `FDMDynamicalFrictionForce`, and `NonInertialFrameForce`. Added callable and
  time-dependent-vector aliases, with valid constructor probes for density,
  dispersion, fuzzy-dark-matter, and rotating-frame configurations.
- **P1 continued:** narrowed the analytic spherical DFs
  `isotropicHernquistdf`, `isotropicNFWdf`, `isotropicPlummerdf`,
  `isotropicPowerLawdf`, and `kingdf`. Runtime inspection established that
  their `fE` implementations require array-shaped energy inputs; the stubs and
  fixtures now reflect that contract.
- **P1 continued:** narrowed `constantbetaHernquistdf`,
  `constantbetaPowerLawdf`, `osipkovmerrittHernquistdf`,
  `osipkovmerrittNFWdf`, and `osipkovmerrittPowerLawdf`. Their array-based
  `fE`/`fQ` contracts pass focused typing and runtime probes.
- **P1 continued:** replaced the unfinished coordinate skeleton with typed
  core transforms for Galactic, rectangular/cylindrical/spherical, and
  Staeckel coordinate conversions. Overloads cover scalar tuple results and
  batch array results; runtime probes record the batch `(N, 3)` convention.
  Covariance and Jacobian helpers remain broad pending matrix-shape audits.
- **P2 continued:** replaced the generated orbit integration helper skeletons
  with typed planar, full, and linear integration entry points, including
  potential inputs, state/time arrays, integration controls, and paired array
  results. Runtime probes pass for all three integrator families.
- **P3 started:** replaced the unfinished action-angle base skeleton and typed
  constructors for `actionAngleHarmonic`, `actionAngleIsochrone`,
  `actionAngleSpherical`, and `actionAngleVertical`. Runtime probes pass for
  harmonic, Isochrone, spherical, and vertical potential configurations;
  result-flag overloads remain the next action-angle pass.
- **P3 continued:** typed `actionAngleInverse` and added fixed constructors for
  `actionAngleHarmonicInverse`, `actionAngleIsochroneInverse`, and
  `actionAngleVerticalInverse`. Focused typing and runtime constructor probes
  pass; inverse result overloads remain part of the shared action-angle pass.
- **P1 continued:** replaced the unfinished `surfaceSigmaProfile` skeleton
  with typed base/profile methods and an `expSurfaceSigmaProfile` constructor.
  Scalar profile evaluations pass focused typing and runtime probes.
- **P1 continued:** replaced the unfinished `diskdf` skeleton with typed
  constructor aliases for `surfaceSigma` classes/instances and profile
  parameters, covering `dehnendf`, `shudf`, and `schwarzschilddf`. Constructor
  and target-profile probes pass; polymorphic DF evaluation remains deferred
  to an overload audit.
- **P3 continued:** replaced the generated `quasiisothermaldf` constructor
  surface with typed scale, potential, action-angle, precomputation, and
  physical-unit parameters. A real LogarithmicHaloPotential/actionAngleStaeckel
  construction passes runtime and focused typing checks.
- **P3 continued:** added reusable action-angle result aliases and a precise
  representative dispatch contract for `actionAngleHarmonic`, covering scalar
  and batch action, frequency, and angle results. Runtime shape probes pass;
  the remaining action-angle classes can now follow this matrix.
- **P3 continued:** applied the three-, six-, and nine-component result
  contracts to `actionAngleSpherical` and `actionAngleIsochrone`, with typed
  scalar/batch-compatible numeric inputs and runtime tuple-length probes.
- **P3 continued:** typed constructors for `actionAngleAdiabatic`,
  `actionAngleStaeckel`, `actionAngleAdiabaticGrid`, and
  `actionAngleStaeckelGrid`. Reduced-grid runtime construction and focused
  typing checks pass; their specialized action methods remain for the next
  dispatch pass.
- **P3 continued:** added three/six/nine result contracts to the adiabatic and
  Stäckel evaluators, plus scalar-or-array `Jz`/`JR` declarations for their
  grid variants. Runtime tuple-length and reduced-grid action probes pass.
- **P2 continued:** refined `CompositePotential`, `linearCompositePotential`,
  and `planarCompositePotential` constructor inputs and physical-unit aliases.
  Focused typing and runtime construction probes pass for 3D, linear, and
  planar composites.
- **P3 continued:** narrowed fixed-signature analytic triaxial potentials
  `FerrersPotential`, `TriaxialGaussianPotential`, and
  `PerfectEllipsoidPotential`, including coordinate-vector and normalization
  parameters. Constructor smoke tests and focused typing checks pass.
- **P3 continued:** narrowed `PowerTriaxialPotential` and the triaxial
  Hernquist, Jaffe, and NFW variants, including their shared axis/orientation,
  quadrature, normalization, and NFW virial parameters. Runtime constructor
  probes and focused typing checks pass.
- **P2 continued:** narrowed `SpiralArmsPotential` and
  `MovingObjectPotential`, including arm coefficient sequences and typed Orbit
  plus potential inputs. Constructor probes and focused typing checks pass.
- **P2 continued:** narrowed `KuzminKutuzovStaeckelPotential`,
  `AnySphericalPotential`, and `AnyAxisymmetricRazorThinDiskPotential`, adding
  callable density/surface-density protocols and fixed geometric parameters.
  Constructor probes and focused typing checks pass.
- **P2 continued:** replaced the generated constructor surfaces for
  `SCFPotential`, `MultipoleExpansionPotential`, `DiskSCFPotential`, and
  `DiskMultipoleExpansionPotential`. Added named aliases for density
  callbacks, profile inputs, and expansion coefficient arrays; the SCF
  coefficient helper functions now have typed array/result contracts. Default
  construction of all four classes passes runtime probes and focused checks.
- **P1 continued:** typed the reusable `mwpot_helpers` density functions with
  array-aware numeric inputs and outputs, and tightened the public Milky Way
  preset helpers in `mwpotentials`, `DehnenBinney98`, `Cautun20`, and
  `McMillan17`. Preset construction and helper evaluation probes pass focused
  formatting/lint/type checks.
- **P2 continued:** replaced the generated `util.conversion` surface with
  precise scalar unit-factor functions, named conversion-input/output aliases,
  typed parsers, and callable decorator boundaries. Numeric conversion and
  decorator runtime probes plus a focused typing fixture pass; Astropy-backed
  parser results remain intentionally broad through `QuantityLike`.
- **P0 continued:** narrowed `util.special.compute_legendre` with literal
  derivative overloads and typed its matrix outputs, alongside the spherical
  harmonic normalization helper. Runtime shape probes and a focused fixture
  pass.
- **P0 continued:** typed the `util.symplecticode` leapfrog integrator and
  its split-step helpers with callable and rank-aware array contracts. A
  focused fixture and runtime import/signature checks pass.
- **P3 continued:** replaced the generated `actionAngleIsochroneApprox`
  constructor and helper skeletons with explicit potential/isochrone,
  integration, and numeric contracts. Its dynamic phase-space dispatch remains
  represented by named result aliases until a scalar/batch probe matrix is
  completed.
- **P3 continued:** replaced the generated `actionAngle.__init__` re-export
  surface with explicit class and helper imports, including the refined
  Isochrone-approximation and Stäckel helpers. Export-level typing fixtures
  pass.
- **P3 continued:** replaced the generated `actionAngleTorus` skeleton with
  explicit constructor, torus-coordinate, frequency, Hessian, and Jacobian
  array contracts. The C-extension availability restriction remains a runtime
  limitation and is documented in the fixture.
- **P2 continued:** typed the initialization boundary of
  `NumericalPotentialDerivativesMixin` as the keyword dictionary consumed by
  galpy's numerical derivative setup, removing one of the remaining
  unannotated shared potential hooks.
- **P1 continued:** narrowed `MN3ExponentialDiskPotential` to its stable
  amplitude, scale-length, profile, normalization, and physical-unit
  constructor contract, with a focused fixture.
- **P0 continued:** typed all optional-dependency availability flags as
  booleans, and replaced the generated shared Kuijken--Dubinski expansion
  base with the same callable/profile aliases used by its SCF and multipole
  subclasses.
- **P4 started:** typed the shared DF physical-unit lifecycle and the large
  `streamdf` constructor boundary. Stream setup/evaluation remains deferred
  because it couples Orbit, action-angle, potential, and optional Astropy
  behavior; a no-setup constructor fixture records the supported lightweight
  check.
- **P4 continued:** replaced the generated `util.plot` declarations with a
  concise optional-Matplotlib surface, typed numerical plotting inputs, and
  isolated the custom polar-transform classes. A plotting fixture covers the
  main histogram, density, and scatter entry points; Matplotlib artist details
  remain intentionally broad.
- **P4 continued:** replaced the generated low-level `util.leung_dop853`
  declarations with explicit ODE, tolerance, state-array, and integration
  result contracts. The public DOP853 entry point has a focused fixture; its
  internal step-control state remains intentionally lower-level.
- **P4 continued:** typed the adaptive-rejection sampler helpers in
  `util.ars` with log-density callbacks, domain/finite-bound inputs, hull
  aliases, and sample results. A focused callback fixture passes.
- **P4 continued:** typed the optional extension-loader globals and return
  contracts in `util._load_extension_libs`, including the ctypes library and
  loaded-state values.
- **P1 continued:** replaced the generated spherical-DF base classes with
  shared potential/input aliases and typed lifecycle, sampling, moment,
  anisotropy, and `fE`/`fQ` boundaries. Constant-beta and Osipkov--Merritt
  base constructor fixtures pass; concrete analytic subclasses retain their
  narrower array contracts.
- **P3 continued:** replaced the generated `evolveddiskdf` grid skeletons
  with explicit evolution inputs and named moment/grid method boundaries.
  Construction fixtures cover the lightweight grid and DF entry points;
  interpolation-node shapes remain intentionally broad.
- **P1 continued:** narrowed `eddingtondf` to the shared spherical-DF and
  array-valued energy contract.
- **P4 continued:** replaced the generated optional AMUSE adapter and
  snapshot container declarations with dependency-neutral lifecycle,
  integration, and plotting contracts. AMUSE quantity/artist types remain
  intentionally represented as `object` because the optional dependency is
  not installed in the supported environment.
- **P4 continued:** replaced the generated `StreamTrack` and
  `StreamTrackPair` surfaces with typed precomputed-track arrays, physical
  unit lifecycle methods, core coordinate accessors, and pair construction.
  Advanced sky/covariance accessors remain available through a documented
  dynamic boundary pending optional-Astropy shape tests.
- **P4 continued:** replaced the generated particle-spray DF declarations
  with shared progenitor-mass, tail-selection, potential, sampling, and
  `StreamTrack` contracts for `basestreamspraydf`, `chen24spraydf`,
  `fardal15spraydf`, and `streamspraydf`. Detailed spray-kernel array shapes
  remain deferred pending model-specific runtime probes.
- **P4 continued:** replaced the generated `streamgapdf` and impulse-kernel
  declarations with a concise gap-DF subclass surface and callable numerical
  helper boundary. Detailed encounter-kernel array shapes remain deferred.
- **P3 continued:** replaced the generated compiled action-angle helper
  skeletons for adiabatic, Stäckel, and Torus calculations with array/rank,
  potential-input, frequency-result, and error-flag contracts. A focused
  compiled-helper fixture records the array-valued boundary.
- **P3 continued:** replaced the 3,500-line generated `Orbit` declaration
  with an explicit core contract for construction, shape/dimension state,
  integration, physical-unit lifecycle, common coordinate/observable
  accessors, and plotting. Advanced SOS/variational and optional-coordinate
  dispatch remains behind a named dynamic boundary until its overload matrix
  is audited.
- **P0/P4 cleanup:** replaced generated Irrgang13, Jeans, ellipsoidal,
  adiabatic-contraction, SnapshotRZ, vertical-potential, snapshot-movie, and
  McMillan preset declarations with typed public boundaries. Package exports
  for `galpy.df`, `galpy.orbit`, `galpy.snapshot`, and action-angle helpers
  now have focused re-export coverage; same-name extension/module collisions
  are isolated in fixtures with narrow callable casts.

## Verification status

The current refined surface passes `just format`, `just lint`, repository-wide
basedpyright and basedmypy over the stubs plus consumer fixtures, ty and
pyrefly over the complete stub tree, and `git diff --check`; the lightweight
Orbit, spherical-DF, and action-angle runtime probes also pass. The consumer
fixtures remain intentionally assigned to basedpyright/basedmypy: ty and
pyrefly currently resolve those `.pyi` imports against the installed runtime
package instead of the configured stub path, producing false unknown/module
diagnostics for same-name galpy exports and optype assertions.

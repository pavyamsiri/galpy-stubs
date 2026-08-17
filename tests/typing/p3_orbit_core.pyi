from collections.abc import Callable
from typing import Protocol, cast

import numpy as np
from galpy.orbit import Orbit
from galpy.potential import LogarithmicHaloPotential

class OrbitLike(Protocol):
    def dim(self) -> int: ...
    def integrate(self, *args: object, **kwargs: object) -> None: ...
    def R(self) -> object: ...
    def vT(self) -> object: ...

orbit = cast(OrbitLike, cast(Callable[..., object], Orbit)([1.0, 0.0, 1.0]))
assert orbit.dim() == 2
orbit.integrate(np.linspace(0.0, 0.1, 3), LogarithmicHaloPotential())
orbit.R()
orbit.vT()

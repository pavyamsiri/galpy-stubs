from collections.abc import Callable

from optype import numpy as onp

from ._typing import Numeric, QuantityLike
from .Potential import Potential
from .SphericalPotential import SphericalPotential

class interpSphericalPotential(SphericalPotential):
    def __init__(
        self,
        rforce: Callable[[Numeric], Numeric]
        | Potential
        | list[Potential]
        | None = None,
        rgrid: onp.ArrayND = ...,
        Phi0: float | None = None,
        ro: QuantityLike | None = None,
        vo: QuantityLike | None = None,
    ) -> None: ...

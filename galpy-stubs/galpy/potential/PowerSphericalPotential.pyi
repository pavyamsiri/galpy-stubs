from .Potential import Potential
from ._typing import QuantityLike

class PowerSphericalPotential(Potential):
    def __init__(
        self,
        amp: QuantityLike = 1.0,
        alpha: float = 1.0,
        normalize: bool | float = False,
        r1: QuantityLike = 1.0,
        ro: QuantityLike | None = None,
        vo: QuantityLike | None = None,
    ) -> None: ...

class KeplerPotential(PowerSphericalPotential):
    def __init__(
        self,
        amp: QuantityLike = 1.0,
        normalize: bool | float = False,
        ro: QuantityLike | None = None,
        vo: QuantityLike | None = None,
    ) -> None: ...

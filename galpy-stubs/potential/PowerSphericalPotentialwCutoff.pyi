from ._typing import QuantityLike
from .Potential import Potential

class PowerSphericalPotentialwCutoff(Potential):
    def __init__(
        self,
        amp: QuantityLike = 1.0,
        alpha: float = 1.0,
        rc: QuantityLike = 1.0,
        normalize: bool | float = False,
        r1: QuantityLike = 1.0,
        ro: QuantityLike | None = None,
        vo: QuantityLike | None = None,
    ) -> None: ...

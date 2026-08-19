from ._typing import QuantityLike
from .Potential import Potential

class FlattenedPowerPotential(Potential):
    def __init__(
        self,
        amp: QuantityLike = 1.0,
        alpha: float = 0.5,
        q: float = 0.9,
        core: QuantityLike = 1e-8,
        normalize: bool | float = False,
        r1: QuantityLike = 1.0,
        ro: QuantityLike | None = None,
        vo: QuantityLike | None = None,
    ) -> None: ...

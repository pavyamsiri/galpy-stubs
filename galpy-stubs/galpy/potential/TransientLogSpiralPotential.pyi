from ._typing import QuantityLike
from .planarPotential import planarPotential

class TransientLogSpiralPotential(planarPotential):
    def __init__(
        self,
        amp: QuantityLike = 1.0,
        omegas: QuantityLike = 0.65,
        A: QuantityLike = -0.035,
        alpha: float = -7.0,
        m: int = 2,
        gamma: float = 0.7853981633974483,
        p: float | None = None,
        sigma: QuantityLike = 1.0,
        to: QuantityLike = 0.0,
        ro: QuantityLike | None = None,
        vo: QuantityLike | None = None,
    ) -> None: ...

from ._typing import QuantityLike
from .planarPotential import planarPotential

class SteadyLogSpiralPotential(planarPotential):
    def __init__(
        self,
        amp: QuantityLike = 1.0,
        omegas: QuantityLike = 0.65,
        A: QuantityLike = -0.035,
        alpha: float = -7.0,
        m: int = 2,
        gamma: float = 0.7853981633974483,
        p: float | None = None,
        tform: QuantityLike | None = None,
        tsteady: QuantityLike | None = None,
        ro: QuantityLike | None = None,
        vo: QuantityLike | None = None,
    ) -> None: ...

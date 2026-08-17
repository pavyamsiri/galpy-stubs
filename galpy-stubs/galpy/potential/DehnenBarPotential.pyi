from .Potential import Potential
from ._typing import QuantityLike

class DehnenBarPotential(Potential):
    def __init__(
        self,
        amp: QuantityLike = 1.0,
        omegab: QuantityLike | None = None,
        rb: QuantityLike | None = None,
        chi: float = 0.8,
        rolr: QuantityLike = 0.9,
        barphi: QuantityLike = 0.4363323129985824,
        tform: float = -4.0,
        tsteady: float | None = None,
        beta: float = 0.0,
        alpha: QuantityLike = 0.01,
        Af: QuantityLike | None = None,
        ro: QuantityLike | None = None,
        vo: QuantityLike | None = None,
    ) -> None: ...
    def tform(self) -> float: ...
    def OmegaP(self) -> float: ...

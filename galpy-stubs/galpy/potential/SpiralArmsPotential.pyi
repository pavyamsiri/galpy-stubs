from collections.abc import Sequence

from .Potential import Potential
from ._typing import QuantityLike

class SpiralArmsPotential(Potential):
    def __init__(
        self,
        amp: QuantityLike = 1.0,
        ro: QuantityLike | None = None,
        vo: QuantityLike | None = None,
        amp_units: str = "density",
        N: int = 2,
        alpha: QuantityLike = 0.2,
        r_ref: QuantityLike = 1.0,
        phi_ref: QuantityLike = 0.0,
        Rs: QuantityLike = 0.3,
        H: QuantityLike = 0.125,
        omega: QuantityLike = 0.0,
        Cs: Sequence[float] = (1.0,),
    ) -> None: ...
    def OmegaP(self) -> float: ...

from optype import numpy as onp

from ._typing import Numeric, QuantityLike
from .Potential import Potential

class EllipsoidalPotential(Potential):
    def __init__(
        self,
        amp: Numeric | QuantityLike = 1.0,
        b: Numeric = 1.0,
        c: Numeric = 1.0,
        zvec: onp.Array1D | None = None,
        pa: Numeric | QuantityLike | None = None,
        glorder: int | None = None,
        ro: QuantityLike | None = None,
        vo: QuantityLike | None = None,
        amp_units: str | None = None,
    ) -> None: ...
    def OmegaP(self) -> Numeric: ...

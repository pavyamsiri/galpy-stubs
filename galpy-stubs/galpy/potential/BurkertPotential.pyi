from .SphericalPotential import SphericalPotential
from ._typing import QuantityLike

class BurkertPotential(SphericalPotential):
    def __init__(
        self,
        amp: QuantityLike = 1.0,
        a: QuantityLike = 2.0,
        normalize: bool | float = False,
        ro: QuantityLike | None = None,
        vo: QuantityLike | None = None,
    ) -> None: ...

from .SphericalPotential import SphericalPotential
from ._typing import QuantityLike

class EinastoPotential(SphericalPotential):
    def __init__(
        self,
        amp: QuantityLike = 1.0,
        h: QuantityLike = 2.0,
        n: float = 1,
        rs: QuantityLike | None = None,
        rm2: QuantityLike | None = None,
        normalize: bool | float = False,
        ro: QuantityLike | None = None,
        vo: QuantityLike | None = None,
    ) -> None: ...

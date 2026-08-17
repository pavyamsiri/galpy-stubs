from ._typing import QuantityLike
from .linearPotential import linearPotential

class IsothermalDiskPotential(linearPotential):
    def __init__(
        self,
        amp: QuantityLike = 1.0,
        sigma: QuantityLike = 0.1,
        ro: QuantityLike | None = None,
        vo: QuantityLike | None = None,
    ) -> None: ...

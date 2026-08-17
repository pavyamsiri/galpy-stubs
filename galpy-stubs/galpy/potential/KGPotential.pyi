from ._typing import QuantityLike
from .linearPotential import linearPotential

class KGPotential(linearPotential):
    def __init__(
        self,
        amp: QuantityLike = 1.0,
        K: QuantityLike = 1.15,
        F: QuantityLike = 0.03,
        D: QuantityLike = 1.8,
        ro: QuantityLike | None = None,
        vo: QuantityLike | None = None,
    ) -> None: ...

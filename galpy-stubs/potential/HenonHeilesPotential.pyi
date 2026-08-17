from ._typing import QuantityLike
from .planarPotential import planarPotential

class HenonHeilesPotential(planarPotential):
    def __init__(
        self,
        amp: QuantityLike = 1.0,
        ro: QuantityLike | None = None,
        vo: QuantityLike | None = None,
    ) -> None: ...

from ._typing import QuantityLike
from .Potential import Potential

class LogarithmicHaloPotential(Potential):
    def __init__(
        self,
        amp: QuantityLike = 1.0,
        core: QuantityLike = 1e-8,
        q: float = 1.0,
        b: float | None = None,
        normalize: bool | float = False,
        ro: QuantityLike | None = None,
        vo: QuantityLike | None = None,
    ) -> None: ...

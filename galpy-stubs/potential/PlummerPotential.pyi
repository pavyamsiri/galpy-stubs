from ._typing import QuantityLike
from .Potential import Potential

class PlummerPotential(Potential):
    def __init__(
        self,
        amp: QuantityLike = 1.0,
        b: QuantityLike = 0.8,
        normalize: bool | float = False,
        ro: QuantityLike | None = None,
        vo: QuantityLike | None = None,
    ) -> None: ...

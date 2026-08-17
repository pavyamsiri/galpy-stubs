from .Potential import Potential
from ._typing import QuantityLike

class MiyamotoNagaiPotential(Potential):
    def __init__(
        self,
        amp: QuantityLike = 1.0,
        a: QuantityLike = 1.0,
        b: QuantityLike = 0.1,
        normalize: bool | float = False,
        ro: QuantityLike | None = None,
        vo: QuantityLike | None = None,
    ) -> None: ...

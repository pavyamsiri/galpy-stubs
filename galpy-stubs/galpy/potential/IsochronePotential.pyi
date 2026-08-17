from .Potential import Potential
from ._typing import QuantityLike

class IsochronePotential(Potential):
    def __init__(
        self,
        amp: QuantityLike = 1.0,
        b: QuantityLike = 1.0,
        normalize: bool | float = False,
        ro: QuantityLike | None = None,
        vo: QuantityLike | None = None,
    ) -> None: ...

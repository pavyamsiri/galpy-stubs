from .Potential import Potential
from ._typing import QuantityLike

class DoubleExponentialDiskPotential(Potential):
    def __init__(
        self,
        amp: QuantityLike = 1.0,
        hr: QuantityLike = 1 / 3,
        hz: QuantityLike = 1 / 16,
        normalize: bool | float = False,
        ro: QuantityLike | None = None,
        vo: QuantityLike | None = None,
        de_h: float = 0.001,
        de_n: int = 10000,
    ) -> None: ...

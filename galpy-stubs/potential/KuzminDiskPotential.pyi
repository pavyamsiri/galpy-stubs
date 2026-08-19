from ._typing import QuantityLike
from .Potential import Potential

class KuzminDiskPotential(Potential):
    def __init__(
        self,
        amp: QuantityLike = 1.0,
        a: QuantityLike = 1.0,
        normalize: bool | float = False,
        ro: QuantityLike | None = None,
        vo: QuantityLike | None = None,
    ) -> None: ...

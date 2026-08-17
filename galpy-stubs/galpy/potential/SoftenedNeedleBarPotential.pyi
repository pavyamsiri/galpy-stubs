from .Potential import Potential
from ._typing import QuantityLike

class SoftenedNeedleBarPotential(Potential):
    def __init__(
        self,
        amp: QuantityLike = 1.0,
        a: QuantityLike = 4.0,
        b: QuantityLike = 0.0,
        c: QuantityLike = 1.0,
        normalize: bool | float = False,
        pa: QuantityLike = 0.4,
        omegab: QuantityLike = 1.8,
        ro: QuantityLike | None = None,
        vo: QuantityLike | None = None,
    ) -> None: ...

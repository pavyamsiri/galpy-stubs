from ._typing import QuantityLike
from .planarPotential import planarPotential

class EllipticalDiskPotential(planarPotential):
    def __init__(
        self,
        amp: QuantityLike = 1.0,
        phib: float = 0.4363323129985824,
        p: float = 1.0,
        twophio: float = 0.01,
        r1: QuantityLike = 1.0,
        tform: QuantityLike | None = None,
        tsteady: QuantityLike | None = None,
        cp: object | None = None,
        sp: object | None = None,
        ro: QuantityLike | None = None,
        vo: QuantityLike | None = None,
    ) -> None: ...

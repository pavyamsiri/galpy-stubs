from ._typing import CoordinateLike, QuantityLike
from .EllipsoidalPotential import EllipsoidalPotential

class PowerTriaxialPotential(EllipsoidalPotential):
    def __init__(
        self,
        amp: QuantityLike = 1.0,
        alpha: float = 1.0,
        r1: QuantityLike = 1.0,
        b: float = 1.0,
        c: float = 1.0,
        zvec: CoordinateLike | None = None,
        pa: QuantityLike | None = None,
        glorder: int = 50,
        normalize: bool | float = False,
        ro: QuantityLike | None = None,
        vo: QuantityLike | None = None,
    ) -> None: ...

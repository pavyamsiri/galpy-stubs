from .EllipsoidalPotential import EllipsoidalPotential
from ._typing import CoordinateLike, QuantityLike

class PerfectEllipsoidPotential(EllipsoidalPotential):
    def __init__(
        self,
        amp: QuantityLike = 1.0,
        a: QuantityLike = 5.0,
        b: float = 1.0,
        c: float = 1.0,
        zvec: CoordinateLike | None = None,
        pa: QuantityLike | None = None,
        glorder: int = 50,
        normalize: bool | float = False,
        ro: QuantityLike | None = None,
        vo: QuantityLike | None = None,
    ) -> None: ...

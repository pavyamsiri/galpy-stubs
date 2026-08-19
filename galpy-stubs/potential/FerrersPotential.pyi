from ._typing import CoordinateLike, Numeric, QuantityLike
from .Potential import Potential

class FerrersPotential(Potential):
    def __init__(
        self,
        amp: QuantityLike = 1.0,
        a: QuantityLike = 1.0,
        n: int = 2,
        b: float = 0.35,
        c: float = 0.2375,
        omegab: QuantityLike = 0.0,
        pa: QuantityLike = 0.0,
        normalize: bool | float = False,
        ro: QuantityLike | None = None,
        vo: QuantityLike | None = None,
    ) -> None: ...
    def OmegaP(self) -> float: ...
    def rot(self, t: Numeric = 0.0, transposed: bool = False) -> CoordinateLike: ...

def lowerlim(
    x: Numeric, y: Numeric, z: Numeric, a: Numeric, b: Numeric, c: Numeric
) -> Numeric: ...

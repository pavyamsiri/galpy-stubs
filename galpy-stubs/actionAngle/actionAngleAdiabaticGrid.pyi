from ..potential._typing import Numeric, QuantityLike
from ..potential.Potential import Potential
from .actionAngle import actionAngle

class actionAngleAdiabaticGrid(actionAngle):
    def __init__(
        self,
        *,
        pot: Potential | list[Potential] | None = None,
        zmax: QuantityLike = 1.0,
        gamma: float = 1.0,
        Rmax: QuantityLike = 5.0,
        nR: int = 16,
        nEz: int = 16,
        nEr: int = 31,
        nLz: int = 31,
        numcores: int = 1,
        **kwargs: object,
    ) -> None: ...
    def Jz(
        self,
        R: Numeric,
        vR: Numeric,
        vT: Numeric,
        z: Numeric,
        vz: Numeric,
        phi: Numeric = 0.0,
    ) -> Numeric: ...

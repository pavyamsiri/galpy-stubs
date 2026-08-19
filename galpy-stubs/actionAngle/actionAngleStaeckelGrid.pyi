from ..potential._typing import Numeric, QuantityLike
from ..potential.Potential import Potential
from .actionAngle import actionAngle

class actionAngleStaeckelGrid(actionAngle):
    def __init__(
        self,
        *,
        pot: Potential | list[Potential] | None = None,
        delta: QuantityLike | None = None,
        Rmax: QuantityLike = 5.0,
        nE: int = 25,
        npsi: int = 25,
        nLz: int = 30,
        numcores: int = 1,
        interpecc: bool = False,
        **kwargs: object,
    ) -> None: ...
    def JR(
        self,
        R: Numeric,
        vR: Numeric,
        vT: Numeric,
        z: Numeric,
        vz: Numeric,
        phi: Numeric = 0.0,
    ) -> Numeric: ...
    def Jz(
        self,
        R: Numeric,
        vR: Numeric,
        vT: Numeric,
        z: Numeric,
        vz: Numeric,
        phi: Numeric = 0.0,
    ) -> Numeric: ...

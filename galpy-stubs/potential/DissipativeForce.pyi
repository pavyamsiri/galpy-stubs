from ._typing import Numeric, QuantityLike
from .Force import Force

class DissipativeForce(Force):
    isNonAxi: bool
    hasC: bool
    hasC_dxdv: bool
    hasC_dxdv3d: bool
    hasC_dens: bool
    hasC_planar: bool
    def __init__(
        self,
        amp: QuantityLike = 1.0,
        ro: QuantityLike | None = None,
        vo: QuantityLike | None = None,
        amp_units: str | None = None,
    ) -> None: ...
    def Rforce(
        self,
        R: Numeric,
        z: Numeric,
        phi: Numeric = 0.0,
        t: Numeric = 0.0,
        v: object | None = None,
    ) -> Numeric: ...
    def zforce(
        self,
        R: Numeric,
        z: Numeric,
        phi: Numeric = 0.0,
        t: Numeric = 0.0,
        v: object | None = None,
    ) -> Numeric: ...
    def phitorque(
        self,
        R: Numeric,
        z: Numeric,
        phi: Numeric = 0.0,
        t: Numeric = 0.0,
        v: object | None = None,
    ) -> Numeric: ...

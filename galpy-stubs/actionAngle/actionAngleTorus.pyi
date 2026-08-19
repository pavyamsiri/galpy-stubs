from optype import numpy as onp

from ..potential._typing import Numeric
from ..potential.Potential import Potential

_autofit_errvals: dict[int, str]

class actionAngleTorus:
    def __init__(
        self,
        *,
        pot: Potential | list[Potential],
        tol: Numeric = 0.001,
        dJ: Numeric = 0.001,
        ro: Numeric | None = None,
        vo: Numeric | None = None,
    ) -> None: ...
    def __call__(
        self,
        jr: Numeric,
        jphi: Numeric,
        jz: Numeric,
        angler: onp.Array1D,
        anglephi: onp.Array1D,
        anglez: onp.Array1D,
        **kwargs: object,
    ) -> onp.Array2D: ...
    def xvFreqs(
        self,
        jr: Numeric,
        jphi: Numeric,
        jz: Numeric,
        angler: onp.Array1D,
        anglephi: onp.Array1D,
        anglez: onp.Array1D,
        **kwargs: object,
    ) -> tuple[onp.Array2D, Numeric, Numeric, Numeric, int]: ...
    def Freqs(
        self, jr: Numeric, jphi: Numeric, jz: Numeric, **kwargs: object
    ) -> tuple[Numeric, Numeric, Numeric, int]: ...
    def hessianFreqs(
        self, jr: Numeric, jphi: Numeric, jz: Numeric, **kwargs: object
    ) -> tuple[onp.Array2D, Numeric, Numeric, Numeric, int]: ...
    def xvJacobianFreqs(
        self,
        jr: Numeric,
        jphi: Numeric,
        jz: Numeric,
        angler: onp.Array1D,
        anglephi: onp.Array1D,
        anglez: onp.Array1D,
        **kwargs: object,
    ) -> tuple[
        onp.Array2D,
        onp.Array3D,
        onp.Array2D,
        Numeric,
        Numeric,
        Numeric,
        int,
    ]: ...

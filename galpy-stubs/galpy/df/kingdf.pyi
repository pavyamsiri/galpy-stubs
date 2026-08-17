from .sphericaldf import isotropicsphericaldf
from typing import override
from ..potential._typing import Numeric, QuantityLike
from optype import numpy as onp

class kingdf(isotropicsphericaldf):
    def __init__(
        self,
        W0: float,
        M: QuantityLike = 1.0,
        rt: QuantityLike = 1.0,
        npt: int = 1001,
        ro: QuantityLike | None = None,
        vo: QuantityLike | None = None,
    ) -> None: ...
    def dens(self, r: Numeric) -> Numeric: ...
    @override
    def fE(self, E: onp.ArrayND) -> onp.ArrayND: ...

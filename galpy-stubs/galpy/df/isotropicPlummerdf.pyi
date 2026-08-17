from .sphericaldf import isotropicsphericaldf
from typing import override
from ..potential.Potential import Potential
from ..potential._typing import QuantityLike
from optype import numpy as onp

class isotropicPlummerdf(isotropicsphericaldf):
    def __init__(
        self,
        pot: Potential | list[Potential] | None = None,
        ro: QuantityLike | None = None,
        vo: QuantityLike | None = None,
    ) -> None: ...
    @override
    def fE(self, E: onp.ArrayND) -> onp.ArrayND: ...

from typing import override

from optype import numpy as onp

from ..potential._typing import QuantityLike
from ..potential.Potential import Potential
from .sphericaldf import isotropicsphericaldf

class isotropicNFWdf(isotropicsphericaldf):
    def __init__(
        self,
        pot: Potential | list[Potential] | None = None,
        widrow: bool = False,
        rmax: QuantityLike = 10000.0,
        ro: QuantityLike | None = None,
        vo: QuantityLike | None = None,
    ) -> None: ...
    @override
    def fE(self, E: onp.ArrayND) -> onp.ArrayND: ...

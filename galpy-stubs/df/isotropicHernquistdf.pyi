from typing import override

from optype import numpy as onp

from ..potential._typing import QuantityLike
from ..potential.Potential import Potential
from .sphericaldf import isotropicsphericaldf

class isotropicHernquistdf(isotropicsphericaldf):
    def __init__(
        self,
        pot: Potential | list[Potential] | None = None,
        ro: QuantityLike | None = None,
        vo: QuantityLike | None = None,
    ) -> None: ...
    @override
    def fE(self, E: onp.ArrayND) -> onp.ArrayND: ...

from typing import override

from optype import numpy as onp

from ..potential._typing import Numeric, QuantityLike
from ..potential.Potential import Potential
from .sphericaldf import isotropicsphericaldf

class eddingtondf(isotropicsphericaldf):
    def __init__(
        self,
        pot: Potential | list[Potential] | None = None,
        denspot: Potential | list[Potential] | None = None,
        rmax: Numeric | QuantityLike | None = None,
        rmin: Numeric | QuantityLike | None = None,
        scale: Numeric | QuantityLike | None = None,
        ro: Numeric | None = None,
        vo: Numeric | None = None,
    ) -> None: ...
    @override
    def fE(self, E: onp.ArrayND) -> onp.ArrayND: ...
    @override
    def sample(self, *args: object, **kwargs: object) -> object: ...

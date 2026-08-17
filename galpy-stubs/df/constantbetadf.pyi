from typing import override

from optype import numpy as onp

from ..potential._typing import Numeric, QuantityLike
from .sphericaldf import SphericalPotentialInput, anisotropicsphericaldf

class _constantbetadf(anisotropicsphericaldf):
    def __init__(
        self,
        pot: SphericalPotentialInput | None = None,
        denspot: SphericalPotentialInput | None = None,
        beta: Numeric | None = None,
        rmax: Numeric | QuantityLike | None = None,
        scale: Numeric | QuantityLike | None = None,
        ro: Numeric | None = None,
        vo: Numeric | None = None,
    ) -> None: ...

class constantbetadf(_constantbetadf):
    def __init__(
        self,
        pot: SphericalPotentialInput | None = None,
        denspot: SphericalPotentialInput | None = None,
        beta: Numeric | None = None,
        twobeta: Numeric | None = None,
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

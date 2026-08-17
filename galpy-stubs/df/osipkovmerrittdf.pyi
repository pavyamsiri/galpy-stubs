from typing import override

from optype import numpy as onp
from ..potential._typing import Numeric, QuantityLike
from .sphericaldf import SphericalPotentialInput, anisotropicsphericaldf

class _osipkovmerrittdf(anisotropicsphericaldf):
    def __init__(
        self,
        pot: SphericalPotentialInput | None = None,
        denspot: SphericalPotentialInput | None = None,
        ra: Numeric | QuantityLike = 1.4,
        rmax: Numeric | QuantityLike | None = None,
        scale: Numeric | QuantityLike | None = None,
        ro: Numeric | None = None,
        vo: Numeric | None = None,
    ) -> None: ...

class osipkovmerrittdf(_osipkovmerrittdf):
    def __init__(
        self,
        pot: SphericalPotentialInput | None = None,
        denspot: SphericalPotentialInput | None = None,
        ra: Numeric | QuantityLike = 1.4,
        rmax: Numeric | QuantityLike | None = None,
        rmin: Numeric | QuantityLike | None = None,
        scale: Numeric | QuantityLike | None = None,
        ro: Numeric | None = None,
        vo: Numeric | None = None,
    ) -> None: ...
    @override
    def fQ(self, Q: onp.ArrayND) -> onp.ArrayND: ...
    @override
    def sample(self, *args: object, **kwargs: object) -> object: ...

from typing import Literal

from ._typing import Numeric, QuantityLike
from .interpSphericalPotential import interpSphericalPotential

type ContractionMethod = Literal["cautun", "blumenthal", "gnedin"]

class AdiabaticContractionWrapperPotential(interpSphericalPotential):
    def __init__(
        self,
        amp: Numeric | QuantityLike = 1.0,
        pot: object = None,
        baryonpot: object = None,
        method: ContractionMethod = "cautun",
        f_bar: Numeric | None = None,
        rmin: Numeric | QuantityLike | None = None,
        rmax: Numeric | QuantityLike = 50.0,
        ro: QuantityLike | None = None,
        vo: QuantityLike | None = None,
    ) -> None: ...

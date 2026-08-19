from ._typing import CoordinateLike, QuantityLike
from .Potential import Potential
from .WrapperPotential import WrapperPotential

class RotateAndTiltWrapperPotential(WrapperPotential):
    def __init__(
        self,
        amp: QuantityLike = 1.0,
        inclination: QuantityLike | None = None,
        galaxy_pa: QuantityLike | None = None,
        sky_pa: QuantityLike | None = None,
        zvec: CoordinateLike | None = None,
        offset: CoordinateLike | None = None,
        pot: Potential | list[Potential] | None = None,
        ro: QuantityLike | None = None,
        vo: QuantityLike | None = None,
    ) -> None: ...

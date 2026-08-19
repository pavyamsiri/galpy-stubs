from ..orbit.Orbits import Orbit
from ._typing import QuantityLike
from .Potential import Potential

class MovingObjectPotential(Potential):
    def __init__(
        self,
        orbit: Orbit,
        pot: Potential | list[Potential] | None = None,
        amp: QuantityLike = 1.0,
        ro: QuantityLike | None = None,
        vo: QuantityLike | None = None,
    ) -> None: ...

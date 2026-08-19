from ._typing import QuantityLike
from .Potential import Potential

class SphericalPotential(Potential):
    def __init__(
        self,
        amp: QuantityLike = 1.0,
        ro: QuantityLike | None = None,
        vo: QuantityLike | None = None,
        amp_units: str | None = None,
    ) -> None: ...

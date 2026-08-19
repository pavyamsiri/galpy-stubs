from ._typing import QuantityLike
from .SphericalPotential import SphericalPotential

class SphericalShellPotential(SphericalPotential):
    def __init__(
        self,
        amp: QuantityLike = 1.0,
        a: QuantityLike = 0.75,
        normalize: bool | float = False,
        ro: QuantityLike | None = None,
        vo: QuantityLike | None = None,
    ) -> None: ...

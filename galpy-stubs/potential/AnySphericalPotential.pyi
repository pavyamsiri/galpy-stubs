from collections.abc import Callable
from .SphericalPotential import SphericalPotential
from ._typing import Numeric, QuantityLike

class AnySphericalPotential(SphericalPotential):
    def __init__(
        self,
        amp: QuantityLike = 1.0,
        dens: Callable[[Numeric], QuantityLike] | None = None,
        normalize: bool | float = False,
        ro: QuantityLike | None = None,
        vo: QuantityLike | None = None,
    ) -> None: ...

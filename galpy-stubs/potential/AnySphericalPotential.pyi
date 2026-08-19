from collections.abc import Callable

from ._typing import Numeric, QuantityLike
from .SphericalPotential import SphericalPotential

class AnySphericalPotential(SphericalPotential):
    def __init__(
        self,
        amp: QuantityLike = 1.0,
        dens: Callable[[Numeric], QuantityLike] | None = None,
        normalize: bool | float = False,
        ro: QuantityLike | None = None,
        vo: QuantityLike | None = None,
    ) -> None: ...

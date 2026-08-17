from collections.abc import Callable
from .Potential import Potential
from ._typing import Numeric, QuantityLike

class AnyAxisymmetricRazorThinDiskPotential(Potential):
    def __init__(
        self,
        amp: QuantityLike = 1.0,
        surfdens: Callable[[Numeric], QuantityLike] | None = None,
        normalize: bool | float = False,
        ro: QuantityLike | None = None,
        vo: QuantityLike | None = None,
    ) -> None: ...

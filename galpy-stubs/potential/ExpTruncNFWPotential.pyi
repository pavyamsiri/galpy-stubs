from ._typing import QuantityLike
from .SphericalPotential import SphericalPotential

class ExpTruncNFWPotential(SphericalPotential):
    def __init__(
        self,
        amp: QuantityLike = 1.0,
        a: QuantityLike = 1.0,
        rc: QuantityLike = 2.0,
        mass: QuantityLike | None = None,
        normalize: bool | float = False,
        ro: QuantityLike | None = None,
        vo: QuantityLike | None = None,
    ) -> None: ...

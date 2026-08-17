from .Potential import Potential
from ._typing import QuantityLike

class HomogeneousSpherePotential(Potential):
    def __init__(
        self,
        amp: QuantityLike = 1.0,
        R: QuantityLike = 1.1,
        normalize: bool | float = False,
        ro: QuantityLike | None = None,
        vo: QuantityLike | None = None,
    ) -> None: ...

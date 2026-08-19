from ._typing import QuantityLike
from .Potential import Potential

class RazorThinExponentialDiskPotential(Potential):
    def __init__(
        self,
        amp: QuantityLike = 1.0,
        hr: QuantityLike = 1 / 3,
        normalize: bool | float = False,
        ro: QuantityLike | None = None,
        vo: QuantityLike | None = None,
        new: bool = True,
        glorder: int = 100,
    ) -> None: ...

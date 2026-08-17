from .Potential import Potential
from ._typing import Number, Numeric

class MN3ExponentialDiskPotential(Potential):
    def __init__(
        self,
        amp: Number = 1.0,
        hr: Numeric = 1.0 / 3.0,
        hz: Numeric = 1.0 / 16.0,
        sech: bool = False,
        posdens: bool = False,
        normalize: bool | Number = False,
        ro: Numeric | None = None,
        vo: Numeric | None = None,
    ) -> None: ...

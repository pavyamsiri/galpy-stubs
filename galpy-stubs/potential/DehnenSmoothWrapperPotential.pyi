from ._typing import QuantityLike
from .Potential import Potential
from .WrapperPotential import parentWrapperPotential

class DehnenSmoothWrapperPotential(parentWrapperPotential):
    def __new__(
        cls,
        amp: QuantityLike = 1.0,
        pot: Potential | list[Potential] | None = None,
        tform: QuantityLike = -4.0,
        tsteady: QuantityLike | None = None,
        decay: bool = False,
        ro: QuantityLike | None = None,
        vo: QuantityLike | None = None,
    ) -> object: ...
    def __init__(
        self,
        amp: QuantityLike = 1.0,
        pot: Potential | list[Potential] | None = None,
        tform: QuantityLike = -4.0,
        tsteady: QuantityLike | None = None,
        decay: bool = False,
        ro: QuantityLike | None = None,
        vo: QuantityLike | None = None,
    ) -> None: ...

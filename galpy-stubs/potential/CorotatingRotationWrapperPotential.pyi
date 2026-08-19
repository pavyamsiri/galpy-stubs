from ._typing import QuantityLike
from .Potential import Potential
from .WrapperPotential import parentWrapperPotential

class CorotatingRotationWrapperPotential(parentWrapperPotential):
    def __new__(
        cls,
        amp: QuantityLike = 1.0,
        pot: Potential | list[Potential] | None = None,
        vpo: QuantityLike = 1.0,
        beta: float = 0.0,
        to: QuantityLike = 0.0,
        pa: QuantityLike = 0.0,
        ro: QuantityLike | None = None,
        vo: QuantityLike | None = None,
    ) -> object: ...
    def __init__(
        self,
        amp: QuantityLike = 1.0,
        pot: Potential | list[Potential] | None = None,
        vpo: QuantityLike = 1.0,
        beta: float = 0.0,
        to: QuantityLike = 0.0,
        pa: QuantityLike = 0.0,
        ro: QuantityLike | None = None,
        vo: QuantityLike | None = None,
    ) -> None: ...

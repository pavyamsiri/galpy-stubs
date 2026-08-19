from ._typing import CoordinatePair, QuantityLike
from .Potential import Potential
from .WrapperPotential import parentWrapperPotential

class OblateStaeckelWrapperPotential(parentWrapperPotential):
    def __new__(
        cls,
        amp: QuantityLike = 1.0,
        pot: Potential | list[Potential] | None = None,
        delta: QuantityLike = 0.5,
        u0: QuantityLike | CoordinatePair = 0.0,
        ro: QuantityLike | None = None,
        vo: QuantityLike | None = None,
    ) -> object: ...
    def __init__(
        self,
        amp: QuantityLike = 1.0,
        pot: Potential | list[Potential] | None = None,
        delta: QuantityLike = 0.5,
        u0: QuantityLike | CoordinatePair = 0.0,
        ro: QuantityLike | None = None,
        vo: QuantityLike | None = None,
    ) -> None: ...

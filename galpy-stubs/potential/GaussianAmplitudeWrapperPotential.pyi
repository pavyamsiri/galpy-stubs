from ._typing import QuantityLike
from .Potential import Potential
from .WrapperPotential import parentWrapperPotential

class GaussianAmplitudeWrapperPotential(parentWrapperPotential):
    def __new__(
        cls,
        amp: QuantityLike = 1.0,
        pot: Potential | list[Potential] | None = None,
        to: QuantityLike = 0.0,
        sigma: QuantityLike = 1.0,
        ro: QuantityLike | None = None,
        vo: QuantityLike | None = None,
    ) -> object: ...
    def __init__(
        self,
        amp: QuantityLike = 1.0,
        pot: Potential | list[Potential] | None = None,
        to: QuantityLike = 0.0,
        sigma: QuantityLike = 1.0,
        ro: QuantityLike | None = None,
        vo: QuantityLike | None = None,
    ) -> None: ...

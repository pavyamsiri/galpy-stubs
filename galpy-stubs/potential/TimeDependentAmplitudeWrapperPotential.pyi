from collections.abc import Callable

from ._typing import QuantityLike
from .Potential import Potential
from .WrapperPotential import parentWrapperPotential

class TimeDependentAmplitudeWrapperPotential(parentWrapperPotential):
    def __new__(
        cls,
        amp: QuantityLike = 1.0,
        A: Callable[[float], float] | None = None,
        pot: Potential | list[Potential] | None = None,
        ro: QuantityLike | None = None,
        vo: QuantityLike | None = None,
    ) -> object: ...
    def __init__(
        self,
        amp: QuantityLike = 1.0,
        A: Callable[[float], float] | None = None,
        pot: Potential | list[Potential] | None = None,
        ro: QuantityLike | None = None,
        vo: QuantityLike | None = None,
    ) -> None: ...

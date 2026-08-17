from .Potential import Potential
from .WrapperPotential import WrapperPotential
from ._typing import QuantityLike

class KuzminLikeWrapperPotential(WrapperPotential):
    def __init__(
        self,
        amp: QuantityLike = 1.0,
        a: QuantityLike = 1.1,
        b: QuantityLike = 0.0,
        pot: Potential | list[Potential] | None = None,
        ro: QuantityLike | None = None,
        vo: QuantityLike | None = None,
    ) -> None: ...

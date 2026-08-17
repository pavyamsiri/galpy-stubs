from ._typing import Numeric, QuantityLike
from .linearCompositePotential import linearCompositePotential
from .linearPotential import linearPotential

class verticalPotential(linearPotential):
    def __init__(
        self,
        Pot: object,
        R: Numeric | QuantityLike = 1.0,
        phi: Numeric | QuantityLike | None = None,
        t0: Numeric | QuantityLike = 0.0,
    ) -> None: ...

def RZToverticalPotential(
    RZPot: object,
    R: Numeric | QuantityLike,
) -> linearCompositePotential | verticalPotential | linearPotential: ...
def toVerticalPotential(
    Pot: object,
    R: Numeric | QuantityLike,
    phi: Numeric | QuantityLike | None = None,
    t0: Numeric | QuantityLike = 0.0,
) -> linearCompositePotential | verticalPotential | linearPotential: ...

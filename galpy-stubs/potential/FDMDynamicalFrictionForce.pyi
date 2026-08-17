from collections.abc import Callable

from .ChandrasekharDynamicalFrictionForce import ChandrasekharDynamicalFrictionForce
from .Potential import Potential
from ._typing import Numeric, QuantityLike

class FDMDynamicalFrictionForce(ChandrasekharDynamicalFrictionForce):
    def __init__(
        self,
        amp: QuantityLike = 1.0,
        GMs: QuantityLike = 0.1,
        gamma: float = 1.0,
        rhm: QuantityLike = 0.0,
        m: QuantityLike = 1e-99,
        dens: Potential | list[Potential] | None = None,
        sigmar: Callable[[Numeric], Numeric] | None = None,
        const_lnLambda: bool | float = False,
        const_FDMfactor: bool | float = False,
        minr: QuantityLike = 0.0001,
        maxr: QuantityLike = 25.0,
        nr: int = 501,
        ro: QuantityLike | None = None,
        vo: QuantityLike | None = None,
    ) -> None: ...
    def krValue(self, r: float, v: float) -> float: ...
    def M_sigma(self, r: float, v: float) -> float: ...

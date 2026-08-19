from ._typing import QuantityLike, TimeDependentVector, TimeFunction
from .DissipativeForce import DissipativeForce

class NonInertialFrameForce(DissipativeForce):
    def __init__(
        self,
        amp: QuantityLike = 1.0,
        Omega: TimeDependentVector | None = None,
        Omegadot: TimeDependentVector | None = None,
        x0: list[TimeFunction] | None = None,
        v0: list[TimeFunction] | None = None,
        a0: TimeDependentVector | None = None,
        cinterp: bool = True,
        cinterp_n: int = 3000,
        ro: QuantityLike | None = None,
        vo: QuantityLike | None = None,
    ) -> None: ...

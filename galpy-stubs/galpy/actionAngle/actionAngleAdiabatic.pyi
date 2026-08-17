from .actionAngle import (
    ActionFrequencyAngleResult,
    ActionFrequencyResult,
    SphericalActionResult,
    actionAngle,
)
from ..potential.Potential import Potential
from ..potential._typing import Numeric, QuantityLike

class actionAngleAdiabatic(actionAngle):
    def __init__(
        self,
        *,
        pot: Potential | list[Potential],
        gamma: float = 1.0,
        ro: QuantityLike | None = None,
        vo: QuantityLike | None = None,
    ) -> None: ...
    def __call__(
        self,
        R: Numeric,
        vR: Numeric,
        vT: Numeric,
        z: Numeric,
        vz: Numeric,
        phi: Numeric = 0.0,
    ) -> SphericalActionResult: ...
    def actionsFreqs(
        self,
        R: Numeric,
        vR: Numeric,
        vT: Numeric,
        z: Numeric,
        vz: Numeric,
        phi: Numeric = 0.0,
    ) -> ActionFrequencyResult | tuple[Numeric, ...]: ...
    def actionsFreqsAngles(
        self,
        R: Numeric,
        vR: Numeric,
        vT: Numeric,
        z: Numeric,
        vz: Numeric,
        phi: Numeric = 0.0,
    ) -> ActionFrequencyAngleResult | tuple[Numeric, ...]: ...

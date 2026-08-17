from .actionAngle import actionAngle
from .actionAngle import (
    ActionFrequencyAngleResult,
    ActionFrequencyResult,
    SphericalActionResult,
)
from ..potential.Potential import Potential
from ..potential._typing import Numeric, QuantityLike

class actionAngleSpherical(actionAngle):
    def __init__(
        self,
        *,
        pot: Potential | list[Potential],
        ro: QuantityLike | None = None,
        vo: QuantityLike | None = None,
        _gamma: float = 0.0,
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
    ) -> (
        ActionFrequencyResult
        | tuple[Numeric, Numeric, Numeric, Numeric, Numeric, Numeric]
    ): ...
    def actionsFreqsAngles(
        self,
        R: Numeric,
        vR: Numeric,
        vT: Numeric,
        z: Numeric,
        vz: Numeric,
        phi: Numeric = 0.0,
    ) -> (
        ActionFrequencyAngleResult
        | tuple[
            Numeric,
            Numeric,
            Numeric,
            Numeric,
            Numeric,
            Numeric,
            Numeric,
            Numeric,
            Numeric,
        ]
    ): ...

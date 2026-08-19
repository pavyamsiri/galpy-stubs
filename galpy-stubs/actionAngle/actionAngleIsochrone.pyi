from ..potential._typing import Numeric, QuantityLike
from ..potential.IsochronePotential import IsochronePotential
from .actionAngle import (
    ActionFrequencyAngleResult,
    ActionFrequencyResult,
    SphericalActionResult,
    actionAngle,
)

class actionAngleIsochrone(actionAngle):
    def __init__(
        self,
        *,
        b: QuantityLike | None = None,
        ip: IsochronePotential | None = None,
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

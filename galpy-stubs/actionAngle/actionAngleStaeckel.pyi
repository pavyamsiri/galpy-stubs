from ..potential._typing import Numeric, QuantityLike
from ..potential.Potential import Potential
from .actionAngle import (
    ActionFrequencyAngleResult,
    ActionFrequencyResult,
    SphericalActionResult,
    actionAngle,
)

class actionAngleStaeckel(actionAngle):
    def __init__(
        self,
        *,
        pot: Potential | list[Potential],
        delta: QuantityLike,
        useu0: bool = False,
        c: bool = False,
        order: int = 10,
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

class actionAngleStaeckelSingle(actionAngle):
    def __init__(
        self,
        *,
        pot: Potential | list[Potential],
        delta: QuantityLike,
        ro: QuantityLike | None = None,
        vo: QuantityLike | None = None,
    ) -> None: ...

def estimateDeltaStaeckel(
    pot: Potential | list[Potential],
    R: Numeric,
    z: Numeric,
    no_median: bool = False,
    delta0: Numeric = 1e-6,
) -> Numeric: ...

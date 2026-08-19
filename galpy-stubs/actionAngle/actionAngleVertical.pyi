from ..potential._typing import Numeric, QuantityLike
from ..potential.linearPotential import linearPotential
from .actionAngle import (
    ActionFrequencyAngleResult,
    ActionFrequencyResult,
    ActionResult,
    actionAngle,
)

class actionAngleVertical(actionAngle):
    def __init__(
        self,
        *,
        pot: linearPotential | list[linearPotential],
        ro: QuantityLike | None = None,
        vo: QuantityLike | None = None,
    ) -> None: ...
    def __call__(self, x: Numeric, vx: Numeric) -> ActionResult: ...
    def actionsFreqs(self, x: Numeric, vx: Numeric) -> ActionFrequencyResult: ...
    def actionsFreqsAngles(
        self, x: Numeric, vx: Numeric
    ) -> ActionFrequencyAngleResult: ...
    def calcxmax(
        self, x: Numeric, vx: Numeric, E: Numeric | None = None
    ) -> Numeric: ...

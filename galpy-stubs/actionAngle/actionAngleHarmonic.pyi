from ..potential._typing import Numeric, QuantityLike
from .actionAngle import (
    ActionFrequencyAngleResult,
    ActionFrequencyResult,
    ActionResult,
    actionAngle,
)

class actionAngleHarmonic(actionAngle):
    def __init__(
        self,
        *,
        omega: QuantityLike,
        ro: QuantityLike | None = None,
        vo: QuantityLike | None = None,
    ) -> None: ...
    def __call__(self, x: Numeric, vx: Numeric) -> ActionResult: ...
    def actionsFreqs(self, x: Numeric, vx: Numeric) -> ActionFrequencyResult: ...
    def actionsFreqsAngles(
        self, x: Numeric, vx: Numeric
    ) -> ActionFrequencyAngleResult: ...

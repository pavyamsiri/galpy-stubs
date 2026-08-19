from optype import numpy as onp

from ..potential._typing import QuantityLike

type ActionResult = onp.ArrayND | float
type ActionFrequencyResult = tuple[ActionResult, ActionResult]
type ActionFrequencyAngleResult = tuple[ActionResult, ActionResult, ActionResult]
type SphericalActionResult = tuple[ActionResult, ActionResult, ActionResult]
type SphericalActionFrequencyResult = tuple[
    ActionResult, ActionResult, ActionResult, ActionResult, ActionResult, ActionResult
]

class actionAngle:
    def __init__(
        self, ro: QuantityLike | None = None, vo: QuantityLike | None = None
    ) -> None: ...
    def turn_physical_off(self) -> None: ...
    def turn_physical_on(
        self, ro: QuantityLike | None = None, vo: QuantityLike | None = None
    ) -> None: ...

class UnboundError(Exception):
    def __init__(self, value: object) -> None: ...

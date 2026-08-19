from optype import numpy as onp

from ..potential._typing import Numeric, QuantityLike
from ..potential.IsochronePotential import IsochronePotential
from ..potential.Potential import Potential
from .actionAngle import (
    ActionResult,
    actionAngle,
)
from .actionAngleIsochrone import actionAngleIsochrone

class actionAngleIsochroneApprox(actionAngle):
    def __init__(
        self,
        *,
        pot: Potential | list[Potential],
        b: Numeric | None = None,
        ip: IsochronePotential | None = None,
        aAI: actionAngleIsochrone | None = None,
        tintJ: Numeric = 100.0,
        ntintJ: int = 10000,
        integrate_method: str = "dopr54_c",
        dt: Numeric | None = None,
        maxn: int = 3,
        ro: Numeric | None = None,
        vo: Numeric | None = None,
        c: bool = True,
    ) -> None: ...
    def __call__(self, *args: object, **kwargs: object) -> object: ...
    def actionsFreqs(
        self, *args: object, **kwargs: object
    ) -> tuple[
        ActionResult,
        ActionResult,
        ActionResult,
        ActionResult,
        ActionResult,
        ActionResult,
    ]: ...
    def actionsFreqsAngles(
        self, *args: object, **kwargs: object
    ) -> tuple[
        ActionResult,
        ActionResult,
        ActionResult,
        ActionResult,
        ActionResult,
        ActionResult,
        ActionResult,
        ActionResult,
        ActionResult,
    ]: ...
    def plot(self, *args: object, **kwargs: object) -> None: ...

def estimateBIsochrone(
    pot: Potential | list[Potential],
    R: Numeric | QuantityLike,
    z: Numeric | QuantityLike,
    phi: Numeric | QuantityLike | None = None,
) -> Numeric | onp.ArrayND | tuple[Numeric, Numeric, Numeric]: ...
def dePeriod(arr: onp.ArrayND) -> onp.ArrayND: ...

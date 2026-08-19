from ..potential._typing import QuantityLike
from ..potential.IsochronePotential import IsochronePotential
from .actionAngleInverse import actionAngleInverse

class actionAngleIsochroneInverse(actionAngleInverse):
    def __init__(
        self,
        *,
        b: QuantityLike | None = None,
        ip: IsochronePotential | None = None,
        ro: QuantityLike | None = None,
        vo: QuantityLike | None = None,
    ) -> None: ...

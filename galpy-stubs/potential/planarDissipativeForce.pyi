from typing import override

from ._typing import QuantityLike, Numeric
from .planarForce import planarForce

class planarDissipativeForce(planarForce):
    isDissipative: bool
    def __init__(
        self,
        amp: QuantityLike = 1.0,
        ro: QuantityLike | None = None,
        vo: QuantityLike | None = None,
        amp_units: str | None = None,
    ) -> None: ...
    @override
    def Rforce(
        self, R: Numeric, phi: Numeric = 0.0, t: Numeric = 0.0, v: object | None = None
    ) -> Numeric: ...
    @override
    def phitorque(
        self, R: Numeric, phi: Numeric = 0.0, t: Numeric = 0.0, v: object | None = None
    ) -> Numeric: ...

class planarDissipativeForceFromFullDissipativeForce(planarDissipativeForce):
    def __init__(self, Pot: object) -> None: ...

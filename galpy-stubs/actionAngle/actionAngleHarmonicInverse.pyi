from ..potential._typing import QuantityLike
from .actionAngleInverse import actionAngleInverse

class actionAngleHarmonicInverse(actionAngleInverse):
    def __init__(
        self,
        *,
        omega: QuantityLike,
        ro: QuantityLike | None = None,
        vo: QuantityLike | None = None,
    ) -> None: ...

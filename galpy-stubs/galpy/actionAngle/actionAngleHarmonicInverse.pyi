from .actionAngleInverse import actionAngleInverse
from ..potential._typing import QuantityLike

class actionAngleHarmonicInverse(actionAngleInverse):
    def __init__(
        self,
        *,
        omega: QuantityLike,
        ro: QuantityLike | None = None,
        vo: QuantityLike | None = None,
    ) -> None: ...

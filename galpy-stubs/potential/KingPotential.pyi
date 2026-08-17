from ._typing import QuantityLike
from .interpSphericalPotential import interpSphericalPotential

class KingPotential(interpSphericalPotential):
    def __init__(
        self,
        W0: float = 2.0,
        M: QuantityLike = 3.0,
        rt: QuantityLike = 1.5,
        npt: int = 1001,
        _sfkdf: object | None = None,
        ro: QuantityLike | None = None,
        vo: QuantityLike | None = None,
    ) -> None: ...

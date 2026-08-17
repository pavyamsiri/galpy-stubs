from ._typing import QuantityLike
from .planarPotential import planarPotential

class CosmphiDiskPotential(planarPotential):
    def __init__(
        self,
        amp: QuantityLike = 1.0,
        phib: QuantityLike = 0.4363323129985824,
        p: float = 1.0,
        phio: QuantityLike = 0.01,
        m: int = 4,
        r1: QuantityLike = 1.0,
        rb: QuantityLike | None = None,
        cp: QuantityLike | None = None,
        sp: QuantityLike | None = None,
        ro: QuantityLike | None = None,
        vo: QuantityLike | None = None,
    ) -> None: ...

class LopsidedDiskPotential(CosmphiDiskPotential):
    def __init__(
        self,
        amp: QuantityLike = 1.0,
        phib: QuantityLike = 0.4363323129985824,
        p: float = 1.0,
        phio: QuantityLike = 0.01,
        r1: QuantityLike = 1.0,
        cp: QuantityLike | None = None,
        sp: QuantityLike | None = None,
        ro: QuantityLike | None = None,
        vo: QuantityLike | None = None,
    ) -> None: ...

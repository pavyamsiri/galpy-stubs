from .EllipsoidalPotential import EllipsoidalPotential
from ._typing import CoordinateLike, QuantityLike

class TwoPowerTriaxialPotential(EllipsoidalPotential):
    def __init__(
        self,
        amp: QuantityLike = 1.0,
        a: QuantityLike = 1.0,
        alpha: float = 1.0,
        beta: float = 3.0,
        b: float = 1.0,
        c: float = 1.0,
        zvec: CoordinateLike | None = None,
        pa: QuantityLike | None = None,
        glorder: int = 50,
        normalize: bool | float = False,
        ro: QuantityLike | None = None,
        vo: QuantityLike | None = None,
    ) -> None: ...

class TriaxialHernquistPotential(EllipsoidalPotential):
    def __init__(
        self,
        amp: QuantityLike = 1.0,
        a: QuantityLike = 2.0,
        normalize: bool | float = False,
        b: float = 1.0,
        c: float = 1.0,
        zvec: CoordinateLike | None = None,
        pa: QuantityLike | None = None,
        glorder: int = 50,
        ro: QuantityLike | None = None,
        vo: QuantityLike | None = None,
    ) -> None: ...

class TriaxialJaffePotential(EllipsoidalPotential):
    def __init__(
        self,
        amp: QuantityLike = 1.0,
        a: QuantityLike = 2.0,
        b: float = 1.0,
        c: float = 1.0,
        zvec: CoordinateLike | None = None,
        pa: QuantityLike | None = None,
        normalize: bool | float = False,
        glorder: int = 50,
        ro: QuantityLike | None = None,
        vo: QuantityLike | None = None,
    ) -> None: ...

class TriaxialNFWPotential(EllipsoidalPotential):
    def __init__(
        self,
        amp: QuantityLike = 1.0,
        a: QuantityLike = 2.0,
        b: float = 1.0,
        c: float = 1.0,
        zvec: CoordinateLike | None = None,
        pa: QuantityLike | None = None,
        normalize: bool | float = False,
        conc: float | None = None,
        mvir: QuantityLike | None = None,
        glorder: int = 50,
        vo: QuantityLike | None = None,
        ro: QuantityLike | None = None,
        H: float = 70.0,
        Om: float = 0.3,
        overdens: float = 200.0,
        wrtcrit: bool = False,
    ) -> None: ...

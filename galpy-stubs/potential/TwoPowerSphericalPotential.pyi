from ._typing import QuantityLike
from .Potential import Potential

class TwoPowerSphericalPotential(Potential):
    def __init__(
        self,
        amp: QuantityLike = 1.0,
        a: QuantityLike = 5.0,
        alpha: float = 1.5,
        beta: float = 3.5,
        normalize: bool | float = False,
        ro: QuantityLike | None = None,
        vo: QuantityLike | None = None,
    ) -> None: ...

class DehnenSphericalPotential(TwoPowerSphericalPotential):
    def __init__(
        self,
        amp: QuantityLike = 1.0,
        a: QuantityLike = 1.0,
        alpha: float = 1.0,
        normalize: bool | float = False,
        ro: QuantityLike | None = None,
        vo: QuantityLike | None = None,
    ) -> None: ...

class DehnenCoreSphericalPotential(DehnenSphericalPotential):
    def __init__(
        self,
        amp: QuantityLike = 1.0,
        a: QuantityLike = 1.0,
        normalize: bool | float = False,
        ro: QuantityLike | None = None,
        vo: QuantityLike | None = None,
    ) -> None: ...

class HernquistPotential(DehnenSphericalPotential):
    def __init__(
        self,
        amp: QuantityLike = 1.0,
        a: QuantityLike = 1.0,
        normalize: bool | float = False,
        ro: QuantityLike | None = None,
        vo: QuantityLike | None = None,
    ) -> None: ...

class JaffePotential(DehnenSphericalPotential):
    def __init__(
        self,
        amp: QuantityLike = 1.0,
        a: QuantityLike = 1.0,
        normalize: bool | float = False,
        ro: QuantityLike | None = None,
        vo: QuantityLike | None = None,
    ) -> None: ...

class NFWPotential(TwoPowerSphericalPotential):
    def __init__(
        self,
        amp: QuantityLike = 1.0,
        a: QuantityLike = 1.0,
        normalize: bool | float = False,
        ro: QuantityLike | None = None,
        vo: QuantityLike | None = None,
    ) -> None: ...

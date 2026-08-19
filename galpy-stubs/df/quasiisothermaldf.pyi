from ..actionAngle.actionAngle import actionAngle
from ..potential._typing import QuantityLike
from ..potential.Potential import Potential
from .df import df

class quasiisothermaldf(df):
    def __init__(
        self,
        hr: QuantityLike,
        sr: QuantityLike,
        sz: QuantityLike,
        hsr: QuantityLike,
        hsz: QuantityLike,
        pot: Potential | list[Potential] | None = None,
        aA: actionAngle | None = None,
        cutcounter: bool = False,
        _precomputerg: bool = True,
        _precomputergrmax: QuantityLike | None = None,
        _precomputergnLz: int = 51,
        refr: QuantityLike = 1.0,
        lo: QuantityLike = 0.005681818181818182,
        ro: QuantityLike | None = None,
        vo: QuantityLike | None = None,
    ) -> None: ...
    def __call__(self, *args: object, **kwargs: object) -> object: ...

from .Potential import Potential
from ._typing import GridSpec, QuantityLike

class interpRZPotential(Potential):
    def __init__(
        self,
        RZPot: Potential | list[Potential] | None = None,
        rgrid: GridSpec = ...,
        zgrid: GridSpec = ...,
        logR: bool = True,
        interpPot: bool = False,
        interpRforce: bool = False,
        interpzforce: bool = False,
        interpDens: bool = False,
        interpvcirc: bool = False,
        interpdvcircdr: bool = False,
        interpepifreq: bool = False,
        interpverticalfreq: bool = False,
        ro: QuantityLike | None = None,
        vo: QuantityLike | None = None,
        use_c: bool = False,
        enable_c: bool = False,
        zsym: bool = True,
        numcores: int | None = None,
        interpR2deriv: bool = False,
        interpz2deriv: bool = False,
        interpRzderiv: bool = False,
    ) -> None: ...

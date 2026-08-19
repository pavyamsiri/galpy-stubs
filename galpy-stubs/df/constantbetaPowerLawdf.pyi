from typing import override

from optype import numpy as onp

from ..potential._typing import QuantityLike
from ..potential.Potential import Potential
from .constantbetadf import _constantbetadf

class constantbetaPowerLawdf(_constantbetadf):
    def __init__(
        self,
        pot: Potential | list[Potential] | None = None,
        denspot: Potential | list[Potential] | None = None,
        beta: float = 0.0,
        rmax: QuantityLike = 10000.0,
        rmin: QuantityLike | None = None,
        ro: QuantityLike | None = None,
        vo: QuantityLike | None = None,
    ) -> None: ...
    @override
    def fE(self, E: onp.ArrayND) -> onp.ArrayND: ...

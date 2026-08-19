from typing import override

from optype import numpy as onp

from ..potential._typing import QuantityLike
from ..potential.Potential import Potential
from .constantbetadf import _constantbetadf

class constantbetaHernquistdf(_constantbetadf):
    def __init__(
        self,
        pot: Potential | list[Potential] | None = None,
        beta: float = 0.0,
        ro: QuantityLike | None = None,
        vo: QuantityLike | None = None,
    ) -> None: ...
    @override
    def fE(self, E: onp.ArrayND) -> onp.ArrayND: ...

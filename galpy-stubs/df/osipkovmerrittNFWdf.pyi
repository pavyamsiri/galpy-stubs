from .osipkovmerrittdf import _osipkovmerrittdf
from typing import override
from ..potential.Potential import Potential
from ..potential._typing import QuantityLike
from optype import numpy as onp

class osipkovmerrittNFWdf(_osipkovmerrittdf):
    def __init__(
        self,
        pot: Potential | list[Potential] | None = None,
        ra: QuantityLike = 1.4,
        rmax: QuantityLike = 10000.0,
        ro: QuantityLike | None = None,
        vo: QuantityLike | None = None,
    ) -> None: ...
    @override
    def fQ(self, Q: onp.ArrayND) -> onp.ArrayND: ...

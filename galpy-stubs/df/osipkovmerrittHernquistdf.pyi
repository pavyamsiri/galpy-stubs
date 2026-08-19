from typing import override

from optype import numpy as onp

from ..potential._typing import QuantityLike
from ..potential.Potential import Potential
from .osipkovmerrittdf import _osipkovmerrittdf

class osipkovmerrittHernquistdf(_osipkovmerrittdf):
    def __init__(
        self,
        pot: Potential | list[Potential] | None = None,
        ra: QuantityLike = 1.4,
        ro: QuantityLike | None = None,
        vo: QuantityLike | None = None,
    ) -> None: ...
    @override
    def fQ(self, Q: onp.ArrayND) -> onp.ArrayND: ...

from typing import override

from ._typing import QuantityLike
from .baseCompositePotential import baseCompositePotential
from .DissipativeForce import DissipativeForce
from .Force import Force
from .Potential import Potential

class CompositePotential(baseCompositePotential, DissipativeForce, Potential):
    def __init__(
        self,
        *args: Force | Potential | list[Force | Potential],
        ro: QuantityLike | None = None,
        vo: QuantityLike | None = None,
    ) -> None: ...
    @override
    def __add__(self, b: Force | Potential) -> CompositePotential: ...
    @override
    def nemo_accname(self) -> str: ...
    @override
    def nemo_accpars(self, vo: object, ro: object) -> str: ...

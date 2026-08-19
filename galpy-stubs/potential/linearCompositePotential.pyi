from typing import override

from ._typing import QuantityLike
from .baseCompositePotential import baseCompositePotential
from .linearPotential import linearPotential

class linearCompositePotential(baseCompositePotential, linearPotential):
    def __init__(
        self,
        *args: linearPotential | list[linearPotential],
        ro: QuantityLike | None = None,
        vo: QuantityLike | None = None,
    ) -> None: ...
    @override
    def __add__(self, b: linearPotential) -> linearCompositePotential: ...

from typing import override

from .baseCompositePotential import baseCompositePotential
from .linearPotential import linearPotential
from ._typing import QuantityLike

class linearCompositePotential(baseCompositePotential, linearPotential):
    def __init__(
        self,
        *args: linearPotential | list[linearPotential],
        ro: QuantityLike | None = None,
        vo: QuantityLike | None = None,
    ) -> None: ...
    @override
    def __add__(self, b: linearPotential) -> linearCompositePotential: ...

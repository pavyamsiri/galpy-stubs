from typing import override

from .baseCompositePotential import baseCompositePotential
from .planarDissipativeForce import planarDissipativeForce
from .planarForce import planarForce
from .planarPotential import planarPotential
from ._typing import QuantityLike

class planarCompositePotential(
    baseCompositePotential, planarDissipativeForce, planarPotential
):
    def __init__(
        self,
        *args: planarForce | list[planarForce],
        ro: QuantityLike | None = None,
        vo: QuantityLike | None = None,
    ) -> None: ...
    @override
    def __add__(self, b: planarForce) -> planarCompositePotential: ...

from optype import numpy as onp

from ..potential.linearPotential import linearPotential
from .actionAngleInverse import actionAngleInverse

class actionAngleVerticalInverse(actionAngleInverse):
    def __init__(
        self,
        *,
        pot: linearPotential | list[linearPotential],
        Es: onp.ArrayND,
        nta: int = 128,
        setup_interp: bool = False,
        use_pointtransform: bool = False,
        pt_deg: int = 7,
        pt_nxa: int = 301,
        maxiter: int = 100,
        angle_tol: float = 1e-12,
        bisect: bool = False,
    ) -> None: ...

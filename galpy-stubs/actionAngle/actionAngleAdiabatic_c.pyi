from optype import numpy as onp

from ..potential.Potential import Potential
from ..potential._typing import Numeric

def actionAngleAdiabatic_c(
    pot: Potential | list[Potential],
    gamma: Numeric,
    R: onp.ArrayND,
    vR: onp.ArrayND,
    vT: onp.ArrayND,
    z: onp.ArrayND,
    vz: onp.ArrayND,
) -> tuple[onp.ArrayND, onp.ArrayND, int]: ...
def actionAngleRperiRapZmaxAdiabatic_c(
    pot: Potential | list[Potential],
    gamma: Numeric,
    R: onp.ArrayND,
    vR: onp.ArrayND,
    vT: onp.ArrayND,
    z: onp.ArrayND,
    vz: onp.ArrayND,
) -> tuple[onp.ArrayND, onp.ArrayND, onp.ArrayND, int]: ...

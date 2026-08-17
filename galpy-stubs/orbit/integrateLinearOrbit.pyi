from optype import numpy as onp

from ..potential.linearPotential import linearPotential

type IntegrationResult = tuple[onp.ArrayND, onp.ArrayND]

def integrateLinearOrbit_c(
    pot: linearPotential,
    yo: onp.ArrayND,
    t: onp.ArrayND,
    int_method: str,
    rtol: float | None = None,
    atol: float | None = None,
    progressbar: bool = True,
    dt: float | None = None,
) -> IntegrationResult: ...
def integrateLinearOrbit(
    pot: linearPotential,
    yo: onp.ArrayND,
    t: onp.ArrayND,
    int_method: str,
    rtol: float | None = None,
    atol: float | None = None,
    numcores: int = 1,
    progressbar: bool = True,
    dt: float | None = None,
) -> IntegrationResult: ...

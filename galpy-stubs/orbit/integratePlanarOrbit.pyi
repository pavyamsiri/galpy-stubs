from optype import numpy as onp

from ..potential.planarForce import planarForce
from ..potential.Potential import Potential

type PotentialInput = Potential | planarForce | list[Potential | planarForce]
type IntegrationResult = tuple[onp.ArrayND, onp.ArrayND]

def integratePlanarOrbit_c(
    pot: PotentialInput,
    yo: onp.ArrayND,
    t: onp.ArrayND,
    int_method: str,
    rtol: float | None = None,
    atol: float | None = None,
    progressbar: bool = True,
    dt: float | None = None,
) -> IntegrationResult: ...
def integratePlanarOrbit_dxdv_c(
    pot: PotentialInput,
    yo: onp.ArrayND,
    dyo: onp.ArrayND,
    t: onp.ArrayND,
    int_method: str,
    rtol: float | None = None,
    atol: float | None = None,
    dt: float | None = None,
) -> IntegrationResult: ...
def integratePlanarOrbit(
    pot: PotentialInput,
    yo: onp.ArrayND,
    t: onp.ArrayND,
    int_method: str,
    rtol: float | None = None,
    atol: float | None = None,
    numcores: int = 1,
    progressbar: bool = True,
    dt: float | None = None,
) -> IntegrationResult: ...
def integratePlanarOrbit_dxdv(
    pot: PotentialInput,
    yo: onp.ArrayND,
    dyo: onp.ArrayND,
    t: onp.ArrayND,
    int_method: str,
    rectIn: bool,
    rectOut: bool,
    rtol: float | None = None,
    atol: float | None = None,
    progressbar: bool = True,
    dt: float | None = None,
    numcores: int = 1,
) -> IntegrationResult: ...
def integratePlanarOrbit_sos(
    pot: PotentialInput,
    yo: onp.ArrayND,
    psi: float,
    t0: float,
    int_method: str,
    surface: str = "x",
    rtol: float | None = None,
    atol: float | None = None,
    numcores: int = 1,
    progressbar: bool = True,
    dpsi: float | None = None,
) -> IntegrationResult: ...
def integratePlanarOrbit_sos_c(
    pot: PotentialInput,
    yo: onp.ArrayND,
    psi: float,
    t0: float,
    int_method: str,
    surface: str = "x",
    rtol: float | None = None,
    atol: float | None = None,
    progressbar: bool = True,
    dpsi: float | None = None,
) -> IntegrationResult: ...

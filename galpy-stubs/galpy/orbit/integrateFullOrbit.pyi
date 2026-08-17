from optype import numpy as onp

from ..potential.Potential import Potential

type PotentialInput = Potential | list[Potential]
type IntegrationResult = tuple[onp.ArrayND, onp.ArrayND]

def integrateFullOrbit_c(
    pot: PotentialInput,
    yo: onp.ArrayND,
    t: onp.ArrayND,
    int_method: str,
    rtol: float | None = None,
    atol: float | None = None,
    progressbar: bool = True,
    dt: float | None = None,
) -> IntegrationResult: ...
def integrateFullOrbit_dxdv_c(
    pot: PotentialInput,
    yo: onp.ArrayND,
    dyo: onp.ArrayND,
    t: onp.ArrayND,
    int_method: str,
    dt: float | None = None,
    rtol: float | None = None,
    atol: float | None = None,
) -> IntegrationResult: ...
def integrateFullOrbit(
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
def integrateFullOrbit_dxdv(
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
def integrateFullOrbit_sos(
    pot: PotentialInput,
    yo: onp.ArrayND,
    psi: float,
    t0: float,
    int_method: str,
    rtol: float | None = None,
    atol: float | None = None,
    numcores: int = 1,
    progressbar: bool = True,
    dpsi: float | None = None,
) -> IntegrationResult: ...
def integrateFullOrbit_sos_c(
    pot: PotentialInput,
    yo: onp.ArrayND,
    psi: float,
    t0: float,
    int_method: str,
    rtol: float | None = None,
    atol: float | None = None,
    progressbar: bool = True,
    dpsi: float | None = None,
) -> IntegrationResult: ...

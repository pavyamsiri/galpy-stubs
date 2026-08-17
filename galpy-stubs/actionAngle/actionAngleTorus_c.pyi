from optype import numpy as onp

from ..potential.Potential import Potential
from ..potential._typing import Numeric

type TorusPotential = Potential | list[Potential]

def actionAngleTorus_xvFreqs_c(
    pot: TorusPotential,
    jr: Numeric,
    jphi: Numeric,
    jz: Numeric,
    angler: onp.Array1D,
    anglephi: onp.Array1D,
    anglez: onp.Array1D,
    tol: Numeric = 0.001,
) -> tuple[
    onp.ArrayND,
    onp.ArrayND,
    onp.ArrayND,
    onp.ArrayND,
    onp.ArrayND,
    onp.ArrayND,
    Numeric,
    Numeric,
    Numeric,
    int,
]: ...
def actionAngleTorus_Freqs_c(
    pot: TorusPotential, jr: Numeric, jphi: Numeric, jz: Numeric, tol: Numeric = 0.001
) -> tuple[Numeric, Numeric, Numeric, int]: ...
def actionAngleTorus_hessian_c(
    pot: TorusPotential,
    jr: Numeric,
    jphi: Numeric,
    jz: Numeric,
    tol: Numeric = 0.001,
    dJ: Numeric = 0.001,
) -> tuple[onp.Array2D, Numeric, Numeric, Numeric, int]: ...
def actionAngleTorus_jacobian_c(
    pot: TorusPotential,
    jr: Numeric,
    jphi: Numeric,
    jz: Numeric,
    angler: onp.Array1D,
    anglephi: onp.Array1D,
    anglez: onp.Array1D,
    tol: Numeric = 0.001,
    dJ: Numeric = 0.001,
) -> tuple[
    onp.ArrayND,
    onp.ArrayND,
    onp.ArrayND,
    onp.ArrayND,
    onp.ArrayND,
    onp.ArrayND,
    onp.Array3D,
    onp.Array2D,
    Numeric,
    Numeric,
    Numeric,
    int,
]: ...

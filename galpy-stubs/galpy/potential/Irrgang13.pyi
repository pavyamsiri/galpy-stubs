from optype import numpy as onp

from ._typing import Numeric

type DensityInput = Numeric | onp.ArrayND

mgal_in_msun: float
Irrgang13I_bulge: object
Irrgang13I_disk: object
Irrgang13I_halo: object
Irrgang13I: object
Irrgang13II_bulge: object
Irrgang13II_disk: object
Irrgang13II_halo: object
Irrgang13II: object
Irrgang13III_bulge: object
Irrgang13III_disk: object
Irrgang13III_halo: object
Irrgang13III: object

def Irrgang13I_halo_dens(
    r: DensityInput,
    amp: Numeric = ...,
    ah: Numeric = ...,
    gamma: Numeric = ...,
    Lambda: Numeric = ...,
) -> Numeric: ...
def Irrgang13II_halo_dens(
    r: DensityInput,
    amp: Numeric = ...,
    ah: Numeric = ...,
) -> Numeric: ...

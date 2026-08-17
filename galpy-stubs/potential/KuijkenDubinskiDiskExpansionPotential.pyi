from ._typing import DensityFunction, Number, Numeric, ProfileInput
from .Potential import Potential

class KuijkenDubinskiDiskExpansionPotential(Potential):
    def __init__(
        self,
        amp: Number = 1.0,
        dens: DensityFunction | None = None,
        Sigma: ProfileInput | None = None,
        hz: ProfileInput | None = None,
        Sigma_amp: Number | None = None,
        dSigmadR: DensityFunction | None = None,
        d2SigmadR2: DensityFunction | None = None,
        Hz: DensityFunction | None = None,
        dHzdz: DensityFunction | None = None,
        ro: Numeric | None = None,
        vo: Numeric | None = None,
    ) -> None: ...

def phiME_dens(
    R: Numeric,
    z: Numeric,
    phi: Numeric,
    dens: DensityFunction,
    Sigma: ProfileInput,
    dSigmadR: DensityFunction,
    d2SigmadR2: DensityFunction,
    hz: ProfileInput,
    Hz: DensityFunction,
    dHzdz: DensityFunction,
    Sigma_amp: Number,
) -> Numeric: ...

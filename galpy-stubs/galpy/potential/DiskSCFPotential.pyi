from ._typing import DensityFunction, Number, Numeric, ProfileInput
from .KuijkenDubinskiDiskExpansionPotential import KuijkenDubinskiDiskExpansionPotential

class DiskSCFPotential(KuijkenDubinskiDiskExpansionPotential):
    def __init__(
        self,
        amp: Number = 1.0,
        normalize: bool | Number = False,
        dens: DensityFunction | None = None,
        Sigma: ProfileInput | None = None,
        hz: ProfileInput | None = None,
        Sigma_amp: Number | None = None,
        dSigmadR: DensityFunction | None = None,
        d2SigmadR2: DensityFunction | None = None,
        Hz: DensityFunction | None = None,
        dHzdz: DensityFunction | None = None,
        N: int = 10,
        L: int = 10,
        a: Numeric = 1.0,
        radial_order: int | None = None,
        costheta_order: int | None = None,
        phi_order: int | None = None,
        ro: Numeric | None = None,
        vo: Numeric | None = None,
    ) -> None: ...

from ._typing import DensityFunction, Number, Numeric, ProfileInput
from .KuijkenDubinskiDiskExpansionPotential import KuijkenDubinskiDiskExpansionPotential

class DiskMultipoleExpansionPotential(KuijkenDubinskiDiskExpansionPotential):
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
        L: int = 10,
        rgrid: Numeric | None = None,
        symmetry: str | None = None,
        costheta_order: int | None = None,
        phi_order: int | None = None,
        ro: Numeric | None = None,
        vo: Numeric | None = None,
    ) -> None: ...

from collections.abc import Callable
from typing import Literal, Self

from optype import numpy as onp

from ._typing import DensityFunction, Number, Numeric
from .Potential import Potential
from .SphericalHarmonicPotentialMixin import SphericalHarmonicPotentialMixin

type SplineGrid = onp.ArrayND | list[Callable[..., Numeric]] | None

class MultipoleExpansionPotential(Potential, SphericalHarmonicPotentialMixin):
    def __init__(
        self,
        amp: Number = 1.0,
        rho_cos_splines: SplineGrid = None,
        rho_sin_splines: SplineGrid = None,
        rgrid: onp.ArrayND = ...,
        tgrid: onp.ArrayND | None = None,
        normalize: bool | Number = False,
        ro: Numeric | None = None,
        vo: Numeric | None = None,
    ) -> None: ...
    @classmethod
    def from_density(
        cls,
        dens: DensityFunction,
        L: int = 6,
        rgrid: onp.ArrayND = ...,
        tgrid: onp.ArrayND | None = None,
        symmetry: str | None = None,
        costheta_order: int | None = None,
        phi_order: int | None = None,
        amp: Number = 1.0,
        normalize: bool | Number = False,
        ro: Numeric | None = None,
        vo: Numeric | None = None,
    ) -> Self: ...
    def OmegaP(self) -> Literal[0]: ...

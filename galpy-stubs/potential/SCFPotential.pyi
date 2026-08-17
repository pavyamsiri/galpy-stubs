from typing import Literal, Self

from optype import numpy as onp

from ._typing import CoefficientArray, DensityFunction, Number, Numeric
from .Potential import Potential
from .SphericalHarmonicPotentialMixin import SphericalHarmonicPotentialMixin

class SCFPotential(Potential, SphericalHarmonicPotentialMixin):
    def __init__(
        self,
        amp: Number = 1.0,
        Acos: CoefficientArray = ...,
        Asin: CoefficientArray | None = None,
        a: Numeric = 1.0,
        normalize: bool | Number = False,
        ro: Numeric | None = None,
        vo: Numeric | None = None,
    ) -> None: ...
    @classmethod
    def from_density(
        cls,
        dens: DensityFunction,
        N: int,
        L: int = 0,
        a: Numeric = 1.0,
        symmetry: str | None = None,
        radial_order: int | None = None,
        costheta_order: int | None = None,
        phi_order: int | None = None,
        ro: Numeric | None = None,
        vo: Numeric | None = None,
    ) -> Self: ...
    def OmegaP(self) -> Literal[0]: ...

def scf_compute_coeffs_spherical_nbody(
    pos: onp.ArrayND,
    N: int,
    mass: Number | onp.ArrayND = 1.0,
    a: Numeric = 1.0,
) -> tuple[CoefficientArray, None]: ...
def scf_compute_coeffs_spherical(
    dens: DensityFunction,
    N: int,
    a: Numeric = 1.0,
    radial_order: int | None = None,
) -> tuple[CoefficientArray, None]: ...
def scf_compute_coeffs_axi_nbody(
    Rz: onp.ArrayND,
    N: int,
    L: int,
    mass: Number | onp.ArrayND = 1.0,
    a: Numeric = 1.0,
) -> tuple[CoefficientArray, None]: ...
def scf_compute_coeffs_axi(
    dens: DensityFunction,
    N: int,
    L: int,
    a: Numeric = 1.0,
    radial_order: int | None = None,
    costheta_order: int | None = None,
) -> tuple[CoefficientArray, None]: ...
def scf_compute_coeffs_nbody(
    pos: onp.ArrayND,
    N: int,
    L: int,
    mass: Number | onp.ArrayND = 1.0,
    a: Numeric = 1.0,
) -> tuple[CoefficientArray, CoefficientArray]: ...
def scf_compute_coeffs(
    dens: DensityFunction,
    N: int,
    L: int,
    a: Numeric = 1.0,
    radial_order: int | None = None,
    costheta_order: int | None = None,
    phi_order: int | None = None,
) -> tuple[CoefficientArray, CoefficientArray]: ...

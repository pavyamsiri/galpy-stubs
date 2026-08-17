from ._typing import Numeric

def expexp_dens(
    R: Numeric, z: Numeric, Rd: Numeric, zd: Numeric, Sigma0: Numeric
) -> Numeric:
    """Density for an exponential radial and vertical disk."""
    ...

def expexp_dens_with_hole(
    R: Numeric, z: Numeric, Rd: Numeric, Rm: Numeric, zd: Numeric, Sigma0: Numeric
) -> Numeric: ...
def expsech2_dens_with_hole(
    R: Numeric, z: Numeric, Rd: Numeric, Rm: Numeric, zd: Numeric, Sigma0: Numeric
) -> Numeric: ...
def core_pow_dens_with_cut(
    R: Numeric,
    z: Numeric,
    alpha: Numeric,
    r0: Numeric,
    rcut: Numeric,
    rho0: Numeric,
    q: Numeric,
) -> Numeric: ...
def pow_dens_with_cut(
    R: Numeric,
    z: Numeric,
    alpha: Numeric,
    r0: Numeric,
    rcut: Numeric,
    rho0: Numeric,
    q: Numeric,
) -> Numeric: ...

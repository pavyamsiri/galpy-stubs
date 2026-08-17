from ._typing import Numeric

type ModelValue = Numeric | object

old_error_settings: object
ro: ModelValue
vo: ModelValue
sigo: ModelValue
rhoo: ModelValue
Rd_HI: ModelValue
Rm_HI: ModelValue
zd_HI: ModelValue
Sigma0_HI: ModelValue
Rd_H2: ModelValue
Rm_H2: ModelValue
zd_H2: ModelValue
Sigma0_H2: ModelValue
Sigma0_thin: ModelValue
Rd_thin: ModelValue
zd_thin: ModelValue
Sigma0_thick: ModelValue
Rd_thick: ModelValue
zd_thick: ModelValue
rho0_bulge: ModelValue
r0_bulge: ModelValue
rcut: ModelValue
rho0_halo: ModelValue
rh: ModelValue

def gas_dens(R: Numeric, z: Numeric) -> Numeric: ...
def stellar_dens(R: Numeric, z: Numeric) -> Numeric: ...
def bulge_dens(R: Numeric, z: Numeric) -> Numeric: ...

sigmadict: dict[str, ModelValue]
hzdict: dict[str, ModelValue]
McMillan_bulge: object
McMillan_disk: object
McMillan_halo: object
McMillan17: object

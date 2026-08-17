from typing import assert_type

import numpy as np
from galpy.df.constantbetaHernquistdf import constantbetaHernquistdf
from galpy.df.constantbetaPowerLawdf import constantbetaPowerLawdf
from galpy.df.osipkovmerrittHernquistdf import osipkovmerrittHernquistdf
from galpy.df.osipkovmerrittNFWdf import osipkovmerrittNFWdf
from galpy.df.osipkovmerrittPowerLawdf import osipkovmerrittPowerLawdf
from galpy.potential.PowerSphericalPotential import PowerSphericalPotential
from galpy.potential.TwoPowerSphericalPotential import (
    HernquistPotential,
    NFWPotential,
)
from optype import numpy as onp

hernquist = HernquistPotential()
nfw = NFWPotential()
power_law = PowerSphericalPotential(alpha=2.5)

constant_hernquist = constantbetaHernquistdf(hernquist, beta=0.2)
constant_power_law = constantbetaPowerLawdf(power_law, beta=0.2, rmin=1e-5)
om_hernquist = osipkovmerrittHernquistdf(hernquist, ra=1.0)
om_nfw = osipkovmerrittNFWdf(nfw, ra=1.0)
om_power_law = osipkovmerrittPowerLawdf(power_law, ra=1.0, rmin=1e-5)

energy = np.array([-0.5])
assert_type(constant_hernquist.fE(energy), onp.ArrayND)
assert_type(constant_power_law.fE(energy), onp.ArrayND)
assert_type(om_hernquist.fQ(energy), onp.ArrayND)
assert_type(om_nfw.fQ(energy), onp.ArrayND)
assert_type(om_power_law.fQ(energy), onp.ArrayND)

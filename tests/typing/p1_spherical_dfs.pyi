from typing import assert_type

import numpy as np
from galpy.df.isotropicHernquistdf import isotropicHernquistdf
from galpy.df.isotropicNFWdf import isotropicNFWdf
from galpy.df.isotropicPlummerdf import isotropicPlummerdf
from galpy.df.isotropicPowerLawdf import isotropicPowerLawdf
from galpy.df.kingdf import kingdf
from galpy.potential.PlummerPotential import PlummerPotential
from galpy.potential.PowerSphericalPotential import PowerSphericalPotential
from galpy.potential.TwoPowerSphericalPotential import (
    HernquistPotential,
    NFWPotential,
)
from optype import numpy as onp

hernquist = isotropicHernquistdf(HernquistPotential())
nfw = isotropicNFWdf(NFWPotential())
plummer = isotropicPlummerdf(PlummerPotential())
power_law = isotropicPowerLawdf(PowerSphericalPotential(alpha=2.5))
king = kingdf(2.0)

energies = np.array([-0.5])
assert_type(hernquist.fE(energies), onp.ArrayND)
assert_type(nfw.fE(energies), onp.ArrayND)
assert_type(plummer.fE(energies), onp.ArrayND)
assert_type(power_law.fE(energies), onp.ArrayND)
assert_type(king.fE(energies), onp.ArrayND)

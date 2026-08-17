from typing import assert_type

from galpy.potential.BurkertPotential import BurkertPotential
from galpy.potential.DoubleExponentialDiskPotential import (
    DoubleExponentialDiskPotential,
)
from galpy.potential.EinastoPotential import EinastoPotential
from galpy.potential.ExpTruncNFWPotential import ExpTruncNFWPotential
from galpy.potential.FlattenedPowerPotential import FlattenedPowerPotential
from galpy.potential.HomogeneousSpherePotential import HomogeneousSpherePotential
from galpy.potential.KuzminDiskPotential import KuzminDiskPotential
from galpy.potential.PseudoIsothermalPotential import PseudoIsothermalPotential
from optype import numpy as onp

for potential in (
    BurkertPotential(),
    EinastoPotential(),
    ExpTruncNFWPotential(),
    PseudoIsothermalPotential(),
    HomogeneousSpherePotential(),
    KuzminDiskPotential(),
    DoubleExponentialDiskPotential(),
    FlattenedPowerPotential(),
):
    assert_type(potential(1.0, 0.0), float | onp.ArrayND)

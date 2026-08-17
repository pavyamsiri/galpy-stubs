from typing import assert_type

from galpy.potential.IsochronePotential import IsochronePotential
from galpy.potential.LogarithmicHaloPotential import LogarithmicHaloPotential
from galpy.potential.MiyamotoNagaiPotential import MiyamotoNagaiPotential
from galpy.potential.PlummerPotential import PlummerPotential
from galpy.potential.PowerSphericalPotential import (
    KeplerPotential,
    PowerSphericalPotential,
)
from galpy.potential.TwoPowerSphericalPotential import (
    DehnenSphericalPotential,
    HernquistPotential,
    NFWPotential,
)
from optype import numpy as onp

for potential in (
    MiyamotoNagaiPotential(),
    PlummerPotential(),
    IsochronePotential(),
    LogarithmicHaloPotential(),
    PowerSphericalPotential(),
    KeplerPotential(),
    DehnenSphericalPotential(),
    HernquistPotential(),
    NFWPotential(),
):
    assert_type(potential(1.0, 0.0), float | onp.ArrayND)
    assert_type(potential.Rforce(1.0, 0.0), float | onp.ArrayND)

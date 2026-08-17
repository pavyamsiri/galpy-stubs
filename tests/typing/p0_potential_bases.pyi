from typing import assert_type

from galpy.potential.Force import Force
from galpy.potential.linearPotential import linearPotential
from galpy.potential.planarPotential import planarPotential
from galpy.potential.Potential import Potential
from galpy.potential.SphericalPotential import SphericalPotential
from optype import numpy as onp

force = Force(amp=2.0)
potential = Potential()
spherical = SphericalPotential()
planar = planarPotential()
linear = linearPotential()

assert_type(force * 2, Force)
assert_type(potential(1.0, 0.0), float | onp.ArrayND)
assert_type(potential.Rforce(1.0, 0.0), float | onp.ArrayND)
assert_type(spherical.dens(1.0, 0.0), float | onp.ArrayND)
assert_type(planar(1.0), float | onp.ArrayND)
assert_type(linear(1.0), float | onp.ArrayND)

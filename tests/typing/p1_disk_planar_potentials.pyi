from typing import assert_type

from galpy.potential.EllipticalDiskPotential import EllipticalDiskPotential
from galpy.potential.HenonHeilesPotential import HenonHeilesPotential
from galpy.potential.IsothermalDiskPotential import IsothermalDiskPotential
from galpy.potential.KGPotential import KGPotential
from galpy.potential.RazorThinExponentialDiskPotential import (
    RazorThinExponentialDiskPotential,
)
from galpy.potential.RingPotential import RingPotential
from galpy.potential.SoftenedNeedleBarPotential import SoftenedNeedleBarPotential
from galpy.potential.SteadyLogSpiralPotential import SteadyLogSpiralPotential
from galpy.potential.TransientLogSpiralPotential import TransientLogSpiralPotential
from optype import numpy as onp

for potential in (
    RazorThinExponentialDiskPotential(),
    RingPotential(),
    SoftenedNeedleBarPotential(),
):
    assert_type(potential(1.0, 0.0), float | onp.ArrayND)

elliptical = EllipticalDiskPotential()
henon_heiles = HenonHeilesPotential()
steady_spiral = SteadyLogSpiralPotential()
transient_spiral = TransientLogSpiralPotential()
assert_type(elliptical(1.0), float | onp.ArrayND)
assert_type(henon_heiles(1.0), float | onp.ArrayND)
assert_type(steady_spiral(1.0), float | onp.ArrayND)
assert_type(transient_spiral(1.0), float | onp.ArrayND)

isothermal = IsothermalDiskPotential()
kg = KGPotential()
assert_type(isothermal(1.0), float | onp.ArrayND)
assert_type(kg(1.0), float | onp.ArrayND)

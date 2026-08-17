from typing import assert_type

from galpy.potential.CosmphiDiskPotential import (
    CosmphiDiskPotential,
    LopsidedDiskPotential,
)
from galpy.potential.NullPotential import NullPotential
from optype import numpy as onp

null = NullPotential()
cosmphi = CosmphiDiskPotential()
lopsided = LopsidedDiskPotential()

assert_type(null(1.0, 0.0), float | onp.ArrayND)
assert_type(cosmphi(1.0), float | onp.ArrayND)
assert_type(lopsided(1.0), float | onp.ArrayND)

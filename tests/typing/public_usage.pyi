from typing import assert_type

import galpy
from galpy import potential
from galpy.potential.MiyamotoNagaiPotential import MiyamotoNagaiPotential

assert_type(galpy.__version__, str)
assert_type(potential.MiyamotoNagaiPotential, type[MiyamotoNagaiPotential])

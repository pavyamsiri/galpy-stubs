from collections.abc import Callable
from typing import cast

from galpy.actionAngle import actionAngleTorus
from galpy.potential import LogarithmicHaloPotential

# The runtime extension is optional; this fixture checks the public contract.
cast(Callable[..., object], actionAngleTorus)(pot=LogarithmicHaloPotential())

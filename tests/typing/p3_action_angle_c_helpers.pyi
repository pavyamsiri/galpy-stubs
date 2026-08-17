from collections.abc import Callable
from typing import cast

import numpy as np
from galpy.actionAngle import actionAngleAdiabatic_c
from galpy.potential import LogarithmicHaloPotential

# The compiled helper accepts array-valued phase-space inputs.
cast(Callable[..., object], actionAngleAdiabatic_c)(
    LogarithmicHaloPotential(),
    1.0,
    np.ones(2),
    np.ones(2),
    np.ones(2),
    np.ones(2),
    np.ones(2),
)

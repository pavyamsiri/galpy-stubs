from typing import assert_type

import numpy as np
from galpy.util.symplecticode import leapfrog, leapfrog_leapp, leapfrog_leapq
from optype import numpy as onp

def oscillator(y: onp.ArrayND, *args: object) -> onp.ArrayND: ...

assert_type(
    leapfrog(oscillator, np.array([1.0, 0.0]), np.linspace(0, 1, 4)), onp.Array2D
)
assert_type(leapfrog_leapq(1.0, 0.0, 0.1), float | onp.ArrayND)
assert_type(leapfrog_leapp(0.0, 0.1, oscillator), float | onp.ArrayND)

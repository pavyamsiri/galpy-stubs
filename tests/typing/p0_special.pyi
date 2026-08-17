from typing import assert_type

from galpy.util.special import compute_legendre, sph_harm_normalization
from optype import numpy as onp

assert_type(compute_legendre(0.2, 4, 4), onp.Array2D)
assert_type(compute_legendre(0.2, 4, 4, deriv=True), tuple[onp.Array2D, onp.Array2D])
assert_type(
    compute_legendre(0.2, 4, 4, deriv=2),
    tuple[onp.Array2D, onp.Array2D, onp.Array2D],
)
assert_type(sph_harm_normalization(4, 4), onp.Array2D)

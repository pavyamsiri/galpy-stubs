from typing import assert_type

import numpy as np
from galpy.util.coords import (
    Rz_to_uv,
    XYZ_to_lbd,
    cyl_to_rect,
    lbd_to_XYZ,
    radec_to_lb,
    rect_to_cyl,
    uv_to_Rz,
)
from optype import numpy as onp

assert_type(radec_to_lb(0.2, 0.3), tuple[float | onp.ArrayND, float | onp.ArrayND])
assert_type(
    lbd_to_XYZ(0.2, 0.3, 2.0),
    tuple[float | onp.ArrayND, float | onp.ArrayND, float | onp.ArrayND],
)
assert_type(
    rect_to_cyl(1.0, 2.0, 3.0),
    tuple[float | onp.ArrayND, float | onp.ArrayND, float | onp.ArrayND],
)
assert_type(
    cyl_to_rect(1.0, 0.2, 3.0),
    tuple[float | onp.ArrayND, float | onp.ArrayND, float | onp.ArrayND],
)
assert_type(
    XYZ_to_lbd(1.0, 2.0, 3.0),
    tuple[float | onp.ArrayND, float | onp.ArrayND, float | onp.ArrayND],
)
assert_type(Rz_to_uv(1.0, 0.2), tuple[float | onp.ArrayND, float | onp.ArrayND])
assert_type(uv_to_Rz(0.8, 1.2), tuple[float | onp.ArrayND, float | onp.ArrayND])

array_result = lbd_to_XYZ(
    np.array([0.2, 0.3]), np.array([0.1, 0.2]), np.array([1.0, 2.0])
)
assert_type(array_result, onp.ArrayND)

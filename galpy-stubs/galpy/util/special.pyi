from typing import Literal, overload

from optype import numpy as onp

@overload
def compute_legendre(
    costheta: float, L: int, M: int, deriv: Literal[False, 0] = False
) -> onp.Array2D: ...
@overload
def compute_legendre(
    costheta: float, L: int, M: int, deriv: Literal[True, 1]
) -> tuple[onp.Array2D, onp.Array2D]: ...
@overload
def compute_legendre(
    costheta: float, L: int, M: int, deriv: Literal[2]
) -> tuple[onp.Array2D, onp.Array2D, onp.Array2D]: ...
def compute_legendre(
    costheta: float, L: int, M: int, deriv: bool | int = False
) -> (
    onp.Array2D
    | tuple[onp.Array2D, onp.Array2D]
    | tuple[onp.Array2D, onp.Array2D, onp.Array2D]
): ...
def sph_harm_normalization(L: int, M: int) -> onp.Array2D: ...

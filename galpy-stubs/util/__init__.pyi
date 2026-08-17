from os import PathLike
from typing import Literal, overload

from optype import numpy as onp

from .config import __config__ as __config__

class galpyWarning(Warning): ...
class galpyWarningVerbose(galpyWarning): ...

def save_pickles(
    savefilename: str | PathLike[str], *args: object, **kwargs: object
) -> None: ...
def logsumexp(
    arr: onp.ArrayND, axis: Literal[0, 1] | None = 0
) -> onp.ArrayND | float: ...
def stable_cho_factor(
    x: onp.Array2D, tiny: float = 1e-9
) -> tuple[onp.Array2D, bool]: ...
@overload
def fast_cholesky_invert(
    A: onp.Array2D, logdet: Literal[False] = False, tiny: float = 1e-9
) -> onp.Array2D: ...
@overload
def fast_cholesky_invert(
    A: onp.Array2D, logdet: Literal[True], tiny: float = 1e-9
) -> tuple[onp.Array2D, float]: ...

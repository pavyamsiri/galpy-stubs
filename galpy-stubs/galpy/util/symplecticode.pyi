from collections.abc import Callable

from optype import numpy as onp

from ..potential._typing import Numeric

type ODEFunction = Callable[..., onp.ArrayND]
type ForceFunction = Callable[..., onp.ArrayND]

_MAX_DT_REDUCE: int

def leapfrog(
    func: ODEFunction,
    yo: onp.ArrayND,
    t: onp.Array1D,
    args: tuple[object, ...] = (),
    rtol: float = 1.49012e-12,
    atol: float = 1.49012e-12,
) -> onp.Array2D: ...
def leapfrog_leapq(q: Numeric, p: Numeric, dt: Numeric) -> Numeric: ...
def leapfrog_leapp(p: Numeric, dt: Numeric, force: ForceFunction) -> Numeric: ...

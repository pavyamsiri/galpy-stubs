from collections.abc import Callable

from optype import numpy as onp

type ODEFunction = Callable[..., onp.ArrayND]

unsigned_int_max: int
uround: float

def custom_sign(a: float, b: float) -> float: ...
def hinit(
    func: ODEFunction,
    x: onp.ArrayND,
    t: float,
    pos_neg: int,
    f0: onp.ArrayND,
    iord: int,
    hmax: float,
    rtol: float | onp.ArrayND,
    atol: float | onp.ArrayND,
    args: tuple[object, ...],
) -> tuple[float, float, onp.ArrayND, float]: ...
def dense_output(
    t_current: float, t_old: float, h_current: float, rcont: onp.ArrayND
) -> onp.ArrayND: ...
def dopri853core(
    n: int,
    func: ODEFunction,
    x: onp.ArrayND,
    t: onp.Array1D,
    hmax: float,
    h: float,
    rtol: float | onp.ArrayND,
    atol: float | onp.ArrayND,
    nmax: int,
    safe: float,
    beta: float,
    fac1: float,
    fac2: float,
    pos_neg: int,
    args: tuple[object, ...],
) -> onp.Array2D: ...
def dop853(
    func: ODEFunction | None = None,
    x: onp.ArrayND | None = None,
    t: onp.Array1D | None = None,
    hmax: float = 0.0,
    h: float = 0.0,
    rtol: float | onp.ArrayND = 1e-12,
    atol: float | onp.ArrayND = 1e-12,
    nmax: int = 100_000_000,
    safe: float = 0.9,
    beta: float = 0.0,
    fac1: float = 0.333,
    fac2: float = 6.0,
    args: tuple[object, ...] = (),
) -> onp.Array2D: ...

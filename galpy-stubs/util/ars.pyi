from collections.abc import Callable, Sequence

from optype import numpy as onp

type LogDensity = Callable[..., float]
type Domain = Sequence[float] | onp.Array1D
type Hull = list[object]

def ars(
    domain: Domain,
    isDomainFinite: Sequence[bool] | onp.Array1D,
    abcissae: Sequence[float] | onp.Array1D,
    hx: LogDensity,
    hpx: LogDensity,
    nsamples: int = 1,
    hxparams: tuple[object, ...] = (),
    maxn: int = 100,
) -> list[float]: ...
def setup_hull(
    domain: Domain,
    isDomainFinite: Sequence[bool] | onp.Array1D,
    abcissae: Sequence[float] | onp.Array1D,
    hx: LogDensity,
    hpx: LogDensity,
    hxparams: tuple[object, ...],
) -> Hull: ...
def sampleone(
    hull: Hull,
    hx: LogDensity,
    hpx: LogDensity,
    domain: Domain,
    isDomainFinite: Sequence[bool] | onp.Array1D,
    maxn: int,
    nupdates: int,
    hxparams: tuple[object, ...],
) -> tuple[float, Hull, int]: ...
def sample_hull(
    hull: Hull, domain: Domain, isDomainFinite: Sequence[bool] | onp.Array1D
) -> float: ...
def evaluate_hull(x: float, hull: Hull) -> tuple[float, float]: ...
def update_hull(
    hull: Hull,
    newx: float,
    newhx: float,
    newhpx: float,
    domain: Domain,
    isDomainFinite: Sequence[bool] | onp.Array1D,
) -> Hull: ...

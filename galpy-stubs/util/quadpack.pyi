from collections.abc import Callable

class AccuracyWarning(Warning): ...

def dblquad(
    func: Callable[..., float],
    a: float,
    b: float,
    gfun: Callable[[float], float],
    hfun: Callable[[float], float],
    args: tuple[object, ...] = (),
    epsabs: float = 1.49e-8,
    epsrel: float = 1.49e-8,
) -> tuple[float, float]: ...
def vectorize1(
    func: Callable[..., object],
    args: tuple[object, ...] = (),
    vec_func: bool = False,
) -> Callable[[object], object]: ...
def quadrature(
    func: Callable[..., object],
    a: float,
    b: float,
    args: tuple[object, ...] = (),
    tol: float = 1.49e-8,
    rtol: float = 1.49e-8,
    maxiter: int = 50,
    vec_func: bool = True,
    miniter: int = 1,
) -> tuple[float, float]: ...
def romberg(
    function: Callable[..., object],
    a: float,
    b: float,
    args: tuple[object, ...] = (),
    tol: float = 1.48e-8,
    rtol: float = 1.48e-8,
    divmax: int = 10,
    vec_func: bool = False,
) -> float: ...

from collections.abc import Callable

from optype import numpy as onp

type Numeric = float | onp.ArrayND
type Number = int | float

# TODO: replace with the supported Astropy Quantity protocol/type once the
# optional Astropy dependency is modelled explicitly.
type QuantityLike = object
type CoordinateLike = onp.ArrayND | QuantityLike
type CoordinatePair = (
    tuple[QuantityLike, QuantityLike] | list[QuantityLike] | onp.ArrayND
)
type GridSpec = tuple[float, float, int]
type TimeFunction = Callable[[float], float]
type TimeDependentVector = (
    QuantityLike | list[QuantityLike] | TimeFunction | list[TimeFunction]
)
type DensityFunction = Callable[..., Numeric]
type ProfileInput = dict[str, object] | Callable[[Numeric], Numeric]
type CoefficientArray = onp.ArrayND | QuantityLike

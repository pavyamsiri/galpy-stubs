from collections.abc import Callable

from ..potential._typing import Numeric

type PotentialInput = object
type Profile = Callable[[Numeric], Numeric] | Numeric | None

def sigmar(
    Pot: PotentialInput,
    r: Numeric,
    dens: Profile = None,
    beta: Profile = None,
) -> Numeric: ...
def sigmalos(
    Pot: PotentialInput,
    R: Numeric,
    dens: Profile = None,
    surfdens: Profile = None,
    beta: Profile = None,
    sigma_r: Profile = None,
) -> Numeric: ...

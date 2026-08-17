from collections.abc import Callable
from typing import cast

from galpy.df.evolveddiskdf import evolveddiskdf, evolveddiskdfGrid
from galpy.potential import LogarithmicHaloPotential

cast(Callable[..., object], evolveddiskdfGrid)()
cast(Callable[..., object], evolveddiskdf)(object(), LogarithmicHaloPotential())

from typing import override

from ._typing import GridSpec, Numeric, QuantityLike
from .interpRZPotential import interpRZPotential
from .Potential import Potential

type SnapshotInput = object

class SnapshotRZPotential(Potential):
    def __init__(
        self,
        s: SnapshotInput,
        num_threads: int | None = None,
        nazimuths: int = 4,
        ro: QuantityLike | None = None,
        vo: QuantityLike | None = None,
    ) -> None: ...

class InterpSnapshotRZPotential(interpRZPotential):
    def __init__(
        self,
        s: SnapshotInput,
        ro: QuantityLike | None = None,
        vo: QuantityLike | None = None,
        rgrid: GridSpec = ...,
        zgrid: GridSpec = ...,
        interpepifreq: bool = False,
        interpverticalfreq: bool = False,
        interpPot: bool = True,
        enable_c: bool = True,
        logR: bool = True,
        zsym: bool = True,
        numcores: int | None = None,
        nazimuths: int = 4,
        use_pkdgrav: bool = False,
    ) -> None: ...
    @override
    def normalize(self, norm: Numeric | QuantityLike) -> None: ...
    def denormalize(self) -> None: ...
    @override
    def __getstate__(self) -> dict[str, object]: ...
    def __setstate__(self, state: object) -> None: ...

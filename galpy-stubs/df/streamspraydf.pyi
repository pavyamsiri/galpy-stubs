from collections.abc import Callable
from typing import Literal, override

from optype import numpy as onp

from ..potential._typing import Numeric, QuantityLike
from ..potential.Potential import Potential
from .df import df
from .streamTrack import StreamTrack, StreamTrackPair

type Tail = Literal["leading", "trailing", "both"]
type ProgenitorMass = Numeric | QuantityLike | Callable[[Numeric], Numeric]

class basestreamspraydf(df):
    def __init__(
        self,
        progenitor_mass: ProgenitorMass,
        progenitor: object = None,
        pot: Potential | list[Potential] | None = None,
        rtpot: Potential | list[Potential] | None = None,
        tdisrupt: Numeric | QuantityLike | None = None,
        stripping_pdf: Callable[..., Numeric] | None = None,
        leading: bool | None = None,
        tail: Tail | None = None,
        center: object = None,
        centerpot: Potential | list[Potential] | None = None,
        progpot: Potential | list[Potential] | None = None,
        ro: Numeric | None = None,
        vo: Numeric | None = None,
    ) -> None: ...
    def sample(self, *args: object, **kwargs: object) -> object: ...
    def streamTrack(
        self, *args: object, **kwargs: object
    ) -> StreamTrack | StreamTrackPair: ...
    def spray_df(self, *args: object, **kwargs: object) -> object: ...

class chen24spraydf(basestreamspraydf):
    def __init__(
        self, *args: object, mean: object = None, cov: object = None, **kwargs: object
    ) -> None: ...
    @override
    def spray_df(self, *args: object, **kwargs: object) -> object: ...

class fardal15spraydf(basestreamspraydf):
    def __init__(
        self,
        *args: object,
        meankvec: onp.Array1D | None = None,
        sigkvec: onp.Array1D | None = None,
        **kwargs: object,
    ) -> None: ...
    @override
    def spray_df(self, *args: object, **kwargs: object) -> object: ...

class streamspraydf(fardal15spraydf):
    def __init__(self, args: object, **kwargs: object) -> None: ...

def pericenter_stripping_pdf(*args: object, **kwargs: object) -> object: ...

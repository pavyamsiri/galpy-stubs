from optype import numpy as onp

from ..potential._typing import Numeric, QuantityLike
from .df import df

class streamdf(df):
    """Distribution function for a tidal stream."""

    def __init__(
        self,
        sigv: Numeric,
        progenitor: object = None,
        pot: object = None,
        aA: object = None,
        useTM: object = False,
        tdisrupt: Numeric | QuantityLike | None = None,
        sigMeanOffset: Numeric = 6.0,
        leading: bool = True,
        sigangle: Numeric | QuantityLike | None = None,
        deltaAngleTrack: Numeric | QuantityLike | None = None,
        nTrackChunks: int | None = None,
        nTrackIterations: int | None = None,
        progIsTrack: bool = False,
        ro: Numeric | None = None,
        vo: Numeric | None = None,
        Vnorm: Numeric | QuantityLike | None = None,
        Rnorm: Numeric | QuantityLike | None = None,
        R0: Numeric | None = None,
        Zsun: Numeric | None = None,
        vsun: onp.Array1D | QuantityLike | None = None,
        multi: int | None = None,
        interpTrack: bool | None = None,
        useInterp: bool | None = None,
        nosetup: bool = False,
        nospreadsetup: bool = False,
        approxConstTrackFreq: bool = False,
        useTMHessian: bool = False,
        custom_sky_transform: onp.Array2D | None = None,
        custom_transform: onp.Array2D | None = None,
    ) -> None: ...
    def __call__(self, *args: object, **kwargs: object) -> object: ...
    def misalignment(self, *args: object, **kwargs: object) -> object: ...
    def sample(self, *args: object, **kwargs: object) -> object: ...
    def sample_t(self, *args: object, **kwargs: object) -> object: ...
    def streamTrack(self, *args: object, **kwargs: object) -> object: ...
    def plotTrack(self, *args: object, **kwargs: object) -> object: ...
    def plotProgenitor(self, *args: object, **kwargs: object) -> object: ...
    def plotCompareTrackAAModel(self, *args: object, **kwargs: object) -> object: ...
    def __getattr__(self, name: str) -> object: ...

def calcaAJac(*args: object, **kwargs: object) -> object: ...
def lbCoordFunc(*args: object, **kwargs: object) -> object: ...

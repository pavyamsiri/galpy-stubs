from .df import df
from .surfaceSigmaProfile import expSurfaceSigmaProfile, surfaceSigmaProfile
from ..potential._typing import Numeric, QuantityLike

type SurfaceSigmaInput = type[surfaceSigmaProfile] | surfaceSigmaProfile
type DiskProfileParams = tuple[QuantityLike, QuantityLike, QuantityLike]

class diskdf(df):
    def __init__(
        self,
        dftype: str = "dehnen",
        surfaceSigma: SurfaceSigmaInput = expSurfaceSigmaProfile,
        profileParams: DiskProfileParams = (1 / 3, 1.0, 0.2),
        correct: bool = False,
        beta: float = 0.0,
        ro: QuantityLike | None = None,
        vo: QuantityLike | None = None,
        **kwargs: object,
    ) -> None: ...
    def __call__(self, *args: object, **kwargs: object) -> object: ...
    def targetSigma2(self, R: Numeric, log: bool = False) -> Numeric: ...
    def targetSurfacemass(self, R: Numeric, log: bool = False) -> Numeric: ...
    def surfacemass(
        self,
        R: Numeric,
        romberg: bool = False,
        nsigma: float = 5.0,
        relative: bool = False,
    ) -> Numeric: ...
    def sigma2surfacemass(
        self,
        R: Numeric,
        romberg: bool = False,
        nsigma: float = 5.0,
        relative: bool = False,
    ) -> Numeric: ...
    def asymmetricdrift(self, R: Numeric) -> Numeric: ...

class dehnendf(diskdf):
    def __init__(
        self,
        surfaceSigma: SurfaceSigmaInput = expSurfaceSigmaProfile,
        profileParams: DiskProfileParams = (1 / 3, 1.0, 0.2),
        correct: bool = False,
        beta: float = 0.0,
        **kwargs: object,
    ) -> None: ...

class shudf(diskdf):
    def __init__(
        self,
        surfaceSigma: SurfaceSigmaInput = expSurfaceSigmaProfile,
        profileParams: DiskProfileParams = (1 / 3, 1.0, 0.2),
        correct: bool = False,
        beta: float = 0.0,
        **kwargs: object,
    ) -> None: ...

class schwarzschilddf(shudf):
    def __init__(
        self,
        surfaceSigma: SurfaceSigmaInput = expSurfaceSigmaProfile,
        profileParams: DiskProfileParams = (1 / 3, 1.0, 0.2),
        correct: bool = False,
        beta: float = 0.0,
        **kwargs: object,
    ) -> None: ...

class DFcorrection:
    def __init__(self, **kwargs: object) -> None: ...

class DFcorrectionError(Exception):
    def __init__(self, value: object) -> None: ...

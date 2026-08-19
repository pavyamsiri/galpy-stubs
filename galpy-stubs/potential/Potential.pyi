from typing import Literal, override

from ._typing import Numeric, QuantityLike
from .Force import Force

class Potential(Force):
    dim: Literal[3]
    isRZ: bool
    isNonAxi: bool
    isDissipative: bool
    hasC: bool
    hasC_dxdv: bool
    hasC_dxdv3d: bool
    hasC_dens: bool
    hasC_planar: bool

    def __init__(
        self,
        amp: QuantityLike = 1.0,
        ro: QuantityLike | None = None,
        vo: QuantityLike | None = None,
        amp_units: str | None = None,
    ) -> None: ...
    def __call__(
        self,
        R: Numeric,
        z: Numeric,
        phi: Numeric = 0.0,
        t: Numeric = 0.0,
        dR: int = 0,
        dphi: int = 0,
    ) -> Numeric: ...
    def Rforce(
        self, R: Numeric, z: Numeric, phi: Numeric = 0.0, t: Numeric = 0.0
    ) -> Numeric: ...
    def zforce(
        self, R: Numeric, z: Numeric, phi: Numeric = 0.0, t: Numeric = 0.0
    ) -> Numeric: ...
    def phitorque(
        self, R: Numeric, z: Numeric, phi: Numeric = 0.0, t: Numeric = 0.0
    ) -> Numeric: ...
    def R2deriv(
        self, R: Numeric, z: Numeric, phi: Numeric = 0.0, t: Numeric = 0.0
    ) -> Numeric: ...
    def z2deriv(
        self, R: Numeric, z: Numeric, phi: Numeric = 0.0, t: Numeric = 0.0
    ) -> Numeric: ...
    def phi2deriv(
        self, R: Numeric, z: Numeric, phi: Numeric = 0.0, t: Numeric = 0.0
    ) -> Numeric: ...
    def Rzderiv(
        self, R: Numeric, z: Numeric, phi: Numeric = 0.0, t: Numeric = 0.0
    ) -> Numeric: ...
    def Rphideriv(
        self, R: Numeric, z: Numeric, phi: Numeric = 0.0, t: Numeric = 0.0
    ) -> Numeric: ...
    def phizderiv(
        self, R: Numeric, z: Numeric, phi: Numeric = 0.0, t: Numeric = 0.0
    ) -> Numeric: ...
    def r2deriv(
        self, R: Numeric, z: Numeric, phi: Numeric = 0.0, t: Numeric = 0.0
    ) -> Numeric: ...
    def dens(
        self,
        R: Numeric,
        z: Numeric,
        phi: Numeric = 0.0,
        t: Numeric = 0.0,
        forcepoisson: bool = False,
    ) -> Numeric: ...
    def surfdens(
        self,
        R: Numeric,
        z: Numeric,
        phi: Numeric = 0.0,
        t: Numeric = 0.0,
        forcepoisson: bool = False,
    ) -> Numeric: ...
    def mass(
        self,
        R: Numeric,
        z: Numeric | None = None,
        t: Numeric = 0.0,
        forceint: bool = False,
    ) -> Numeric: ...
    def rhalf(self, t: Numeric = 0.0, INF: float = float("inf")) -> Numeric: ...
    def tdyn(self, R: Numeric, t: Numeric = 0.0) -> Numeric: ...
    def mvir(
        self,
        H: float = 70.0,
        Om: float = 0.3,
        t: Numeric = 0.0,
        overdens: float = 200.0,
        wrtcrit: bool = False,
        forceint: bool = False,
        ro: object | None = None,
        vo: object | None = None,
        use_physical: bool = False,
    ) -> Numeric: ...
    def normalize(self, norm: object) -> None: ...
    @override
    def toPlanar(self) -> object: ...
    def toVertical(
        self, R: Numeric, phi: Numeric | None = None, t0: Numeric = 0.0
    ) -> object: ...
    def vcirc(
        self, R: Numeric, phi: Numeric | None = None, t: Numeric = 0.0
    ) -> Numeric: ...
    def dvcircdR(
        self, R: Numeric, phi: Numeric | None = None, t: Numeric = 0.0
    ) -> Numeric: ...
    def omegac(self, R: Numeric, t: Numeric = 0.0) -> Numeric: ...
    def epifreq(self, R: Numeric, t: Numeric = 0.0) -> Numeric: ...
    def verticalfreq(self, R: Numeric, t: Numeric = 0.0) -> Numeric: ...
    def lindbladR(
        self, OmegaP: Numeric, m: int = 2, t: Numeric = 0.0, **kwargs: object
    ) -> Numeric: ...
    def vesc(self, R: Numeric, t: Numeric = 0.0) -> Numeric: ...
    def rl(self, lz: Numeric, t: Numeric = 0.0) -> Numeric: ...
    def rE(self, E: Numeric, t: Numeric = 0.0) -> Numeric: ...
    def LcE(self, E: Numeric, t: Numeric = 0.0) -> Numeric: ...
    def flattening(self, R: Numeric, z: Numeric, t: Numeric = 0.0) -> Numeric: ...
    def vterm(self, l: Numeric, t: Numeric = 0.0, deg: bool = True) -> Numeric: ...
    def conc(
        self,
        H: float = 70.0,
        Om: float = 0.3,
        t: Numeric = 0.0,
        overdens: float = 200.0,
        wrtcrit: bool = False,
        ro: object | None = None,
        vo: object | None = None,
    ) -> Numeric: ...
    def nemo_accname(self) -> str: ...
    def nemo_accpars(self, vo: QuantityLike, ro: QuantityLike) -> str: ...
    def rtide(
        self,
        R: Numeric,
        z: Numeric,
        phi: Numeric = 0.0,
        t: Numeric = 0.0,
        M: Numeric | None = None,
    ) -> Numeric: ...
    def ttensor(
        self,
        R: Numeric,
        z: Numeric,
        phi: Numeric = 0.0,
        t: Numeric = 0.0,
        eigenval: bool = False,
    ) -> object: ...
    def zvc(
        self, R: Numeric, E: Numeric, Lz: Numeric, phi: Numeric = 0.0, t: Numeric = 0.0
    ) -> object: ...
    def zvc_range(
        self, E: Numeric, Lz: Numeric, phi: Numeric = 0.0, t: Numeric = 0.0
    ) -> object: ...

class PotentialError(Exception):
    def __init__(self, value: object) -> None: ...

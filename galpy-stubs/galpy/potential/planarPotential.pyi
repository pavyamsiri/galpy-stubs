from typing import override

from ._typing import Numeric
from .planarForce import planarForce

class planarPotential(planarForce):
    dim: int
    isNonAxi: bool
    def __init__(
        self, amp: object = 1.0, ro: object | None = None, vo: object | None = None
    ) -> None: ...
    def __call__(
        self,
        R: Numeric,
        phi: Numeric = 0.0,
        t: Numeric = 0.0,
        dR: int = 0,
        dphi: int = 0,
    ) -> Numeric: ...
    @override
    def Rforce(self, R: Numeric, phi: Numeric = 0.0, t: Numeric = 0.0) -> Numeric: ...
    @override
    def phitorque(
        self, R: Numeric, phi: Numeric = 0.0, t: Numeric = 0.0
    ) -> Numeric: ...
    def R2deriv(self, R: Numeric, phi: Numeric = 0.0, t: Numeric = 0.0) -> Numeric: ...
    def phi2deriv(
        self, R: Numeric, phi: Numeric = 0.0, t: Numeric = 0.0
    ) -> Numeric: ...
    def Rphideriv(
        self, R: Numeric, phi: Numeric = 0.0, t: Numeric = 0.0
    ) -> Numeric: ...
    def vcirc(
        self, R: Numeric, phi: Numeric | None = None, t: Numeric = 0.0
    ) -> Numeric: ...
    def omegac(self, R: Numeric, t: Numeric = 0.0) -> Numeric: ...
    def epifreq(self, R: Numeric, t: Numeric = 0.0) -> Numeric: ...

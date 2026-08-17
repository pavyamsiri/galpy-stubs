from collections.abc import Callable
from typing import Self, override

from .Potential import Potential
from ._typing import QuantityLike
from .planarPotential import planarPotential

class parentWrapperPotential:
    def __new__(cls, *args: object, **kwargs: object) -> Self: ...

class WrapperPotential(Potential):
    def __init__(
        self,
        amp: QuantityLike = 1.0,
        pot: object | None = None,
        ro: QuantityLike | None = None,
        vo: QuantityLike | None = None,
        _init: bool | None = None,
        **kwargs: object,
    ) -> None: ...
    @override
    def __repr__(self) -> str: ...
    def __getattr__(self, attribute: str) -> Callable[..., object]: ...

class planarWrapperPotential(planarPotential):
    def __init__(
        self,
        amp: QuantityLike = 1.0,
        pot: object | None = None,
        ro: QuantityLike | None = None,
        vo: QuantityLike | None = None,
        _init: bool | None = None,
        **kwargs: object,
    ) -> None: ...
    @override
    def __repr__(self) -> str: ...
    def __getattr__(self, attribute: str) -> Callable[..., object]: ...

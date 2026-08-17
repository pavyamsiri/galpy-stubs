from optype import numpy as onp

from ..potential.Potential import Potential
from ..potential._typing import Numeric

type StaeckelInput = Potential | list[Potential]

def actionAngleStaeckel_c(
    pot: StaeckelInput,
    delta: Numeric,
    R: onp.ArrayND,
    vR: onp.ArrayND,
    vT: onp.ArrayND,
    z: onp.ArrayND,
    vz: onp.ArrayND,
    u0: Numeric | None = None,
    order: int = 10,
) -> tuple[onp.ArrayND, onp.ArrayND, int]: ...
def actionAngleStaeckel_calcu0(
    E: onp.ArrayND, Lz: onp.ArrayND, pot: StaeckelInput, delta: Numeric
) -> tuple[onp.ArrayND, int]: ...
def actionAngleFreqStaeckel_c(
    pot: StaeckelInput,
    delta: Numeric,
    R: onp.ArrayND,
    vR: onp.ArrayND,
    vT: onp.ArrayND,
    z: onp.ArrayND,
    vz: onp.ArrayND,
    u0: Numeric | None = None,
    order: int = 10,
) -> tuple[onp.ArrayND, onp.ArrayND, onp.ArrayND, onp.ArrayND, onp.ArrayND, int]: ...
def actionAngleFreqAngleStaeckel_c(
    pot: StaeckelInput,
    delta: Numeric,
    R: onp.ArrayND,
    vR: onp.ArrayND,
    vT: onp.ArrayND,
    z: onp.ArrayND,
    vz: onp.ArrayND,
    phi: onp.ArrayND,
    u0: Numeric | None = None,
    order: int = 10,
) -> tuple[
    onp.ArrayND,
    onp.ArrayND,
    onp.ArrayND,
    onp.ArrayND,
    onp.ArrayND,
    onp.ArrayND,
    onp.ArrayND,
    onp.ArrayND,
    int,
]: ...
def actionAngleUminUmaxVminStaeckel_c(
    pot: StaeckelInput,
    delta: Numeric,
    R: onp.ArrayND,
    vR: onp.ArrayND,
    vT: onp.ArrayND,
    z: onp.ArrayND,
    vz: onp.ArrayND,
    u0: Numeric | None = None,
) -> tuple[onp.ArrayND, onp.ArrayND, onp.ArrayND, int]: ...

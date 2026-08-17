from collections.abc import Callable
from typing import cast

from galpy.actionAngle import actionAngleIsochroneApprox
from galpy.potential import LogarithmicHaloPotential

cast(Callable[..., object], actionAngleIsochroneApprox)(
    pot=LogarithmicHaloPotential(), b=1.0
)

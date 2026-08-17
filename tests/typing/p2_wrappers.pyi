import numpy as np
from galpy.potential.ChandrasekharDynamicalFrictionForce import (
    ChandrasekharDynamicalFrictionForce,
)
from galpy.potential.CorotatingRotationWrapperPotential import (
    CorotatingRotationWrapperPotential,
)
from galpy.potential.CylindricallySeparablePotentialWrapper import (
    CylindricallySeparablePotentialWrapper,
)
from galpy.potential.DehnenBarPotential import DehnenBarPotential
from galpy.potential.DehnenSmoothWrapperPotential import DehnenSmoothWrapperPotential
from galpy.potential.FDMDynamicalFrictionForce import FDMDynamicalFrictionForce
from galpy.potential.GaussianAmplitudeWrapperPotential import (
    GaussianAmplitudeWrapperPotential,
)
from galpy.potential.interpRZPotential import interpRZPotential
from galpy.potential.interpSphericalPotential import interpSphericalPotential
from galpy.potential.KingPotential import KingPotential
from galpy.potential.KuzminLikeWrapperPotential import KuzminLikeWrapperPotential
from galpy.potential.NonInertialFrameForce import NonInertialFrameForce
from galpy.potential.OblateStaeckelWrapperPotential import (
    OblateStaeckelWrapperPotential,
)
from galpy.potential.PlummerPotential import PlummerPotential
from galpy.potential.RotateAndTiltWrapperPotential import RotateAndTiltWrapperPotential
from galpy.potential.SolidBodyRotationWrapperPotential import (
    SolidBodyRotationWrapperPotential,
)
from galpy.potential.TimeDependentAmplitudeWrapperPotential import (
    TimeDependentAmplitudeWrapperPotential,
)

base = PlummerPotential()

def amplitude(t: float) -> float:
    return 1.0 + t

DehnenSmoothWrapperPotential(pot=base)
GaussianAmplitudeWrapperPotential(pot=[base])
TimeDependentAmplitudeWrapperPotential(pot=base, A=amplitude)
SolidBodyRotationWrapperPotential(pot=base)
CorotatingRotationWrapperPotential(pot=base)
CylindricallySeparablePotentialWrapper(pot=base)
KuzminLikeWrapperPotential(pot=base)
DehnenBarPotential()
RotateAndTiltWrapperPotential(pot=base, inclination=0.2, galaxy_pa=0.1, sky_pa=0.3)
OblateStaeckelWrapperPotential(pot=base, u0=0.7)
OblateStaeckelWrapperPotential(pot=base, u0=(1.0, 0.2))
interpSphericalPotential(rforce=lambda r: -r, rgrid=np.array([0.1, 0.3, 1.0, 2.0]))
interpSphericalPotential(rforce=base, rgrid=np.array([0.1, 0.3, 1.0, 2.0]))
KingPotential(W0=3.0, M=1.0, rt=2.0, npt=101)
interpRZPotential(
    RZPot=base,
    rgrid=(-2.0, 1.0, 5),
    zgrid=(0.0, 1.0, 5),
    interpPot=True,
)
ChandrasekharDynamicalFrictionForce(dens=base, sigmar=lambda r: 0.1, const_lnLambda=1.0)
FDMDynamicalFrictionForce(dens=base, sigmar=lambda r: 0.1)
NonInertialFrameForce(Omega=0.1)

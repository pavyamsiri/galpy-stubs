import numpy as np
from galpy.actionAngle.actionAngleAdiabatic import actionAngleAdiabatic
from galpy.actionAngle.actionAngleAdiabaticGrid import actionAngleAdiabaticGrid
from galpy.actionAngle.actionAngleHarmonic import actionAngleHarmonic
from galpy.actionAngle.actionAngleHarmonicInverse import actionAngleHarmonicInverse
from galpy.actionAngle.actionAngleIsochrone import actionAngleIsochrone
from galpy.actionAngle.actionAngleIsochroneInverse import actionAngleIsochroneInverse
from galpy.actionAngle.actionAngleSpherical import actionAngleSpherical
from galpy.actionAngle.actionAngleStaeckel import actionAngleStaeckel
from galpy.actionAngle.actionAngleStaeckelGrid import actionAngleStaeckelGrid
from galpy.actionAngle.actionAngleVertical import actionAngleVertical
from galpy.actionAngle.actionAngleVerticalInverse import actionAngleVerticalInverse
from galpy.potential.IsochronePotential import IsochronePotential
from galpy.potential.KGPotential import KGPotential
from galpy.potential.PlummerPotential import PlummerPotential

actionAngleHarmonic(omega=1.0)
actionAngleIsochrone(b=1.0)
actionAngleIsochrone(ip=IsochronePotential())
actionAngleSpherical(pot=PlummerPotential())
actionAngleVertical(pot=KGPotential())
actionAngleHarmonicInverse(omega=1.0)
actionAngleIsochroneInverse(b=1.0)
actionAngleVerticalInverse(pot=KGPotential(), Es=np.array([0.1, 0.3]))
actionAngleAdiabatic(pot=PlummerPotential())
actionAngleStaeckel(pot=PlummerPotential(), delta=0.5)
actionAngleAdiabaticGrid(pot=PlummerPotential(), nR=4, nEz=4, nEr=4, nLz=4)
actionAngleStaeckelGrid(pot=PlummerPotential(), delta=0.5, nE=4, npsi=4, nLz=4)

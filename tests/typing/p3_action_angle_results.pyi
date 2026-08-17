from galpy.actionAngle.actionAngle import (
    ActionFrequencyAngleResult,
    ActionFrequencyResult,
    ActionResult,
)
from galpy.actionAngle.actionAngleHarmonic import actionAngleHarmonic
from galpy.actionAngle.actionAngleIsochrone import actionAngleIsochrone
from galpy.actionAngle.actionAngleSpherical import actionAngleSpherical
from galpy.actionAngle.actionAngleVertical import actionAngleVertical
from galpy.potential.IsochronePotential import IsochronePotential
from galpy.potential.KGPotential import KGPotential
from galpy.potential.PlummerPotential import PlummerPotential

harmonic = actionAngleHarmonic(omega=1.0)
action: ActionResult = harmonic(1.0, 0.5)
action_frequency: ActionFrequencyResult = harmonic.actionsFreqs(1.0, 0.5)
action_frequency_angle: ActionFrequencyAngleResult = harmonic.actionsFreqsAngles(
    1.0, 0.5
)
spherical = actionAngleSpherical(pot=PlummerPotential())
isochrone = actionAngleIsochrone(ip=IsochronePotential())
args = (1.0, 0.1, 1.0, 0.2, 0.1, 0.3)
spherical_action: tuple[ActionResult, ActionResult, ActionResult] = spherical(*args)
isochrone_frequency: tuple[ActionResult, ...] = isochrone.actionsFreqs(*args)
vertical = actionAngleVertical(pot=KGPotential())
vertical_action: ActionResult = vertical(0.2, 0.1)

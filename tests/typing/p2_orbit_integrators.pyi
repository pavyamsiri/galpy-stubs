import numpy as np
from galpy.orbit.integrateFullOrbit import integrateFullOrbit
from galpy.orbit.integrateLinearOrbit import integrateLinearOrbit
from galpy.orbit.integratePlanarOrbit import integratePlanarOrbit
from galpy.potential.HenonHeilesPotential import HenonHeilesPotential
from galpy.potential.KGPotential import KGPotential
from galpy.potential.PlummerPotential import PlummerPotential

times = np.linspace(0.0, 0.1, 3)
planar_result = integratePlanarOrbit(
    HenonHeilesPotential(), np.array([[1.0, 0.0, 1.0, 0.0]]), times, "leapfrog"
)
full_result = integrateFullOrbit(
    PlummerPotential(), np.array([[1.0, 0.0, 1.0, 0.0, 0.0, 0.0]]), times, "leapfrog"
)
linear_result = integrateLinearOrbit(
    KGPotential(), np.array([[0.0, 1.0]]), times, "leapfrog"
)

assert isinstance(planar_result, tuple)
assert isinstance(full_result, tuple)
assert isinstance(linear_result, tuple)

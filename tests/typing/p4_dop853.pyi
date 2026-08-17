import numpy as np
from galpy.util.leung_dop853 import dop853

def oscillator(y: object, *args: object) -> np.ndarray: ...

dop853(oscillator, np.array([1.0, 0.0]), np.linspace(0.0, 1.0, 4))

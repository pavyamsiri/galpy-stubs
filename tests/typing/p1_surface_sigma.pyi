from typing import assert_type

from galpy.df.surfaceSigmaProfile import expSurfaceSigmaProfile
from optype import numpy as onp

profile = expSurfaceSigmaProfile((0.3333333333333333, 1.0, 0.2))
assert_type(profile.surfacemass(1.0), float | onp.ArrayND)
assert_type(profile.sigma2(1.0), float | onp.ArrayND)

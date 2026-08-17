from typing import assert_type

from galpy.df.diskdf import dehnendf, schwarzschilddf, shudf
from galpy.df.surfaceSigmaProfile import expSurfaceSigmaProfile
from optype import numpy as onp

for df in (
    dehnendf(),
    shudf(surfaceSigma=expSurfaceSigmaProfile, profileParams=(0.3, 1.0, 0.2)),
    schwarzschilddf(surfaceSigma=expSurfaceSigmaProfile),
):
    assert_type(df.targetSigma2(1.0), float | onp.ArrayND)
    assert_type(df.surfacemass(1.0), float | onp.ArrayND)

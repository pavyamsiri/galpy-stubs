from galpy.potential.AnyAxisymmetricRazorThinDiskPotential import (
    AnyAxisymmetricRazorThinDiskPotential,
)
from galpy.potential.AnySphericalPotential import AnySphericalPotential
from galpy.potential.KuzminKutuzovStaeckelPotential import (
    KuzminKutuzovStaeckelPotential,
)

AnySphericalPotential(dens=lambda r: 1.0 / (1.0 + r) ** 4)
AnyAxisymmetricRazorThinDiskPotential(surfdens=lambda R: 1.0 / (1.0 + R) ** 3)
KuzminKutuzovStaeckelPotential(ac=3.0, Delta=0.5)

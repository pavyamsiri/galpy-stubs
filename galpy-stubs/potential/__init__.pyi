from collections.abc import Callable

from .CompositePotential import CompositePotential
from .DoubleExponentialDiskPotential import DoubleExponentialDiskPotential
from .Force import Force
from .IsochronePotential import IsochronePotential
from .linearCompositePotential import linearCompositePotential
from .linearPotential import linearPotential
from .LogarithmicHaloPotential import (
    LogarithmicHaloPotential as _LogarithmicHaloPotential,
)
from .MiyamotoNagaiPotential import MiyamotoNagaiPotential as _MiyamotoNagaiPotential
from .MultipoleExpansionPotential import MultipoleExpansionPotential
from .mwpotentials import MWPotential2014
from .planarCompositePotential import planarCompositePotential
from .planarForce import planarForce
from .planarPotential import planarPotential
from .PlummerPotential import PlummerPotential
from .Potential import Potential, PotentialError
from .PowerSphericalPotential import KeplerPotential, PowerSphericalPotential
from .SCFPotential import SCFPotential
from .TwoPowerSphericalPotential import (
    DehnenCoreSphericalPotential,
    DehnenSphericalPotential,
    HernquistPotential,
    JaffePotential,
    NFWPotential,
    TwoPowerSphericalPotential,
)
from .TwoPowerTriaxialPotential import (
    TriaxialHernquistPotential,
    TriaxialJaffePotential,
    TriaxialNFWPotential,
    TwoPowerTriaxialPotential,
)

CompositePotential = CompositePotential
DoubleExponentialDiskPotential = DoubleExponentialDiskPotential
Force = Force
IsochronePotential = IsochronePotential
LogarithmicHaloPotential = _LogarithmicHaloPotential
MiyamotoNagaiPotential = _MiyamotoNagaiPotential
MultipoleExpansionPotential = MultipoleExpansionPotential
PlummerPotential = PlummerPotential
Potential = Potential
PotentialError = PotentialError
KeplerPotential = KeplerPotential
PowerSphericalPotential = PowerSphericalPotential
SCFPotential = SCFPotential
DehnenCoreSphericalPotential = DehnenCoreSphericalPotential
DehnenSphericalPotential = DehnenSphericalPotential
HernquistPotential = HernquistPotential
JaffePotential = JaffePotential
NFWPotential = NFWPotential
TwoPowerSphericalPotential = TwoPowerSphericalPotential
TriaxialHernquistPotential = TriaxialHernquistPotential
TriaxialJaffePotential = TriaxialJaffePotential
TriaxialNFWPotential = TriaxialNFWPotential
TwoPowerTriaxialPotential = TwoPowerTriaxialPotential
linearCompositePotential = linearCompositePotential
linearPotential = linearPotential
planarCompositePotential = planarCompositePotential
planarForce = planarForce
planarPotential = planarPotential
MWPotential2014 = MWPotential2014

planarAxiPotential: object
MWPotential: object

def _dynamic_function(*args: object, **kwargs: object) -> object: ...

evaluatePotentials: Callable[..., object] = _dynamic_function
evaluateDensities: Callable[..., object] = _dynamic_function
evaluateSurfaceDensities: Callable[..., object] = _dynamic_function
mass: Callable[..., object] = _dynamic_function
evaluateRforces: Callable[..., object] = _dynamic_function
evaluatephitorques: Callable[..., object] = _dynamic_function
evaluatezforces: Callable[..., object] = _dynamic_function
evaluaterforces: Callable[..., object] = _dynamic_function
evaluateR2derivs: Callable[..., object] = _dynamic_function
evaluatez2derivs: Callable[..., object] = _dynamic_function
evaluateRzderivs: Callable[..., object] = _dynamic_function
evaluatephi2derivs: Callable[..., object] = _dynamic_function
evaluateRphiderivs: Callable[..., object] = _dynamic_function
evaluatephizderivs: Callable[..., object] = _dynamic_function
evaluater2derivs: Callable[..., object] = _dynamic_function
RZToplanarPotential: Callable[..., object] = _dynamic_function
toPlanarPotential: Callable[..., object] = _dynamic_function
RZToverticalPotential: Callable[..., object] = _dynamic_function
toVerticalPotential: Callable[..., object] = _dynamic_function
plotPotentials: Callable[..., object] = _dynamic_function
plotDensities: Callable[..., object] = _dynamic_function
plotSurfaceDensities: Callable[..., object] = _dynamic_function
plotplanarPotentials: Callable[..., object] = _dynamic_function
plotlinearPotentials: Callable[..., object] = _dynamic_function
calcRotcurve: Callable[..., object] = _dynamic_function
vcirc: Callable[..., object] = _dynamic_function
dvcircdR: Callable[..., object] = _dynamic_function
epifreq: Callable[..., object] = _dynamic_function
verticalfreq: Callable[..., object] = _dynamic_function
flattening: Callable[..., object] = _dynamic_function
rl: Callable[..., object] = _dynamic_function
omegac: Callable[..., object] = _dynamic_function
vterm: Callable[..., object] = _dynamic_function
lindbladR: Callable[..., object] = _dynamic_function
plotRotcurve: Callable[..., object] = _dynamic_function
calcEscapecurve: Callable[..., object] = _dynamic_function
vesc: Callable[..., object] = _dynamic_function
plotEscapecurve: Callable[..., object] = _dynamic_function
evaluateplanarPotentials: Callable[..., object] = _dynamic_function
evaluateplanarRforces: Callable[..., object] = _dynamic_function
evaluateplanarR2derivs: Callable[..., object] = _dynamic_function
evaluateplanarphitorques: Callable[..., object] = _dynamic_function
evaluatelinearPotentials: Callable[..., object] = _dynamic_function
evaluatelinearForces: Callable[..., object] = _dynamic_function
turn_physical_off: Callable[..., object] = _dynamic_function
turn_physical_on: Callable[..., object] = _dynamic_function
rtide: Callable[..., object] = _dynamic_function
ttensor: Callable[..., object] = _dynamic_function
flatten: Callable[..., object] = _dynamic_function
to_amuse: Callable[..., object] = _dynamic_function
zvc: Callable[..., object] = _dynamic_function
zvc_range: Callable[..., object] = _dynamic_function
rhalf: Callable[..., object] = _dynamic_function
tdyn: Callable[..., object] = _dynamic_function
rE: Callable[..., object] = _dynamic_function
LcE: Callable[..., object] = _dynamic_function

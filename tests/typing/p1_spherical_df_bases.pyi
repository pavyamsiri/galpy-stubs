from galpy.df.constantbetadf import constantbetadf
from galpy.df.osipkovmerrittdf import osipkovmerrittdf
from galpy.potential import HernquistPotential

constantbetadf(pot=HernquistPotential(), beta=0.2)
osipkovmerrittdf(pot=HernquistPotential(), ra=1.0)

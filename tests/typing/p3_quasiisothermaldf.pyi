from galpy.actionAngle.actionAngleStaeckel import actionAngleStaeckel
from galpy.df.quasiisothermaldf import quasiisothermaldf
from galpy.potential.LogarithmicHaloPotential import LogarithmicHaloPotential

quasiisothermaldf(
    0.3,
    0.2,
    0.1,
    0.3,
    0.3,
    pot=LogarithmicHaloPotential(),
    aA=actionAngleStaeckel(pot=LogarithmicHaloPotential(), delta=0.5),
)

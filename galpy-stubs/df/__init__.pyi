from collections.abc import Callable

from .constantbetadf import constantbetadf as _constantbetadf
from .constantbetaHernquistdf import constantbetaHernquistdf as _constantbetaHernquistdf
from .constantbetaPowerLawdf import constantbetaPowerLawdf as _constantbetaPowerLawdf
from .df import df as _df
from .eddingtondf import eddingtondf as _eddingtondf
from .evolveddiskdf import evolveddiskdf as _evolveddiskdf
from .isotropicHernquistdf import isotropicHernquistdf as _isotropicHernquistdf
from .isotropicNFWdf import isotropicNFWdf as _isotropicNFWdf
from .isotropicPlummerdf import isotropicPlummerdf as _isotropicPlummerdf
from .isotropicPowerLawdf import isotropicPowerLawdf as _isotropicPowerLawdf
from .kingdf import kingdf as _kingdf
from .osipkovmerrittdf import osipkovmerrittdf as _osipkovmerrittdf
from .osipkovmerrittHernquistdf import (
    osipkovmerrittHernquistdf as _osipkovmerrittHernquistdf,
)
from .osipkovmerrittNFWdf import osipkovmerrittNFWdf as _osipkovmerrittNFWdf
from .osipkovmerrittPowerLawdf import (
    osipkovmerrittPowerLawdf as _osipkovmerrittPowerLawdf,
)
from .quasiisothermaldf import quasiisothermaldf as _quasiisothermaldf
from .sphericaldf import sphericaldf as _sphericaldf
from .streamdf import streamdf as _streamdf
from .streamgapdf import streamgapdf as _streamgapdf
from .streamspraydf import (
    chen24spraydf as _chen24spraydf,
)
from .streamspraydf import (
    fardal15spraydf as _fardal15spraydf,
)
from .streamspraydf import (
    pericenter_stripping_pdf as _pericenter_stripping_pdf,
)
from .streamspraydf import (
    streamspraydf as _streamspraydf,
)
from .streamTrack import (
    StreamTrack as _StreamTrack,
)
from .streamTrack import (
    StreamTrackPair as _StreamTrackPair,
)

type DynamicDF = Callable[..., object]

df = _df
chen24spraydf = _chen24spraydf
fardal15spraydf = _fardal15spraydf
pericenter_stripping_pdf = _pericenter_stripping_pdf
streamspraydf = _streamspraydf
StreamTrack = _StreamTrack
StreamTrackPair = _StreamTrackPair

constantbetadf = _constantbetadf
constantbetaHernquistdf = _constantbetaHernquistdf
constantbetaPowerLawdf = _constantbetaPowerLawdf
eddingtondf = _eddingtondf
evolveddiskdf = _evolveddiskdf
isotropicHernquistdf = _isotropicHernquistdf
isotropicNFWdf = _isotropicNFWdf
isotropicPlummerdf = _isotropicPlummerdf
isotropicPowerLawdf = _isotropicPowerLawdf
kingdf = _kingdf
osipkovmerrittdf = _osipkovmerrittdf
osipkovmerrittHernquistdf = _osipkovmerrittHernquistdf
osipkovmerrittNFWdf = _osipkovmerrittNFWdf
osipkovmerrittPowerLawdf = _osipkovmerrittPowerLawdf
quasiisothermaldf = _quasiisothermaldf
sphericaldf = _sphericaldf
streamdf = _streamdf
streamgapdf = _streamgapdf

diskdf: DynamicDF
dehnendf: DynamicDF
shudf: DynamicDF
schwarzschilddf: DynamicDF
DFcorrection: DynamicDF
surfaceSigmaProfile: DynamicDF
expSurfaceSigmaProfile: DynamicDF
impulse_deltav_plummer: DynamicDF
impulse_deltav_plummer_curvedstream: DynamicDF
impulse_deltav_hernquist: DynamicDF
impulse_deltav_hernquist_curvedstream: DynamicDF
impulse_deltav_general: DynamicDF
impulse_deltav_general_curvedstream: DynamicDF
impulse_deltav_general_orbitintegration: DynamicDF
impulse_deltav_general_fullplummerintegration: DynamicDF
impulse_deltav_plummerstream: DynamicDF
impulse_deltav_plummerstream_curvedstream: DynamicDF

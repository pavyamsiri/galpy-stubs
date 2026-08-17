from collections.abc import Callable
from typing import assert_type

from galpy.util import conversion

assert_type(conversion.dens_in_msolpc3(220.0, 8.0), float)
assert_type(conversion.freq_in_Gyr(220.0, 8.0), float)
assert_type(conversion.get_physical(object()), dict[str, object])

def scale(value: float) -> float: ...

decorated: Callable[..., object] = conversion.physical_conversion("length")(scale)
assert_type(decorated, Callable[..., object])

from configparser import ConfigParser
from typing import assert_type

import galpy
from galpy.util import config, multi, quadpack

assert_type(galpy.__version__, str)
assert_type(galpy.configfilename, str)
assert_type(config.fix_config(), ConfigParser)
assert_type(config.check_config(config.fix_config()), bool)

values = multi.parallel_map(lambda value: value + 1, [1, 2, 3])
assert_type(values, map[int] | list[int])

def square(value: float) -> float: ...

assert_type(quadpack.quadrature(square, 0.0, 1.0), tuple[float, float])
assert_type(quadpack.romberg(square, 0.0, 1.0), float)

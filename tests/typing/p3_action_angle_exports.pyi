from typing import assert_type

import galpy.actionAngle as aa
from galpy.actionAngle.actionAngle import actionAngle
from galpy.actionAngle.actionAngleHarmonic import actionAngleHarmonic

assert_type(aa.actionAngle, type[actionAngle])
assert_type(aa.actionAngleHarmonic, type[actionAngleHarmonic])

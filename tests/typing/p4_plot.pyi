import numpy as np
from galpy.util import plot

plot.hist(np.array([1.0, 2.0, 3.0]))
plot.dens2d(np.ones((2, 2)))
plot.scatterplot(np.ones(2), np.ones(2))

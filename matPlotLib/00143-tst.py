# use masked arrays to plot a line with different colors by y-value
import numpy as np
import matplotlib.pyplot as plt

t = np.arange(0.0, 2.0, 0.01)
s = np.sin(2*np.pi*t) * 2

upper = 0.77
lower = -0.77


supper = np.ma.masked_where(s < upper, s)
slower = np.ma.masked_where(s > lower, s)
smiddle = np.ma.masked_where(np.logical_or(s < lower, s > upper), s)
zero = np.ma.masked_where(np.logical_or(s > 0.2, s < -0.2), s)

plt.plot(t, smiddle, t, slower, t, supper, t, zero)
plt.show()
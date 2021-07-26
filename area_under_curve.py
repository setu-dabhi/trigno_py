import numpy as np
from scipy.integrate import simps
from numpy import trapz
import matplotlib.pyplot as plt
#x = np.arange(0,1*np.pi,0.01)
x = np.arange(0,10,0.01)
#print(x)
#y = (np.cos(x)+np.sin(x))
y = (np.cos(x)-3*np.sin(x)+4)
print(y)
# The y values.  A numpy array is used here,
# but a python list could also be used.
#y = np.array([5, 20, 4, 18, 19, 18, 7, 4])

# Compute the area using the composite trapezoidal rule.
area = trapz(abs(y), dx=0.01)
print("area =", int(area))

# Compute the area using the composite Simpson's rule.
area = simps(abs(y), dx=0.01)
print("area =", int(area))

fig, ax  = plt.subplots()
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.plot(x, y)
plt.show()


import matplotlib.pyplot as plt
import numpy as np

retsX = np.random.normal(0.0, 1.0, size=1000)
retsY = np.random.normal(0.0, 1.0, size=1000)

#time series plot
plt.plot(retsX)
plt.show()

plt.plot(retsY)
plt.show()

#histogram
plt.hist(retsX)
plt.show()

plt.hist(retsY)
plt.show()

#scatter plot
plt.scatter(retsX, retsY)
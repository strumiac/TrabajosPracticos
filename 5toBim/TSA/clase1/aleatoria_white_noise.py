import numpy as np
import matplotlib.pyplot as plt

X = np.random.normal(2, 0.5, 100)

plt.plot(X)
plt.plot(2*np.ones(100), '--r')
plt.title(r'Ruido blanco ($\mu = 2$, $\sigma = 0.5$)', fontsize = 14)
plt.show()
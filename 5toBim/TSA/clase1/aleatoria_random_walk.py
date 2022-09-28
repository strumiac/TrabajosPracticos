from cProfile import label
import numpy as np
import matplotlib.pyplot as plt

X = np.random.normal(0, 1, 500)
Y = np.cumsum(X)

plt.plot(X, label = '$e_{t}$')
plt.plot(Y, label = '$Y_{t}$')
plt.title(r'Caminata aleatoria ($e_{t}$ con $\mu = 0$, $\sigma = 1$)', fontsize = 14)
plt.legend()
plt.show()
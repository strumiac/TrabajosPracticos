import numpy as np
import matplotlib.pyplot as plt

nube = 100
centroide_n = 4
epochs = 5
colors = np.array(["red","green","blue","purple","black","orange","pink","beige","brown","gray","cyan","magenta","yellow"])


X = np.random.rand(nube,2)
centroide_ix = np.random.randint(low = 0, high = nube - 1, size = centroide_n)
C = X[centroide_ix]

fig = plt.figure(figsize=(5, 5))
plt.scatter(X[:,0],X[:,1])
plt.scatter(C[:,0],C[:,1], marker = 'x', c = 'r')
plt.title('Nube aleatoria')
plt.show()


def dist_centroide(C, X):
  C_broad=np.reshape(np.repeat(C, X.shape[0], axis = 0), (C.shape[0],X.shape[0],X.shape[1]))
  dist_a_centroide = np.sqrt(np.sum((X-C_broad)**2, axis = 2))
  return dist_a_centroide

def get_cluster(dist_a_centroide):
  return np.argmin(dist_a_centroide, axis = 0)


for j in range(epochs):
  fig = plt.figure()
  ax = fig.add_subplot(111, autoscale_on=False)
  print (C)
  for i in range(centroide_n):
    cluster = get_cluster(dist_centroide(C, X))
    # para plotear
    X_plot = X[np.where(cluster == i)[0]]
    ax.scatter(X_plot[:,0], X_plot[:,1], c = colors[i])
    ax.scatter(C[i,0], C[i,1], c = colors[i], marker = 'x', s = 200)
    ax.set_xlim([-0.1, 1.1])
    ax.set_ylim([-0.1, 1.1])
    C[i] = np.mean(X[np.where(cluster == i)[0]], axis = 0)
    
  ax.set_title(f"Epochs: {j+1}")  
  plt.show()
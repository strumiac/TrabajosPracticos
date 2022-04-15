import numpy as np
from sklearn.decomposition import PCA

X = np.array([[0.8,0.7],[0.1,-0.1]]) # R^(d x n)

def pca_a_mano(X, n_comp = 1):
    d = X.shape[0]
    X_centered = X - np.mean(X, axis = 0)
    S = np.cov(X_centered.T)
    eigvalue, eigvector = np.linalg.eig(S)
    idx = eigvalue.argsort()[::-1]
    eigvalue = eigvalue[idx]
    eigvector = eigvector[:,idx]
    z = X_centered.dot(eigvector[:, :n_comp])
    return z

z_pca = pca_a_mano(X)
print('Proyeccion a la 1er componente (a mano):\n', z_pca)

pca = PCA(n_components = 1)
pca.fit(X)
z_skl=pca.transform(X)
print('Proyección a la 1er componente (scikit learn):\n', z_skl)

np.testing.assert_allclose(z_pca, z_skl)
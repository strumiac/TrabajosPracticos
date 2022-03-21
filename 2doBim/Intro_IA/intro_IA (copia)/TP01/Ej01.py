import numpy as np

def norma_0(matriz):
    norma = np.count_nonzero(matriz, axis = 1, keepdims = True)
    return norma

def norma_1(matriz):
    norma = np.sum(np.abs(matriz), axis = 1, keepdims = True)
    return norma

def norma_2(matriz):
    norma = np.sqrt(np.sum(np.power(matriz, 2), axis = 1, keepdims = True))
    return norma

def norma_inf(matriz):
    norma = np.max(np.abs(matriz), axis = 1, keepdims = True)
    return norma

a = np.array([[1,3],[0,-4]])

print('La norma L0 de a es:\n',norma_0(a))
print('La norma L1 de a es:\n',norma_1(a))
print('La norma L2 de a es:\n',norma_2(a))
print('La norma Linf de a es:\n',norma_inf(a))

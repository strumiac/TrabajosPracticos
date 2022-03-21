import numpy as np

def norma_2(matriz):
    norma = np.argsort(np.sqrt(np.sum(np.power(matriz, 2), axis = 1)))
    ind = norma[::-1]
    return ind

# matriz
a = np.array([[0,-4],[1,3],[4,-5]])

print('La matriz original es:\n',a)
print('La matriz original ordenada según L2 es:\n',a[norma_2(a)])
#print('Forma de la matriz: ',a[norma_2(a)].shape)
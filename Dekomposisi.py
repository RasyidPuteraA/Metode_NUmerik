import numpy as np

def decomposition(A):
    n = len(A)
    L = np.zeros((n, n))
    U = np.zeros((n, n))
    for p in range(n):
        for j in range(p, n):
            sum = np.dot(L[p, :p], U[:p, j])
            U[p, j] = A[p, j] - sum
        for i in range(p, n):
            sum = np.dot(L[i, :p], U[:p, p])
            L[i, p] = (A[i, p] - sum) / U[p, p]
            if p == i:
                L[i, p] = 1
    return L, U

def solve_LU(A, b):
    L, U = decomposition(A)
    t = np.linalg.solve(L, b)
    x = np.linalg.solve(U, t)
    return x

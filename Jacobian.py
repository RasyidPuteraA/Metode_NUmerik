import numpy as np

def jacobi(A, b, x0, tol=1e-8, max_iter=1000):
    """
    Metode Jacobi untuk menyelesaikan sistem persamaan linear Ax=b
    dengan memulai iterasi dari x0 dan menggunakan toleransi tol dan
    maksimum iterasi max_iter.
    """
    n = len(b)
    x = x0.copy()
    iterasi = 0

    # Pengecekan syarat cukup koefisien persamaan dominan secara diagonal
    is_diagonal_dominant = True
    for i in range(n):
        if abs(A[i,i]) < np.sum(np.abs(A[i,:])) - abs(A[i,i]):
            is_diagonal_dominant = False
            break

    if not is_diagonal_dominant:
        print("Matriks koefisien A tidak memenuhi syarat koefisien persamaan dominan secara diagonal.")
        return None, iterasi

    for k in range(max_iter):
        x_new = np.zeros_like(x)
        for i in range(n):
            x_new[i] = (b[i] - np.dot(A[i,:], x) + A[i,i]*x[i]) / A[i,i]
        err = np.linalg.norm(x_new - x)
        if err < tol:
            break
        x = x_new.copy()
        iterasi += 1

    return x, iterasi
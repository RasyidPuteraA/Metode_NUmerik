import numpy as np

def gauss_seidel(A, b, x0, tol=1e-8, max_iter=1000):
    """
    Metode Gauss-Seidel untuk menyelesaikan sistem persamaan linear Ax=b
    dengan memulai iterasi dari x0 dan menggunakan toleransi tol dan
    maksimum iterasi max_iter.
    """
    n = len(b)
    x = x0.copy()
    iterasi = 0

    for k in range(max_iter):
        for i in range(n):
            # Menghitung x[i] pada iterasi k+1
            x[i] = (b[i] - np.dot(A[i,:i], x[:i]) - np.dot(A[i,i+1:], x0[i+1:])) / A[i,i]
        # Menghitung selisih ||x^(k+1)-x^(k)||2
        err = np.linalg.norm(x-x0)
        if err < tol:
            break
        # Memperbarui nilai x0 untuk iterasi selanjutnya
        x0 = x.copy()
        iterasi += 1

    return x, iterasi

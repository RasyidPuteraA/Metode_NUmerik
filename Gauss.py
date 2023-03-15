import numpy as np

def gauss_elimination(A):
    """
    Fungsi untuk melakukan eliminasi Gauss pada SPL
    
    Parameters:
        A (numpy.ndarray): matriks augmented SPL
    
    Returns:
        A (numpy.ndarray): matriks augmented setelah eliminasi Gauss
        solutions (numpy.ndarray): array solusi SPL setelah eliminasi Gauss
    """
    # eliminasi Gauss
    for i in range(A.shape[0]):
        # pivot untuk memilih baris utama
        pivot = A[i, i]
        # normalisasi baris utama dengan pivot
        A[i, :] /= pivot
        # operasi pada baris lainnya untuk mengeliminasi variabel pada kolom i
        for j in range(i+1, A.shape[0]):
            factor = A[j, i] / A[i, i]
            A[j, :] -= factor * A[i, :]
    
    # back-substitution
    solutions = np.zeros(A.shape[0])
    for i in range(A.shape[0]-1, -1, -1):
        # inisialisasi nilai x dengan konstanta di matriks augmented
        solutions[i] = A[i, -1]
        # operasi pada variabel yang belum diketahui
        for j in range(i+1, A.shape[0]):
            solutions[i] -= A[i, j] * solutions[j]
    
    return A, solutions

import numpy as np

def gauss_jordan(A):
    """
    Fungsi untuk melakukan eliminasi Gauss-Jordan pada SPL
    
    Parameters:
        A (numpy.ndarray): matriks augmented SPL
    
    Returns:
        A (numpy.ndarray): matriks augmented setelah eliminasi Gauss-Jordan
        solutions (numpy.ndarray): array solusi SPL setelah eliminasi Gauss-Jordan
    """
    # eliminasi Gauss-Jordan
    for i in range(A.shape[0]):
        # pivot untuk memilih baris utama
        pivot = A[i, i]
        # normalisasi baris utama dengan pivot
        A[i, :] /= pivot
        # operasi pada baris lainnya untuk mengeliminasi variabel pada kolom i
        for j in range(A.shape[0]):
            if j != i:
                factor = A[j, i] / A[i, i]
                A[j, :] -= factor * A[i, :]
    
    # solusi SPL
    solutions = A[:, -1]
    
    return A, solutions

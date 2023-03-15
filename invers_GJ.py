import numpy as np

def inverse(A):
    """
    Fungsi untuk menghitung invers dari matriks A menggunakan metode Matriks Balikan
    
    Parameters:
        A (numpy.ndarray): matriks input
    
    Returns:
        A_inv (numpy.ndarray): matriks invers dari A
    """
    # menghitung determinan A
    det_A = np.linalg.det(A)
    
    # matriks tidak dapat diinvers jika determinannya nol
    if det_A == 0:
        print("Matriks tidak dapat diinvers")
        return None
    else:
        # menghitung matriks balikan
        print("Matriks dapat diinvers")
        A_inv = np.linalg.inv(A)
        return A_inv

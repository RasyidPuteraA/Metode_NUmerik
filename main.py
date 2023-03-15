import numpy as np
from Gauss import gauss_elimination
from Gauss_Jordan import gauss_jordan
from Dekomposisi import decomposition
from Dekomposisi import solve_LU

while True:
    #Versi Komplit
    A = np.array([[2, 8, 6, 20], [4, 2, -2, -2], [3, -2, 1, 12]], dtype=float)

    #Versi Parsial X
    a = np.array([[2, 8, 6], [4, 2, -2], [3, -2, 1]], dtype=float)
    b = np.array([20, -2, 12], dtype=float)
    
    
    print("\n\nPilih metode penyelesaian SPL:")
    print("1. Gauss")
    print("2. Gauss-Jordan")
    print("3. Dekomposisi LU")
    print("4. Keluar")
    choice = input("Masukkan pilihan Anda (1/2/3/4): ")

    if choice == '1':
        # panggil fungsi gauss_elimination dari modul gauss_elimination
        A_gauss, x_gauss = gauss_elimination(A)

        # menampilkan solusi SPL setelah eliminasi Gauss
        print("\n\nMetode Eliminasi Gauss:")
        print("Matriks augmented setelah eliminasi Gauss:\n", A_gauss)
        print("Solusi SPL: ", x_gauss)

    elif choice == '2':
        # panggil fungsi gauss_jordan dari modul gauss_jordan
        A_gauss_jordan, x_gauss_jordan = gauss_jordan(A)

        # menampilkan solusi SPL setelah eliminasi Gauss-Jordan
        print("\n\nMetode Eliminasi Gauss-Jordan:")
        print("Matriks augmented setelah eliminasi Gauss-Jordan:\n", A_gauss_jordan)
        print("Solusi SPL: ", x_gauss_jordan)

    elif choice == '3':
        L, U = decomposition(A)
        print("\n\nMetode Dekomposisi LU:")
        print("Matriks L :\n", L)
        print("\nMatriks U :\n", U)
        x = solve_LU(a,b)
        print("Solusi SPL: ", x)

    elif choice == '4':
        break

    else:
        print("Pilihan tidak valid. Silakan coba lagi.")


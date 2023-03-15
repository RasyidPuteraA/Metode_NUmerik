import numpy as np
from Gauss import gauss_elimination
from Gauss_Jordan import gauss_jordan
from Dekomposisi import decomposition
from Dekomposisi import solve_LU
from invers_GJ import inverse
from Gauss_Seidel import gauss_seidel
from Jacobian import jacobi

while True:

    print("\n\nPilih metode penyelesaian SPL:")
    print("1. Gauss")
    print("2. Gauss-Jordan")
    print("3. Dekomposisi LU")
    print("4. Invers Gauss Jordan")
    print("5. Jacobian")
    print("6. Gauss-Seidel")
    print("7. Keluar")
    choice = input("Masukkan pilihan Anda (1/2/3/4/5/6/7): ")

    if choice == '1' or choice == '2' or choice == '3' or choice == '4' or choice == '5' or choice == '6':
        n = int(input("Masukkan ukuran matriks A: "))
        A = np.zeros((n,n), dtype=float)
        b = np.zeros(n, dtype=float)

        print("Masukkan elemen matriks A dan vektor b:")
        for i in range(n):
            for j in range(n):
                A[i,j] = float(input("A[" + str(i+1) + "," + str(j+1) + "] = "))
            b[i] = float(input("b[" + str(i+1) + "] = "))

    if choice == '1':
        # panggil fungsi gauss_elimination dari modul gauss_elimination
        A_gauss, x_gauss = gauss_elimination(np.concatenate((A,b[:,None]), axis=1))

        # menampilkan solusi SPL setelah eliminasi Gauss
        print("\n\nMetode Eliminasi Gauss:")
        print("Matriks augmented setelah eliminasi Gauss:\n", A_gauss)
        print("Solusi SPL: ", x_gauss)

    elif choice == '2':
        # panggil fungsi gauss_jordan dari modul gauss_jordan
        A_gauss_jordan, x_gauss_jordan = gauss_jordan(np.concatenate((A,b[:,None]), axis=1))

        # menampilkan solusi SPL setelah eliminasi Gauss-Jordan
        print("\n\nMetode Eliminasi Gauss-Jordan:")
        print("Matriks augmented setelah eliminasi Gauss-Jordan:\n", A_gauss_jordan)
        print("Solusi SPL: ", x_gauss_jordan)

    elif choice == '3':
        L, U = decomposition(A)
        print("\n\nMetode Dekomposisi LU:")
        print("Matriks L :\n", L)
        print("\nMatriks U :\n", U)
        x = solve_LU(L, U, b)
        print("Solusi SPL: ", x)
        
    elif choice == '4':
        
        B_invers = inverse(A)
        # menampilkan solusi SPL setelah eliminasi Gauss-Jordan Invers
        print("\n\nMetode Invers Gauss-Jordan:")
        print("Matriks augmented setelah eliminasi Gauss-Jordan untuk invers:\n",B_invers)
        
    elif choice == '5':
        x0 = np.zeros_like(b)
        tol = 1e-8
        max_iter = 1000
        A_jacobi, x_jacobi = jacobi(A, b, x0, tol=tol, max_iter=max_iter)
        # menampilkan solusi SPL setelah eliminasi Gauss-Jordan Invers
        print("\n\nMetode Jacobi:")
        print("Matriks augmented setelah Metode Jacobi:\n",A_jacobi)
        print("Jumlah Iterasi : ", x_jacobi)
        
    elif choice == '6':
        x0 = np.zeros_like(b)
        tol = 1e-8
        max_iter = 1000
        A_gauss_seidel, x_gauss_seidel = gauss_seidel(A, b, x0, tol=tol, max_iter=max_iter)
        
        # menampilkan solusi SPL setelah eliminasi Gauss-Seidel
        print("\n\nMetode Gauss-Seidel:")
        print("Matriks augmented setelah Metode Gauss-Seidel:\n",A_gauss_seidel)
        print("Jumlah Iterasi : ", x_gauss_seidel)
        
    elif choice == '7':
        print("\n\nTerimakasih Telah Menggunakan Program SPL\n\tBy 21524002_KOM\n\n")
        break

    else:
        print("\n\nPilihan tidak valid. Silakan coba lagi.\n\n")

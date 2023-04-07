import random
from bisection import bisection
from regula_falsi import regulafalsi
from Newton_raphson import newtonraphson
from Secant import secant


n = input("Masukkan NIM: ")
print(f"\nPersamaan yang akan diselesaikan: f(x) = x^2 - A = 0\n")
A = int(n[-3:])
print("Persamaan baru: x^2 - {} = 0".format(A))
while True:
    
    print("\n\nPilih metode penyelesaian :")
    print("1. Bisection")
    print("2. Regula Falsi")
    print("3. Newton - Raphson")
    print("4. Secant")
    print("5. Keluar")
    choice = input("Masukkan pilihan Anda (1/2/3/4/5): \n")

    if choice == '1' or choice == '2' or choice == '3' or choice == '4' or choice == '5':
        print("...")
        
    if choice == '1':
        solution1 = bisection(A)
        print("Solusi: {:.4f}".format(solution1))
        
    elif choice == '2':
        solution2 = regulafalsi(A)
        print("Solusi: {:.4f}".format(solution2))
    
    elif choice == '3':
        x1 = random.uniform(0, A)
        print(f'X1 = ',(x1))
        solution3 = newtonraphson(A, x1, 100)
        print("Solusi: {:.4f}".format(solution3))
        
    elif choice == '4':
        x1 = random.uniform(0, A)
        x2 = random.uniform(0, A)
        print(f'X1 = ',(x1))
        print(f'X2 = ',(x2))
        solution4 = secant(A, x1, x2, 100)
        
    elif choice == '5':
        print("\n\nTerimakasih Telah Menggunakan Program \n\tBy 21524002_KOM\n\n")
        break

    else:
        print("\n\nPilihan tidak valid. Silakan coba lagi.\n\n")

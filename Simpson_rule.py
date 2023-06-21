from simpsons_one_third import simpsons_one_third
from simpsons_three_eighth import simpsons_three_eighth

while True:
    
    print("\n\nPilih metode penyelesaian :")
    print("1. Simpson's 1/3 Rule (8 Segment)")
    print("2. Simpson's 3/8 Rule")
    print("3. Keluar")
    choice = input("Masukkan pilihan Anda (1/2/3): \n")
    if choice == '1' or choice == '2' :
        a = float(input("Masukkan batas bawah (a): "))
        b = float(input("Masukkan batas atas (b): "))
        n = int(input("Masukkan Jumlah Segment: "))
        
    if choice == '1':
        result1 = simpsons_one_third(a,b,n)
        print("\n\nSimpson's 1/3 Rule (8 Segment):")
        print(f"Hasil dengan segment {n} : {round(result1, 4)}\n")
    elif choice == '2':
        result2 = simpsons_three_eighth(a,b,n)
        print("\n\nsimpsons_three_eighth:")
        print(f"Hasil dengan segment {n} : {round(result2, 4)}\n")

    elif choice == '3':
        print("\n\nTerimakasih Telah Menggunakan Program Simpson Rule\n\tBy 21524002_KOM\n\n")
        break

    else:
        print("\n\nPilihan tidak valid. Silakan coba lagi.\n\n")




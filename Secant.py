def secant(a, x1, x2, iterasi):
    # inisialisasi nilai x3
    x3 = x2 - (x2 - x1) / ((x2**2 - a) - (x1**2 - a)) * (x2**2 - a)

    # melakukan iterasi sampai ditemukan solusi yang cukup akurat
    for i in range(iterasi):
        # menghitung f(x3) dan abs(f(x3))
        f_x3 = x3**2 - a
        abs_f_x3 = abs(f_x3)

        # jika abs(f(x3)) sudah cukup kecil, maka x3 adalah solusi yang cukup akurat
        if abs_f_x3 <= 0.001:
            print(f"x1 dan x2 konvergen dan memiliki solusi: {x3}")
            return x3
        
        # jika x3 tidak konvergen, maka hentikan proses
        if abs(x3 - x2) >= abs(x2 - x1):
            print("x1 dan x2 tidak konvergen dan tidak memiliki solusi")
            return None
        
        # update nilai x1, x2, dan x3, dan lanjutkan iterasi
        x1 = x2
        x2 = x3
        x3 = x2 - (x2 - x1) / ((x2**2 - a) - (x1**2 - a)) * (x2**2 - a)

    # jika iterasi selesai dan belum menemukan solusi yang cukup akurat, maka x3 adalah solusi terbaik yang ditemukan
    print(f"x1 dan x2 konvergen tetapi belum menemukan solusi yang cukup akurat: {x3}")
    return x3
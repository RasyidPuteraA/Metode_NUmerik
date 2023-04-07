def newtonraphson(a, x1, iterasi):
    # inisialisasi nilai x2
    x2 = x1 - (x1**2 - a) / (2 * x1)

    # melakukan iterasi sampai ditemukan solusi yang cukup akurat
    for i in range(iterasi):
        # menghitung f(x2) dan abs(f(x2))
        f_x2 = x2**2 - a
        abs_f_x2 = abs(f_x2)

        # jika abs(f(x2)) sudah cukup kecil, maka x2 adalah solusi yang cukup akurat
        if abs_f_x2 <= 0.001:
            return x2
        
        # jika x2 tidak konvergen, maka hentikan proses
        if abs(f_x2 - (x2**2 - a) / (2 * x2)) >= abs_f_x2:
            return None
        
        # update nilai x2 dan lanjutkan iterasi
        x1 = x2
        x2 = x1 - (x1**2 - a) / (2 * x1)

    # jika iterasi selesai dan belum menemukan solusi yang cukup akurat, maka x2 adalah solusi terbaik yang ditemukan
    return x2

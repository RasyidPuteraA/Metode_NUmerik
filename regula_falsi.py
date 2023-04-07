def regulafalsi(a):
    # menentukan batas bawah dan atas
    batas_bawah = 0
    batas_atas = a

    # melakukan iterasi sampai ditemukan solusi yang cukup akurat
    while True:
        # mencari titik potong garis
        nilai_tengah = batas_atas - ((batas_atas - batas_bawah) / (2 * a - batas_bawah))

        # menghitung f(nilai_tengah)
        f_tengah = nilai_tengah ** 2 - a

        # jika f(nilai_tengah) cukup kecil, maka nilai_tengah adalah solusi yang cukup akurat
        if abs(f_tengah) < 0.0001:
            return nilai_tengah
    
        # jika f(nilai_tengah) positif, maka cari solusi di sebelah kiri nilai_tengah
        elif f_tengah > 0:
            batas_atas = nilai_tengah
    
        # jika f(nilai_tengah) negatif, maka cari solusi di sebelah kanan nilai_tengah
        else:
            batas_bawah = nilai_tengah

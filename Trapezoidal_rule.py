
a = float(input("Masukkan batas bawah (a): "))
b = float(input("Masukkan batas atas (b): "))


def f(x):
    return 5 - 2*x - 4*x**2 - 2*x**5


def trapezoidal_rule(a, b, n):
    h = (b - a) / n
    # Memulai dengan jumlah f(a) dan f(b)
    integral_sum = (f(a) + f(b)) / 2.0
    # Menambahkan nilai f(x) pada titik-titik dalam interval
    for i in range(1, n):
        x = a + i * h
        integral_sum += f(x)
    # Mengalikan dengan h untuk mendapatkan hasil integral
    integral = h * integral_sum
    return integral


intervals = [2, 4, 8]
for n in intervals:
    result = trapezoidal_rule(a, b, n)
    # Mencetak hasil dengan format yang jelas
    print(f"Hasil dengan {n} interval: {round(result, 4)}\n")
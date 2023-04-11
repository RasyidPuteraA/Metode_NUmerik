import math

# Fungsi untuk menghitung nilai f(x)
def f(x):
    return 0.25 * x**4 - 1.1 * x**3 + 1.75 * x**2 - 2 * x

# Menentukan interval awal
xL = -2
xU = 4

# Menentukan panjang interval
L = xU - xL

# Menentukan nilai phi (golden ratio)
phi = (math.sqrt(5) + 1) / 2

# Menentukan toleransi epsilon
epsilon = 1e-6

# Iterasi metode golden section
while L > epsilon:
    # Menentukan panjang interval baru
    L = L / phi

    # Menentukan dua titik dalam interval baru
    x1 = xU - L
    x2 = xL + L

    # Menghitung nilai f(x) pada dua titik tersebut
    f1 = f(x1)
    f2 = f(x2)

    # Membandingkan nilai f(x) pada dua titik tersebut
    if f1 < f2:
        xU = x2
    else:
        xL = x1

# Nilai x optimum yang menghasilkan nilai minimum
x_optimum = (xL + xU) / 2

# Nilai minimum dari fungsi f(x)
min_value = f(x_optimum)

# Menampilkan hasil
print("Nilai x optimum yang menghasilkan nilai minimum: ", x_optimum)
print("Nilai minimum dari fungsi f(x): ", min_value)

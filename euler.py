#Metode Euler
x0 = int(input("Masukkan Kondisi awal x: "))
y0 = int(input("\nMasukkan Kondisi awal y: "))
h = float(input("\nMasukkan Ukuran langkah (step size): "))
x_target = int(input("\nMasukkan Nilai x yang ingin dicapai: "))

def f(x, y):
    return -2*x**3 + 12*x**2 - 20*x + 8.5

def euler_method(x0, y0, h, x_target):
    x = x0
    y = y0

    while x < x_target:
        y += h * f(x, y)
        x += h

    return y

result = euler_method(x0, y0, h, x_target)
print(f"\nHasil : {round(result, 4)}\n")

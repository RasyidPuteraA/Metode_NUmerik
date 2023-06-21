from fx_sr import f

def simpsons_one_third(a, b, n):
    if n % 2 != 0:
        print("Jumlah segmen harus genap.")
        return None

    h = (b - a) / n
    x = a
    integral = f(x)

    for i in range(1, n):
        x += h
        if i % 2 == 0:
            integral += 2 * f(x)
        else:
            integral += 4 * f(x)

    integral += f(b)
    integral *= h / 3

    return integral
from fx_sr import f

def simpsons_three_eighth(a, b, n):
    h = (b - a) / n
    x0 = a
    x1 = a + h
    x2 = a + 2*h
    x3 = b

    integral = (f(x0) + 3*f(x1) + 3*f(x2) + f(x3)) * h * 3 / 8

    return integral
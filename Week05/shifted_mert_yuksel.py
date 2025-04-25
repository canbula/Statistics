def shifted(x):

    n = len(x)

    x_bar = sum(x) / n

    if n % 2 == 1:
        x_tilde = x[int((n + 1) / 2 - 1)]
    else:
        x_tilde = (x[int((n / 2) - 1)] + x[int(n / 2)]) / 2

    diff = abs(x_bar - x_tilde)

    return int(diff * 100) 

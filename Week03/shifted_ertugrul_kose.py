def shifted(values):
    n = len(values)
    sorted_vals = sorted(values)
    avg = sum(values) / n

    if n % 2 == 0:
        med = (sorted_vals[n // 2] + sorted_vals[n // 2 - 1]) / 2
    else:
        med = sorted_vals[n // 2]

    return abs(avg - med) / abs(avg) * 100

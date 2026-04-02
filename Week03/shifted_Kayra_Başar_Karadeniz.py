def shifted(sample):
    x, y = sorted(sample), len(sample)
    mn = sum(x) / y
    if y % 2 != 0:
        md = x[y // 2]
    else:
        md = (x[y // 2 - 1] + x[y // 2]) / 2
    return abs(mn - md) / abs(mn) * 100 if mn != 0 else 0

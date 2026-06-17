def shifted(data):
    d = sorted(map(abs, data))
    n = len(d)
    avg, med = sum(d) / n, (d[n//2] + d[~(n//2)]) / 2
    return int(abs(avg - med) / avg * 100)

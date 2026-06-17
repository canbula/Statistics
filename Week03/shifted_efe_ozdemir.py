def shifted(sample):
    s = sorted(sample)
    n = len(s)
    avg = sum(s) / n
    med = s[n // 2] if n % 2 else (s[n // 2 - 1] + s[n // 2]) / 2

    if avg == 0:
        return 0
    return abs(avg - med) / abs(avg) * 100

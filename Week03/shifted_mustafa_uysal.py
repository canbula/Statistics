def shifted(data):
    n = len(data)
    if n == 0: return 0
    mean = sum(data) / n
    s = sorted(data)
    median = s[n // 2] if n % 2 == 1 else (s[(n // 2) - 1] + s[n // 2]) / 2
    if mean == 0: return 0
    return (abs(mean - median) / abs(mean)) * 100

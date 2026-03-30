def shifted(data):
    n = len(data)
    if n == 0: return 0.0
    mean = sum(data) / n
    s = sorted(data)
    mid = n // 2
    med = (s[mid-1] + s[mid]) / 2 if n % 2 == 0 else s[mid]
    if mean == 0: return 0.0
    return abs((mean - med) / mean) * 100

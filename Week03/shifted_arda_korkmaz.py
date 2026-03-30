def shifted(data):
    if not data: return 0.0
    n = len(data)
    mean = sum(data) / n
    s = sorted(data)
    mid = n // 2
    if n % 2 == 0:
        median = (s[mid - 1] + s[mid]) / 2
    else:
        median = s[mid]
    if median == 0: return 0.0
    return ((mean - median) / median) * 100

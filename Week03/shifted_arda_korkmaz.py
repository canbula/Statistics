def shifted(data):
    n = len(data)
    if n == 0: return 0.0
    mean = sum(data) / n
    s = sorted(data)
    mid = n // 2
    res = (s[mid-1] + s[mid]) / 2 if n % 2 == 0 else s[mid]
    if res == 0: return 0.0
    return abs((mean - res) / res) * 100

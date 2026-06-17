def shifted(data):
    n, s = len(data), sorted(data)
    mean = sum(data) / n
    if n % 2 != 0: median = s[n // 2]
    else: median = (s[n // 2 - 1] + s[n // 2]) / 2
    return abs((mean - median) / mean) * 100

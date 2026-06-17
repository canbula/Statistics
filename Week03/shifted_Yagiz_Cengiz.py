def shifted(data):
    if not data: return 0
    n, s = len(data), sorted(data)
    mean = sum(data) / n
    median = s[n // 2] if n % 2 != 0 else (s[n // 2 - 1] + s[n // 2]) / 2
    return (abs(mean - median) / abs(mean)) * 100 if mean != 0 else 0

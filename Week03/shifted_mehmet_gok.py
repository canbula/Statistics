def shifted(data):
    m, s, l = sum(data) / len(data), sorted(data), len(data)
    med = (s[l//2] + s[(l-1)//2]) / 2
    return abs(m - med) / abs(m) * 100 if m != 0 else 0

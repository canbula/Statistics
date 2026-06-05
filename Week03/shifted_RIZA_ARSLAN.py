def shifted(data):
    if not data or sum(data) == 0: return 0.0
    ortalama = sum(data) / len(data)
    sirali = sorted(data)
    medyan = (sirali[len(data) // 2] + sirali[~(len(data) // 2)]) / 2
    return (abs(ortalama - medyan) / abs(ortalama)) * 100

def shifted(data):
    data.sort()
    size = len(data)
    mean = sum(data) / size
    if size % 2 == 1:
        median = data[size // 2]
    else:
        median = (data[size // 2-1] + data[size // 2]) / 2
    return abs((mean - median) / mean) * 100
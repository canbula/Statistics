def shifted(data):
    if not data:
        return 0
    data.sort()
    mean = sum(data) / len(data)
    median = data[len(data) // 2] if len(data) % 2 == 1 else (data[len(data) // 2 - 1] + data[len(data) // 2]) / 2
    difference = mean - median
    percentage = abs((difference / mean)) * 100
    return percentage

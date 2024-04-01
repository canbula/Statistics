def shifted(data):
    sorted_data = sorted(data)
    mean = sum(data) / len(data)
    if len(data) % 2 != 0:
        median = sorted_data[len(data) // 2]
    else:
        median = (sorted_data[len(data) // 2 - 1] + sorted_data[len(data) // 2]) / 2
    difference = abs(mean - median)
    percentage = abs((difference / mean) * 100)
    return percentage

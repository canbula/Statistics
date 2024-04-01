def shifted(data):
    total = sum(data)
    length = len(data)
    sorted_data = sorted(data)
    mean = total / length

    if length % 2 != 0:
        median = sorted_data[length // 2]
    else:
        median = (sorted_data[length // 2 - 1] + sorted_data[length // 2]) / 2

    difference = abs(mean - median)
    percentage = abs((difference / mean) * 100)

    return percentage

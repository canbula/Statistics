def shifted(data):
    sorted_data = sorted(data)
    if len(data) % 2 != 0:
        median = sorted_data[len(data) // 2]
    else:
        median = (sorted_data[len(data) // 2 - 1] + sorted_data[len(data) // 2]) / 2
    difference = abs((sum(data) / len(data)) - median)
    percentage = abs((difference / (sum(data) / len(data))) * 100)
    return percentage

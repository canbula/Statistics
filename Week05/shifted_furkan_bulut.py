def shifted(data):
    if not data:
        return "There is not data to calculate the shifted mean and median. Please provide a valid data."
    mean = sum(data) / len(data)
    data_sorted = sorted(data)
    n = len(data_sorted)
    if n % 2 == 0:
        median = (data_sorted[n // 2 - 1] + data_sorted[n // 2]) / 2
    else:
        median = data_sorted[n // 2]
    diff = abs(((mean - median) / ((mean + median) / 2)) * 100)
    return diff



def shifted(data):
    if not data: return "There is no data to calculate the shifted mean and median. Please provide valid data."
    mean = sum(data) / len(data)
    median = sorted(data)[len(data) // 2] if len(data) % 2 else sum(sorted(data)[len(data) // 2 - 1:len(data) // 2 + 1]) / 2
    return abs(((mean - median) / ((mean + median) / 2)) * 100) if median else "Invalid data."

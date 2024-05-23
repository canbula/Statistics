def shifted(data):
    # Check if the list is empty
    if len(data) == 0:
        return None
    # Calculate the mean
    mean = sum(data) / len(data)
    # Calculate the median
    median = sorted(data)[len(data) // 2] if len(data) % 2 != 0 else (sorted(data)[len(data) // 2 - 1] + sorted(data)[len(data) // 2]) / 2    # If the number of elements is odd, median is the middle value. If the number of elements is even, median is the average of two middle values.
    difference = abs(mean - median) / mean * 100  # Calculate the percentage difference between mean and median
    return difference

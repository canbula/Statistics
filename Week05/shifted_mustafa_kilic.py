import statistics

def shifted(data):
    if not data:
        return None

    mean = sum(data) / len(data)
    median = statistics.median(data)

    if median == 0:
        return 0

    percentage_shift = abs((mean - median / median)) * 100

    return percentage_shift

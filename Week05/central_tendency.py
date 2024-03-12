def mean(data):
    return sum(data) / len(data)


def median(data):
    data = sorted(data)
    n = len(data)
    if n % 2 == 1:
        return data[int((n + 1) / 2) - 1]
    return (data[(n // 2) - 1] + data[((n // 2) + 1) - 1]) / 2


def mode(data):
    counts = {}
    for value in data:
        if value in counts:
            counts[value] += 1
        else:
            counts[value] = 1
    max_count = max(counts.values())
    mode = [value for value, count in counts.items() if count == max_count]
    return mode


if __name__ == "__main__":
    data = [1, 2, 3, 4, 5]
    print("Data:", data)
    print("Mean:", mean(data))
    print("Median:", median(data))
    data = [1, 2, 3, 4, 5, 6]
    print("Data:", data)
    print("Mean:", mean(data))
    print("Median:", median(data))
    data = [1, 2, 2, 3, 4, 5, 5, 5, 6, 7, 8, 9]
    print("Data:", data)
    print("Mean:", mean(data))
    print("Median:", median(data))
    print("Mode:", mode(data))
    data = [1, 2, 2, 3, 4, 5, 5, 6]
    print("Data:", data)
    print("Mean:", mean(data))
    print("Median:", median(data))
    print("Mode:", mode(data))

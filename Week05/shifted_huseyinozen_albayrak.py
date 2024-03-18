import central_tendency as ct

def shifted(data):
    mean = ct.mean(data)
    median = ct.median(data)
    return abs((mean - median) / mean) * 100

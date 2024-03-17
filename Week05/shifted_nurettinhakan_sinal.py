import central_tendency as c

def shifted(data):
    mean = c.mean(data)
    median = c.median(data)
    result = abs((mean - median)/mean) * 100
    return result

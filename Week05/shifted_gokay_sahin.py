import central_tendency

def shifted(data):
    mean = central_tendency.mean(data)
    median = central_tendency.median(data)
    return ((mean - median) / mean ) * 100

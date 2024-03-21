
def shifted(first):
    mean = central_tendency.mean(first)
    median = central_tendency.median(first)
    result = abs(((mean - median) / mean) * 100) 
    return result

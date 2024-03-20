import central_tendency

def shifted(first):
    mean = central_tendency.mean(first)
    median = central_tendency.median(first)
    percentage = abs(((mean - median) / mean) * 100) 
    return percentage

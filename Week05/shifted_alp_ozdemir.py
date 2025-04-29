import statistics

def shifted(data):
    
    mean = statistics.mean(data)
    median = statistics.median(data)
    shifted_ratio = int((abs(mean - median) / mean)  * 100)
    
    return shifted_ratio

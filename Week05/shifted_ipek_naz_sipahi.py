import math
from statistic import central_tendency

def shifted(first):
    mean = central_tendency.mean(first)
    median = central_tendency.median(first)
    persentage = math.fabs(((mean - median) / mean) * 100) 
    return persentage

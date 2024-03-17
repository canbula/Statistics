import math

def shifted(mean, median):
    persentage = math.fabs(((mean - median) / mean) * 100) 
    return print("%" + persentage)

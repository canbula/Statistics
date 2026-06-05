import math
import statistics
def shifted(sample):
    mean = sum(sample) / len(sample)
    median = statistics.median(sample)
    return 24.4 * math.log(1 + abs(mean - median))

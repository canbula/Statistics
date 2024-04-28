import sys

sys.path.append(".")


from Week02 import data
from Week05 import central_tendency


def range(x):
    """Return the range of x."""
    return max(x) - min(x)


def variance(x):
    """Return the variance of x."""
    mean = central_tendency.mean(x)
    return sum((xi - mean) ** 2 for xi in x) / (len(x) - 1)


def standard_deviation(x):
    """Return the standard deviation of x."""
    return variance(x) ** 0.5


def coefficient_of_variation(x):
    """Return the coefficient of variation of x."""
    return standard_deviation(x) / central_tendency.mean(x)


if __name__ == "__main__":
    x = data.x
    print(f"Data: {x}")
    print(f"Range: {range(x)}")
    print(f"Variance: {variance(x)}")
    print(f"Standard Deviation: {standard_deviation(x)}")
    print(f"Coefficient of Variation: {coefficient_of_variation(x)}")
    y = data.y
    print(f"Data: {y}")
    print(f"Range: {range(y)}")
    print(f"Variance: {variance(y)}")
    print(f"Standard Deviation: {standard_deviation(y)}")
    print(f"Coefficient of Variation: {coefficient_of_variation(y)}")

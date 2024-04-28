import sys


sys.path.append(".")

from Week02 import data
from Week05 import central_tendency
from Week06 import variation


def covariance(x, y):
    """Return the covariance of x and y."""
    mean_x = central_tendency.mean(x)
    mean_y = central_tendency.mean(y)
    return sum((xi - mean_x) * (yi - mean_y) for xi, yi in zip(x, y)) / (len(x) - 1)


def correlation_coefficient(x, y):
    """Return the correlation coefficient of x and y."""
    return covariance(x, y) / (
        variation.standard_deviation(x) * variation.standard_deviation(y)
    )


def r2(x, y):
    """Return the R^2 value of x and y."""
    return correlation_coefficient(x, y) ** 2


def linear_regression(x, y):
    """Return the linear regression of x and y."""
    mean_x = central_tendency.mean(x)
    mean_y = central_tendency.mean(y)
    slope = covariance(x, y) / variation.variance(x)
    intercept = mean_y - slope * mean_x
    return slope, intercept


def predict(x, slope, intercept):
    """Return the predicted y values for x."""
    return [slope * xi + intercept for xi in x]


if __name__ == "__main__":
    x = data.x
    y = data.y
    print(f"Covaariance: {covariance(x, y)}")
    print(f"Correlation Coefficient: {correlation_coefficient(x, y)}")
    print(f"R^2: {r2(x, y)}")
    slope, intercept = linear_regression(x, y)
    print(f"Linear Regression: y = {intercept:.2f} + {slope:.2f}x")
    print(f"Actual Values: {y}")
    print(f"Predicted Values: {predict(x, slope, intercept)}")

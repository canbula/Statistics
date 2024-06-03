import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score


def quiz_q(X, y):
    # returns coefficients and R^2 score of a linear regression model
    model = LinearRegression()
    model.fit(X, y)
    return model.intercept_, model.coef_, r2_score(y, model.predict(X))


def main():
    student_id = input("Enter your student ID: ")
    x = [i for i in range(1, 12)]
    X = [[i for i in range(1, 12)]]
    y = [int(s) for s in student_id]
    y = sorted(y)
    print(X)
    print(y)
    print(f"{len(x):4d} {sum(x):4d} {sum(y):4d}")
    print(
        f"{sum(x):4d} {sum([i**2 for i in x]):4d} {sum([i * j for i, j in zip(x, y)]):4d}"
    )
    X = np.array(X).reshape(-1, 1)
    y = np.array(y).reshape(-1, 1)
    print(quiz_q(X, y))


if __name__ == "__main__":
    while True:
        main()

import sys

sys.path.append(".")


from Week02 import data
import random
from pprint import pprint
import numpy as np
import pandas as pd


# show all columns and rows for pandas
pd.set_option("display.max_columns", None)
pd.set_option("display.max_rows", None)


def weighted_srs(data, n, weights, with_replacement=False):
    if with_replacement:
        return random.choices(data, weights=weights, k=n)
    return random.sample(data, n, counts=weights)


def generate_persons(num_persons):
    if num_persons < 1:
        raise ValueError("Number of persons must be at least 1")

    # generate a weighted list of cities
    weighted_cities = {
        "Manisa": 1000,
        "İzmir": 500,
        "Ankara": 200,
        "İstanbul": 200,
    }
    weights = []
    for city in data.cities:
        weights.append(weighted_cities.get(city, 1))
    cities = weighted_srs(data.cities, num_persons, weights)

    num_male_names = num_persons // 2
    num_female_names = num_persons - num_male_names
    persons = []

    for num, first_names in zip(
        [num_male_names, num_female_names],
        [data.first_names_male, data.first_names_female],
    ):
        for _ in range(num):
            first_name = random.choice(first_names)
            surname = random.choice(data.surnames)
            city = random.choice(cities)
            persons.append({"first_name": first_name, "surname": surname, "city": city})

    return persons


# One-hot encoding with pandas
def one_hot_encode(data, categories):
    encoded = np.zeros((len(data), len(categories)), dtype=int)
    for i, category in enumerate(data):
        encoded[i, categories.index(category)] = 1
    return pd.DataFrame(encoded, columns=categories)


if __name__ == "__main__":
    # generate 10 persons
    persons = generate_persons(10)
    pprint(persons)
    # one-hot encode the cities
    cities = list(data.cities)
    df = one_hot_encode([person["city"] for person in persons], cities)
    df["first_name"] = [person["first_name"] for person in persons]
    df["surname"] = [person["surname"] for person in persons]
    # drop the city columns if no one is from that city
    df = df.loc[:, (df != 0).any(axis=0)]
    print(df)

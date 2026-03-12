import random  # I only allowed the use of the random module


def weighted_srs(data, n, weights=None, with_replacement=False):
    if weights is None:
        weights = [1] * len(data)
    if with_replacement:
        return random.choices(data, weights=weights, k=n)
    sample, population, pop_weights = [], list(data), list(weights)
    for _ in range(n): # set up a loop for the desired sample size
        selected = random.choices(population, weights=pop_weights, k=1)[0]
        sample.append(selected)
        idx = population.index(selected)
        population.pop(idx), pop_weights.pop(idx)
    return sample

cities = ["manisa", "izmir", "istanbul", "aydın", "ankara"] # population list

city_weights = [0.3, 0.2, 0.2, 0.2, 0.1] 
selected_cities = weighted_srs(cities, 1, weights=city_weights, with_replacement=False)

print("sample result", selected_cities)

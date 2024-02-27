import sys

sys.path.append(".")


from Week02 import data
import random


def simple_random_sampling(data, n, replacement=False):
    if replacement:
        return [random.choice(data) for _ in range(n)]
    return random.sample(data, min(n, len(data)))


def stratified_sampling(data, n, strata):
    sample = []
    for key in strata:
        sample += random.sample(data[key], min(n // len(strata), len(data[key])))
    return sample


def cluster_sampling(data, n, clusters):
    picked_clusters = random.sample(clusters, min(n, len(clusters)))
    sample = []
    for cluster in picked_clusters:
        sample += data[cluster]
    sample = list(set(sample))
    return sample


def systematic_sampling(data, n):
    sample = []
    for i in range(0, len(data), n):
        sample.append(data[i])
    return sample


srs_sample = simple_random_sampling(data.cities, 10)
print(srs_sample)

stratified_sample = stratified_sampling(data.cities_by_region, 15, data.regions)
print(stratified_sample)

cluster_sample = cluster_sampling(data.cities_by_region, 2, data.regions)
print(cluster_sample)

systematic_sample = systematic_sampling(data.cities, 5)
print(systematic_sample)

true_srs_sample = simple_random_sampling(data.cities, 30, True)
print(true_srs_sample)

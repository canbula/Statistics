import random

def weighted_srs(data, n, weights, with_replacement=False):
    if with_replacement:
        return random.choices(data, weights=weights, k=n)
    secimler = []
    veri, agirlik = list(data), list(weights)
    for _ in range(n):
        secilen = random.choices(veri, weights=agirlik, k=1)[0]
        indeks = veri.index(secilen)
        secimler.append(veri.pop(indeks))
        agirlik.pop(indeks)
    return secimler

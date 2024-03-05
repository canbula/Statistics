import random
#weighted_srs fonksiyonunu oluştur, parametreler: data, n(seçilecek öğe sayısı, weights(öğelerin seçilme ağırlığı,
#with_replacement(seçilen öğenin listeye geri eklenip eklenmemesi)
def weighted_srs(data, n, weights, with_replacement=False):
    #geri yerine eklencekse data'dan n adet öğe al ve bu işlemi weights'e göre yap, eklenmeyecekse random.sample() kullanarak ağırlıksız öğe seç; return ile de sonucu döndür.
    if with_replacement == True or weights != None :
        randomlist = random.choices(data, k=n, weights = weights)
    else:
        random.list = random.sample(data, n)
    return randomlist

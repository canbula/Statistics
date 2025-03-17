def shifted(arr):
   arr.sort()  # Liste elemanlarını sırala
   mid = len(arr) // 2    # Listenin ortasındaki elemanın indexi
   mean = sum(arr) / len(arr)   # Ortalama
     # Medyan
   if len(arr) % 2 == 0:
        median = (arr[mid - 1] + arr[mid]) / 2
    else:
        median = arr[mid]

    # Farkı ve yüzdelik değişimini hesapla
    difference = mean - median
    percentage = (difference / mean) * 100

    return percentage

# Örnek olarak bir liste tanımlayalım
liste = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# shifted fonksiyonunu kullanarak listenin farkını hesaplayalım
sonuc = shifted(liste)
print("Ortalama ile medyan arasındaki farkın yüzdesi:", sonuc)

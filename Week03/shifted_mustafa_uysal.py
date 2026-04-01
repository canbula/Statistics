def shifted(data):
    n = len(data)
    if n == 0:
        return 0
        
    # 1. average (Mean) calculation
    mean = sum(data) / n
    
    # 2. Median calculation
    sorted_data = sorted(data)
    # if data is odd
    if n % 2 == 1:
        median = sorted_data[n // 2]
    # id data is even
    else:
        median = (sorted_data[(n // 2) - 1] + sorted_data[n // 2]) / 2
        
    # 3. Yüzdelik Fark (Percentage Difference) Hesaplama
    # Mean ile Median arasındaki farkın, Mean'e göre yüzde kaçlık bir sapma yarattığını hesaplar.
    if mean == 0:
        return 0 # Sıfıra bölünme hatasını önlemek için
        
    percentage_difference = (abs(mean - median) / abs(mean)) * 100
    
    return percentage_difference

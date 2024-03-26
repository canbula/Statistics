def shifted(data):
  data = sorted(data)
  n = len(data)
  mean = sum(data)/n
  median = data[n//2] if n % 2 == 1 else (data[n//2 - 1] + data[n//2])/2
  return (abs(mean - median)/mean) * 100

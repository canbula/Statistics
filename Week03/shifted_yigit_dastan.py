def shifted(data):
  length = len(data)
  s_data = sorted(data)
  mean = sum(data) / length
  if length % 2 == 0:
    median = (s_data[length // 2] + s_data[length // 2 - 1]) / 2
  else:
    median = s_data[length // 2]
  return abs(mean - median) / abs(mean) * 100
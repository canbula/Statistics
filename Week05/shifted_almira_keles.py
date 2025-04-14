def shifted(data):
if len(data) == 0:
    return Non  
  mean = sum(data) / len(data)
 sorted_data = sorted(data)
   if len(data) % 2 == 0:
      median = (sorted_data[len(data)//2 - 1] + sorted_data[len(data)//2]) / 2
    else:    
        median = sorted_data[len(data)//2]
   difference = mean - median
   percentage_difference = (difference / mean) * 100
      return percentage_difference

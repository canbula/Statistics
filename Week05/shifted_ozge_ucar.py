def shifted(data):
    if not data:
        return None
    mean = sum(data)/len(data)
    sorted_data = sorted(data)
    print(f'your mean is: {mean}')
    i = len(sorted_data)
    if i % 2 == 1:
        median = sorted_data[(i + 1) // 2 - 1]
        print(f'your median is: {median}')
    else:
        median = (sorted_data[i // 2 - 1] + data[i // 2]) / 2
        print(f'your median is: {median}')
    return (mean - median)
data= [33,45,45,46,47,56,57,58,62]
print(f'Your Difference between mean and median is: {shifted(data)}')

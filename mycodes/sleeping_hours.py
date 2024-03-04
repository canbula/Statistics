#Ozgur Ucar 210316032
sleeping_values = [7,7,6.5,7,6.5,8,6.5,8.5,8,8,8,8.5,7,7,7.5,7,5,7,7,7,7,7,9.5,7.5,6,7]

sleeping_dictionary = {}
sleeping_values.sort()
for s in sleeping_values:
    if s in sleeping_dictionary.keys():
        sleeping_dictionary[s] += 1
    else:
        sleeping_dictionary[s] = 1
print(f"Dictionary of data {sleeping_dictionary}")

max = max(sleeping_dictionary.values())
print("-------------------------------------------")
print("     Dot Plot Vision")
for i in range(max, 0 , -1):
    if i > 0:
        for key in sleeping_dictionary:
            if i == sleeping_dictionary[key]:
                print("○", end='     ')
                sleeping_dictionary[key] -= 1
            else:
                print(" ", end='     ')
        print("")
print("--------------------------------------------")
for key in sleeping_dictionary:
    print(f"{key}", end= '    ')

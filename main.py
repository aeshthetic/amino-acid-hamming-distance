import data
import compare 

animals = []

for item in compare.distance_list:
    animals.insert(0, item[0])

inequality = " < ".join(animals)

print(inequality)



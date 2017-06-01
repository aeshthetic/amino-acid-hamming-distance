import Levenshtein
import data

def massCompare(animal):
    comparisons = []
    for subject, sequence in data.animals.items():
            comparisons.insert(0, h_distance(data.animals[animal], sequence))
                
    return comparisons

def h_distance(sequence_1, sequence_2):
    return sum(e1 != e2 for e1, e2 in zip(sequence_1, sequence_2))


comparisons = {
}

for animal, sequence in data.animals.items():
    comparisons[animal] = massCompare(animal)

           
average_distance = {}

for animal, distance in comparisons.items():
    average_distance[animal] = (sum(distance)/9)
    

distance_list = []

for animal, distance in average_distance.items():
    distance_list.insert(0, [animal, distance])

def getKey(item):
    return item[1]
    
distance_list = sorted(distance_list, key=getKey)



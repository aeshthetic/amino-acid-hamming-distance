import Levenshtein
import data

def massCompare(animal):
    comparisons = []
    for subject, sequence in data.animals.items():
            comparisons.insert(0, Levenshtein.ratio(data.animals[animal], sequence))
                
    return comparisons

def h_distance(sequence_1, sequence_2):
    return sum(e1 != e2 for e1, e2 in zip(sequence_1, sequence_2))


comparisons = {
}

for animal, sequence in data.animals.items():
    comparisons[animal] = massCompare(animal)

            
average_ratios = {}

for animal, ratio in comparisons.items():
    average_ratios[animal] = (sum(ratio)/10)
    

ratio_list = []

for animal, ratio in average_ratios.items():
    ratio_list.insert(0, [animal, ratio])

def getKey(item):
    return item[1]
    
ratio_list = sorted(ratio_list, key=getKey)

import Levenshtein
import data

def compare_all(animal):
    comparisons = []
    for subject, sequence in data.animals.items():
            comparisons.insert(0, Levenshtein.ratio(data.animals[animal], sequence))
                
    return comparisons

comparisons = {}

for animal, sequence in data.animals.items():
    comparisons[animal] = compare_all(animal)


def printComparisons():
    for animal, sequence in data.animals.items():
        for alt, alt_seq in data.animals.items():
            print(f"{animal} and {alt}: {Levenshtein.ratio(sequence, alt_seq)}")
            
average_ratios = {}

for animal, ratio in comparisons.items():
    average_ratios[animal] = (sum(ratio)/10)
    

ratio_list = []

for animal, ratio in average_ratios.items():
    ratio_list.insert(0, [animal, ratio])

def getKey(item):
    return item[1]
    
ratio_list = sorted(ratio_list, key=getKey)

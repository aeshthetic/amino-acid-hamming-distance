import json

sequences = open("./sequences.json", "r")

data = json.load(sequences)

def massCompare(animal):
    return [h_distance(data[animal], sequence) for sequence in data.values()]

def h_distance(sequence_1, sequence_2):
    return sum(e1 != e2 for e1, e2 in zip(sequence_1, sequence_2))


comparisons = {animal: massCompare(animal) for animal in data}
           
average_distance = {animal: sum(distance)/9 for animal, distance in comparisons.items()}

distance_list = sorted(list(average_distance.items()), key=lambda i: i[1])

sequences.close()

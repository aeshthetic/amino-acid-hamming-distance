import compare 
import matplotlib.pyplot as plt

animals = [item[0] for item in compare.distance_list]
distances = [item[1] for item in compare.distance_list]
inequality = " < ".join(animals)

plt.bar([1, 2, 3, 4, 5, 6, 7, 8, 9], distances, label="Animals", color="b")
plt.xlabel("Animal")
plt.ylabel("Average Common Acids")
plt.title("Average Hamming Distance of Amino Acid Sequences")

plt.legend()
plt.show()

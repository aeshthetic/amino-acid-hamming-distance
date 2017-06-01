# Levenshtein Comparison of Amino Acid Sequences of 10 Organisms

This repository contains the source for a script I wrote to assist in the completion of an assignment for my Biology class. The materials included raw amino acid sequences for 10 organisms, and asked us to analyze the sequences and create a cladogram using our analysis. Our solution was to compare the similarity in the sequences to find out which organism was "most similar" to the others. We accomplished this by

1. Converting the sequences to strings
2. Creating a dictionary of the sequences and their animal names
3. Creating empty shells of data structures to be filled through iteration
4. Iterating through the dictionary of sequences and animal names in a handful of ways in order to represent our data in more workable ways. E.g. storing the levenshtein ratios for each animal (and all the others compared to it) in a dictionary entry, averaging these ratios and storing them in a multidimensional list for sorting
5. Sorting the list comparing the average of each animal's levenshtein ratios and representing the resultant in an inequality

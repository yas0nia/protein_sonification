# imports used libraries below
import random

c_minor_scale = ["C", "D", "Eb", "F", "G", "Ab", "Bb", "C"]

# for every element in c_minor_scale adds every number between 1 and 5 to the end of the element in the list and saves the new list in a mapped_list
mapped_list = [x + str(i) for x in c_minor_scale for i in range(1, 6)]


codons = {
    'GCT': 'A', 'GCA': 'A', 'GCG': 'A', 'GCC': 'A',
    'CGT': 'R', 'CGC': 'R', 'CGA': 'R', 'AGA': 'R', 'AGG': 'R', 'CGG': 'R',
    'AAT': 'N', 'AAC': 'N',
    'GAT': 'D', 'GAC': 'D',
    'TGT': 'C', 'TGC': 'C',
    'CAA': 'Q', 'CAG': 'Q',
    'GAA': 'E', 'GAG': 'E',
    'GGT': 'G', 'GGC': 'G', 'GGA': 'G', 'GGG': 'G',
    'CAT': 'H', 'CAC': 'H',
    'ATT': 'I', 'ATC': 'I', 'ATA': 'I',
    'CTT': 'L', 'CTC': 'L', 'CTA': 'L', 'CTG': 'L', 'TTA': 'L', 'TTG': 'L',
    'AAA': 'K', 'AAG': 'K',
    'ATG': 'M',
    'TTT': 'F', 'TTC': 'F',
    'CCT': 'P', 'CCC': 'P', 'CCA': 'P', 'CCG': 'P',
    'TCT': 'S', 'TCC': 'S', 'TCA': 'S', 'TCG': 'S', 'AGT': 'S', 'AGC': 'S',
    'ACT': 'T', 'ACC': 'T', 'ACA': 'T', 'ACG': 'T',
    'TGG': 'W',
    'TAT': 'Y', 'TAC': 'Y',
    'GTT': 'V', 'GTC': 'V', 'GTA': 'V', 'GTG': 'V',
    'TAA': 'STOP', 'TGA': 'STOP', 'TAG': 'STOP'
}

# create a list of single letter amino acids
single_letter_amino_acids = ['A', 'R', 'N', 'D', 'C', 'Q', 'E', 'G',
                             'H', 'I', 'L', 'K', 'M', 'F', 'P', 'S', 'T', 'W', 'Y', 'V', 'STOP']

# for each element of single_letter_amino_acids map selects a random element from mapped_list if the element !== "STOP" and saves it in a dictionary "random_mappings"
random_melody_mappings = {x: random.choice(
    mapped_list) for x in single_letter_amino_acids if x != "STOP"}


print(random_melody_mappings)

#!/usr/bin/env python3

# Protein input
protein_input = input("Enter Protein (one letter code) : ")

# Converting the protein abbriviations to uppercase.
protein_input = protein_input.upper()

# Checking if wrong amino acid code is entered.
amino_acids = [ "A", "R", "N", "D", "C", "Q", "G", "E", "H", "I", "L", "K", "M", "F", "P", "S", "T", "W", "Y", "V" ]
wrong_input = False
for aa in protein_input:
    if aa not in amino_acids:
        print("Wrong input")
        wrong_input = True
        break

# Checking if protein starts with Methionine or not.
if protein_input[0] != "M" and wrong_input == False:
    print("Note : The protein does not starts from Methionine")

# Making list of protein.
protein_list = []
for aa in protein_input:
    protein_list.append(aa)

# Key for Abbreviation.
nt_key = { "A" : "Adenoside",
        "C" : "Cytidine",
        "T" : "Thymidine",
        "G" : "Guanosine",
        "U" : "Uridine",
        "R" : "A, G",
        "Y" : "C, T",
        "W" : "A, T",
        "S" : "C, G",
        "M" : "A, C",
        "K" : "G, T",
        "B" : "C, G, T",
        "D" : "A, G, T",
        "H" : "A, C, T",
        "V" : "A, C, G"
}

# Function to convert amino acid into codon.
def protein_to_nt(protein_list):
    list_of_codons = []

    if wrong_input == True:
        error_msg = "Please check the amino acid sequence you entered."
        return error_msg

    for aa in protein_list:
        if aa == "M" :                        # Methionine
            codon = ("A", "U", "G")
            list_of_codons.append(codon)
        elif aa == "A" :                      # Alanine
            codon = ("G", "C", "X")
            list_of_codons.append(codon)
        elif aa == "N" :                      # Asparagine
            codon = ("A", "A", "Y")
            list_of_codons.append(codon)
        elif aa == "D" :                      #Aspartate
            codon = ("G", "A", "Y")
            list_of_codons.append(codon)
        elif aa == "C" :                      # Cystine
            codon = ("U", "G", "Y")
            list_of_codons.append(codon)
        elif aa == "Q" :                      # Glutamine
            codon = ("C", "A", "R")
            list_of_codons.append(codon)
        elif aa == "G" :                      # Glycine
            codon = ("G", "G", "X")
            list_of_codons.append(codon)
        elif aa == "E" :                      # Glutamate
            codon = ("G", "A", "R")
            list_of_codons.append(codon)
        elif aa == "H" :                      # Histidine
            codon = ("C", "A", "Y")
            list_of_codons.append(codon)
        elif aa == "I" :                      # Isoleucine
            codon = ("A", "U", "H")
            list_of_codons.append(codon)
        elif aa == "K" :                      # Lysine
            codon = ("A", "A", "R")
            list_of_codons.append(codon)
        elif aa == "F" :                      # Phenylalanine
            codon = ("U", "U", "Y")
            list_of_codons.append(codon)
        elif aa == "P" :                      # Proline
            codon = ("C", "C", "X" )
            list_of_codons.append(codon)
        elif aa == "T" :                      # Threonine
            codon = ("A", "C", "X")
            list_of_codons.append(codon)
        elif aa == "W" :                      # Tryptophan
            codon = ("U", "G", "G")
            list_of_codons.append(codon)
        elif aa == "Y" :                      # Tyrosine
            codon = ("U", "A", "Y")
            list_of_codons.append(codon)
        elif aa == "V" :                      # Valine
            codon = ("G", "U", "X")
            list_of_codons.append(codon)
        elif aa == "L" :                      # Leucine
            codon = ("Y", "U", "X")
            list_of_codons.append(codon)
        elif aa == "R" :                      # Argenine
            codon = ("M", "G", "X")
            list_of_codons.append(codon)
        elif aa == "S" :                      # Serine
            codon = ("W", "S", "X")
            list_of_codons.append(codon)


    return list_of_codons



# Driver code

codon_list = protein_to_nt(protein_list)
print("\nThe corrosponing nucleotide sequence is : \n" , codon_list)


# key
print("\n\nKey : ")
print("\t{:^15} {:<15}".format("Abbreviation", "Base"))
for key, value in nt_key.items():
    print("\t{:^15} {:<15}".format(key, value))

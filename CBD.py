
import sys
from sys import *


nucelotide_sequence = open(sys.argv[1], "r")
codons = open(sys.argv[2], "r")


def amino_acids(): #in part 2, possibly consider removing this function because it is not needed. Can just take everything in the start and pass that through
    amino_dict = {} #this will store a dict of the amino acids
    for line in codons:
        line = line.strip()
        if line: #this makes sure that the lines that are empty do not get filled? 

            codon, acid = line.split()[:2] #this splits the codons and gets just the two first parts that are needed
            amino_dict[codon.lower()] = acid.lower() #turns it lowercase to check
    return amino_dict

def makelist(DNA, amino_dict):
    amino_list = ""
    for line in DNA:

        line = line.strip().upper() #makes it uppercase 
        if(line[0] != '>'): #doesn't start checkign until after the starting value 
         for char in range(0, len(line), 3): #for loop that checks 3 

            codon= line[char:char+3]
            amino_list += amino_dict[codon.lower()].upper() #added upper to ensure we get uppercase results back
            
    return amino_list #returns list

amino_dict = amino_acids() #takes both and compares them before printing
amino_list = makelist(nucelotide_sequence, amino_dict)
    
print(amino_list) #prints the list back
        








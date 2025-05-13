#import library to read fasta file
from Bio import SeqIO

#def a fucntion to load sequence from fasta file
def load_seq(file):
    return str(next(SeqIO.parse(file, 'fasta')).seq)

#def a function to calculate Hamming distance and percentage of identical amino acids
def Hamming_distance(seq1, seq2):
    edit_distance = 0
    identical_amino_acid = len(seq1)
    for i in range(len(seq1)):
        if seq1[i] != seq2[i]:
            edit_distance += 1
            identical_amino_acid -= 1
    identical_percentage = identical_amino_acid / len(seq1) * 100
    return edit_distance, identical_percentage

#name the seq
human_seq = load_seq('human.fasta')
mouse_seq = load_seq('mouse.fasta')
random_seq = load_seq('random.fasta')

#calculate Hamming distance and percentage of identical amino acids
distance_human_mouse = Hamming_distance(human_seq, mouse_seq)
distance_human_random = Hamming_distance(human_seq, random_seq)
distance_mouse_random = Hamming_distance(mouse_seq, random_seq)

#print the result
print(f'The Hamming distance between human and mouse SOD2 sequences is: {distance_human_mouse[0]}, and the percentage of identical amino acids is: {distance_human_mouse[1]}%')
print(f'The Hamming distance between human SOD2 sequence and random sequence is: {distance_human_random[0]}, and the percentage of identical amino acids is: {distance_human_random[1]}%')
print(f'The Hamming distance between mouse SOD2 sequence and random sequence is: {distance_mouse_random[0]}, and the percentage of identical amino acids is: {distance_mouse_random[1]}%')
#import library to read fasta file
from Bio import SeqIO
import blosum as bl
matrix = bl.BLOSUM(62)

#def a fucntion to load sequence from fasta file
def load_seq(file):
    return str(next(SeqIO.parse(file, 'fasta')).seq)

#def a function to calculate Hamming distance and percentage of identical amino acids
def alignment_score(seq1, seq2):
    alignment_score = 0
    identical_amino_acid = len(seq1)
    for i in range(len(seq1)):
            alignment_score += matrix[seq1[i]][seq2[i]]
            if seq1[i] != seq2[i]:
                identical_amino_acid -= 1
    identical_percentage = identical_amino_acid / len(seq1) * 100
    return alignment_score, identical_percentage

#name the seq
human_seq = load_seq('human.fasta')
mouse_seq = load_seq('mouse.fasta')
random_seq = load_seq('random.fasta')

#calculate Hamming distance and percentage of identical amino acids
alignment_human_mouse = alignment_score(human_seq, mouse_seq)
alignment_human_random = alignment_score(human_seq, random_seq)
alignment_mouse_random = alignment_score(mouse_seq, random_seq)

#print the result
print(f'The alignment score between human and mouse SOD2 sequences is: {alignment_human_mouse[0]}, and the percentage of identical amino acids is: {alignment_human_mouse[1]}%')
print(f'The alignment score between human SOD2 sequence and random sequence is: {alignment_human_random[0]}, and the percentage of identical amino acids is: {alignment_human_random[1]}%')
print(f'The alignment score between mouse SOD2 sequence and random sequence is: {alignment_mouse_random[0]}, and the percentage of identical amino acids is: {alignment_mouse_random[1]}%')
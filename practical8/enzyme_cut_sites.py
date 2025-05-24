#define a function to check if the nucleotides in the DNA sequence only contain A, T, G, C
def check_nucleotides(seq):
    for nucleotide in seq:
        if nucleotide not in 'ATGC':
            return False
    return True
            
def enzyme_cut_sites(dna_seq, recognised_seq):
    
    #check if the sequences contain only A, T, G, C
    if check_nucleotides(dna_seq) == False or check_nucleotides(recognised_seq) == False:
        print('invalid nucleotides in the sequence')
    
    #create an empty list to store the cut sites
    cut_sites = []
    for i in range(len(dna_seq) - len(recognised_seq) + 1):
        if dna_seq[i:i + len(recognised_seq)] == recognised_seq:
            cut_sites.append(i+1)

    return cut_sites

if __name__=='__main__':
    #input the DNA sequence to be cut
    dna_seq = input('enter the DNA sequence to be cut: ').strip().upper()

    #if the DNA sequence is valid, ask for the input of restriction enzyme recognised sequence
    recognised_seq = input('enter the recognised sequence: ').strip().upper()

    sites = enzyme_cut_sites(dna_seq, recognised_seq)

    if sites:
        print(f"Cut sites found at positions: {sites}")
    else:
        print("No cut sites found")

    #appropiate example:
    #dna_seq = 'ATCGATCGATCGATCG'
    #recognised_seq = 'CGAT'
    #expected output: cut sites found at positions: [3, 7, 11]
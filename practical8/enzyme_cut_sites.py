def enzyme_cut_sites(dna_seq, recognised_seq):
    dna_seq=input('enter the DNA sequence to be cut: ')
    for nucleotide in dna_seq:
        if nucleotide not in ['A','T','G','C']:
            raise ValueError('DNA sequence should only contain A, T, G, C')
    else:
        recognised_seq=input('enter the recognised sequence: ')
        for nucleotide in recognised_seq:
            if nucleotide not in ['A','T','G','C']:
                raise ValueError('sequence recognised by restriction enzyme should only contain A, T, G, C')
        else:
            cut_sizes=[]
            enzyme_len=len(recognised_seq)
            for i in range(len(dna_seq)-enzyme_len+1):
                if dna_seq[i:i+enzyme_len]==recognised_seq:
                    cut_sizes.append(i+1)
            if cut_sizes==[]:
                print('no cut site found')
            else:
                return cut_sizes

if __name__=='__main__':
    #appropiate example:
    
    try:
        test_dna_seq='ATCGATCGATCGATCG'
        test_recognised_seq='CGAT'
        sites=enzyme_cut_sites(test_dna_seq, test_recognised_seq)
        print(f'cut sites found at positions: {sites}')
    except ValueError as e:
        print(e)
    # example with non-canonical nucleotides
    try:
        non_canonical_seq='ATCGANCGATCGATCG'
        sites=enzyme_cut_sites(non_canonical_seq, test_recognised_seq)
    except ValueError as e:
        print(e)
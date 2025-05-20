import re
with open('tata_genes.fa', 'r') as input, open('tata_box.fa', 'w') as output:
    current_gene=[]#initialize a variable to store the current gene name
    current_sequence=[]#initialize an empty list to store the current sequence
    tata_pattern=re.compile(r'TATA[AT]A[AT]')#define a regular expression pattern to match TATWAW
    for line in input: #iterate through each line in the file
        if re.search(r'^>\w+_mRNA',line):#check gene name line
            if current_gene and current_sequence:#if the current gene and sequence are not empty
                full_sequence=''.join(line.strip() for seq in current_sequence)#join the sequence lines
                if tata_pattern.search(full_sequence):#check if the sequence includes TATWAW
                    output.write(f'{current_gene}\n')
                    output.writelines(current_sequence)#write the sequence to the output file                   
            current_gene=re.findall(r'(>\w+)_mRNA',line)#extract the gene name
            current_sequence=[]
        else:#for seqenece line
            current_sequence.append(line)  #add the sequence line to the current sequence list

    #write the last gene and sequence to the output file
    if current_gene and current_sequence:#if the current gene and sequence are not empty
        full_sequence=''.join(line.strip() for line in current_sequence)#join the sequence lines
        if tata_pattern.search(full_sequence):#check if the sequence includes TATWAW
            gene_match=re.search(r'>(\w+)_mRNA',current_gene[0])#extract the gene name
            if gene_match:#if the gene name is found
                output.write(f'>{current_gene[0]}\n')
                output.writelines(current_sequence)

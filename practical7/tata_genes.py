import re

with open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa', 'r') as input, open('tata_genes.fa', 'w') as output:
    #initialize lists to store the current gene name and sequence
    current_gene = []
    current_sequence = []
    tata_pattern = re.compile(r'TATA[AT]A[AT]')#define a regular expression pattern to match TATAWAW
    gene_name = re.compile(r'^>.*?gene:(\S+) ')

    #iterate through each line in the file to get the gene name and sequence
    for line in input:
        #check gene name line
        if gene_name.search(line):
            #if the current gene and sequence are not empty
            if current_gene and current_sequence:
                #join the sequence lines
                full_sequence = ''.join(line.strip() for line in current_sequence)

                #check if the sequence includes TATAWAW
                if tata_pattern.search(full_sequence):
                    #write the sequence to the output file
                    output.write(f'>{current_gene[0]}\n')
                    output.writelines(current_sequence)         

            current_gene = gene_name.findall(line) #extract the gene name
            current_sequence = [] #clear the previous sequence

        else:
            current_sequence.append(line)  #add the sequence line to the current sequence list

    #write the last gene and sequence to the output file
    if current_gene and current_sequence:
        #join the sequence lines
        full_sequence = ''.join(line.strip() for line in current_sequence)

        if tata_pattern.search(full_sequence):
            output.write(f'>{current_gene[0]}\n')
            output.writelines(current_sequence)

    else:
        current_sequence.append(line)
        
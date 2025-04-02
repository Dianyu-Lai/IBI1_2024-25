import re
filename=input('one	of three possible splice donor/acceptor combination (GTAG,GCAG,ATAC)')
input=open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa','r')#open the file
output=open(f'{filename}_spliced_genes.fa','w')#create a new file to write the output
current_gene=None#initialize a variable to store the current gene name
current_sequence=[]#initialize an empty list to store the current sequence
for line in input: #iterate through each line in the file
    if re.search(r'^>\w+mRNA',line):#check gene name line
        if current_gene and current_sequence:#if the current gene and sequence are not empty
            full_sequence=''.join(line.strip() for line in current_sequence)#join the sequence lines
            if re.search(r'TAT[AT]A[AT]',full_sequence):#check if the sequence includes TATWAW
                output.write(current_gene[0])
                output.write('\n')
                output.write(full_sequence)
        current_gene=re.findall(r'(>\w+)_mRNA',line)#extract the gene name
        current_sequence=[]
    else:#for seqenece line
        current_sequence.append(line)   #delete the enter
input.close()#close the input file
output.close()#close the output file
import re

splice_combinations = ['GTAG','GCAG','ATAC']
splice_input = input(f'enter splice combination in {splice_combinations[:]}').strip().upper()

#check if the input is valid
while splice_input not in splice_combinations:
    print('invalid input. try again')
    splice_input = input(f'enter splice combination in {splice_combinations[:]}').strip().upper()

output_filename = f'{splice_input}_spliced_genes.fa'

with open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa', 'r') as infile, open(output_filename, 'w') as outfile:

    #initialize lists to store the current gene name and seq
    current_gene = []
    current_sequence = []

    #define 3 regular expression patterns
    tata_pattern = re.compile(r'TATA[AT]A[AT]')
    gene_name = re.compile(r'^>.*?gene:(\S+) ')
    splice_pattern = re.compile(fr'{splice_input[:2]}.*?{splice_input[-2:]}')

    for line in infile: #iterate through each line in the file
        if gene_name.search(line):#check gene name line
            if current_gene and current_sequence:#if the current gene and sequence are not empty
                full_sequence = ''.join(seq.strip() for seq in current_sequence)#join the sequence lines
                if splice_pattern.search(full_sequence):#check if the sequence includes splice signal
                    splice_seq=splice_pattern.findall(full_sequence)
                    tata_box_number = 0
                    for i in splice_seq:
                        if tata_pattern.search(i):#check if the spliced sequence includes TATAWAW
                            tata_box_seq = tata_pattern.findall(i)
                            tata_box_number = len(tata_box_seq)
                            outfile.write(f'\n>{current_gene[0]}, the number of instances of TATA box is {tata_box_number} \n')
                            outfile.write(full_sequence)#write the sequence to the output file                       
            current_gene = gene_name.findall(line)#extract the gene name
            current_sequence = []

        else:#for sequence lines
            current_sequence.append(line)  #add the sequence line to the current sequence list

    #write the last gene and sequence to the output file
    if current_gene and current_sequence:#if the current gene and sequence are not empty
        full_sequence = ''.join(line.strip() for line in current_sequence)#join the sequence lines
        if splice_pattern.search(full_sequence):#check if the sequence includes TATWAW
            splice_seq = splice_pattern.findall(full_sequence)
            for i in splice_seq:
                if tata_pattern.search(i):#check if the spliced sequence includes TATWAW
                    tata_box_seq = tata_pattern.findall(i)
                    tata_box_number = len(tata_box_seq)
                    outfile.write(f'\n>{current_gene[0]}, the number of instances of TATA box is {tata_box_number} \n')
                    outfile.writelines(full_sequence)

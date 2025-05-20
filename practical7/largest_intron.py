import re   #import library
seq = 'ATGCAAGTGGTGTGTCTGTTCTGAGAGGGCCTAA' #the sequence
intron = re.findall(r'GT.*？AG',seq)#find the largest intron
# if any introns found, find the longest one
if introns:
    longest_intron = max(introns, key=len)
    print("The largest intron is:", longest_intron)
    print("Length:", len(longest_intron))
else:
    print("No intron found.")

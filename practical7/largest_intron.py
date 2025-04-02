import re   #import library
seq = 'ATGCAAGTGGTGTGTCTGTTCTGAGAGGGCCTAA' #the sequence
intron=re.findall(r'GT.+AG',seq)#find the largest intron
print(intron)
length=len(intron[0])#transform it into string
print(length)#calculate the len

import os

FileNameLeft= "BHL_4517_8T_Folmer_S11_L001_R1_001.fastq"

FileNameRight = "BHL_4517_8T_Folmer_S11_L001_R2_001.fastq"

def complement(seq):
    complement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A','N':'N'}
    bases = list(seq)
    bases = [complement[base] for base in bases]
    return ''.join(bases)

def reverse_complement(s):
    return complement(s[::-1])

f=open(FileNameLeft)
w=open(FileNameLeft+'.combined.fasta', 'a')
d=open(FileNameRight)
lines1 = [line.rstrip('\n') for line in f]
lines2 = [line.rstrip('\n') for line in d]

i=0
while (i<len(lines1)):
	if(lines1[i][0:45]==lines2[i][0:45]):
		w.write(lines1[i]+os.linesep)
		w.write(lines1[i+1]+reverse_complement(lines2[i+1])+os.linesep)
	i=i+4
f.close()
w.close()
d.close()
print("Paired end combination Finished!")


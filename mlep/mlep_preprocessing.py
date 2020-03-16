import os

FileNameLeft= "3BHL22317_mlep_S89_L001_R1_001.fastq"

FileNameRight = "3BHL22317_mlep_S89_L001_R2_001.fastq"


# merge pair-end reads using FLASh 1.2.11
os.system("../FLASH-master/flash "+FileNameLeft+" "+FileNameRight+" -o "+FileNameLeft)
MergedFileName = FileNameLeft + ".extendedFrags.fastq";

# convert fastq file to fasta file using seqtk
ConvertedFileName=MergedFileName+".fasta"
os.system("../seqtk-master/seqtk seq -a "+MergedFileName+" > "+ConvertedFileName)

# cluster sequences using cd-hit-est
os.system('../cdhit-master/cd-hit-est -i '+ConvertedFileName+' -o '+ConvertedFileName+'.cluster'+' -c 0.97 -d 75 -sc 1 -sf 1 -T 0' )

# select DNA clusters with at least 4 sequences for blast
MinCluster=4

class dna:
	def __init__(self,description,seq):
		self.description=description
		self.seq=seq
		

cluster=0
sequence=0

SelectedClusterFileName=ConvertedFileName+".cluster"

f=open(SelectedClusterFileName+".clstr")
f1=open(SelectedClusterFileName)
w=open(SelectedClusterFileName+'.selected','w')   # clusters with >=4 sequences will be put into this file
w1=open(SelectedClusterFileName+'.notSeleted','w') # clusters with <4 sequences will be put into this file
w2=open(SelectedClusterFileName+'.abnormal','w')   # clusters with abnormal records will be put into this file
#lines=f.readlines()
lines1 = f1.readlines()
	
dict={}
for i in range(len(lines1)):
	if (i%2==0):
		temp=dna(lines1[i][:-1].replace(' ','_'),lines1[i+1][:-1])
		dict[lines1[i][:-25]]=temp	

for line in f:
	if (line[0]=='>'):
		if (sequence>=MinCluster):
			if (rep[0]=='>'):
				w.write(dict[rep].description+'_'+str(sequence)+'\n')
				w.write(dict[rep].seq+'\n')
			else:
				print(rep,sequence)
				w2.write(rep+'_'+str(sequence)+'\n')
		elif (sequence>0):
			if (rep[0]=='>'):
				w1.write(dict[rep].description+'_'+str(sequence)+'\n')
				w1.write(dict[rep].seq+'\n')
			else:
				print(rep,sequence)
				w2.write(rep+'_'+str(sequence)+'\n')
		cluster=cluster+1
		sequence=0
	else:
		sequence=sequence+1
	if (line[len(line)-2]=='*'):
		rep=line[line.find('>'):-6]


f.close()
f1.close()
w.close()
w1.close() 
w2.close()

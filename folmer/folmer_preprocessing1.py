import os

FileNameLeft= "BHL_4517_8T_Folmer_S11_L001_R1_001.fastq"

FileNameRight = "BHL_4517_8T_Folmer_S11_L001_R2_001.fastq"

ConvertedFileName=FileNameLeft+".combined.fasta"
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

fs=open(SelectedClusterFileName+".clstr")
fs1=open(SelectedClusterFileName)
ws=open(SelectedClusterFileName+'.selected','w')   # clusters with >=4 sequences will be put into this file
ws1=open(SelectedClusterFileName+'.notSeleted','w') # clusters with <4 sequences will be put into this file
ws2=open(SelectedClusterFileName+'.abnormal','w')   # clusters with abnormal records will be put into this file

lines1 = fs1.readlines()
	
dict={}

for i in range(len(lines1)):
	if (i%2==0):
		temp=dna(lines1[i][:-1].replace('@','>').replace(' ','_'),lines1[i+1][:-1])
		dict[lines1[i][:-25].replace('@','>')]=temp	
for line in fs:
	if (line[0]=='>'):
		if (sequence>=MinCluster):
			if (rep[0]=='>'):
				ws.write(dict[rep].description+'_'+str(sequence)+'\n')
				ws.write(dict[rep].seq+'\n')
			else:
				print(rep,sequence)
				ws2.write(rep+'_'+str(sequence)+'\n')
		elif (sequence>0):
			if (rep[0]=='>'):
				ws1.write(dict[rep].description+'_'+str(sequence)+'\n')
				ws1.write(dict[rep].seq+'\n')
			else:
				print(rep,sequence)
				ws2.write(rep+'_'+str(sequence)+'\n')
		cluster=cluster+1
		sequence=0
	else:
		sequence=sequence+1
	if (line[len(line)-2]=='*'):
		rep=line[line.find('>'):-6]


fs.close()
fs1.close()
ws.close()
ws1.close() 
ws2.close()

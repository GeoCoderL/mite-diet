fileName="BHL_4517_8T_Folmer_S11_L001_R1_001.fastq.combined.fasta.cluster.clstr.selected.blastResult"   # name of the file t 

filterTxt="Lebertia";  # filter out the blast results with species as 'Lebertia'

f=open(fileName)    #open a file for reading (delete the CR at the end of line)
w=open(fileName+'.frequencyResult.csv','w') # open a file with adding afterfix to write the results



lines = f.readlines()
temp=''
totalNumOfSequence=0	
others=0

for i in range(0,len(lines)-1):
	results1=lines[i].split(',')
	results2=lines[i+1].split(',')
	if (results1[0]==results2[0] and results1[1]==results2[1] and temp!=results1[0]):
		temp=results1[0]
		l=int(results1[4])+int(results2[4])
		c=int(results1[7])+int(results2[7])
		p=round((float(results1[5])*float(results1[4])+float(results2[5])*float(results2[4]))/(float(results1[4])+float(results2[4])),1)
		if (c>50 and p>80 and results1[2].find(filterTxt)<0):			
			totalNumOfSequence=totalNumOfSequence+float(results1[0].split('_')[2])                        
if (totalNumOfSequence==0):
	print("no useful data in this file!")
	w.write("no useful data!\n")
else:
	print("normal data file")


for i in range(0,len(lines)-1):
	results1=lines[i].split(',')
	results2=lines[i+1].split(',')
	if (results1[0]==results2[0] and results1[1]==results2[1] and temp!=results1[0]):
		temp=results1[0]
		l=int(results1[4])+int(results2[4])
		c=int(results1[7])+int(results2[7])
		p=round((float(results1[5])*float(results1[4])+float(results2[5])*float(results2[4]))/(float(results1[4])+float(results2[4])),1)
		if (c>50 and p>80 and results1[2].find(filterTxt)<0):
			if (float(results1[0].split('_')[2])/totalNumOfSequence>=0.001):
				w.write(results1[0].split('_')[2]+','+results1[2]+'_'+results1[4]+'_'+str(round(float(results1[5]),1))+'_'+results1[7]+','+ str(float(results1[0].split('_')[2])/totalNumOfSequence) +'\n')                                         
			else:
				others=others+int(results1[0].split('_')[2])

w.write(str(others)+','+'Others'+','+str(others/totalNumOfSequence));
w.write("\n\n");



for i in range(0,len(lines)-1):
	results1=lines[i].split(',')
	results2=lines[i+1].split(',')
	if (results1[0]==results2[0] and results1[1]==results2[1] and temp!=results1[0]):
		temp=results1[0]
		l=int(results1[4])+int(results2[4])
		c=int(results1[7])+int(results2[7])
		p=round((float(results1[5])*float(results1[4])+float(results2[5])*float(results2[4]))/(float(results1[4])+float(results2[4])),1)
		if (c>100 or p>100):
			print('data error:'+line,lines[i],lines[i+1],'/n')
		if (c>50 and p>80 and results1[2].find(filterTxt)<0):
			if (float(results1[0].split('_')[2])/totalNumOfSequence<0.001):
				print("others:"+results1[0]+results1[2])
				w.write(results1[0].split('_')[2]+','+results1[2]+'_'+results1[4]+'_'+str(round(float(results1[5]),1))+'_'+results1[7]+','+str(float(results1[0].split('_')[2])/totalNumOfSequence)   +'\n')

f.close()
w.close()


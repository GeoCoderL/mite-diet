fileName="3BHL22317_mlep_S89_L001_R1_001.fastq.extendedFrags.fasta.cluster.selected.blastResult"   # name of the file t 

f=open(fileName)    #open a file for reading (delete the CR at the end of line)
w=open(fileName+'.frequencyResult.csv','w') # open a file with adding afterfix to write the results
lines = f.readlines()
temp='';
totalNumOfSequence=0
others=0
for i in range(0,len(lines)-1):
	results1=lines[i].split(',')   # split a long string to an array of small strings using comma
	results2=lines[i+1].split(',')
	if (results1[0]==results2[0] and temp!=results1[0]):   # blast results will have top 5 matches for each DNA, this line of code detect the end of each piece of DNA
		temp=results1[0]
		totalNumOfSequence=totalNumOfSequence+float(results1[0].split('_')[2])
        
for i in range(0,len(lines)-1):
	results1=lines[i].split(',')   # split a long string to an array of small strings using comma
	results2=lines[i+1].split(',')
	if (results1[0]==results2[0] and temp!=results1[0]):   # blast results will have top 5 matches for each DNA, this line of code detect the end of each piece of DNA
		temp=results1[0]
		if (float(results1[7])>50 and float(results1[5])>80):
			if (float(results1[0].split('_')[2])/totalNumOfSequence>=0.001):
				w.write(results1[0].split('_')[2]+','+results1[2]+'_'+results1[4]+'_'+str(round(float(results1[5]),1))+'_'+results1[7]+','+ str(float(results1[0].split('_')[2])/totalNumOfSequence) +'\n') # results1[0] split with '_' to get the freqency  
			else:
                        	others=others+int(results1[0].split('_')[2])
w.write(str(others)+','+'Others'+','+str(others/totalNumOfSequence));
w.write("\n\n");

for i in range(0,len(lines)-1):
	results1=lines[i].split(',')   # split a long string to an array of small strings using comma
	results2=lines[i+1].split(',')
	if (results1[0]==results2[0] and temp!=results1[0]):   # blast results will have top 5 matches for each DNA, this line of code detect the end of each piece of DNA
		temp=results1[0]
	if (float(results1[7])>50 and float(results1[5])>80):
		if (float(results1[0].split('_')[2])/totalNumOfSequence<0.001):
			w.write(results1[0].split('_')[2]+','+results1[2]+'_'+results1[4]+'_'+str(round(float(results1[5]),1))+'_'+results1[7]+','+str(float(results1[0].split('_')[2])/totalNumOfSequence)   +'\n') # results1[0] split with '_'$
f.close()
w.close()

# mite-diet
DNA analysis code for water mite diet project

There are two folders: folmer and mlep. Each folder contains the scripts and sample date files.

# How to run the scripts:
1. Build the FLASh, seqtk, CD-HIT tools
./cdhit-master/make 
./seqtk-master/make
./FLASH-master/make

2. Run blast preprocessing scripts  
For mlep datasets:
# merge paired end reads, cluster similar sequences, select interesting sequences for blast 
python ./mlep/mlep-preprocessing.py 
 

For folmer datasets:
# stitch paired end reads
python ./folmer/folmer-preprocessing1.py  
# cluster similar sequences and select intersting sequences for blast
python ./folmer/folmer-preprocessing2.py  

3. Run blast 
blastn -task blastn -db {blast database folder} -query {DNA datafile} -num_alignments 5 -outfmt "10 qseqid sseqid sscinames evalue length pident qcovs qcovhsp qseq sseq" -out {blast result filename}

4. Run blast postprocessing script
# filter blast results and output summary data in CSV files
For mlep datasets:
python ./mlep/mlep-postprocessing.py  
For folmer datasets:
python ./folmer/folmer-postprocessing1.py




#!/usr/bin/python

import sys
import matplotlib.pyplot as plt
import os
import glob
import re

#Open input file
input_file = open(sys.argv[1],"rt")

occ = {} #Declare empty dictionary for the trimmers

count = 1 #Declare counter for the name of the output files

#Read FASTA/FASTQ records and split into files of a single record
while True:
    tag = input_file.readline() #Read TAG or end-of-file
    if not tag: break
    sequence = input_file.readline().rstrip('\n')  # Read sequence
    for i in range(len(sequence)-2): #Traverse sequence (3-mers)
        kmer = sequence[i:i+3]
        if kmer not in occ: occ[kmer] = 0
        occ[kmer] += 1
    output_name = sys.argv[1] + ".part." + str(count) #Open an output file for each sequence
    output_file = open(output_name,"wt")
    output_file.write(tag + sequence + "\n")
    if tag[0] == "@":    #If it is a FASTQ file
        input_file.readline()
        #Save the quality line
        qual = input_file.readline().rstrip('\n')
        output_file.write("+\n%s\n" % qual)
    count += 1  #Add to the counter

#Reopen the generated files to trim the sequences
os.chdir("./")
for file in glob.glob("*.part.*"):
    original_file = open(file, "rt")
    tag = original_file.readline().rstrip('\n')
    if not tag: break
    sequence = original_file.readline().rstrip('\n')
    trimmed_file = open(file, "wt")
    trimmed_file.write("%s\n%s" % (tag,sequence[:-20])) #Rewrite the file with the trimmed sequence
    if tag[0] == "@":
        original_file.readline()
        qual = original_file.readline().rstrip('\n')
        trimmed_file.write("\n+\n%s"% qual[:-20])
    original_file.close()
    trimmed_file.close()
        
#Open a stats file and save the trimmer frequencies
output_file = open(sys.argv[1] + ".stats","wt")
output_file.write(str(occ))

input_file.close()  #Close files
output_file.close()

#Represent a histogram with the frequencies of the trimers
plt.bar(range(len(occ)), list(occ.values()), align='center')
plt.xticks(range(len(occ)), list(occ.keys()))
#Save histogram as a png file
plt.savefig("trimer_frequencies.png")

#Download the Saccharomyces cerevisiae genome
os.system("wget --timestamping ftp://hgdownload.cse.ucsc.edu/goldenPath/sacCer3/chromosomes/*")
#Unzip the chromosome files
os.system("gunzip *fa.gz")
#Join the chromosome files into a single file
os.system("cat *fa >> wg.fa")
#Delete the chromosome files
os.system("rm chr*")
#Create an index for the sc genome
os.system("bwa index -p scgenome -a bwtsw wg.fa")

#For every file, create a sam file obtained from the BWA alignment
os.chdir("./")
for file in glob.glob("*.part.*"):
    os.system("bwa mem %s %s > %s"%('scgenome', file, file+".txt.sam"))

#Open empty file which will have the merged sam records
merged_samfile=open("merged.txt.sam", "wt")

#Find all sam files in a directory created from the splitted files
os.chdir("./") #replace by directory where the SAM files were created
for sam in glob.glob("*part.*.sam"):
    file=open(sam,"rt")
    while True:
        line=file.readline()
        if not line: break
        if line[0]!="@":   #Ignoring the headers
            merged_samfile.write(line)  #Merge them into a single file

merged_samfile.close()
file.close()



merged_list=[] #Open an empty list of lists
merged_list_stars=[] #Open an empty list for the not aligned sequences

#Index each element of the record by columns
splitted_sam=open("merged.txt.sam","rt")
for sequence in splitted_sam:  #Traverse each sequence record in the merged sam file
    split_sequence=sequence.split("\t")   #Add each element between tabs in each sequence to a list
    if split_sequence[2]=="*" or split_sequence[3]=="*":
        merged_list_stars.append(split_sequence)  #Append to a list the sequences that have a * on the crh or position
    else: #Substitute the roman numbers of the chromosomes if necessary
        match=re.search(r'(V|I|X)',split_sequence[2])
        if match:
            #Create a dictionary for the roman numbers
            roman={"chrXVI": "chr16", "chrXV": "chr15", "chrXIV": "chr14", "chrXIII": "chr13", "chrXII": "chr12", "chrXI": "chr11", "chrX": "chr10", "chrIX": "chr9", "chrVIII": "chr8", "chrVII": "chr7", "chrVI": "chr6", "chrV": "chr5", "chrIV": "chr4", "chrIII": "chr3", "chrII": "chr2", "chrI": "chr1"}
            for key in roman:
                if split_sequence[2]==key:
                    split_sequence[2]=roman[key]
        merged_list.append(split_sequence)

#Sort first by chromosome and then by position 
s=sorted(merged_list, key=lambda i: (int(i[2][3:]),int(i[3]))) #Sort complete sequences

#Write into a file the sorted lines of the sam file and the not aligned (merged_list_stars) lines
with open ('mergedsorted.txt.sam','w') as file:
    file.writelines('\t'.join(i) for i in s)
    file.writelines('\t'.join(i) for i in merged_list_stars)

file.close()

print("%s reads have been aligned"%len(s))  #Compute how many reads have been aligned

#Remove generated files
os.system("rm *fa")

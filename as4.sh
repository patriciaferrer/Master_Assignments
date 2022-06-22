#!/bin/bash

#Names: Aintzane Rueda and Patricia Ferrer

FILE=$1  #Save the input file into a variable

#Calculate the trimers' frequencies
if [[ $(grep "^>" $FILE) ]]  #If it is a FASTA file
then
  grep -v "^>" $FILE | tr -d '\n' | fold -w 3 > trimers.1.txt
  grep -v "^>" $FILE | fold -w 1 | tail -n +2 | tr -d '\n' | fold -w 3 > trimers.2.txt
  grep -v "^>" $FILE | fold -w 1 | tail -n +3 | tr -d '\n' | fold -w 3 > trimers.3.txt
else  #If it is a FASTQ file
  sed -n '/^@/{n;p;}' $FILE | fold -w 3 | tr -d '\n' > trimers.1.txt
  sed -n '/^@/{n;p;}' $FILE | fold -w 1 | tail -n +2 | tr -d '\n' | fold -w 3 > trimers.2.txt
  sed -n '/^@/{n;p;}' $FILE | fold -w 1 | tail -n +3 | tr -d '\n' | fold -w 3 > trimers.3.txt
fi

#Add a newline so that trimers from different files dont join
printf "\n" >> trimers.1.txt
printf "\n" >> trimers.2.txt
printf "\n" >> trimers.3.txt

#Write the trimer frequencies into a file, avoiding the kmers that are smaller than 3
cat trimers.* |  grep -E '^.{3}$' | sort | uniq -c > stats2

#Remove generated files
rm *trimers* 

#Represent a histogram of the frequencies
cat $FILE.stats | awk '{$1=sprintf("%-*s", $1, ""); gsub(" ", "=", $1); printf("%-10s%s\n", $2, $1)}'

#Split the file into a file with only one sequence
if [[ $(grep "^>" $FILE) ]]
then
  split -d -l2 $FILE $FILE.part.
else
  split -d -l4 $FILE $FILE.part.
fi

#Hard trim the sequences from the rigth and rewrite the files
for X in $FILE.part.*
do
  if [[ $(grep "^>" $FILE) ]]
  then
    awk 'NR%2 == 1 {print} NR%2 == 0 {print substr($1,1,length($1)-20)}' $X > temporal.txt
    mv temporal.txt $X
  else
    awk 'NR%4 == 1 {print} NR%4 == 2 {print substr($1,1,length($1)-20)} NR%4 == 3 {print} NR%4 == 0 {print substr($1,1,length($1)-20)}' $X > temporal.txt
    mv temporal.txt $X
  fi
done

#Downloading the SC genome
wget --timestamping 'ftp://hgdownload.cse.ucsc.edu/goldenPath/sacCer3/chromosomes/*'

#Unzipping the files
gunzip *.fa.gz

#Concatenating the chromosome files into a single file
cat *.fa > wg.fa
rm chr*
    
#Indexing
bwa index -p scgenome -a bwtsw wg.fa

#Aligning to SC genome and generating a sam file
for Y in $FILE.part.*
do
    #bwa aln -t 4 "scgenome" $Y >  $Y.txt.bwa
    #bwa samse "scgenome" $Y.txt.bwa $Y > $Y.txt.sam
    bwa mem "scgenome" $Y > $Y.txt.sam
done


#Merges the sam files ignoring headers
cat *txt.sam | grep -v "^@" >> mergedtemp.txt.sam

#Replaces roman numbers (if necessary)
if ! [[ $(cut -f 3 mergedtemp.txt.sam | grep [0-9]) ]]
then
    sed -e 's/chrXVI/chr16/' -e 's/chrXV/chr15/' -e 's/chrXIV/chr14/' -e 's/chrXIII/chr13/' -e 's/chrXII/chr12/'   \
    -e 's/chrXI/chr11/' -e 's/chrX/chr10/' -e 's/chrIX/chr9/' -e 's/chrVIII/chr8/' -e 's/chrVII/chr7/'  \
    -e 's/chrVI/chr6/' -e 's/chrV/chr5/' -e 's/chrIV/chr4/' -e 's/chrIII/chr3/' -e 's/chrII/chr2/' \
    -e 's/chrI/chr1/' mergedtemp.txt.sam > merged.txt.sam
fi

#Remove temporal file
rm mergedtemp.txt.sam

#Sorts the aligned lines by chromosome and position 
cat merged.txt.sam | awk '$3!="*" {print}' | sort -n -k4 | sort -srn -k3.5 | tac > mergedsorted.txt.sam
#Calculates the number of aligned reads
NUM=$(cat mergedsorted.txt.sam | wc -l)
#Add the unmapped sequences
cat merged.txt.sam | awk '$3=="*" {print}' >> mergedsorted.txt.sam

echo $NUM reads have been aligned




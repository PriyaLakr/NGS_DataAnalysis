#!/usr/bin/bash

echo -e "======Give name of your experiment as first argument, path of input files as second argument, path of ouput folder as third argument, number of threads as fourth argument ====== \nRun -> bash mafft.sh filename inpath outpath" 

name=$1
in_data=$2
out="$3/${name}_out"

cd $in_data 
mkdir $out

echo -e "changed dir to ${in_data} input directory"

for i in *.faa; do mafft  --auto --leavegappyregion --thread $4 ${i} > $out/${i}_aligned.fasta; done

## parallel: 

#parallel -j 2 'mafft --quiet --auto {} > {.}.fasta':::*.fasta


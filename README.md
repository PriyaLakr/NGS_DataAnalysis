# DataAnalysis
Some scripts to make your bioinformatics analyses a bit easy! 🤓

# bulk_mafft.sh
Script to perform bulk multiple sequence analysis using mafft by using this one simple command. Dependency: [mafft](https://mafft.cbrc.jp/alignment/software/source.html)
                    
   `bash bulk_mafft.sh [experiment_name] [inpath] [outpath] [threads]`

# pl_count_length.py
Script for counting the total length of sequences in a FASTA file. This script will read all FASTA files in a directory specified by the user, and print the total sequence length of each FASTA file. The user needs to provide the path of the directory where all FASTA files are located. This input path is specified with `--path` flag.
   
   `python pl_count_length.py --path`


# DataAnalysis

Scripts to make your bioinformatics analyses a bit easy 🤓 and reproducible 🤓

Best practices:     1. Keep your input files and scripts for one analysis in one folder \n
                    2. Always modify your $PATH environment variable to include all the dependencies required for the analysis

# Dependencies 

| Software | version tested |
| -------- | -------------- |
| [mafft](https://mafft.cbrc.jp/alignment/software/source.html)  |   v7.475       |
| [bowtie2](http://bowtie-bio.sourceforge.net/bowtie2/index.shtml) | v2.3.5.1    |
| [samtools](http://www.htslib.org) | v1.9 |
| python | 3.7.6 |


# bulk_mafft.sh
Script to perform bulk multiple sequence analysis using mafft by using this one simple command. Dependency: [mafft](https://mafft.cbrc.jp/alignment/software/source.html)
                    
   `bash bulk_mafft.sh [experiment_name] [inpath] [outpath] [threads]`

# pl_count_length.py
Script for counting the total length of sequences in a FASTA file. This script will read all FASTA files in a directory specified by the user, and print the total sequence length of each FASTA file. The user needs to provide the path of the directory where all FASTA files are located. This input path is specified with `--path`.
   
   `python pl_count_length.py --path`
   
# pl_NGS_process.sh
This is a great script to perform multiple steps during NGS analysis with single command line script!

It can 1) extract unaligned reads from bam files
       2) align reads using bowtie2 
       3) process post-alignment sam files and produce idx stats 
    
    bash pl_NGS_process.sh [options]
    
    # Usage: -i input_dir  -f filetype  -d out_dir_path  -l indexlocation -t number_of_threads  -x index_file_name  -r bowtie2_run_mode. -e extractreads -a alignreads -p process_reads
    
    








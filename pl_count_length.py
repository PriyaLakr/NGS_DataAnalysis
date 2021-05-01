import os
import argparse 


# count the length of all fasta sequences in a file
def count_length(file_path):
	from Bio import SeqIO
	with open(file_path, 'r') as f:
		f.seek(0)

		total_len = 0

		for record in SeqIO.parse(f, "fasta"):
			read_len = len(record.seq)
			total_len = total_len + read_len

	print(f"Total sequence length: {total_len}   File: {file}")


if __name__ == "__main__":
	# initialize your parser
	parser = argparse.ArgumentParser(description = "This script counts total length of sequences in a fasta file")   

	# parse the arguments
	parser.add_argument("--path", type=str, help="Path of the directory where files are stored")
	args = parser.parse_args()

	path = args.path

	os.chdir(path) 

	# iterate through all files in the directory
	for file in os.listdir(): 
	    # Check whether file is in correct format or not 
		if file.endswith(".fna") or file.endswith(".fasta"): 
			file_path = f"{path}/{file}"
  
	    	# call count_length function 
			count_length(file_path) 











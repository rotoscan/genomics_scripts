# this script takes three inputs files, on this order.
#		       1) list of ids that you DON'T want to have on your output
#		       2) multi-fasta file
#		       3) output file with selected fasta
# example: $ python ~/extract_fa_from_id.py <ids_of_interest.txt> <multi_fasta_file.fa> <output_file.fa>
# Rodolfo Toscan/rodolfo.toscan@ufz.de
import os
import sys
from itertools import groupby
def get_ids(id_file):

	# get ids from id_file and put into dictionary
	# return dic
	l="a"
	f=open(id_file,"r")
	ids = f.readlines()
	dic = {}
	for id in ids:
		dic[id.strip()]=""
	f.close()
	return dic

def extract_fa(id_dic,fa_in,fa_out,type):
	# given the id dic and the fasta file, extracts the desired fasta seqs
	l="a"
	fout = open(fa_out,"w")
	dic = {}
	if type == 1:
		f=open(fa_in) # opens fasta 
		# ditch the boolean (x[0]) and just keep the header or sequence 
		# we know they 
		f_iterator = (x[1] for x in groupby(f, lambda line: line[0] == ">"))
		for header in f_iterator:
			header = header.next()[1:].strip()		   # drop the ">"   # <-- optional
			seq = "".join(s.strip() for s in f_iterator.next())  # join all sequence lines to one.
			seq = str(seq)				       # cast sequence to string  #  
			#header = str(header)				 # cast header to string    #  for troubleshooting purpose
			if header in id_dic:
				fout.write(">"+header+"\n")
				fout.write(seq+"\n")

		f.close()

	else:
		f=open(fa_in,"r")
		l="a"
		while True:
			l=f.readline()
			if not l:break
			else:
				if ">" in l:
					header = l.strip()
					seq = f.readline().strip()
					if header not in id_dic:
						fout.write(header+"\n")
						fout.write(seq+"\n")
	f.close()
	fout.close()
def check_type(fa_in):
	c = 0
	list = []
	f=open(fa_in,"r")
	l="a"
	while True:
		l=f.readline()
		if not l:break
		else:
			if ">" in l:
				list.append(l)
				c = c +1
				if c == 5: break
	if ">" in list[0]:
		if ">" in list[2]:
			f.close()
			return 2	# if first and third lines have headers, this is a long line multi-fasta file
		else:
			f.close()
			return 1	# else, its a "broken" line fasta file
	


def main(id_file,fa_in,fa_out):
	# check what type of multi fasta file you have: long line or broken line
	type = check_type(fa_in)	
	#print type
	# extract dictionary
	id_dic = get_ids(id_file)
	#print id_dic
	# dumps to the outputfile
	extract_fa(id_dic,fa_in,fa_out,type)


# get inputs from user keyboard
id_file,fa_in,fa_out = sys.argv[1], sys.argv[2], sys.argv[3]
main(id_file,fa_in,fa_out)

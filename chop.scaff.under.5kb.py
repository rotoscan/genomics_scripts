
################### script for chopping contigs/scaffolds smaller than 5000kb #############################################
import os
import sys
from itertools import groupby
def filt_5kb(input_fasta,output_fasta):
  #fin = open(input_fasta,"r")
  #fout = open(input_fasta.replace(input_fasta.split("/")[-1],"filt_5kb_"+input_fasta.split("/")[-1]),"w")
  fout = open(output_fasta,"w")
  fin = open(input_fasta)
  faiter = (x[1] for x in groupby(fin, lambda line: line[0] == ">"))
  for header in faiter:
    # drop the ">"
    header = header.next()[1:].strip()
    # join all sequence lines to one.
    seq = "".join(s.strip() for s in faiter.next())
    #header = str(">"+header)
    seq = str(seq)
    seqlen = len(seq)
    if seqlen >= 5000:
      fout.write(">"+header+"\n")
      fout.write(seq+"\n")
filt_5kb(sys.argv[1],sys.argv[2])
# first input is the assembly to be chopped, second input is the outputted file

import os
import sys
import random


def rarefy (lib,size):
        f = open(lib,"r")
	size = int(size)
        dic = {}
        copydic = {}
	c = 0
        l="a"
        print "building dictionary..."
        while True:
                l = f.readline()
                if not l: break
                else:
                        #if l[0] == "@" and "SN1035" in l:			# * for fastq files
                        if ">" in l: #l[0] == "@" and "SN1035" in l:
                                seq = f.readline()
                                #plus = f.readline()				# *
                                #q = f.readline()				# *
                                #dic[c]  = [l,seq,plus,q]
                                dic[c]  = [l,seq]
                                #copydic[c] = ""
				c = c +1

	print "dictionary built!"
	f.close()
	print "doing sampling..."
	sampkeys = random.sample(list(dic), int(size))
	print "Done with sampling."
	ext = lib.split(".")[-1]
	fout = open(lib.replace(ext,"samp."+str(size)+"."+ext),"w")
	for item in sampkeys:
		info = dic[item]
		fout.write(str(info[0]))
                fout.write(str(info[1]))		
                #fout.write(str(info[2]))					# *
                #fout.write(str(info[3]))					# *
	print "DONE!"
	print "check",lib.replace(ext,"samp."+str(size)+"."+ext)		

	fout.close()

lib = sys.argv[1]
size = sys.argv[2]


rarefy (lib,size)

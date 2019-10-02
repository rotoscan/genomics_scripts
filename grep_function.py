def grep(file,query):
	l="a"
	f=open(file,"r")
	while True:
		l=f.readline()
		if not l: break
		else:
			if query in l:
				f.close()
				return l
	f.close()
	return '0'

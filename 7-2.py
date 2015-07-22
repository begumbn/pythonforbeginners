# reads mbox-short.txt, identifies dspam confidence, converts into integers and calculates average

add = 0
count = 0

fname = raw_input("Enter file name: ")
fh = open(fname)
for line in fh:
	if line.startswith("X-DSPAM-Confidence:") :      
		line = line.rstrip()
		val = line[20:]
		val = float(val)
		count = count + 1
		add = add + val
        
print 'Average spam confidence:', add/count

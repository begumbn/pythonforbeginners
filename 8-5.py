# counts lines with sender email addresses

fname = raw_input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"
fh = open(fname)
lst = list()
count = 0

for line in fh :
    line = line.rstrip()
    if not line.startswith('From ') : continue
    words = line.split()
    words = words[1]
    lst.append(words)
    print words

for i in lst :
    count = count + 1

print "There were", count, "lines in the file with From as the first word"

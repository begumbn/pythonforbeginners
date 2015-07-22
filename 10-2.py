#counts the hours emails were sent and sorts by hour

name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
counts=dict()

for line in handle :
    line = line.rstrip()
    if not line.startswith('From ') : continue
    words = line.split()
    words = words[5]
    words = words[:2]  
    counts[words] = counts.get(words, 0) + 1

lst = list()
for t, c in counts.items() :
    lst.append( (t, c) )
    
lst.sort()

for t,c in lst :
    print t,c

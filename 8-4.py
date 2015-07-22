#reads text romeo.txt, splits lines into list of unique words

fname = raw_input("Enter file name: ")
fh = open(fname)
list1 = list()
for line in fh:
	list1= list1 + line.split()
    
list2 = list()
for word in list1 :
	if word not in list2 :
    	list2.append(word)

list2.sort()
print list2

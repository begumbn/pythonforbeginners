# figures out who sent the greatest number of email messages

name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
counts = dict()
bigcount = None
bigmail = None

for line in handle :
    line = line.rstrip()
    if not line.startswith('From ') : continue
    words = line.split()
    words = words[1]
    counts[words]=counts.get(words,0) + 1

for word, count in counts.items() :
    if bigcount == None or count>bigcount:
        bigmail = word
        bigcount = count

print bigmail, bigcount

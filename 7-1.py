# opens and reads words.txt and prints all in uppercase

fname = raw_input("Enter file name: ")
fh = open(fname)
inp = fh.read()
inp = inp.rstrip()
up = inp.upper()
print up

# exam grading

input = raw_input()
input = float(input)

if input<0.0 and input>1.0 :
    print "Error"
elif input>=0.9 :
	print "A"
elif input>=0.8 :
    print "B"
elif input>=0.7 :
    print "C"
elif input>=0.6 :
    print "D"
else :
    print "F"

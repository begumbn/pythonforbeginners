# calculate pay with build-in function

hrs = raw_input("Enter Hours:")
h = float(hrs)
rate= raw_input("Enter Rate:")
r = float(rate)

def computepay(h,r):
    if h<40 :
		computepay = h*r 
    else :
    	computepay = (40 * r) + ((h%40) * (r*1.5))
    return computepay

p = computepay(h,r)

print p

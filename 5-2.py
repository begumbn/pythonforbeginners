# prints minimum and maximum numbers entered and stops when done is entered

largest = None
smallest = None

while True:
    num = raw_input("Please enter a number here: ")
    if num == "done" : break

    try:
        num = int(num)    
    except:
        print 'Invalid input'
        continue

    if largest is None:
        largest = num
    elif largest < num:
        largest = num
    
    if smallest is None:
        smallest = num
    elif smallest > num:
        smallest = num
        
print 'Maximum is', largest
print 'Minimum is', smallest

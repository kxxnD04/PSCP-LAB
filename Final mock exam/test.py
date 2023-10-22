x = str(input()).lower()
y = str(input()).lower()
if x == "iphone 15" :
    if y == "128 gb" :
        print ("32900")
    elif y == "256 gb" :
        print ("36900")
elif x == "iphone 15 plus" :
    if y == "128 gb" :
        print ("37900")
    elif y == "256 gb" :
        print ("41900")
elif x == "iphone 15 pro" :
    if y == "128 gb" :
        print ("41900")
    elif y == "256 gb" :
        print ("45900")
elif x == "iphone 15 pro max" :
    if y == "256 gb" :
        print ("48900")
else :
    print ("Not Sell")
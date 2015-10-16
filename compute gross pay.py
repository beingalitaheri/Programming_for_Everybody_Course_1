#user input
try:
    hrs = raw_input("Enter Hours:")
    h = float(hrs)

    rat = raw_input("Enter Rate:")
    r = float(rat)
    
except:
    print "Error, Please enter numeric input"
    quit()
    
    
#compute gross pay
if h <= 40 :
    pay = h * r
    
else:
    pay = (40 * r) + (r * 1.5 * (h - 40))

print pay
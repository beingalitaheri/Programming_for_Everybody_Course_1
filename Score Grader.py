try:
    score = raw_input("Enter Score:")
    s = float(score)
    
except:
    print "Error, Please enter numeric input"
    quit()
    
   
if s >= 0.9 :
    print "A"
    
elif s >= 0.8 :
    print "B"
    
elif s >= 0.7 :
    print "C"

elif s >= 0.6 :
    print "D"
    
else:
    print "F"
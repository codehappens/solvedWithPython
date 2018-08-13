
n=0
for i in range(500, 45789):
    n=n+1
print n

print 45789-500

print 500+45789
print 501+45788
print 502+45787

print bin(46289)
print bin(500|45789)



def findVals(a,b):
    n=b-a
    print n
    b=bin(a|b)
    print b

s=0
for i in range(2,4):
    s=i|s

print bin(s)
    

    

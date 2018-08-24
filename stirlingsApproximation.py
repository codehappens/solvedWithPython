#http://mathworld.wolfram.com/StirlingsApproximation.html
#StirlingsApproximation for factorial

import math

    
def nFact(n):
    
	x=((2*n)+(1.0/3))*math.pi
    
    
	return round(math.sqrt(x)*(n**n)*(math.e**(-n)))
    
	

print nFact(100)
#Binets formulah fibonacci
#to find the nth fibonacci number
#http://mathworld.wolfram.com/BinetsFibonacciNumberFormula.html
#http://www.maths.surrey.ac.uk/hosted-sites/R.Knott/Fibonacci/fibGen.html#CALC3


def binet(n):
	s5=2.236 # square root of 5 rouded
	phi=(1+s5)**n/2**n
	nphi=(1-s5)**n/2**n
   	fn=int(round((phi - nphi)/s5))
	return fn

binet(7)
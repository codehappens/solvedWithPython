def square(n):

	#base case

	if (n==0):
        
	return 0
    
	#get rid of negative n

	if (n < 0):

	n = -n

	x = n>>1
 #divide by 2 
	if (n&1): #n is odd

		return ((square(x)<<2) + (x<<2) + 1)

	else: #n is even

		return (square(x)<<2)




print square(3)
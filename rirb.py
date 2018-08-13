#https://www.hackerrank.com/challenges/rirb/editorial
#
a=2
b=4

def count(a,b):
    c=b+1-a
    return c

def bitlength(n):
    """length of biary representation of n"""
    #return n.bit_length()
    return len(bin(n))-2

def bitcount(n):
    """number of 1s in the binary representation of n"""
    return bin(n).count("1")

def bitsum(n):
    s=0.0
    for k in range(n):
        s=bitcount(k)+s
    return s

def S(n):
    s=0.0
    for k in range(n):
        s=((2**(k-1))/(k+1))+s
    return s
        
BA=bitsum(a)
BB=bitsum(b+1)

LA=bitlength(a)
LB=bitlength(b+1)

FA=S(LA)+(BA/LA)
FB=S(LB)+(BB/LB)

C=count(a,b)
ans1=(FB-FA)/C

ans2=(BB-BA)/C

#0.61111 1.33333
print ans1
print ans2


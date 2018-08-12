#trying to solve this in python
#My solution is too slow this is just my first crack at it
#Needs to have a faster solution, just not sure what yet.
#https://www.hackerrank.com/challenges/rirb/problem

# Enter your code here. Read input from STDIN. Print output to STDOUT

def findVals(a,b):
    n=0
    li=[]
    li2=[]
    for i in range(a,b+1):
        onesCount=bin(i).count("1")
        totalLength=(float(len(bin(i)))-2)
        li.append(onesCount)
        li2.append(onesCount/totalLength)
        n=n+1
    nl = [i/float(n) for i in li]
    n2 = [i/float(n) for i in li2]
    x= sum(nl)
    y= sum(n2)
    z='%.5f %.5f'%(y,x)
    return z
        

n = int(raw_input())
for i in range(n):
    arr = map(int, raw_input().split())
    print findVals(arr[0],arr[1])
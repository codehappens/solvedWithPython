#https://www.hackerrank.com/challenges/extra-long-factorials/problem

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the extraLongFactorials function below.
def extraLongFactorials(n):
    arr=[0]*200
    carry=0
    l=str(n)[::-1] #reversing to put into the array backwards
    sl=len(l)
    for i in range(sl):
        arr[i]=int(l[i])
    #print(arr)
    
    #addme=10000
    #carry=addme
    #for i in range(200): 
    #    t=(arr[i]+carry)%10
    #    t2=int((arr[i]+carry)/10)
    #    arr[i]=t
    #    carry=t2
    
    #multme=8
    #carry=0
    #for i in range(200):
    #    t=(arr[i]*multme+carry)%10
    #    t2=int((arr[i]*multme+carry)/10)
    #    arr[i]=t
    #    carry=t2
    #print(arr)
    
    for j in range(1,n):
        carry=0
        for i in range(200):
            t=(arr[i]*j+carry)%10
            t2=int((arr[i]*j+carry)/10)
            arr[i]=t
            carry=t2
    #print(arr)
    arr.reverse()
    #print(arr)
    x=''.join(map(str, arr))
    x=x.lstrip("0")
    print(x)
    

if __name__ == '__main__':
    n = int(input())

    extraLongFactorials(n)

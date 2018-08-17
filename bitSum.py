#!/bin/python
#https://www.hackerrank.com/challenges/summing-the-n-series/problem

from __future__ import print_function

import os
import sys

#
# Complete the summingSeries function below.
#


def summingSeries(n):
    #
    # Write your code here.
    #
    n=n%1000000007
    if n==1:
        return 1
    m=int(n/2)
    nevenOrodd=n%2
    z=((n<<1)-1)
    #print(z)
    if nevenOrodd==0: #even
        ans=(z+1)*m
    else: #odd
        ans=(z+1)*m + ((m+1)<<1)-1
    return ans%1000000007
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(raw_input())

    for t_itr in xrange(t):
        n = int(raw_input())

        result = summingSeries(n)

        fptr.write(str(result) + '\n')

    fptr.close()

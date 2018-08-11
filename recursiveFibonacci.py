Recursive Fibonacci problem from Hackerrank
The problem specifically asked to do this
recusrively. 
https://www.hackerrank.com/challenges/ctci-fibonacci-numbers/problem


def fibonacci(n):
    if n == 0:
        return 0
    if n ==1:
        return 1
    if n>1:
        return fibonacci(n-1)+fibonacci(n-2)
    
   
n = int(raw_input())
print(fibonacci(n))
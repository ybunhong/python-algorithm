import sys

sys.setrecursionlimit(10**5)
print(sys.getrecursionlimit())

def factorial(N):
    if N == 0:
        return 1
    else:
        return N * factorial(N-1)
 
print(factorial(int(1000)))



def primeDetection(n):
    nsqrt = int(n**0.5)
    if n <= 1:
        return False
    for i in range(2, nsqrt+1):
        if n % i == 0:
            return False
    return True


def palindromeDetection(n):
    r, m = 0, n
    while m > 0:
        r *= 10
        r += m % 10
        m //= 10
    return n == r


def solve(n, m):
    ctn = 0
    for i in range(n, m+1):
        if primeDetection(i) and palindromeDetection(i):
            ctn += 1
    return ctn


print(solve(1, 1000000))

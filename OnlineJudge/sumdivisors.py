import math as m


def sumDivisor(N):
    ctn = 0
    sqrtN = int(N**0.5)
    for i in range(1, sqrtN+1):
        if N % i == 0:
            ctn += i

            if i != (m.floor(N / i)):
                ctn += (m.floor(N / i))
    return ctn


print(sumDivisor(1234567890))

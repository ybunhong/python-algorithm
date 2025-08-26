def primeFactorization(n):
    sqrtN = int(n**0.5)
    if n <= 1:
        return []
    for i in range(2, sqrtN+1):
        if n % i == 0:
            return [i] + primeFactorization(n//i)
    return [n]


def solve(n):
    factors = primeFactorization(n)
    return (" ").join(map(str, factors))


print(solve(100000300))

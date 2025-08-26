def find_prime(n):
    sieve = [0, 0] + [1] * (n-1)
    for i in range(2, n+1):
        if sieve[i] == 1:
            for j in range(i*i, n+1, i):
                sieve[j] = 0
    return sieve


def solve(n):
    sieve = find_prime(n)
    return sum(sieve)


print(solve(1000000))

# ort yol te

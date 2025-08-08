def findPrimeNum(n):
    primes = []
    for num in range(n+1):
        is_prime = True  # Assume the number is prime until proven otherwise
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:  # If num is divisible by i
                is_prime = False  # num is not prime
                break
        if is_prime:
            primes.append(num)
    return primes


def TwinPrime(n):
    primelst = findPrimeNum(n)
    cnt = 0
    for i in range(len(primelst)-1):
        # Check if the current prime and the next prime differ by exactly 2
        if primelst[i+1] - primelst[i] == 2:
            print(primelst[i], primelst[i+1])
            cnt += 1

    print(cnt)


print(TwinPrime(10))

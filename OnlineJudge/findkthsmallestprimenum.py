def findPrimeNum(start, end):
    primes = []
    for num in range(start, end + 1):
        is_prime = True  # Assume the number is prime until proven otherwise
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:  # If num is divisible by i
                is_prime = False  # num is not prime
                break
        if is_prime:
            primes.append(num)
    return primes


def findkthsmallestprimenumber(A, B, K):
    kth = findPrimeNum(A, B)
    print(f"{kth[0]}{kth[-1]}")
    try:
        if kth[K]:
            return kth[K]
    except IndexError:
        return -1


print(findkthsmallestprimenumber(1, 10, 3))

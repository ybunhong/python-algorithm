def primeNum(N):
    sqrtN= int(N**0.5)
    if N <=1:
        return ("Nor prime or compisite number")
    for i in range(2,sqrtN):
        if N % i ==0:
            return ("No")
    return ("Yes")

print(primeNum(1239130933))
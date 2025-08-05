# def primenum(n):
#     sqrtn=int(n**0.5)
#     if n <= 1:
#         return False
    
#     for i in range(2, sqrtn + 1):
#         if n % i ==0:
#             return False
        
#     return True

# def find5MaxPrime(N,M):
#     lst=[]
#     while M>=N and len(lst)<5:
#         if primenum(M):
#             lst.append(M)
#         M-=1
    
#     return (lst)
    
        
# print(find5MaxPrime(2147483647,4294967295))
def primenum(n):
    sqrtn=int(n**0.5)
    if n <= 1:
        return False
    
    for i in range(2, sqrtn + 1):
        if n % i ==0:
            return False
        
    return True

def find5MaxPrime():
    N= 2147483647 
    M= 4294967295
    lst= [ ]
    while M >= N and len(lst) < 5:
        if primenum(M):
            lst.append(M)
        M-=1
    return " ".join(str(i) for i in lst)

# prime_count = 0
#     for i in range(m, n - 1, -1):
#         if isPrime(i) == True:
#             print(i, end = ' ')
#             prime_count += 1

#         if prime_count == 5:
#             break
        

print(find5MaxPrime())
    
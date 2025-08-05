# def sumDivisor(N):
#     ctn=0
#     sqrtN= int(N**0.5)
#     for i in range(1,sqrtN+1):
#         if N % i ==0:
#             ctn+= i
            
#             if i !=N //i:
#                 ctn +=N//i
#     return ctn

# print(sumDivisor(1234567890)) 
# import math as m
# print(m.floor(10/3))
# print(m.floor(10002/3))
# print(m.floor(231/3))
# print(m.floor(3141/3))

# print(10//3)
# print(10002//3)
# print(231//3)
# print(3141//3)

# import math as m
# def sumDivisor(N):
#     ctn=0
#     sqrtN= int(N**0.5)
#     for i in range(1,sqrtN+1):
#         if N % i ==0:
#             ctn+= i
            
#             if i !=(m.floor(N / i)):
#                 ctn +=(m.floor(N / i))
#     return ctn
    
# print(sumDivisor(1234567890)) 

import math as m

def sumDivisor(N):
    ctn=0
    sqrtN= int(N**0.5)
    for i in range(1,sqrtN+1):
        if N % i ==0:
            ctn+= i
            
            if i !=(m.floor(N / i)):
                ctn +=(m.floor(N / i))
    return ctn
print(sumDivisor(1234567890)) 
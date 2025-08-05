# def solve(N):
#     ctn = 0
#     for i in range(1,N+1):
#         if N % i== 0:
#             ctn+=1
#     return ctn

def solve(N):
    ctn=0
    sqrtn= int(N**0.5)
    for i in range(1, sqrtn + 1):
        if N % i ==0:
            ctn+=2
    
    if sqrtn*sqrtn== N :
        ctn-=1
    return ctn


N=int(input())

import time
start = time.time()
print(solve(N))
end= time.time()

print(f"solve() elapsed time: {end - start}")

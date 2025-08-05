def sumAll(N,M):
    G= len(range(N,M+1))
    return G *(N+M)//2

N,M=list(map(int,input().split()))
print(sumAll(N,M))
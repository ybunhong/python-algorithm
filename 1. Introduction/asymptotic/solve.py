# def solve(maxn, maxi)
def solve(N,S):
    maxn = S[0]
    maxi = 0
    for i in range(1,N):
        if maxn < S[i]:
            maxn = S[i]
            maxi = i
            
    return maxn, maxi

#maxi is index holder

N= int(input())
S= list(map(int, input().split()))
print(solve(N,S))
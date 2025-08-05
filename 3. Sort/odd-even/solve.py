def solve(n,s):
    odd,even= [],[]
    for i in range(n):
        if s[i] % 2 ==0:
            even.append(s[i])
        else:
            odd.append(s[i])
            
    odd.sort()
    even.sort(reverse =True)
            
    print("odd:"," ".join(map(str, odd)))
    print("even:"," ".join(map(str, even)))
    
n=int(input())
s=list(map(int, input().split()))

solve(n,s)
def perm(n, r):
    if n == r:
        return 1
    result = 1
    for i in range(r):
        result *= (n - i)
    return result


n, r = map(int, input().split())
print(perm(n, r))

def fibonaci(n, memo={}):
    # If value already computed, return it directly
    if n in memo:
        return memo[n]
    if n == 1 or n == 2:
        return 1
    # Store the result in memo to avoid recomputing
    memo[n] = fibonaci(n-1, memo) + fibonaci(n-2, memo)
    return memo[n]

n = int(input())
print(fibonaci(n))

def fibonaci(n):
    if n == 1 or n == 2:
        return 1
    a, b = 1, 1
    for _ in range(3, n + 1):
        a, b = b, a + b
    return b

n = 10000
print(fibonaci(n))

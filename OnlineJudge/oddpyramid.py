def pyramidSum(N):
    total_numbers = N * (N + 1) // 2
    return total_numbers ** 2


N = int(input())
print(pyramidSum(N))

def bubblesort(n, s):
    cnt = 0                  # Count of swaps
    for i in range(n-1):     # Outer loop runs n-1 times
        for j in range(n-1-i):       # Inner loop, shrinking each time
            if s[j] > s[j+1]:        # Compare adjacent elements
                s[j], s[j+1] = s[j+1], s[j]  # Swap if out of order
                cnt += 1             # Record the swap
    return cnt


n = int(input())
s = list(map(int, input().split()))
print(bubblesort(n, s))

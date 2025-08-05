def perm(i, n, s):
    if i == n - 1:
        print("".join(s))
    else:
        for j in range(i, n):
            s[i], s[j] = s[j], s[i]  # swap
            perm(i + 1, n, s)        # recurse
            s[i], s[j] = s[j], s[i]  # backtrack

N = int(input())  # e.g. input 3
S = [chr(ord('A') + i) for i in range(N)]
print(0, N, S)

# Add this to generate the permutations:
perm(0, N, S)

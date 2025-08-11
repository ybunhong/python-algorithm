def findIndexElement(n, m, S, X):
    for i in range(m):                          # Loop over each element in X
        print(seqsearch(X[i], n, S), end=" ")   # Print index or -1
    print()


def seqsearch(x, n, S):
    for i in range(n):   # Linear search in S
        if x == S[i]:
            return i     # Return index if found (0-based)
    return -1            # Return -1 if not found


N, M = map(int, input().split())
S = list(map(int, input().split()))
X = list(map(int, input().split()))

findIndexElement(N, M, S, X)

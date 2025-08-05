def solve(n, tups):
    tups.sort(key=lambda x: (x[0], -x[-1]))
    for i in range(n):
        print("coordinate:", " ".join(map(str, tups[i])))


n = int(input())
tups = []

for i in range(n):
    x, y = map(int, input().split())
    tups.append((x, y))

solve(n, tups)

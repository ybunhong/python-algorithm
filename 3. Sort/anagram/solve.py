def solve(n):
    anagrams = set([])
    for i in range(n):
        word1 = input()
        word2 = "".join(sorted(word1))
        if word2 not in anagrams:
            print(word1)
            anagrams.add(word2)


N = int(input())
solve(N)

# doesn't work as i expected

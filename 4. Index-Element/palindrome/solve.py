# not passing bigO notation

# def palindromeNum(start, end):
#     rangenum = list(range(start, end+1))
#     cnt = 0
#     for i in rangenum:
#         s = str(i)
#         if s == s[::-1]:
#             cnt += 1
#     return cnt


# print(palindromeNum(10, 100000000000))

def is_palindrome(n):
    s = str(n)
    return s == s[::-1]


def solve(n, m=None):
    if m is None:
        if is_palindrome(n):
            return "yes"
        else:
            return "no"
    else:
        cnt = 0
        for i in range(n, m + 1):
            if is_palindrome(i):
                cnt += 1
        return cnt


n = input("Enter a word or two numbers separated by space: ").split()

if len(n) == 1:
    print(solve(n[0]))
elif len(n) == 2:
    print(solve(int(n[0]), int(n[1])))

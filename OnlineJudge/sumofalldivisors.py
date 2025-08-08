import math as m
import re


def sumDivisor(N):
    # This assumes we already counted 1 and n (the two trivial divisors). # So the loop only needs to find divisors strictly between 2 and n-1.
    total = N + 1
    sqrtN = int(N**0.5)
    for i in range(2, sqrtN+1):
        if N % i == 0:
            total += i

            if i != (N // i):
                total += (N // i)
    return total

# Extract the first number from the given string, convert it to integer, and store in n
# \d mean match a digit (0–9)
# + mean match one or more of them in a row.
# "Enter a number: 20" is the text we’re scanning. this searches the string and finds the first number "20".


# The search() function returns a match object
# .group() extracts the matched text as a string.
n = int(re.search(r'\d+', "Enter a number: 20").group())
if (2 <= n <= 20):
    print("Sum of divisors:", sumDivisor(n))


# If you put "Enter a number: 21",
# 2 <= 21 <= 20 is False, so nothing will print.

def insertionsort(n, s):
    cnt = 0

    for i in range(1, n):
        j = i - 1           # Index for comparing with previous elements
        val = s[i]          # The value we want to insert into the sorted part
        cnt += 1            # Count picking this element (or a comparison)

        # Shift elements in the sorted part to the right until correct position is found
        while j >= 0 and s[j] > val:
            s[j + 1] = s[j]  # Move element one step to the right
            j -= 1          # Move to the previous index
            cnt += 1        # Count the shift operation

        # Insert the element in the correct position
        s[j + 1] = val

    return cnt


n = int(input())
s = list(map(int, input().split(" ")))
print(insertionsort(n, s))

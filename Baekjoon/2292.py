import sys

n = int(sys.stdin.readline())
lst = [1]
i = 0
sums = 0

# f[i] = f[1] + 6 * (1 + 2 + 3 + . . + i-1)
if n == 1:
    print(1)
else:
    while 1:
        sums += i
        k = lst[0] + 6 * sums
        lst.append(k)
        if k == n:
            lst.pop()
        elif k > n:
            break
        i += 1
    print(len(lst)-1)


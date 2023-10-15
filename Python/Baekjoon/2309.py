# 일곱 난쟁이의 키의 합은 100

lst = []
for _ in range(9):
    lst.append(int(input()))

total = sum(lst)

for i in range(len(lst)-1):
    s = 0
    for j in range(i+1, len(lst)):
        if total - lst[i] - lst[j] == 100:
            s = (i, j)
            break
    if s != 0:
        break

lst.pop(s[1])
lst.pop(s[0])

lst.sort()
for i in lst:
    print(i)
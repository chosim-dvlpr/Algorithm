n, k = map(int, input().split())
lst = list(map(int, range(1, n+1)))
res = []
i = 0
cnt = 1

while lst:  # lst가 비어있게 되면 종료
    if i == len(lst):
        i = 0
    if cnt == k:
        res.append(lst.pop(i))
        cnt = 1
        continue
    cnt += 1
    i += 1

print('<', end='')
for i in res:
    print(i, end='')
    if i != res[-1]:
        print(', ', end='')
print('>')
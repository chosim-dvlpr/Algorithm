'''
나이가 증가하는 순으로,
먼저 가입한 사람이 먼저 오도록
'''
lst = []
for _ in range(int(input())):
    a, b = map(str, input().split())
    lst.append((int(a), b))
lst.sort(key=lambda x:x[0])
for i in lst:
    print(*i)
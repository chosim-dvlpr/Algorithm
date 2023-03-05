'''
m, n : 가로, 세로 길이
num : 상점의 개수
a, b : 북1 남2 서3 동4 + 왼쪽/위쪽 경계로부터의 거리
상점/최초 위치는 꼭짓점x
'''

def func(k, sq):    # 크기 비교
    if k > sq/2:
        return sq - k
    else:
        return k


m, n = map(int, input().split())
num = int(input())
lst = []
length = []

for _ in range(num):
    a, b = map(int, input().split())
    lst.append((a, b))

x, y = map(int, input().split())    # 최초 위치
sq = 2 * (n+m)  # 둘레의 길이

if x == 1:      # 최초 위치가 북쪽일때
    for a, b in lst:
        if a == 1:  # 북쪽
            length.append(abs(b-y))
        elif a == 2:    # 남쪽
            k = y + n + b
            length.append(func(k, sq))
        elif a == 3:    # 서쪽
            k = y + b
            length.append(func(k, sq))
        elif a == 4:    # 동쪽
            k = (m - y) + b
            length.append(func(k, sq))
elif x == 2:    # 최초 위치가 남쪽일 때
    for a, b in lst:
        if a == 1:  # 북쪽
            k = y + n + b
            length.append(func(k, sq))
        elif a == 2:    # 남쪽
            length.append(abs(b - y))
        elif a == 3:    # 서쪽
            k = y + (n-b)
            length.append(func(k, sq))
        elif a == 4:    # 동쪽
            k = (m - y) + (n - b)
            length.append(func(k, sq))
elif x == 3:    # 최초 위치가 서쪽일 때
    for a, b in lst:
        if a == 1:  # 북쪽
            k = y + b
            length.append(func(k, sq))
        elif a == 2:    # 남쪽
            k = (n - y) + b
            length.append(func(k, sq))
        elif a == 3:    # 서쪽
            length.append(abs(y - b))
        elif a == 4:    # 동쪽
            k = y + m + b
            length.append(func(k, sq))
elif x == 4:    # 최초 위치가 동쪽일 때
    for a, b in lst:
        if a == 1:  # 북쪽
            k = (m - b) + y
            length.append(func(k, sq))
        elif a == 2:    # 남쪽
            k = (m - b) + (n - y)
            length.append(func(k, sq))
        elif a == 3:    # 서쪽
            k = m + b + y
            length.append(func(k, sq))
        elif a == 4:    # 동쪽
            length.append(abs(y - b))

print(sum(length))


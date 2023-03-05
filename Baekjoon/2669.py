'''
직사각형의 좌표 : 왼하 (x, y), 우상 (x, y)
네 개의 직사각형이 차지하는 면적 출력 (중복 = 1로 계산)
좌표는 1 이상 100 이하
'''

arr = [[0] * 101 for _ in range(101)]
for _ in range(4):
    a, b, c, d = map(int, input().split())
    if c > a:
        m = 1
    else:
        m = -1
    if d > b:
        n = 1
    else:
        n = -1
    for i in range(a, c, m):
        for j in range(b, d, n):
            arr[i][j] += 1
cnt = 0
for i in range(len(arr)):
    for j in range(len(arr)):
        if arr[i][j] > 0:
            cnt += 1
print(cnt)
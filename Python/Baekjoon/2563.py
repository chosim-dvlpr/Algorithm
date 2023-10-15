'''
겹치는 부분을 포함해서, (중복 제외) 총 넓이를 구하시오
n : 색종이의 수
lst : 색종이를 붙인 위치 (색종이 왼쪽변과 도화지 왼쪽변사이의 거리(x), y)
= 사각형의 왼쪽 아래 점의 위치
색종이의 크기 : 10 * 10
'''

n = int(input())
arr = [[0]*100 for _ in range(100)]
lst = []

for _ in range(n):
    x, y = map(int, input().split())
    lst.append((x, y))

cnt = 0
for x, y in lst:
    for i in range(x-1, x-1+10):
        for j in range(y-1, y-1+10):
            arr[i][j] += 1
            cnt += 1
            if arr[i][j] > 1:
                cnt -= 1
print(cnt)
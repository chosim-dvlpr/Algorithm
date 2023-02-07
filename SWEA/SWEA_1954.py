import sys
sys.stdin = open("input.txt", "r")

'''
# ci : 현재 i
# cj : 현재 j
right = arr[ci + di[0]][cj + dj[0]]
down = arr[ci + di[1]][cj + dj[1]]
left = arr[ci + di[2]][cj + dj[2]]
up = arr[ci + di[3]][cj + dj[3]]

(ci, cj) = (1,1) ~ (1,5)
1,6 == 1이면 방향 바꿈 (di[0], dj[0]) - 아래쪽으로
(ci, cj) = (2,5) ~ (5,5)
(6,5) == 이면 방향 바꿈 (di[1], dj[1]) - 왼쪽으로
'''

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [[0]*N for _ in range(N)]

    # 1로 둘러싸인 arr 배열 만듦
    for i in range(N+2):
        if i == 0:
            arr = [[-1] * (N+2)] + arr
        elif i == N+1:
            arr = arr + [[-1] * (N + 2)]
        else:
            arr[i] = [-1] + arr[i] + [-1]

    # 오른쪽 -> 아래 -> 왼쪽 -> 위쪽
    # i : 세로
    # j : 가로
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]

    aa = True
    while aa == True:
        k = 0
        if N == 1:
            arr[1][1] = 1
        else:
            ci = 1
            cj = 1

            for i in range(1, (N+2)**2+1):
                if arr[ci][cj] != 0:
                    ci -= di[k]
                    cj -= dj[k]
                    k = (k + 1) % 4
                    ci += di[k]
                    cj += dj[k]
                if arr[ci][cj] == 0:
                    arr[ci][cj] = i
                    ci += di[k]
                    cj += dj[k]
                else:
                    aa = False
        break
    print(f'#{tc}')
    for i in range(1, len(arr)-1):
        print(*arr[i][1:-1])




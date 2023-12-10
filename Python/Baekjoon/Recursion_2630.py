# 종이를 반으로 자르는 것을 반복
# 모두 같은 색으로 칠해져 있거나 한 칸이 되어 더 이상 자를 수 없게 되면 종료

import sys
input = sys.stdin.readline

# 0 : 하얀색
# 1 : 파란색
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
white = 0
blue = 0
def recursion(start, end):
    global white, blue
    length = end[0] - start[0] + 1

    if length <= 1:
        if arr[start[0]][start[1]] == 1:
            blue += 1
            return
        white += 1
        return

    color = arr[start[0]][start[1]]
    for i in range(start[0], end[0]+1):
        for j in range(start[1], end[1]+1):
            # 색이 다른 부분이 있다면 종이를 4등분하여 재귀
            if arr[i][j] != color:
                recursion((start[0], start[1]), (start[0]+length//2-1, start[1]+length//2-1))
                recursion((start[0], start[1]+length//2), (start[0]+length//2-1, start[1]+length-1))
                recursion((start[0]+length//2, start[1]), (start[0]+length-1, start[1]+length//2-1))
                recursion((start[0]+length//2, start[1]+length//2), (start[0]+length-1, start[1]+length-1))
                return
    if arr[start[0]][start[1]] == 1:
        blue += 1
        return
    white += 1

recursion((0, 0), (n-1, n-1))
print(white)
print(blue)

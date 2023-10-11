# n*n인 체스판 위에 퀸 n개를 서로 공격할 수 없도록 놓기
# n이 주어졌을 때, 퀸을 놓는 방법의 수를 구하기
# 모든 대각선 방향에는 퀸이 없어야 함

n = int(input())
row = [0] * n # row[i] = j 표시하기 위함
ans = 0

def is_promising(x):
  for i in range(x): # 0부터 x-1까지
    # 대칭 방향에 퀸이 놓여있는 경우는 제외
    # 대각선 위치에 퀸이 놓여있는 경우는 제외
    if row[x] == row[i] or abs(row[x] - row[i]) == abs(x - i):
      return False
  
  return True

def n_queen(x):
  global ans
  if x == n: # row가 마지막 인덱스를 넘었을 때
    ans += 1 # is_promising()함수의 종료 없이 마지막까지 종료되었음을 의미
    return

  else:
    for y in range(n):
      row[x] = y # [x, y] 위치에 퀸을 놓음
      if is_promising(x):
        n_queen(x+1)

n_queen(0)
print(ans)


# arr = [[0]*n for _ in range(n)]
# delta = [(-1, 0), (1, 0), (-1, -1), (0, -1), (1, -1), (-1, 1), (0, 1), (1, 1)]
# res = 0

# def bt(row, col, cnt):
#   global res
#   # print("cnt : ", cnt)

#   if cnt == n:
#     print(cnt)
#     return
  
#   for i in range(row, n):
#     for j in range(col, n):
#       for d in delta:
#         # print(i, j, d)
#         nx, ny = i+d[0], j+d[1]
#         if 0 <= nx and nx < n and 0 <= ny and ny < n :
#           # print("여기")
#           if arr[nx][ny] == 0:
#             arr[i][j] = 1 # queen의 위치
#             res += 1
#             bt(i+1, j+1, cnt+1)
#             res -= 1
#           else:
#             arr[i][j] = 0
#             break


# bt(0, 0, 0)
# print(arr)

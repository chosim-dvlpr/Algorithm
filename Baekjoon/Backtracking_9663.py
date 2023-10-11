# n*n인 체스판 위에 퀸 n개를 서로 공격할 수 없도록 놓기
# n이 주어졌을 때, 퀸을 놓는 방법의 수를 구하기

n = int(input())
arr = [[0]*n for _ in range(n)]
delta = [(-1, 0), (1, 0), (-1, -1), (0, -1), (1, -1), (-1, 1), (0, 1), (1, 1)]
res = 0

def bt(row, col, cnt):
  global res
  # print("cnt : ", cnt)

  if cnt == n:
    print(cnt)
    return
  
  for i in range(row, n):
    for j in range(col, n):
      for d in delta:
        # print(i, j, d)
        nx, ny = i+d[0], j+d[1]
        if 0 <= nx and nx < n and 0 <= ny and ny < n :
          # print("여기")
          if arr[nx][ny] == 0:
            arr[i][j] = 1 # queen의 위치
            res += 1
            bt(i+1, j+1, cnt+1)
            res -= 1
          else:
            arr[i][j] = 0
            break


bt(0, 0, 0)
# print(arr)

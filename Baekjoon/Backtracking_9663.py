# n*n인 체스판 위에 퀸 n개를 서로 공격할 수 없도록 놓기
# n이 주어졌을 때, 퀸을 놓는 방법의 수를 구하기

n = int(input())
arr = [[0]*n for _ in range(n)]
delta = [(-1, 0), (1, 0), (-1, -1), (0, -1), (1, -1), (-1, 1), (0, 1), (1, 1)]
cnt = 0

def bt():
  for i in range(n):
    for j in range(n):
      arr[i][j] = 1 # queen의 위치
      for d in delta:
        nx, ny = i+d[0], j+d[1]
        if 0 <= nx and nx < n and 0 <= ny and ny < n and arr[nx][ny] == 1:
          arr[i][j] = 0
          break


bt()
print(arr)
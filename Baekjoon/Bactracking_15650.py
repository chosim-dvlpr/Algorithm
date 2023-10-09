# 고른 수열은 오름차순이어야 함
# 중복되는 수열은 제거

n, m = map(int, input().split())
lst = [_ for _ in range(1, n+1)]
visited = [0] * (n+1)
res = [[]]

def bt(idx, visited):
  global res
  print(res)
  if idx == m:
    print(res)
    # print(*r for r in res)

  for i in range(1, n+1):
    if not visited[i]:
      visited[i] = 1
      res[-1].append([i])
      bt(idx+1, visited)
      res[-1].pop()
      visited[i] = 0
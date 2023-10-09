# 고른 수열은 오름차순이어야 함
# 중복되는 수열은 제거

n, m = map(int, input().split())
res = [] # 수열을 담을 리스트

def bt(idx):
  if len(res) == m:
    print(*res)
    return 
    
  for i in range(idx, n+1): # idx부터 순회
    if i not in res: # 아직 수열에 포함이 안되어있다면
      res.append(i)
      bt(i+1)        # 현재 값 다음부터 순회하도록 함 (중복 제거 위해)
      res.pop()

bt(1)

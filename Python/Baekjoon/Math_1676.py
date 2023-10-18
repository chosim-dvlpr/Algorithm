n = int(input())
res = 1

def pac(n):
  global res

  if n <= 1:
    return
  
  res *= n
  pac(n-1)

pac(n)
lst = list(map(str, str(res)))

# 인덱스 마지막부터 첫번째까지 순회
cnt = 0

for i in range(len(lst)-1, -1, -1):
  if lst[i] != '0':
    break
  cnt += 1

print(cnt)